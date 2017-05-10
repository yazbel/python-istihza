.. meta:: 
    :description: Bu bölümde Python'ın etkileşimli kabuğundan söz edeceğiz. 
    :keywords: etkileşimli, kabuk, Python, işleçler, aritmetik, type, str,
     string, fonksiyon, değişkenler, len 

.. highlight:: py3

******************* 
Etkileşimli Python 
*******************

Şu ana kadar öğrendiklerimiz sayesinde Python programlama dilinin farklı
sistemlere nasıl kurulacağını ve nasıl çalıştırılacağını biliyoruz. Dolayısıyla
Python'ı bir önceki bölümde anlattığımız şekilde çalıştırdığımız zaman şuna
benzer bir ekranla karşılaşacağımızın farkındayız:

.. container:: screenshot

    |screenshotlin|

Biz şimdiye kadar bu ekrana Python komut satırı demeyi tercih ettik. Dilerseniz
bundan sonra da bu adı kullanmaya devam edebilirsiniz. Ancak teknik olarak bu
ekrana etkileşimli kabuk (*interactive shell*) adı verildiğini bilmemizde fayda
var. Etkileşimli kabuk, bizim Python programlama dili ile ilişki
kurabileceğimiz, yani onunla etkileşebileceğimiz bir üst katmandır. Etkileşimli
kabuk, asıl programımız içinde kullanacağımız kodları deneme imkanı sunar bize.
Burası bir nevi test alanı gibidir. Örneğin bir Python kodunun çalışıp
çalışmadığını denemek veya nasıl çalıştığını, ne sonuç verdiğini görmek
istediğimizde bu ekran son derece faydalı bir araç olarak karşımıza çıkar. Bu
ortam, özellikle Python'a yeni başlayanların bu programlama diline aşinalık
kazanmasını sağlaması açısından da bulunmaz bir araçtır. Biz de bu bölümde
etkileşimli kabuk üzerinde bazı çalışmalar yaparak, Python'a alışma turları
atacağız.

Bu arada, geçen bölümde söylediğimiz gibi, bu ortamın sistem komut satırı adını
verdiğimiz ortamdan farklı olduğunu aklımızdan çıkarmıyoruz. O zaman da
dediğimiz gibi, sistem komut satırında sistem komutları, Python komut satırında
(yani etkileşimli kabukta) ise Python komutları verilir. Mesela ``echo %PATH%``,
``cd Desktop``, ``dir`` ve ``ls`` birer sistem komutudur. Eğer bu komutları
etkileşimli kabukta vermeye kalkışırsanız, bunlar birer Python komutu olmadığı
için, Python size bir hata mesajı gösterecektir. Mesela Python'ın etkileşimli
kabuğunda ``cd Desktop`` komutunu verirseniz şöyle bir hata alırsınız::

    >>> cd Desktop
    
      File "<stdin>", line 1
        cd Desktop
                 ^
    SyntaxError: invalid syntax

Çünkü ``cd Desktop`` bir Python komutu değildir. O yüzden bu komutu Python'ın
etkileşimli kabuğunda veremeyiz. Bu komutu ancak ve ancak kullandığımız işletim
sisteminin komut satırında verebiliriz.

Ne diyorduk? Etkileşimli kabuk bir veya birkaç satırlık kodları denemek/test
etmek için gayet uygun bir araçtır. İsterseniz konuyu daha fazla lafa
boğmayalım. Zira etkileşimli kabuğu kullandıkça bunun ne büyük bir nimet
olduğunu siz de anlayacaksınız. Özellikle derlenerek çalıştırılan programlama
dilleri ile uğraşmış olan arkadaşlarım, etkileşimli kabuğun gücünü gördüklerinde
göz yaşlarına hakim olamayacaklar.

Farklı işletim sistemlerinde ``py3``, ``py -3``, ``python3`` veya ``python``
komutunu vererek Python'ın komut satırına nasıl erişebileceğimizi önceki
derslerde ayrıntılı olarak anlatmıştık. Etkileşimli kabuğa ulaşmakta sıkıntı
yaşıyorsanız eski konuları tekrar gözden geçirmenizi tavsiye ederim.

Etkileşimli kabuk üzerinde çalışmaya başlamadan önce dilerseniz önemli bir
konuyu açıklığa kavuşturalım: Etkileşimli kabuğu başarıyla çalıştırdık. Peki bu
kabuktan çıkmak istersek ne yapacağız? Elbette doğrudan pencere üzerindeki çarpı
tuşuna basarak bu ortamı terk edebilirsiniz. Ancak bu işlemi kaba kuvvete
başvurmadan yapmanın bir yolu olmalı, değil mi?

Etkileşimli kabuktan çıkmanın birkaç farklı yolu vardır:

#. Pencere üzerindeki çarpı düğmesine basmak (kaba kuvvet)

#. Önce `Ctrl+Z` tuşlarına, ardından da `Enter` tuşuna basmak (Windows)

#. `Ctrl+Z` tuşlarına basmak (GNU/Linux)

#. Önce `F6` tuşuna, ardından da `Enter` tuşuna basmak (Windows)

#. ``quit()`` yazıp `Enter` tuşuna basmak (Bütün işletim sistemleri)

#. ``import sys; sys.exit()`` komutunu vermek (Bütün işletim sistemleri)

Siz bu farklı yöntemler arasından, kolayınıza hangisi geliyorsa onu
seçebilirsiniz. Bu satırların yazarı, Windows'ta 2 numaralı; GNU/Linux'ta ise 3
numaralı seçeneği tercih ediyor.

Etkileşimli Kabukta İlk Adımlar 
*******************************

Python'da etkileşimli kabuğu nasıl çalıştıracağımızı ve bu ortamı nasıl terk
edeceğimizi öğrendiğimize göre artık etkileşimli kabuk aracılığıyla Python
programlama dilinde ilk adımlarımızı atmaya başlayabiliriz.

Şimdi kendi sistemimize uygun bir şekilde etkileşimli kabuğu tekrar
çalıştıralım. Etkileşimli kabuğu çalıştırdığımızda ekranda görünen `>>>` işareti
Python'ın bizden komut almaya hazır olduğunu gösteriyor. Python kodlarımızı bu
`>>>` işaretinden hemen sonra, **hiç boşluk bırakmadan** yazacağız.

Buradaki 'hiç boşluk bırakmadan' kısmı önemli. Python'a yeni başlayanların en
sık yaptığı hatalardan biri `>>>` işareti ile komut arasında boşluk
bırakmalarıdır. Eğer bu şekilde boşluk bırakırsanız yazdığınız kod hata
verecektir.

İsterseniz basit bir deneme yapalım. `>>>` işaretinden hemen sonra, hiç boşluk
bırakmadan şu komutu yazalım::

    >>> "Merhaba Zalim Dünya!" 
    
Bu arada yukarıdaki kodlar içinde görünen `>>>` işaretini siz yazmayacaksınız.
Bu işareti etkileşimli kabuğun görünümünü temsil etmek için yerleştirdik oraya.
Siz `"Merhaba Zalim Dünya!"` satırını yazdıktan sonra doğruca `Enter` düğmesine
basacaksınız.

Bu komutu yazıp `Enter` tuşuna bastığımızda şöyle bir çıktı almış olmalıyız::

	'Merhaba Zalim Dünya!'

Böylece yarım yamalak da olsa ilk Python programımızı yazmış olduk...

Muhtemelen bu kod, içinizde en ufak bir heyecan dahi uyandırmamıştır. Hatta
böyle bir kod yazmak size anlamsız bile gelmiş olabilir. Ama aslında şu küçücük
kod parçası bile bize Python programlama dili hakkında çok önemli ipuçları
veriyor. Gelin isterseniz bu tek satırlık kodu biraz inceleyelim... 

Karakter Dizilerine Giriş 
==========================

Dediğimiz gibi, yukarıda yazdığımız küçücük kod parçası sizi heyecanlandırmamış
olabilir, ama aslında bu kod Python programlama dili ve bu dilin yapısı hakkında
çok önemli bilgileri içinde barındırıyor.

Teknik olarak söylemek gerekirse, yukarıda yazdığımız `"Merhaba Zalim Dünya!"`
ifadesi bir karakter dizisidir. İngilizcede buna *string* adı verilir ve
programlama açısından son derece önemli bir kavramdır bu. Kavramın adından da
rahatlıkla anlayabileceğiniz gibi, bir veya daha fazla karakterden oluşan
öğelere karakter dizisi (*string*) diyoruz.

Karakter dizileri bütün programcılık maceramız boyunca karşımıza çıkacak. O
yüzden bu kavramı ne kadar erken öğrenirsek o kadar iyi.

Peki bir verinin karakter dizisi olup olmamasının bize ne faydası var? Yani
yukarıdaki cümle karakter dizisi olmuş olmamış bize ne?

