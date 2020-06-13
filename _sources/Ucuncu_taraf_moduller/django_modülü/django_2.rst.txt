.. meta::
   :description: Bu bölümde django API'ını öğreneceğiz.
   :keywords: python, django, çeviri
   
.. highlight:: python3

*********************************
İLK DJANGO PROJENİ YAZ, part 2
*********************************

Veritabanı Kurulumu
********************

Şimdi **mysite/settings.py** dosyasını açın. Önce TIME_ZONE 
değerini `Europe/Istanbul`  yaparak İstanbul'a ayarlayın.

.. Note:: Dosyanın en başındaki INSTALLED_APPS ayarına dikkat edin.
         Projenizde kullandığınız uygulamaları tutar. Yeni bir uygulama 
         kullanacağınız zaman bu listeye eklemelisiniz. 

Varsayılan olarak gelen uygulamalar şunlardır::

    django.contrib.admin --> Yönetici panelini oluşturur.
    django.contrib.auth --> Bir kimlik doğrulama sistemi.
    django.contrib.contenttypes --> İçerik türleri için bir framework.
    django.contrib.sessions --> Bir oturum frameworku
    django.contrib.messages --> Bir mesajlaşma frameworku
    django.contrib.staticfiles --> Statik dosyaları yönetmek için bir framework.

Bu uygulamalardan bazıları en az bir veritabanı kullanıyor. 
Ancak bu veritabanlarının kullanılabilmesi için bir 
tablo oluşturmalıyız. O tablo da şu komutla oluşuyor::

    python manage.py migrate

Model oluşturalım
******************

Şimdi modellerimizi tanımlayacağız.
Anket uygulamamızda iki tane model olacak: Question(Soru), Choice(Seçenek). 
Question modeli bir soru ve yayınlama tarihi içerecek. Choice modeli ise iki alandan 
oluşacak: Bir yazı alanı ve oy çetelesi. Her Choice bir Question ile ilişkili olacak.
Şimdi **polls/models.py** dosyasını şu şekilde düzenleyin::

    from django.db import models


    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')


    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

Burada iki model oluşturduk. Bu modeller django.db.models.Model 
sınıfını miras alıyor ve veritabanı alanını temsil eden 
değişkenlere sahip. Bu veritabanı alanlarının her biri bir 
Field sınıfı ile ilişkili. Mesela CharField karakter 
dizilerini , DateTimeField tarih ve zamanı veritabanına 
eklemek için. Bu sistem Django'nun, her alanın hangi veri 
tipini tuttuğunu anlamasını sağlar. Bazı Field sınıfları 
zorunlu olarak parametreye ihtiyaç duyuyor. Buna en iyi 
örnek olan CharField sınıfı max_length değeri olmadan 
çalışmıyor.Field sınıfları isteğe bağlı parametrelere de 
sahip.Mesela votes değerinin default parametresi-ki biz 
bu örnekte 0 olarak ayarladık-buna bir örnek.Son olarak 
ForeignKey kullanarak  her Choice  örneğini bir Question 
örneği ile ilişkilendirdik.

Modellerin Aktifleştirilmesi
****************************

Model kodları Django'ya bazı bilgiler verir. 
Django bu bilgilerle şunları yapabilir:

    #. Uygulama için bir veritabanı şeması oluşturmak. 
    #. Question ve Choice nesneleri için bir veritabanı erişim API'ı oluşturmak.

