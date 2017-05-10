.. meta::
   :description: Python 3.x'te karakter dizileri
   :keywords: python, string, karakter dizisi, metotlar

.. highlight:: py3

*******************************
Karakter Dizilerinin Metotları
*******************************

Geçen bölümde karakter dizilerinin genel özelliklerinden söz ettik. Bu ikinci
bölümde ise karakter dizilerini biraz daha ayrıntılı bir şekilde incelemeye ve
karakter dizilerinin yepyeni özelliklerini görmeye başlayacağız.

Hatırlarsanız, geçen bölümün en başında, metot diye bir şeyden söz edeceğimizi
söylemiştik. Orada da kabaca tarif ettiğimiz gibi, metotlar Python'da nesnelerin
niteliklerini değiştirmemizi, sorgulamamızı veya bu nesnelere yeni özellikler
katmamızı sağlayan araçlardır. Metotlar sayesinde karakter dizilerini
istediğimiz gibi eğip bükebileceğiz.

Geçen bölümün sonlarına doğru, bir karakter dizisinin hangi metotlara sahip
olduğunu şu komut yardımıyla listeleyebileceğimizi öğrenmiştik::
    
    >>> dir("")

Bu komutu verdiğinizde aldığınız çıktıdan da gördüğünüz gibi, karakter
dizilerinin `40`'ın üzerinde metodu var. Dolayısıyla metot sayısının çokluğu
gözünüzü korkutmuş olabilir. Ama aslında buna hiç lüzum yok. Çünkü programcılık
maceranızda bu metotların bazılarını ya çok nadiren kullanacaksınız, ya da hiç
kullanmayacaksınız. Çok kullanılan metotlar belli başlıdır. Elbette bütün
metotlar hakkında fikir sahibi olmak gerekir. Zaten siz de göreceksiniz ki, bu
metotlar kullandıkça aklınızda kalacak. Doğal olarak çok kullandığınız metotları
daha kolay öğreneceksiniz. Eğer bir program yazarken hangi metodu kullanmanız
gerektiğini veya kullanacağınız metodun ismini hatırlayamazsanız etkileşimli
kabukta ``dir("")`` gibi bir komut verip çıkan sonucu incelemek pek zor olmasa
gerek. Ayrıca hatırlayamadığınız bir metot olması durumunda dönüp bu sayfaları
tekrar gözden geçirme imkanına da sahipsiniz. Unutmayın, bütün metotları ve bu
metotların nasıl kullanıldığını ezbere bilmeniz zaten beklenmiyor. Metotları
hatırlayamamanız gayet normal. Böyle bir durumda referans kitaplarına bakmak en
doğal hakkınız.

replace()
==============

Karakter dizisi metotları arasında inceleyeceğimiz ilk metot ``replace()``
metodu olacak. *replace* kelimesi Türkçede 'değiştirmek, yerine koymak' gibi
anlamlar taşır. İşte bu metodun yerine getirdiği görev de tam olarak budur. Yani
bu metodu kullanarak bir karakter dizisi içindeki karakterleri başka
karakterlerle değiştirebileceğiz.

Peki bu metodu nasıl kullanacağız? Hemen bir örnek verelim::

    >>> kardiz = "elma"

Burada `"elma"` değerini taşıyan `kardiz` adlı bir karakter dizisi tanımladık.
Şimdi bu karakter dizisinin içinde geçen `"e"` harfini `"E"` ile değiştirelim.
Dikkatlice bakın::
    
    >>> kardiz.replace("e", "E")
    
    'Elma'

Gördüğünüz gibi, ``replace()`` son derece yararlı ve kullanımı oldukça kolay bir
metot. Bu arada bu ilk metodumuz sayesinde Python'daki metotların nasıl
kullanılacağı konusunda da bilgi edinmiş olduk. Yukarıdaki örneklerin bize
gösterdiği gibi şöyle bir formülle karşı karşıyayız::
    
    karakter_dizisi.metot(parametre)

Metotlar karakter dizilerinden nokta ile ayrılır. Python'da bu yönteme 'noktalı
gösterim' (*dot notation*) adı verilir.

Bu arada metotların görünüş ve kullanım olarak fonksiyonlara ne kadar
benzediğine dikkat edin. Tıpkı fonksiyonlarda olduğu gibi, metotlar da birtakım
parametreler alabiliyor. 

Yukarıdaki örnekte, ``replace()`` metodunun iki farklı parametre aldığını
görüyoruz. Bu metoda verdiğimiz ilk parametre değiştirmek istediğimiz karakter
dizisini gösteriyor. İkinci parametre ise birinci parametrede belirlediğimiz
karakter dizisinin yerine ne koyacağımızı belirtiyor. Yani ``replace()`` metodu
şöyle bir formüle sahiptir::
    
    karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)

Gelin isterseniz elimizin alışması için ``replace()`` metoduyla birkaç örnek
daha verelim::
    
    >>> kardiz = "memleket"
    >>> kardiz.replace("ket", "KET")
    
    'memleKET'

Burada gördüğünüz gibi, ``replace()`` metodu aynı anda birden fazla karakteri
değiştirme yeteneğine de sahip.

``replace()`` metodunun iki parametreden oluştuğunu, ilk parametrenin
değiştirilecek karakter dizisini, ikinci parametrenin ise ilk karakter dizisinin
yerine geçecek yeni karakter dizisini gösterdiğini söylemiştik. Aslında
``replace()`` metodu üçüncü bir parametre daha alır. Bu parametre ise bir
karakter dizisi içindeki karakterlerin kaç tanesinin değiştirileceğini gösterir.
Eğer bu parametreyi belirtmezsek ``replace()`` metodu ilgili karakterlerin
tamamını değiştirir. Yani::
    
    >>> kardiz = "memleket"
    
    >>> kardiz.replace("e", "")
    
    'mmlkt'
    
Gördüğünüz gibi, ``replace()`` metodunu iki parametre ile kullanıp üçüncü
parametreyi belirtmediğimizde, `"memleket"` kelimesi içindeki bütün `"e"`
harfleri boş karakter dizisi ile değiştiriliyor (yani bir anlamda siliniyor).

