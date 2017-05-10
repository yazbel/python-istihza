.. meta::
   :description: Bu bölümde datetime modülünü inceleyeceğiz. 
   :keywords: python, modül, import, datetime

.. highlight:: py3

datetime Modülü
*****************

Bu bölümde, zaman, saat ve tarihlerle ilgili işlemler yapmamızı sağlayan
önemli bir standart kütüphane modülünden söz edeceğiz. Bu modülün adı
``datetime``.

``datetime`` modülü; zaman, saat ve tarihlerle ilgili işlemler yapabilmemiz
için bize çeşitli fonksiyon ve nitelikler sunan bazı sınıflardan oluşur. Bu
modül içinde temel olarak üç farklı sınıf bulunur. 

.. note:: 'Sınıf' kavramına çok takılmayın. İlerleyen derslerde sınıflardan
    ayrıntılı olarak söz edeceğiz.

``datetime`` modülü içinde yer alan bu üç sınıf şunlardır:

#. `date` sınıfı; tarihle ilgili işlemler yapabilmemizi sağlayan fonksiyon ve nitelikleri barındırır.
#. `time` sınıfı; zamanla/saatle ilgili işlemler yapabilmemizi sağlayan fonksiyon ve nitelikleri barındırır.
#. `datetime` sınıfı; `date` ve `time` sınıflarının birleşiminden ve ilave birkaç nitelik ve fonksiyondan oluşur.

Buna göre, `datetime` adlı sınıf hem `date` sınıfını hem de `time` sınıfını
kapsadığı için, ``datetime`` modülü ile işlem yapmak istediğinizde, çoğunlukla
yalnızca `datetime` sınıfını kullanarak bütün işlerinizi halledebilirsiniz.

Dolayısıyla::
    
    >>> from datetime import datetime
    
Komutunu vererek ``datetime`` modülü içindeki `datetime` adlı sınıfı içe
aktarmayı tercih edebilirsiniz.

Bakalım ``datetime`` modülünün `datetime` sınıfı içinde neler varmış::
    
    >>> dir(datetime)
        
    ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
    '__forma t__', '__ge__', '__getattribute__', '__gt__', '__hash__',
    '__init__', '__le__', '__lt__', '__ne__', '__new__', '__radd__',
    '__reduce__', '__reduce_ex__', '__rep r__', '__rsub__', '__setattr__',
    '__sizeof__', '__str__', '__sub__', '__subclass hook__', 'astimezone',
    'combine', 'ctime', 'date', 'day', 'dst', 'fromordinal', 'fromtimestamp',
    'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond',
    'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 
    'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today',
    'toord inal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset',
    'utctimetuple', 'weekday', 'year']

Elbette, eğer isterseniz doğrudan ``datetime`` modülünü de içe
aktarabilirsiniz::
    
    >>> import datetime
    
Bu durumda, ``datetime`` modülü içindeki `datetime` sınıfına erişmek için modül
adını da kullanmanız gerekir::
    
    >>> dir(datetime.datetime)
 
İşte biz bu bölümde, yukarıdaki komutun çıktısında gördüğümüz nitelik ve
fonksiyonlar arasından en önemli olanlarını inceleyeceğiz.

now()
=======

``datetime`` modülünün içindeki `datetime` sınıfının ``now()`` adlı fonksiyonu,
bize içindeki bulunduğumuz andaki tarih, saat ve zaman bilgilerini verir.
``datetime`` modülünü ``import datetime`` şeklinde içe aktardığımızı varsayarsak
bunu şu şekilde kullanıyoruz::
    
    >>> an = datetime.datetime.now()
    
Bu fonksiyon bize `datetime.datetime` adlı özel bir sınıf nesnesi verir::
    
    >>> an

    datetime.datetime(2014, 12, 5, 9, 54, 53, 867108)
    
Bu özel sınıfın da kendine özgü birtakım nitelikleri bulunur.

Mesela `year` adlı niteliği kullanarak içinde bulunduğumuz yılı
sorgulayabiliriz::
    
    >>> an.year
    
    2014
    
Aynı şekilde aşağıdaki nitelikler de, içinde bulunduğumuz ana ilişkin çeşitli
bilgiler verir::

    >>> an.month #ay
    
    12
    
    >>> an.day #gün
    
    5
    
    >>> an.hour #saat
    
    10
    
    >>> an.minute #dakika
    
    20
    
    >>> an.second #saniye
    
    33
    
    >>> an.microsecond #mikrosaniye
    
    337309

