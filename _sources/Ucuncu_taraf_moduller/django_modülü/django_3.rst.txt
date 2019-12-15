.. meta::
   :description: Bu bölümde django view yazmayı ve şablon yazmayı öğreneceğiz.
   :keywords: python, django, çeviri, şablon, view, görünüm, dinamik URL 
   
.. highlight:: python3

******************************
İLK DJANGO PROJENİ YAZ, part 3
******************************

Genel Bakış
***********

Görünüm, genellikle belirli bir işleve hizmet eden ve belirli 
bir şablona sahip olan Django uygulamanızdaki bir Web sayfası 
türüdür. Örneğin, bir blog uygulamasında aşağıdaki viewları (viyıvları) 
kullanabilirsiniz:

- Blog ana sayfası --> Son birkaç gönderiyi gösterir.
- Gönderi detay sayfası --> Gönderiye özel sayfa
- Yıl tabanlı arşiv sayfası --> Tüm ayları, belirli bir yıldaki gönderilerle birlikte görüntüler.
- Ay tabanlı arşiv sayfası --> Tüm günleri, belirli bir ay içindeki gönderilerle birlikte görüntüler.
- Gün tabanlı arşiv sayfası --> Belirtilen güne ait tüm kayıtları görüntüler.
- Yorum eylemi --> Belirli bir girdiye yorum gönderilmesini sağlar.

Anket uygulamamızda aşağıdaki dört viewa sahip olacağız:

- Soru dizin sayfası --> Son birkaç soruyu gösterir.
- Soru detay sayfası --> Bir soru metni görüntüler (sonuçsuz ancak oy kullanacak biçimdedir.).
- Soru sonuç sayfası --> Sorunun sonucunu gösterir.
- Oylama eylemi --> Belirli bir soruda belirli bir seçim için oylama yapar.

Django'da web sayfaları ve diğer içerikler viewlara gönderilir.
Her view basit bir Python fonksiyonu ile ilişkilidir (veya sınıf temelli 
viewlarda bir metotla). Django, istenen URL’yi (Alan adından sonra URL’nin 
bir bölümü) inceleyerek bir view seçecektir .

Web’de bulunduğunuz süre içinde “ME2 / Siteler / dirmod.asp? 
Sid = & type = gen & mod = Core + Sayfalar & gid = A6CD4967199
A42D9B65B1B” gibi güzelliklerle karşılaşmış olabilirsiniz. 
Django'nun bize bundan daha zarif URL kalıpları sağladığını 
bilmekten memnun olacaksınız.

Bir URL deseni basitçe genel bir URL formudur. Örneğin: 
`/newsarchive/<year>/<month>/`.

Bir URL’den viewa ulaşmak için Django, `URLconfs` olarak 
bilinen şeyi kullanır. Bir URLconf, URL modellerini viewlara
eşler.

Birkaç view yazalım
*******************

Şimdi **pools/views.py** dosyasına birkaç view daha ekleyelim.
Bu viewlar biraz farklı çünkü birer argümanları var::

    def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)

    def results(request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)

    def vote(request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)

Yeni viewlarımızı **pools.urls** dosyasına path fonksiyonuyla 
çağırarak ekleyelim::

    from django.urls import path

    from . import views

    urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]

Tarayıcınıza “/polls/34/” sayfasına göz atın. `detail` fonksiyonu
çalışacak ve URL'de tanımladığınız ID her neyse onu gösterecektir.
“/Polls/34/results/” ve “/Polls/34/vote/” sayfalarını da deneyin.
Bunlar sonuç ve oylama sayfalarını gösterecektir.

Birisi sitenizden "/polls/34/" sayfasını istediğinde Django 
**mysite.urls** modülünü çalıştırır. Çünkü `ROOT_URLCONF` ayarında
bu modül belirtilmiştir. `urlpatterns` isimli değişkeni bulur ve 
desenleri sırayla geçirir. "polls/" eşleşmesini bulduktan sonra
eşleşen metni("polls/") çıkarır ve geri kalan metni("34/") işlemin
devamı için **polls.urls** dosyasındaki URLconf'a gönderir. 
Orada "<int:question_id>/" ile eşleşir ve `detail` viewı 
şöyle bir çıktıyla çalışır::

    detail(request=<HttpRequest object>, question_id=34)

`question_id=34` kısmı `<int:question_id>` kısmından geliyor. 
Küçüktür ve büyüktür işaretleri kullanmak URL'nin bir kısmını
yakalar ve viewa isimli parametre olarak yollar. `:question_id>` 
kısmı parametrenin ismini tanımlar. `<int:` kısmı ise yakalanması 
gereken veri türünü belirtir.