Python'da, o anda elinizde bulunan bir verinin hangi tipte olduğunu bilmek son
derece önemlidir. Çünkü bir verinin ait olduğu tip, o veriyle neler yapıp neler
yapamayacağınızı belirler. Python'da her veri tipinin belli başlı özellikleri
vardır. Dolayısıyla, elimizdeki bir verinin tipini bilmezsek o veriyi
programlarımızda etkin bir şekilde kullanamayız. İşte yukarıda örneğini
verdiğimiz `"Merhaba Zalim Dünya!"` adlı karakter dizisi de bir veri tipidir.
Python'da karakter dizileri dışında başka veri tipleri de bulunur. Biraz sonra
başka veri tiplerini de inceleyeceğiz.

Dikkat ederseniz `"Merhaba Zalim Dünya!"` adlı karakter dizisini tırnak içinde
gösterdik. Bu da çok önemli bir bilgidir. Eğer bu cümleyi tırnak içine almazsak
programımız hata verecektir::

    >>> Merhaba Zalim Dünya!
    
      File "<stdin>", line 1
        Merhaba Zalim Dünya!
                    ^
    SyntaxError: invalid syntax

Zaten tırnak işaretleri, karakter dizilerinin ayırt edici özelliğidir. Öyle ki,
Python'da tırnak içinde gösterdiğiniz her şey bir karakter dizisidir. Örneğin şu
bir karakter dizisidir::

    >>> "a"

Gördüğünüz gibi, tırnak içinde gösterilen tek karakterlik bir öğe de Python'da
karakter dizisi sınıfına giriyor.

Mesela şu, içi boş bir karakter dizisidir::

    >>> ""

Şu da içinde bir adet boşluk karakteri barındıran bir karakter dizisi...

::

    >>> " "

Bu ikisi arasındaki farka dikkat ediyoruz: Python'da 'boş karakter dizisi' ve
'bir adet boşluktan oluşan karakter dizisi' birbirlerinden farklı iki kavramdır.
Adından da anlaşılacağı gibi, boş karakter dizileri içlerinde hiçbir karakter
(başka bir deyişle 'öğe') barındırmayan karakter dizileridir. Bir (veya daha
fazla) boşluktan oluşan karakter dizileri ise içlerinde boşluk karakteri
barındıran karakter dizileridir. Yani bu karakter dizilerinden biri boş, öteki
ise doludur. Ama neticede her ikisi de karakter dizisidir. Şu anda oldukça
anlamsız bir konu üzerinde vakit kaybediyormuşuz hissine kapılmış olabilirsiniz,
ama emin olun, Python programlama diline yeni başlayanların önemli tökezleme
noktalarından biridir bu söylediğimiz şey...

Dilerseniz biz karakter dizilerine elimizin alışması için birkaç örnek verelim::

    >>> "Elma" 
    
    'Elma' 
    
    >>> "Guido Van Rossum" 
    
    'Guido Van Rossum' 
    
    >>> "Python programlama dili" 
    
    'Python programlama dili' 
    
    >>> "ömnhbgfgh" 
    
    'ömnhbgfgh' 
    
    >>> "$5&" 
    
    '$5&' 
    
    >>> "" 
    
    '' 
    
    >>> " " 
    
    ' ' 
    
    >>> " " 
    
    ' '

Yukarıdaki örneklerin hepsi birer karakter dizisidir. Dikkat ettiyseniz
yukarıdaki karakter dizilerinin hepsinin ortak özelliği tırnak içinde
gösteriliyor olmasıdır. Dediğimiz gibi, tırnak işaretleri karakter dizilerinin
ayırt edici özelliğidir.

Peki bir verinin karakter dizisi olup olmadığından nasıl emin olabilirsiniz?

Eğer herhangi bir verinin karakter dizisi olup olmadığı konusunda tereddütünüz
varsa, ``type()`` adlı bir fonksiyondan yararlanarak o verinin tipini
sorgulayabilirsiniz. Bu fonksiyonu şöyle kullanıyoruz::

    >>> type("Elma") 
    
    <class 'str'>

.. note:: Bu 'fonksiyon' kelimesinin kafanızı karıştırmasına izin vermeyin.
          İlerde fonksiyonları oldukça ayrıntılı bir şekilde inceleyeceğimiz için,
          ``type()`` ifadesinin bir fonksiyon olduğunu bilmeniz şimdilik yeterli
          olacaktır. Üstelik fonksiyon konusunu ayrıntılı bir şekilde anlatma
          vakti geldiğinde siz fonksiyonlara dair pek çok şeyi zaten öğrenmiş
          olacaksınız.

Burada amacımız `"Elma"` adlı öğenin tipini denetlemek. Denetlenecek öğeyi
``type()`` fonksiyonunun parantezleri arasında belirttiğimize dikkat edin.
(Fonksiyonların parantezleri içinde belirtilen değerlere teknik dilde parametre
adı verilir.)

Yukarıdaki çıktıda bizi ilgilendiren kısım, sondaki 'str' ifadesi. Tahmin
edebileceğiniz gibi, bu ifade *string* kelimesinin kısaltmasıdır. Bu kelimenin
Türkçede karakter dizisi anlamına geldiğini söylemiştik. O halde yukarıdaki
çıktıya bakarak, `"Elma"` öğesinin bir karakter dizisi olduğunu
söyleyebiliyoruz.

``type()`` fonksiyonu yardımıyla kendi kendinize bazı denemeler yaparak konuyu
iyice sindirmenizi tavsiye ederim. Mesela `"½{656$#gfd"` ifadesinin hangi sınıfa
girdiğini kontrol etmekle başlayabilirsiniz.

Peki karakter dizileri ile neler yapabiliriz? Şu anda Python bilgimiz kısıtlı
olduğu için karakter dizileri ile çok fazla şey yapamayız, ama ilerde bilgimiz
arttıkça, karakter dizileriyle sıkı fıkı olacağız.

Esasında, henüz bilgimiz kısıtlı da olsa karakter dizileriyle yine de ufak tefek
bazı şeyler yapamayacak durumda değiliz. Mesela şu anki bilgilerimizi ve görür
görmez size tanıdık gelecek bazı basit parçaları kullanarak, karakter dizilerini
birbirleriyle birleştirebiliriz::

    >>> "istihza" + ".com" 
    
    'istihza.com'

Burada `+` işaretini kullanarak karakter dizilerini nasıl birleştirebildiğimize
dikkat edin. İki karakter dizisini `+` işareti ile birleştirdiğimizde karakter
dizilerinin arasında boşluk olmadığına özellikle dikkatinizi çekmek isterim. Bu
durumu şu örnekte daha net görebiliriz::

    >>> "Fırat" + "Özgül" 
    
    'FıratÖzgül'

Gördüğünüz gibi, bu iki karakter dizisi, arada boşluk olmadan birbiriyle
bitiştirildi. Araya boşluk eklemek için birkaç farklı yöntemden
yararlanabilirsiniz::

    >>> "Fırat" + " " + "Özgül" 
    
    'Fırat Özgül'

Burada iki karakter dizisi arasına bir adet boşluk karakteri yerleştirdik. Aynı
etkiyi şu şekilde de elde edebilirsiniz::

    >>> "Fırat" + " Özgül"

Burada da `Özgül` karakter dizisinin başına bir adet boşluk yerleştirerek
istediğimiz çıktıyı elde ettik.

Bu arada, karakter dizilerini birleştirmek için mutlaka `+` işareti kullanmak
zorunda değilsiniz. Siz `+` işaretini kullanmasanız da Python sizin karakter
dizilerini birleştirmek istediğinizi anlayacak kadar zekidir::

    >>> "www" "." "google" "." "com" 
    
    'www.google.com'

Ancak gördüğünüz gibi, `+` işaretini kullandığınızda kodlarınız daha okunaklı
oluyor.

`+` işareti dışında karakter dizileri ile birlikte `*` (çarpı) işaretini de
kullanabiliriz. O zaman şöyle bir etki elde ederiz::

    >>> "w" * 3 
    
    'www' 
    
    >>> "yavaş " * 2 
    
    'yavaş yavaş ' 
    
    >>> "-" * 10 
    
    '----------'
    
    >>> "uzak" + " " * 5 + "çok uzak..." 
    
    'uzak     çok uzak...'

Gördüğünüz gibi, çok basit parçaları bir araya getirerek karmaşık çıktılar elde
edebiliyoruz. Mesela son örnekte `"uzak"` adlı karakter dizisine önce `5` adet
boşluk karakteri (``" " * 5``), ardından da `"çok uzak..."` adlı karakter
dizisini ekleyerek istediğimiz çıktıyı aldık.