Şimdi şu örneğe bakalım::

    >>> kardiz.replace("e", "", 1)
    
    'mmleket'

Burada ``replace()`` metodunu üçüncü bir parametre ile birlikte kullandık.
Üçüncü parametre olarak `1` sayısını verdiğimiz için ``replace()`` metodu sadece
tek bir `"e"` harfini sildi.

Bu üçüncü parametreyi, silmek istediğiniz harf sayısı kadar artırabilirsiniz.
Mesela::
    
    >>> kardiz.replace("e", "", 2)
    
    'mmlket'
    
    >>> kardiz.replace("e", "", 3)
    
    'mmlkt'

Burada ilk örnekte üçüncü parametre olarak `2` sayısını kullandığımız için,
'replace' işleminden karakter dizisi içindeki `2` adet `"e"` harfi etkilendi.
Üçüncü örnekte ise `"memleket"` adlı karakter dizisi içinde geçen üç adet `"e"`
harfi değişiklikten etkilendi.

Karakter dizileri konusunun ilk bölümünde 'değiştirilebilirlik' (*mutability*)
üzerine söylediğimiz şeylerin burada da geçerli olduğunu unutmayın. Orada da
söylediğimiz gibi, karakter dizileri değiştirilemeyen veri tipleridir.
Dolayısıyla eğer bir karakter dizisi üzerinde değişiklik yapmak istiyorsanız, o
karakter dizisini baştan tanımlamalısınız. Örneğin::
    
    >>> meyve = "elma"
    >>> meyve = meyve.replace("e", "E")
    >>> meyve
    
    'Elma'

Böylece ``replace()`` metodunu incelemiş olduk. Sırada üç önemli metot var.


split(), rsplit(), splitlines()
============================================

Şimdi size şöyle bir soru sorduğumu düşünün: Acaba aşağıdaki karakter dizisinde
yer alan bütün kelimelerin ilk harfini nasıl alırız?

::

    >>> kardiz = "İstanbul Büyükşehir Belediyesi"

Yani diyorum ki burada `"İBB"` gibi bir çıktıyı nasıl elde ederiz? 

Sadece bu karakter dizisi söz konusu ise, elbette karakter dizilerinin
dilimlenme özelliğinden yararlanarak, `kardiz` değişkeni içindeki `"İ"`, `"B"`,
ve `"B"` harflerini tek tek alabiliriz::
    
    >>> print(kardiz[0], kardiz[9], kardiz[20], sep="")
    
    İBB

Ancak bu yöntemin ne kadar kullanışsız olduğu ortada. Çünkü bu metot yalnızca
`"İstanbul Büyükşehir Belediyesi"` adlı karakter dizisi için geçerlidir. Eğer
karakter dizisi değişirse bu yöntem de çöpe gider. Bu soruna genel bir çözüm
üretebilsek ne güzel olurdu, değil mi?

İşte Python'da bu sorunu çözmemizi sağlayacak çok güzel bir metot bulunur. Bu
metodun adı ``split()``.

Bu metodun görevi karakter dizilerini belli noktalardan bölmektir. Zaten *split*
kelimesi Türkçede 'bölmek, ayırmak' gibi anlamlara gelir. İşte bu metot, üzerine
uygulandığı karakter dizilerini parçalarına ayırır. Örneğin::
    
    >>> kardiz = "İstanbul Büyükşehir Belediyesi"
    >>> kardiz.split()
    
    ['İstanbul', 'Büyükşehir', 'Belediyesi']

Gördüğünüz gibi bu metot sayesinde `"İstanbul Büyükşehir Belediyesi"` adlı
karakter dizisini kelimelere bölmeyi başardık. Eğer bu çıktı üzerine bir ``for``
döngüsü uygularsak şöyle bir sonuç elde ederiz::
    
    >>> for i in kardiz.split():
    ...     print(i)
    ...
    İstanbul
    Büyükşehir
    Belediyesi

Artık bu bilgiyi kullanarak şöyle bir program yazabiliriz::

    kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")

    for i in kardiz.split():
        print(i[0], end="")

Burada kullanıcı hangi kurum adını girerse girsin, bu kurum adının her
kelimesinin ilk harfi ekrana dökülecektir. Örneğin kullanıcı burada `"Türkiye
Büyük Millet Meclisi"` ifadesini girmişse ``split()`` metodu öncelikle bu
ifadeyi alıp şu şekle dönüştürür::
    
    ['Türkiye', 'Büyük', 'Millet', 'Meclisi']

Daha sonra biz bu çıktı üzerinde bir ``for`` döngüsü kurarsak bu kelime grubunun
her bir öğesine tek tek müdahale etme imkanına erişiriz. Örneğin yukarıdaki
programda bu kelime grubunun her bir öğesinin ilk harfini tek tek ekrana döktük
ve `"TBMM"` çıktısını elde ettik.

Yukarıdaki örneklerde ``split()`` metodunu herhangi bir parametre içermeyecek
şekilde kullandık. Yani metodun parantezleri içine herhangi bir şey eklemedik.
``split()`` metodunu bu şekilde parametresiz olarak kullandığımızda bu metot
karakter dizilerini bölerken boşluk karakterini ölçüt alacaktır. Yani karakter
dizisi içinde karşılaştığı her boşluk karakterinde bir bölme işlemi
uygulayacaktır. Ama bazen istediğimiz şey, bir karakter dizisini boşluklardan
bölmek değildir. Mesela şu örneğe bakalım::
    
    >>> kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"

Eğer bu karakter dizisi üzerine ``split()`` metodunu parametresiz olarak
uygularsak şöyle bir çıktı elde ederiz::
    
    ['Bolvadin,', 'Kilis,', 'Siverek,', 'İskenderun,', 'İstanbul']

``split()`` metoduna herhangi bir parametre vermediğimiz için bu metot karakter
dizisi içindeki kelimeleri boşluklardan böldü. Bu yüzden karakter dizisi
içindeki virgül işaretleri de bölünen kelimeler içinde görünüyor::
    
    >>> kardiz = kardiz.split()
    >>> for i in kardiz:
    ...     print(i)
    ...
    Bolvadin,
    Kilis,
    Siverek,
    İskenderun,
    İstanbul

