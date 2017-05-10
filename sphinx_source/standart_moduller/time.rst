.. meta::
   :description: Bu bölümde time modülünü inceleyeceğiz. 
   :keywords: python, modül, import, time

.. highlight:: py3

time Modülü
*****************

``time`` modülü, bir önceki bölümde öğrendiğimiz ``datetime`` modülüne benzer.
Hatta bu iki modülün aynı işi yapan ortak nitelik ve fonksiyonları vardır.
Ancak ``datetime`` modülünden farklı olarak ``time`` modülünü daha çok saatle
ilgili işlemleri yapmak için kullanacağız. 

Her zaman olduğu gibi, bu modülü kullanabilmek için de öncelikle modülü içe
aktarmamız gerekiyor::
    
    >>> import time
    
Modülü içe aktardığımıza göre, artık modülün içeriğinden yararlanabiliriz. 

gmtime()
=========

Python'da (ve başka programlama dillerinde), zaman-tarih hesaplamalarında
'zamanın başlangıcı' (EPOCH) diye bir kavram bulunur. 'Zamanın başlangıcı', bir
işletim sisteminin, tarih hesaplamalarında sıfır noktası olarak aldığı tarihtir.
Kullandığınız işletim sisteminin hangi tarihi 'zamanın başlangıcı' olarak kabul
ettiğini bulmak için şu komutu verebilirsiniz::
    
    >>> time.gmtime(0)
    
Buradan şu çıktıyı alıyoruz::
    
    time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, 
    tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
    
Bu, `struct_time` adlı özel bir veri tipidir. Bu veri tipi içindeki niteliklere
şu şekilde ulaşabilirsiniz::
    
    >>> epoch = time.gmtime(0)
    >>> epoch.tm_year #yıl
    
    1970
    
    >>> epoch.tm_mon #ay
    
    1
    
    >>> epoch.tm_mday #gün
    
    1
    
Demek ki zamanın başlangıcı 1 Ocak 1970 tarihi olarak alınıyormuş... İşte
bilgisayarımız, içinde bulunduğumuz zaman ve saati, bu başlangıç zamanından bu
yana geçen saniyeleri hesaplayarak bulur.

``gmtime()`` fonksiyonunu parametresiz olarak kullandığınızda, o anda içinde
bulunduğunuz tarih ve saat bilgisini elde edersiniz.

    time.struct_time(tm_year=2014, tm_mon=12, tm_mday=10, 
    tm_hour=12, tm_min=5, tm_sec=33, tm_wday=2, tm_yday=344, 
    tm_isdst=0)
    
Ancak bu çıktı, özellikle saat kısmı konusunda her zaman doğru olmayabilir.
Çıktının birkaç saat saptığını görebilirsiniz.

time()
=======

``time()`` fonksiyonu, zamanın başlangıcından, o anda içinde bulunduğumuz ana
kadar geçen toplam saniye miktarını verir::
    
    >>> time.time()
    
    1418213083.726988
    
Elde ettiğiniz bu değeri, ``gmtime()`` fonksiyonunu kullanarak anlamlı bir tarih
değerine dönüştürebilirsiniz::
    
    >>> time.gmtime(time.time())

    time.struct_time(tm_year=2014, tm_mon=12, tm_mday=10, 
    tm_hour=12, tm_min=9, tm_sec=19, tm_wday=2, tm_yday=344, 
    tm_isdst=0)
    
Ancak bu çıktı da özellikle saat kısmında sapmalara uğrayabilir.

localtime()
==============

Tıpkı ``gmtime()`` fonksiyonundan olduğu gibi, anlık tarih ve zaman bilgisini
bir `struct_time` nesnesi olarak almak için ``localtime()`` fonksiyonunu da
kullanabiliriz. Bu fonksiyon bize yerel saati doğru bir şekilde verecektir::

    >>> time.localtime()
    
    time.struct_time(tm_year=2014, tm_mon=12, tm_mday=10, 
    tm_hour=14, tm_min=24, tm_sec=21, tm_wday=2, tm_yday=344, tm_isdst=0)
    
Bu nesnenin içindeki yıl, ay ve gün gibi bilgilere tek tek nasıl
erişebileceğinizi biliyorsunuz.

asctime()
==========

Başta da söylediğimiz gibi, ``time`` modülü, ``datetime`` modülüne benzer.
Bunların aynı işi gören çeşitli fonksiyonları vardır. Bir örnek verelim.

Hatırlarsanız, bugünün tarihini bir karakter dizisi olarak almak için
``datetime`` modülünü şu şekilde kullanabiliyorduk::
    
    >>> import datetime
    >>> an = datetime.datetime.now()
    >>> datetime.datetime.ctime(an)
    
    'Wed Dec 10 13:56:22 2014'
    
Yukarıdaki işlemi ``time`` modülünün ``asctime()`` fonksiyonunu kullanarak da
yapabiliriz::
    
    >>> import time
    >>> time.asctime()
    
    'Wed Dec 10 13:58:31 2014'  
    
``asctime()`` fonksiyonu tercihe bağlı bir parametre de alabilir. İsterseniz bu
fonksiyona 9 öğeli bir demet veya bir `struct_time` nesnesi verebilirsiniz.

Yukarıda, ``gmtime()`` fonksiyonunun bir `struct_time` nesnesi ürettiğini
öğrenmiştik. Dolayısıyla bu nesneyi ``asctime()`` fonksiyonuna parametre olarak
verebilirsiniz::
    
    >>> time.asctime(time.gmtime())
    
    'Wed Dec 10 12:14:29 2014'
    
    >>> time.asctime(time.gmtime(0))
    
    'Thu Jan  1 00:00:00 1970'
    
