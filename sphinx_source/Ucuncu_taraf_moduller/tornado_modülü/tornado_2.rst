.. meta::
   :description: Bu bölümde tornado ile web uygulaması geliştirmeye başlıyoruz.
   :keywords: python, tornado, Kurulum, Proje Oluşturma, View, Template

.. highlight:: python3

***************
Tornado(devamı)
***************

Websocket
=========

Bazen amacımız web sayfaları sunmak olmaz. Uygulamamızla sürekli olarak veri 
alışverişinde bulunmak isteriz. Mesela çevrimiçi oyunlarda veya mesajlaşma
uygulamalarında bu durumla sık karşılaşırız. Ancak `HTTP` protokolü bu iş 
için yetersiz kalır. Çünkü `HTTP` protokolü en basit haliyle şu şekilde çalışır: 
Kullanıcı istek yollar, sunucu isteğe karşılık sayfa yollar, bağlantı kesilir. 
Sürekli olarak bağlantı kurmak istediğimizde yeni bir protokol kullanmalıyız: `WS`. 
`WS` protokolü kullanıcı veya sunucu kapatana kadar bağlantı açık kalır. 
Sunucu veya kullanıcı herhangi bir istek olmadan birbirine veri yollayabilir. 

`Websocket`'ler, en basit tabirle `HTTP` yerine `WS` protokolü kullanan 
viewlardır. Biz bir `view` tanımlarken sadece `get` metodunu yazmıştık. 
Çünkü bir `view` sadece sayfamızı sunuyordu. Ancak `websocket`ler sadece 
sayfa sunmuyorlar, aynı zamanda veri de alıyorlar. Bu yüzden 3 tane 
metoda sahipler: `on_open`, `on_message`, `on_close`.

`Websocket` ile bağlantı kurulduğunda `on_open` metodu çağrılıyor. 
`Websocket`'e mesaj geldiğinde `on_message` metodu çağrılıyor. 
`Websocket`'in bağlantısı kapatıldığında `on_close` metodu çağrılıyor. 

Biz `view` ile kullanıcıya veri yollarken `write` metodundan faydalanmıştık. 
Fakat `websocket`ler bu iş için `write_message` metodunu kullanıyor.

Şimdi gelen mesajları geri gönderen bir `websocket` yazalım::

    import tornado.web
    import tornado.ioloop

    import tornado.websocket

    class Geri(tornado.websocket.WebSocketHandler):

        def on_open(self):
            print("Bağlantı kuruldu")
        
        def on_message(self, mesaj):
            print(mesaj)
            self.write_message(mesaj)

        def on_close(self):
            print("Bağlantı kapandı")

    app = tornado.web.Application([
        ("/ws/geri", Geri)
    ])
    app.listen(8888)

    tornado.ioloop.IOLoop.current().start()

İlk işimiz yeni bir kütüphane eklemek oldu.Bu kütüphane bizim `websocket` 
yazmamız için gerekli sınıfı bulunduruyor.

::

    import tornado.websocket

Yeni bir sınıf oluşturduk::

    class Geri(tornado.websocket.WebSocketHandler):

Bu sınıf bizim `websocket`imiz. Daha önce `view` yazarken 
`tornado.web.RequestHandler` sınıfından faydalanmıştık. Şimdi ise 
`tornado.websocket.WebSocketHandler` sınıfından faydalandık. 

`Websocket` ile bağlantı kurulduğunda bize `Bağlantı kuruldu` yazması için 
`on_open` metodunu düzenledik::

    def on_open(self):
        print("Bağlantı kuruldu")

`Websocket`e mesaj geldiğinde onu yazdırıp geri yollaması için `on_message` 
metodunu düzenledik. Burada metodumuzun bir parametresi daha olduğuna dikkat 
edelim::

    def on_message(self, mesaj):
        # Mesajı yazdır
        print(mesaj)
        # Mesajı geri yolla
        self.write_message(mesaj)

`Websocket` kapandığında ekrana yazdırması için `on_close` metodunu düzenledik::

    def on_close(self):
        print("Bağlantı kapandı")

Gerekli yönlendirmeyi yapması için `Application` nesnemizi düzenledik::

    app = tornado.web.Application([
        ("/ws/geri/", Geri)
    ])

Biz hem `websocket`leri hem `view`ları aynı `Application` nesnesine yazıyoruz. 
Burada ayrım yapmak için genelde `websocket`lerin isteklerini "`/ws/`" ile 
başlatmaya önem veriyoruz.

`Websocket`lere tarayıcımızdaki adres çubuğuna yazarak ulaşamayız. 
Tarayıcımızdaki adres çubuğu sadece `HTTP` protokolünü kullanır. 
`Websocket`lere ulaşmak için kütüphaneleri kullanıyoruz. Neredeyse 
her programlama dilinde bu iş için bir kütüphane bulunuyor. Python da 
böyle bir kütüphaneye sahip ancak genelde Javascript daha çok tercih 
edildiği için ben Size Javascript'teki `websocket` kullanımı üzerine bir örnek 
yazmak istiyorum. Elbette bu noktada temel seviyede Javascript bilgisi 
gerekecektir.

.. code-block ::

    var ws = WebSocket("ws://localhost/ws/geri/")
    // Bir websocket örneği oluşturduk.
    // Bu iş için http yerine ws kullandığımıza dikkat edelim

    ws.onopen = function(){
        // Bağlantı kurulduğunda çalışan fonksiyon
        console.log("Bağlantı kuruldu!")
        // Konsola 'Bağlantı Kuruldu' yazdırdık
        ws.send("Merhaba Zalim Dünya")
        // Sunucuya mesaj yolladık
    }

    ws.onmessage = function(mesaj){
        // Mesaj geldiğinde çalışan fonksiyon
        console.log(mesaj.data)
        // Mesajımızın içeriğini konsola yazdırdık
        ws.close()
        // Bağlantıyı kapattık
        // Burada kapatmak zorunda değiliz.
        // Sadece kapatma yöntemini göstermek istedim.
    }

.. note :: Bu kodları sadece localhost alan adı altında ve `__init__.py` 
           dosyası çalışırken çalıştırabilirsiniz.
