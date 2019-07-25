.. meta::
   :description: Bu bölümde sched modülünü inceleyeceğiz.
   :keywords: python, modül, import, sched, zamanlı işlemler

.. highlight:: python3

************
sched modülü
************

Bu modülün amacı belirli fonksiyonları sırayla çalıştırmaktır.
Modülün içinde scheduler diye bir sınıf mevcut.
(Sınıfın adı dikkat ettiyseniz küçük harfle başlıyor.)
Bu modülü kullanmadan önce `scheduler` sınıfından bir örnek
oluşturmalısınız::

    import sched
    s=sched.scheduler()

Örneğimizi bu şekilde oluşturabiliriz. Ancak bu şekilde
oluşturmamız bize daha sonra sorun teşkil edebilir.
Bu sınıfın iki tane parametresi var. Bunlardan ilki: `timefunc`.
Bu parametrenin varsayılan değeri `time.monotonic`. Örnek oluşturulurken
bu parametreyi `time.time` olarak ayarlayalım. Bunun sebebini
birazdan açıklayacağım. İkinci ve son parametre ise `delayfunc`.
Bu parametrenin varsayılan değeri `time.sleep`. Bu parametreyi de
kodun okunaklılığı açısından belirtelim. Sonuç olarak örneğimizi
şu şekilde tanımlayalım::

    import sched, time
    s=sched.scheduler(time.time, time.sleep)

Şimdi sıra bu örneğin metodlarında.

scheduler.enter()
******************

Bu metod çalıştırılacak fonksiyonların sıraya eklenmesini sağlıyor.
5 tane parametresi var. İlki bekleme süresini belirliyor.
İkincisi önceliğini belirliyor. Eğer aynı zamanda çalışacak
fonksiyonlar varsa önceliğine göre çalıştırılır. Üçüncüsü
çalışacak fonksiyon. Diğer ikisi isimli parametre. Bunlardan
`argument` olan eğer varsa demet olarak fonksiyonun parametrelerini alıyor.
Diğerinin adı da tahmin edeceğiniz üzere `kwargs`. Değeri de
sözlük olarak fonksiyonun isimli parametreleri.

`scheduler` sınıfının `delayfunc` parametresi burada kullanılıyor.

scheduler.enterabs()
********************

Bu metod `enter` metodundan çok da farklı değil. Tek farkı ilk
değeri bekleme süresini değil çalışacağı süreyi belirliyor.

`scheduler` sınıfının `timefunc` parametresi burada kullanılıyor.

scheduler.cancel()
******************

`enter` veya `enterabs` ile sıraya eklenmiş fonksiyonları
sıradan çıkarmayı sağlıyor.

scheduler.empty()
*****************

Eğer sırada herhangi bir fonksiyon yoksa `True` döndürür.
Eğer fonksiyon varsa `False` döndürür.

scheduler.run()
***************

Sıradaki fonksiyonları hazırlandığı şekilde çalıştırır.
Tek parametresi olan `blocking` eğer `False` ise ilk çalışacak
fonksiyonun çalışmasına kalan süreyi döndürür.

scheduler.queue
****************

Bu değişken `scheduler` nesnelerinin sahip olduğu ve bizim
kullanabileceğimiz tek değişken. Daha önce sıraya eklenmiş
`Event` nesnelerini tutuyor.

Örnekler
********

Anlatım biraz kafa karıştırıcı oldu. Ancak şimdi birkaç
Örnek yaparak mantığını kavramanızı sağlayalım.
::

    >>> import sched,time
    >>> s=sched.scheduler(time.time,time.sleep)
    >>> def zamanı_yazdır(sıra):
        print(f"Zaman: {time.time()} ,{sıra}")

    >>> def farklı_zamanları_yazdır():
        print(time.time())
        s.enter(10,1,zamanı_yazdır,argument=("Birinci",))
        s.enter(5,1,zamanı_yazdır,argument=("İkinci",))
        s.enter(5,2,zamanı_yazdır,argument=("Üçüncü",))
        s.enter(5,1,zamanı_yazdır,argument=("Dördüncü",))
        s.run()
        print(time.time())

    >>> farklı_zamanları_yazdır()
    1532176259.627274
    Zaman: 1532176264.6953058 ,İkinci
    Zaman: 1532176264.6953058 ,Dördüncü
    Zaman: 1532176264.6953058 ,Üçüncü
    Zaman: 1532176269.6955397 ,Birinci
    1532176269.7111597

Çalışmaya başladıktan 5 saniye sonra "İkinci", "Üçüncü" ve "Dördüncü"
çalıştı. "İkinci" ve "Dördüncü"nün sırası aynıydı. O yüzden
tanımlanma sıralarına bakıldı. "Üçüncü"nün öncelik sırası
2 olduğu için onlardan daha sonra yazıldı. "Birinci" onlardan 5
saniye sonra yani çalışmaya başladıktan 10 saniye sonra çalıştı.

Bir başka örnek::

    import sched,time
    s=sched.scheduler(time.time,time.sleep)
    yazdırılacak_değer="Merhaba Dünya"
    def değiştir():
        global yazdırılacak_değer
        yazdırılacak_değer="Merhaba Zalim Dünya"

    def yazdır():
        print(yazdırılacak_değer)

    suan=time.time()
    if(s.empty()):
        s.enterabs(suan+5,1,yazdır)
        s.enterabs(suan+6,2,değiştir)
        s.enterabs(suan+6,1,yazdır)
        s.enter(10,1,yazdır)
    s.run()

`if` bloğunda eğer sıra boşsa çalışmasını söyledik.
Sıra boş olduğu için altındaki fonksiyonlar çalışacaktır.
İlk önce 5 saniye sonra bir kere `yazdır` fonksiyonu çalışacaktır.
Daha sonra çalışmaya başladıktan 6 saniye sonra ikinci
`yazdır` fonksiyonu çalışacaktır. Çıktısı ilkiyle aynı olur.
Ancak hemen sonra çalışan `değiştir` fonksiyonu ile `yazdırılacak_değer`
değiştiği için 10. saniyede çalışan `yazdır` fonksiyonu
farklı bir çıktı veriyor.

Şu şekilde fantastik bir döngü oluşturulabilir::

    import sched,time
    s=sched.scheduler(time.time,time.sleep)
    suan=time.time()
    def çıktı():
        global suan
        suan+=2
        print(suan)
        s.enterabs(suan,1,çıktı)

    s.enter(5,1,çıktı)
    s.run()

Her iki saniyede bir aynı kod çalışacaktır.
Eğer `2`'yi değiştirirseniz süreyi de düzenlemiş olursunuz.