Fakat önce polls uygulamasını projeye yüklemeliyiz.
Projeye yüklemek için  **setting.py** dosyasını açıp 
INSTALLED_APPS  ayarını düzenlemeliyiz. Bu listeye 
**polls/apps.py** dosyasındaki PollsConfig sınıfını referans 
olarak ekleyelim. **setting.py** dosyasındaki INSTALLED_APPS 
son hali şöyle olmalı::

    INSTALLED_APPS = [
        'polls.apps.PollsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

Artık Django, polls isimli uygulamamızı projeye eklediğimizi biliyor. 
Şimdi farklı bir komutu çalıştıralım::

    python manage.py makemigrations polls

Talimatlara benzer şeyler görmelisiniz::

    Migrations for 'polls':
      polls/migrations/0001_initial.py:
        - Create model Choice
        - Create model Question
        - Add field question to choice

`makemigrations` komutu ile ürettiğimiz modellerde değişiklik 
yaptığımızı (Aynı zamanda yeni modeller ürettiğimizi de) ve 
değişikliklerin migration olarak depolanmasını istediğimizi 
söyledik. Migrationlar senin modellerindeki değişiklerin 
depolanma şeklidir(ve bu yüzden veritabanı şeması). 
İstersen yeni modelinin migrationını okuyabilirsin. 
Migration **polls/migrations/0001_inital.py** isimli dosyada. 
Endişelenmeyin, bu dosyayı her zaman okumak zorunda değilsiniz.  
"`migrate`" komutu, senin veritabanı 
şemanı otomatik olarak yönetmek için  migrationları çalıştırır.
Birazdan bu konuya tekrar geleceğiz. Ama önce migrationın çalıştırdığı 
SQL dosyasına bakalım. "`sqlmigrate`" komutuna migration adını 
parametre olarak verin ve SQL çıktısını alın::

    python manage.py sqlmigrate polls 0001

İngilizce yönerge tarzında bir şeyler görüyor olmalısın::

    BEGIN;
    --
    -- Create model Choice
    --
    CREATE TABLE "polls_choice" (
        "id" serial NOT NULL PRIMARY KEY,
        "choice_text" varchar(200) NOT NULL,
        "votes" integer NOT NULL
    );
    --
    -- Create model Question
    --
    CREATE TABLE "polls_question" (
        "id" serial NOT NULL PRIMARY KEY,
        "question_text" varchar(200) NOT NULL,
        "pub_date" timestamp with time zone NOT NULL
    );
    --
    -- Add field question to choice
    --
    ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
    ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
    CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
    ALTER TABLE "polls_choice"
    ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
        FOREIGN KEY ("question_id")
        REFERENCES "polls_question" ("id")
        DEFERRABLE INITIALLY DEFERRED;

    COMMIT;

Aşağıdakilere dikkat et:
    - Çıktı kullandığınız veritabanına göre değişir. 
      Yukarıdaki örnek PostgreSQL için yazılmıştır.
    - Tablo adı, uygulamanın adını ve modelin adını
      (küçük harflerle) kullanarak otomatik olarak oluşturulur .
      (Bu davranış geçersiz kılınabilir.)
    - Birincil anahtarlar(ID) otomatik olarak eklenir.
      (Bu da geçersiz kılınabilir.)
    - Düzenlenirken  Django, foreign key alanının adına "_id" 
      ekler.(Evet, bunu da geçersiz kılabilirsiniz.)
    - Kullandığınız veritabanına göre düzenlenmiştir. Bu yüzden 
      auto_increment(MySQL), serial(PostgreSQL) gibi veritabanına 
      özgü alan türleri otomatik olarak ayarlanır. Aynı şey alan 
      adlarının alıntılanması için de geçerlidir.
    - `sqlmigrate` komutu aslında veritabanındaki migrationları 
      çalıştırmaz. Sadece onları senin görebileceğin SQL kodları 
      halinde ekrana yazdırır.  Bu Djangonun yaptıklarını 
      kontrol etmek veya SQL kodlarını düzenlemek için kullanışlıdır.

Eğer bunu ilgi çekici bulduysan bir de şunu çalıştır:`python manage.py check`. 
Bu kod projende herhangi bir problem olup olmadığını veritabanıyla 
uğraşmadan kontrol eder. Şimdi `migrate` komutunu tekrar 
çalıştırıp modelleri veritabanında oluştur::

    python manage.py migrate

`migrate` komutu daha önce uygulanmayan tüm migrationları alır 
(Django, veritabanınızda django_migrations adlı özel bir tablo 
kullanarak hangi uygulamaların uygulandığını izler) ve bunları 
veritabanınıza karşı çalıştırır - temel olarak modelinize yaptığınız 
değişiklikleri veritabanındaki şema ile senkronize eder. 
Migrationlar çok güçlüdür ve zamanla, projenizi geliştirirken, veritabanınızı 
veya tablolarınızı silmenize ve yenilerini oluşturmanıza gerek kalmadan 
modellerinizi değiştirmenize izin verir - 
veri kaybetmeden veritabanınızı canlı hale getirme konusunda 
uzmanlaşmıştır. Eğiticinin daha sonraki bir bölümünde bunları 
daha ayrıntılı bir şekilde ele alacağız, ancak şimdilik, model 
değişikliklerini yapmak için üç adımlı kılavuzu hatırlayın:

    - Modeli değiştirin (**models.py** de)
    - `python manage.py makemigrations` komutunu çalıştırarak bu değişiklikler için  migration oluşturun.
    - `python manage.py migrate` komutunu çalıştırarak bu değişiklikleri veritabanına uygulayın.

API ile oynayalım
*****************

Şimdi etkileşimli kabuğa atlayıp Django'nun sunduğu API ile uğraşalım. 
Etkileşimli kabuğu çağırmak için şu komutu kullanın::

    python manage.py shell

Basitçe `python` yazmak yerine bunu kullanıyoruz. 
Çünkü manage.py dosyası kullanacağımız django dosyalarını içe aktarıyor.
Kabuğa girdikten sonra veritabanı API'ını keşfedin::


    >>> from polls.models import Choice, Question  # Az önce yazdığımız model sınıflarını içe aktar.
     
    #Henüz sistemde Question nesnesi yok.
    >>> Question.objects.all()
    <QuerySet []>
    
    # Yeni bir Question nesnesi oluştur.
    # Varsayılan ayarlar dosyasında saat dilimleri desteği etkinleştirilmiştir, bu nedenle
    # Django pub_date değişkeni için tzinfo ile bir tarih bekler. timezone.now()'ı kullanın.
    # datetime.datetime.now () yerine ve doğru olanı yapacağız.
    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())
    
    # Oluşturduğumuz nesneyi veritabanına kaydedelim. Bunun için save() metodunu kullanmalısın.
    >>> q.save()
    
    # Şimdi bir ID'ye sahip.
    >>> q.id
    1
    
    # Python ile model alan değerlerine erişin.
    >>> q.question_text
    "What's new?"
    >>> q.pub_date
    datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)
    
    # Öznitelikleri değiştirip save() metodunu çağıralım.
    >>> q.question_text = "What's up?"
    >>> q.save()
    
    # objects.all(), veritabanındaki tüm Questionları görüntüler.
    >>> Question.objects.all()
    <QuerySet [<Question: Question object (1)>]>

