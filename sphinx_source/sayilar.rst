.. meta::
   :description: Bu bölümde sayılar ve sayı sistemleri konusundan söz edeceğiz.
   :keywords: python, python3, sayma sistemleri, ikili, binary, hex, oct, bin,
              int, ikili, onaltılı, sekizli, onlu

.. highlight:: py3

Sayılar
*******

Geçen bölümde sayma sistemlerini ayrıntılı bir şekilde inceledik. Bu bölümde ise
yine bununla bağlantılı bir konu olan sayılar konusunu ele alacağız. Esasında
biz sayıların ne olduğuna ve Python'da bunların nasıl kullanılacağına dair
tamamen bilgisiz değiliz. Buraya gelene kadar, sayılar konusunda epey şey
söyledik aslında. Mesela biz Python'da üç tür sayı olduğunu biliyoruz:

    #. Tam Sayılar (*integers*)
    #. Kayan Noktalı Sayılar (*floating point numbers* veya kısaca *floats*)
    #. Karmaşık Sayılar (*complex numbers*)
    
Eğer bir veri ``type(veri)`` sorgulamasına `int` cevabı veriyorsa o veri bir
tam sayıdır. Eğer bir veri ``type(veri)`` sorgulamasına `float` cevabı veriyorsa
o veri bir kayan noktalı sayıdır. Eğer bir veri ``type(veri)`` sorgulamasına
`complex` cevabını veriyorsa o veri bir karmaşık sayıdır. 

Mesela şunlar birer tam sayıdır:

    15, 4, 33

Şunlar birer kayan noktalı sayıdır:

    3.5, 6.6, 2.3 

Şunlarsa birer karmaşık sayıdır:

    3+3j, 5+2j, 19+10j
    
Ayrıca şimdiye kadar öğrendiklerimiz sayesinde bu sayıların çeşitli fonksiyonlar
yardımıyla birbirlerine dönüştürülebileceğini de biliyoruz:

    ===============  ===================================  =================
     Fonksiyon        Görevi                                Örnek
    ---------------  -----------------------------------  -----------------
     ``int()``        Bir veriyi tam sayıya dönüştürür      ``int('2')``
     
     ``float()``      Bir veriyi kayan noktalı sayıya       ``float(2)``
                      dönüştürür
     
     ``complex()``    Bir veriyi karmaşık sayıya            ``complex(2)``
                      dönüştürür
    ===============  ===================================  =================
    
Dediğimiz gibi, bunlar bizim zaten sayılara dair bildiğimiz şeyler. Elbette bir
de henüz öğrenmediklerimiz var. 

Gelin şimdi bunların neler olduğunu inceleyelim.

Sayıların Metotları
===================

Tıpkı öteki veri tiplerinde olduğu gibi, sayıların da bazı metotları bulunur. Bu
metotları kullanarak sayılar üzerinde çeşitli işlemler gerçekleştirebiliriz. 

Tam Sayıların Metotları
------------------------

Dediğimiz gibi, Python'da birkaç farklı sayı tipi bulunur. Biz ilk olarak tam
sayı (*integer*) denen sayı tipinin metot ve niteliklerini inceleyeceğiz. 

Öncelikle hangi metotlar ve niteliklerle karşı karşıya olduğumuza bakalım::
    
    >>> [i for i in dir(int) if not i.startswith("_")]
    
    ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 
    'real', 'to_bytes']
    
Bu listede şimdilik bizi ilgilendiren tek bir metot var. Bu metodun adı
``bit_length()``.
    
bit_length()
.............

Bilgisayarlar hakkında bilmemiz gereken en önemli bilgilerden biri şudur:
Bilgisayarlar ancak ve ancak sayılarla işlem yapabilir. Bilgisayarların işlem
yapabildiği sayılar da onlu sistemdeki sayılar değil, ikili sistemdeki
sayılardır. Yani 0'lar ve 1'ler. 