today()
=======

Bu fonksiyon ``now()`` ile aynı içeriğe ve işleve sahiptir. ``today()``
fonksiyonunu ``now`` fonksiyonunu kullandığınız gibi kullanabilirsiniz::

    >>> bugün = datetime.datetime.today()
    
    >>> bugün.year
    
    2014
    
    >>> bugün.month
    
    12
    
    >>> bugün.minute
    
    35
    
    >>> bugün.second
    
    24
    
    >>> bugün.microsecond
    
    669774

ctime()
========

``ctime()`` fonksiyonu, içinde bulunduğumuz ana ilişkin tarih ve zaman
bilgilerini içeren okunaklı bir karakter dizisi verir. Bu fonksiyona, parametre
olarak biraz önce oluşturduğumuza benzer bir `datetime.datetime` sınıfı vermemiz
gerekir. Yani::
    
    >>> an = datetime.datetime.now()
    >>> tarih = datetime.datetime.ctime(an)  
    >>> tarih

    'Fri Dec  5 10:30:35 2014'
    
Bu fonksiyon tarihleri İngilizce olarak gösterir. Yukarıdaki çıktıya göre tarih
5 Aralık Cuma 2014 saat 10:30:35.

strftime()
============

``strftime()`` fonksiyonu, size tarih ve zaman bilgilerini ihtiyaçlarınız
doğrultusunda biçimlendirme imkanı sunar. 

Bu fonksiyon toplam iki parametre alır. İlk parametre, tıpkı ``ctime()``
fonksiyonunda olduğu gibi, bir `datetime.datetime` sınıfıdır. İkinci parametre
ise, tarih/zaman bilgisini içeren karakter dizisini nasıl biçimlendirmek
istediğimizi gösteren bir biçimlendiricidir. Yani::
    
    >>> an = datetime.datetime.now()
    >>> tarih = datetime.datetime.strftime(an, '%c')
    >>> tarih
    
    'Fri 05 Dec 2014 12:53:21 PM '
    
Burada ilk parametre olarak `an` değişkeninin tuttuğu `datetime.datetime`
sınıfını, ikinci parametre olarak ise ``%c`` adlı biçimlendiriciyi kullandık. 

``%c`` dışında başka tarih biçimlendiricileri de bulunur:

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

Yukarıdaki biçimlendiricilerle ilgili birkaç örnek verelim::
    
    >>> datetime.datetime.strftime(an, '%Y') # Yıl

    '2014'
    
    >>> datetime.datetime.strftime(an, %'X') # Saat

    '12:26:32'
    
    >>> datetime.datetime.strftime(an, '%d') # Gün
    
    '05'
    
``strftime()`` fonksiyonu öntanımlı olarak İngilizce çıktı verecektir::
    
    >>> datetime.datetime.strftime(an, '%A')
    
    'Friday'
    
    >>> datetime.datetime.strftime(an, '%B')
    
    'December'
    
Eğer isterseniz, ``locale`` adlı başka bir modülü kullanarak, ``strftime()``
modülünün, sisteminizdeki tanımlı dili kullanmasını sağlayabilirsiniz.

Bunun için öncelikle ``locale`` modülünü içe aktaralım::
    
    >>> import locale
    
Ardından Python'ın kullanmasını istediğimiz yerel/dil bilgisini, sistemdeki
öntanımlı yerel/dil olarak ayarlayalım::
    
    >>> locale.setlocale(locale.LC_ALL, '')
    
    'Turkish_Turkey.1254'
    
Bu çıktı bize sistemimizdeki tanımlı dilin/yerelin Türkçe olduğunu söylüyor.
Bu komutu verdikten sonra, artık ``strftime()`` fonksiyonu, ilgili dile/yerele
uygun bir çıktı verecektir::
    
    >>> datetime.datetime.strftime(an, '%B')
    
    'Aralık'
    
    >>> datetime.datetime.strftime(an, '%A')
    
    'Cuma'
    
Eğer isterseniz, dili kendiniz de seçebilirsiniz. Mesela İtalyanca yapalım::
    
    >>> locale.setlocale(locale.LC_ALL, 'italian')

    'Italian_Italy.1252'

    >>> datetime.datetime.strftime(an, '%B')

    'dicembre'
    
    >>> datetime.datetime.strftime(an, '%A')
    
    'venerdì'
    
