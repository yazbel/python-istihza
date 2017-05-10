.. meta::
   :description: Bu bölümde sayılar ve sayı sistemleri konusundan söz edeceğiz.
   :keywords: python, python3, sayma sistemleri, ikili, binary, hex, oct, bin,
              int, ikili, onaltılı, sekizli, onlu

.. highlight:: py3

*****************
Sayma Sistemleri
*****************

Sayılar olmadan bilgisayar ve programlama düşünülemez. O yüzden, önceki
derslerimizde karakter dizilerini anlatırken şöyle bir değinip geçtiğimiz
sayılar konusunu, sayma sistemleri konusunu da ilave ederek, birer programcı
adayı olan bizleri yakından ilgilendirdiği için mümkün olduğunca ayrıntılı bir
şekilde ele almaya çalışacağız.

Sayılar ve Sayma Sistemleri konusunu iki farklı bölümde inceleyeceğiz.

Sayılar konusunun temelini oluşturduğu için, öncelikle sayma sistemlerinden söz
edelim.

Öncelikle 'sayma sistemi' kavramını tanımlayarak işe başlayalım. Nedir bu 'sayma
sistemi' denen şey?

Sayma işleminin hangi ölçütlere göre yapılacağını belirleyen kurallar bütününe
sayma sistemi adı verilir.

Dünyada yaygın olarak kullanılan dört farklı sayma sistemi vardır. Bunlar, onlu,
sekizli, on altılı ve ikili sayma sistemleridir. Bu dördü arasında en yaygın
kullanılan sayma sistemi ise, tabii ki, onlu sistemdir. İnsanların elleri ve
ayaklarında on parmak olduğunu düşünürsek, bu sistemin neden daha yaygın
kullanıldığını anlamak aslında hiç de zor değil!

Onlu sistemin yaygınlığını düşünerek, sayma sistemleri konusunu anlatmaya onlu
sayma sisteminden başlayalım.

Onlu Sayma Sistemi
*******************

Biz insanlar genellikle hesap işlemleri için onlu sayma sistemini kullanırız.
Hepinizin bildiği gibi bu sistem; `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` ve
`9` olmak üzere toplam on rakamdan oluşur. Yani sayıları gösteren, birbirinden
farklı toplam on simge (rakam) vardır bu sistemde. Bu on simgeyi kullanarak,
olası bütün sayıları gösterebiliriz.

Bu arada terminoloji ile ilgili ufak bir açıklama yapalım:

Rakamlar, sayıları göstermeye yarayan simgelerdir. Onlu sayma sisteminde toplam
on farklı rakam vardır. Bütün rakamlar birer sayıdır, ama bütün sayılar birer
rakam değildir. Örneğin `8` hem bir rakam hem de bir sayıdır. Ancak mesela `32`
bir sayı olup bu sayı, `3` ve `2` adlı iki farklı rakamın bir araya getirilmesi
ile gösterilir. Yani `32` sayısı tek başına bir rakam değildir.

Açıklamamızı da yaptığımıza göre yolumuza devam edebiliriz.

İnsanlar yukarıda bahsettiğimiz bu onlu sisteme ve bu sistemi oluşturan
rakamlara/simgelere o kadar alışmıştır ki, çoğu zaman başka bir sistemin
varlığından veya var olma olasılığından haberdar bile değildir.

Ama elbette dünya üzerindeki tek sayma sistemi onlu sistem olmadığı gibi,
sayıları göstermek için kullanılabilecek rakamlar da yukarıdakilerle sınırlı
değildir.

Nihayetinde rakam dediğimiz şeyler insan icadı birtakım simgelerden ibarettir.
Elbette doğada '2' veya '7' diye bir şey bulunmaz. Bizim yaygın olarak
yukarıdaki şekilde gösterdiğimiz rakamlar Arap rakamlarıdır. Mesela Romalılar
yukarıdakiler yerine I, II, III, IV, V, VI, VII, VIII, IX ve X gibi farklı
simgeler kullanıyordu... Neticede `2` ve `II` aynı kavrama işaret ediyor. Sadece
kullanılan simgeler birbirinden farklı, o kadar.

Onlu sayma sisteminde bir sayıyı oluşturan rakamlar `10`'un kuvvetleri olarak
hesaplanır. Örneğin `1980` sayısını ele alalım. Bu sayıyı `10`'un kuvvetlerini
kullanarak şu şekilde hesaplayabiliriz::
    
    >>> (0 * (10 ** 0)) + (8 * (10 ** 1)) + (9 * (10 ** 2)) + (1 * (10 ** 3))
    
    1980
    
