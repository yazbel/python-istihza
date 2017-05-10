.. meta::
   :description: Python 3.x'te karakter dizileri
   :keywords: python, string, karakter dizisi, metotlar

.. highlight:: py3

****************************************
Karakter Dizilerinin Metotları (Devamı)
****************************************

Karakter dizileri konusunun en başında söylediğimiz gibi, karakter dizileri
metot yönünden bir hayli zengin bir veri tipidir. Bir önceki bölümde karakter
dizileri metotlarının bir kısmını incelemiştik. Bu bölümde yine metotları
incelemeye devam edeceğiz.

capitalize()
=============

Hatırlarsanız, bir önceki bölümde öğrendiğimiz ``startswith()`` ve
``endswith()`` metotları karakter dizileri üzerinde herhangi bir değişiklik
yapmıyordu. Bu iki metodun görevi, karakter dizilerini sorgulamamızı sağlamaktı.
Şimdi göreceğimiz ``capitalize()`` metodu ise karakter dizileri üzerinde
değişiklik yapmamızı sağlayacak. Dolayısıyla bu ``capitalize()`` metodu da
'değiştirici metotlar'dan biridir diyebiliriz.

Hatırlarsanız, ``upper()`` ve ``lower()`` metotları bir karakter dizisi içindeki
bütün karakterleri etkiliyordu. Yani mesela ``upper()`` metodunu bir karakter
dizisine uygularsak, o karakter dizisi içindeki bütün karakterler büyük harfe
dönecektir. Aynı şekilde ``lower()`` metodu da bir karakter dizisi içindeki
bütün karakterleri küçük harfe çevirir.

Şimdi göreceğimiz ``capitalize()`` metodu da ``upper()`` ve ``lower()``
metotlarına benzemekle birlikte onlardan biraz daha farklı davranır:
``capitalize()`` metodunun görevi karakter dizilerinin yalnızca ilk harfini
büyütmektir. Örneğin::
    
    >>> a = "python"
    >>> a.capitalize()

    'Python'

Bu metodu kullanırken dikkat etmemiz gereken bir nokta var: Bu metot bir
karakter dizisinin yalnızca ilk harfini büyütür. Yani birden fazla kelimeden
oluşan karakter dizilerine bu metodu uyguladığımızda bütün kelimelerin ilk harfi
büyümez. Yalnızca ilk kelimenin ilk harfi büyür. Yani::
    
    >>> a = "python programlama dili"
    >>> a.capitalize()
    
    'Python programlama dili'

`"python programlama dili"` üç kelimeden oluşan bir karakter dizisidir. Bu
karakter dizisi üzerine ``capitalize()`` metodunu uyguladığımızda bu üç
kelimenin tamamının ilk harfleri büyümüyor. Yalnızca ilk 'python' kelimesinin
ilk harfi bu metottan etkileniyor.

Bu arada ``capitalize()`` metodunu kullanırken bir şey dikkatinizi çekmiş
olmalı. Bu metodun da, tıpkı ``upper()`` ve ``lower()`` metotlarında olduğu
gibi, Türkçe karakterlerden bazıları ile ufak bir problemi var. Mesela şu örneğe
bir bakın::
    
    >>> kardiz = "istanbul"
    >>> kardiz.capitalize()
    
    'Istanbul'

'istanbul' kelimesinin ilk harfi büyütüldüğünde 'İ' olması gerekirken 'I' oldu.
Bildiğiniz gibi bu problem 'ş', 'ç', 'ö', 'ğ' ve 'ü' gibi öteki Türkçe
karakterlerde karşımıza çıkmaz. Sadece 'i' ve 'İ' harfleri karakter dizisi
metotlarında bize problem çıkaracaktır. Ama endişe etmemize hiç gerek yok. Bu
sorunu da basit bir 'if-else' yapısıyla çözebilecek kadar Python bilgisine
sahibiz::
        
    kardiz = "istanbul büyükşehir belediyesi"
    
    if kardiz.startswith("i"):
        kardiz = "İ" + kardiz[1:]
    
    kardiz = kardiz.capitalize()
    
    print(kardiz)
    
Burada yaptığımız şey şu: Eğer değişkenin tuttuğu karakter dizisi 'i' harfi ile
başlıyorsa, ``"İ" + kardiz[1:]`` kodunu kullanarak karakter dizisinin ilk harfi
dışında kalan kısmıyla 'İ' harfini birleştiriyoruz. Bu yapıyı daha iyi
anlayabilmek için etkileşimli kabukta şu denemeleri yapabilirsiniz::
    
    >>> kardiz = "istanbul"
    >>> kardiz[1:]
    
    'stanbul'

Gördüğünüz gibi, ``kardiz[1:]`` kodu bize karakter dizisinin ilk harfi hariç
geri kalan kısmını veriyor. Bu yapıyı dilimleme konusundan hatırlıyor
olmalısınız. İşte biz dilimleme tekniğinin bu özelliğinden yararlanarak,
karakter dizisinin ilk harfini kesip, baş tarafa bir adet 'İ' harfi ekliyoruz::

    >>> "İ" + kardiz[1:]
    
    'İstanbul'

Hatırlarsanız karakter dizilerinin değiştirilemeyen bir veri tipi olduğunu
söylemiştik. O yüzden, karakter dizisinin `"stanbul"` kısmını 'İ' harfiyle
birleştirdikten sonra, bu değişikliğin kalıcı olabilmesi için ``kardiz = "İ" +
kardiz[1:]`` kodu yardımıyla, yaptığımız değişikliği tekrar `kardiz` adlı bir
değişkene atıyoruz.

Böylece;

::

    if kardiz.startswith("i"):
        kardiz = "İ" + kardiz[1:]

kodlarının ne yaptığını anlamış olduk. Kodların geri kalanında ise şöyle bir kod
bloğu görüyoruz::
    
    kardiz = kardiz.capitalize()

Buna göre, hangi harfle başlarsa başlasın Python'ın standart ``capitalize()``
metodunu bu karakter dizisi üzerine uyguluyoruz.

Son olarak da ``print(kardiz)`` kodunu kullanarak yeni karakter dizisini ekrana
yazdırıyoruz ve böylece ``capitalize()`` metodundaki Türkçe karakter sorununu
kıvrak bir çalımla aşmış oluyoruz.

title()
========

Bu metot biraz önce öğrendiğimiz ``capitalize()`` metoduna benzer. Bildiğiniz
gibi ``capitalize()`` metodu bir karakter dizisinin yalnızca ilk harfini
büyütüyordu. ``title()`` metodu da karakter dizilerinin ilk harfini büyütür. Ama
``capitalize()`` metodundan farklı olarak bu metot, birden fazla kelimeden
oluşan karakter dizilerinin her kelimesinin ilk harflerini büyütür.

Bunu bir örnek üzerinde anlatsak sanırım daha iyi olacak::

    >>> a = "python programlama dili"
    >>> a.capitalize()
    
    'Python programlama dili'
    
    >>> a.title()
    
    'Python Programlama Dili'

``capitalize()`` metodu ile ``title()`` metodu arasındaki fark bariz bir biçimde
görünüyor. Dediğimiz gibi, ``capitalize()`` metodu yalnızca ilk kelimenin ilk
harfini büyütmekle yetinirken, ``title()`` metodu karakter dizisi içindeki bütün
kelimelerin ilk harflerini büyütüyor.

Tahmin edebileceğiniz gibi, ``capitalize()`` metodundaki Türkçe karakter
problemi ``title()`` metodu için de geçerlidir. Yani::

    >>> kardiz = "istanbul"
    >>> kardiz.title()
    
    'Istanbul'
    
    >>> kardiz = "istanbul büyükşehir belediyesi"
    >>> kardiz.title()
    
    'Istanbul Büyükşehir Belediyesi'  

Gördüğünüz gibi, burada da Python 'i' harfini düzgün büyütemedi. Ama tabii ki bu
bizi durduramaz! Çözümümüz hazır::
    
    kardiz = "istanbul"

    if kardiz.startswith("i"):
        kardiz = "İ" + kardiz[1:]
        kardiz = kardiz.title()
    else:
        kardiz = kardiz.title()

    print(kardiz)
   