Bilgisayar terminolojisinde bu 0'lar ve 1'lerden oluşan herbir basamağa 'bit'
adı verilir. Yani ikili sayma sisteminde '0' ve '1' sayılarından herbiri 1
bit'tir. Mesela onlu sistemde `2` sayısının ikili sistemdeki karşılığı olan `10`
sayısı iki bit'lik bir sayıdır. Onlu sistemdeki `100` sayısının ikili sistemdeki
karşılığı olan `1100100` sayısı ise yedi bitlik bir sayıdır.

Bu durumu daha net bir şekilde görebilmek için şu kodları yazalım::
    
    >>> for i in range(11):
    ...     print(i, bin(i)[2:], len(bin(i)[2:]), sep="\t")
    ...
    0       0       1
    1       1       1
    2       10      2
    3       11      2
    4       100     3
    5       101     3
    6       110     3
    7       111     3
    8       1000    4
    9       1001    4
    10      1010    4
    
Burada ikinci sütundaki sayılar ilk sütundaki sayıların ikili sistemdeki
karşılıklarıdır. Üçüncü sütundaki sayılar ise her bir sayının kaç bit olduğunu,
yani bir bakıma ikili sayma sisteminde kaç basamağa sahip olduğunu gösteriyor.

İşte herhangi bir tam sayının kaç bit'lik bir yer kapladığını öğrenmek için, tam
sayıların metotlarından biri olan ``bit_length()`` metodundan yararlanacağız::
    
    >>> sayı = 10
    >>> sayı.bit_length()
    
    4
    
Demek ki `10` sayısı bellekte dört bitlik bir yer kaplıyormuş. Yani bu sayının
ikili sistemdeki karşılığı olan `1010` sayısı dört basamaktan oluşuyormuş.

Yukarıdaki örneklerden de rahatlıkla çıkarabileceğiniz gibi, ``bit_length()``
metodu, ikili sayma sistemindeki bir sayı üzerine ``len()`` fonksiyonunun
uygulanması ile eşdeğerdir. Yani::
    
    >>> len(bin(10)[2:]) == (10).bit_length()
    True
    
Bu arada şu son örnekte bir şey dikkatinizi çekmiş olmalı: ``bit_length()``
metodunu doğrudan sayılar üzerine uygulayamıyoruz. Yani::
    
    >>> 10.bit_length()
      File "<stdin>", line 1
        10.bit_length()
                    ^
    SyntaxError: invalid syntax
    
Bu metodu sayılarla birlikte kullanabilmek için iki seçeneğimiz var:
``bit_length()`` metodunu uygulamak istediğimiz sayıyı önce bir değişkene
atayabiliriz::
    
    >>> a = 10
    >>> a.bit_length()
    
    4
    
...veya ilgili sayıyı parantez içine alabiliriz::

    >>> (10).bit_length()

    4
    
Bu durum, yani sayıyı parantez içinde gösterme zorunluluğu, `10` sayısının
sağına bir nokta işareti koyduğumuzda, Python'ın bu sayıyı bir kayan noktalı
sayı olarak değerlendirmesinden kaynaklanıyor. Yani biz '10' yazıp,
``bit_length()`` metodunu bu sayıya bağlama amacıyla sayının sağına bir nokta
koyduğumuz anda, Python bu sayının bir kayan noktalı sayı olduğunu zannediyor.
Çünkü Python açısından, `10.` sayısı bir kayan noktalı sayıdır. Bunu teyit
edelim::
    
    >>> type(10.)
    
    <class 'float'>
    
Kayan noktalı sayıların ``bit_length()`` adlı bir metodu olmadığı için de
Python'ın bize bir hata mesajı göstermekten başka yapabileceği bir şey kalmıyor.
  
Kayan Noktalı Sayıların Metotları
----------------------------------

Python'da tam sayılar dışında kayan noktalı sayıların da olduğunu biliyoruz. Bu
sayı tipinin şu metotları vardır::
        
    >>> [i for i in dir(float) if not i.startswith("_")]

    ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
    
Biz bu metotlar arasından, ``as_integer_ratio()`` ve ``is_integer()`` adlı
metotlarla ilgileneceğiz. 

as_integer_ratio()
....................