.. seealso:: Yerel dil adları için Windows'ta
    http://msdn.microsoft.com/en-us/library/39cwe7zf%28vs.71%29.aspx adresine
    bakabilirsiniz. GNU/Linux'ta ise, desteklenen yerel/dil adlarını görmek için
    sistem komut satırında ``locale - a`` komutunu verebilirsiniz.
    
Yukarıda gördüğünüz tarih biçimlendiricileri kullanarak istediğiniz
karmaşıklıktaki tarihleri oluşturabilirsiniz. Mesela::
    
    >>> datetime.datetime.strftime(an, '%d %B %Y')
    
    '05 Aralık 2014'
    
Veya:

    >>> datetime.datetime.strftime(an, '%d.%m.%Y tarihinde buluşalım.')
    
    '05.12.2014 tarihinde buluşalım.'
    
Gördüğünüz gibi, ``strftime()`` fonksiyonu, tarihler üzerinde istediğimiz
karakter dizisi biçimlendirme işlemini uygulayabilmemizi sağlıyor.
    
strptime()
==============

Diyelim ki elimizde, herhangi bir kaynaktan gelmiş şöyle bir karakter dizisi
var::
    
    >>> t = '27 Mayıs 2014'
    
Amacımız, tarih bilgisi içeren bu karakter dizisini gün, ay ve yıl öğelerine
ayırmak. Bunun için basitçe şöyle bir kod yazabiliriz::
    
    >>> gün, ay, yıl = t.split()
    >>> gün
    
    '27'
    
    >>> ay
    
    'Mayıs'
    
    >>> yıl
    
    '2014'
    
Peki eğer elimizdeki karakter dizisi şöyle bir şeyse ne yapacağız?

    >>> t = '27 Mayıs 2014 saat 12:34:44'

Bunun için de `t` değişkeni üzerine ``split()`` metodunu uyguladıktan sonra
'saat' kelimesini listeden atmayı tercih edebiliriz::
    
    >>> gün, ay, yıl, saat = [i for i in t.split() if 'saat' not in i]
    >>> gün
    
    '27'
    
    >>> ay
    
    'Mayıs'
    
    >>> yıl
    
    '2014'
    
    >>> saat
    
    '12:34:44'
    
Yukarıdaki yöntemler, tarih bilgisi içeren karakter dizilerini ayıklamak için
geçerli ve uygun olsa da epey meşakkatlidir. Üstelik bu şekilde ayıkladığımız
verilerin kullanım alanı da oldukça kısıtlı olacaktır. Mesela bu verileri
`datetime.datetime` türünde verileri bekleyen uygulamalar içinde kullanamayız. 

İşte böyle bir durumda ``strptime()`` adlı fonksiyon devreye girerek,
tarih/zaman bilgisi içeren herhangi bir karakter dizisini `datetime.datetime`
türünde bir nesneye dönüştürebilmemiz için bize bir yol sunar.

Şimdi dikkatlice bakın:

Elimizdeki karakter dizisi şu::
    
    >>> t = '27 Mayıs 2014 saat 12:34:44'
    
Şimdi bu karakter dizisini ``strptime()`` fonksiyonunu kullanarak ayıklıyoruz::
    
    >>> z = datetime.datetime.strptime(t, '%d %B %Y saat %H:%M:%S')
    
    datetime.datetime(2014, 5, 27, 0, 34, 44)
    
Gördüğünüz gibi, ``strptime()`` fonksiyonu iki parametre alıyor. İlk parametre,
ayıklamak istediğimiz, tarih-zaman bilgisi içeren karakter dizisi. İkinci
parametre ise, bu karakter dizisinin yapısını temsil eden tarih
biçimlendiricilerden oluşan başka bir karakter dizisi. Bu karakter dizisi,
``'27 Mayıs 2014 saat 12:34:44'`` adlı karakter dizisinin içindeki, tarih ve
saati gösteren kısımların her biri için bir biçimlendirici içeriyor::
    
    27      ==> %d
    Mayıs   ==> %B
    2014    ==> %Y
    12      ==> %H
    34      ==> %M
    44      ==> %S
    
Bu şekilde bir `datetime.datetime` nesnesi oluşturduktan sonra, artık bu
nesnenin öğelerine, herhangi bir `datetime.datetime` nesnesi gibi erişebiliriz::
    
    >>> z.month #ay
    
    5
    
    >>> z.day #gün
    
    27
    
    >>> z.year #yıl
    
    2014
    
    >>> z.hour #saat
    
    12
    
    >>> z.minute #dakika
    
    34
    
    >>> z.second #saniye
    
    44