Burada `+` ve `*` adlı iki yeni araç görüyoruz. Bunlar aslında sayılarla
birlikte kullanılan birer aritmetik işleçtir. Normalde `+` işleci toplama
işlemleri için, `*` işleci ise çarpma işlemleri için kullanılır. Ama yukarıdaki
örneklerde, `+` işaretinin 'birleştirme'; `*` işaretinin ise 'tekrarlama'
anlamından ötürü bu iki işleci bazı durumlarda karakter dizileri ile birlikte de
kullanabiliyoruz. Bunların dışında bir de `-` (eksi) ve `/` (bölü) işleçleri
bulunur. Ancak bu işaretleri karakter dizileri ile birlikte kullanamıyoruz.

Karakter dizilerini sonraki bir bölümde bütün ayrıntılarıyla inceleyeceğiz. O
yüzden şimdilik bu konuya bir ara verelim.

Sayılara Giriş 
===============

Dedik ki, Python'da birtakım veri tipleri bulunur ve karakter dizileri de bu
veri tiplerinden yalnızca biridir. Veri tipi olarak karakter dizilerinin
dışında, biraz önce aritmetik işleçler vesilesiyle sözünü ettiğimiz, bir de
'sayı' (*number*) adlı bir veri tipi vardır.

Herhalde sayıların ne anlama geldiğini tarif etmeye gerek yok. Bunlar bildiğimiz
sayılardır. Mesela::

    >>> 23 
    
    23 
    
    >>> 4567 
    
    4567 
    
    >>> 2.3 
    
    2.3 
    
    >>> (10+2j) 
    
    (10+2j)

Python'da sayıların farklı alt türleri bulunur. Mesela tamsayılar, kayan noktalı
sayılar, karmaşık sayılar...

Yukarıdaki örnekler arasında geçen `23` ve `4567` birer tamsayıdır. İngilizcede
bu tür sayılara *integer* adı verilir.

`2.3` ise bir kayan noktalı sayıdır (*floating point number* veya kısaca
*float*). Bu arada kayan noktalı sayılarda basamak ayracı olarak virgül değil,
nokta işareti kullandığımıza dikkat edin.

En sonda gördüğümüz `10+2j` sayısı ise bir karmaşık sayıdır (*complex*). Ancak
eğer matematikle yoğun bir şekilde uğraşmıyorsanız karmaşık sayılar pek
karşınıza çıkmaz.

Sayıları temel olarak öğrendiğimize göre etkileşimli kabuğu basit bir hesap
makinesi niyetine kullanabiliriz::

    >>> 5 + 2 
    
    7 
    
    >>> 25 * 25 
    
    625 
    
    >>> 5 / 2 
    
    2.5 
    
    >>> 10 - 3 
    
    7

Yukarıdaki örneklerde kullandığımız aritmetik işleçlerden biraz önce
bahsetmiştik. O yüzden bunlara yabancılık çektiğinizi zannetmiyorum. Ama biz
yine de bu işleçleri ve görevlerini şöylece sıralayalım:

    +-------------+------------------+ 
    | İşleç       | Görevi           |
    +=============+==================+ 
    | `+`         | toplama          |
    +-------------+------------------+ 
    | `-`         | çıkarma          |
    +-------------+------------------+ 
    | `*`         | çarpma           |
    +-------------+------------------+ 
    | `/`         | bölme            |
    +-------------+------------------+

Yukarıdaki örneklerde bir şey dikkatinizi çekmiş olmalı: Karakter dizilerini
tanımlarken tırnak işaretlerini kullandık. Ancak sayılarda tırnak işareti yok.
Daha önce de dediğimiz gibi, tırnak işaretleri karakter dizilerinin ayırt edici
özelliğidir. Python'da tırnak içinde gösterdiğiniz her şey bir karakter
dizisidir. Mesela şu örneklere bakalım::

    >>> 34657 
    
    34657

Bu bir sayıdır. Peki ya şu?

::

    >>> "34657" 
    
    '34657'

Bu ise bir karakter dizisidir. Dilerseniz biraz önce öğrendiğimiz ``type()``
fonksiyonu yardımıyla bu verilerin tipini sorgulayalım::

    >>> type(34657) 
    
    <class 'int'>

Buradaki 'int' ifadesi İngilizce "*integer*", yani tamsayı kelimesinin
kısaltmasıdır. Demek ki `34657` sayısı bir tamsayı imiş. Bir de şuna bakalım::

    >>> type("34657") 
    
    <class 'str'> 
    
Gördüğünüz gibi, `34657` sayısını tırnak içine aldığımızda bu sayı artık sayı
olma özelliğini yitiriyor ve bir karakter dizisi oluyor. Şu anda bu çok önemsiz
bir ayrıntıymış gibi gelebilir size, ama aslında son derece önemli bir konudur
bu. Bu durumun etkilerini şu örneklerde görebilirsiniz::

    >>> 23 + 65 
    
    88

Burada normal bir şekilde iki sayıyı birbiriyle topladık.

Bir de şuna bakın::

    >>> "23" + "65" 
    
    '2365'

Burada ise Python iki karakter dizisini yan yana yazmakla yetindi; yani bunları
birleştirdi. Python açısından `"23"` ve `23` birbirinden farklıdır. `"23"` bir
karakter dizisi iken, `23` bir sayıdır. Aynı şey `"65"` ve `65` için de
geçerlidir. Yani Python açısından `"65"` ile `"Merhaba Zalim Dünya!"` arasında
hiç bir fark yoktur. Bunların ikisi de karakter dizisi sınıfına girer. Ancak
`65` ile `"65"` birbirinden farklıdır. `65` bir sayı iken, `"65"` bir karakter
dizisidir.

Bu bilgi, özellikle aritmetik işlemlerde büyük önem taşır. Bunu dilerseniz şu
örnekler üzerinde gösterelim::

    >>> 45 + "45"
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

Gördüğünüz gibi, yukarıdaki kodlar hata veriyor. Bunun sebebi bir sayı (`45`)
ile bir karakter dizisini (`"45"`) birbiriyle toplamaya çalışmamızdır. Asla
unutmayın, aritmetik işlemler ancak sayılar arasında yapılır. Karakter dizileri
ile herhangi bir aritmetik işlem yapılamaz.

Bir de şuna bakalım::

    >>> 45 + 45 
    
    90

Bu kodlar ise düzgün çalışır. Çünkü burada iki sayıyı aritmetik işleme soktuk ve
başarılı olduk.

Son olarak şu örneği verelim::

    >>> "45" + "45" 
    
    '4545'

Burada `+` işlecinin toplama anlamına gelmediğine dikkat edin. Bu işleç burada
iki karakter dizisini birleştirme görevi üstleniyor. Yani yukarıdaki örneğin şu
örnekten hiçbir farkı yoktur::

    >>> "istihza." + "com" 
    
    'istihza.com'

Bu iki örnekte de yaptığımız şey karakter dizilerini birbiriyle birleştirmektir.

Gördüğünüz gibi, `+` işlecinin sağındaki ve solundaki değerler birer karakter
dizisi ise bu işleç bu iki değeri birbiriyle birleştiriyor. Ama eğer bu değerler
birer sayı ise `+` işleci bu değerleri birbiriyle aritmetik olarak topluyor.

`*` işleci de `+` işlecine benzer bir iş yapar. Yani eğer `*` işleci bir sayı ve
bir karakter dizisi ile karşılaşırsa, o karakter dizisini, verilen sayı kadar
tekrarlar. Örneğin::

    >>> "w" * 3 
    
    'www'

Burada `*` işleci bir karakter dizisi (`"w"`) ve bir sayı (`3`) arasında işlem
yaptığı için, karakter dizisini, ilgili sayı kadar tekrarlıyor. Yani `"w"`
karakter dizisini `3` kez tekrarlıyor.

Bir de şuna bakalım::

    >>> 25 * 3 
    
    75

Burada ise `*` işleci iki adet sayı arasında işlem yaptığı için bu değerleri
birbiriyle aritmetik olarak çarpıyor ve `75` değerini elde etmemizi sağlıyor.

Gördüğünüz gibi, o anda elimizde bulunan verilerin tipini bilmek gerçekten de
büyük önem taşıyor. Çünkü eğer elimizdeki verilerin tipini bilmezsek nasıl
sonuçlar elde edeceğimizi de kestiremeyiz.

Böylece karakter dizileri ile sayılar arasındaki farkı öğrenmiş olduk. Bu
bilgiler size önemsizmiş gibi gelebilir, ama aslında karakter dizileri ile
sayılar arasındaki farkı anlamak, Python programlama dilinin önemli bir bölümünü
öğrenmiş olmak demektir. İleride yazacağınız en karmaşık programlarda bile,
bazen programınızın çalışmamasının (veya daha kötüsü yanlış çalışmasının)
nedeninin karakter dizileri ile sayıları birbirine karıştırmanız olduğunu
göreceksiniz. O yüzden burada öğrendiğiniz hiçbir bilgi kırıntısını baştan
savmamanızı (ve sabırsızlık ya da acelecilik etmemenizi) tavsiye ederim.

Değişkenler 
============