Bu kodların ``capitalize()`` metodunu anlatırken verdiğimiz koda ne kadar
benzediğini görüyorsunuz. Bu iki kod hemen hemen birbirinin aynısı. Tek fark, en
sondaki ``kardiz.capitalize()`` kodunun burada ``kardiz.title()`` olması ve
``if`` bloğu içine ek olarak ``kardiz = kardiz.title()`` satırını yazmış
olmamız. ``kardiz.capitalize()`` kodunun neden ``kardiz.title()`` koduna
dönüştüğünü açıklamaya gerek yok. Ama eğer ``kardiz = kardiz.title()`` kodunun
ne işe yaradığını tam olarak anlamadıysanız o satırı silin ve `kardiz`
değişkeninin değerini `"istanbul büyükşehir belediyesi"` yapın. Yani::
    
    kardiz = "istanbul büyükşehir belediyesi"

    if kardiz.startswith("i"):
        kardiz = "İ" + kardiz[1:]
    else:
        kardiz = kardiz.title()

    print(kardiz)

Bu kodları bu şekilde çalıştırırsanız şu çıktıyı alırsınız::

    İstanbul büyükşehir belediyesi

Burada yalnızca ilk kelimenin ilk harfi büyüdü. Halbuki ``title()`` metodunun
işleyişi gereğince karakter dizisi içindeki bütün kelimelerin ilk harflerinin
büyümesi gerekiyordu. İşte o satır bütün kelimelerin ilk harflerinin büyümesini
sağlıyor. Eğer bir kelimenin ilk harfi zaten büyükse ``title()`` metodu bu harfe
dokunmaz, ama karakter dizisi içindeki öbür kelimelerin ilk harflerini yine de
büyütür.

İşte yukarıda ``title()`` metodunun bu özelliğinden faydalanıyoruz. ``kardiz =
"İ" + kardiz[1:]`` komutu karakter dizisinin ilk kelimesinin ilk harfini düzgün
bir şekilde büyütüyor, ama geri kalan kelimelere hiçbir şey yapmıyor. ``kardiz =
kardiz.title()`` komutu ise karakter dizisi içindeki geri kalan kelimelerin ilk
harflerini büyütüyor. Böylece istediğimiz çıktıyı elde edebilmiş oluyoruz.
Yalnız bu kodlarda bir şey dikkatinizi çekmiş olmalı. ``kardiz =
kardiz.title()`` komutunu program içinde iki yerde kullandık. Programcılıktaki
en önemli ilkelerden biri de mümkün olduğunca tekrardan kaçınmaktır. Eğer
yazdığınız bir programda aynı kodları program boyunca tekrar tekrar yazıyorsanız
muhtemelen bir yerde hata yapıyorsunuzdur. Öyle bir durumda yapmanız gereken şey
kodlarınızı tekrar gözden geçirip, tekrar eden kodları nasıl azaltabileceğinizi
düşünmektir. İşte burada da böyle bir tekrar söz konusu. Biz tekrara düşmekten
kurtulmak için yukarıdaki kodları şöyle de yazabiliriz::
    
    kardiz = "istanbul büyükşehir belediyesi"

    if kardiz.startswith("i"):
        kardiz = "İ" + kardiz[1:]

    kardiz = kardiz.title()

    print(kardiz)

``kardiz = kardiz.title()`` komutunu hem ``if`` bloğunda, hem de ``else``
bloğunda kullandığımız için, programımız her koşulda bu kodu zaten çalıştıracak.
O yüzden bu satırı ``if`` bloğuna yazdıktan sonra bir de aynı şeyi ``else``
bloğu içine yazmak gereksiz. Onun yerine ``else`` bloğunu tamamen kaldırıp, o
satırı ``if`` bloğunun çıkışına yerleştirebiliriz.

Eski kodlardaki mantık işleyişi şöyle idi:

    #. `kardiz` adlı bir değişken tanımla
    
    #. Eğer `kardiz` 'i' harfi ile başlıyorsa (``if``), `kardiz`'in ilk harfi 
       hariç geri kalan kısmı ile 'İ' harfini birleştir. 
    
    #. Daha sonra `kardiz` değişkenine ``title()`` metodunu uygula.
    
    #. Eğer `kardiz` 'i' harfi ile değil de başka bir harfle başlıyorsa (``else``), 
       `kardiz` değişkenine ``title()`` metodunu uygula.
    
    #. Son olarak `kardiz` değişkenini yazdır. 

Tekrar eden kodları çıkardıktan sonra ise kodlarımızın mantık işleyişi şöyle
oldu:

    #. `kardiz` adlı bir değişken tanımla
    
    #. Eğer `kardiz` 'i' harfi ile başlıyorsa (``if``), `kardiz`'in ilk harfi 
       hariç geri kalan kısmı ile 'İ' harfini birleştir. 
    
    #. Daha sonra `kardiz` değişkenine ``title()`` metodunu uygula.
    
    #. Son olarak `kardiz` değişkenini yazdır. 

Gördüğünüz gibi, aynı sonuca daha kısa bir yoldan ulaşabiliyoruz. 

Ama bir dakika! Burada bir sorun var! 

Bu kodlar 'i' harfinin karakter dizisinin yalnızca en başında yer aldığı
durumlarda düzgün çalışacaktır. Bu kodlar mesela şu karakter dizisini düzgün
büyütemez::
    
    on iki ada

Aynı şekilde bu kodlar şu karakter dizisini de büyütemez::
    
    hükümet istifa!
    
Çünkü bu karakter dizilerinde 'i' harfi karakter dizisini oluşturan kelimelerin
ilkinde yer almıyor. Bizim yazdığımız kod ise yalnızca ilk kelime düşünülerek
yazılmış. Peki bu sorunun üstesinden nasıl geleceğiz?

Evet, doğru tahmin ettiniz. Bizi kurtaracak şey ``split()`` metodu ve basit bir
``for`` döngüsü. Dikkatlice bakın::
    
    kardiz = "on iki ada"
    
    for kelime in kardiz.split():
        if kelime.startswith("i"):
            kelime = "İ" + kelime[1:]
            
        kelime = kelime.title()
    
        print(kelime, end=" ")
        
Bu defa istediğimizi gerçekleştiren bir kod yazabildik. Bu kodlar, 'i' harfi
karakter dizisini oluşturan kelimelerin hangisinde bulunursa bulunsun, karakter
dizisini Türkçeye uygun bir şekilde büyütebilecektir.

Bir önceki kodlara göre, bu son kodlardaki tek farkın ``split()`` metodu ve
``for`` döngüsü olduğuna dikkat edin. 

Bu kodları daha iyi anlayabilmek için etkileşimli kabukta kendi kendinize bazı
deneme çalışmaları yapabilirsiniz::
    
    >>> kardiz = "on iki ada"
    >>> kardiz.split()
    
    ['on', 'iki', 'ada']
    
    >>> for kelime in kardiz.split():
    ...     print(kelime[0])
    ...
    o
    i
    a
    
Gördüğünüz gibi, ``split()`` metodu ``"on iki ada"`` adlı karakter dizisini
kelimelerine ayırıyor. İşte biz de kelimelerine ayrılmış bu yapı üzerinde bir
``for`` döngüsü kurarak herbir öğenin ilk harfinin 'i' olup olmadığını kontrol
edebiliyoruz.

swapcase()
=============

``swapcase()`` metodu da büyük-küçük harfle ilgili bir metottur. Bu metot bir
karakter dizisi içindeki büyük harfleri küçük harfe; küçük harfleri de büyük
harfe dönüştürür. Örneğin::
    
    >>> kardiz = "python"
    >>> kardiz.swapcase()
    
    'PYTHON'
    
    >>> kardiz = "PYTHON"
    >>> kardiz.swapcase()
    
    'python'
    
    >>> kardiz = "Python"
    >>> kardiz.swapcase()
    
    'pYTHON'

Gördüğünüz gibi, bu metot aynen dediğimiz gibi işliyor. Yani küçük harfleri
büyük harfe; büyük harfleri de küçük harfe dönüştürüyor.

Yine tahmin edebileceğiniz gibi, bu metodun da bazı Türkçe karakterlerle
problemi var::

    >>> kardiz = "istihza"
    >>> kardiz.swapcase()
    
    'ISTIHZA'

Bu sorunu da aşmak tabii ki bizim elimizde::

    kardiz = "istanbul"
    
    for i in kardiz:
        if i == 'İ':
            kardiz = kardiz.replace('İ', 'i')
        elif i == 'i':
            kardiz = kardiz.replace('i', 'İ')
        else:
            kardiz = kardiz.replace(i, i.swapcase())
                
    print(kardiz)