fromtimestamp()
===============

Hatırlarsanız ``os`` modülünü anlatırken ``stat()`` adlı bir fonksiyondan söz
etmiştik. Bu fonksiyonun, dosyalar hakkında bilgi almamızı sağladığını
biliyorsunuz::
    
    >>> os.stat('dosya_adı')
    
Mesela bir dosyanın son değiştirilme tarihi öğrenmek için şöyle bir kod
kullanıyorduk::
    
    >>> os.stat('dosya_adı').st_mtime
    
`st_mtime` niteliği bize şuna benzer bir çıktı veriyor::
    
    1417784445.8881965
    
Bu, içinde ayrıntılı tarih bilgisi barındıran bir zaman damgasıdır (timestamp).
İşte bu zaman damgasını anlamlı bir tarih bilgisine dönüştürebilmek için
``datetime`` modülünün `datetime` sınıfı içindeki ``fromtimestamp()`` adlı
fonksiyondan yararlanacağız::
    
    >>> zaman_damgası = os.stat('dosya_adı').st_mtime
    >>> tarih = datetime.datetime.fromtimestamp(zaman_damgası)
    >>> tarih

    datetime.datetime(2014, 12, 5, 15, 0, 45, 888196)
    
Bu şekilde bir `datetime.datetime` nesnesi elde ettikten sonra artık bu nesneyi
istediğimiz şekilde manipüle edebiliriz. Mesela::
    
    >>> datetime.datetime.strftime(tarih, '%c')

    '12/05/14 15:00:45'
    
Demek ki `1417784445.8881965` zaman damgası, içinde '12/05/14 15:00:45' tarihini
barındırıyormuş.    
    
timestamp()
============

Eğer `datetime.datetime` nesnelerinden bir zaman damgası üretmek isterseniz
``timestamp()`` fonksiyonunu kullanabilirsiniz::
    
    >>> tarih = datetime.datetime.now()
    >>> zaman_damgası = datetime.datetime.timestamp(tarih)
    >>> zaman_damgası
    
    1417790594.558625
    
Eğer daha sonra bu zaman damgasını anlamlı bir tarihe dönüştürmeniz gerekirse
``fromtimestamp()`` fonksiyonunu kullanabileceğinizi biliyorsunuz::
    
    >>> tarih = datetime.datetime.fromtimestamp(zaman_damgası)
    
Tarihlerle İlgili Aritmetik İşlemler
======================================

``datetime`` modülünü kullanarak, tarihler arasında çıkarma-toplama gibi çeşitli
aritmetik işlemler de yapabilirsiniz. Bu bölümde bu işlemleri nasıl yapacağımızı
anlatacağız.

Belirli Bir Tarihi Kaydetmek
----------------------------

Python'da ``datetime`` modülünü kullanarak bugünün tarihini bir
`datetime.datetime` sınıfı olarak nasıl alabileceğimizi biliyoruz::
    
    >>> datetime.datetime.now()
    
veya::
    
    >>> datetime.datetime.today()
    
Peki biz mesela bugünün değil de, geçmişteki veya gelecekteki belirli bir tarihi
almak istersek ne yapacağız? 

Bu iş içinde yine ``datetime`` modülünün `datetime` adlı sınıfından
yararlanacağız. 

Diyelim ki 16 Şubat 2016, saat 13:45:32'yi bir `datetime` sınıfı olarak
kaydetmek istiyoruz. Bunun için şöyle bir kod kullanacağız::
    
    >>> tarih = datetime.datetime(2016, 2, 16, 13, 45, 32)
    
Gördüğünüz gibi, belirli bir tarihi bir `datetime.datetime` nesnesi olarak
kaydetmek istediğimizde `datetime` sınıfına parametre olarak sırasıyla ilgili
tarihin yıl, ay, gün, saat, dakika ve saniye kısımlarını giriyoruz. 

Bu arada, eğer isterseniz bu tarih için bir mikrosaniye de belirtebilirsiniz::
    
    >>> tarih = datetime.datetime(2016, 2, 16, 13, 45, 32, 5)
    