Bu metot, birbirine bölündüğünde ilgili kayan noktalı sayıyı veren iki adet tam
sayı verir bize. Örnek üzerinden açıklayalım::
    
    >>> sayı = 4.5
    >>> sayı.as_integer_ratio()
    
    (9, 2)
    
`9` sayısını `2` sayısına böldüğümüzde `4.5` sayısını elde ederiz. İşte
``as_integer_ratio()`` metodu, bu `9` ve `2` sayılarını bize ayrı ayrı verir.

is_integer()
.............

Bir kayan noktalı sayının ondalık kısmında `0` harici bir sayının olup
olmadığını kontrol etmek için bu metodu kullanıyoruz. Örneğin::
    
    >>> (12.0).is_integer()
    
    True
    
    >>> (12.5).is_integer()
    
    False

Karmaşık Sayıların Metotları
----------------------------

Gelelim karmaşık sayıların metot ve niteliklerine... 

::
    
    >>> [i for i in dir(complex) if not i.startswith("_")]
    
    ['conjugate', 'imag', 'real']
    
Gördüğünüz gibi, karmaşık sayıların da birkaç tane metot ve niteliği var. Biz
bunlar arasından ``imag`` ve ``real`` adlı nitelikleri inceleyeceğiz.

imag
.....

Bir gerçek bir de sanal kısımdan oluşan sayılara karmaşık sayılar (*complex*)
adı verildiğini biliyorsunuz. Örneğin şu bir karmaşık sayıdır:

    12+4j
    
İşte ``imag`` adlı nitelik, bize bir karmaşık sayının sanal kısmını verir::
    
    >>> c = 12+4j
    >>> c.imag
    
    4.0

real
.....

``real`` adlı nitelik bize bir karmaşık sayının gerçek kısmını verir::
    
    >>> c = 12+4j
    >>> c.real
    
    12.0    

Aritmetik Fonksiyonlar
==================================

Python programlama dili, bize sayılarla rahat çalışabilmemiz için bazı
fonksiyonlar sunar. Bu fonksiyonları kullanarak, karmaşık aritmetik işlemleri
kolayca yapabiliriz.

Biz bu bölümde Python'ın bize sunduğu bu gömülü fonksiyonları tek tek
inceleyeceğiz.

Gömülü fonksiyonlar, Python programlama dilinde, herhangi bir özel işlem
yapmamıza gerek olmadan, kodlarımız içinde doğrudan kullanabileceğimiz
fonksiyonlardır. Biz şimdiye kadar pek çok gömülü fonksiyonla zaten tanışmıştık.
O yüzden gömülü fonksiyonlar bizim yabancısı olduğumuz bir konu değil. Mesela
buraya gelene kadar gördüğümüz, ``len()``, ``range()``, ``type()``, ``open()``,
``print()`` ve ``id()`` gibi fonksiyonların tamamı birer gömülü fonksiyondur.
Biz bu fonksiyonları ilerleyen derslerde çok daha ayrıntılı bir şekilde
inceleyeceğiz. Ama şu anda bile fonksiyonlar konusunda epey bilgiye
sahibiz.

Şimdiye kadar öğrendiğimiz gömülü fonksiyonlardan şu listede yer alanlar,
matematik işlemlerinde kullanılmaya uygun olanlardır:

    #. ``complex()`` 
    #. ``float()``
    #. ``int()``
    #. ``pow()``
    #. ``round()``
    #. ``hex()``
    #. ``oct()``
    #. ``bin()``
    
Biz bu fonksiyonların ne işe yaradığını önceki derslerimizde zaten ayrıntılı
olarak incelemiştik. O yüzden burada bunlardan söz etmeyeceğiz. Onun yerine,
henüz öğrenmediğimiz, ama mutlaka bilmemiz gereken gömülü fonksiyonları ele
alacağız. 

O halde hiç vakit kaybetmeden yola koyulalım...

abs()
--------

Bu fonksiyon bize bir sayının mutlak değerini verir::
    
    >>> abs(-2)
    
    2
    
    >>> abs(2)
    
    2

divmod()
-----------

Bu fonksiyon, bir sayının bir sayıya bölünmesi işleminde **bölümü** ve
**kalanı** verir::
    
    >>> divmod(10, 2)
    
    (5, 0)
    