URL'nin sonuna `.html` gibi ifadeler eklemeye gerek yok. 
İsterseniz böyle bir şey yapabilirsiniz::

    path('polls/latest.html', views.index),

Fakat bunu yapmayın. Çok saçma.

Gerçekten bir şeyler yapan viewlar yazalım
******************************************

Her view iki şeyi yapmak ile sorumludur: `HttpResponse` nesnesiyle 
istenen sayfayı döndürmek ve `Http404` gibi bir hata oluşturmak.
Gerisi size kalmış.

Viewın bir veritabanındaki kayıtları okuyabilir. 
Sayfa kalıplarını(template) kullanabilir(Django'nun ve 3. taraf 
bir sayfa kalıbı). PDF, XML çıktısı veya ZIP dosyası oluşturabilir. 
İstediğin Python kütüphanesini kullanabilir.

Pratik olduğu için Django'nun kendi veritabanı API'ını kullanalım. 
İşte son 5 soruyu yayınlanma tarihine göre aralarına virgül 
koyarak sıralayıp sunan bir index viewı::

    #polls/views.py
    from django.http import HttpResponse

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)

    # Diğer viewlar(detail, results, vote) değişmedi.

Burada bir problem var: Sayfanın düzeni viewdaki sabit koddan 
ibaret. Eğer sayfanın görünüşünü değiştirmek istersen Python 
kodunu düzenleyeceksiz. Django'nun sayfa kalıbı sistemi, viewın 
kullanabileceği bir sayfa kalıbı oluşturarak tasarımı Python'dan 
ayırır.

İlk önce **polls** klasöründe bir **templates** klasörü oluştur. 
Django sayfa kalıplarını burada arayacak.

Projendeki `TEMPLATES` ayarı Django'nun sayfa kalıplarını neye 
göre yükleyip yorumlayacağını açıklar. Varsayılan olarak `DjangoTemplates` 
kullanılır. Eğer `APP_DIRS` seçeneği `True` ise `DjangoTemplates` 
`INSTALLED_APPS`'deki her uygulama dizininde **templates** dizinini arar.

Yeni oluşturduğun **templates** dizininde **polls** isimli bir dizin 
oluştur ve onun da içinde **index.html** isimli bir dosya oluştur. 
Diğer bir deyişle şablon şurada olmalı: **polls/templates/polls/index.html**. 
Çünkü şablon yükleyicisi yukarıda anlatıldığı şekliyle çalıştığında 
Django içindeki bu şablona kolayca **polls/index.html** şeklinde 
başvurabilirsiniz.

Aşağıdaki kodu bu şablona yerleştirin::

    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}

Şimdi **polls/views.py** index viewını şablonu kullanacak şekilde 
güncelleyelim::

    from django.http import HttpResponse
    from django.template import loader

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))

Bu kod **polls/index.html** isimli şablonu yükler ve bir içerik iletir. 
Bu içerik şablonun değişken isimleriyle Python nesnelerini eşleştiren 
bir sözlüktür.

Tarayıcınızda "/polls/" ekleyerek sayfayı yeniden yükleyin. Bir önceki 
bölümden "What’s up" sorusunu içeren bir liste görmelisiniz. Link sorunun 
detay sayfasına götürür.

render()
********

Bu şablon yüklemek için çok sıradan bir deyimdir, içeriği doldurur ve bir 
`HttpResponse` nesnesiyle işlenmiş şablon sonucunu döndürür. Burada 
index viewının tamamen tekrar yazılmış hali var::

    from django.shortcuts import render

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

Bunu tüm bu görünümlerde yaptıktan sonra, artık yükleyici ve 
HttpResponse'yi içe aktarmamız gerekmiyor (detay, sonuç ve oylama 
için hala bu yöntemleri kullanıyorsanız `HttpResponse`'yi tutmak 
isteyeceksiniz).

`render` fonksiyonu, ilk parametre olarak `request` nesnesini, ikinici 
parametre olarak şablonun adını ve üçüncü parametre olarak isteğe bağlı 
bir sözlük alır. İçerikle işlenmiş şablonun `HttpResponse` nesnesini döndürür.

404 hatası
**********

Şimdi soru detay sayfasını ele alalım. Bu sayfa verilen anket için 
soru metnini gösterir. Bu işi sağlayan view::

    from django.http import Http404
    from django.shortcuts import render

    from .models import Question
    # ...
    def detail(request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'polls/detail.html', {'question': question})