Gördüğünüz gibi, sayının en sağındaki basamak `10`'un `0.` kuvveti olacak
şekilde, sola doğru kuvveti artırarak ilerliyoruz. 

Gelelim öteki sayma sistemlerine...
    
Sekizli Sayma Sistemi
**********************

Onlu sayma sisteminin aksine sekizli sayma sisteminde toplam sekiz rakam
bulunur. Bu rakamlar şunlardır:

    0, 1, 2, 3, 4, 5, 6, 7

Gördüğünüz gibi, onlu sistemde toplam on farklı simge varken, sekizli sistemde
toplam sekiz farklı simge var. 

Bu bölümün en başında da söylediğimiz gibi, insanlar onlu sayma sistemine ve bu
sistemi oluşturan simgelere o kadar alışmıştır ki, çoğu zaman başka bir sistemin
varlığından veya var olma olasılığından haberdar bile değildir. Hatta başka
sayma sistemlerinden bir vesileyle haberdar olup, bu sistemleri öğrenmeye
çalışanlar onlu sayma sistemine olan alışkanlıkları nedeniyle yeni sayma
sistemlerini anlamakta dahi zorluk çekebilirler. Bunun birincil nedeni,
iyi tanıdıklarını zannettikleri onlu sistemi de aslında o kadar iyi tanımıyor
olmalarıdır. 

O halde başka sayma sistemlerini daha iyi anlayabilmek için öncelikle yaygın
olarak kullandığımız sayma sisteminin nasıl işlediğini anlamaya çalışalım:

Onlu sistemde toplam on farklı simge bulunur: 
    
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        
`9`'dan büyük bir sayıyı göstermek gerektiğinde simge listesinin en başına
dönülür ve basamak sayısı bir artırılarak, semboller birleştirilir:

    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ..., 99, 100, ..., 999, 1000
    
İşte bu kural öteki sayma sistemleri için de geçerlidir. Mesela sekizli sayma
sistemini ele alalım.

Dediğimiz gibi, sekizli sistemde toplam sekiz farklı simge bulunur:

    0, 1, 2, 3, 4, 5, 6, 7 
    
Bu sistemde `7`'den büyük bir sayıyı göstermek gerektiğinde, tıpkı onlu sistemde
olduğu gibi, simge listesinin en başına dönüyoruz ve basamak sayısını bir
artırarak sembolleri birleştiriyoruz:

    10, 11, 12, 13, 14, 15, 16, 17, 20, ..., 77, 100
    
