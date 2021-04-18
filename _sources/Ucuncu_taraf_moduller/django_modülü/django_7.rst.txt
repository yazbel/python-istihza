.. meta::
   :description: Bu bölümde Django ile gelen kullanıcı modülünü kişiselleştireceğiz.
   :keywords: python, python3, django, model

==========================================================================
Django Kişiselleştirilmiş Kullanıcı Modelini Dahili Model ile Genişletmek
==========================================================================

Django içinde hazır birçok modül ve modeller ile gelir. Bunlardan biri de kullanıcı modeli. Bu model ile hazırladığınız Django projesine çok hızlı bir şekilde üyelik sistemi geliştirebilirsiniz. Ancak bazen bu model tek başına yeterli gelmez. Böyle durumlarda kendi yazdığımız modeli Django ile gelen kullanıcı modeli ile genişletebiliriz.

Bu Yöntemin Avantajları Neler?
================================

Django kullanıcı modeli yetki yönetim sistemi ve bazı hazır fonksiyonlar ile beraber gelir. Bu sayede kullanıcıların yetkisiz erişimlerini, yetki yönetimlerini, giriş, çıkış, parola değiştirme fonksiyonlarına ve bazı bezeyicilere(decarator) sahip oluruz. Bunlar sayesinde projemiz çok hızlı şekilde ilerleyebilir.

.. image:: ../../../images/customusermodel/django_admin.png
   :target: _images/customusermodel/django_admin.png
   :align: center

Django Admin Panelinden Kullanıcı ve Grup İzinleri Yönetimi


Nasıl Yapılır?
===============

Projemize bir adet uygulama ekliyoruz. Bu uygulama kullanıcı modelimizi barındıracak ve Django'nun dahili kullanıcı modeli ile genişletilecek.
`settings.py` dosyamıza `AUTH_USER_MODEL = uygulama_adi.model_adi` değişkenini ekliyoruz böylece varsayılan kullanıcı modelini geçersiz kılarak kendi modelimizi kullanabiliriz.


    .. |warning| image:: ../../../images/customusermodel/warning_icon.png
       :width: 32

    |warning| Hazırladığınız uygulamayı `settings.py` dosyasında `INSTALLED_APPS` kısmına eklemeyi unutmayın.

Ardından uygulamamızın `models.py` dosyasında bir model oluşturmamız gerekli. Bu model dosyasını dahili Django kullanıcı modeli ile genişleteceğz. Öncelikle genişleşme sırasında doğru olan modeli seçmeliyiz. Django bize iki adet sınıf sunuyor bunlar
`Abstractuser` ve `AbstractBaseUser`.


    * AbstractUser: Bu model ile beraber temel kullanıcı veri giriş alanları da geliyor. (Ad, soyad, son giriş, kayıt tarihi vs.)
    * AbstractBaseUser: Bu model ile beraber sadece kimlik doğrulama fonksiyonları gelmekte. Kullanıcı veri giriş alanları gelmiyor.

Bu anlatıda AbstractUser ile genişletme yapacağız. Sınıfımızı yazıyoruz ve test etmek amacıyla fazladan veri giriş alanları ekleyelim.
Örnek kod:

    .. code-block:: py

        class CustomUserModel(AbstractUser):
            website = models.URL_Fields(verbose_name='Web Sitesi', blank=True)
            os = models.CharField(verbose_name='Kullandığı İşletim Sistemi', max_length=256)
            def __int__(self):
                return self.id

Hazırladığımız modeli veritabanı şemamıza uygulayacağız.


    .. code-block:: bash

        python manage.py makemigrations

    .. code-block:: bash

        python manage.py migrate


Yaptıklarımızı kontrol etmek için Python konsolunu açarak modelimizi dahil edelim.


    .. code-block:: py

        from user.models import *
        CustomUserModel._meta.get_fields()

Çıktı:
        (<ManyToOneRel: admin.logentry>, <django.db.models.fields.AutoField: id>, <django.db.models.fields.CharField: password>, <django.db.models.fields.DateTimeField: last_login>, <django.db.models.fields.BooleanField: is_superuser>, <django.db.models.fields.CharField: username>, <django.db.models.fields.CharField: first_name>, <django.db.models.fields.CharField: last_name>, <django.db.models.fields.EmailField: email>, <django.db.models.fields.BooleanField: is_staff>, <django.db.models.fields.BooleanField: is_active>, <django.db.models.fields.DateTimeField: date_joined>, <django.db.models.fields.URLField: website>, <django.db.models.fields.CharField: os>, <django.db.models.fields.related.ManyToManyField: groups>, <django.db.models.fields.related.ManyToManyField: user_permissions>)


Çıktıyı incelediğimiz zaman `<django.db.models.fields.URLField: website>, <django.db.models.fields.CharField: os>` veri giriş yerlerini görüyoruz. Böylece yaptıklarımızın sıkıntısızca sisteme işlendiğini anlayabiliriz. Artık Django'nun dahili yetkliendirme ve kullanıcı sistemini kendi kullanıcı modelimiz üzerinden kullanabiliriz.

