.. meta::
   :description: Bu bölümde tornado ile web uygulaması geliştirmeye başlıyoruz.
   :keywords: python, tornado, Kurulum, Proje Oluşturma, View, Template

.. highlight:: python3

*******
Tornado 
*******

Eğer yazdığınız sitede gerçek zamanlı(real-time) bağlantılar kullanacaksanız 
ya da bir mikro çerçeveye(micro framework) ihtiyacınız varsa tornado tamamen 
sizin ihtiyaçlarınız için tasarlanmış bir çerçeve.

Kurulum
=======

Tornado'yu kullanmak için önce indirmemiz gerekiyor. Aşağıdaki komutu komut 
istemcisinde yazın::

    pip install tornado

`Successfully installed tornado-6.1` yazısını gördüyseniz sorunsuzca inmiştir.

Proje Oluşturma
===============

Tornado, herhangi bir dizinde açtığınız herhangi bir dosyada çalışabilir. Yani 
normal bir python dosyası açalım ve yazmaya başlayalım. Ben `torn` isimli bir 
klasör açıp `__init__.py` dosyasında yazacağım. Önce dosyanın ana 
bileşenlerini yazalım::

    import tornado.web
    import tornado.ioloop

    app = tornado.web.Application()
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()

Hemen burada ne yaptığımızı açıklayalım.

Önce kullanacağımız modülleri içeri aktardık::

    import tornado.web
    import tornado.ioloop

Daha sonra bir sitemizi çalıştırmak için gerekli ayarları yaptık::

    app = tornado.web.Application()
    # İleride yönlendirme(routing) için kullanacağımız araç.
    app.listen(8888)
    # Port olarak 8888 belirledik. Siz başka bir sayı seçebilirsiniz.

    tornado.ioloop.IOLoop.current().start()
    # Sitemizi çalıştırmaya başladık

Sitemizi açmak için önce yazdığımız dosyayı çalıştıralım. Daha sonra 
`http://localhost:8888/` adresine gidelim. Elbette farklı bir port seçtiyseniz 
portu değiştirmeyi unutmayın.

Siteye girdiğiniz zaman sizi `404: Not Found` yazısı karşılayacak. Çünkü daha 
hiç sayfa oluşturmadık. Hadi şimdi bir sayfa oluşturalım.

Sayfa Sunma
===========

Sitemizde sayfa sunmak için bir view yazmalıyız. Geleneği bozmayalım ve 
"Merhaba Zalim Dünya" yazarak başlayalım. Bu iş için `Application`'da olduğu 
gibi `tornado.web` modülünü kullancağız. Bu sefer `RequestHandler` isimli 
bir sınıf bize yardımcı olacak.

Şimdi yazacağımız kodları içe aktarma ile `app` değişkeni arasına yazalım::

    class Merhaba(tornado.web.RequestHandler):
        # View için bir sınıf oluşturduk
        def get(self):
            # Sayfayı yollayan fonksiyonumuz
            self.write("Merhaba, Zalim Dünya!")
            # En basit yolu kullanarak "Merhaba, Zalim Dünya!" yazdık

İlk viewımızı yazdık. Şimdi dosyamızı tekrar çalıştırıp test edelim.

Sonuçta bir değişiklik olmadığını göreceksiniz. Yani hâlâ `404: Not Found` 
yazıyor. Çünkü sitemize gelen istekle view arasındaki bağlantıyı kurmadık.
Hadi hemen yapalım.

Kullanıcının siteye girmesiyle sunucuya bir istek yollanır. Bu istek 
kullanıcının adres çubuğuna yazdığı ifadeyle doğrudan ilişkilidir.
Mesela kullanıcı `http://localhost:8888/istihza/` yazarsa bizden `/istihza/` 
adresini istemiştir. Eğer biz bu adresi bir view ile ilişkilendirdiysek bu view 
çalışır. Eğer ilişkilendirmediysek `404` hatası alırız. Biz `Tornado`'da bu 
ilişkilendirme işini `Application`'dan faydalanarak yapıyoruz. Yani
`app = tornado.web.Application()` diye yazdığımız bölümü düzenleyeceğiz::

    app = tornado.web.Application([
        ("/", Merhaba)
    ])