Onlu sayma sistemi ile sekizli sayma sistemi arasındaki farkı daha belirgin bir
şekilde görebilmek için şu kodları yazalım::
    
    sayı_sistemleri = ["onlu", "sekizli"]

    print(("{:^5} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
    
    for i in range(17):
        print("{0:^5} {0:^5o}".format(i))
        
Bu kodlarda öğrenmediğimiz ve anlayamayacağımız hiçbir şey yok. Bu kodları
oluşturan bütün parçaları önceki derslerimizde ayrıntılı olarak incelemiştik.
        
Bu kodlardan şöyle bir çıktı alacağız::

    onlu  sekizli
      0     0
      1     1
      2     2
      3     3
      4     4
      5     5
      6     6
      7     7
      8    10
      9    11
     10    12
     11    13
     12    14
     13    15
     14    16
     15    17
     16    20

Gördüğünüz gibi, onlu sistemde elimizde toplam on farklı simge olduğu için,
elimizdeki simgeleri kullanarak 10. sayıya kadar ilerleyebiliyoruz. Bu noktadan
sonra simge stoğumuz tükendiği için en başa dönüp bir basamak artırıyoruz ve
simgeleri birbiriyle birleştirerek yeni sayılar elde ediyoruz. 

Sekizli sistemde ise elimizde yalnızca sekiz farklı simge olduğu için,
elimizdeki simgeleri kullanarak ancak 8. sayıya kadar gelebiliyoruz. Öteki
sayıları gösterebilmek için bu noktadan sonra başa dönüp bir artırmamız ve
simgeleri birbiriyle birleştirerek yeni sayılar elde etmemiz gerekiyor. 

Sekizli sayma sisteminde bir sayıyı oluşturan rakamlar `8`'in kuvvetleri olarak
hesaplanır. Örneğin sekizli sayma sistemindeki `3674` sayısını ele alalım. Bu
sayıyı `8`'in kuvvetlerini kullanarak şu şekilde hesaplayabiliriz::
    
    >>> (4 * (8 ** 0)) + (7 * (8 ** 1)) + (6 * (8 ** 2)) + (3 * (8 ** 3))
    
    1980
    
Bu hesaplama şeklini onlu sayma sisteminden hatırlıyor olmalısınız. Gördüğünüz
gibi, sekizli sistemdeki bir sayının her bir basamağını `8`'in kuvvetleri olarak
hesapladığımızda, bu sayının onlu sistemdeki karşılığını elde ediyoruz. 

..
    sayı = 3456
    taban = 8
    basamak = 0
    toplam = []
    
    sayı_kardiz = str(sayı)
    sayı_uzunluğu = len(sayı_kardiz)
    
    while basamak <= sayı_uzunluğu-1:
        toplam.append(int(sayı_kardiz[0-(basamak+1)]) * pow(taban, basamak))
        basamak += 1  
        
    print(sum(toplam))

On Altılı Sayma Sistemi
***********************

Şu ana kadar onlu ve sekizli sayma sistemlerinden bahsettik. Önemli bir başka
sayma sistemi de on altılı sayma sistemidir. 

Onlu sayma sisteminde on farklı rakam, sekizli sayma sisteminde sekiz farklı
rakam olduğunu öğrenmiştik. On altılı sayma sisteminde ise, tahmin
edebileceğiniz gibi, on altı farklı rakam bulunur:

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
    
Şimdiye kadar öğrenmiş olduğumuz sayma sistemleri arasındaki farkı daha net
görmek için biraz önce yazdığımız kodlara on altılı sayma sistemini de
ekleyelim::
    
    sayı_sistemleri = ["onlu", "sekizli", "on altılı"]
    
    print(("{:^8} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
    
    for i in range(17):
        print("{0:^8} {0:^8o} {0:^8x}".format(i))
        
Buradan şöyle bir çıktı alacağız::
    
    onlu   sekizli  on altılı
     0        0        0
     1        1        1
     2        2        2
     3        3        3
     4        4        4
     5        5        5
     6        6        6
     7        7        7
     8        10       8
     9        11       9
     10       12       a
     11       13       b
     12       14       c
     13       15       d
     14       16       e
     15       17       f
     16       20       10    
    
Gördüğünüz gibi, onlu sistemde birbirinden farklı toplam `10` adet rakam/simge
varken, sekizli sistemde toplam `8` farklı simge, on altılı sistemde ise toplam
`16` farklı simge var. Yani onlu sistemde olası bütün sayılar eldeki `10` farklı
simge ve bunların kombinasyonunun kullanılması yoluyla; sekizli sistemde `8`
farklı simge ve bunların kombinasyonunun kullanılması yoluyla; on altılı
sistemde ise `16` farklı simge ve bunların kombinasyonunun kullanılması yoluyla
gösteriliyor. Bu sebeple onlu sistemde `9` sayısından itibaren bir basamak
artırılıp simge listesinin başına dönülürken, sekizli sistemde `7` sayısından
itibaren; on altılı sistemde ise `f` sayısından itibaren başa dönülüyor.

On altılı sistemde `9` sayısından sonra gelen harfleri yadırgamış olabilirsiniz.
Bu durumu şöyle düşünün: Sayı dediğimiz şeyler insan icadı birtakım simgelerden
ibarettir. Daha önce de söylediğimiz gibi, doğada '2' veya '7' diye bir şey
göremezsiniz...

İşte on altılık sistemdeki sayıları gösterebilmek için de birtakım simgelere
ihtiyaç var. İlk on simge, onluk sayma sistemindekilerle aynı. Ancak `10`'dan
sonraki sayıları gösterebilmek için elimizde başka simge yok. On altılık sistemi
tasarlayanlar, bir tercih sonucu olarak, eksik sembolleri alfabe harfleriyle
tamamlamayı tercih etmişler. Alfabe harfleri yerine pekala Roma rakamlarını da
tercih edebilirlerdi. Eğer bu sistemi tasarlayanlar böyle tercih etmiş olsaydı
bugün on altılık sistemi şöyle gösteriyor olabilirdik::
    
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    I
    II
    III
    IV
    V
    VI
    
Bugün bu sayıları bu şekilde kullanmıyor olmamızın tek sebebi, sistemi
tasarlayanların bunu böyle tercih etmemiş olmasıdır...

On altılı sayma sisteminde bir sayıyı oluşturan rakamlar `16`'nın kuvvetleri
olarak hesaplanır. Peki ama bu sayma sistemindeki `a`, `b`, `c`, `d`, `e` ve `f`
harfleriyle nasıl aritmetik işlem yapacağız? Örneğin on altılı sayma
sistemindeki `7bc` sayısını ele alalım. Bu sayının onlu sistemdeki karşılığını
`16`'nın kuvvetlerini kullanarak hesaplayabiliriz hesaplamasına, ama peki
yukarıda bahsettiğimiz harfler ne olacak? Yani şöyle bir işlem tabii ki mümkün
değil::
    
    >>> ((c * 16 ** 0)) + ((b * 16 ** 1)) + ((7 * 16 ** 2))
            
Elbette `c` ve `b` sayılarını herhangi bir aritmetik işlemde kullanamayız. Bunun
yerine, bu harflerin onlu sistemdeki karşılıklarını kullanacağız:

    a --> 10
    
    b --> 11
    
    c --> 12
    
    d --> 13
    
    e --> 14
    
    f --> 15
    
Buna göre::
    
    >>> ((12 * (16 ** 0)) + ((11 * (16 ** 1)) + ((7 * (16 ** 2))
    
    1980
    
Demek ki on altılı sistemdeki '7bc' sayısının onlu sistemdeki karşılığı
`1980`'miş.

İkili Sayma Sistemi
********************
    
Bildiğiniz, veya orada burada duymuş olabileceğiniz gibi, bilgisayarların
temelinde iki tane sayı vardır: `0` ve `1`. Bilgisayarlar bütün işlemleri sadece
bu iki sayı ile yerine getirir. 

Onlu, sekizli ve on altılı sayı sistemleri dışında, özellikle bilgisayarların
altyapısında tercih edilen bir başka sayı sistemi daha bulunur. İşte bu sistemin
adı ikili (*binary*) sayı sistemidir. Nasıl onlu sistemde `10`, sekizli sistemde
`8`, on altılı sistemde ise sayıları gösteren `16` farklı simge varsa, bu sayı
sisteminde de sayıları gösteren toplam iki farklı sembol vardır: `0` ve `1`. 

İkili sayı sisteminde olası bütün sayılar işte bu iki simge ile gösterilir. 

Gelin isterseniz durumu daha net bir şekilde görebilmek için yukarıda verdiğimiz
sayı sistemi tablosuna ikili sayıları da ekleyelim::

    sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
    
    print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
    
    for i in range(17):
        print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
        
Bu kodlar şu çıktıyı verecektir::
    
    onlu     sekizli  on altılı   ikili
     0         0         0         0
     1         1         1         1
     2         2         2        10
     3         3         3        11
     4         4         4        100
     5         5         5        101
     6         6         6        110
     7         7         7        111
     8         10        8        1000
     9         11        9        1001
     10        12        a        1010
     11        13        b        1011
     12        14        c        1100
     13        15        d        1101
     14        16        e        1110
     15        17        f        1111
     16        20       10        10000

Burada, onlu, sekizli ve on altılı sayı sistemleri için geçerli olan durumun
aynen ikili sayı sistemi için de geçerli olduğunu rahatlıkla görebiliyoruz.
İkili sayı sistemindeki mevcut sayıları gösterebilmemiz için toplam iki farklı
simge var. Bunlar: `0` ve `1`. İkili sayı sisteminde `0` ve `1` diye saymaya
başlayıp üçüncü sayıyı söylememiz gerektiğinde, elimizde `0` ve `1`'den başka
simge olmadığı için bir basamak artırıp simge listesinin başına dönüyoruz ve
böylece onluk düzendeki `2` sayısını ikili düzende gösterebilmek için `0` ve
`1`'den sonra `10` simgesini kullanıyoruz.

Bu söylediklerimizden sonra İnternet üzerinde sıkça karşılaştığınız şu sözün
anlamını herhalde artık daha iyi anlıyor olmalısınız:

    İnsanlar 10'a ayrılır: İkili sistemi bilenler ve bilmeyenler!

Bu arada, elbette ikili düzendeki `10` sayısı 'on' şeklinde telaffuz edilmiyor.
Bu sayıyı "bir-sıfır" diye seslendiriyoruz... 

İkili sayma sisteminde bir sayıyı oluşturan rakamlar `2`'nin kuvvetleri olarak
hesaplanır. Örneğin ikili sayma sistemindeki `1100` sayısını ele alalım. Bu
sayıyı `2`'nin kuvvetlerini kullanarak şu şekilde hesaplayabiliriz::

    >>> (0 * (2 ** 0)) + (0 * (2 ** 1)) + (1 * (2 ** 2)) + (1 * (2 ** 3))
    
    12
    
Demek ki '1100' sayısı onlu sistemde `12` sayısına karşılık geliyormuş.
    
Sayma Sistemlerini Birbirine Dönüştürme
**********************************************

Sıklıkla kullanılan dört farklı sayma sistemini öğrendik. Peki biz bir sayma
sisteminden öbürüne dönüştürme işlemi yapmak istersek ne olacak? Örneğin onlu
sistemdeki bir sayıyı ikili sisteme nasıl çevireceğiz? 

Python programlama dilinde bu tür işlemleri kolaylıkla yapmamızı sağlayan
birtakım fonksiyonlar bulunur. Ayrıca özel fonksiyonları kullanmanın yanısıra
karakter dizisi biçimlendirme (*string formatting*) yöntemlerini kullanarak da
sayma sistemlerini birbirine dönüştürebiliriz. Biz burada her iki yöntemi de tek
tek inceleyeceğiz. 

Gelin isterseniz bu dönüştürme işlemleri için hangi özel fonksiyonların olduğuna
bakalım önce. 

Fonksiyon Kullanarak
====================

bin()
-------

Bu fonksiyon bir sayının ikili (*binary*) sayı sistemindeki karşılığını verir::
    
    >>> bin(2)
    
    '0b10'
    
Bu fonksiyonun çıktı olarak bir karakter dizisi verdiğine dikkat edin. Bu
karakter dizisinin ilk iki karakteri (`'0b'`), o sayının ikili sisteme ait bir
sayı olduğunu gösteren bir işarettir. Bu bilgilerden yola çıkarak, yukarıdaki
karakter dizisinin gerçek ikili kısmını almak için şu yöntemi
kullanabilirsiniz::
    
    >>> bin(2)[2:]
    
    '10'

hex()
-------

Bu fonksiyon, herhangi bir sayıyı alıp, o sayının on altılı sistemdeki
karşılığını verir::
    
    >>> hex(10)
    
    'Oxa'
    
Tıpkı ``bin()`` fonksiyonunda olduğu gibi, ``hex()`` fonksiyonunun da çıktı
olarak bir karakter dizisi verdiğine dikkat edin. Hatırlarsanız ``bin()``
fonksiyonunun çıktısındaki ilk iki karakter (`0b`), o sayının ikili sisteme ait
bir sayı olduğunu gösteren bir işaret olarak kullanılıyordu. ``hex()``
fonksiyonunun çıktısındaki ilk iki karakter de (`0x`), o sayının on altılı
sisteme ait bir sayı olduğunu gösteriyor.

oct()
-------

Bu fonksiyon, herhangi bir sayıyı alıp, o sayının sekizli sistemdeki karşılığını
verir::
    
    >>> oct(10)
    
    '0o12'
    
Tıpkı ``bin()`` ve ``hex()`` fonksiyonlarında olduğu gibi, ``oct()``
fonksiyonunun da çıktı olarak bir karakter dizisi verdiğine dikkat edin.
Hatırlarsanız ``bin()`` ve ``hex()`` fonksiyonlarının çıktısındaki ilk iki
karakter (`0b` ve `0x`), o sayıların hangi sisteme ait sayılar olduğunu
gösteriyordu. Aynı şekilde ``oct()`` fonksiyonunun çıktısındaki ilk iki karakter
de (`0o`), o sayının sekizli sisteme ait bir sayı olduğunu gösteriyor.

int()
-------

Aslında biz bu fonksiyonu yakından tanıyoruz. Bildiğiniz gibi bu fonksiyon
herhangi bir sayı veya sayı değerli karakter dizisini tam sayıya (*integer*)
dönüştürmek için kullanılıyor. ``int()`` fonksiyonunun şimdiye kadar gördüğümüz
işlevi dışında bir işlevi daha bulunur: Biz bu fonksiyonu kullanarak herhangi
bir sayıyı onlu sistemdeki karşılığına dönüştürebiliriz::
    
    >>> int('7bc', 16)
    
    1980
    
Gördüğünüz gibi, bu fonksiyonu kullanırken dikkat etmemiz gereken bazı noktalar
var. İlkin, eğer ``int()`` fonksiyonunu yukarıdaki gibi bir dönüştürme işlemi için
kullanacaksak, bu fonksiyona verdiğimiz ilk parametrenin bir karakter
dizisi olması gerekiyor. Dikkat etmemiz gereken ikinci nokta, ``int()``
fonksiyonuna verdiğimiz ikinci parametrenin niteliği. Bu parametre, dönüştürmek
istediğimiz sayının hangi tabanda olduğunu gösteriyor. Yukarıdaki örneğe göre
biz, on altı tabanındaki `7bc` sayısını on tabanına dönüştürmek istiyoruz. 

Bir de şu örneklere bakalım::
    
    >>> int('1100', 2)
    
    12
    
    >>> int('1100', 16)
    
    4352
    
İlk örnekte, ikili sistemdeki `1100` sayısını onlu sisteme çeviriyoruz ve `12`
sayısını elde ediyoruz. İkinci örnekte ise on altılı sistemdeki `1100` sayısını
onlu sisteme çeviriyoruz ve `4352` sayısını elde ediyoruz. 

Biçimlendirme Yoluyla
=====================

Esasında biz karakter dizisi biçimlendirme yöntemlerini kullanarak dönüştürme
işlemlerini nasıl gerçekleştireceğimizi biliyoruz. Biz burada zaten öğrendiğimiz
bu bilgileri tekrar ederek öğrendiklerimizi pekiştirme amacı güdeceğiz. 

b
--

Bu karakteri kullanarak bir sayıyı ikili düzendeki karşılığına
dönüştürebiliriz::
    
    >>> '{:b}'.format(12)
    
    '1100'
    
Bu karakter, ``bin()`` fonksiyonuyla aynı işi yapar.

x
--

Bu karakteri kullanarak bir sayıyı on altılı düzendeki karşılığına
dönüştürebiliriz::
    
    >>> '{:x}'.format(1980)
    
    '7bc'
    
Bu karakter, ``hex()`` fonksiyonuyla aynı işi yapar.

o
--

Bu karakteri kullanarak bir sayıyı sekizli düzendeki karşılığına
dönüştürebiliriz::
    
    >>> '{:o}'.format(1980)
    
    '3674'
    
Bu karakter, ``oct()`` fonksiyonuyla aynı işi yapar.

Bütün bu anlattıklarımızdan sonra (eğer o zaman anlamakta zorluk çekmişseniz)
aşağıdaki kodları daha iyi anlamış olmalısınız::
    
    sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
    
    print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
    
    for i in range(17):
        print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
        
Bu arada, yukarıda bir sayının, karakter dizisi biçimlendirme yöntemleri
kullanılarak ikili, sekizli ve on altılı düzene nasıl çevrileceğini gördük. Bir
sayıyı onlu düzene çevirmek için ise sadece ``int()`` fonksiyonunu
kullanabiliyoruz. Böyle bir çevirme işlemini karakter dizisi biçimlendirme
yöntemlerini kullanarak yapamıyoruz. Ama elbette, eğer başka bir sayma
sisteminden onlu sisteme çevirdiğiniz bir sayıyı herhangi bir karakter dizisi
içinde biçimlendirmek isterseniz şöyle bir kod kullanabilirsiniz::
    
     >>> n = '7bc'
     >>> "{} sayısının onlu karşılığı {:d} sayısıdır.".format(n, int(n, 16))
     
...veya::
    
    >>> n = '7bc'
    >>> "{} sayısının onlu karşılığı {} sayısıdır.".format(n, int(n, 16))
    
Zira bildiğiniz gibi, Python'da onlu sayıları temsil eden harf `d` harfidir.
Eğer `{}` yapısı içinde herhangi bir harf kullanmazsanız yukarıdaki durumda
Python `{:d}` yazmışsınız gibi davranacaktır.

Sayma Sistemlerinin Birbirlerine Karşı Avantajları
***************************************************

Böylece dört farklı sayı sisteminin hangi mantık üzerine işlediğini anlamış
olduk. Ayrıca sayı sistemleri arasında dönüştürme işlemlerini de öğrendik. 

İşte bilgisayarlar bu sayı sistemleri arasında sadece ikili sayı sistemini
'anlayabilir'. Aslında bu da hiç mantıksız değil. Bilgisayar dediğimiz şey,
üzerinden elektrik geçen devrelerden ibaret bir makinedir. Eğer bir devrede
elektrik yoksa o devrenin değeri ~0 volt iken, o devreden elektrik geçtiğinde
devrenin değeri ~5 volttur. Gördüğünüz gibi, ortada iki farklı değer var: ~0
volt ve ~5 volt. Yukarıda anlattığımız gibi, ikili (*binary*) sayma sisteminde
de iki değer bulunur: `0` ve `1`. Dolayısıyla ikili sayma sistemi bilgisayarın
iç işleyişine en uygun sistemdir. ikili sistemde ~0 volt'u 0 ile, ~5 volt'u ise
`1` ile temsil edebiliyoruz. Yani devreden elektrik geçtiğinde o devrenin değeri
`1`, elektrik geçmediğinde ise `0` olmuş oluyor. Tabii bilgisayar açısından
bakıldığında devrede elektrik vardır veya yoktur. Biz insanlar bu ikili durumu
daha kolay bir şekilde temsil edebilmek için her bir duruma `0` ve `1` gibi bir
ad veriyoruz.

Bilgisayarın işlemcisi sadece bu iki farklı durumu kullanarak her türlü
hesaplama işlemini gerçekleştirebilir. Bu sebeple ikili sayı sistemi
bilgisayarın çalışma mantığı için gayet yeterli ve uygundur. İkili sayı sistemi
yerine mesela onlu sayı sistemini kullanmak herhalde simge israfından başka bir
şey olmazdı. Neticede, dediğimiz gibi, bilgisayarın işleyebilmesi için iki
farklı simge yeterlidir.

Dediğimiz gibi, ikili sayma sistemi bilgisayarın yapısına gayet uygundur. Ama
biz insanlar açısından sadece iki simge yardımıyla saymaya çalışmak epey zor
olacaktır. Ayrıca sayı büyüdükçe, ikili sistemde sayının kapladığı alan hızla ve
kolayca artacak, yığılan bu sayıları idare etmek hiç de kolay olmayacaktır. İşte
bu noktada devreye on altılı (*hexadecimal*) sayılar girer. Bu sayma sisteminde
toplam `16` farklı rakam/simge olduğu için, büyük sayılar çok daha az yer
kaplayacak şekilde gösterilebilir. 

Bildiğiniz gibi, ikili sayma sistemindeki herbir basamağa 'bit' adı verilir.
İkili sayma sistemini kullanarak, `0`'dan `256`'ya kadar sayabilmek için toplam
`8` bitlik (yani `8` hanelik) bir yer kullanmanız gerekir. On altılı sistemde
ise bu işlemi sadece iki basamakla halledebilirsiniz. Yani on altılı sistemde 00
ile FF arasına toplam 255 tane sayı sığdırılabilir. Dolayısıyla on altılı
sistemi kullanarak, çok büyük sayıları çok az yer kullanarak gösterebilirsiniz::
    
    >>> for i in range(256):
    ...     print(i, bin(i)[2:], hex(i)[2:])
    ...
    0 0 0
    (...)
    255 11111111 ff
    >>>

Gördüğünüz gibi, onlu sistemde `255` şeklinde, ikili sistemde ise `11111111`
şeklinde gösterilen sayı on altılı sistemde yalnızca `ff` şeklinde
gösterilebiliyor. Dolayısıyla, kullanım açısından, biz insanlar için on altılık
sayma sisteminin ikili sisteme kıyasla çok daha pratik bir yöntem olduğunu
söyleyebiliriz.

Ayrıca on altılı sistem, az alana çok veri sığdırabilme özelliği nedeniyle HTML
renk kodlarının gösterilmesinde de tercih edilir. Örneğin beyaz rengi temsil
etmek için on altılı sistemdeki `#FFFFFF` ifadesini kullanmak `rgb(255,255,255)`
ifadesini kullanmaya kıyasla çok daha mantıklıdır. Hatta `#FFFFFF` ifadesini
`#FFF` şeklinde kısaltma imkanı dahi vardır.