Daha önceki örneklerde de olduğu gibi, bu kodlarda da 'i' ve 'I' harflerini tek
tek kontrolden geçiriyoruz. Eğer bir karakter dizisi içinde bu iki harften biri
varsa, bunların büyük harf veya küçük harf karşılıklarını elle yerine koyuyoruz.
Bu karakterler dışında kalan karakterlere ise doğrudan ``swapcase()`` metodunu
uygulayarak istediğimiz sonucu elde ediyoruz. Bu kodlarda kafanıza yatmayan
yerler varsa, kodlar içinde kendinize göre bazı eklemeler çıkarmalar yaparak
neyin ne işe yaradığını daha kolay anlayabilirsiniz.

casefold()
============

Bu metot işlev olarak ``lower()`` metoduna çok benzer. Hatta Türkçe açısından,
bu metodun ``lower()`` metodundan hiçbir farkı yoktur. Ancak bazı başka
dillerde, bu metot bazı harfler için ``lower()`` metodunun verdiğinden farklı
bir çıktı verir. Örneğin Almancadaki 'ß' harfi bu duruma bir örnek olabilir::

    >>> "ß".lower()
    'ß'
    
    >>> "ß".casefold()
    'ss'
    
Gördüğünüz gibi, ``lower()`` ve ``casefold()`` metotları bu harfe farklı
davranıyor.

Türkçedeki İ-i sorunu bu metot için de aynen geçerlidir.

strip(), lstrip(), rstrip()
============================

Bu başlıkta birbiriyle bağlantılı üç adet karakter dizisi metodunu
inceleyeceğiz. Bu metotlar ``strip()``, ``lstrip()`` ve ``rstrip()``. İlk olarak
``strip()`` metoduyla başlayalım.

Zaman zaman, içinde anlamsız ya da gereksiz karakterler barındıran metinleri bu
anlamsız ve gereksiz karakterlerden temizlemeniz gereken durumlarla
karşılaşabilirsiniz. Örneğin arkadaşınızdan gelen bir e.postada her satırın
başında ve/veya sonunda `>` gibi bir karakter olabilir. Arkadaşınızdan gelen bu
e.postayı kullanabilmek için öncelikle metin içindeki o `>` karakterlerini
silmeniz gerekebilir. Hepimizin bildiği gibi, bu tür karakterleri elle
temizlemeye kalkışmak son derece sıkıcı ve zaman alıcı bir yöntemdir. Ama artık
siz bir Python programcısı olduğunuza göre bu tür angaryaları Python'a
devredebilirsiniz.

Yukarıda bahsettiğimiz duruma yönelik bir örnek vermeden önce dilerseniz
``strip()`` metoduyla ilgili çok basit örnekler vererek başlayalım işe::

    >>> kardiz = " istihza "

Burada değeri `" istihza "` olan `kardiz` adlı bir karakter dizisi tanımladık.
Dikkat ederseniz bu karakter dizisinin sağında ve solunda birer boşluk karakteri
var. Bazı durumlarda kullanıcıdan ya da başka kaynaktan gelen karakter
dizilerinde bu tür istenmeyen boşluklar olabilir. Ama sizin kullanıcıdan veya
başka bir kaynaktan gelen o karakter dizisini düzgün kullanabilmeniz için
öncelikle o karakter dizisinin sağında ve solunda bulunan boşluk
karakterlerinden kurtulmanız gerekebilir. İşte böyle anlarda ``strip()`` metodu
yardımınıza yetişecektir. Dikkatlice inceleyin::
    
    >>> kardiz = " istihza "
    >>> print(kardiz)
    
    ' istihza '
    
    >>> kardiz.strip()
    
    'istihza'

Gördüğünüz gibi, ``strip()`` metodunu kullanarak, karakter dizisinin
orijinalinde bulunan sağlı sollu boşluk karakterlerini bir çırpıda ortadan
kaldırdık.

``strip()`` metodu yukarıdaki örnekte olduğu gibi parametresiz olarak
kullanıldığında, bir karakter dizisinin sağında veya solunda bulunan belli başlı
karakterleri kırpar. ``strip()`` metodunun öntanımlı olarak kırptığı karakterler
şunlardır:
    
    +----------+---------------------------------------------------------------+
    | `' '`    | boşluk karakteri                                              |
    +----------+---------------------------------------------------------------+
    | `\\t`    | sekme (TAB) oluşturan kaçış dizisi                            |
    +----------+---------------------------------------------------------------+
    | `\\n`    | satır başına geçiren kaçış dizisi                             |
    +----------+---------------------------------------------------------------+
    | `\\r`    | imleci aynı satırın başına döndüren kaçış dizisi              |
    +----------+---------------------------------------------------------------+
    | `\\v`    | düşey sekme oluşturan kaçış dizisi                            |
    +----------+---------------------------------------------------------------+
    | `\\f`    | yeni bir sayfaya geçiren kaçış dizisi                         |
    +----------+---------------------------------------------------------------+

Yani eğer ``strip()`` metoduna herhangi bir parametre vermezsek bu metot
otomatik olarak karakter dizilerinin sağında ve solunda bulunan yukarıdaki
karakterleri kırpacaktır. Ancak eğer biz istersek ``strip()`` metoduna bir
parametre vererek bu metodun istediğimiz herhangi başka bir karakteri kırpmasını
da sağlayabiliriz. Örneğin::
    
    >>> kardiz = "python"
    >>> kardiz.strip("p")
    
    'ython'
    
Burada ``strip()`` metoduna parametre olarak `"p"` karakter dizisini vererek,
``strip()`` metodunun, karakter dizisinin başında bulunan `"p"` karakterini
ortadan kaldırmasını sağladık. Yalnız ``strip()`` metodunu kullanırken bir
noktaya dikkat etmelisiniz. Bu metot bir karakter dizisinin hem başında, hem de
sonunda bulunan karakterlerle ilgilenir. Mesela şu örneğe bakalım::
    
    >>> kardiz = "kazak"
    >>> kardiz.strip("k")
    
    'aza'

Gördüğünüz gibi, ``strip()`` metoduna `"k"` parametresini vererek, `"kazak"`
adlı karakter dizisinin hem başındaki hem de sonundaki `"k"` harflerini kırpmayı
başardık. Eğer bu metoda verdiğiniz parametre karakter dizisinde geçmiyorsa, bu
durumda ``strip()`` metodu herhangi bir işlem yapmaz. Ya da aradığınız karakter,
karakter dizisinin yalnızca tek bir tarafında (mesela sadece başında veya sadece
sonunda) geçiyorsa, ``strip()`` metodu, ilgili karakter hangi taraftaysa onu
siler. Aranan karakterin bulunmadığı tarafla ilgilenmez.

``strip()`` metodunu anlatmaya başlarken, içinde gereksiz yere `>` işaretlerinin
geçtiği e.postalardan söz etmiş ve bu e.postalardaki o gereksiz karakterleri
elle silmenin ne kadar da sıkıcı bir iş olduğunu söylemiştik. Eğer
e.postalarınızda bu tip durumlarla sık sık karşılaşıyorsanız, gereksiz
karakterleri silme görevini sizin yerinize Python yerine getirebilir. Şimdi şu
kodları dikkatlice inceleyin::
    
    metin = """
    > Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 
    > 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python 
    > olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür. 
    > Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez. 
    > Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi 
    > grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. 
    > Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde 
    > bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
    """

    for i in metin.split():
        print(i.strip("> "), end=" ")

.. highlight:: none

Bu programı çalıştırdığınızda şöyle bir çıktı elde edeceksiniz::

    Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından  
    90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python  
    olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.  
    Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.  
    Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi  
    grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.  
    Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde  
    bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.

.. highlight:: py3

Gördüğünüz gibi, her satırın başında bulunan `'> '` karakterlerini ufacık birkaç
kod yardımıyla rahatlıkla temizledik. Burada ``strip()`` metoduyla birlikte
``split()`` metodunu da kullandığımızı görüyorsunuz. ``split()`` metodu ile önce
`metin` adlı karakter dizisini parçaladık. Daha sonra da ``strip()`` metodu
yardımıyla baş taraftaki istenmeyen karakterleri temizledik.