Böylece belirli bir tarihi bir `datetime` sınıfı olarak kaydetmiş olduk. Bu
sınıf, `datetime.datetime` nesnelerinin bütün özelliklerine sahiptir::
    
    >>> tarih.year #yıl
    
    2016
    
    >>> tarih.day #gün
    
    16
    
    >>> tarih.month #ay
    
    2

İki Tarih Arasındaki Farkı Bulmak
-----------------------------------

Size şöyle bir soru sormama izin verin: Diyelim ki bugünün tarihi 9 Aralık 2014.
Doğum tarihimizin 27 Mayıs olduğunu varsayarsak, acaba 2015 yılındaki doğum
günümüze kaç gün kaldığını nasıl bulabiliriz?

Bunun için öncelikle bugünün tarihini bir `datetime.datetime` nesnesi olarak
alalım::
    
    >>> bugün = datetime.datetime.today()
    
Şimdi de doğumgünümüze denk gelen tarihi bir `datetime.datetime` nesnesi olarak
kaydedelim::
    
    >>> doğumgünü = datetime.datetime(2015, 5, 27)
    
Şimdi de bu iki tarih arasındaki farkı bulalım::
    
    >>> fark = doğumgünü - bugün
    >>> fark
    
    datetime.timedelta(168, 34694, 719236)
    
Buradan elde ettiğimiz şey bir `timedelta` nesnesi. Bu nesne, tarihler
arasındaki farkı gün, saniye ve mikrosaniye olarak tutan özel bir veri tipidir.
Yukarıdaki çıktıdan anladığımıza göre, 27 Mayıs 2015 tarihi ile 9 Aralık 2014
tarihi arasında 168 gün, 34694 saniye ve 719236 mikrosaniye varmış...

Yukarıdaki `timedelta` nesnesinin niteliklerine şu şekilde ulaşabilirsiniz::

    >>> fark.days #gün
    
    168
    
    >>> fark.seconds #saniye
    
    34694
    
    >>> fark.microseconds #mikrosaniye
    
    719236

    
İleri Bir Tarihi Bulmak
------------------------

Diyelim ki 200 gün sonra hangi tarihte olacağımızı bulmak istiyoruz. Tıpkı bir
önceki başlıkta tartıştığımız gibi, bu isteğimizi yerine getirmek için de
`timedelta` nesnesinden yararlanacağız.

Önce bugünün tarihini bulalım::
    
    >>> bugün = datetime.datetime.today()
    
Şimdi 200 günlük farkı bir `timedelta` nesnesi olarak kaydedelim::
    
    >>> fark = datetime.timedelta(days=200)
    
Burada ``datetime`` modülünün ``timedelta()`` fonksiyonunun `days` adlı
parametresini `200` değeri ile çağırdığımıza dikkat edin. `days` adlı
parametrenin dışında, ``timedelta()`` fonksiyonu şu parametrelere de sahiptir::
    
    >>> fark = datetime.timedelta(days=200, seconds=40, microseconds=30)
    
Gördüğünüz gibi, gün dışında saniye (seconds) ve mikrosaniye (microseconds)
ayarlarını da yapabiliyoruz. Yukarıdaki belirlediğimiz `timedelta` nesnesi
doğrultusunda 200 gün, 40 saniye ve 30 mikrosaniye geleceğe gidelim::
    
    >>> gelecek = bugün + fark
    
    >>> gelecek

    datetime.datetime(2015, 6, 27, 14, 47, 32, 826771)
 
Bu tarihi anlamlı bir karakter dizisine dönüştürelim::
    
    >>> gelecek.strftime('%c')

    '27.06.2015 14:47:32'
    
Demek ki bugünden 200 gün, 40 saniye ve 30 mikrosaniye sonrası 27 Haziran 2015,
saat 14:47:32'ye denk geliyormuş...

Geçmiş Bir Tarihi Bulmak
-------------------------

Geçmiş bir tarihi bulmak da, tahmin edebileceğiniz gibi, ileri bir tarihi
bulmaya çok benzer. Basit bir örnek verelim::
    
    >>> bugün = datetime.datetime.today()
    
Bugünden 200 gün geriye gidelim::
    
    >>> fark = datetime.timedelta(days=200)
    >>> geçmiş = bugün - fark
    >>> geçmiş
    
    datetime.datetime(2014, 5, 23, 15, 5, 11, 487643)

    >>> geçmiş.strftime('%c')
    
    '23.05.2014 15:05:11'
    
Demek ki 200 gün öncesi 23 Mayıs 2014 imiş... 
