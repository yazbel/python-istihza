.. meta::
   :description: Bu bölümde tornado ile basit bir site yapacağız.
   :keywords: python, tornado, framework, mikro framework, web framework

.. highlight:: python3

*******
Tornado 
*******

Eğer yazdığınız sitede gerçek zamanlı(real-time) bağlantılar kullanacaksanız 
ya da bir mikro çerçeveye(micro framework) ihtiyacınız varsa tornado tamamen 
sizin ihtiyaçlarınız için tasarlanmış bir çerçeve.

Bu yazıda sizlerle bir sayaç yapacağız. Sizler öğrendikten sonra daha karmaşık 
işler yapabilirsiniz.

Kurulum
=======

Tornadoyu kullanmak için önce indirmemiz gerekeiyor. Aşağıdaki komutu komut 
istemcisinde yazın::

    pip install tornado

`Successfully installed tornado-6.1` yazısını gördüyseniz sorunsuzca indirmişsiniz.

Proje Oluşturma
===============

Tornado, herhangi bir dizinde açtığınız herhangi bir dosyada çalışabilir. Yani 
normal bir python dosyası açalım ve yazmaya başlayalım. Ben bir klasör açıp 
`__init__.py` dosyasında yazacağım. Önce dosyanın ana bileşenlerini yazalım::

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

Sitemizde sayfa sunmak için bir view yazmalıyız. Bir sayaç uygulaması yapacağımızı
söyledim ancak geleneği bozmayalım ve "Merhaba Zalim Dünya" yazarak başlayalım.
Bu iş için `Application`'da olduğu gibi `tornado.web` modülünü kullancağız. 
Bu sefer `RequestHandler` isimli bir sınıf bize yardımcı olacak.

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

Yazdığımız kodları paylaşarak bu yazıyı bitirelim::

    import tornado.web
    import tornado.ioloop

    class Merhaba(tornado.web.RequestHandler):
        # View için bir sınıf oluşturduk
        def get(self):
            # Sayfayı yollayan fonksiyonumuz
            self.write("Merhaba, Zalim Dünya!")
            # En basit yolu kullanarak "Merhaba, Zalim Dünya!"

    app = tornado.web.Application([
        ("/", Merhaba)
    ])
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()