Buradaki yeni olayımız şu: İstenen kimliğe sahip bir soru yoksa view 
`Http404` hatası yollar.

**polls/detail.html** şablonuna ne koyabildiğimizi tartışacağız ancak 
yukarıdaki örneği hızlıca çalıştırmak istiyorsanız sadece şunu yazın::

    {{ question }}

Bu başlamak için yeterli.

get_object_or_404()
*******************

Bu eğer nesne varsa `get` fonksiyonunu kullanarak nesneyi getirir, yoksa 
`Http404` hatası yollar. Burada detay viewının tamamen tekrar yazılmış 
hali var::

    from django.shortcuts import get_object_or_404, render

    from .models import Question
    # ...
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})

`get_object_or_404()` fonkiyonu ilk parametre olarak Django modelini 
ve `get` fonksiyonuna vermek için istediğiniz sayıda isimli parametreyi alır.
Eğer nesne yoksa `Http404` hatası yollar.

Ayrıca, `get_object_or_404` fonksiyonu üzerine kurulu `get_list_or_404` 
fonkiyonu da vardır. Tek farkı `get` yerine `filter` kullanır. Eğer liste 
boşsa `Http404` hatası verir.

Şablon sistemi kullanalım
*************************

Anket uygulamanızdaki detay viewına geri dönelim. İçerik değişkeni 
`question` göz önüne alınıp tekrar yazıldığında **polls/detail.html** 
şablonu şöyle görülmeli::

    <h1>{{ question.question_text }}</h1>
    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
    </ul>

Şablon sistemi değişken özelliklerine erişmek için nokta arama 
sözdizimini kullanır. `{{ question.question_text }}` örneğinde Django önce 
sözlükte `question` nesnesini arar. Bunu başaramazsa, bu durumda çalışan 
bir öznitelik aramaya çalışır. O da başarısız olsaydı, liste 
dizini aramayı denerdi.

`question.choice_set.all` metodu `{% for %}` döngüsünde çağırılır. Metod 
Choice nesnelerini iterable olarak döndüren ve `{% for %}` döngüsünde 
kullanmak için en müsait kod olan `question.choice_set.all()` olarak yorumlanır.

Şablonlardaki sabit URL'leri kaldıralım
***************************************

Hatırla, `polls/index.html` şablonunda sorular için link yazdığımızda 
linki kısmen böyle kodlamıştık::

    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>

Bu kodlamada tipinde çok sayıda şablon içeren projelerde URL'leri 
değiştirmeye kalktığımızda sorun ortaya çıkıyor. Bununla 
birlikte, **polls.urls** modülünde path fonksiyonlarında `name` 
değişkenini tanımladığımızdan, url yapılandırmalarınızda tanımlanmış 
belirli URL yolları üzerine kurulu düzeni `{% url%}` template 
etiketini kullanarak kaldırabilirsiniz::

    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}
    </a></li>

Bunun çalışma şekli, polls.urls modülünde belirtilen URL tanımını 
aramaktır. Tam olarak 'detail' URL'sinin adının nerede tanımlandığını 
görebilirsiniz::

    ...
    # {% url %} şablon etiketiyle çağrılan 'name' değeri
    path('<int:question_id>/', views.detail, name='detail'),
    ...

Eğer anket detay sayfasının URL'sini değiştirmek istersen -mesela "polls/specifics/12/" 
gibi- bunu şablon ya da şablonlarda yapmak yerine **polls/urls.py**'de 
yapmanız yeterli::

    ...
    # 'specifics' sözcüğü eklendi.
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    ...

URL alanları
************

Bu öğretici bir uygulamaya sahip:`polls`. Gerçek bir Django projesi 
belki beş belki on belki daha fazla uygulamaya sahip olur. Peki Django 
farklı URL alanlarını nasıl birbirinden ayırır? Mesela `polls` uygulaması 
detay viewına sahip ve aynı projede bir de `blog` uygulaması detay sayfasına sahip. 
Django hangi uygulamanın viewının çağırıldığını nasıl bilebilir?

Cevap: URL şemasına alan adı eklemek. Alan adı oluşturmak için 
**polls/urls.py** dosyasında `app_name` değişkeni ekleyelim::

    from django.urls import path

    from . import views

    app_name = 'polls'
    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/', views.detail, name='detail'),
        path('<int:question_id>/results/', views.results, name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]

Şimdi **polls/index.html** şablonunda  değiştirelim::

    <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