Yukarıdaki örnekte verdiğimiz metin, istenmeyen karakterleri yalnızca tek bir
tarafta içeriyor. Ama elbette istenmeyen karakterler, karakter dizisinin ne
tarafında olursa olsun ``strip()`` metodu bu karakterleri başarıyla kırpacaktır.

Bu bölümün başlığında ``strip()`` metodu ile birlikte ``lstrip()`` ve
``rstrip()`` adlı iki metodun daha adı geçiyordu. ``strip()`` metodunun ne işe
yaradığını öğrendik. Peki bu ``lstrip()`` ve ``rstrip()`` metotları ne işe
yarıyor?

``lstrip()`` metodundan başlayalım anlatmaya...

``strip()`` metodunu anlatırken, bu metodun bir karakter dizisinin sağında ve
solunda bulunan istenmeyen karakterleri kırptığını söylemiştik. Ancak bazen,
istediğimiz şey bu olmayabilir. Yani biz bir karakter dizisinin hem sağında, hem
de solunda bulunan gereksiz karakterleri değil, yalnızca sağında veya yalnızca
solunda bulunan gereksiz karakterleri kırpmak isteyebiliriz. Örneğin ``strip()``
metodunu anlatırken verdiğimiz `"kazak"` örneğini ele alalım. Şöyle bir komutun
ne yapacağını biliyorsunuz::
    
    >>> "kazak".strip("k")

Bu komut hem sol, hem de sağ taraftaki `"k"` karakterlerini kırpacaktır. Ama
peki ya biz sadece sol taraftaki `"k"` karakterini atmak istersek ne olacak?
İşte böyle bir durumda ``strip()`` metodundan değil, ``lstrip()`` metodundan
faydalanacağız.

``lstrip()`` metodu bir karakter dizisinin sol tarafındaki gereksiz
karakterlerden kurtulmamızı sağlar. Mesela bu bilgiyi yukarıdaki örneğe
uygulayalım::
    
    >>> "kazak".lstrip("k")
    
    'azak'

Gördüğünüz gibi, ``lstrip()`` metodu yalnızca sol baştaki `"k"` harfiyle
ilgilendi. Sağ taraftaki `"k"` harfine ise dokunmadı. Eğer sol taraftaki
karakteri değil de yalnızca sağ taraftaki karakteri uçurmak istemeniz halinde
ise ``rstrip()`` metodundan yararlanacaksınız::
    
    >>> "kazak".rstrip("k")
    
    'kaza'

Bu arada, yukarıdaki metotları doğrudan karakter dizileri üzerine
uygulayabildiğimize de dikkat edin. Yani şu iki yöntem de uygun ve doğrudur::
    
    >>> kardiz = "karakter dizisi"
    >>> kardiz.metot_adı()

veya::

    >>> "karakter dizisi".metot_adı()

join()
======

Hatırlarsanız şimdiye kadar öğrendiğimiz metotlar arasında ``split()`` adlı bir
metot vardı. Bu metodun ne işe yaradığını ve nasıl kullanıldığını biliyorsunuz::
    
    >>> kardiz = "Beşiktaş Jimnastik Kulübü"
    >>> bölünmüş = kardiz.split()
    >>> print(bölünmüş)
    
    ['Beşiktaş', 'Jimnastik', 'Kulübü']

Gördüğünüz gibi ``split()`` metodu bir karakter dizisini belli yerlerden bölerek
parçalara ayırıyor. Bu noktada insanın aklına şöyle bir soru geliyor: Diyelim ki
elimizde böyle bölünmüş bir karakter dizisi grubu var. Biz bu grup içindeki
karakter dizilerini tekrar birleştirmek istersek ne yapacağız?

Şimdi şu kodlara çok dikkatlice bakın::

    >>> " ".join(bölünmüş)
    
    'Beşiktaş Jimnastik Kulübü'

Gördüğünüz gibi, `"Beşiktaş Jimnastik Kulübü"` adlı karakter dizisinin ilk
halini tekrar elde ettik. Yani bu karakter dizisine ait, bölünmüş parçaları
tekrar bir araya getirdik. Ancak bu işi yapan kod gözünüzüne biraz tuhaf ve
anlaşılmaz görünmüş olabilir.

İlk başta dikkatimizi çeken şey, bu metodun öbür metotlara göre biraz daha
farklı bir yapıya sahipmiş gibi görünmesi. Ama belki yukarıdaki örneği şöyle
yazarsak bu örnek biraz daha anlaşılır gelebilir gözünüze::
    
    >>> birleştirme_karakteri = " "
    >>> birleştirme_karakteri.join(bölünmüş)

Burada da tıpkı öteki metotlarda olduğu gibi, ``join()`` metodunu bir karakter
dizisi üzerine uyguladık. Bu karakter dizisi bir adet boşluk karakteri. Ayrıca
gördüğünüz gibi ``join()`` metodu bir adet de parametre alıyor. Bu örnekte
``join()`` metoduna verdiğimiz parametre `bölünmüş` adlı değişken. Aslında şöyle
bir düşününce yukarıdaki kodların sanki şöyle yazılması gerekiyormuş gibi
gelebilir size::
    
    >>> bölünmüş.join(birleştirme_karakteri)

Ama bu kullanım yanlıştır. Üstelik kodunuzu böyle yazarsanız Python size bir
hata mesajı gösterecektir::

    >>> bölünmüş.join(birleştirme_karakteri)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'join'