Bu arada tıpkı ``replace()`` metodunu anlatırken gösterdiğimiz gibi,
``kardiz.split()`` ifadesini de yine `kardiz` adını taşıyan bir değişkene
atadık. Böylece ``kardiz.split()`` komutu ile elde ettiğimiz değişiklik
kaybolmamış oldu. Karakter dizilerinin değiştirilemeyen bir veri tipi olduğunu
biliyorsunuz. Dolayısıyla yukarıdaki karakter dizisi üzerine ``split()``
metodunu uyguladığımızda aslında orijinal karakter dizisi üzerinde herhangi bir
değişiklik yapmış olmuyoruz. Çıktıda görünen değişikliğin orijinal karakter
dizisini etkileyebilmesi için eski karakter dizisini silip, yerine yeni
değerleri yazmamız gerekiyor. Bunu da ``kardiz = kardiz.split()`` gibi bir
komutla hallediyoruz.

Nerede kalmıştık? Gördüğünüz gibi ``split()`` metodu parametresiz olarak
kullanıldığında karakter dizisini boşluklardan bölüyor. Ama yukarıdaki örnekte
karakter dizisini boşluklardan değil de virgüllerden bölsek çok daha anlamlı bir
çıktı elde edebiliriz.

Dikkatlice inceleyin::
    
    >>> kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
    >>> kardiz = kardiz.split(",")
    >>> print(kardiz)

    ['Bolvadin', ' Kilis', ' Siverek', ' İskenderun', ' İstanbul']
    
    >>> for i in kardiz:
    ...     print(i)
    ...
    Bolvadin
    Kilis
    Siverek
    İskenderun
    İstanbul

Gördüğünüz gibi, ``split()`` metodu tam da istediğimiz gibi, karakter dizisini
bu kez boşluklardan değil virgüllerden böldü. Peki bunu nasıl başardı? Aslında
bu sorunun cevabı gayet net bir şekilde görünüyor. Dikkat ederseniz yukarıdaki
örnekte ``split()`` metoduna parametre olarak virgül karakter dizisini verdik.
Yani şöyle bir şey yazdık::
    
    kardiz.split(",")

Bu sayede ``split()`` metodu karakter dizisini virgüllerden bölmeyi başardı.
Tahmin edebileceğiniz gibi, ``split()`` metoduna hangi parametreyi verirseniz bu
metot ilgili karakter dizisini o karakterin geçtiği yerlerden bölecektir. Yani
mesela siz bu metoda `"l"` parametresini verirseniz, bu metot da 'l' harfi geçen
yerden karakter dizisini bölecektir::
    
    >>> kardiz.split("l")
    
    ['Bo', 'vadin, Ki', 'is, Siverek, İskenderun, İstanbu', '']
    
    >>> for i in kardiz.split("l"):
    ...     print(i)
    ...
    Bo
    vadin, Ki
    is, Siverek, İskenderun, İstanbu
    
Eğer parametre olarak verdiğiniz değer karakter dizisi içinde hiç geçmiyorsa
karakter dizisi üzerinde herhangi bir değişiklik yapılmaz::
    
    >>> kardiz.split("z")
    
    ['Bolvadin, Kilis, Siverek, İskenderun, İstanbul']

Aynı şey, ``split()`` metodundan önce öğrendiğimiz ``replace()`` metodu için de
geçerlidir. Yani eğer değiştirilmek istenen karakter, karakter dizisi içinde yer
almıyorsa herhangi bir işlem yapılmaz.

``split()`` metodu çoğunlukla, yukarıda anlattığımız şekilde parametresiz olarak
veya tek parametre ile kullanılır. Ama aslında bu metot ikinci bir parametre
daha alır. Bu ikinci parametre, karakter dizisinin kaç kez bölüneceğini
belirler::
    
    >>> kardiz = "Ankara Büyükşehir Belediyesi"
    
    >>> kardiz.split(" ", 1)
    
    ['Ankara', 'Büyükşehir Belediyesi']
    
    >>> kardiz.split(" ", 2)
    
    ['Ankara', 'Büyükşehir', 'Belediyesi']

Gördüğünüz gibi, ilk örnekte kullandığımız `1` sayısı sayesinde bölme işlemi
karakter dizisi üzerine bir kez uygulandı. İkinci örnekte ise `2` sayısının
etkisiyle karakter dizimiz iki kez bölme işlemine maruz kaldı.

Elbette, ``split()`` metodunun ikinci parametresini kullanabilmek için ilk
parametreyi de mutlaka yazmanız gerekir. Aksi halde Python ne yapmaya
çalıştığınızı anlayamaz::
    
    >>> kardiz.split(2)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

Gördüğünüz gibi, ilk parametreyi es geçip doğrudan ikinci parametreyi yazmaya
çalıştığımızda Python parametre olarak verdiğimiz `2` sayısının bölme ölçütü
olduğunu zannediyor. Yukarıdaki hatayı engellemek için bölme ölçütünü de açıkça
belirtmemiz gerekir. Yukarıdaki örnekte bölme ölçütümüz bir adet boşluk
karakteri idi. Bildiğiniz gibi, bölme ölçütü herhangi bir şey olabilir. Mesela
virgül.

::

    >>> arkadaşlar = "Ahmet, Mehmet, Kezban, Mualla, Süreyya, Veli"
    >>> arkadaşlar.split(",", 3)
    
    ['Ahmet', ' Mehmet', ' Kezban', ' Mualla, Süreyya, Veli']

Burada da bölme ölçütü olarak virgül karakterini kullandık ve `arkadaşlar` adlı
karakter dizisi üzerine `3` kez bölme işlemi uyguladık. İlk bölme işlemi
`"Ahmet"` karakter dizisini; ikinci bölme işlemi `"Mehmet"` karakter dizisini;
üçüncü bölme işlemi ise `"Kezban"` karakter dizisini ayırdı. `arkadaşlar` adlı
karakter dizisinin geri kalanını oluşturan `"Mualla, Süreyya, Veli"` kısmı ise
herhangi bir bölme işlemine tabi tutulmadan tek parça olarak kaldı.