`10` sayısı `2` sayısına bölündüğünde 'bölüm' `5`, 'kalan' ise `0`'dır.

Bir örnek daha verelim::
    
    >>> divmod(14, 3)
    
    (4, 2)
    
Bu sonuçtan gördüğünüz gibi, aslında ``divmod()`` fonksiyonu şu kodlarla aynı
işi yapıyor::
    
    >>> 14 // 3, 14 % 3
    
Bu fonksiyonun gerçekleştirdiği bölme işleminin bir 'taban bölme' işlemi
olduğuna özellikle dikkatinizi çekmek istiyorum.

max()
-------

Size şöyle bir soru sorduğumu düşünün: Acaba aşağıdaki listede yer alan
sayıların en büyüğü kaçtır? 

::

    [882388, 260409, 72923, 692476, 131925, 259114, 47630, 84513, 25413, 614654,
     239479, 299159, 175488, 345972, 458112, 791030, 243610, 413702, 565285,
     773607, 131583, 979177, 247202, 615485, 647512, 556823, 242460, 852928,
     893126, 792435, 273904, 544434, 627222, 601984, 966446, 384143, 308858,
     915106, 914423, 826315, 258342, 188056, 934954, 253918, 468223, 262875,
     462902, 370061, 336521, 367829, 147846, 838385, 605377, 175140, 957437,
     105779, 153499, 435097, 9934, 435761, 989066, 357279, 341319, 420455,
     220075, 28839, 910043, 891209, 975758, 140968, 837021, 526798, 235190,
     634295, 521918, 400634, 385922, 842289, 106889, 742531, 359913, 842431,
     666182, 516933, 22222, 445705, 589281, 709098, 48521, 513501, 277645,
     860937, 655966, 923944, 7895, 77482, 929007, 562981, 904166, 619260,
     616293, 203512, 67534, 615578, 74381, 484273, 941872, 110617, 53517,
     402324, 156156, 839504 , 625325, 694080, 904277, 163914, 756250, 809689,
     354050, 523654, 26723, 167882, 103404, 689579, 121439, 158946, 485258,
     850804, 650603, 717388, 981770, 573882, 358726, 957285, 418479, 851590,
     960182, 11955, 894146, 856069, 369866, 740623, 867622, 616830, 894801,
     827179, 580024, 987174, 638930, 129200, 214789, 45268, 455924, 655940,
     335481, 845907, 942437, 759380, 790660, 432715, 858959, 289617, 757317,
     982063, 237940, 141714, 939369, 198282, 975017, 785968, 49954, 854914,
     996780, 121633, 436419, 471, 776271, 91626, 209175, 894281, 417963, 624464,
     736535, 418888, 506194, 591087, 64075, 50252, 952943, 25878, 217085,
     223996, 416042, 484123, 810460, 423284, 956886, 237772, 960241, 601551,
     830147, 449088, 364567, 337281, 524358, 980387, 393760, 619710, 100181,
     96738, 275199, 553783, 975654, 662536, 979103, 869504, 702350, 174361,
     970250, 267625, 661580, 444662, 871532, 881977, 981660, 446047, 508758,
     530694, 608789, 339540, 242774, 637473, 874011, 732999, 511638, 744144,
     710805, 641326, 88085, 128487, 59732, 739340, 443638, 830333, 832136,
     882277, 403538, 441349, 721048, 32859]
    
İşte böyle bir soruyu çözmek için ``max()`` fonksiyonundan yararlanabilirsiniz.
Yukarıdaki listeyi `sayılar` adlı bir değişkene atadığımızı varsayarsak,
aşağıdaki kod bize listedeki en büyük sayıyı verecektir::
    
    >>> max(sayılar)

.. 
    sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
    
    enuzun = len(max(sayı_sistemleri, key=len))
    
    print(("{:^{e}} "*len(sayı_sistemleri)).format(*sayı_sistemleri, e=enuzun))
    
    for i in range(17):
        print("{0:^{1}} {0:^{1}o} {0:^{1}x} {0:^{1}b}".format(i, enuzun))  
        