Şimdi şöyle bir durum düşünün: Diyelim ki sisteme kayıt için kullanıcı adı ve
parola belirlenmesini isteyen bir program yazıyorsunuz. Yazacağınız bu
programda, belirlenebilecek kullanıcı adı ve parolanın toplam uzunluğu `40`
karakteri geçmeyecek.

Bu programı yazarken ilk aşamada yapmanız gereken şey, kullanıcının belirlediği
kullanıcı adı ve parolanın uzunluğunu tek tek denetlemek olmalı.

Mesela kullanıcı şöyle bir kullanıcı adı belirlemiş olsun::

    firat_ozgul_1980 

.. highlight:: none

Kullanıcının belirlediği parola ise şu olsun::

    rT%65#$hGfUY56123

İşte bizim öncelikle kullanıcıdan gelen bu verilerin teker teker uzunluğunu
biliyor olmamız lazım, ki bu verilerin toplam `40` karakter sınırını aşıp
aşmadığını denetleyebilelim.

Peki bu verilerin uzunluğunu nasıl ölçeceğiz? Elbette bunun için verilerdeki
harfleri elle tek tek saymayacağız. Bunun yerine, Python programlama dilinin
bize sunduğu bir aracı kullanacağız. Peki nedir bu araç?

Hatırlarsanız birkaç sayfa önce ``type()`` adlı bir fonksiyondan söz etmiştik.
Bu fonksiyonun görevi bir verinin hangi tipte olduğunu bize bildirmekti. İşte
tıpkı ``type()`` gibi, Python'da ``len()`` adlı başka bir fonksiyon daha
bulunur. Bu fonksiyonun görevi ise karakter dizilerinin (ve ileride göreceğimiz
gibi, başka veri tiplerinin) uzunluğunu ölçmektir. Yani bu fonksiyonu kullanarak
bir karakter dizisinin toplam kaç karakterden oluştuğunu öğrenebiliriz.

.. highlight:: py3

Biz henüz kullanıcıdan nasıl veri alacağımızı bilmiyoruz. Ama şimdilik şunu
söyleyebiliriz: Python'da kullanıcıdan herhangi bir veri aldığımızda, bu veri
bize bir karakter dizisi olarak gelecektir. Yani kullanıcıdan yukarıdaki
kullanıcı adı ve parolayı aldığımızı varsayarsak, bu veriler bize şu şekilde
gelir::

    "firat_ozgul_1980"

ve::

    "rT%65#$hGfUY56123"

Gördüğünüz gibi, elde ettiğimiz veriler tırnak içinde yer alıyor. Yani bunlar
birer karakter dizisi. Şimdi gelin yukarıda bahsettiğimiz ``len()`` fonksiyonunu
kullanarak bu karakter dizilerinin uzunluğunu ölçelim.

Dediğimiz gibi, ``len()`` de tıpkı ``type()`` gibi bir fonksiyondur. Dolayısıyla
``len()`` fonksiyonunun kullanımı ``type()`` fonksiyonunun kullanımına çok
benzer. Nasıl ``type()`` fonksiyonu bize, kendisine verdiğimiz parametrelerin
**tipini** söylüyorsa, ``len()`` fonksiyonu da kendisine verdiğimiz
parametrelerin **uzunluğunu** söyler.

Dikkatlice bakın::

    >>> len("firat_ozgul_1980")

    16

    >>> len("rT%65#$hGfUY56123") 
    
    17

Demek ki `"firat_ozgul_1980"` adlı karakter dizisinde `16`;
`"rT%65#$hGfUY56123"` adlı karakter dizisinde ise `17` karakter varmış. Bizim
istediğimiz şey bu iki değerin toplam uzunluğunun `40` karakteri aşmaması. Bunu
denetlemek için yapmamız gereken şey bu iki değerin uzunluğunu birbiriyle
toplamak olmalı. Yani::

    >>> len("firat_ozgul_1980") + len("rT%65#$hGfUY56123")

Buradan alacağımız sonuç `33` olacaktır. Demek ki kullanıcı `40` karakter
limitini aşmamış. O halde programımız bu kullanıcı adı ve parolayı kabul
edebilir...

Bu arada, belki farkettiniz, belki de farketmediniz, ama burada da çok önemli
bir durumla karşı karşıyayız. Gördüğünüz gibi ``len()`` fonksiyonu bize sayı
değerli bir veri gönderiyor. Gelin isterseniz bunu teyit edelim::

    >>> type(len("firat_ozgul_1980"))

    <class 'int'>

``len()`` fonksiyonunun bize sayı değerli bir veri göndermesi sayesinde bu
fonksiyondan elde ettiğimiz değerleri birbiriyle toplayabiliyoruz::

    >>> len("firat_ozgul_1980") + len("rT%65#$hGfUY56123") 
    
    33

Eğer ``len()`` fonksiyonu bize sayı değil de mesela karakter dizisi verseydi,
bu fonksiyondan elde ettiğimiz değerleri yukarıdaki gibi doğrudan birbiriyle
aritmetik olarak toplayamazdık. Öyle bir durumda, bu iki veriyi birbiriyle
toplamaya çalıştığımızda, `+` işleci `16` ve `17` değerlerini birbiriyle
toplamak yerine bu değerleri birbiriyle birleştirerek bize `'1617'` gibi bir
sonuç verecekti.

Her zaman söylediğimiz gibi, Python'da veri tipi kavramını çok iyi anlamak ve o
anda elimizde bulunan bir verinin hangi tipte olduğunu bilmek çok önemlidir.
Aksi halde programlarımızda hata yapmamız kaçınılmazdır.

Eğer yukarıda anlattığımız şeyleri kafa karıştırıcı bulduysanız hiç endişe
etmeyin. Birkaç bölüm sonra ``input()`` adlı bir fonksiyondan bahsettiğimizde
şimdi söylediğimiz şeyleri çok daha net anlayacaksınız.

Biraz sonra ``len()`` fonksiyonundan bahsetmeye devam edeceğiz, ama isterseniz
ondan önce çok önemli bir konuya değinelim.

Biraz önce şöyle bir örnek vermiştik::

    >>> len("firat_ozgul_1980")

    16

    >>> len("rT%65#$hGfUY56123") 
    
    17 
    
    >>> len("firat_ozgul_1980") + len("rT%65#$hGfUY56123")

Bu kodlar, istediğimiz şeyi gayet güzel yerine getiriyor. Ama sizce de
yukarıdaki kodlarda çok rahatsız edici bir durum yok mu?

Dikkat ederseniz, yukarıdaki örneklerde kullandığımız verileri, program içinde
her ihtiyaç duyduğumuzda tekrar tekrar yazdık. Böylece aynı program içinde iki
kez `"firat_ozgul_1980"`; iki kez de `"rT%65#$hGfUY56123"` yazmak zorunda
kaldık. Halbuki bu verileri programlarımızın içinde her ihtiyaç duyduğumuzda
tekrar tekrar yazmak yerine bir değişkene atasak ve gerektiğinde o değişkeni
kullansak çok daha iyi olmaz mı? Herhalde olur...

Peki nedir bu değişken dediğimiz şey?

Python'da bir program içinde değerlere verilen isimlere değişken denir. Hemen
bir örnek verelim::

    >>> n = 5

Burada `5` sayısını bir değişkene atadık. Değişkenimiz ise `n`. Ayrıca `5`
sayısını bir değişkene atamak için `=` işaretinden yararlandığımıza da çok
dikkat edin. Buradan, `=` işaretinin Python programlama dilinde değer atama
işlemleri için kullanıldığı sonucunu çıkarıyoruz.

``n = 5`` gibi bir komut yardımıyla `5` değerini `n` adlı değişkene atamamız
sayesinde artık ne zaman `5` sayısına ihtiyaç duysak bu `n` değişkenini
çağırmamız yeterli olacaktır::

    >>> n 
    
    5

    >>> n * 10 
    
    50
    
    >>> n / 2 
    
    2.5

Gördüğünüz gibi, `5` değerini bir değişkene atadıktan sonra, bu `5` değerini
kullanmamız gereken yerlerde sadece değişkenin adını kullandığımızda değişkenin
değerini Python otomatik olarak yerine koyabiliyor. Yani ``n = 5`` komutuyla `n`
adlı bir değişken tanımladıktan sonra, artık ne zaman `5` sayısına ihtiyaç
duysak `n` değişkenini çağırmamız yeterli olacaktır. Python o `5` değerini
otomatik olarak yerine koyar.

Şimdi de `pi` adlı başka bir değişken tanımlayalım:: 

    >>> pi = 3.14

Bu `pi` değişkeninin değeri ile `n` değişkeninin değerini toplayalım:: 

    >>> pi + n 
    
    8.14

Gördüğünüz gibi, değerleri her defasında tekrar yazmak yerine bunları bir
değişkene atayıp, gereken yerde bu değişkeni kullanmak çok daha pratik bir
yöntem.

