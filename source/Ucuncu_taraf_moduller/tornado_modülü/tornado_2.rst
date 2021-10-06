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
`view`'lardır. Biz bir `view` tanımlarken sadece `get` metodunu yazmıştık. 
Çünkü bir `view` sadece sayfamızı sunuyordu. Ancak `websocket`'ler sadece 
sayfa sunmuyorlar, aynı zamanda veri de alıyorlar. Bu yüzden 3 tane 
metoda sahipler: `on_open`, `on_message`, `on_close`.

`Websocket` ile bağlantı kurulduğunda `on_open` metodu çağrılıyor. 
`Websocket`'e mesaj geldiğinde `on_message` metodu çağrılıyor. 
`Websocket`'in bağlantısı kapatıldığında `on_close` metodu çağrılıyor. 

Biz `view` ile kullanıcıya veri yollarken `write` metodundan faydalanmıştık. 
Fakat `websocket`'ler bu iş için `write_message` metodunu kullanıyor.

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

Bu sınıf bizim `websocket`'imiz. Daha önce `view` yazarken 
`tornado.web.RequestHandler` sınıfından faydalanmıştık. Şimdi ise 
`tornado.websocket.WebSocketHandler` sınıfından faydalandık. 

`Websocket` ile bağlantı kurulduğunda bize `Bağlantı kuruldu` yazması için 
`on_open` metodunu düzenledik::

    def on_open(self):
        print("Bağlantı kuruldu")

`Websocket`'e mesaj geldiğinde onu yazdırıp geri yollaması için `on_message` 
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

Burada 2 önemli nokta var. Biz hem `websocket`'leri hem `view`'ları aynı 
`Application` nesnesine yazıyoruz. Burada ayrım yapmak için genelde 
`websocket`'lerin isteklerini "`/ws/`" ile başlatmaya önem veriyoruz. Diğer 
sıkıntı ise gelen isteklerin protokollerine göre ayrılmadan işlenmesi. Yani 
kullanıcı "`HTTP` ile mi istekte bulundu, `WS` ile mi istekte bulundu?" diye 
sorulmuyor. Bu ayrım direkt olarak bizim o isteğe karşı ne yazdımız ile ilgili.

`Websocket`'lere tarayıcımızdaki adres çubuğuna yazarak ulaşamayız. 
Tarayıcımızdaki adres çubuğu sadece `HTTP` protokolünü kullanır. 
`Websocket`'lere ulaşmak için kütüphaneleri kullanıyoruz. Ben size javascript 
ile nasıl bağlantı kurabileceğinizi göstereceğim. Bu noktada basit seviyede 
javascript bilgisine sahip olmanız gerekiyor.

.. note :: Burada javascript için yazdığımız kodları tarayıcınızın konsolunda 
           yazabilirsiniz. (Tarayıcınızda F12 tuşuna basın ve yukarıdaki 
           sekmelerden "console" yazanı seçin.)

`__init__.py` dosyamızı çalıştıralım ve javascript kodlarımızı yazmaya 
başlayalım.

`ws` isminde bir `Websocket` nesnesi oluşturacağız. Javascript'te nesne 
oluşturmak için `var` deyimi kullanılıyor ve satır sonuna `;` koyuluyor. 
Bir `Websocket` nesnesi oluştururken hangi siteye bağlanacağımızı belirtiyoruz:

.. code-block ::

    var ws = new WebSocket("ws://localhost/ws/geri/");


Bu kodda `HTTP` yerine `WS` protokolünü kullandığıza ve nasıl kullanıldığına 
dikkat edelim: Normalde `http` yazdığımız yere `ws` yazdık.

Şimdi mesaj geldiğinde çalışacak olan `onmessage` fonksiyonumuzu yazalım. 
Bizim Python'da yaptığımız gibi nesnenin devamına `.` koyup `on_message` 
ekleyerek tanımlayacağız. Javascript'te fonksiyon tanımlarken `function` deyimi 
kullanılıyor. Parametreler `function` deyiminden hemen sonra parantez içinde 
tanımlanıyor. Fonksiyon ile ilgili kodlar küme parantezleri içinde yine `;` 
kullanarak yazılıyor.

Yazdığımız fonksiyon gelen mesajları konsolumuzda yazdırsın. Konsolda yazdırmak 
istediğimiz yazıları `console.log` fonksiyonuna parametre olarak veriyoruz.

.. code-block ::

    ws.onmessage = function(mesaj){console.log(mesaj)}

Tornado'da mesaj yollamak için `write_message` metodunu kullanmıştık. 
Javascript'te ise `send` metodunu kullanacağız. 