Şu an `/` isteği ile `Merhaba` viewı arasında bir ilişki kurduk. Nasıl 
yazdığımıza dikkat edelim: Bir liste içinde önce istek sonra view içeren 
bir demet. Eğer daha fazla view eklemek isterseniz aynı liste içine demet 
ekleyerek yapabilirsiniz. `http://localhost:8888/` adresine giderek 
`Merhaba, Zalim Dünya!` yazdığını görebiliriz.

Yazdığımız kodları topluca paylaşayım::

    import tornado.web
    import tornado.ioloop

    class Merhaba(tornado.web.RequestHandler):
        # View için bir sınıf oluşturduk
        def get(self):
            # Sayfayı yollayan fonksiyonumuz
            self.write("Merhaba, Zalim Dünya!")
            # En basit yolu kullanarak "Merhaba, Zalim Dünya!" yazdık

    app = tornado.web.Application([
        ("/", Merhaba)
    ])
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()

Template(Şablon) Sistemi
========================

Sitemizde göstereceğimiz sayfaları `html` formatında yazıp kaydetmeliyiz.
Daha sonra bu dosyaları `Tornado` ile çağırıp servis etmeliyiz.

Göstereceğimiz sayfalar ikiye ayrılıyor: "Statik" ve "Dinamik". Statik sayfalar 
`Tornado`'nun çağırıp değiştirmeden servis ettiği dosyalardır. Dinamik sayfalar 
ise `Tornado`'nun çağırdıktan sonra düzenleyip servis ettiği dosyalardır.

Önce bir `html` dosyası oluşturalım, ardından bu dosyayı servis edelim.

.. code-block ::

    <!DOCTYPE html>
    <html>
    <head>
        <title>Merhaba Zalim Dünya</title>
    </head>
    <body>
        <h1>Merhaba Zalim Dünya</h1>
    </body>
    </html>

Bu dosyayı "`index.html`" ismiyle `torn` klasörüme kaydedeceğim. Siz başka bir 
isimle başka bir klasöre de kaydedebilirsiniz. Hemen servis etmek için `Merhaba` 
`view`'ını düzenleyelim::

    class Merhaba(tornado.web.RequestHandler):
        def get(self):
            loader = tornado.template.Loader(".")
            sayfa = loader.load("index.html").generate()
            self.write(sayfa)

Ben servis etmek için `Merhaba view`'ını düzenlemeyi tercih ettim. Ancak siz yeni 
bir `view` yazmak isteyebilirsiniz. Bu durumda yazdığınız `view`'ı yeni bir istek 
ile eşleştirmeniz gerekir. Bu iş için de bir örnek verip kodlarımızı açıklayayım. 
Oluşturduğunuz `view`'ın adı `Yazbel` olsun ve `/yazbel/` isteği ile 
ilişkilendirelim::

    app = tornado.web.Application([
        ("/", Merhaba), # Buradaki virgülü koymayı unutmayınız
        ("/yazbel/", Yazbel)
    ])

Bu durumu geçip yukarıdaki kodlara tekrar bakalım. İlk satırda eklediğimiz kod::

    loader = tornado.template.Loader(".")

Burada `Html` dosyalarımızın bulunduğu dizini `Tornado`'ya bildirdik. Eğer 
`Html` dosyalarınız farklı bir dizinde yer alıyorsa benim `.` yazdığım yeri 
o dizin ile değiştirmelisiniz. 

Peki neden bildirdik? Çünkü web programlamada 
`Html`, `Css`, `Js`, `Resim` gibi dosyalar kendilerine ait bir klasörde bulunur. 
Biz `Html` dosyalarının bulunduğu klasörü bildirerek tekrar tekrar yazmaktan 
kurtulduk. İkinci eklediğimiz satıra bakalım::

    sayfa = loader.load("index.html").generate()

Burada daha önce oluşturduğumuz `loader` değişkenini kullanarak sayfamızı 
getirdik. `generate` fonksiyonunu kullanarak sayfayı `Tornado`'nun sunabileceği 
bir hale dönüştürdük. Daha sonra `write` fonksiyonuyla sayfamızı gösterdik::

    self.write(sayfa)