Aynı şeyi programımız için de yapabiliriz::

    >>> kullanıcı_adı = "firat_ozgul_1980" 
    >>> parola = "rT%65#$hGfUY56123"

`=` işaretini kullanarak ilgili değerlere artık birer ad verdiğimiz, yani bu
değerleri birer değişkene atadığımız için, bu değerleri kullanmamız gereken
yerlerde değerlerin kendisini uzun uzun yazmak yerine, belirlediğimiz
değişken adlarını kullanabiliriz. Mesela::

    >>> len(kullanıcı_adı) 
    
    16 
    
    >>> len(parola) 
    
    17 
    
    >>> len(kullanıcı_adı) + len(parola) 
    
    33
    
    >>> k_adı_uzunluğu = len(kullanıcı_adı)
    >>> type(k_adı_uzunluğu)
    
    <class 'int'>

Gördüğünüz gibi, değişken kullanımı işlerimizi bir hayli kolaylaştırıyor.

Değişken Adı Belirleme Kuralları
---------------------------------

Python programlama dilinde, değişken adı olarak belirleyebileceğimiz kelime
sayısı neredeyse sınırsızdır. Yani hemen hemen her kelimeyi değişken adı olarak
kullanabiliriz. Ama yine de değişken adı belirlerken dikkat etmemiz gereken bazı
kurallar var. Bu kuralların bazıları zorunluluk, bazıları ise yalnızca tavsiye
niteliğindedir.

Şimdi bu kuralları tek tek inceleyelim:

\1. Değişken adları bir sayı ile başlayamaz. Yani şu kullanım yanlıştır::

    >>> 3_kilo_elma = "5 TL"

\2. Değişken adları aritmetik işleçlerle başlayamaz. Yani şu kullanım
yanlıştır::

    >>> +değer = 4568

\3. Değişken adları ya bir alfabe harfiyle ya da `_` işaretiyle başlamalıdır::

    >>> _değer = 4568 
    >>> değer = 4568

\4. Değişken adları içinde Türkçe karakterler kullanabilirsiniz. Ancak ileride
beklenmedik uyum sorunları çıkması ihtimaline karşı değişken adlarında Türkçe
karakter kullanmaktan kaçınmak isteyebilirsiniz.

\5. Aşağıdaki kelimeleri değişken adı olarak kullanamazsınız::

    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    
Bunlar Python'da özel anlam ifade eden kelimelerdir. Etkileşimli kabuk zaten bu
kelimeleri değişken adı olarak kullanmanıza izin vermez. Örneğin:: 

    >>> elif = "hoş kız"
    
      File "<stdin>", line 1
        elif = "hoş kız"
           ^
    SyntaxError: invalid syntax
    
    >>> as = "kare"

      File "<stdin>", line 1
        as = "kare"
         ^
    SyntaxError: invalid syntax
    
    >>> False = 45
    
      File "<stdin>", line 1
    SyntaxError: assignment to keyword
    
Ama ilerde göreceğimiz gibi, programlarınızı bir dosyaya yazarken bu kelimeleri
değişken adı olarak kullanmaya çalışırsanız programınız tespit etmesi çok güç
hatalar üretecektir.

Bu arada elbette yukarıdaki listeyi bir çırpıda ezberlemeniz beklenmiyor sizden.
Python programlama dilini öğrendikçe özel kelimeleri bir bakışta tanıyabilecek
duruma geleceksiniz. Ayrıca eğer isterseniz şu komutları vererek, istediğiniz
her an yukarıdaki listeye ulaşabilirsiniz::
    
    >>> import keyword
    >>> keyword.kwlist
    
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Size bir soru: Acaba bu listede kaç tane kelime var?

Bu soru karşısında listedeki kelimeleri tek tek elle saymaya kalkışan
arkadaşlarıma teessüflerimi iletiyorum... Bu tür işler için hangi aracı
kullanabileceğimizi artık çok iyi biliyor olmalısınız::
    
    >>> len(keyword.kwlist)
    
    33

Bu kodları şöyle yazabileceğimizi de biliyorsunuz::
    
    >>> yasaklı_kelimeler = keyword.kwlist
    >>> len(yasaklı_kelimeler)
    
    33
    
Bu arada, yukarıdaki kodların bir kısmını henüz anlayamamış olabilirsiniz. Hiç
endişe etmeyin. Yukarıdaki kodları vermemizin sebebi değişken adı olarak
kullanılamayacak kelimelere kısa yoldan nasıl ulaşabileceğinizi gösterebilmek
içindir. Bir-iki bölüm sonra burada yazdığımız kodları rahatlıkla anlayabilecek
düzeye geleceksiniz.

Yukarıda verdiğimiz kodların çıktısından anladığımıza göre, toplam `33` tane
kelime varmış değişken adı belirlerken kullanmaktan kaçınmamız gereken...
    
\6. Yukarıdaki kelimeler dışında, Python programlama diline ait fonksiyon ve
benzeri araçların adlarını da değişken adı olarak kullanmamalısınız. Örneğin
yazdığınız programlarda değişkenlerinize `type` veya `len` adı vermeyin. Çünkü
'type' ve 'len' Python'a ait iki önemli fonksiyonun adıdır. Eğer mesela bir
değişkene `type` adını verirseniz, o programda artık ``type()`` fonksiyonunu
kullanamazsınız::
    
    >>> type = 3456

Bu örnekte `type` adında bir değişken tanımladık. Şimdi mesela `"elma"`
kelimesinin tipini denetlemek için ``type()`` fonksiyonunu kullanmaya
çalışalım::
    
    >>> type("elma")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not callable

Gördüğünüz gibi, artık ``type()`` fonksiyonu çalışmıyor. Çünkü siz 'type'
kelimesini bir değişken adı olarak kullanarak, ``type()`` fonksiyonunu
kullanılamaz hale getirdiniz.

Bu durumdan kurtulmak için etkileşimli kabuğu kapatıp tekrar açabilirsiniz. Ya
da eğer etkileşimli kabuğu kapatmak istemiyorsanız şu komut yardımıyla `type`
değişkenini ortadan kaldırmayı da tercih edebilirsiniz::
    
    >>> del type

Böylece, (tahmin edebileceğiniz gibi *delete* (silmek) kelimesinin kısaltması
olan) ``del`` komutuyla `type` değişkenini silmiş oldunuz. Artık 'type' kelimesi
yine ``type()`` fonksiyonunu çağıracak::
    
    >>> type("elma")
    
    <class 'str'>

\7. Değişken adlarını belirlerken, değişkeni oluşturan kelimeler arasında boşluk
bırakılamaz. Yani şu kullanım yanlıştır::

    >>> kullanıcı adı = "istihza"

Yukarıdaki değişkeni şu şekilde tanımlayabiliriz::

    >>> kullanıcı_adı = "istihza"

Ya da şöyle::

    >>> kullanıcıAdı = "istihza"

\8. Değişken adları belirlerken, değişken adının, değişkenin değerini
olabildiğince betimlemesine dikkat etmemiz kodlarımızın okunaklılığını
artıracaktır. Örneğin::
    
    >>> personel_sayısı = 45
 
Yukarıdaki, tanımladığı değere uygun bir değişken adıdır. Şu ise kurallara 
uygun bir değişken adı olsa da yeterince betimleyici değildir::
    
    >>> sayı = 45

\9. Değişken adları ne çok kısa, ne de çok uzun olmalıdır. Mesela şu değişken
adı, kodları okuyan kişiye, değişken değerinin anlamı konusunda pek fikir
vermez::
    
    >>> a = 345542353

Şu değişken adı ise gereksiz yere uzundur::
    
    >>> türkiye_büyük_millet_meclisi_milletvekili_sayısı = 550

Değişken adlarının uzunluğunu makul seviyede tutmak esastır::
    
    >>> tbmm_mv_sayısı = 550
    
Yukarıda verdiğimiz bütün bu örnekler bize, Python'da değişkenlerin, değerlere
atanmış adlardan ibaret olduğunu gösteriyor. Değişkenler, yazdığımız
programlarda bize çok büyük kolaylık sağlar. Mesela `123432456322` gibi bir
sayıyı ya da `"Türkiye Cumhuriyeti Çalışma ve Sosyal Güvenlik Bakanlığı"` gibi
bir karakter dizisini gerektiği her yerde tek tek elle yazmak yerine, bunları
birer değişkene atayarak, gerektiğinde sadece bu değişken adını kullanmak çok
daha mantıklı bir iştir. 

Ayrıca zaten ileride kullanıcıdan veri almaya başladığınızda, aldığınız bu
verileri, yazdığınız programda kullanabilmek için mutlaka bir değişkene atamanız
gerekecek. O yüzden Python'daki değişken kavramını şimdiden iyi tanıyıp
anlamakta büyük fayda var.

Uygulama Örnekleri
-----------------------