Buradaki hata mesajı bize şöyle diyor: 'liste nesnesinin `join` adlı bir
niteliği yoktur!'. Bu cümledeki 'liste nesnesi' ifadesine özellikle dikkatinizi
çekmek istiyorum. Biz şimdiye kadar iki tür nesne (ya da başka bir ifadeyle veri
tipi) görmüştük. Bunlar karakter dizileri ve sayılardı. Burada karşımıza üçüncü
bir nesne çıkıyor. Gördüğümüz kadarıyla bu yeni nesnenin adı 'liste'. (Liste
adlı veri tipini birkaç bölüm sonra en ince ayrıntısına kadar inceleyeceğiz.
Python'da böyle bir veri tipi olduğunu bilmemiz bizim için şimdilik yeterli.)

İşte yukarıdaki hatayı almamızın nedeni, aslında karakter dizilerine ait bir
metot olan ``join()`` metodunu bir liste üzerinde uygulamaya çalışmamız. Böyle
bir durumda da Python doğal olarak bizi 'liste nesnelerinin `join` adlı bir
niteliği olmadığı' konusunda uyarıyor. Bütün bu anlattıklarımız bizi şu sonuca
ulaştırıyor: Bir veri tipine ait metotlar doğal olarak yalnızca o veri tipi
üzerinde kullanılabilir. Mesela yukarıdaki örnekte gördüğümüz gibi, bir karakter
dizisi metodu olan ``join()``'i başka bir veri tipine uygulamaya çalışırsak hata
alırız.

Sonuç olarak, ``join()`` adlı metodu `bölünmüş` adlı değişkene
uygulayamayacağımızı anlamış bulunuyoruz. O halde bu metotla birlikte
kullanılmak üzere bir karakter dizisi bulmamız gerekiyor.

En başta da söylediğimiz gibi, ``join()`` metodunun görevi bölünmüş karakter
dizisi gruplarını birleştirmektir. Bu metot görevini yerine getirirken, yani
karakter dizisi gruplarını birleştirirken bir birleştirme karakterine ihtiyaç
duyar. Bizim örneğimizde bu birleştirme karakteri bir adet boşluktur. Durumu
daha iyi anlayabilmek için örneğimizi tekrar gözümünün önüne getirelim::
    
    >>> kardiz = "Beşiktaş Jimnastik Kulübü"
    >>> bölünmüş = kardiz.split()
    >>> print(bölünmüş)
    
    ['Beşiktaş', 'Jimnastik', 'Kulübü']
    
    >>> kardiz = " ".join(bölünmüş)
    >>> print(kardiz)
    
    Beşiktaş Jimnastik Kulübü

Gördüğünüz gibi, orijinal karakter dizisinin bölünmüş parçalarını, her bir
parçanın arasında bir adet boşluk olacak şekilde yeniden birleştirdik. Elbette
sadece boşluk karakteri kullanabileceğiz diye bir kaide yok. Mesela şu örneklere
bakın::
    
    >>> kardiz = "-".join(bölünmüş)
    
    Beşiktaş-Jimnastik-Kulübü
    
    >>> kardiz = "".join(bölünmüş)
    
    BeşiktaşJimnastikKulübü

İlk örnekte, bölünmüş karakter dizilerini `-` işareti ile birleştirdik. İkinci
örnekte ise bu karakter dizilerini birleştirmek için boş bir karakter dizisi
kullandık. Yani parçaları birleştirirken arada boşluk olmamasını sağladık.

``join()`` metodu ile bol bol pratik yaparak bu metodu hakkıyla öğrenmenizi
tavsiye ederim. Zira programcılık maceranız boyunca en sık kullanacağınız
karakter dizisi metotları listesinin en başlarında bu metot yer alır.

count()
============

Tıpkı daha önce öğrendiğimiz sorgulayıcı metotlar gibi, ``count()`` metodu da
bir karakter dizisi üzerinde herhangi bir değişiklik yapmamızı sağlamaz. Bu
metodun görevi bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini
sorgulamaktır. Bununla ilgili hemen bir örnek verelim::
    
    >>> şehir = "Kahramanmaraş"
    >>> şehir.count("a")
    
    5

Buradan anlıyoruz ki, `"Kahramanmaraş"` adlı karakter dizisi içinde toplam `5`
adet `"a"` karakteri geçiyor.

``count()`` metodu yaygın olarak yukarıdaki örnekte görüldüğü şekilde sadece tek
bir parametre ile kullanılır. Ama aslında bu metot toplam 3 parametre alır.
Şimdi şu örnekleri dikkatlice inceleyin::
    
    >>> şehir = "adana"
    >>> şehir.count("a")
    
    3
    
    >>> şehir.count("a", 1)
    
    2
    
    >>> şehir.count("a", 2)
    
    2
    
    >>> şehir.count("a", 3)
    
    1
    
    >>> şehir.count("a", 4)
    
    1
    
İlk örnekte ``count()`` metodunu tek bir parametre ile birlikte kullandığımız
için `"adana"` adlı karakter dizisi içindeki bütün `"a"` harflerinin toplam
sayısı çıktı olarak verildi.

İkinci örnekte ise ``count()`` metoduna ikinci bir parametre daha verdik. Bu
ikinci parametre, ``count()`` metodunun bir karakteri saymaya başlarken karakter
dizisinin kaçıncı sırasından başlayacağını gösteriyor. Bu örnekte ikinci
parametre olarak `1` sayısını verdiğimiz için, Python saymaya `"adana"` karakter
dizisinin `1.` sırasından başlayacak. Dolayısıyla `0.` sıradaki `"a"` harfi
sayım işleminin dışında kalacağı için toplam `"a"` sayısı `4` değil `3` olarak
görünecek. Gördüğünüz gibi, sonraki örneklerde de aynı mantığı takip ettiğimiz
için aradığımız karakterin toplam sayısı örnekten örneğe farklılık gösteriyor.

Peki bu metodu gerçek programlarda ne amaçla kullanabilirsiniz? Bu metodu
kullanarak, örneğin, kullanıcıyı aynı karakterden yalnızca bir adet girmeye
zorlayabilirsiniz. Bunun için mesela şöyle bir yapı kullanabilirsiniz::
    
    parola = input("parolanız: ")
    
    kontrol = True
    
    for i in parola:
        if parola.count(i) > 1:
            kontrol = False
    
    if kontrol:
        print('Parolanız onaylandı!')
    else:
        print('Parolanızda aynı harfi bir kez kullanabilirsiniz!')
        
Burada `kontrol` değişkeninin değerini `True` olarak belirledik. Eğer `parola`
içindeki harflerden herhangi biri 1'den fazla geçiyorsa bu durumda `kontrol`
değişkeninin değerini `False` yapıyoruz:: 

    for i in parola:
        if parola.count(i) > 1:
            kontrol = False
            
Daha sonra da `kontrol` değişkeninin durumuna göre kullanıcıya parolanın
onaylandığı veya onaylanmadığı bilgisini veriyoruz. Buna göre eğer `kontrol`
değişkeninin değeri `True` ise şu çıktıyı veriyoruz::
    
    Parolanız onaylandı!
   
Aksi halde şu çıktıyı veriyoruz::
    
    Parolanızda aynı harfi bir kez kullanabilirsiniz!

Yukarıdakine benzer durumların dışında ``count()`` metodunu şöyle durumlarda da
kullanabilirsiniz::

    kelime = input("Herhangi bir kelime: ")

    for harf in kelime:
        print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf, 
                                                               kelime, 
                                                               kelime.count(harf)))

Burada amacımız kullanıcının girdiği bir kelime içindeki bütün harflerin o
kelime içinde kaç kez geçtiğini bulmak. ``count()`` metodunu kullanarak bu işi
çok kolay bir şekilde halledebiliyoruz. Kullanıcının mesela 'adana' kelimesini
girdiğini varsayarsak yukarıdaki program şöyle bir çıktı verecektir::
    
    a harfi adana kelimesinde 3 kez geçiyor!
    d harfi adana kelimesinde 1 kez geçiyor!
    a harfi adana kelimesinde 3 kez geçiyor!
    n harfi adana kelimesinde 1 kez geçiyor!
    a harfi adana kelimesinde 3 kez geçiyor! 

Ancak burada şöyle bir problem var: 'adana' kelimesi içinde birden fazla geçen
harfler (mesela 'a' harfi) çıktıda birkaç kez tekrarlanıyor. Yani mesela 'a'
harfinin geçtiği her yerde programımız 'a' harfinin kelime içinde kaç kez
geçtiğini rapor ediyor. İstediğiniz davranış bu olabilir. Ama bazı durumlarda
her harfin kelime içinde kaç kez geçtiği bilgisinin yalnızca bir kez
raporlanmasını isteyebilirsiniz. Yani siz yukarıdaki gibi bir çıktı yerine şöyle
bir çıktı elde etmek istiyor olabilirsiniz::
    
    a harfi adana kelimesinde 3 kez geçiyor!
    d harfi adana kelimesinde 1 kez geçiyor!
    n harfi adana kelimesinde 1 kez geçiyor!

Böyle bir çıktı elde edebilmek için şöyle bir program yazabilirsiniz::

    kelime = input("Herhangi bir kelime: ")
    sayaç = ""

    for harf in kelime:
        if harf not in sayaç:
            sayaç += harf

    for harf in sayaç:
        print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf, 
                                                               kelime, 
                                                               kelime.count(harf)))

Gelin isterseniz bu kodları şöyle bir inceleyelim.

Bu kodlarda öncelikle kullanıcıdan herhangi bir kelime girmesini istiyoruz.

Daha sonra `sayaç` adlı bir değişken tanımlıyoruz. Bu değişken, kullanıcının
girdiği kelime içindeki harfleri tutacak. Bu değişken, `kelime` değişkeninden
farklı olarak, kullanıcının girdiği sözcük içinde birden fazla geçen harflerden
yalnızca tek bir örnek içerecek.

Değişkenimizi tanımladıktan sonra bir ``for`` döngüsü kuruyoruz. Bu döngüye
dikkatlice bakın. Kullanıcının girdiği kelime içinde geçen harflerden her birini
yalnızca bir kez alıp `sayaç` değişkenine gönderiyoruz. Böylece elimizde her
harften sadece bir adet olmuş oluyor. Burada Python'ın arka planda neler
çevirdiğini daha iyi anlayabilmek için isterseniz döngüden sonra şöyle bir satır
ekleyerek `sayaç` değişkeninin içeriğini inceleyebilir, böylece burada
kullandığımız ``for`` döngüsünün nasıl çalıştığını daha iyi görebilirsiniz::
    
    print("sayaç içeriği: ", sayaç)

İlk döngümüz sayesinde, kullanıcının girdiği kelime içindeki her harfi teke
indirerek, bu harfleri `sayaç` değişkeni içinde topladık. Şimdi yapmamız gereken
şey, `sayaç` değişkenine gönderilen her bir harfin, `kelime` adlı değişken
içinde kaç kez geçtiğini hesaplamak olmalı. Bunu da yine bir `for` döngüsü ile
yapabiliriz::
    
    for harf in sayaç:
        print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf, 
                                                               kelime, 
                                                               kelime.count(harf)))