Aynı şekilde ``localtime()`` fonksiyonunun da bize bir `struct_time()` nesnesi
verdiğini biliyoruz. Dolayısıyla bu fonksiyon da ``asctime()`` fonksiyonuna
parametre olarak verilebilir::
    
    >>> time.asctime(time.localtime())
    
    'Wed Dec 10 14:28:05 2014'
    
Veya, sırasıyla yıl, ay, gün, saat, dakika, saniye, haftanın günü, yılın günü,
gün ışığından yararlanma durumu değerini içeren bir demet de
oluşturabilir, daha sonra bunu ``asctime()`` fonksiyonuna parametre olarak
verebilirsiniz::
    
    >>> demet = (2014, 5, 27, 13, 45, 23, 0, 0, 0)
    >>> time.asctime(demet)
    
Ancak özellikle haftanın günü, yılın günü ve gün ışığından yararlanma durumu
bilgilerini doğru tahmin etmek zor olduğu için, bu demeti elle oluşturmanızı pek
tavsiye etmem. 

strftime()
============

Hatırlarsanız ``datetime`` modülünü anlatırken, `datetime` sınıfı içindeki
``strftime()`` adlı bir fonksiyondan söz etmiştik. Bu fonksiyonun, tarih-saat
bilgisi içeren karakter dizilerini manipüle edebilmemizi sağladığını
biliyorsunuz. 

Bu fonksiyonu şöyle kullanıyorduk::
    
    >>> import datetime
    >>> an = datetime.datetime.now()
    >>> datetime.datetime.strftime(an, '%c')
    
    '10.12.2014 14:57:48'
    
İşte yukarıdaki işlemi, ``time`` modülünün ``strftime()`` fonksiyonunu
kullanarak biraz daha pratik bir şekilde gerçekleştirebiliriz::
    
    >>> import time
    >>> time.strftime('%c')
    
    '10.12.2014 14:58:02'
    
``datetime`` modülünü incelerken gördüğümüz tarih biçimlendiricileri ``time``
modülü için de geçerlidir:

:``%a``: hafta gününün kısaltılmış adı
:``%A``: hafta gününün tam adı
:``%b``: ayın kısaltılmış adı
:``%B``: ayın tam adı
:``%c``: tam tarih, saat ve zaman bilgisi
:``%d``: sayı değerli bir karakter dizisi olarak gün
:``%j``: belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı 
:``%m``: sayı değerli bir karakter dizisi olarak ay
:``%U``: belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
:``%y``: yılın son iki rakamı
:``%Y``: yılın dört haneli tam hali
:``%x``: tam tarih bilgisi
:``%X``: tam saat bilgisi

.. warning:: Sistem yerelinin ``locale`` modülü aracılığıyla Türkçeye ayarlanmış
    olması gerektiğini unutmuyoruz::
        
        import locale
        locale.setlocale(locale.LC_ALL, 'turkish')
    
    
strptime()
==========

``time`` modülünün ``strptime()`` fonksiyonunun yaptığı iş, ``datetime``
modülünün `datetime` sınıfının ``strptime()`` fonksiyonunun yaptığı işe çok
benzer::
    
    >>> import datetime
    >>> t = '27 Mayıs 1980'
    >>> tarih = datetime.datetime.strptime(t, '%d %B %Y')
    >>> tarih
    
    datetime.datetime(1980, 5, 27, 0, 0)
    
Burada '27 Mayıs 1980' tarihini, ``strptime()`` fonksiyonu yardımıyla bir
`datetime` nesnesine dönüştürdük. Aynı şeyi şu şekilde de yapabiliriz::
    
    >>> import time
    >>> t = '27 Mayıs 1980'
    >>> tarih = time.strptime(t, '%d %B %Y')
    >>> tarih
    
    time.struct_time(tm_year=1980, tm_mon=5, tm_mday=27, 
    tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=148, 
    tm_isdst=-1)

Gördüğünüz gibi, ``time`` modülünün ``strptime()`` fonksiyonu ``datetime``
modülü içindeki ``strptime()`` fonksiyonunun aksine bir `struct_time` nesnesi
veriyor.
    
sleep()
=========

``sleep()`` fonksiyonu, ``time`` modülünün en sık kullanılan araçlarından bir
tanesidir. Bu fonksiyonu kullanarak kodlarımızın işleyişini belli sürelerle
kesintiye uğratabiliriz.

Basit bir örnek verelim::
    
    >>> for i in range(10):
    ...     time.sleep(1)
    ...     print(i)
    
Bu kodları çalıştırdığınızda, 0'dan 10'a kadar olan sayılar ekrana basılırken
her bir sayı arasına 1'er saniyelik duraklamalar eklendiğini göreceksiniz. Eğer
arzu ederseniz bu süreyi 1 saniyenin de altına çekebilirsiniz::
    
    >>> for i in range(10):
    ...     time.sleep(0.5)
    ...     print(i)
    
Gördüğünüz gibi, ``sleep()`` fonksiyonuna `0.5` parametresini vererek, duraklama
süresinin 500 milisaniye olmasını sağladık. 

``time`` modülünün ``sleep()`` fonksiyonunu, kodlarınız arasına duraklama
eklemek istediğiniz her durumda kullanabilirsiniz.