``split()`` metoduyla son bir örnek verip yolumuza devam edelim. 

Bildiğiniz gibi `sys` modülünün `version` değişkeni bize bir karakter dizisi
veriyor:

.. parsed-literal::

    |version3-string|
    
Bu karakter dizisi içinden yalnızca sürüm kısmını ayıklamak için karakter
dizilerinin dilimlenme özelliğinden yararlanabiliyoruz:

.. parsed-literal::
   
    >>> sürüm = sys.version
    >>> print(sürüm[:5])
    
    |py3|
    
Bu işlemin bir benzerini ``split()`` metoduyla da yapabiliriz. Dikkatlice
inceleyin:

.. parsed-literal::
    
    >>> sürüm = sys.version
    >>> sürüm.split()
    
    ['3.3.0', '(v3.3.0:bd8afb90ebf2,', 'Sep', '29', '2012,', '10:55:48)', 
     '[MSC', 'v.1600', '32', 'bit', '(Intel)]']
     
Gördüğünüz gibi, ``sys.version`` komutuna ``split()`` metodunu uyguladığımızda,
üzerinde işlem yapması çok daha kolay olan bir veri tipi elde ediyoruz. Bu veri
tipinin adı 'liste'. Önceki derslerimizde öğrendiğimiz ``dir()`` fonksiyonunun
da liste adlı bu veri tipini verdiğini hatırlıyor olmalısınız. İlerleyen
derslerde, tıpkı karakter dizileri ve sayılar adlı veri tipleri gibi, liste adlı
veri tipini de bütün ayrıntılarıyla inceleyeceğiz. Şimdilik biz sadece **bazı
durumlarda** liste veri tipinin karakter dizilerine kıyasla daha kullanışlı bir
veri tipi olduğunu bilelim yeter.

Yukarıdaki örnekten de gördüğünüz gibi, ``sys.version`` komutunun çıktısını
``split()`` metodu yardımıyla boşluklardan bölerek bir liste elde ettik. Bu
listenin ilk öğesi, kullandığımız Python serisinin sürüm numarasını verecektir:

.. parsed-literal::
    
    >>> print(sürüm.split()[0])
    
    |py3|

Böylece ``split()`` metodunu öğrenmiş olduk. Gelelim ``rsplit()`` metoduna...

``rsplit()`` metodu her yönüyle ``split()`` metoduna benzer. ``split()`` ile
``rsplit()`` arasındaki tek fark, ``split()`` metodunun karakter dizisini soldan
sağa, ``rsplit()`` metodunun ise sağdan sola doğru okumasıdır. Şu örnekleri
dikkatlice inceleyerek bu iki metot arasındaki farkı bariz bir şekilde
görebilirsiniz::
    
    >>> kardiz.split(" ", 1)

    ['Ankara', 'Büyükşehir Belediyesi']

    >>> kardiz.rsplit(" ", 1)

    ['Ankara Büyükşehir', 'Belediyesi']

Gördüğünüz gibi, ``split()`` metodu karakter dizisini soldan sağa doğru okuduğu
için bölme işlemini `"Ankara"` karakter dizisine uyguladı. ``rsplit()`` metodu
ise karakter dizisini sağdan sola soğru okuduğu için bölme işlemini
`"Belediyesi"` adlı karakter dizisine uyguladı.

``rsplit()`` metodunun pek yaygın kullanılan bir metot olmadığını belirterek
``splitlines()`` metoduna geçelim.

Bildiğiniz gibi, ``split()`` metodunu bir karakter dizisini kelime kelime
ayırabilmek için kullanabiliyoruz. ``splitlines()`` metodunu ise bir karakter
dizisini satır satır ayırmak için kullanabiliriz. Mesela elinizde uzun bir metin
olduğunu ve amacınızın bu metin içindeki herbir satırı ayrı ayrı almak olduğunu
düşünün. İşte ``splitlines()`` metoduyla bu amacınızı gerçekleştirebilirsiniz.
Hemen bir örnek verelim::
    
    metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı 
    tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin 
    Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını 
    düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından 
    gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz 
    komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek 
    adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama 
    dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek 
    halini almıştır diyebiliriz."""

    print(metin.splitlines())

.. highlight:: none

Bu programı çalıştırdığınızda şöyle bir çıktı alırsınız::

    ['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı ', 
    "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, 
    isminin", 'Python olmasına bakarak, bu programlama dilinin, adını piton 
    yılanından aldığını ', 'düşünür. Ancak zannedildiğinin aksine bu programlama 
    dilinin adı piton yılanından ', 'gelmez. Guido Van Rossum bu programlama 
    dilini, The Monty Python adlı bir İngiliz ', "komedi grubunun, Monty Python's 
    Flying Circus adlı gösterisinden esinlenerek ", 'adlandırmıştır. Ancak her ne 
    kadar gerçek böyle olsa da, Python programlama ', 'dilinin pek çok yerde bir 
    yılan figürü ile temsil edilmesi neredeyse bir gelenek ', 'halini almıştır 
    diyebiliriz.']

Gördüğünüz gibi, metnimiz `Enter` tuşuna bastığımız noktalardan bölündü. Biz
henüz bu çıktıyı nasıl değerlendireceğimizi ve bu çıktıdan nasıl
yararlanacağımızı bilmiyoruz. Ayrıca şu anda bu çıktı gözünüze çok anlamlı
görünmemiş olabilir. Ama 'Listeler' adlı konuyu öğrendiğimizde bu çıktı size çok
daha anlamlı görünecek.

.. highlight:: py3

``splitlines()`` metodu yukarıdaki gibi parametresiz olarak kullanılabileceği
gibi, bir adet parametre ile de kullanılabilir. Bunu bir örnek üzerinde
gösterelim::
    
    metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı 
    tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin 
    Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını 
    düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından 
    gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz 
    komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek 
    adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama 
    dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek 
    halini almıştır diyebiliriz."""

    print(metin.splitlines(True))

.. highlight:: none