Gelin isterseniz yukarıda verdiğimiz bilgileri pekiştirmek için birkaç ufak
alıştırma yapalım, alıştırma yaparken de sizi yine Python programlama diline
ilişkin çok önemli bazı yeni bilgilerle tanıştıralım.

Diyelim ki aylık yol masrafımızı hesaplayan bir program yazmak istiyoruz.
Elimizdeki verilerin şunlar olduğunu varsayalım:

1. Cumartesi-Pazar günleri çalışmıyoruz. 

2. Dolayısıyla ayda `22` gün çalışıyoruz. 

3. Evden işe gitmek için kullandığımız vasıtanın ücreti `1.5` TL 

4. İşten eve dönmek için kullandığımız vasıtanın ücreti `1.4` TL

Aylık yol masrafımızı hesaplayabilmek için gidiş ve dönüş ücretlerini toplayıp,
bunları çalıştığımız gün sayısıyla çarpmamız yeterli olacaktır. Elimizdeki bu
bilgilere göre aylık yol masrafımızı hesaplamak için şöyle bir formül
üretebiliriz::

    masraf = gün sayısı x (gidiş ücreti + dönüş ücreti)

Dilerseniz hemen bunu bir Python programı haline getirelim::

    >>> 22 * (1.5 + 1.4) 
    
    63.8

Demek ki bir ayda `63.8` TL'lik bir yol masrafımız varmış.

Bu arada, yukarıdaki örnekte bir şey dikkatinizi çekmiş olmalı. Aritmetik işlemi
yaparken bazı sayıları parantez içine aldık. Python'da aritmetik işlemler
yapılırken alıştığımız matematik kuralları geçerlidir. Yani mesela aynı anda
bölme, çıkarma, toplama ve çarpma işlemleri yapılacaksa işlem öncelik sırası
önce bölme ve çarpma, sonra toplama ve çıkarma şeklinde olacaktır. Elbette siz
parantezler yardımıyla bu işlem sırasını değiştirebilirsiniz.

Bu anlattıklarımıza göre, eğer yukarıda yol masrafını hesaplayan programda
parantezleri kullanmazsak, işlem öncelik kuralları gereğince Python önce `22`
ile `1.5`'i çarpıp, çıkan sonucu `1.4` ile toplayacağı için elde ettiğimiz sonuç
yanlış çıkacaktır. Bizim burada doğru sonuç alabilmemiz için önce `1.5` ile
`1.4`'ü toplamamız, çıkan sonucu da `22` ile çarpmamız gerekiyor. Bu sıralamayı
da parantezler yardımıyla elde ediyoruz.

Yine dikkat ederseniz, yukarıdaki örnek programda aslında çok verimsiz bir yol
izledik. Gördüğünüz gibi, bu programda bütün değerleri tek tek elle kendimiz
giriyoruz. Örneğin çalışılan gün sayısına karşılık gelen `22` değerini başka bir
yerde daha kullanmak istesek aynı sayıyı tekrar elle doğrudan kendimiz girmek
zorundayız. Mesela yılda kaç gün çalıştığımızı hesaplayalım::

    >>> 22 * 12 
    
    264

Gördüğünüz gibi, burada da `22` sayısına ihtiyaç duyduk. Aslında değerleri bu
şekilde her defasında tekrar tekrar elle girmek hem hata yapma riskini
artırdığı, hem de bize fazladan iş çıkardığı için tercih edilmeyen bir
yöntemdir. Bunun yerine, `22` sayısına bir isim verip, gereken yerlerde bu ismi
kullanmak daha mantıklı olacaktır. Yani tıpkı kullanıcı ve parola örneğinde
olduğu gibi, burada da verileri öncelikle bir değişkene atamak çok daha akıllıca
bir iştir::

    >>> gün = 22 
    >>> gidiş_ücreti = 1.5 
    >>> dönüş_ücreti = 1.4 
    >>> gün * (gidiş_ücreti + dönüş_ücreti) 
    
    63.8

Bütün değerleri birer değişkene atadığımız için, artık bu değişkenleri
istediğimiz yerde kullanabiliriz. Mesela yılda toplam kaç gün çalıştığımızı
bulmak istersek, ilgili değeri elle yazmak yerine, yukarıda tanımladığımız `gün`
değişkenini kullanabiliriz::

    >>> gün * 12 
    
    264

İlerleyen zamanda aylık çalışılan gün sayısı değişirse sadece `gün` değişkeninin
değerini değiştirmemiz yeterli olacaktır::

    >>> gün = 23 
    >>> gün * (gidiş_ücreti + dönüş_ücreti) 
    
    66.7 
    
    >>> gün * 12 
    
    276

Eğer bu şekilde değişken atamak yerine, değerleri gerektiği her yerde elle
yazsaydık, bu değerlerde herhangi bir değişiklik yapmamız gerektiğinde program
içinde geçen ilgili bütün değerleri bulup tek tek değiştirmemiz gerekecekti::

    >>> 23 * (1.6 + 1.5) 
    
    71.3 
    
    >>> 23 * 12 
    
    276

Değişken kavramı şu anda gözünüze pek anlamlı görünmemiş olabilir. Ama
programlarımızı ilerde dosyaya kaydettiğimiz zaman bu değişkenler çok daha
kullanışlı araçlar olarak karşımıza çıkacaktır.

Dilerseniz bir örnek daha yaparak yukarıdaki bilgilerin kafamıza iyice
yerleşmesiniz sağlayalım. Mesela bir dairenin alanını (yaklaşık olarak)
hesaplayan bir program yazalım.

Öncelikle `çap` adlı bir değişken tanımlayarak dairenin çapını belirleyelim::

    >>> çap = 16

Bu değeri kullanarak dairemizin yarıçapını hesaplayabiliriz. Bunun için `çap`
değişkeninin değerinin yarısını almamız yeterli olacaktır::

    >>> yarıçap = çap / 2

pi sayısını `3.14159` olarak alalım.

    >>> pi = 3.14159

Bir dairenin alan formülü (pi)r\ :sup:`2`'dir::

    >>> alan = pi * (yarıçap * yarıçap)

Son olarak `alan` değişkeninin değerini ekrana yazdırabiliriz::

    >>> alan 
    
    201.06176

Böylece bir dairenin alanını yaklaşık olarak hesaplamış olduk. Dilerseniz
programımızı bir de derli toplu olarak görelim::

    >>> çap = 16 
    >>> yarıçap = çap / 2 
    >>> pi = 3.14159 
    >>> alan = pi * (yarıçap * yarıçap) 
    >>> alan 
    
    201.06176

Görüyorsunuz ya, değişkenler işimizi nasıl da kolaylaştırıyor. Eğer yukarıdaki
programda değişken kullanmasaydık kodlarımız şöyle görünecekti::

    >>> 3.14159 * ((16/2) * (16/2)) 
    
    201.06176

Bu kodlar tek kullanımlıktır. Eğer yukarıdaki örnekte mesela dairenin çapını
değiştirmeniz gerekirse, iki yerde elle değişiklik yapmanız gerekir. Ama
değişkenleri kullandığımızda sadece `çap` değişkeninin değerini değiştirmeniz
yeterli olacaktır. Ayrıca değişken kullanmadığınızda, ilgili değeri program
boyunca aklınızda tutmanız gerekir. Örneğin `çap` değişkenini kullanmak yerine,
gereken her yerde `16` değerini kullanacaksanız, bu `16` değerini sürekli
aklınızda tutmanız lazım. Ama bu değeri en başta bir değişkene atarsanız, `16`
değerini kullanmanız gereken yerlerde, akılda tutması daha kolay bir ifade olan
`çap` ismini kullanabilirsiniz.

Bu arada yeri gelmişken sizi yeni bir işleçle daha tanıştıralım. Şimdiye kadar
Python'da toplama (`+`), çıkarma (`-`), çarpma (`*`), bölme (`/`) ve değer atama
(`=`) işleçlerini gördük. Ama yukarıda verdiğimiz son örnek, başka bir işleç
daha öğrenmemizi gerektiriyor...

Yukarıdaki şu örneğe tekrar bakalım::
    
    alan = pi * (yarıçap * yarıçap)

Burada `yarıçap` değişkeninin karesini alabilmek için bu değeri kendisiyle
çarptık. Aslında gayet mantıklı ve makul bir yöntem. Kare bulmak için değeri
kendisiyle çarpıyoruz. Eğer bir sayının küpünü bulmak isteseydik o sayıyı üç kez
kendisiyle çarpacaktık::
    
    >>> 3 * 3 * 3
    
    27

Peki ya bir sayının mesela beşinci kuvvetini hesaplamak istersek ne yapacağız? O
sayıyı beş kez kendisiyle mi çarpacağız? Bu ne kadar vasat bir yöntem, değil mi?