Burada yaptığımız şey şu: ``count()`` metodunu kullanarak, `sayaç` değişkeninin
içindeki her bir harfin, `kelime` değişkeninin içinde kaç kez geçtiğini
buluyoruz. Bu döngünün nasıl çalıştığını daha iyi anlayabilmek için, isterseniz
bu döngüyü şu şekilde sadeleştirebilirsiniz::
    
    for harf in sayaç:
        print(harf, kelime, kelime.count(harf))

Gördüğünüz gibi, `sayaç` değişkeni içindeki herbir harfin `kelime` adlı karakter
dizisi içinde kaç kez geçtiğini tek tek sorguladık.

Yukarıdaki örneklerde ``count()`` metodunun iki farklı parametre aldığını
gördük. Bu metot bunların dışında üçüncü bir parametre daha alır. Bu üçüncü
parametre ikinci parametreyle ilişkilidir. Dilerseniz bu ilişkiyi bir örnek
üzerinde görelim::
    
    >>> kardiz = "python programlama dili"
    >>> kardiz.count("a")
    
    3
    
    >>> kardiz.count("a", 15)
    
    2

Bu örneklerden anladığımıza göre, `"python programlama dili"` adlı karakter
dizisi içinde toplam `3` adet 'a' harfi var. Eğer bu karakter dizisi içindeki
'a' harflerini karakter dizisinin en başından itibaren değil de, `15.`
karakterden itibaren saymaya başlarsak bu durumda `2` adet 'a' harfi buluyoruz.
Şimdi de şu örneğe bakalım::
    
    >>> kardiz.count("a", 15, 17)

    1

Burada, `15.` karakter ile `17.` karakter arasında kalan 'a' harflerini saymış
olduk. `15.` karakter ile `17.` karakter arasında toplam `1` adet 'a' harfi
olduğu için de Python bize `1` sonucunu verdi. Bütün bu örneklerden sonra
``count()`` metoduna ilişkin olarak şöyle bir tespitte bulunabiliriz:

    ``count()`` metodu bir karakter dizisi içinde belli bir karakterin kaç kez
    geçtiğini sorgulamamızı sağlar. Örneğin bu metodu ``count("a")`` şeklinde
    kullanırsak Python bize karakter dizisi içindeki bütün "a" harflerinin
    sayısını verecektir. Eğer bu metoda 2. ve 3. parametreleri de verirsek,
    sorgulama işlemi karakter dizisinin belli bir kısmında
    gerçekleştirilecektir. Örneğin ``count("a", 4, 7)`` gibi bir kullanım, bize
    karakter dizisinin 4. ve 7. karakterleri arasında kalan "a" harflerinin
    sayısını verecektir.
    
Böylece bir metodu daha ayrıntılı bir şekilde incelemiş olduk. Artık başka bir
metot incelemeye geçebiliriz.

index(), rindex()
=======================

Bu bölümün başında karakter dizilerinin dilimlenme özelliğinden söz ederken,
karakter dizisi içindeki her harfin bir sırası olduğunu söylemiştik. Örneğin
`"python"` adlı karakter dizisinde 'p' harfinin sırası `0`'dır. Aynı şekilde 'n'
harfinin sırası ise `5`'tir. Karakterlerin, bir karakter dizisi içinde hangi
sırada bulunduğunu öğrenmek için ``index()`` adlı bir metottan yararlanabiliriz.
Örneğin::
    
    >>> kardiz = "python"
    >>> kardiz.index("p")
    
    0
    
    >>> kardiz.index("n")
    
    5

Eğer sırasını sorguladığımız karakter, o karakter dizisi içinde bulunmuyorsa, bu
durumda Python bize bir hata mesajı gösterir::
    
    >>> kardiz.index("z")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: substring not found

Bu metodun özelliği, sorguladığımız karakterin, karakter dizisi içinde geçtiği
ilk konumu vermesidir. Yani örneğin::
    
    >>> kardiz = "adana"
    >>> kardiz.index("a")
    
    0

`"adana"` adlı karakter dizisi içinde `3` adet 'a' harfi var. Ancak biz
``index()`` metodu yardımıyla `"adana"` karakter dizisi içindeki 'a' harfinin
konumunu sorgularsak, Python bize 'a' harfinin geçtiği ilk konumu, yani `0.`
konumu, bildirecektir. Halbuki `"adana"` karakter dizisi içinde `2.` ve `4.`
sıralarda da birer 'a' harfi var. Ancak ``index()`` metodu `0.` konumdaki 'a'
harfini gördükten sonra karakter dizisinin geri kalanına bakmaz.

``index()`` metodunu biz yukarıda tek bir parametre ile birlikte kullandık. Bu
parametre, karakter dizisi içinde konumunu öğrenmek istediğimiz karakteri
gösteriyor. Ama bu metot aslında toplam `3` parametre alır. Şu örnekleri
dikkatlice inceleyelim::
    
    >>> kardiz = "adana"
    >>> kardiz.index("a")
    
    0

Burada normal bir şekilde ``index()`` metodunu tek bir parametre ile birlikte
kullandık. Böylece Python bize 'a' harfinin karakter dizisi içinde ilk olarak
hangi sırada bulunduğunu gösterdi. Bir de şu örneğe bakalım::
    
    >>> kardiz.index("a", 1)
    
    2

Gördüğünüz gibi, bu defa ``index()`` metoduna ikinci bir parametre daha verdik.
``index()`` metodunun ikinci parametresi, Python'ın aramaya kaçıncı sıradan
itibaren başlayacağını gösteriyor. Biz yukarıdaki örnekte Python'ın aramaya 1.
sıradan itibaren başlamasını istedik. Bu yüzden Python 0. sıradaki "a"
karakterini es geçti ve 2. sırada bulunan "a" karakterini gördü. Bir de şuna
bakalım::
    
    >>> kardiz.index("a", 3)

Bu defa Python'ın aramaya `3.` sıradan başlamasını istedik. Dolayısıyla Python
`0.` ve `2.` sıralardaki 'a' harflerini görmezden gelip bize `4.` sıradaki 'a'
harfinin sırasını bildirdi.

Gelelim ``index()`` metodunun `3.` parametresine... Dilerseniz `3.` parametrenin
ne işe yaradığını bir örnek üzerinde gösterelim::
    
    >>> kardiz = "adana"
    >>> kardiz.index("a", 1, 3)
    
    2

Hatırlarsanız, bundan önce ``count()`` adlı bir metot öğrenmiştik. O metot da
toplam `3` parametre alıyordu. ``count()`` metodunda kullandığımız `2.` ve `3.`
parametrelerin görevlerini hatırlıyor olmalısınız. İşte ``index()`` metodunun
`2.` ve `3.` parametreleri de aynen ``count()`` metodundaki gibi çalışır. Yani
Python'ın sorgulama işlemini hangi sıra aralıklarından gerçekleştireceğini
gösterir. Mesela yukarıdaki örnekte biz "adana" karakter dizisinin `1.` ve `3.`
sıraları arasındaki 'a' harflerini sorguladık. Yani yukarıdaki örnekte Python
'a' harfini aramaya `1.` konumdan başladı ve aramayı `3.` konumda kesti. Böylece
`"adana"` karakter dizisinin `2.` sırasındaki 'a' harfinin konumunu bize
bildirdi.

Gördüğünüz gibi, ``index()`` metodu bize aradığımız karakterin yalnızca ilk
konumunu bildiriyor. Peki biz mesela `"adana"` karakter dizisi içindeki bütün
'a' harflerinin sırasını öğrenmek istersek ne yapacağız?

Bu isteğimizi yerine getirmek için karakter dizisinin her bir sırasını tek tek
kontrol etmemiz yeterli olacaktır. Yani şöyle bir şey yazmamız gerekiyor::
    
    kardiz = "adana"

    print(kardiz.index("a", 0))
    print(kardiz.index("a", 1))
    print(kardiz.index("a", 2))
    print(kardiz.index("a", 3))
    print(kardiz.index("a", 4))

Buradaki mantığı anladığınızı sanıyorum. Bildiğiniz gibi, ``index()`` metodunun
ikinci parametresi sayesinde karakter dizisi içinde aradığımız bir karakteri
hangi konumdan itibaren arayacağımızı belirleyebiliyoruz. Örneğin yukarıdaki
kodlarda gördüğünüz ilk ``print()`` satırı 'a' karakterini `0.` konumdan
itibaren arıyor ve gördüğü ilk 'a' harfinin konumunu raporluyor. İkinci
``print()`` satırı 'a' karakterini `1.` konumdan itibaren arıyor ve gördüğü ilk
'a' harfinin konumunu raporluyor. Bu süreç karakter dizisinin sonuna
ulaşılıncaya kadar devam ediyor. Böylece karakter dizisi içinde geçen bütün 'a'
harflerinin konumunu elde etmiş oluyoruz.