Bu programı çalıştırdığımızda şuna benzer bir sonuç elde ederiz::

    ['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı \n', 
    "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, 
    isminin \n", 'Python olmasına bakarak, bu programlama dilinin, adını piton 
    yılanından aldığını \n', 'düşünür. Ancak zannedildiğinin aksine bu programlama 
    dilinin adı piton yılanından \n', 'gelmez. Guido Van Rossum bu programlama 
    dilini, The Monty Python adlı bir İngiliz \n', "komedi grubunun, Monty 
    Python's Flying Circus adlı gösterisinden esinlenerek \n", 'adlandırmıştır. 
    Ancak her ne kadar gerçek böyle olsa da, Python programlama \n', 'dilinin pek 
    çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek \n', 
    'halini almıştır diyebiliriz.']

.. highlight:: py3

Gördüğünüz gibi, parametresiz kullanımda, program çıktısında satır başı
karakterleri (`\\n`) görünmüyor. Ama eğer ``splitlines()`` metoduna parametre
olarak ``True`` verirsek program çıktısında satır başı karakterleri de
görünüyor. Yazdığınız programlarda ihtiyacınıza göre ``splitlines()`` metodunu
parametreli olarak veya parametresiz bir şekilde kullanabilirsiniz.

lower()
=============

Mutlaka karşılaşmışsınızdır. Bazı programlarda kullanıcıdan istenen veriler
büyük-küçük harfe duyarlıdır. Yani mesela kullanıcıdan bir parola isteniyorsa,
kullanıcının bu parolayı büyük-küçük harfe dikkat ederek yazması gerekir. Bu
programlar açısından, örneğin 'parola' ve 'Parola' aynı kelimeler değildir.
Mesela kullanıcının parolası 'parola' ise, bu kullanıcı programa 'Parola'
yazarak giremez.

Bazı başka programlarda ise bu durumun tam tersi söz konusudur. Yani büyük-küçük
harfe duyarlı programların aksine bazı programlar da kullanıcıdan gelen verinin
büyük harfli mi yoksa küçük harfli mi olduğunu önemsemez. Kullanıcı doğru
kelimeyi büyük harfle de yazsa, küçük harfle de yazsa program istenen işlemi
gerçekleştirir. Mesela Google'da yapılan aramalar bu mantık üzerine çalışır.
Örneğin 'kitap' kelimesini Google'da aratıyorsanız, bu kelimeyi büyük harfle de
yazsanız, küçük harfle de yazsanız Google size aynı sonuçları gösterecektir.
Google açısından, aradığınız kelimeyi büyük ya da küçük harfle yazmanızın bir
önemi yoktur.

Şimdi şöyle bir program yazdığımızı düşünün::

    kişi = input("Aradığınız kişinin adı ve soyadı: ")

    if kişi == "Ahmet Öz":
        print("email: aoz@hmail.com")
        print("tel  : 02121231212")
        print("şehir: istanbul")

    elif kişi == "Mehmet Söz":
        print("email: msoz@zmail.com")
        print("tel  : 03121231212")
        print("şehir: ankara")

    elif kişi == "Mahmut Göz":
        print("email: mgoz@jmail.com")
        print("tel  : 02161231212")
        print("şehir: istanbul")

    else:
        print("Aradığınız kişi veritabanında yok!") 

Bu programın doğru çalışabilmesi için kullanıcının, örneğin, Ahmet Öz adlı
kişiyi ararken büyük-küçük harfe dikkat etmesi gerekir. Eğer kullanıcı Ahmet Öz
yazarsa o kişiyle ilgili bilgileri alabilir, ama eğer mesela Ahmet öz yazarsa
bilgileri alamaz. Peki acaba biz bu sorunun üstesinden nasıl gelebiliriz? Yani
programımızın büyük-küçük harfe duyarlı olmamasını nasıl sağlayabiliriz?

Bu işi yapmanın iki yolu var: Birincisi ``if`` bloklarını her türlü ihtimali
düşünerek yazabiliriz. Mesela::

    if kişi == "Ahmet Öz" or "Ahmet öz" or "ahmet öz":
        ...

Ama burada bazı problemler var. Birincisi, kullanıcının kaç türlü veri
girebileceğini kestiremeyebilirsiniz. İkincisi, kestirebilseniz bile, her kişi
için olasılıkları girmeye çalışmak eziyetten başka bir şey değildir...

İşte burada imdadımıza ``lower()`` metodu yetişecek. Dikkatlice inceleyin::

    kişi = input("Aradığınız kişinin adı ve soyadı: ")
    kişi = kişi.lower()

    if kişi == "ahmet öz":
        print("email: aoz@hmail.com")
        print("tel  : 02121231212")
        print("şehir: istanbul")

    elif kişi == "mehmet söz":
        print("email: msoz@zmail.com")
        print("tel  : 03121231212")
        print("şehir: ankara")

    elif kişi == "mahmut göz":
        print("email: mgoz@jmail.com")
        print("tel  : 02161231212")
        print("şehir: istanbul")

    else:
        print("Aradığınız kişi veritabanında yok!") 

Artık kullanıcı 'ahmet öz' de yazsa, 'Ahmet Öz' de yazsa, hatta 'AhMeT öZ' de
yazsa programımız doğru çalışacaktır. Peki bu nasıl oluyor? Elbette ``lower()``
metodu sayesinde...

Yukarıdaki örneklerin de bize gösterdiği gibi, ``lower()`` metodu, karakter
dizisindeki bütün harfleri küçük harfe çeviriyor. Örneğin::

    >>> kardiz = "ELMA"
    >>> kardiz.lower()
    
    'elma'
    
    >>> kardiz = "arMuT"
    >>> kardiz.lower()
    
    'armut'
    
    >>> kardiz = "PYTHON PROGRAMLAMA"
    >>> kardiz.lower()
    
    'python programlama'

Eğer karakter dizisi zaten tamamen küçük harflerden oluşuyorsa bu metot hiçbir
işlem yapmaz::
    
    >>> kardiz = "elma"
    >>> kardiz.lower()
    
    'elma'