Elbette bir sayının herhangi bir kuvvetini hesaplamak için o sayıyı kendisiyle
kuvvetince çarpmayacağız. Python'da bu tür 'kuvvet hesaplamaları' için ayrı bir
işleç (ve fonksiyon) bulunur.

Öncelikle kuvvet hesaplarını yapmamızı sağlayan işleçten söz edelim. 

Python'da `**` adlı bir işleç bulunur. Bu işlecin görevi bir sayının kuvvetini
hesaplamamızı sağlamaktır. Örneğin bir sayının `2.` kuvvetini, ya da başka bir
deyişle karesini hesaplamak istersek şöyle bir kod yazabiliriz::
    
    >>> 12 ** 2
    
    144

Burada `12` sayısının `2.` kuvvetini, yani karesini hesapladık. Bu bilgiyi
yukarıdaki formüle uygulayalım::
    
    >>> alan = pi * (yarıçap ** 2)

Bu işleci herhangi bir sayının herhangi bir kuvvetini hesaplamak için
kullanabiliriz elbette. Mesela `23` sayısının küpünü (yani `3.` kuvvetini)
hesaplayalım::
    
    >>> 23 ** 3
    
    12167

Aynı işleçten, bir sayının karekökünü hesaplamak için de yararlanabilirsiniz.
Neticede bir sayının `0.5`'inci kuvveti, o sayının kareköküdür::
    
    >>> 144 ** 0.5
    
    12.0

Gördüğünüz gibi, kuvvet hesaplama işlemleri için bu işleç son derece kullanışlı
bir araç vazifesi görüyor. Ama eğer istersek aynı iş için özel bir fonksiyondan
da yararlanabiliriz. Bu fonksiyonun adı ``pow()``.

Peki bu fonksiyonu nasıl kullanacağız?

Daha önce öğrendiğimiz ``type()`` ve ``len()`` fonksiyonlarını nasıl
kullanıyorsak ``pow()`` fonksiyonu da aynı şekilde kullanacağız.

``type()`` ve ``len()`` fonksiyonlarını birtakım parametreler ile birlikte
kullanıyorduk hatırlarsanız. Aynı şekilde ``pow()`` fonksiyonu da birtakım
parametreler alır.

Daha önce öğrendiğimiz fonksiyonları tek bir parametre ile birlikte
kullanmıştık. ``pow()`` fonksiyonu ise toplam üç farklı parametre alır. Ama
genellikle bu fonksiyon yalnızca iki parametre ile kullanılır.

Bu fonksiyonu şöyle kullanıyoruz::
    
    >>> pow(12, 2)
    
    144
    
    >>> pow(23, 3)
    
    12167
    
    >>> pow(144, 0.5)
    
    12.0

Gördüğünüz gibi, ``pow()`` fonksiyonunun ilk parametresi asıl sayıyı, ikinci
parametresi ise bu sayının hangi kuvvetini hesaplamak istediğimizi gösteriyor.

Bu arada, fonksiyonun parantezleri içinde belirttiğimiz parametreleri
birbirinden virgül ile ayırdığımızı gözden kaçırmayın.

Dediğimiz gibi, ``pow()`` fonksiyonu, pek kullanılmayan üçüncü bir parametre
daha alır. Bu fonksiyonun üçüncü parametresi şöyle kullanılır. Dikkatlice
bakın::
    
    >>> pow(16, 2, 2)
    
    0

Bu komut şu anlama gelir: 

    `16` sayısının `2`'nci kuvvetini hesapla ve çıkan sayıyı `2`'ye bölüp, bölme
    işleminden kalan sayıyı göster!

`16` sayısının `2.` kuvveti `256` sayısıdır. `256` sayısını `2`'ye böldüğümüzde,
bölme işleminin kalanı `0`'dır. Yani `256` sayısı `2`'ye tam bölünür... 

Bir örnek daha verelim::
    
    >>> pow(11, 3, 4)
    
    3

Demek ki, `11` sayısının `3.` kuvveti olan `1331` sayısı `4`'e bölündüğünde,
bölme işleminden kalan sayı `3` imiş...

Dediğimiz gibi, ``pow()`` fonksiyonu genellikle sadece iki parametre ile
kullanılır. Üçüncü parametrenin kullanım alanı oldukça dardır.

Değişkenlere Dair Bazı İpuçları
--------------------------------

Değişkenin ne demek olduğunu öğrendiğimize göre, değişkenlere dair bazı ufak
ipuçları verebiliriz.

Aynı Değere Sahip Değişkenler Tanımlama 
........................................

Şimdi size şöyle bir soru sormama izin verin: Acaba aynı değere sahip iki
değişkeni nasıl tanımlayabiliriz? Yani mesela değeri `4` sayısı olan iki farklı
değişkeni nasıl belirleyeceğiz?

Aklınıza şöyle bir çözüm gelmiş olabilir::

    >>> a = 4 
    >>> b = 4

Böylece ikisi de `4` değerine sahip `a` ve `b` adlı iki farklı değişken
tanımlamış olduk. Bu tamamen geçerli bir yöntemdir. Ancak Python'da bu işlemi
yapmanın daha kolay bir yolu var. Bakalım::

    >>> a = b = 4 
    
Bu kodlar bir öncekiyle tamamen aynı işlevi görür. Yani her iki kod da `4`
değerine sahip `a` ve `b` değişkenleri tanımlamamızı sağlar::
    
    >>> a 
    
    4 
    
    >>> b 
    
    4

Bu bilgiyi kullanarak mesela bir yıl içindeki her bir ayın çektiği gün sayısını
ay adlarına atayabilirsiniz::

    >>> ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31 
    >>> nisan = haziran = eylül = kasım = 30 
    >>> şubat = 28

Böylece bir çırpıda değeri `31` olan yedi adet değişken, değeri `30` olan dört
adet değişken, değeri `28` olan bir adet değişken tanımlamış olduk. Bu
değişkenlerin değerine nasıl ulaşacağınızı biliyorsunuz::

    >>> ocak 
    
    31 
    >>> haziran 
    
    30 
    
    >>> şubat 
    
    28 
    
    >>> mayıs 
    
    31 
    
    >>> ekim 
    
    31 
    
    >>> eylül
    
    30

Eğer Python'ın aynı anda birden fazla değişkene tek bir değer atama özelliği
olmasaydı yukarıdaki kodları şöyle yazmamız gerekirdi::

    >>> ocak = 31 
    >>> şubat = 28 
    >>> mart = 31 
    >>> nisan = 30 
    >>> mayıs = 31 
    >>> haziran = 30 
    >>> temmuz = 31 
    >>> ağustos = 31 
    >>> eylül = 30 
    >>> ekim = 31
    >>> kasım = 30 
    >>> aralık = 31

Bu değişkenleri nasıl bir program içinde kullanacağınız tamamen sizin hayal
gücünüze kalmış. Mesela bu değişkenleri kullanarak aylara göre doğalgaz
faturasını hesaplayan bir program yazabiliriz.

Hemen son gelen doğalgaz faturasını (örn. Mart ayı) elimize alıp inceliyoruz ve
bu faturadan şu verileri elde ediyoruz:

Mart ayı doğalgaz faturasına göre sayaçtan ölçülen hacim `346` m\ :sup:`3`.
Demek ki bir ayda toplam `346` m\ :sup:`3` doğalgaz harcamışız.

Fatura tutarı `273.87` TL imiş. Yani `346` m\ :sup:`3` doğalgaz tüketmenin
bedeli `273.87` TL. Buna göre değişkenlerimizi tanımlayalım::

    >>> aylık_sarfiyat = 346 
    >>> fatura_tutarı = 273.87

Bu bilgiyi kullanarak doğalgazın birim fiyatını hesaplayabiliriz. Formülümüz
şöyle olmalı::

    >>> birim_fiyat = fatura_tutarı / aylık_sarfiyat

    >>> birim_fiyat 
    
    0.7915317919075144

Demek ki doğalgazın m\ :sup:`3` fiyatı (vergilerle birlikte yaklaşık) `0.79`
TL'ye karşılık geliyormuş.

Bu noktada günlük ortalama doğalgaz sarfiyatımızı da hesaplamamız gerekiyor::

    >>> günlük_sarfiyat = aylık_sarfiyat / mart 
    >>> günlük_sarfiyat
   
    11.161290322580646

Demek ki Mart ayında günlük ortalama `11` m\ :sup:`3` doğalgaz tüketmişiz.

Bütün bu bilgileri kullanarak Nisan ayında gelecek faturayı tahmin edebiliriz::

    >>> nisan_faturası = birim_fiyat * günlük_sarfiyat * nisan 
    >>> nisan_faturası

    265.03548387096777

Şubat ayı faturası ise şöyle olabilir::

    >>> şubat_faturası = birim_fiyat * günlük_sarfiyat * şubat 
    >>> şubat_faturası
    
    247.36645161290326