Elbette yukarıdaki kodları, sadece işin mantığını anlamanızı sağlamak için bu
şekilde verdik. Tahmin edebileceğiniz gibi, yukarıdaki kod yazımı son derece
verimsiz bir yoldur. Ayrıca gördüğünüz gibi, yukarıdaki kodlar sadece `5`
karakter uzunluğundaki karakter dizileri için geçerlidir. Halbuki programlamada
esas alınması gereken yöntem, kodlarınızı olabildiğince genel amaçlı tutup,
farklı durumlarda da çalışabilmesini sağlamaktır. Dolayısıyla yukarıdaki mantığı
şu şekilde kodlara dökmek çok daha akıllıca bir yol olacaktır::
    
    kardiz = "adana"

    for i in range(len(kardiz)):
        print(kardiz.index("a", i))

Gördüğünüz gibi, yukarıdaki kodlar yardımıyla, bir önceki verimsiz kodları hem
kısalttık, hem de daha geniş kapsamlı bir hale getirdik. Hatta yukarıdaki
kodları şöyle yazarsanız karakter dizisi ve bu karakter dizisi içinde aranacak
karakteri kullanıcıdan da alabilirsiniz::
    
    kardiz = input("Metin girin: ")
    aranacak = input("Aradığınız harf: ")
    
    for i in range(len(kardiz)):
        print(kardiz.index(aranacak, i))

Bu kodlarda bazı problemler dikkatinizi çekmiş olmalı. Mesela, aranan karakter
dizisinin bulunduğu konumlar çıktıda tekrar ediyor. Örneğin, kullanıcının
`"adana"` karakter dizisi içinde 'a' harfini aramak istediğini varsayarsak
programımız şöyle bir çıktı veriyor::
    
    0
    2
    2
    4
    4 

Burada `2` ve `4` sayılarının birden fazla geçtiğini görüyoruz. Bunu engellemek
için şöyle bir kod yazabiliriz::
    
    kardiz = input("Metin girin: ")
    aranacak = input("Aradığınız harf: ")

    for i in range(len(kardiz)):
        if i == kardiz.index(aranacak, i):
            print(i)

Bu kodlarla yaptığımız şey şu: Öncelikle karakter dizisinin uzunluğunu gösteren
sayı aralığı üzerinde bir ``for`` döngüsü kuruyoruz. Kullanıcının burada yine
`"adana"` karakter dizisini girdiğini varsayarsak, `"adana"` karakter dizisinin
uzunluğu `5` olduğu için ``for`` döngümüz şöyle görünecektir::
    
    for i in range(5):
        ...

Daha sonra ``for`` döngüsü içinde tanımladığımız `i` değişkeninin değerinin,
karakter dizisi içinde aradığımız karakterin konumu ile eşleşip eşleşmediğini
kontrol ediyoruz ve değeri eşleşen sayıları ``print()`` fonksiyonunu kullanarak
ekrana döküyoruz.

Eğer bu kodlar ilk bakışta gözünüze anlaşılmaz göründüyse bu kodları bir de şu
şekilde yazarak arka planda neler olup bittiğini daha net görebilirsiniz::
    
    kardiz = input("Metin girin: ")
    aranacak = input("Aradığınız harf: ")

    for i in range(len(kardiz)):
        print("i'nin değeri: ", i)
        if i == kardiz.index(aranacak, i):
            print("%s. sırada 1 adet %s harfi bulunuyor" %(i, aranacak))
        else:
            print("%s. sırada %s harfi bulunmuyor" %(i, aranacak))

Gördüğünüz gibi ``index()`` metodu bir karakter dizisi içindeki karakterleri
ararken karakter dizisini soldan sağa doğru okuyor. Python'da bu işlemin tersi
de mümkündür. Yani isterseniz Python'ın, karakter dizisini soldan sağa doğru
değil de, sağdan sola doğru okumasını da sağlayabilirsiniz. Bu iş için
``rindex()`` adlı bir metottan yararlanacağız. Bu metot her yönden ``index()``
metoduyla aynıdır. ``index()`` ve ``rindex()`` metotlarının birbirinden tek
farkı, ``index()`` metodunun karakter dizilerini soldan sağa, ``rindex()``
metodunun ise sağdan sola doğru okumasıdır. Hemen bir örnekle durumu açıklamaya
çalışalım::
    
    >>> kardiz = "adana"
    >>> kardiz.index("a")
    
    0
    
    >>> kardiz.rindex("a")
    
    4

Bu iki örnek, ``index()`` ve ``rindex()`` metotları arasındaki farkı gayet net
bir şekilde ortaya koyuyor. ``index()`` metodu, karakter dizisini soldan sağa
doğru okuduğu için `"adana"` karakter dizisinin 0. sırasındaki 'a' harfini
yakaladı. ``rindex()`` metodu ise karakter dizisini sağdan sola doğru okuduğu
için `"adana"` karakter dizisinin `4.` sırasındaki 'a' harfini yakaladı...

find, rfind()
==============

``find()`` ve ``rfind()`` metotları tamamen ``index()`` ve ``rindex()``
metotlarına benzer. ``find()`` ve ``rfind()`` metotlarının görevi de bir
karakter dizisi içindeki bir karakterin konumunu sorgulamaktır::
    
    >>> kardiz = "adana"
    >>> kardiz.find("a")
    
    0
    
    >>> kardiz.rfind("a")
    
    4

Peki ``index()``/``rindex()`` ve ``find()``/``rfind()`` metotları arasında ne
fark var?

``index()`` ve ``rindex()`` metotları karakter dizisi içindeki karakteri
sorgularken, eğer o karakteri bulamazsa bir ``ValueError`` hatası verir::
    
    >>> kardiz = "adana"
    >>> kardiz.index("z")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: substring not found

Ama ``find()`` ve ``rfind()`` metotları böyle bir durumda -1 çıktısı verir::

    >>> kardiz = "adana"
    >>> kardiz.find("z")

    -1

Bu iki metot çifti arasındaki tek fark budur.


center()
=========

*Center* kelimesi İngilizce'de 'orta, merkez, ortalamak' gibi anlamlara gelir.
Bu anlama uygun olarak, ``center()`` metodunu karakter dizilerini ortalamak için
kullanabilirsiniz. Örneğin::
    
    for metot in dir(""):
        print(metot.center(15))

Gördüğünüz gibi ``center()`` metodu bir adet parametre alıyor. Bu parametre,
karakter dizisine uygulanacak ortalama işleminin genişliğini gösteriyor. Bu
parametrenin nasıl bir etki ortaya çıkardığını daha iyi anlayabilmek için
isterseniz bir iki basit örnek verelim::
    
    >>> kardiz = "python"

Burada `6` karakterlik bir karakter dizisi tanımladık. Şimdi dikkatlice bakın::

    >>> kardiz.center(1)
    
    'python'

Burada ise ``center()`` metoduna parametre olarak `1` sayısını verdik. Ancak bu
parametre karakter dizimizinin uzunluğundan az olduğu için çıktı üzerinde
herhangi bir etkisi olmadı. Bir de şuna bakalım::
    
    >>> kardiz.center(10)
    
    '  python  '

Çıktıdaki tırnak işaretlerine bakarak, 'python' kelimesinin ortalandığını
görebilirsiniz. Buradan şu sonucu çıkarıyoruz: ``center()`` metoduna verilen
genişlik parametresi aslında bir karakter dizisinin toplam kaç karakterlik bir
yer kaplayacağını gösteriyor. Mesela yukarıdaki örnekte bu metoda verdiğimiz
`10` sayısı ``"python"`` adlı karakter dizisinin toplam `10` karakterlik bir yer
kaplayacağını gösteriyor. Kaplanacak yere karakter dizisinin kendisi de
dahildir. Yani `10` olarak belirttiğimiz boşluk adedinin `6`'sı 'python'
kelimesinin kendisi tarafından işgal ediliyor. Geriye kalan `4` boşlukluk mesafe
ise karakter dizisinin sol ve sağ tarafına paylaştırılıyor.