Şimdi de dinamik sayfaların nasıl oluşturulduğuna bakalım. Dinamik sayfaların 
çağrıldıktan sonra düzenlendiğini söylemiştik. Düzenleyeceğimiz yeri 
`Tornado`'ya bildirmek için `Template`(Şablon) denen bir yöntemden faydalanacağız.
Değişiklik yapmak istediğimiz yeri 2 tane küme parantezi içinde bir isimle 
`Html` dosyamızda kullanıyoruz. Hemen bir `index.html` dosyasını düzenleyerek bir 
örnek verelim.

.. code-block ::

    <!DOCTYPE html>
    <html>
    <head>
        <title>Merhaba {{ yazbel }}</title>
    </head>
    <body>
        <h1>Merhaba {{ yazbel }}</h1>
    </body>
    </html>

Burada `{{ yazbel }}` yazarak `yazbel` isimli bir değişken tanımladık. Tabi ki 
siz farklı bir değişken isimi seçebilirsiniz.

Şu an `__init__.py` dosyamızı çalıştırıp `http://localhost:8888/` adresine 
gidersek `500` hatasıyla karşılaşacağız. `__init__.py`'nin çalıştığı komut 
istemcisine bakarsak bir hata göreceğiz.

.. code-block ::

    NameError: name 'yazbel' is not defined

Bu hatadan `yazbel` isimli bir değişken tanımlayıp ona bir değer vermediğimiz 
için karşımıza çıktı. Bu değişkene değer vermek için `generate` fonksiyonunu 
kullanacağız::

    sayfa = loader.load("index.html").generate(yazbel="Yazbel")

`__init__.py` dosyasını tekrar çalıştırdığımızda `Merhaba Yazbel` yazısıyla 
karşılaşacağız.

Aklınıza şöyle bir soru takılmış olabilir: Bu şekilde yapmak yerine `Html` 
dosyasını düzenlemek daha kolay olmaz mı?

Elbetteki olabilir ancak aynı işi yapan birkaç view daha yazdığımızda 
birkaç `Html` dosyası daha oluşturmamız gerekir. Mesela sitemize şu iki 
`view` da katıldığında dinamik olarak oluşturmak daha mantıklı oluyor::

    class Merhaba_istihza(tornado.web.RequestHandler):
        def get(self):
            loader = tornado.template.Loader(".")
            sayfa = loader.load("index.html").generate(yazbel="İstihza")
            self.write(sayfa)

    class Merhaba_Dünya(tornado.web.RequestHandler):
        def get(self):
            loader = tornado.template.Loader(".")
            sayfa = loader.load("index.html").generate(yazbel="Dünya")
            self.write(sayfa)

`Template` sisteminde kullanabileceğimiz bir özellik daha var:`if`, `else`, 
`else`, `for`. Fakat bu özelliği 2 küme işareti arasında değil 1 küme 1 yüzde 
işareti arasında kullanıyoruz: `{% else %}`. Bu özelliği anlatma için 
listelerden faydalanalım. `Merhaba` viewımızı `yazbel` değişkenine bir liste 
verecek şekilde düzenleyelim::

    class Merhaba(tornado.web.RequestHandler):
        def get(self):
            loader = tornado.template.Loader(".")
            liste = [0, 1, 2, 3]
            sayfa = loader.load("index.html").generate(yazbel=liste)
            self.write(sayfa)

Hemen bu sayıları listeleyecek bir `Template` (Şablon) yazalım. Bu listede 
çift sayılar büyük, tek sayılar küçük gözüksün.

.. code-block ::

    <!DOCTYPE html>
    <html>
    <body>
        {% for sayı in yazbel %}
            {% if sayı%2==0 %}
                <h1> {{ sayı }} </h1>
            {% else %}
                <h4> {{ sayı }} </h4>
            {% end %}
        {% end %}
    </body>
    </html>

Gördüğünüz gibi genel olarak `python` ile çok benzer bir yapıya sahip ancak 
çok önemli bir fark var. `for` döngüsü bir `end` ifadesiyle bitiyor. Aynı 
şekilde birbiriyle ilişkili kontrol ifadeleri(`if`, `else`) hep birlikte 
bir `end` ile bitiyor.