Burada farklı değişkenlerin değerini değiştirerek daha başka işlemler de
yapabilirsiniz. Örneğin pratik olması açısından `günlük_sarfiyat` değişkeninin
değerini `15` yaparak hesaplamalarınızı buna göre güncelleyebilirsiniz.

Gördüğünüz gibi, aynı anda birden fazla değişken tanımlayabilmek işlerimizi epey
kolaylaştırıyor.

Değişkenlerle ilgili bir ipucu daha verelim...

Değişkenlerin Değerini Takas Etme 
..................................

Diyelim ki, işyerinizdeki personelin unvanlarını tuttuğunuz bir veritabanı var
elinizde. Bu veritabanında şuna benzer ilişkiler tanımlı::

    >>> osman = "Araştırma Geliştirme Müdürü" 
    >>> mehmet = "Proje Sorumlusu"

İlerleyen zamanda işvereniniz sizden Osman ve Mehmet'in unvanlarını
değiştirmenizi talep edebilir. Yani Osman'ı Proje Sorumlusu, Mehmet'i de
Araştırma Geliştirme Müdürü yapmanızı isteyebilir sizden.

Patronunuzun bu isteğini Python'da çok rahat bir biçimde yerine
getirebilirsiniz. Dikkatlice bakın::

    >>> osman, mehmet = mehmet, osman

Böylece tek hamlede bu iki kişinin unvanlarını takas etmiş oldunuz. Gelin
isterseniz değişkenlerin son durumuna bakalım:: 

    >>> osman 
    
    'Proje Sorumlusu 
    
    >>> mehmet 
    
    'Araştırma Geliştirme Müdürü'

Gördüğünüz gibi, `osman` değişkeninin değerini `mehmet`'e; `mehmet` değişkeninin
değerini ise `osman`'a başarıyla verebilmişiz.

Yukarıdaki yöntem Python'ın öteki diller üzerinde önemli bir üstünlüğüdür. Başka
programlama dillerinde bu işlemi yapmak için geçici bir değişken tanımlamanız
gerekir. Yani mesela::

    >>> osman = "Araştırma Geliştirme Müdürü" 
    >>> mehmet = "Proje Sorumlusu"

Elimizdeki değerler bunlar. Biz şimdi Osman'ın değerini Mehmet'e; Mehmet'in
değerini ise Osman'a aktaracağız. Bunun için öncelikle bir geçici değişken
tanımlamalıyız::

    >>> geçici = "Proje Sorumlusu"

Bu sayede `"Proje Sorumlusu"` değerini yedeklemiş olduk. Bu işlem sayesinde,
takas sırasında bu değeri kaybetmeyeceğiz.

Şimdi Osman'ın değerini Mehmet'e aktaralım::

    >>> mehmet = osman

Şimdi elimizde iki tane Araştırma Geliştirme Müdürü olmuş oldu::

    >>> mehmet 
    
    'Araştırma Geliştirme Müdürü' 
    
    >>> osman 
    
    'Araştırma Geliştirme Müdürü'

Gördüğünüz gibi, ``mehmet = osman`` kodunu kullanarak `mehmet` değişkeninin
değerini `osman` değişkeninin değeriyle değiştirdiğimiz için `"Proje Sorumlusu"`
değeri ortadan kayboldu. Ama biz önceden bu değeri `geçici` adlı değişkene
atadığımız için bu değeri kaybetmemiş olduk. Şimdi Osman'a `geçici` değişkeni
içinde tuttuğumuz `"Proje Sorumlusu"` değerini verebiliriz::

    >>> osman = geçici

Böylece istediğimiz takas işlemini gerçekleştirmiş olduk. Son durumu kontrol
edelim::

    >>> osman 
    
    'Proje Sorumlusu 
    
    >>> mehmet 
    
    'Araştırma Geliştirme Müdürü'

Basit bir işlem için ne kadar büyük bir zaman kaybı, değil mi? Ama dediğimiz
gibi, Python'da bu şekilde geçici bir değişken atamakla uğraşmamıza hiç gerek
yok. Sadece şu formülü kullanarak değişkenlerin değerini takas edebiliriz::

    a, b = b, a 
    
Bu şekilde `a` değişkeninin değerini `b` değişkenine; `b` değişkeninin değerini
ise `a` değerine vermiş oluyoruz. Eğer bu işlemi geri alıp her şeyi eski haline
döndürmek istersek, tahmin edebileceğiniz gibi yine aynı yöntemden
yararlanabiliriz::

    b, a = a, b

Böylece değişkenler konusunu da oldukça ayrıntılı bir şekilde incelemiş olduk.
Ayrıca bu esnada ``len()`` ve ``pow()`` adlı iki yeni fonksiyon ile `**` adlı
bir işleç de öğrendik.

Hazır lafı geçmişken, ``len()`` fonksiyonunun bazı kısıtlamalarından söz edelim.
Dediğimiz gibi, bu fonksiyonu kullanarak karakter dizileri içinde toplam kaç
adet karakter bulunduğunu hesaplayabiliyoruz. Örneğin::

    >>> kelime = "muvaffakiyet" 
    >>> len(kelime) 
    
    12

Yalnız bu ``len()`` fonksiyonunu sayıların uzunluğunu ölçmek için
kullanamıyoruz::

    >>> len(123456)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

Gördüğünüz gibi, ``len()`` fonksiyonu, şu ana kadar öğrendiğimiz veri tipleri
arasında yalnızca karakter dizileri ile birlikte kullanılabiliyor. Bu fonksiyonu
sayılarla birlikte kullanamıyoruz.

Bu bölümün başında, o anda elimizde bulunan bir verinin tipini bilmemizin çok
önemli olduğunu ve Python'da bir verinin tipinin, o veri ile neler yapıp neler
yapamayacağınızı belirlediğini söylediğimizi hatırlıyorsunuz, değil mi? İşte
``len()`` fonksiyonu bu duruma çok güzel bir örnektir.

``len()`` fonksiyonu sayılarla birlikte kullanılamaz. Dolayısıyla eğer
elinizdeki verinin bir sayı olduğunu bilmezseniz, bu sayıyı ``len()`` fonksiyonu
ile birlikte kullanmaya çalışabilir ve bu şekilde programınızın hata vererek
çökmesine yol açabilirsiniz.

Ayrıca daha önce de söylediğimiz gibi, ``len()`` fonksiyonunu doğru
kullanabilmek için, bu fonksiyonun bize sayı değerli bir çıktı verdiğini de
bilmemiz gerekir.

``len()`` fonksiyonu ile ilgili bu durumu da bir kenara not ettikten sonra
yolumuza kaldığımız yerden devam edelim.

Etkileşimli Kabuğun Hafızası 
**************************** 

Bir önceki bölümde Python'ın etkileşimli kabuğunun nasıl kullanılacağına dair
epey örnek verdik ve etkileşimli kabuk üzerinden Python'ın bazı temel araçlarına
kısa bir giriş yaptık. Şimdi isterseniz yeri gelmişken Python'ın etkileşimli
kabuğunun bir başka yeteneğinden daha söz edelim.

Etkileşimli kabukta `_` adlı işaret (alt çizgi işareti), yapılan son işlemin
veya girilen son öğenin değerini tutma işlevi görür. Yani::

    >>> 2345 + 54355 
    
    56700

Eğer bu işlemin ardından ``_`` komutunu verirsek şöyle bir çıktı alırız::

    >>> _ 
    
    56700

Gördüğünüz gibi, ``_`` komutu son girilen öğeyi hafızasında tutuyor. Bu
özellikten çeşitli şekillerde yararlanabilirsiniz::

    >>> _ + 15 
    
    56715 
    
Burada ``_`` komutunun değeri bir önceki işlemin sonucu olan `56715` değeri
olduğu için, ``_`` komutuna `15` eklediğimizde `56715` değerini elde ediyoruz.
``_`` komutunun değerini tekrar kontrol edelim::

    >>> _ 
    
    56715

Gördüğünüz gibi, ``_`` komutunun değeri artık `56715` sayısıdır...

``_`` komutu yalnızca sayıları değil, karakter dizilerini de hafızasında
tutabilir::

    >>> "www" 
    
    'www' 
    
    >>> _ 
    
    'www' 
    
    >>> _ + ".istihza.com" 
    
    'www.istihza.com'

Bu işaret öyle çok sık kullanılan bir araç değildir, ama zaman zaman işinizi
epey kolaylaştırır. Yalnız, unutmamamız gereken şey, bu özelliğin sadece
etkileşimli kabuk ortamında geçerli olmasıdır. ``_`` komutunun etkileşimli kabuk
ortamı dışında herhangi bir geçerliliği yoktur.

Aslında burada söylenecek daha çok şey var. Ama biz şimdilik bunları sonraki
konulara bırakacağız. Zira bu bölümdeki amacımız size konuların her ayrıntısını
vermekten ziyade, Python'a ısınmanızı sağlamaktır.
