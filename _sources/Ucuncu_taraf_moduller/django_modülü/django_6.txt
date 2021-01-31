.. meta::
   :description: Bu bölümde reCAPTCHA s2 ile güvenlik konusunu inceleyeceğiz.
   :keywords: python, python3, django, reCAPTCHA


====================================
Django ile reCAPTCHA Kullanımı
====================================

1. Giriş.
    1.1 reCAPTCHA Nedir?

reCAPTCHA temelinde internet sayfalarının güvenliği insan ve bot davranışlarının ayrılmasını sağlayan bir uygulamadır.
    1.2	Neden reCAPTCHA Kullanmalıyım?

Bir yorum sistemi düşünelim herhangi bir güvenlik önlemi olmayan, bir gece basit bir saldırı ile milyonlarca istenmeyen yorum eklenebilir.
Bu tür olayların önüne geçmek için bazı önlemler alabiliriz. Yorum eklerken basit bir matematik sorusu veya
eski yöntem captcha kullanabiliriz ancak bunlar artık pek kullanışlı değiller. En basitinden eski usul captchalar size
bozulmuş bir görüntü verir ve o görüntüde bulunan matematik işlemini veya harfleri ister. Bazen bunlar aşırı bozulmalar oluyor ve
görüntünün okunması neredeyse imkânsız hale geliyor. Bunun yerine reCAPTCHA gibi bir servis kullanarak bu tür sıkıntıların önüne geçebiliriz.

2. Kurulum.
    2.1 reCAPTCHA Servisine Kayıt Olmak.

reCAPTCHA kullanmak için öncelikle sitesi üzerinden bir uygulama oluşturmak gerekli.
Bu `adres <https://www.google.com/recaptcha/admin/create>`_ üzerinden Google reCAPTCHA servisine kaydolmak gerekli.

.. image:: ../../../images/recaptcha/config.png
   :target: _images/recaptcha/config.png
    :align: center


Kaydolma sayfasını açtığımız zaman bizi böyle bir sayfa karşılıyor. Burada bulunan bölümleri açıklayalım.

* Etiket: Uygulamamızı açıklayacak isim.
* reCAPTCHA türü: İnternet sitemizde kullanacağımız reCAPTCHA türünü buradan seçiyoruz.
    * reCAPTCHA s3: Bu sürümde kullanıcının bot olup olmadığını bir puan yardımıyla hesaplayan ve size bu puanı döndüren bir Javascript API’dır.
    * reCAPTCHA s2: Kullanıcı isteklerini yine kullanıcının eylemleri ile doğrulayan sürümdür.
    * "Robot değilim" Onay Kutusu:  Kullanıcıya “Ben Robot Değilim” şeklinde bir kutu işaretletir.

.. image:: ../../../images/recaptcha/notrobot.gif
   :target: _images/recaptcha/notrobot.gif
   :align: center

.
    * Görünmez reCAPTCHA rozeti: İstekleri arka planda doğrular. Görünmez reCAPTCHA rozeti ile kullanıcının bir onay kutusuna tıklaması gerekmez. Bunun yerine kullanıcı sitenizde bulunan düğmeye tıkladığı zaman bir Javascript API çağrısı başlatılır.

.. image:: ../../../images/recaptcha/invisible_badge.png
   :target: _images/recaptcha/invisible_badge.png
   :align: center

.
    * reCAPTCHA v2 (Android): Android servisleri için kullanılacak olan seçimdir.

Detaylar için `adrese <https://developers.google.com/recaptcha/docs/version>`_ bakabilirsiniz.

* Alan Adları: Bu uygulamayı hazırlayacağınız servislerin hangi alan adları altında kullanacağınızı belirler.

`Not: Kayıt işleminiz burada girdiğiniz alan adları ve alt alan adlarıyla sınırlıdır. Başka bir deyişle example.com kayıt işlemi subdomain.example.com adresini de kaydeder. Geçerli bir alan adında ana makine bulunmalıdır; yol, bağlantı noktası, sorgu veya parça bulunmamalıdır.`

* Sahipler: reCAPTCHA uygulamasına yeni yöneticiler ekleyebilirsiniz. Varsayılan olarak sizin hesabınız eklidir.

* reCAPTCHA Hizmet Şartları'nı kabul edin: Servisi kullanmak için servis sahibi tarafından bizlere sunulan şartları kabul etmemiz gerekli.