Bir dakika! <Question: Question object (1)> bu nesne 
ilişkisi hiç yararlı değil. Question modeline (**polls/models.py** dosyasında) 
__str__() metodunu ekleyelim(Choice modeline de)::

    from django.db import models
    
    class Question(models.Model):
        # ...
        def __str__(self):
            return self.question_text

    class Choice(models.Model):
        # ...
        def __str__(self):
            return self.choice_text


Modellerinize, yalnızca etkileşimli komut istemiyle 
çalışırken kendi rahatlığınız için değil, aynı zamanda nesnelerin 
temsillerinin Django’nun otomatik olarak oluşturulan yöneticisi 
boyunca kullanılmasından dolayı `__str__()` yöntemlerini eklemeniz 
önemlidir. Bunların normal Python yöntemleri olduğunu unutmayın. 
Bunu kanıtlamak için özel bir yöntem ekleyelim::

    #polls/models.py
    import datetime

    from django.db import models
    from django.utils import timezone
    
    
    class Question(models.Model):
        # ...
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

Python standart kütüphanesinden datetime modülünü ve Django'nun
saat dilimleri ile ilgili kütüphanesinden timezone modülünü içe 
aktaralım.

Bu yaptığımız değişiklikleri kaydetmek için şu komutla yeni bir 
kabuk açalım::
`python manage.py shell`
::

    >>> from polls.models import Choice, Question

    # Eklediğimiz __str__() fonksiyonunun çalıştığından emin olalım.
    >>> Question.objects.all()
    <QuerySet [<Question: What's up?>]>

    # Django'nun içinde veritabanı araması için zengin bir API var.
    >>> Question.objects.filter(id=1)
    <QuerySet [<Question: What's up?>]>
    >>> Question.objects.filter(question_text__startswith='What')
    <QuerySet [<Question: What's up?>]>

    # Bu yıl paylaşılan question nesnelerini bulalım.
    >>> from django.utils import timezone
    >>> current_year = timezone.now().year
    >>> Question.objects.get(pub_date__year=current_year)
    <Question: What's up?>

    # Veritabanında olmayan bir ID değerini parametre olarak verirseniz
    # size bir hata çıktısı verecektir.
    >>> Question.objects.get(id=2)
    Traceback (most recent call last):
        ...
    DoesNotExist: Question matching query does not exist.

    # Birincil anahtar aramalarda en çok kullanılan ifadedir, bundan dolayı
    # Django birincil anahtar aramaları için bir kısayola sahip.
    # Sonraki örnek şu kodla aynı :Question.objects.get(id=1).
    >>> Question.objects.get(pk=1)
    <Question: What's up?>

    # Yazdığımız metodun da çalıştığından emin olalım.
    >>> q = Question.objects.get(pk=1)
    >>> q.was_published_recently()
    True

    # Question nesnemize birkaç Choice nesnesi oluşturalım.
    >>> q = Question.objects.get(pk=1)

    # Bu Question nesnesine hiçbir Choice nesnesi bağlı değil(şimdilik)
    >>> q.choice_set.all()
    <QuerySet []>

    # 3 Choice nesnesi oluşturalım.
    >>> q.choice_set.create(choice_text='Not much', votes=0)
    <Choice: Not much>
    >>> q.choice_set.create(choice_text='The sky', votes=0)
    <Choice: The sky>
    >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

    # Choice nesnelerinin Question nesnelerine erişimi var.
    >>> c.question
    <Question: What's up?>

    # Ve tam tersi: Question nesnelerinin de Choice nesnelerine erişimi var.
    >>> q.choice_set.all()
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
    >>> q.choice_set.count()
    3

    # API, ihtiyaç duyduğunuz kadarıyla ilişkileri otomatik olarak takip eder.
    # İlişkileri ayırmak için çift alt çizgi kullanın.
    # Bu, istediğiniz kadar derin bir seviyede çalışır. Sınır yok.
    # Bir Question nesnesi için bu yıl yayımlanan tüm Choice nesnelerini bulalım.
    # (Yukarıda oluşturduğumuz current_year değişkenini kullanalım).
    >>> Choice.objects.filter(question__pub_date__year=current_year)
    <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

    # delete() fonksiyonunu kullanarak bir Choice nesnesini silelim.
    >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
    >>> c.delete()

Yönetici Paneli
***************

Bir yönetici kullanıcısı oluşturalım
=====================================

Yönetici paneline giriş yapmak için bir süper kullanıcıya ihtiyacımız
var. Komut satırında şu kodu çalıştıralım::

    python manage.py createsuperuser

İstediğiniz kullanıcı adını girin ve entera basın::

    Username: admin

Sizden email adresi istenecektir. Doldurmak istemezseniz boş bırakın::

    Email address: admin@example.com

Son olarak şifrenizi girin. Sizden iki kere şifre isteyecek 
(İkincisi doğrulama için).
::

    Password: **********
    Password (again): *********
    Superuser created successfully.

Geliştirme Sunucusunu Başlatın
==============================

Django'da yönetici paneli varsayılan olarak aktiftir. Geliştirme
sunucusunu başlatalım ve onu biraz araştıralım::

    python manage.py runserver

Şimdi tarayıcınızı açın ve yerel alan adınızda "`/admin/`" sayfasına
gidin.(Mesela şöyle `http://127.0.0.1:8000/admin/`) Şöyle bir
yönetici sayfası görüyor olmalısın:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin01.png

Yönetici Paneline Giriş yapalım
================================

Şimdi oluşturduğun süper kullanıcı ile yönetici paneline giriş yap.
Yönetici panelinin anasayfasını görüyor olmalısın:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin02.png


Birkaç düzenlenebilen içerik türü görmelisiniz: gruplar ve 
kullanıcılar. Django tarafından gönderilen kimlik doğrulama 
çerçevesi `django.contrib.auth` tarafından sağlanmıştır.

Anket uygulamamızı yönetici panelinden kontrol edelim
======================================================

Fakat bizim anket uygulamamız nerede? Yönetici panelinin
anasayfasında gözükmüyor.

Bu sorunu çözmek için yapmanız gereken tek şey:
Yönetici paneline Question nesnelerimizin yönetici panelinden 
düzenlenebildiğini söylemek. Bunu yapmak için **polls/admin.py**
dosyasını açıp şu kodla düzenlemek::

    from django.contrib import admin
    from .models import Question
    admin.site.register(Question)

Yönetici panelinin işlevselliğini keşfedelim
=============================================

Question nesnelerini kaydettiğimize göre yönetici panelinin
anasayfası şu şekilde gözükmeli:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin03t.png

`Question` yazısına tıkla. Şimdi Question nesnelerinin değiştirme
sayfasındasın. Bu sayfa veritabanındaki tüm Question nesnelerini
gösterir ve değiştirmek için birini seçmeni sağlar. Şu an daha 
önce oluşturduğumuz "What’s up?" nesnesi var:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin04t.png

Düzenlemek için “What’s up?” nesnesine tıkla:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin05t.png

Burada birkaç not:

- Bu form Question modelinden otomatik olarak oluşturulur.
- Farklı model alanlarına karşılık olarak uygun HTML etiketleri kullanılır.
- DateTimeField alanı için "Bugün" veya "Şimdi" gibi kısayollar bulunur.

Alt tarafta birkaç ayar bulunuyor:

- Save – Değişiklikleri kaydeder ve değişiklik listesi sayfasına nesne tipini ekler.
- Save and continue editing – Değişiklikleri kaydeder ve sayfayı yeniden yükler.
- Save and add another – Değişiklikleri kaydeder ve yeni bir yükleme sayfası açar.
- Delete – Gösterilen nesneyi siler.


“Date Published” değeri, part 1'de oluşturduğunuz zamanla uyuşmuyorsa 
muhtemelen TIME_ZONE ayarı için doğru değeri ayarlamamışsınız. 
Değiştirin, sayfayı yeniden yükleyin ve doğru değerin görünüp görünmediğini 
kontrol edin.


“Today” ve “Now” kısayollarını tıklayarak “Date Published” değerini değiştirin. 
Ardından “Save and continue editing” i tıklayın. Daha sonra sağ üstteki 
"History"yi tıklayın. Bu nesnede yapılan tüm değişiklikleri, değişikliği yapan 
kişinin değişiklik yaptığı zaman ve kullanıcı adıyla listeleyen bir sayfa görürsünüz:

.. image:: https://docs.djangoproject.com/en/2.0/_images/admin06t.png