İşte verdiğimiz örnek programda da ``lower()`` metodunun bu özelliğinden
yararlandık. Bu metot sayesinde, kullanıcı ne tür bir kelime girerse girsin, bu
kelimeler her halükarda küçük harfe çevrileceği için, ``if`` blokları
kullanıcıdan gelen veriyi yakalayabilecektir.

Gördüğünüz gibi, son derece kolay ve kullanışlı bir metot bu. Ama bu metodun bir
problemi var. Şu örneği dikkatlice inceleyin::
    
    >>> il = "İSTANBUL"
    >>> print(il.lower())
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Python33\lib\encodings\cp857.py", line 19, in encode
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]
    UnicodeEncodeError: 'charmap' codec can't encode character '\u0307' in position
    1: character maps to <undefined>
    
Buradaki problem 'İ' harfinden kaynaklanıyor. Python programlama dili bu harfi
Türkçeye uygun bir şekilde küçültemediği için yukarıdaki hatayı alıyoruz.
Yukarıdaki hatanın tam olarak ne anlama geldiğini birkaç bölüm sonra
anlayacaksınız. Biz şimdilik sadece Python'ın 'İ' harfini Türkçeye uygun olarak
küçültemediğini bilelim yeter.

Bir de şu örneğe bakalım::
    
    >>> il = "ADIYAMAN"
    >>> print(il.lower())
    
    adiyaman

Gördüğünüz gibi, Python programlama dili 'I' harfini de düzgün küçültemiyor. 'I'
harfinin küçük biçimi 'ı' olması gerekirken, bu metot 'I' harfini 'i' diye
küçültüyor. Yani::
    
    >>> "I".lower()
    
    'i'

Peki bu durumda ne yapacağız? Elimiz kolumuz bağlı oturacak mıyız? Elbette
hayır! Biz bu tür küçük sorunları aşabilecek kadar Python bilgisine sahibiz. 'İ'
ve 'I' harfleri ile ilgili problemi, yalnızca mevcut bilgilerimizi kullanarak
rahatlıkla çözebiliriz::

    iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"

    iller = iller.replace("I", "ı").replace("İ", "i").lower()
    print(iller)
    
Bu kodlarla yaptığımız şey çok basit: 

    #. İlk ``replace()`` metoduyla karakter dizisi içinde geçen bütün 'I'
       harflerini, 'ı' ile değiştiriyoruz.
    #. İkinci ``replace()`` metoduyla karakter dizisi içinde geçen bütün 'İ'
       harflerini 'i' ile değiştiriyoruz.
    #. Bu iki işlemin ardından karakter dizisi içinde geçen 'I' ve 'İ'
       harflerini küçültmüş olduk. Ancak öteki harfler henüz küçülmedi. O yüzden de
       karakter dizimiz üzerine bir de ``lower()`` metodunu uyguluyoruz. Böylece
       bütün harfler düzgün bir şekilde küçülmüş oluyor.
    #. Bu kodlarda farklı metotları uç uca nasıl eklediğimize dikkat edin.   
    
Bu örnek size şunu göstermiş olmalı: Aslında programlama dediğimiz şey gerçekten
de çok basit parçaların uygun bir şekilde birleştirilmesinden ibaret. Tıpkı bir
yap-bozun parçalarını birleştirmek gibi...

Ayrıca bu örnek sizi bir gerçekle daha tanıştırıyor: Gördüğünüz gibi, artık
Python'da o kadar ilerlediniz ki Python'ın problemlerini tespit edip bu
problemlere çözüm dahi üretebiliyorsunuz!

upper()
===========

Bu metot biraz önce öğrendiğimiz ``lower()`` metodunun yaptığı işin tam tersini
yapar. Hatırlarsanız ``lower()`` metodu yardımıyla karakter dizileri içindeki
harfleri küçültüyorduk. ``upper()`` metodu ise bu harfleri büyütmemizi sağlar.

Örneğin::

    >>> kardiz = "kalem"
    >>> kardiz.upper()
    
    'KALEM'

``lower()`` metodunu anlatırken, kullanıcıdan gelen verileri belli bir düzene
sokmak konusunda bu metodun oldukça faydalı olduğunu söylemiştik. Kullanıcıdan
gelen verilerin ``lower()`` metodu yardımıyla standart bir hale getirilmesi
sayesinde, kullanıcının girdiği kelimelerin büyük-küçük harfli olmasının önemli
olmadığı programlar yazabiliyoruz. Elbette eğer isterseniz kullanıcıdan gelen
bütün verileri ``lower()`` metoduyla küçük harfe çevirmek yerine, ``upper()``
metoduyla büyük harfe çevirmeyi de tercih edebilirsiniz. Python programcıları
genellikle kullanıcı verilerini standart bir hale getirmek için bütün harfleri
küçültmeyi tercih eder, ama tabii ki sizin bunun tersini yapmak istemenizin
önünde hiçbir engel yok.

Diyelim ki, şehirlere göre hava durumu bilgisi veren bir program yazmak
istiyorsunuz. Bunun için şöyle bir kod yazarak işe başlayabilirsiniz::

    şehir = input("Hava durumunu öğrenmek için bir şehir adı girin: ")

    if şehir == "ADANA":
        print("parçalı bulutlu")

    elif şehir == "ERZURUM":
        print("karla karışık yağmurlu")

    elif şehir == "ANTAKYA":
        print("açık ve güneşli")

    else:
        print("Girdiğiniz şehir veritabanında yok!")

Burada programımızın doğru çalışabilmesi, kullanıcının şehir adlarını büyük
harfle girmesine bağlıdır. Örneğin programımız 'ADANA' cevabını kabul edecek,
ama mesela 'Adana' cevabını kabul etmeyecektir. Bunu engellemek için ``lower()``
metodunu kullanabileceğimizi biliyoruz. Bu sorunu çözmek için aynı şekilde
``upper()`` metodunu da kullanabiliriz::
    
    şehir = input("Hava durumunu öğrenmek için bir şehir adı girin: ")

    şehir = şehir.upper()

    if şehir == "ADANA":
        print("parçalı bulutlu")

    elif şehir == "ERZURUM":
        print("karla karışık yağmurlu")

    elif şehir == "ANTAKYA":
        print("açık ve güneşli")

    else:
        print("Girdiğiniz şehir veritabanında yok!")