* Site sahiplerine uyarı gönder: Şüpheli trafik gibi durumlarda mail yardımıyla uyarılar gönderir.

Yapılandırma işlemi oldukça kolay biz bu metin boyunda reCAPTCHA s2 `Robot Değilim` onay kutusunu kullanacağız.
Uygulamamızı kayıt ettiğimiz zaman bize iki adet anahtar hazırlanacak.
Bu anahtarlardan `Site Anahtarı` olan sitemizin HTML tarafında `Gizli Anahtar` olan ise sitemizin arka planında olacaktır.
**Gizli Anahtarı asla kullanıcılar ile paylaşmayın ve sitenizin HTML tarafında kullanmayınız.**

.. image:: ../../../images/recaptcha/keys.png
   :target: _images/recaptcha/keys.png
   :align: center

reCAPTCHA tarafıyla işimiz bitti. Şimdi reCAPTCHA’yı uygulamamıza entegre etme kaldı.

2.2 reCAPTCHA Servisini Uygulamaya Ekleme.
    reCAPTCHA servisini sitemize eklerken iki aşamalı olarak yapacağız. İlk aşaması sitemizin ön yüz için ikincisi için arka uç tarafında yapacağız. Bu belgede anlatılacak reCAPTCHA servisini bir yorum sistemine ekleyeceğiz.

    2.2.1 reCAPTCHA Servisini Ön Yüz için Hazırlama.

    `Google Geliştirici Belgelerine <https://developers.google.com/recaptcha/docs/display>`_ baktığımız zaman ön yüz tarafı için işimiz aşırı kolay. Öncelikle reCAPTCHA Javascript dosyasını projemize dahil ediyoruz.::

        <script src="https://www.google.com/recaptcha/api.js" async defer></script>

    reCAPTCHA servisne ihtiyaç duyduğumuz forma aşağıdaki kodu ekliyoruz.::

      <div class="g-recaptcha" data-sitekey="your_site_key"></div>

`data-sitekey` niteliğine reCAPTCHA tarafından bize sağlanan `Site Anahtarı` nı ekliyoruz. Ön yüz ile tüm işimiz bu.
    2.2.2 reCAPTCHA Servisini Arka Uç Tarafına Ekleme.

    Kendimize örnek bir proje ve bu proje için bir uygulama oluşturuyoruz. Gerekli anlatımlar önceki derslerde mevcuttur. Öncelikle örnek bir model oluşturuyoruz. Ben reCAPTCHA servisini yorum sisteminde kullanacağım içi yorumlar için bir model oluşturuyorum.

::

    from django.db import models

    class Comments(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=55, verbose_name='Kullanıcı Adınız')
        comment = models.TextField(verbose_name='Yorumunuz')

Ardından yorum uygulamamızın içine `forms.py` adında bir dosya oluşturuyoruz.

::

    from django import forms
    from blog.models import *


    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comments
            fields = [
                'name',
                'comment',
            ]


Şimdi ise kullanıcıyı karşılayacak sayfayı yazıyoruz. `templates` klasörü altında `index.html` adında bir dosya oluşturalım ve içine bu kodları yazalım.

::

    <html>
    <head>
        <title>reCAPTCHA Demo</title>
        <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    </head>
    <body>
    <h4>Yorum Gönder</h4>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <div class="g-recaptcha" data-sitekey="6LdBO6cZAAAAAKVrVb26js1qHkeg23ks213nQgpBq7L6dva9lMuwTmX"></div>
        <br/>
        <input type="submit" value="Gönder">
    </form>
    <hr>
    <h4>Gelen Yorumlar:</h4>
    <hr>
    {% for comment in comments %}
        <p><b>İsim: {{ comment.name }}</b> <br>Yorum: <b>{{ comment.comment }}</b></p>
        <hr>
    {% endfor %}
    </body>
    </html>