``center()`` metodunun karakter dizileri üzerindeki etkisini daha net olarak
görmek için şöyle bir döngü kurabilirsiniz::

    >>> for i in range(1, 20):
    ...     kardiz.center(i)
    ...
    'python'
    'python'
    'python'
    'python'
    'python'
    'python'
    ' python'
    ' python '
    '  python '
    '  python  '
    '   python  '
    '   python   '
    '    python   '
    '    python    '
    '     python    '
    '     python     '
    '      python     '
    '      python      '
    '       python      '

Bu örnekte, karakter dizisinin her adımda nasıl ortaya doğru kaydığı açıkça
görülüyor. Dikkat ederseniz çıktının ilk altı satırında karakter dizisinin
konumu değişmiyor. Ancak ``center()`` metoduna verilen parametrenin değeri
karakter dizisinin uzunluğunu aştığı anda karakter dizisi ortaya doğru
ilerlemeye başlıyor.

``center()`` metodu genellikle yukarıdaki gösterdiğimiz şekilde tek bir
parametre ile birlikte kullanılır. Ancak bu metot aslında bir parametre daha
alır. Şu örneği inceleyelim::
    
    >>> kardiz = "elma"
    >>> kardiz.center(10, "-")

    '---elma---'

Gördüğünüz gibi, ``center()`` metoduna verdiğimiz `"-"` değeri sayesinde
`"elma"` karakteri ortalanırken, sağ ve sol taraftaki boşluklara da `"-"`
karakteri eklenmiş oldu.

rjust(), ljust()
================

Bu metotlar da tıpkı bir önceki ``center()`` metodu gibi karakter dizilerini
hizalama vazifesi görür. ``rjust()`` metodu bir karakter dizisini sağa
yaslarken, ``ljust()`` metodu karakter dizisini sola yaslar. Mesela şu iki kod
parçasının çıktılarını inceleyin::
    
    >>> for i in dir(""):
    ...     print(i.ljust(20))
    
    >>> for i in dir(""):
    ...     print(i.rjust(20))

``ljust()`` metodu bize özellikle karakter dizilerinin hizalama işlemlerinde
yardımcı oluyor. Bu metot yardımıyla karakter dizilerimizi sola yaslayıp, sağ
tarafına da istediğimiz karakterleri yerleştirebiliyoruz. Hemen bir örnek
verelim::
    
    >>> kardiz = "tel no"
    >>> kardiz.ljust(10, ".")

    'tel no....'
    
Burada olan şey şu: ``ljust()`` metodu, kendisine verilen `10` parametresinin
etkisiyle `10` karakterlik bir alan oluşturuyor. Bu 10 karakterlik alanın içine
önce `6` karakterlik yer kaplayan `"tel no"` ifadesini, geri kalan `4`
karakterlik boşluğa ise `"."` karakterini yerleştiriyor. Eğer ``ljust()``
metoduna verilen sayı karakter dizisinin uzunluğundan az yer tutarsa, karakter
dizisinin görünüşünde herhangi bir değişiklik olmayacaktır. Örneğin yukarıdaki
örnekte karakter dizimizin uzunluğu `6`. Dolayısıyla kodumuzu şu şekilde
yazarsak bir sonuç elde edemeyiz::
    
    >>> kardiz.ljust(5, ".")

    'tel no'
    
Gördüğünüz gibi, karakter dizisinde herhangi bir değişiklik olmadı. ``ljust()``
metoduna verdiğimiz `"."` karakterini görebilmemiz için, verdiğimiz sayı cinsli
parametrenin en az karakter dizisinin boyunun bir fazlası olması gerekir::
    
    >>> kardiz.ljust(7, ".")

    'tel no.'
    
``ljust()`` metoduyla ilgili basit bir örnek daha verelim::

    >>> for i in "elma", "armut", "patlıcan":
    ...     i.ljust(10, ".")
    ...
    'elma......'
    'armut.....'
    'patlıcan..'
    
Gördüğünüz gibi, bu metot karakter dizilerini şık bir biçimde sola hizalamamıza
yardımcı oluyor.

``rjust()`` metodu ise, ``ljust()`` metodunun yaptığı işin tam tersini yapar.
Yani karakter dizilerini sola değil sağa yaslar::
    
    >>> for i in "elma", "armut", "patlıcan":
    ...     i.rjust(10, ".")
    ...
    '......elma'
    '.....armut'
    '..patlıcan'

``ljust()`` ve ``rjust()`` metotları, kullanıcılarınıza göstereceğiniz
çıktıların düzgün görünmesini sağlamak açısından oldukça faydalıdır.    

zfill()
========

Bu metot kimi yerlerde işimizi epey kolaylaştırabilir. ``zfill()`` metodu
yardımıyla karakter dizilerinin sol tarafına istediğimiz sayıda sıfır
ekleyebiliriz::
    
    >>> a = "12"
    >>> a.zfill(3)

    '012'
    
Bu metodu şöyle bir iş için kullanabilirsiniz::

    >>> for i in range(11):
    ...     print(str(i).zfill(2))
    00
    01
    02
    03
    04
    05
    06
    07
    08
    09
    10
    
Burada ``str()`` fonksiyonunu kullanarak, ``range()`` fonksiyonundan elde
ettiğimiz sayıları birer karakter dizisine çevirdiğimize dikkat edin. Çünkü
``zfill()`` karakter dizilerinin bir metodudur. Sayıların değil...

partition(), rpartition()
==========================

Bu metot yardımıyla bir karakter dizisini belli bir ölçüte göre üçe bölüyoruz.
Örneğin::
    
    >>> a = "istanbul"
    >>> a.partition("an")
    
    ('ist', 'an', 'bul')
    
Eğer ``partition()`` metoduna parantez içinde verdiğimiz ölçüt karakter dizisi
içinde bulunmuyorsa şu sonuçla karşılaşırız::
    
    >>> a = "istanbul"
    >>> a.partition("h")
    
    ('istanbul', '', '')

Gelelim ``rpartition()`` metoduna... Bu metot da ``partition()`` metodu ile aynı
işi yapar, ama yöntemi biraz farklıdır. ``partition()`` metodu karakter
dizilerini soldan sağa doğru okur. ``rpartition()`` metodu ise sağdan sola
doğru. Peki bu durumun ne gibi bir sonucu vardır? Hemen görelim::
    
    >>> b = "istihza"
    >>> b.partition("i")

    ('', 'i', 'stihza')
    
Gördüğünüz gibi, ``partition()`` metodu karakter dizisini ilk 'i' harfinden
böldü. Şimdi aynı işlemi ``rpartition()`` metodu ile yapalım::
    
    >>> b.rpartition("i")

    ('ist', 'i', 'hza')
    
``rpartition()`` metodu ise, karakter dizisini sağdan sola doğru okuduğu için
ilk 'i' harfinden değil, son 'i' harfinden böldü karakter dizisini.

``partition()`` ve ``rpartition()`` metotları, ölçütün karakter dizisi içinde
bulunmadığı durumlarda da farklı tepkiler verir::
    
    >>> b.partition("g")

    ('istihza', '', '')

    >>> b.rpartition("g")

    ('', '', 'istihza')
    
Gördüğünüz gibi, ``partition()`` metodu boş karakter dizilerini sağa doğru
yaslarken, ``rpartition()`` metodu sola doğru yasladı.

encode()
=========

Bu metot yardımıyla karakter dizilerimizi istediğimiz kodlama sistemine göre
kodlayabiliriz. Python 3.x'te varsayılan karakter kodlaması `utf-8`'dir. Eğer
istersek şu karakter dizisini `utf-8` yerine `cp1254` ile kodlayabiliriz::
    
    >>> "çilek".encode("cp1254")

expandtabs()
============

Bu metot yardımıyla bir karakter dizisi içindeki sekme boşluklarını
genişletebiliyoruz. Örneğin::
    
    >>> a = "elma\tbir\tmeyvedir"
    >>> a.expandtabs(10)

    'elma   bir     meyvedir'

Böylece bir metot grubunu daha geride bırakmış olduk. Gördüğünüz gibi bazı
metotlar sıklıkla kullanılabilme potansiyeli taşırken, bazı metotlar pek öyle
sık kullanılacakmış gibi görünmüyor...

Sonraki bölümde metotları incelemeye devam edeceğiz.