Burada yazdığımız ``şehir = şehir.upper()`` kodu sayesinde artık kullanıcı şehir
adını büyük harfle de girse, küçük harfle de girse programımız düzgün
çalışacaktır.

Hatırlarsanız ``lower()`` metodunu anlatırken bu metodun bazı Türkçe
karakterlerle problemi olduğunu söylemiştik. Aynı sorun, tahmin edebileceğiniz
gibi, ``upper()`` metodu için de geçerlidir.

Dikkatlice inceleyin::

    >>> kardiz = "istanbul"
    >>> kardiz.upper()
    
    'ISTANBUL'
 
``lower()`` metodu Türkçe'deki 'I' harfini 'i' şeklinde küçültüyordu.
``upper()`` metodu ise 'i' harfini yanlış olarak 'I' şeklinde büyütüyor. Elbette
bu sorun da çözülemeyecek gibi değil. Burada da ``lower()`` metodu için
uyguladığımız yöntemin bir benzerini uygulayacağız::
    
    iller = "istanbul, izmir, siirt, mersin"
    
    iller = iller.replace("i", "İ").upper()
    print(iller)

Bu kodlarla, önce karakter dizisi içinde geçen 'i' harflerini 'İ' ile
değiştiriyoruz. Böylece şöyle bir şey elde etmiş oluyoruz::
    
    İstanbul, İzmİr, sİİrt, mersİn

Gördüğünüz gibi öteki harfler eski hallerinde kaldı. Öteki harfleri de
büyütebilmek için karakter dizisine ``upper()`` metodunu uygulamamız yeterli
olacaktır.
    
Bir sorunun daha üstesinden geldiğimize göre kendimizden emin bir şekilde bir
sonraki metodumuzu incelemeye geçebiliriz.

islower(), isupper()
=============================

Yukarıda öğrendiğimiz ``lower()`` ve ``upper()`` adlı metotlar karakter dizileri
üzerinde bazı değişiklikler yapmamıza yardımcı oluyor. Karakter dizileri
üzerinde birtakım değişiklikler yapmamızı sağlayan bu tür metotlara 'değiştirici
metotlar' adı verilir. Bu tür metotların dışında bir de 'sorgulayıcı
metotlar'dan söz edebiliriz. Sorgulayıcı metotlar, değiştirici metotların
aksine, bir karakter dizisi üzerinde değişiklik yapmamızı sağlamaz. Bu tür
metotların görevi karakter dizilerinin durumunu sorgulamaktır. Sorgulayıcı
metotlara örnek olarak ``islower()`` ve ``isupper()`` metotlarını verebiliriz.

Bildiğiniz gibi, ``lower()`` metodu bir karakter dizisini tamamen küçük
harflerden oluşacak şekle getiriyordu. ``islower()`` metodu ise bir karakter
dizisinin tamamen küçük harflerden oluşup oluşmadığını sorguluyor.

Hemen bir örnek verelim::

    >>> kardiz = "istihza"
    >>> kardiz.islower()
    
    True

`"istihza"` tamamen küçük harflerden oluşan bir karakter dizisi olduğu için
``islower()`` sorgusu `True` çıktısı veriyor. Bir de şuna bakalım::
    
    >>> kardiz = "Ankara"
    >>> kardiz.islower()
    
    False

`"Ankara"` ise içinde bir adet büyük harf barındırdığı için ``islower()``
sorgusuna `False` cevabı veriyor.

Yazdığınız programlarda, örneğin, kullanıcıdan gelen verinin sadece küçük
harflerden oluşmasını istiyorsanız bu metottan yararlanarak kullanıcıdan gelen
verinin gerçekten tamamen küçük harflerden oluşup oluşmadığını
denetleyebilirsiniz::
    
    veri = input("Adınız: ")

    if not veri.islower():
        print("Lütfen isminizi sadece küçük harflerle yazın")

``isupper()`` metodu da ``islower()`` metodunun yaptığı işin tam tersini yapar.
Bildiğiniz gibi, ``upper()`` metodu bir karakter dizisini tamamen büyük
harflerden oluşacak şekle getiriyordu. ``isupper()`` metodu ise bir karakter
dizisinin tamamen büyük harflerden oluşup oluşmadığını sorguluyor::
    
    >>> kardiz = "İSTİHZA"
    >>> kardiz.isupper()
    
    True
    
    >>> kardiz = "python"
    >>> kardiz.isupper()
    
    False
    
Tıpkı ``islower()`` metodunda olduğu gibi, ``isupper()`` metodunu da
kullanıcıdan gelen verinin büyük harfli mi yoksa küçük harfli mi olduğunu
denetlemek için kullanabilirsiniz.

Örneğin, internet kültüründe kullanıcıların forum ve e.posta listesi gibi
yerlerde tamamı büyük harflerden oluşan kelimelerle yazması kaba bir davranış
olarak kabul edilir. Kullanıcıların tamamı büyük harflerden oluşan kelimeler
kullanmasını engellemek için yukarıdaki metotlardan yararlanabilirsiniz::
    
    veri = input("mesajınız: ")
    böl = veri.split()

    for i in böl:
        if i.isupper():
            print("Tamamı büyük harflerden oluşan kelimeler kullanmayın!")

Burada kullanıcının girdiği mesaj içindeki her kelimeyi tek tek sorgulayabilmek
için öncelikle ``split()`` metodu yardımıyla karakter dizisini parçalarına
ayırdığımıza dikkat edin. ``böl = veri.split()`` satırının tam olarak ne işe
yaradığını anlamak için bu programı bir de o satır olmadan çalıştırmayı
deneyebilirsiniz.

``islower()`` ve ``isupper()`` metotları programlamada sıklıkla kullanılan
karakter dizisi metotlarından ikisidir. Dolayısıyla bu iki metodu iyi öğrenmek
programlama maceranız sırasında işlerinizi epey kolaylaştıracaktır.

endswith()
===============