Kısaca HTML kodlarımızdan bahsedersek `POST` yöntemiyle gönderilecek bir form hazırladık. Ardından `{% csrf_token %}` değişkenini ekledik. Böylece formumuz doğru şekilde çalışacak. Ardından `forms.py`` sayfasında hazırladığımız formu kullanıcıya gösteriyoruz. Son olarak da Google Belgelerinde aldığımız reCAPTCHA kodunu ekledik.
Gelen yorumlar kısmında ise başarıyla kaydedilen yorumlar yer alacak.

Sıra tüm işi yapacak `views.py` dosyasında.

::

    from django.shortcuts import render #1
    from blog.models import Comments    #2
    from recaptcha import recaptcha_check #3
    from blog.forms import CommentForm  #4


    def index(request): #5
        comments = Comments.objects.all() #6
        comment_form = CommentForm(request.POST or None) #7
        recaptcha_response = request.POST.get('g-recaptcha-response') #8
        recaptcha_response_result = recaptcha_check(recaptcha_response) #9
        if recaptcha_response_result is True and comment_form.is_valid(): #10
            comment_form.save() #11
        context = {   # 12
            'form': comment_form,
            'comments': comments
        }
        return render(request, 'index.html', context) #13


Örnek kodumuz yukarıda. Bu kodu satır satır inceleyelim.

* #1, #2, #3, #4 Bu 4 kod satırı gerekli ihtiyaç duyduğumuz kütüphane ve modülleri dahil ediyoruz.
* #5 `index` isminde bir fonksiyon oluşturuyoruz.
* #6 Ana sayfamızda tüm yorumları listelemek bu satırda `Comments` modelinde bulunan tüm kayıtları listeliyoruz.
* #7 `forms.py` sayfasında oluşturduğumuz formu burada çağırıp bir değişkene atıyoruz.
* #8 reCAPTCHA  Django Formunda olmadığı için bu satırda `POST` yöntemiyle `'g-recaptcha-response` değişkenin değerini alıyoruz.
* #9 `recaptcha_check` isimli bir fonksiyon hazırladık böylece daha temiz bir görünüm elde ediyoruz. Bu fonksiyon ön yüz tarafından gelen kodu Google'ın doğrulama sunucusuna gönderiyor. Eğer sunucu doğrulamayı yaparsa sonuç olarak `True` veya hata olursa hatanın sebebini içeren bir sonuç dönecektir.
* #10 Bu satırda hazırladığımız `recaptcha_check` fonksiyonundan gelen değer ve Django Formunun geçerliliğini kontrol ediyoruz. Eğer iki karşılama da olumlu ise kod if bloğu devam eder.
* #11 Django Formunu kayıt ediyor.
* #12 `context` isimli bir sözlük hazırlıyoruz ve içine Django Formunu ve kayıt edilen tüm yorumları ekliyoruz.
* #13 `render` fonksiyonu ile `index.html` dosyasını `context` değişkenini ekliyoruz.

`recaptcha_check` fonksiyonunu satır satır inceleyelim.

::

    import requests #1


    def recaptcha_check(recaptcha_response): #2
        verify_url = 'https://www.google.com/recaptcha/api/siteverify' #3
        value = { #4
            'secret': '6LdBO6cZAAAAAAALlKFW656QWAPLOKasoPfLfYTVWV91Quo0H2tWBfRrc',
            'response': recaptcha_response
        }
        response = requests.post(verify_url, value) #5
        result = response.json() #6
        if result['success'] is True: #7
            return True
        else: #8
            return {'status': result['success'], 'reason': result['error-codes']} #


* #1 `requests` kütüphanesini dahil ediyoruz.
* #2 `recaptcha_response` parametresini alan `recaptcha_check` isimli bir fonksiyon hazırlıyoruz.
* #3 Google doğrulama sunucusunun adresini yazıyoruz.
* #4 `value` isimli değişken oluşturuyoruz ve içine reCAPTCHA'nın uygulamasını kurulumunu yaparken bize sağlanan `Gizli Anahtar` değerini `secret` anahtarına, fonksiyona gelen `recaptcha_response` değerini `response` anahtarına atıyoruz.
* #5 requests kütüphanesini kullanarak `POST` yöntemiyle Google doğrulama sunucusuna `value` değişkenini gönderiyoruz.
* #6 Google doğrulama sunucusundan gelen değeri json haline getiriyoruz.
* #7 Eğer dönen sonuç başarılı ise fonksiyon `True` döndürür
* #8 Sonuç başarısız olursa neden başarısız olduğu dahil bir sözlük değeri döndürür.

Bu anlatımda hazırlanan kodlara `buradan <https://github.com/mehmetkiran/reCAPTCHA>`_ ulaşabilirisniz.