Yukarıdaki örneklerde ``max()`` fonksiyonunu kullanarak bir dizi içindeki en
**büyük** sayıyı bulduk. Peki bu fonksiyonu kullanarak bir dizi içindeki en
**uzun** karakter dizisini bulabilir miyiz? Evet, bulabiliriz.

Diyelim ki elimizde şöyle bir liste var::
    
    isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
               "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
               
Amacımız bu liste içindeki en uzun kelimeyi bulmak. İşte bunu ``max()``
fonksiyonu ile yapabiliriz. Dikkatlice bakın::

    print(max(isimler, key=len))
    
Bu kodları çalıştırdığımızda, listedeki en uzun isim olan 'gıyaseddin'i elde
edeceğiz. 

Gördüğünüz gibi, ``max()`` fonksiyonu `key` adlı özel bir parametre daha alıyor.
Bu parametreye biz 'len' değerini verdik. Böylece ``max()`` fonksiyonu liste
içindeki öğeleri uzunluklarına göre sıralayıp en uzun öğeyi bize sundu.  

Hatırlarsanız geçen bölümde şöyle bir kod yazmıştık::
    
    sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
    
    print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
    
    for i in range(17):
        print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
        
Bu kodlar, farklı sayma sistemleri arasındaki farkları daha net görmemizi
sağlamıştı. Yalnız burada dikkat ettiyseniz, `sayı_sistemleri` adlı listeye her
öğe ekleyişimizde, listedeki en uzun değeri dikkate alarak karakter dizisi
biçimlendiricileri içindeki, öğeler arasında ne kadar boşluk bırakılacağını
belirleyen sayıları güncelliyorduk. Mesela yukarıdaki örnekte, öğeler arasında
yeterince boşluk bırakabilmek için bu sayıyı `9` olarak belirlemiştik. İşte
şimdi öğrendiğimiz ``max()`` fonksiyonunu kullanarak bu sayının otomatik olarak
belirlenmesini sağlayabiliriz. Dikkatlice inceleyin::
    
    sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
    
    en_uzun = len(max(sayı_sistemleri, key=len))
    
    print(("{:^{aralık}} "*len(sayı_sistemleri)).format(*sayı_sistemleri, aralık=en_uzun))
    
    for i in range(17):
        print("{0:^{1}} {0:^{1}o} {0:^{1}x} {0:^{1}b}".format(i, en_uzun))
        
Gördüğünüz gibi, ``max()`` fonksiyonunu ve bu fonksiyonun `key` parametresini
kullanarak, oluşturduğumuz tablodaki öğelerin arasına uygun boşluğu otomatik
olarak eklemiş olduk. Bunun için, `sayı_sistemleri` adlı listedeki en uzun
öğenin uzunluk miktarını temel aldık. 
    
min()
---------

Bu fonksiyon, ``max()`` fonksiyonun yaptığı işin tam tersini yapar. Yani bu
fonksiyonu kullanarak bir dizi içindeki en küçük sayıyı bulabilirsiniz::
    
    >>> min(sayılar)
    
Tıpkı ``max()`` fonksiyonunda olduğu gibi, ``min()`` fonksiyonunda da `key`
parametresini kullanabilirsiniz. Mesela ``max()`` fonksiyonunu anlatırken
verdiğimiz isim listesindeki en kısa ismi bulabilmek için şu kodu
yazabilirsiniz::
    
    print(min(isimler, key=len))

sum()
----------

Bu fonksiyon bir dizi içinde yer alan bütün sayıları birbiriyle toplar.
Örneğin::
    
    >>> a = [10, 20, 43, 45 , 77, 2, 0, 1]
    >>> sum(a)

    198
    
Eğer bu fonksiyonun, toplama işlemini belli bir sayının üzerine
gerçekleştirmesini istiyorsanız şu kodu yazabilirsiniz::
    
    >>> sum(a, 10)
    
    208
    
``sum()`` fonksiyonuna bu şekilde ikinci bir parametre verdiğinizde, bu ikinci
parametre toplam değere eklenecektir.