Tıpkı ``isupper()`` ve ``islower()`` metotları gibi, ``endswith()`` metodu da
sorgulayıcı metotlardan biridir. ``endswith()`` metodu karakter dizileri
üzerinde herhangi bir değişiklik yapmamızı sağlamaz. Bu metodun görevi karakter
dizisinin durumunu sorgulamaktır.

Bu metot yardımıyla bir karakter dizisinin hangi karakter dizisi ile bittiğini
sorgulayabiliyoruz. Yani örneğin::

    >>> kardiz = "istihza"
    >>> kardiz.endswith("a")
    
    True

Burada, değeri `"istihza"` olan `kardiz` adlı bir karakter dizisi tanımladık.
Daha sonra da ``kardiz.endswith("a")`` ifadesiyle bu karakter dizisinin `"a"`
karakteri ile bitip bitmediğini sorguladık. Gerçekten de `"istihza"` karakter
dizisinin sonunda `"a"` karakteri bulunduğu için Python bize `True` cevabı
verdi. Bir de şuna bakalım::
    
    >>> kardiz.endswith("z")
    
    False

Bu defa da `False` çıktısı aldık. Çünkü karakter dizimiz 'z' harfiyle bitmiyor.

Gelin isterseniz elimizi alıştırmak için bu metotla birkaç örnek daha yapalım::

    d1 = "python.ogg"
    d2 = "tkinter.mp3"
    d3 = "pygtk.ogg"
    d4 = "movie.avi"
    d5 = "sarki.mp3"
    d6 = "filanca.ogg"
    d7 = "falanca.mp3"
    d8 = "dosya.avi"
    d9 = "perl.ogg"
    d10 = "c.avi"
    d11 = "c++.mp3"

    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i.endswith(".mp3"):
            print(i)

Bu örnekte, elimizde farklı uzantılara sahip bazı dosyalar olduğunu varsaydık ve
bu dosya adlarının herbirini ayrı birer değişken içinde depoladık. Gördüğünüz
gibi, dosya uzantıları `.ogg`, `.mp3` veya `.avi`. Bizim burada amacımız
elimizdeki mp3 dosyalarını listelemek. Bu işlem için ``endswith()`` metodundan
yararlanabiliyoruz. Burada yaptığımız şey şu:

Öncelikle `d1`, `d2`, `d3`, `d4`, `d5`, `d6`, `d7`, `d8`, `d9`, `d10` ve `d11`
adlı değişkenleri bir ``for`` döngüsü içine alıyoruz ve bu değişkenlerinin
herbirinin içeriğini tek tek kontrol ediyoruz (``for i in d1, d2, d3, d4, d5,
d6, d7, d8, d9, d10, d11:``). Ardından, eğer baktığımız bu değişkenlerin
değerleri ".mp3" ifadesi ile bitiyorsa (``if i.endswith(".mp3"):``), ölçüte uyan
bütün karakter dizilerini ekrana döküyoruz (``print(i)``).

Yukarıdaki örneği, dilerseniz, ``endswith()`` metodunu kullanmadan şöyle de
yazabilirsiniz::

    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i[-4:len(i)] == ".mp3":
            print(i)

Burada karakter dizilerinin dilimlenebilme özelliğinden yararlandık. Ancak
gördüğünüz gibi, dilimlenecek kısmı ayarlamaya uğraşmak yerine ``endswith()``
metodunu kullanmak çok daha mantıklı ve kolay bir yöntemdir.

Yukarıdaki örnekte de gördüğünüz gibi, ``endswith()`` metodu özellikle dosya
uzantılarına göre dosya türlerini tespit etmede oldukça işe yarar bir metottur.

startswith()
==================

Bu metot, biraz önce gördüğümüz ``endswith()`` metodunun yaptığı işin tam
tersini yapar. Hatırlarsanız ``endswith()`` metodu bir karakter dizisinin hangi
karakter veya karakterlerle bittiğini denetliyordu. ``startswith()`` metodu ise
bir karakter dizisinin hangi karakter veya karakterlerle başladığını denetler::
    
    >>> kardiz = "python"
    >>> kardiz.startswith("p")
    
    True
    
    >>> kardiz.startswith("a")
    
    False

Gördüğünüz gibi, eğer karakter dizisi gerçekten belirtilen karakterle başlıyorsa
Python `True` çıktısı, yok eğer belirtilen karakterle başlamıyorsa `False`
çıktısı veriyor.

Bu metodun gerçek hayatta nasıl kullanılabileceğine dair bir örnek verelim::

    d1 = "python.ogg"
    d2 = "tkinter.mp3"
    d3 = "pygtk.ogg"
    d4 = "movie.avi"
    d5 = "sarki.mp3"
    d6 = "filanca.ogg"
    d7 = "falanca.mp3"
    d8 = "dosya.avi"
    d9 = "perl.ogg"
    d10 = "c.avi"
    d11 = "c++.mp3"

    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i.startswith("p"):
            print(i)

Burada 'p' harfiyle başlayan bütün dosyaları listeledik. Elbette aynı etkiyi şu
şekilde de elde edebilirsiniz::
    
    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i[0] == "p":
            print(i)

Sadece tek bir harfi sorguluyorsanız yukarıdaki yöntem de en az ``startswith()``
metodunu kullanmak kadar pratiktir. Ama birden fazla karakteri sorguladığınız
durumlarda elbette ``startswith()`` çok daha mantıklı bir tercih olacaktır::
    
    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i.startswith("py"):
            print(i)

Yukarıda yazdığımız kodu dilimleme tekniğinden yararlanarak yeniden yazmak
isterseniz şöyle bir şeyler yapmanız gerekiyor::
    
    for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
        if i[:2] == "py":
            print(i)

Dediğim gibi, birden fazla karakteri sorguladığınız durumlarda, dilimlemek
istediğiniz kısmın karakter dizisi içinde hangi aralığa denk geldiğini
hesaplamaya uğraşmak yerine, daha kolay bir yöntem olan ``startswith()``
metodundan yararlanmayı tercih edebilirsiniz.

Böylece karakter dizilerinin 2. bölümünü de bitirmiş olduk. Sonraki bölümde yine
karakter dizilerinin metotlarından söz etmeye devam edeceğiz.

