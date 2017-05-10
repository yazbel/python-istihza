.. meta::
   :description: Bu bölümde işleçleri inceleyeceğiz.
   :keywords: python, işlec, bool, aritmetik, True, False, eşit, eşit değil, 
    karşılaştırma, değer atama, aitlik, kimlik
   
.. highlight:: python3

*********
İşleçler
*********


Bu bölümde, aslında pek de yabancısı olmadığımız ve hatta önceki derslerimizde
üstünkörü de olsa değindiğimiz bir konuyu çok daha ayrıntılı bir şekilde ele
alacağız. Burada anlatacağımız konu size yer yer sıkıcı gelebilir. Ancak bu
konuyu hakkıyla öğrenmenizin, programcılık maceranız açısından hayati önemde
olduğunu rahatlıkla söyleyebilirim.

Gelelim konumuza...

Bu bölümün konusu işleçler. Peki nedir bu 'işleç' denen şey?

İngilizce'de *operator* adı verilen işleçler, sağında ve solunda bulunan
değerler arasında bir ilişki kuran işaretlerdir. Bir işlecin sağında ve solunda
bulunan değerlere ise işlenen (*operand*) adı veriyoruz.

.. note:: Türkçede işleç yerine operatör, işlenen yerine de operant dendiğine 
          tanık olabilirsiniz. 

Biz bu bölümde işleçleri altı başlık altında inceleyeceğiz: 

    #. Aritmetik İşleçler 
    
    #. Karşılaştırma İşleçleri
    
    #. Bool İşleçleri
    
    #. Değer Atama İşleçleri
    
    #. Aitlik İşleçleri
    
    #. Kimlik İşleçleri
    
Gördüğünüz gibi, işlememiz gereken konu çok, gitmemiz gereken yol uzun. O halde
hiç vakit kaybetmeden, aritmetik işleçlerle yolculuğumuza başlayalım.

Aritmetik İşleçler
*******************

Dedik ki, sağında ve solunda bulunan değerler arasında bir ilişki kuran
işaretlere işleç (*operator*) adı verilir. Önceki derslerimizde temel işleçlerin
bazılarını öğrenmiştik. İsterseniz bunları şöyle bir hatırlayalım:

   +------+---------+
   | `+`  | toplama |
   +------+---------+
   | `-`  | çıkarma |
   +------+---------+
   | `*`  | çarpma  |
   +------+---------+
   | `/`  | bölme   |
   +------+---------+
   | `**` | kuvvet  |
   +------+---------+
    
Bu işleçlere aritmetik işleçler adı verilir. Aritmetik işleçler; matematikte
kullanılan ve sayılarla aritmetik işlemler yapmamızı sağlayan yardımcı
araçlardır.

Dilerseniz bu tanımı bir örnekle somutlaştıralım::

    >>> 45 + 33
    
    78

Burada `45` ve `33` değerlerine işlenen (*operand*) adı verilir. Bu iki değer
arasında yer alan `+` işareti ise bir işleçtir (*operator*). Dikkat ederseniz
`+` işleci `45` ve `33` adlı işlenenler arasında bir toplama ilişkisi kuruyor.

Bir örnek daha verelim::

    >>> 23 * 46
    
    1058

Burada da `23` ve `46` değerleri birer işlenendir. Bu iki değer arasında yer
alan `*` işareti ise, işlenenler arasında bir çarpma ilişkisi kuran bir
işleçtir.

Ancak bir noktaya özellikle dikkatinizi çekmek istiyorum. Daha önceki
derslerimizde de değindiğimiz gibi, `+` ve `*` işleçleri Python'da birden fazla
anlama gelir. Örneğin yukarıdaki örnekte `+` işleci, işlenenler arasında bir
toplama ilişkisi kuruyor. Ama aşağıdaki durum biraz farklıdır::
    
    >>> "istihza" + ".com"
    
    'istihza.com'

Burada `+` işleci işlenenler (`"istihza"` ve `".com"`) arasında bir birleştirme
ilişkisi kuruyor.

Tıpkı `+` işlecinde olduğu gibi, `*` işleci de Python'da birden fazla anlama
gelir. Bu işlecin, çarpma ilişkisi kurma işlevi dışında tekrar etme ilişkisi
kurma işlevi de vardır. Yani::
    
    >>> "hızlı " * 2
    
    'hızlı hızlı '

...veya::

    >>> "-" * 30
    
    '------------------------------'

Burada `*` işlecinin, sayılar arasında çarpma işlemi yapmak dışında bir görev
üstlendiğini görüyoruz.

Python'da bu tür farklar, yazacağınız programın sağlıklı çalışabilmesi açısından
büyük önem taşır. O yüzden bu tür farklara karşı her zaman uyanık olmamız
gerekiyor. 

`+` ve `*` işleçlerinin aksine `/` ve `-` işleçleri ise işlenenler arasında
sadece bölme ve çıkarma ilişkisi kurar. Bu işleçler tek işlevlidir::
    
    >>> 25 / 4
    
    6.25
    
    >>> 10 - 5
    
    5
    
Önceki derslerde gördüğümüz ve yukarıda da tekrar ettiğimiz dört adet temel
aritmetik işlece şu iki aritmetik işleci de ekleyelim:

   +------+----------------------------+
   | `%`  | modülüs                    |
   +------+----------------------------+
   | `//` | taban bölme                |
   +------+----------------------------+ 

İlk önce modülüsün ne olduğunu ve ne işe yaradığını anlamaya çalışalım. 

Şu bölme işlemine bir bakın:

.. image:: ../images/misc/bolme.png
    :align: center
    
Burada `02` sayısı bölme işleminin kalanıdır. İşte modülüs denen işleç de bölme
işleminden kalan bu değeri gösterir. Yani::
    
    >>> 30 % 4
    
    2

Gördüğünüz gibi modülüs işleci (`%`) gerçekten de bölme işleminden kalan sayıyı
gösteriyor... Peki bu bilgi ne işimize yarar?

Mesela bu bilgiyi kullanarak bir sayının tek mi yoksa çift mi olduğunu tespit
edebiliriz::

    sayı = int(input("Bir sayı girin: "))
    
    if sayı % 2 == 0:
        print("Girdiğiniz sayı bir çift sayıdır.")
    else:
        print("Girdiğiniz sayı bir tek sayıdır.")

Eğer bir sayı `2`'ye bölündüğünde kalan değer `0` ise o sayı çifttir. Aksi halde
o sayı tektir. Mesela::
    
    >>> 14 % 2
    
    0

Gördüğünüz gibi, bir çift sayı olan `14`'ü `2`'ye böldüğümüzde kalan sayı `0`
oluyor. Çünkü çift sayılar `2`'ye tam bölünürler.

Bir de şuna bakalım::

    >>> 15 % 2
    
    1

Bir tek sayı olan `15` ise `2`'ye bölündüğünde kalan sayı `1` oluyor. Yani `15`
sayısı `2`'ye tam bölünmüyor. Bu bilgiden yola çıkarak 15 sayısının bir tek sayı
olduğunu söyleyebiliyoruz.

Bir sayının tek mi yoksa çift mi olduğunu tespit etme işlemini küçümsememenizi
tavsiye ederim. Bir sayının tek mi yoksa çift mi olduğu bilgisinin, arayüz
geliştirirken dahi işinize yarayacağından emin olabilirsiniz.

Elbette modülüs işlecini bir sayının yalnızca `2`'ye tam bölünüp bölünmediğini
denetlemek için kullanmıyoruz. Bu işleci kullanarak herhangi bir sayının
herhangi bir sayıya tam bölünüp bölünmediğini de denetleyebilirsiniz. Örneğin::
    
    >>> 45 % 4
    
    1
    
    >>> 36 % 9
    
    0

Bu bilgiyi kullanarak mesela şöyle bir program yazabilirsiniz::
    
    bölünen = int(input("Bir sayı girin: "))
    bölen = int(input("Bir sayı daha girin: "))
    
    şablon = "{} sayısı {} sayısına tam".format(bölünen, bölen)
    
    if bölünen % bölen == 0:
        print(şablon, "bölünüyor!")
    else:
        print(şablon, "bölünmüyor!")

Programımız, kullanıcının girdiği ilk sayının ikinci sayıya tam bölünüp
bölünmediğini hesaplıyor ve sonuca göre kullanıcıyı bilgilendiriyor. Bu kodlarda
özellikle şu satıra dikkat edin::
    
    if bölünen % bölen == 0:
        ...
        
Programımızın temelini bu kod oluşturuyor. Çünkü bir sayının bir sayıya tam
bölünüp bölünmediğini bu kodla belirliyoruz. Eğer bir sayı başka bir sayıya
bölündüğünde kalan değer, yani modülüs `0` ise, o sayı öbür sayıya tam bölünüyor
demektir.

Ayrıca bir sayının son basamağını elde etmek için de modülüsten
yararlanabilirsiniz. Herhangi bir tamsayı `10`'a bölündüğünde kalan (yani
modülüs), bölünen sayının son basamağı olacaktır::
    
    >>> 65 % 10
    
    5
    
    >>> 543 % 10
    
    3

Programlama tecrübeniz arttıkça, aslında modülüsün ne kadar faydalı bir araç
olduğunu kendi gözlerinizle göreceksiniz.

Modülüs işlecini örnekler eşliğinde ayrıntılı bir şekilde incelediğimize göre
sıra geldi taban bölme işlecini açıklamaya...

Öncelikle şu örneği inceleyelim::

    >>> 5 / 2
    
    2.5
    
Burada, bildiğimiz bölme işlecini (`/`) kullanarak basit bir bölme işlemi
yaptık. Elde ettiğimiz sonuç doğal olarak `2.5`.

Matematikte bölme işleminin sonucunun kesirli olması durumuna 'kesirli bölme'
adı verilir. Bunun tersi ise tamsayılı bölme veya taban bölmedir. Eğer herhangi
bir sebeple kesirli bölme işlemi değil de taban bölme işlemi yapmanız gerekirse
`//` işlecinden yararlanabilirsiniz::
    
    >>> 5 // 2
    
    2

Gördüğünüz gibi, `//` işleci sayesinde bölme işleminin sonucu kesirli değil,
tamsayı olarak elde ediliyor.

Yukarıda yaptığımız taban bölme işlemi şununla aynı anlama gelir::

    >>> int(5 / 2)
    
    2
    
Daha açık ifade etmemiz gerekirse::

    >>> a = 5 / 2
    >>> a
    
    2.5
    
    >>> int(a)
    
    2

Burada olan şu: ``5 / 2`` işleminin sonucu bir kayan noktalı sayıdır (`2.5`).
Bunu şu şekilde teyit edebiliriz::
    
    >>> a = 5 / 2
    >>> type(a)
    
    <class 'float'>

Buradaki `float` çıktısının *floating point number*, yani kayan noktalı sayı
anlamına geldiğini biliyorsunuz.

Bu kayan noktalı sayının sadece tabanını elde etmek için bu sayıyı tamsayıya
(*integer*) çevirmemiz yeterli olacaktır. Yani::
    
    >>> int(a)
    
    2

Bu arada yeri gelmişken ``round()`` adlı bir gömülü fonksiyondan bahsetmeden
geçmeyelim. Eğer bir sayının değerini yuvarlamanız gerekirse ``round()``
fonksiyonundan yararlanabilirsiniz. Bu fonksiyon şöyle kullanılır::
    
    >>> round(2.55)
    
    3

Gördüğünüz gibi, ``round()`` fonksiyonuna parametre olarak bir sayı veriyoruz.
Bu fonksiyon da bize o sayının yuvarlanmış halini döndürüyor. Bu fonksiyonu
kullanarak yuvarlanacak sayının noktadan sonraki hassasiyetini de
belirleyebilirsiniz. Örneğin::
    
    >>> round(2.55, 1)
    
    2.5

Burada ikinci parametre olarak `1` sayısını verdiğimiz için, noktadan sonraki
bir basamak görüntüleniyor. Bir de şuna bakalım::
    
    >>> round(2.68, 1)
    
    2.7

Burada da yuvarlama işlemi yapılırken noktadan sonra bir basamak korunuyor. Eğer
`1` sayısı yerine `2` sayısını kullanırsanız, yukarıdaki örnek şu çıktıyı
verir::
    
    >>> round(2.68, 2)
    
    2.68

``round()`` fonksiyonunun çalışma prensibini anlamak için kendi kendinize
örnekler yapabilirsiniz.

Şimdiye kadar öğrendiğimiz ve yukarıdaki tabloda andığımız bir başka aritmetik 
işleç de kuvvet işleci (`**`) idi. Mesela bu işleci kullanarak bir sayının
karesini hesaplayabileceğimizi biliyorsunuz::
    
    >>> 25 ** 2
    
    625
    
Bir sayının `2.` kuvveti o sayının karesidir. Bir sayının `0.5.` kuvveti ise o
sayının kareköküdür::
    
    >>> 625 ** 0.5
    
    25.0

Bu arada, eğer karekökün kayan noktalı sayı cinsinden olması hoşunuza
gitmediyse, bu sayıyı ``int()`` fonksiyonu ile tam sayıya çevirebileceğinizi
biliyorsunuz::
    
    >>> int(625 ** 0.5)
    
    25

Kuvvet hesaplamaları için `**` işlecinin yanısıra ``pow()`` adlı bir
fonksiyondan da yararlanabileceğimizi öğrenmiştik::
    
    >>> pow(25, 2)
    
    625

Bildiğiniz gibi ``pow()`` fonksiyonu aslında toplam üç parametre alabiliyor::
    
    >>> pow(25, 2, 5)
    
    0

Bu işlemin şununla aynı anlama geliyor::
    
    >>> (25 ** 2) % 5
    
    0

Yani ``pow(25, 2, 5)`` gibi bir komut verdiğimizde, `25` sayısının `2.`
kuvvetini alıp, elde ettiğimiz sayının `5`'e bölünmesinden kalan sayıyı
hesaplamış oluyoruz.

Böylece aritmetik işleçleri tamamlamış olduk. Artık karşılaştırma işleçlerini
inceleyebiliriz.

Karşılaştırma İşleçleri
***********************

Adından da anlaşılacağı gibi, karşılaştırma işleçleri, işlenenler (*operands*)
arasında bir karşılaştırma ilişkisi kuran işleçlerdir. Bu işleçleri şöyle
sıralayabiliriz:

   +------+------------------------------+
   | `==` | eşittir                      |
   +------+------------------------------+
   | `!=` | eşit değildir                |
   +------+------------------------------+  
   | `>`  | büyüktür                     |
   +------+------------------------------+ 
   | `<`  | küçüktür                     |
   +------+------------------------------+
   | `>=` | büyük eşittir                |
   +------+------------------------------+ 
   | `<=` | küçük eşittir                |
   +------+------------------------------+
   
Bu işleçlerin hiçbiri size yabancı değil, zira bunların hepsini aslında daha
önceki derslerde verdiğimiz örneklerde kullanmıştık. Burada da bunlarla ilgili
basit bir örnek vererek yolumuza devam edelim::
    
    parola = "xyz05"
    
    soru = input("parolanız: ")
    
    if soru == parola:
        print("doğru parola!")
        
    elif soru != parola:
        print("yanlış parola!")

Burada `soru` değişkeniyle kullanıcıdan alınan verinin, programın başında
tanımladığımız `parola` değişkeninin değerine eşit olup olmadığını sorguluyoruz.
Buna göre, eğer kullanıcıdan gelen veri parolayla eşleşiyorsa (``if soru ==
parola``), kullanıcıyı parolanın doğru olduğu konusunda bilgilendiriyoruz
(``print("doğru parola!")``). Ama eğer kullanıcıdan gelen veri parolayla
eşleşmiyorsa (``elif soru != parola``), o zaman da kullanıcıya parolanın yanlış
olduğunu bildiriyoruz (``print("yanlış parola!")``).

Yukarıdaki örnekte `==` (eşittir) ve `!=` (eşit değildir) işleçlerinin
kullanımını örneklendirdik. Öteki karşılaştırma işleçlerinin de nasıl
kullanıldığını biliyorsunuz. Basit bir örnek verelim::

    sayı = input("sayı: ")

    if int(sayı) <= 100: 
        print("sayı 100 veya 100'den küçük")

    elif int(sayı) >= 100: 
        print("sayı 100 veya 100'den büyük")

Böylece karşılaştırma işleçlerini de incelemiş olduk. O halde gelelim bool
işleçlerine...

Bool İşleçleri
***************

Bu bölümde bool işleçlerinden söz edeceğiz, ancak bool işleçlerine geçmeden önce
biraz bool kavramından bahsetmemiz yerinde olacaktır.

Nedir bu bool denen şey?

Bilgisayar bilimi iki adet değer üzerine kuruludur: `1` ve `0`. Yani sırasıyla
`True` ve `False`. Bilgisayar biliminde herhangi bir şeyin değeri ya `True`, ya
da `False`'tur. İşte bu `True` ve `False` olarak ifade edilen değerlere bool
değerleri adı verilir (George Boole adlı İngiliz matematikçi ve filozofun
adından). Türkçe olarak söylemek gerekirse, `True` değerinin karşılığı `Doğru`,
`False` değerinin karşılığı ise `Yanlış`'tır.

Örneğin::

    >>> a = 1

Burada `a` adlı bir değişken tanımladık. Bu değişkenin değeri `1`. Şimdi bu
değişkenin değerini sorgulayalım::

    >>> a == 1 #a değeri 1'e eşit mi?
    
    True

Gördüğünüz gibi, `a == 1` sorgusu `True` (Doğru) çıktısı veriyor. Çünkü `a`
değişkeninin değeri gerçekten de `1`. Bir de şunu deneyelim::
    
    >>> a == 2
    
    False

Burada da `a` değişkeninin değerinin `2` sayısına eşdeğer olup olmadığını
sorguladık. `a` değişkeninin değeri `2` olmadığı için de Python bize `False`
(Yanlış) çıktısı verdi.

Gördüğünüz gibi, bool işleçleri herhangi bir ifadenin doğruluğunu veya
yanlışlığını sorgulamak için kullanılabiliyor. Buna göre, eğer bir sorgulamanın
sonucu doğru ise `True`, eğer yanlış ise `False` çıktısı alıyoruz.

Bool işleçleri sadece yukarıda verdiğimiz örneklerdeki gibi, salt bir
doğruluk-yanlışlık sorgulamaya yarayan araçlar değildir. Bilgisayar biliminde
her şeyin bir bool değeri vardır. Bununla ilgili genel kuralımız şu: `0` değeri
ve boş veri tipleri `False`'tur. Bunlar dışında kalan her şey ise `True`'dur.

Bu durumu ``bool()`` adlı özel bir fonksiyondan yararlanarak teyit edebiliriz::

    >>> bool(3)
    
    True
    
    >>> bool("elma")
    
    True
    
    >>> bool(" ")
    
    True
    
    >>> bool("     ")
    
    True
    
    >>> bool("fdsdfsdg")
    
    True
    
    >>> bool("0")
    
    True
    
    >>> bool(0)
    
    False
    
    >>> bool("")
    
    False

Gördüğünüz gibi, gerçekten de `0` sayısının ve boş karakter dizilerinin bool
değeri `False`'tur. Geri kalan her şey ise `True`'dur.

.. note:: `0`'ın bir sayı, `"0"`'ın ise bir karakter dizisi olduğunu unutmayın.
 Sayı olan `0`'ın bool değeri `False`'tur, ama karakter dizisi olan `"0"`'ın
 değeri `True`'dur.

Yukarıdaki örneklere göre, içinde herhangi bir değer barındıran karakter
dizileri (`0` hariç) `True` çıktısı veriyor. Burada söylediğimiz şey bütün veri
tipleri için geçerlidir. Eğer herhangi bir veri tipi herhangi bir değer
içermiyorsa o veri tipi `False` çıktısı verir.

Peki bu bilgi bizim ne işimize yarar? Yani mesela boş veri tiplerinin `False`,
içinde bir veri barındıran veri tiplerinin ise `True` olması bizim için neden bu
kadar önemli? Bunu birazdan açıklayacağız. Ama önce isterseniz, bool değerleri
ile ilgili çok önemli bir konuya değinelim.

Belki kendiniz de farketmişsinizdir; bool değerleri Python'da koşul belirten
``if``, ``elif`` ve ``else`` deyimlerinin de temelini oluşturur. Şu örneği ele
alalım mesela::
    
    isim = input("İsminiz: ")
    
    if isim == "Ferhat":
        print("Ne güzel bir isim bu!")
    else:
        print(isim, "ismini pek sevmem!")

Burada ``if isim == "Ferhat"`` dediğimizde, aslında Python'a şu emri vermiş
oluyoruz:

    Eğer ``isim == "Ferhat"`` ifadesi `True` ise...

Bunu teyit etmek için şöyle bir kod yazabilirsiniz::

    isim = input("İsminiz: ")

    print(isim == "Ferhat")

Eğer burada kullanıcı 'Ferhat' ismini girecek olursa programımız `True` çıktısı
verir. Ama eğer kullanıcı başka bir isim girerse bu kez `False` çıktısını
alırız. İşte koşul bildiren deyimler, karar verme görevini, kendilerine verilen
ifadelerin bool değerlerine bakarak yerine getirir. Dolayısıyla yukarıdaki
örneği şu şekilde Türkçeye çevirebiliriz:

    Eğer ``isim == "Ferhat"`` ifadesinin bool değeri `True` ise, `Ne güzel bir
    isim bu!` çıktısı ver! Ama eğer ``isim == "Ferhat"`` ifadesinin bool değeri
    `True` dışında herhangi bir şey ise (yani `False` ise), `... ismini pek
    sevmem!` çıktısı ver!
    
Koşul bildiren deyimlerle bool değerleri arasındaki ilişkiyi daha iyi anlamak
için bir örnek daha verelim:

Hatırlarsanız içi boş veri tiplerinin bool değerinin her zaman `False` olacağını
söylemiştik. Yani::

    >>> a = ""
    
    >>> bool(a)
    
    False

Herhangi bir değere sahip veri tiplerinin bool değeri ise her zaman `True` olur
(`0` hariç)::
    
    >>> a = "gdfg"
    
    >>> bool(a)
    
    True

İçi boş veri tiplerinin bool değerinin her zaman `False` olacağı bilgisini
kullanarak şöyle bir uygulama yazabiliriz::
    
    kullanıcı = input("Kullanıcı adınız: ")
    
    if bool(kullanıcı) == True:
        print("Teşekkürler!")
    else:
        print("Kullanıcı adı alanı boş bırakılamaz!")

Burada şöyle bir emir verdik:

    "Eğer `kullanıcı` değişkeninin bool değeri `True` ise `Teşekkürler!` çıktısı
    ver! Değilse `Kullanıcı adı alanı boş bırakılamaz!` uyarısını göster!
    
Eğer kullanıcı, kullanıcı adına herhangi bir şey yazdıktan sonra `Enter` tuşuna
basarsa `kullanıcı` değişkeni, kullanıcının girdiği değeri gösterecek ve böylece
``bool(kullanıcı)`` komutu `True` çıktısı verecektir. Bu sayede de kodlarımızın
içindeki ``if`` bloğu çalışmaya başlayacaktır.

Ama eğer kullanıcı, kullanıcı adını yazmadan `Enter` tuşuna basarsa, `kullanıcı`
değişkeni boş kalacağı için (yani ``kullanıcı = ""`` gibi bir durum ortaya
çıkacağı için) ``bool(kullanıcı)`` komutu `False` çıktısı verecek ve böylece
``else`` bloğu çalışacaktır.

Yalnız bu noktada şöyle bir uyarı yapalım. Yukarıdaki komutlar sözdizimi
açısından tamamen doğru olsa da, etrafta yukarıdakine benzer bir kullanımı pek
görmezsiniz. Aynı iş için genellikle şöyle bir şeyler yazılır::
    
    kullanıcı = input("Kullanıcı adınız: ")
    
    if kullanıcı:
        print("Teşekkürler!")

Gördüğünüz gibi, ``if bool(kullanıcı) == True:`` kodunu ``if kullanıcı:``
şeklinde kısaltabiliyoruz. Bu ikisi tamamen aynı anlama gelir. Yani ikisi de
'kullanıcı değişkeninin bool değeri `True` ise...' demektir.

Bool kavramına aşinalık kazandığımıza göre şimdi bool işleçlerini incelemeye
başlayabiliriz.

Bool işleçleri, bool değerlerinden birini elde etmemizi sağlayan işleçlerdir. Bu
işleçler şunlardır:

    `and`
        
    `or`
        
    `not`

Eğer mantık dersleri aldıysanız bu işleçler size hiç yabancı gelmeyecektir. Eğer
lisede mantık dersleri almadıysanız veya aldığınız derslerden hiçbir şey
hatırlamıyorsanız, yine de ziyanı yok. Biz burada bu işleçleri bütün
ayrıntılarıyla inceleyeceğiz.

Önce `and` ile başlayalım... 

Türkçe söylemek gerekirse `and` 've' anlamına gelir. Peki bu `and` ne işimize
yarar? Çok basit bir örnek verelim:

Hatırlarsanız geçen bölümde koşullu durumlara örnek verirken şöyle bir durumdan
bahsetmiştik:

    Diyelim ki Google'ın Gmail hizmeti aracılığıyla bir e.posta hesabı aldınız.
    Bu hesaba gireceğiniz zaman Gmail size bir kullanıcı adı ve parola sorar.
    Siz de kendinize ait kullanıcı adını ve parolayı sayfadaki kutucuklara
    yazarsınız. Eğer yazdığınız kullanıcı adı ve parola doğruysa hesabınıza
    erişebilirsiniz. Ama eğer kullanıcı adınız ve parolanız doğru değilse
    hesabınıza erişemezsiniz. Yani e.posta hesabınıza erişmeniz, kullanıcı adı
    ve parolayı doğru girme koşuluna bağlıdır.
    
Burada çok önemli bir nokta var. Kullanıcının Gmail sistemine girebilmesi için
hem kullanıcı adını hem de parolayı doğru yazması gerekiyor. Yani kullanıcı adı
veya paroladan herhangi biri yanlış ise sisteme giriş mümkün olmayacaktır.

Yukarıdaki durumu taklit eden bir programı, şu ana kadar olan bilgilerimizi
kullanarak şöyle yazabiliyoruz::

    kullanıcı_adı = input("Kullanıcı adınız: ")
    parola = input("Parolanız: ")
    
    if kullanıcı_adı == "aliveli":
        if parola == "12345678":
            print("Programa hoşgeldiniz")
        else:
            print("Yanlış kullanıcı adı veya parola!")
            
    else:
        print("Yanlış kullanıcı adı veya parola!")

Burada yeni bir bilgiyle daha karşılaşıyoruz. Gördüğünüz gibi, burada ``if``
deyimlerini iç içe kullandık. Python'da istediğiniz kadar iç içe geçmiş ``if``
deyimi kullanabilirsiniz. Ancak yazdığınız bir programda eğer üçten fazla iç içe
``if`` deyimi kullandıysanız, benimsediğiniz yöntemi yeniden gözden geçirmenizi
tavsiye ederim. Çünkü iç içe geçmiş ``if`` deyimleri bir süre sonra anlaşılması
güç bir kod yapısı ortaya çıkarabilir. Neyse... Biz konumuza dönelim.

Yukarıdaki yazdığımız programda kullanıcının sisteme giriş yapabilmesi için hem
kullanıcı adını hem de parolayı doğru girmesi gerekiyor. Kullanıcı adı ve
paroladan herhangi biri yanlışsa sisteme girişe izin verilmiyor. Ancak
yukarıdaki yöntem dolambaçlıdır. Halbuki aynı işlevi yerine getirmenin,
Python'da çok daha kolay bir yolu var. Bakalım::
    
    kullanıcı_adı = input("Kullanıcı adınız: ")
    parola = input("Parolanız: ")

    if kullanıcı_adı == "aliveli" and parola == "12345678":
        print("Programa hoşgeldiniz")
        
    else:
        print("Yanlış kullanıcı adı veya parola!") 

Burada `and` işlecini nasıl kullandığımızı görüyorsunuz. Bu işleci kullanarak
iki farklı ifadeyi birbirine bağladık. Böylece kullanıcının sisteme girişini hem
kullanıcı adının hem de parolanın doğru olması koşuluna dayandırdık.

Peki `and` işlecinin çalışma mantığı nedir? Dediğim gibi, `and` Türkçede 've'
anlamına geliyor. Bu işleci daha iyi anlayabilmek için şu cümleler arasındaki
farkı düşünün:

    a. Toplantıya Ali ve Veli katılacak.
    
    b. Toplantıya Ali veya Veli katılacak. 

İlk cümlede 've' bağlacı kullanıldığı için, bu cümlenin gereğinin yerine
getirilebilmesi, hem Ali'nin hem de Veli'nin toplantıya katılmasına bağlıdır.
Sadece Ali veya sadece Veli'nin toplantıya katılması durumunda bu cümlenin
gereği yerine getirilememiş olacaktır.

İkinci cümlede ise toplantıya Ali ve Veli'den herhangi birisinin katılması
yeterlidir. Toplantıya sadece Ali'nin katılması, sadece Veli'nin katılması veya
her ikisinin birden katılması, bu cümlenin gereğinin yerine getirilebilmesi
açısından yeterlidir.

İşte Python'daki `and` işleci de aynı bu şekilde işler. Şu örneklere bir
bakalım::

    >>> a = 23
    >>> b = 10
    >>> a == 23
    
    True
    
    >>> b == 10
    
    True
    
    >>> a == 23 and b == 10
    
    True

Burada değeri `23` olan bir adet `a` değişkeni ve değeri `10` olan bir adet `b`
değişkeni tanımladık. Daha sonra bu iki değişkenin değerini tek tek sorguladık
ve bunların gerçekten de sırasıyla 23 ve 10 sayısına eşit olduğunu gördük. Son
olarak da bunları `and` işleci ile birbirine bağlayarak sorguladık. `a`
değişkeninin değeri 23, `b` değişkeninin değeri de 10 olduğu için, yani `and`
ile bağlanan her iki önerme de `True` çıktısı verdiği için ``a == 23 and b ==
10`` ifadesi `True` değeri verdi.

Bir de şuna bakalım::

    >>> a = 23
    >>> b = 10
    >>> a == 23
    
    True
    
    >>> b == 54
    
    False
    
    >>> a == 23 and b == 54
    
    False

Burada ise `a` değişkenin değeri `23`'tür. Dolayısıyla ``a == 23`` ifadesi
`True` çıktısı verir. Ancak `b` değişkeninin değeri `54` değildir. O yüzden de
``b == 54`` komutu `False` çıktısı verir. Gördüğünüz gibi, `and` işleci ile
bağlanan önermelerden herhangi biri `False` olduğunda çıktımız da `False`
oluyor. Unutmayın: `and` işlecinin `True` çıktısı verebilmesi için bu işleç
tarafından bağlanan her iki önermenin de `True` olması gerekir. Eğer
önermelerden biri bile `True` değilse çıktı da `True` olmayacaktır.

Tahmin edebileceğiniz gibi, `and` işleci en yaygın ``if`` deyimleriyle birlikte
kullanılır. Mesela yukarıda kullanıcıdan kullanıcı adı ve parola alırken de bu
`and` işlecinden yararlanmıştık.

Gelelim `or` işlecine... 

Tıpkı `and` gibi bir bool işleci olan `or`'un Türkçede karşılığı 'veya'dır.
Yukarıda 'Toplantıya Ali veya Veli katılacak.' cümlesini tartışırken aslında bu
`or` kelimesinin anlamını açıklamıştık. Hatırlarsanız `and` işlecinin `True`
çıktısı verebilmesi için bu işleçle bağlanan bütün önermelerin `True` değerine
sahip olması gerekiyordu. `or` işlecinin `True` çıktısı verebilmesi için ise
`or` işleciyle bağlanan önermelerden herhangi birinin `True` çıktısı vermesi
yeterli olacaktır. Söylediğimiz bu şeyleri birkaç örnek üzerinde
somutlaştıralım::
    
    >>> a = 23
    >>> b = 10
    >>> a == 23
    
    True
    
    >>> b == 10
    
    True
    
    >>> a == 11
    
    False
    
    >>> a == 11 or b == 10
    
    True
    
Gördüğünüz gibi, ``a == 11`` ifadesinin bool değeri `False` olduğu halde, ``b ==
10`` ifadesinin bool değeri `True` olduğu için ``a == 11 or b == 10`` ifadesi
`True` değerini veriyor.

`and` ve `or` işleçlerini öğrendiğimize göre, bir sınavdan alınan notların harf
karşılıklarını gösteren bir uygulama yazabiliriz::
    
    x = int(input("Notunuz: "))

    if x > 100 or x < 0:
        print("Böyle bir not yok")

    elif x >= 90 and x <= 100:
        print("A aldınız.")

    elif x >= 80 and x <= 89:
        print("B aldınız.")

    elif x >= 70 and x <= 79:
        print("C aldınız.")

    elif x >= 60 and x <= 69:
        print("D aldınız.")

    elif x >= 0 and x <= 59:
        print("F aldınız.")

Bu programda eğer kullanıcı `100`'den büyük ya da `0`'dan küçük bir sayı girerse
`Böyle bir not yok` uyarısı alacaktır. 0-100 arası notlarda ise, her bir not
aralığına karşılık gelen harf görüntülecektir. Eğer isterseniz yukarıdaki
kodları şu şekilde de kısaltabilirsiniz::
    
    x = int(input("Notunuz: "))

    if x > 100 or x < 0:
        print("Böyle bir not yok")

    elif x >= 90 <= 100:
        print("A aldınız.")

    elif x >= 80 <= 89:
        print("B aldınız.")

    elif x >= 70 <= 79:
        print("C aldınız.")

    elif x >= 60 <= 69:
        print("D aldınız.")

    elif x >= 0 <= 59:
        print("F aldınız.")

Gördüğünüz gibi, ``and x`` kısımlarını çıkardığımızda da bir önceki kodlarla
aynı anlamı yakalayabiliyoruz.

Hatta yukarıdaki kodları şöyle de yazabilirsiniz::

    x = int(input("Notunuz: "))

    if x > 100 or x < 0:
        print("Böyle bir not yok")

    #90 sayısı x'ten küçük veya x'e eşit, 
    #x sayısı 100'den küçük veya 100'e eşit ise,
    #Yani x, 90 ile 100 arasında bir sayı ise 
    elif 90 <= x <= 100: 
        print("A aldınız.")

    #80 sayısı x'ten küçük veya x'e eşit, 
    #x sayısı 89'dan küçük veya 89'a eşit ise,
    #Yani x, 80 ile 89 arasında bir sayı ise 
    elif 80 <= x <= 89:
        print("B aldınız.")

    elif 70 <= x <= 79:
        print("C aldınız.")

    elif 60 <= x <= 69:
        print("D aldınız.")

    elif 0 <= x <= 59:
        print("F aldınız.")

Bu kodlar bir öncekiyle aynı işi yapar. Yorumlardan da göreceğiniz gibi, bu iki
kod arasında sadece mantık farkı var.

Son bool işlecimiz `not`. Bu kelimenin İngilizce'deki anlamı 'değil'dir. Bu
işleci şöyle kullanıyoruz::
    
    >>> a = 23
    >>> not a
    
    False
    
    >>> a = ""
    >>> not a
    
    True

Bu işleç, özellikle kullanıcı tarafından bir değişkene veri girilip
girilmediğini denetlemek için kullanılabilir. Örneğin::
    
    parola = input("parola: ")

    if not parola:
        print("Parola boş bırakılamaz!")

Eğer kullanıcı herhangi bir parola belirlemeden doğrudan `Enter` tuşuna basacak
olursa `parola` değişkeninin değeri boş bir karakter dizisi olacaktır. Yani
``parola = ""``. Boş veri tiplerinin bool değerinin `False` olacağını biliyoruz.
Dolayısıyla, yukarıdaki gibi bir örnekte, kullanıcı parolayı boş geçtiğinde
``not parola`` kodu `True` verecek ve böylece ekrana `"Parola boş bırakılamaz!"`
karakter dizisi yazdırılacaktır. Eğer yukarıdaki örneğin mantığını kavramakta
zorluk çekiyorsanız şu örnekleri incelemenizi öneririm::
    
    >>> parola = ""
    >>> bool(parola)
    
    False
    
    >>> bool(not parola)
    
    True
    
    >>> parola = "1243"
    >>> bool(parola)
    
    True
    
    >>> bool(not parola)
    
    False

Aslında yukarıdaki örneklerde şuna benzer sorular sormuş gibi oluyoruz::

    >>> parola = ""
    >>> bool(parola) #parola boş bırakılmamış, değil mi?
    
    >>> False #Hayır, parola boş bırakılmış.
    
    >>> bool(not parola) #parola boş bırakılmış, değil mi?
    
    >>> True #Evet, parola boş bırakılmış

Kendi kendinize pratik yaparak bu işlecin görevini daha iyi anlayabilirsiniz.

Böylece kısmen çetrefilli bir konu olan bool işleçlerini de geride bırakmış
olduk. Sırada değer atama işleçleri var.

Değer Atama İşleçleri
*********************

Bu noktaya kadar yaptığımız çalışmalarda sadece tek bir değer atama işleci
gördük. Bu işleç `=` işlecidir. Adından da anlaşılacağı gibi, bu işlecin görevi
bir değişkene değer atamaktır. Mesela::
    
    >>> a = 23

Burada `=` işleci `a` değişkenine `23` değerini atama işlevi görüyor. 

Python'daki tek değer atama işleci elbette `=` değildir. Bunun dışında başka
değer atama işleçleri de bulunur. Tek tek inceleyelim:

**+= işleci**

Bu işlecin ne işe yaradığını anlamak için şöyle bir örnek düşünün::

    >>> a = 23

`a` değerine mesela `5` ekleyip bu değeri `28`'e eşitlemek için ne yapmamız
lazım? Tabii ki şunu:

::

    >>> a = a + 5
    >>> print(a)
    
    28

Burada yaptığımız şey çok basit: `a` değişkeninin taşıdığı değere `5` ilave
ediyoruz ve daha sonra bu değeri tekrar `a` değişkenine atıyoruz. Aynı işlemi
çok daha kolay bir şekilde de yapabiliriz::
    
    >>> a += 5
    >>> print(a)
    
    28

Bu kod, yukarıdakiyle tamamen aynı anlama gelir. Ama bir önceki koda göre çok
daha verimlidir. Çünkü ``a += 5`` kodunda Python `a` değişkeninin değerini
sadece bir kez kontrol ettiği için, işlemi ``a = a + 5`` koduna göre daha hızlı
yapacaktır.

**-= işleci**

Bir önceki `+=` işleci toplama işlemi yapıp, ortaya çıkan değeri tekrar aynı
değişkene atıyordu. `-=` işleci de buna benzer bir işlem gerçekleştirir::
    
    >>> a = 23
    >>> a -= 5
    >>> print(a)
    
    18

Yukarıdaki kullanım şununla tamamen aynıdır::

    >>> a = 23
    >>> a = a - 5
    >>> print(a)
    
    18

Ancak tıpkı `+=` işlecinde olduğu gibi, `-=` işleci de alternatifine göre daha
hızlı çalışan bir araçtır.

**/= işleci**

Bu işlecin çalışma mantığı da yukarıdaki işleçlerle aynıdır::

    >>> a = 30
    >>> a /= 3
    >>> print(a)
    
    10

Yukarıdaki işlem de şununla tamamen aynıdır::

    >>> a = 30
    >>> a = a / 3
    >>> print(a)
    
    10

**\*= işleci**

Bu da ötekiler gibi, çarpma işlemi yapıp, bu işlemin sonucunu aynı değişkene atar::

    >>> a = 20
    >>> a *= 2
    >>> print(a)
    
    40

Bu işlecin eşdeğeri de şudur::

    >>> a = 20
    >>> a = a * 2
    >>> print(a)
    
    40

**%= işleci**

Bu işlecimiz ise bölme işleminden kalan sayıyı aynı değişkene atar::

    >>> a = 40
    >>> a %= 3
    >>> print(a)
    
    1

Bu işleç de şuna eşdeğerdir::

    >>> a = 40
    >>> a = a % 3
    >>> print(a)
    
    1

**\**= işleci**

Bu işlecin ne yaptığını tahmin etmek zor değil. Bu işlecimiz, bir sayının
kuvvetini hesapladıktan sonra çıkan değeri aynı değişkene atıyor::
    
    >>> a = 12
    >>> a **= 2
    >>> print(a)
    
    144

Eşdeğeri::

    >>> a = 12
    >>> a = a ** 2
    >>> print(a)
    
    144

**//= işleci**

Değer atama işleçlerinin sonuncusu olan `//=` işlecinin görevi ise taban bölme
işleminin sonucunu aynı değişkene atamaktır::
    
    >>> a = 5
    >>> a //= 2
    >>> print(a)
    
    2

Eşdeğeri::

    >>> a = 5
    >>> a = a // 2
    >>> print(a)
    
    2

Bu işleçler arasından, özellikle `+=` ve `-=` işleçleri işinize bir hayli yarayacak. 

Bu arada eğer bu işleçleri kullanırken mesela `+=` mi yoksa `=+` mı yazacağınızı
karıştırıyorsanız, şöyle düşünebilirsiniz::
    
    >>> a = 5
    >>> a += 5
    >>> print(a)
    
    10

Burada, değeri `5` olan bir `a` değişkenine `5` daha ekleyip, çıkan sonucu
tekrar `a` değişkenine atadık. Böylece değeri `10` olan bir `a` değişkeni elde
ettik. `+=` işlecinin doğru kullanımı yukarıdaki gibidir. Bir de yukarıdaki
örneği şöyle yazmayı deneyelim::
    
    >>> a = 5
    >>> a =+ 5
    >>> print(a)
    
    5

Burada `+` işleci ile `=` işlecinin yerini değiştirdik. 

``a =+ 5`` satırına dikkatlice bakın. Aslında burada yaptığımız şeyin ``a = +5``
işlemi olduğunu, yani `a` değişkenine `+5` gibi bir değer verdiğimizi
göreceksiniz. Durum şu örnekte daha net görünecektir::
    
    >>> a = 5
    >>> a =- 5
    >>> print(a)
    >>> -5

Gördüğünüz gibi, ``a =- 5`` yazdığımızda, aslında yaptığımız şey `a` değişkenine
`-5` değerini vermekten ibarettir. Yani ``a = -5``.

Aitlik İşleçleri
****************

Aitlik işleçleri, bir karakter dizisi ya da sayının, herhangi bir veri tipi
içinde bulunup bulunmadığını sorgulamamızı sağlayan işleçlerdir.

Python'da bir tane aitlik işleci bulunur. Bu işleç de `in` işlecidir. Bu işleci
şöyle kullanıyoruz::

    >>> a = "abcd"
    >>> "a" in a
    
    True
    
    >>> "f" in a
    
    False

Gördüğünüz gibi, `in` adlı bu işleç, bir öğenin, veri tipi içinde bulunup
bulunmadığını sorguluyor. Eğer bahsedilen öğe, veri tipi içinde geçiyorsa `True`
çıktısı, eğer geçmiyorsa `False` çıktısı alıyoruz.

Henüz bu `in` işlecini verimli bir şekilde kullanmamızı sağlayacak araçlardan
yoksunuz. Ancak birkaç sayfa sonra öğreneceğimiz yeni araçlarla birlikte bu
işleci çok daha düzgün ve verimli bir şekilde kullanabilecek duruma geleceğiz.

Kimlik İşleçleri
****************

Python'da her şeyin (ya da başka bir deyişle her nesnenin) bir kimlik numarası
(*identity*) vardır. Kabaca söylemek gerekirse, bu kimlik numarası denen şey
esasında o nesnenin bellekteki adresini gösterir.

Peki bir nesnenin kimlik numarasına nasıl ulaşırız?

Python'da bu işi yapmamızı sağlayacak ``id()`` adlı bir fonksiyon bulunur
(İngilizcedeki *identity* (kimlik) kelimesinin kısaltması). Şimdi bir örnek
üzerinde bu ``id()`` fonksiyonunu nasıl kullanacağımıza bakalım::
    
    >>> a = 100
    >>> id(a)

    137990748

Çıktıda gördüğümüz `137990748` sayısı `a` değişkeninin tuttuğu `100` sayısının
kimlik numarasını gösteriyor.

Bir de şu örneklere bakalım::

    >>> a = 50
    >>> id(a)
    
    505494576
    
    >>> kardiz = "Elveda Zalim Dünya!"
    >>> id(kardiz)
    
    14461728

Gördüğünüz gibi, Python'daki her nesnenin kimliği eşşiz, tek ve benzersizdir.

Yukarıda verdiğimiz ilk örnekte bir `a` değişkeni tanımlayıp bunun değerini
`100` olarak belirlemiş ve ``id(a)`` komutuyla da bu nesnenin kimlik numarasına
ulaşmıştık. Yani::
    
    >>> a = 100
    >>> id(a)
    137990748

Bir de şu örneğe bakalım::

    >>> b = 100
    >>> id(b)

    137990748

Gördüğünüz gibi, Python `a` ve `b` değişkenlerinin değeri için aynı kimlik
numarasını gösterdi. Bu demek oluyor ki, Python iki adet `100` sayısı için
bellekte iki farklı nesne oluşturmuyor. İlk kullanımda önbelleğine aldığı
sayıyı, ikinci kez ihtiyaç olduğunda bellekten alıp kullanıyor. Bu tür bir
önbellekleme mekanizmasının gerekçesi performansı artırmaktır.

Ama bir de şu örneklere bakalım::

    >>> a = 1000
    >>> id(a)
    
    15163440
    
    >>> b = 1000
    >>> id(b)
    
    14447040
    
    >>> id(1000)
    
    15163632

Bu defa Python `a` değişkeninin tuttuğu `1000` sayısı, `b` değişkeninin tuttuğu
1000 sayısı ve tek başına yazdığımız `1000` sayısı için farklı kimlik numaraları
gösterdi. Bu demek oluyor ki, Python `a` değişkeninin tuttuğu `1000` sayısı
için, `b` değişkeninin tuttuğu `1000` sayısı için ve doğrudan girdiğimiz `1000`
sayısı için bellekte üç farklı nesne oluşturuyor. Yani bu üç adet `1000` sayısı
Python açısından birbirinden farklı...

Yukarıdaki durumu görebileceğimiz başka bir yöntem de Python'daki `is` adlı
kimlik işlecini kullanmaktır. Deneyelim::

    >>> a is 1000

    False
    
    >>> b is 1000
    
    False

Gördüğünüz gibi, Python `False` (Yanlış) çıktısını suratımıza bir tokat gibi
çarptı... Peki bu ne anlama geliyor?

Bu şu anlama geliyor: Demek ki görünüşte aynı olan iki nesne aslında birbirinin
aynı olmayabiliyor. Bunun neden bu kadar önemli olduğunu ilerleyen derslerde çok
daha iyi anlayacağız.

Yukarıdaki durumun bir başka yansıması daha vardır. Özellikle Python'a yeni
başlayıp da bu dilde yer alan `is` işlecini öğrenenler, bu işlecin `==`
işleciyle aynı işleve sahip olduğu yanılgısına kapılabiliyor ve `is` işlecini
kullanarak iki nesne arasında karşılaştırma işlemi yapmaya kalkışabiliyor.

Ancak Python'da `is` işlecini kullanarak iki nesne arasında karşılaştırma yapmak
güvenli değildir. Yani `is` ve `==` işleçleri birbirleriyle aynı işlevi görmez.
Bu iki işleç nesnelerin farklı yönlerini sorgular: `is` işleci nesnelerin
kimliklerine bakıp o nesnelerin aynı nesneler olup olmadığını kontrol ederken,
`==` işleci nesnelerin içeriğine bakarak o nesnelerin aynı değere sahip olup
olmadıklarını sorgular. Bu iki tanım arasındaki ince farka dikkat edin.

Yani::

    >>> a is 1000

    False

Ama::

    >>> a == 1000

    True

Burada `is` işleci `a` değişkeninin tuttuğu veri ile `1000` sayısının aynı
kimlik numarasına sahip olup olmadığını sorgularken, `==` işleci `a`
değişkeninin tuttuğu verinin `1000` olup olmadığını denetliyor. Yani `is`
işlecinin yaptığı şey kabaca şu oluyor::
    
    >>> id(a) == id(1000)

    False

Şimdiye kadar denediğimiz örnekler hep sayıydı. Şimdi isterseniz bir de karakter
dizilerinin durumuna bakalım::
    
    >>> a = "python"
    >>> a is "python"

    True

Burada `True` çıktısını aldık. Bir de `==` işleci ile bir karşılaştırma
yapalım::
    
    >>> a == "python"

    True

Bu da normal olarak `True` çıktısı veriyor. Ama şu örneğe bakarsak::

    >>> a = "python güçlü ve kolay bir programlama dilidir"
    >>> a is "python güçlü ve kolay bir programlama dilidir"

    False

Ama::

    >>> a == "python güçlü ve kolay bir programlama dilidir"

    True

`is` ve `==` işleçlerinin nasıl da farklı sonuçlar verdiğini görüyorsunuz. Çünkü
bunlardan biri nesnelerin kimliğini sorgularken, öbürü nesnelerin içeriğini
sorguluyor. Ayrıca burada dikkatimizi çekmesi gereken başka bir nokta da
`"python"` karakter dizisinin önbelleğe alınıp gerektiğinde tekrar tekrar
kullanılıyorken, `"python güçlü ve kolay bir programlama dilidir"` karakter
dizisinin ise önbelleğe alınmıyor olmasıdır. Aynı karakter dizisinin tekrar
kullanılması gerektiğinde Python bunun için bellekte yeni bir nesne daha
oluşturuyor.

Peki neden Python, örneğin, `100` sayısını ve `"python"` karakter dizisini
önbelleklerken `1000` sayısını ve `"python güçlü ve kolay bir programlama
dilidir"` karakter dizisini önbelleğe almıyor. Sebebi şu: Python kendi iç
mekanizmasının işleyişi gereğince 'ufak' nesneleri önbelleğe alırken 'büyük'
nesneler için her defasında yeni bir depolama işlemi yapıyor. Peki ufak ve büyük
kavramlarının ölçütü nedir? İsterseniz Python açısından ufak kavramının
sınırının ne olabileceğini şöyle bir kod yardımıyla sorgulayabiliriz::
    
    >>> for k in range(-1000, 1000):
    ...     for v in range(-1000, 1000):
    ...         if k is v:       
    ...             print(k)  

.. note:: Burada henüz öğrenmediğimiz şeyler var. Bunları birkaç bölüm sonra
          ayrıntılı bir şekilde inceleyeceğiz.

Bu kod `-1000` ve `1000` aralığındaki iki sayı grubunu karşılaştırıp, kimlikleri
aynı olan sayıları ekrana döküyor. Yani bir bakıma Python'un hangi sayıya kadar
önbellekleme yaptığını gösteriyor. Buna göre `-5` ile `257` arasında kalan
sayılar Python tarafından ufak olarak değerlendiriliyor ve önbelleğe alınıyor.
Bu aralığın dışında kalan sayılar için ise bellekte her defasında ayrı bir nesne
oluşturuluyor.

Burada aldığımız sonuca göre şöyle bir denetleme işlemi yapalım::

    >>> a = 256
    >>> a is 256

    True
    
    >>> a = 257
    >>> a is 257

    False
    
    >>> a = -5
    >>> a is -5
    
    True
    
    >>> a = -6
    >>> a is -6
    
    False

Böylece Python'daki kimlik işleçlerini de incelemiş olduk. Belki programcılık
maceranız boyunca ``id()`` fonksiyonunu hiç kullanmayacaksınız, ancak bu
fonksiyonun arkasındaki mantığı anlamak, Python'ın kimi yerlerde alttan alta
neler çevirdiğini çok daha kolay kavramanızı sağlayacaktır.

.. note:: http://forum.ceviz.net/showthread.php?t=87565 adresindeki tartışmaya
 bakınız.

Böylece Python'daki bütün işleçleri ayrıntılı bir şekilde incelemiş olduk.
Dilerseniz şimdi bu konuyla ilgili birkaç uygulama örneği yapalım.

Uygulama Örnekleri
******************

Basit Bir Hesap Makinesi
=========================

Şu ana kadar Python'da pek çok şey öğrendik. Bu öğrendiğimiz şeylerle artık
kısmen yararlı bazı programlar yazabiliriz. Elbette henüz yazacağımız programlar
pek yetenekli olamayacak olsa da, en azından bize öğrendiklerimizle pratik yapma
imkanı sağlayacak. Bu bölümde, ``if``, ``elif``, ``else`` yapılarını ve
öğrendiğimiz temel aritmetik işleçleri kullanarak çok basit bir hesap makinesi
yapmayı deneyeceğiz. Bu arada, bu derste yeni şeyler öğrenerek ufkumuzu ve
bilgimizi genişletmeyi de ihmal etmeyeceğiz.

İsterseniz önce kullanıcıya bazı seçenekler sunarak işe başlayalım::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) kare kök hesapla
    """

    print(giriş)

Burada kullanıcıya bazı seçenekler sunduk. Bu seçenekleri ekrana yazdırmak için
üç tırnak işaretlerinden yararlandığımıza dikkat edin. Birden fazla satıra
yayılmış bu tür ifadeleri en kolay üç tırnak işaretleri yardımıyla
yazdırabileceğimizi biliyorsunuz artık.

Biz burada bütün seçenekleri tek bir değişken içine yerleştirdik. Esasında her
bir seçenek için ayrı bir değişken tanımlamak da mümkündür. Yani aslında
yukarıdaki kodları şöyle de yazabiliriz::
    
    seçenek1 = "(1) topla"
    seçenek2 = "(2) çıkar"
    seçenek3 = "(3) çarp"
    seçenek4 = "(4) böl"
    seçenek5 = "(5) karesini hesapla"
    seçenek6 = "(6) karekök hesapla"

    print(seçenek1, seçenek2, seçenek3, seçenek4, seçenek5)

Yalnız burada dikkat ederseniz, seçenekler hep yan yana diziliyor. Eğer
programınızda yukarıdaki şekli kullanmak isterseniz, bu seçeneklerin yan yana
değil de, alt alta görünmesini sağlamak için, önceki derslerimizde öğrendiğimiz
`sep` parametresini kullanabilirsiniz::
    
    seçenek1 = "(1) topla"
    seçenek2 = "(2) çıkar"
    seçenek3 = "(3) çarp"
    seçenek4 = "(4) böl"
    seçenek5 = "(5) karesini hesapla"
    seçenek6 = "(6) karekök hesapla"

    print(seçenek1, seçenek2, seçenek3, seçenek4, seçenek5, seçenek6, sep="\n")

Burada `sep` parametresinin değeri olarak `\\n` kaçış dizisini belirlediğimize
dikkat edin. `\\n` kaçış dizisinin ne işe yaradığını hatırlıyorsunuz. Bu dizi,
satır başına geçmemizi sağlıyordu. Burada, ayraç olarak satır başı kaçış
dizisini belirlediğimiz için her bir seçenek yan yana değil, alt alta
görünecektir. Elbette `sep` parametresi için istediğiniz değeri
belirleyebilirsiniz. Mesela her bir seçeneği satır başı işaretiyle ayırmak
yerine, çift tire gibi bir işaretle ayırmayı da tercih edebilirsiniz::

    print(seçenek1, seçenek2, seçenek3, seçenek4, seçenek5, sep="--")

Programınızda nasıl bir giriş paragrafı belirleyeceğiniz konusunda özgürsünüz.
Gelin isterseniz biz birinci şekille yolumuza devam edelim::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

Burada `giriş` adlı bir değişken oluşturduk. Bu değişkenin içinde barındırdığı
değeri kullanıcıların görebilmesi için ``print()`` fonksiyonu yardımıyla bu
değişkeni ekrana yazdırıyoruz. Devam edelim::

    soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

Bu kod yardımıyla kullanıcıya bir soru soruyoruz. Kullanıcıdan yapmasını
istediğimiz şey, yukarıda belirlediğimiz giriş seçenekleri içinden bir sayı
seçmesi. Kullanıcı `1`, `2`, `3`, `4`, `5` veya `6` seçeneklerinden herhangi
birini seçebilir. Kullanıcıyı, seçtiği numaranın karşısında yazan işleme
yönlendireceğiz. Yani mesela eğer kullanıcı klavyedeki `1` tuşuna basarsa hesap
makinemiz toplama işlemi yapacaktır. `2` tuşu ise kullanıcıyı çıkarma işlemine
yönlendirir...

``input()`` fonksiyonunu işlediğimiz bölümde, bu fonksiyonun değer olarak her
zaman bir karakter dizisi (*string*) verdiğini söylemiştik. Yukarıdaki kodun
çıktısı da doğal olarak bir karakter dizisi olacaktır. Bizim şu aşamada
kullanıcıdan karakter dizisi almamızın bir sakıncası yok. Çünkü kullanıcının
gireceği `1`, `2`, `3`, `4`, `5` veya `6` değerleriyle herhangi bir aritmetik
işlem yapmayacağız. Kullanıcının gireceği bu değerler, yalnızca bize onun hangi
işlemi yapmak istediğini belirtecek. Dolayısıyla ``input()`` fonksiyonunu
yukarıdaki şekilde kullanıyoruz.

İsterseniz şimdiye kadar gördüğümüz kısma topluca bakalım::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

    soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

Bu kodları çalıştırdığımızda, ekranda giriş paragrafımız görünecek ve
kullanıcıya, yapmak istediği işlemin ne olduğu sorulacaktır. Henüz kodlarımız
eksik olduğu için, kullanıcı hangi sayıyı girerse girsin, programımız hiç bir iş
yapmadan kapanacaktır. O halde yolumuza devam edelim::
    
	if soru == "1":

Böylece ilk ``if`` deyimimizi tanımlamış olduk. Buradaki yazım şekline çok
dikkat edin. Bu kodlarla Python'a şu emri vermiş oluyoruz:

	Eğer `soru` adlı değişkenin değeri `1` ise, yani eğer kullanıcı klavyede `1`
	tuşuna basarsa...
	
``if`` deyimlerinin en sonuna `:` işaretini koymayı unutmuyoruz. Python'a yeni
başlayanların en çok yaptığı hatalardan birisi, sondaki bu `:` işaretini koymayı
unutmalarıdır. Bu işaret bize çok ufak bir ayrıntıymış gibi görünse de Python
için manevi değeri çok büyüktür! Python'un bize öfkeli mesajlar göstermesini
istemiyorsak bu işareti koymayı unutmayacağız. Bu arada, burada `==` işaretini
kullandığımıza da dikkat edin. Bunun ne anlama geldiğini önceki derslerimizde
öğrenmiştik. Bu işaret, iki şeyin aynı değere sahip olup olmadığını
sorgulamamızı sağlıyor. Biz burada `soru` adlı değişkenin değerinin `1` olup
olmadığını sorguladık. `soru` değişkeninin değeri kullanıcı tarafından
belirleneceği için henüz bu değişkenin değerinin ne olduğunu bilmiyoruz. Bizim
programımızda kullanıcı klavyeden `1`, `2`, `3`, `4`, `5` veya `6` değerlerinden
herhangi birini seçebilir. Biz yukarıdaki kod yardımıyla, eğer kullanıcı
klavyede `1` tuşuna basarsa ne yapılacağını belirleyeceğiz. O halde devam
edelim::
    
	if soru == "1":
	    sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
	    sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
	    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

Böylece ilk ``if`` bloğumuzu tanımlamış olduk. 

.. highlight:: none

``if`` deyimimizi yazdıktan sonra ne yaptığımız çok önemli. Buradaki
girintileri, programımız güzel görünsün diye yapmıyoruz. Bu girintilerin Python
için bir anlamı var. Eğer bu girintileri vermezsek programımız çalışmayacaktır.
Eğer Python kodlarına duyarlı bir metin düzenleyici kullanıyorsanız, `:`
işaretini koyup `Enter` tuşuna bastıktan sonra otomatik olarak girinti
verilecektir. Eğer kullandığınız metin düzenleyici size böyle bir kolaylık
sunmuyorsa `Enter` tuşuna bastıktan sonra klavyedeki boşluk (`SPACE`) tuşunu
kullanarak dört vuruşluk bir girinti oluşturabilirsiniz. Bu girintiler, ilk
satırda belirlediğimiz ``if`` deyimiyle gösterilecek işlemlere işaret ediyor.
Dolayısıyla burada yazılan kodları Pythoncadan Türkçeye çevirecek olursak şöyle
bir şey elde ederiz::
    
	eğer sorunun değeri '1' ise:
	    Toplama işlemi için ilk sayı girilsin. Bu değere 'sayı1' diyelim.
	    Sonra ikinci sayı girilsin. Bu değere de 'sayı2' diyelim.
	    En son, 'sayı1', '+' işleci, 'sayı2', '=' işleci ve 'sayı1 + sayı2' 
	    ekrana yazdırılsın...

.. highlight:: py3

Gelin isterseniz buraya kadar olan bölümü yine topluca görelim::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

    soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

    if soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

Bu kodları çalıştırıp, klavyede `1` tuşuna bastığımızda, bizden bir sayı
girmemiz istenecektir. İlk sayımızı girdikten sonra bize tekrar bir sayı
girmemiz söylenecek. Bu emre de uyup `Enter` tuşuna basınca, girdiğimiz bu iki
sayının toplandığını göreceğiz. Fena sayılmaz, değil mi?

Şimdi programımızın geri kalan kısmını yazıyoruz. İşin temelini kavradığımıza
göre birden fazla kod bloğunu aynı anda yazabiliriz::

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

Bunlarla birlikte kodlarımızın büyük bölümünü tamamlamış oluyoruz. Bu bölümdeki
tek fark, ilk ``if`` bloğunun aksine, burada ``elif`` bloklarını kullanmış
olmamız. Eğer burada bütün blokları ``if`` kullanarak yazarsanız, biraz sonra
kullanacağımız ``else`` bloğu her koşulda çalışacağı için beklentinizin dışında
sonuçlar elde edersiniz.

Yukarıdaki kodlarda az da olsa farklılık gösteren tek yer son iki ``elif``
bloğumuz. Esasında buradaki fark da pek büyük bir fark sayılmaz. Neticede tek
bir sayının karesini ve karekökünü hesaplayacağımız için, kullanıcıdan yalnızca
tek bir giriş istiyoruz.

Şimdi de son bloğumuzu yazalım. Az evvel çıtlattığımız gibi, bu son blok bir
``else`` bloğu olacak::

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

Çok basit bir ``else`` bloğu ile işimizi bitirdik. Bu bloğun ne işe yaradığını
biliyorsunuz:

    Eğer kullanıcının girdiği değer yukarıdaki bloklardan hiç birine uymuyorsa
    bu `else` bloğunu işlet!
    
gibi bir emir vermiş oluyoruz bu ``else`` bloğu yardımıyla. Mesela kullanıcımız
`1`, `2`, `3`, `4`, `5` veya `6` seçeneklerini girmek yerine `7` yazarsa, bu
blok işletilecek.

Gelin isterseniz son kez kodlarımızı topluca bir görelim::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

    soru = input("Yapmak istediğiniz işlemin numarasını girin: ")

    if soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

    else:
        print("Yanlış giriş.") 
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

Genel olarak baktığımızda, bütün programın aslında basit bir 'if, elif, else'
yapısından ibaret olduğunu görüyoruz. Ayrıca bu kodlardaki simetriye de
dikkatinizi çekmek isterim. Gördüğünüz gibi her 'paragraf' bir ``if``, ``elif``
veya ``else`` bloğundan oluşuyor ve her blok kendi içinde girintili bir yapı
sergiliyor. Temel olarak şöyle bir şeyle karşı karşıyayız::
    
	Eğer böyle bir durum varsa:
	    şöyle bir işlem yap

	Yok eğer şöyle bir durum varsa:
	    böyle bir işlem yap

	Eğer bambaşka bir durum varsa:
	    şöyle bir şey yap

Böylelikle şirin bir hesap makinesine sahip olmuş olduk! Hesap makinemiz pek
yetenekli değil, ama olsun... Henüz bildiklerimiz bunu yapmamıza müsaade ediyor.
Yine de başlangıçtan bu noktaya kadar epey yol katettiğimizi görüyorsunuz.

Şimdi bu programı çalıştırın ve neler yapabildiğine göz atın. Bu arada kodları
da iyice inceleyin. Programı yeterince anladıktan sonra, program üzerinde
kendinize göre bazı değişiklikler yapın, yeni özellikler ekleyin.
Eksikliklerini, zayıf yönlerini bulmaya çalışın. Böylece bu dersten azami
faydayı sağlamış olacaksınız.

Sürüme Göre İşlem Yapan Program
================================
    
Bildiğiniz gibi, şu anda piyasada iki farklı Python serisi bulunuyor: Python2 ve
Python3. Daha önce de söylediğimiz gibi, Python'ın 2.x serisi ile çalışan bir
program Python'ın 3.x serisi ile muhtemelen çalışmayacaktır. Aynı şekilde bunun
tersi de geçerlidir. Yani 3.x ile çalışan bir program 2.x ile büyük ihtimalle
çalışmayacaktır. 

Bu durum, yazdığınız programların farklı Python sürümleri ile çalıştırılma
ihtimaline karşı bazı önlemler almanızı gerektirebilir. Örneğin yazdığınız bir
programda kullanıcılarınızdan beklentiniz, programınızı Python'ın 3.x
sürümlerinden biri ile çalıştırmaları olabilir. Eğer programınız Python'ın 2.x
sürümlerinden biri ile çalıştırılırsa kullanıcıya bir uyarı mesajı göstermek
isteyebilirsiniz.

Hatta yazdığınız bir program, aynı serinin farklı sürümlerinde dahi çalışmayı
engelleyecek özellikler içeriyor olabilir. Örneğin ``print()`` fonksiyonunun
`flush` adlı parametresi dile `3.3` sürümü ile birlikte eklendi. Dolayısıyla bu
parametreyi kullanan bir program, kullanıcının `3.3` veya daha yüksek bir Python
sürümü kullanmasını gerektirir. Böyle bir durumda, programınızı çalıştıran
Python sürümünün en düşük `3.3` olmasını temin etmeniz gerekir. 

Peki bunu nasıl yapacaksınız?

Burada aklınızda ilk olarak, kodlarınıza `#!/usr/bin/env python3.3` veya `#!
python3.3` gibi bir satır eklemek gelmiş olabilir. Ama unutmayın, bu çözüm ancak
kısıtlı bir işlevsellik sunabilir. Programımıza böyle bir satır eklediğimizde,
programımızın Python'ın `3.3` sürümü ile çalıştırılması gerektiğini belirtiyoruz.
Ama `3.3` dışı bir sürümle çalıştırıldığında ne olacağını belirtmiyoruz. Böyle
bir durumda, eğer programımız `3.3` dışı bir sürümle çalıştırılırsa çökecektir.
Bizim burada daha kapsamlı ve esnek bir çözüm bulmamız gerekiyor.

Hatırlarsanız önceki derslerden birinde `sys` adlı bir modülden söz etmiştik.
Bildiğiniz gibi, bu modül içinde pek çok yararlı değişken ve fonksiyon
bulunuyor. Önceki derslerimizde, bu modül içinde bulunan ``exit()`` fonksiyonu
ile `stdout` ve `version` değişkenlerini gördüğümüzü hatırlıyor olmalısınız.
`sys` modülü içinde bulunan ``exit()`` fonksiyonunun programdan çıkmamızı
sağladığını, `stdout` değişkeninin standart çıktı konumu bilgisini tuttuğunu ve
`version` değişkeninin de kullandığımız Python sürümü hakkında bilgi verdiğini
biliyoruz. İşte yukarıda bahsettiğimiz programda da bu `sys` modülünden
yararlanacağız.

Bu iş için, `version` değişkenine çok benzeyen `version_info` adlı bir
değişkeni kullanacağız. 

Bu değişkenin nasıl kullanıldığına etkileşimli kabukta beraberce bakalım...

`sys` modülü içindeki araçları kullanabilmek için öncelikle bu modülü içe
aktarmamız gerektiğini biliyorsunuz::
    
    >>> import sys

Şimdi de bu modül içindeki `version_info` adlı değişkene erişelim::
    
    >>> sys.version_info

Bu komut bize şöyle bir çıktı verir:

.. parsed-literal::

    |version-info3|
    
Gördüğünüz gibi, bu değişken de bize tıpkı `version` adlı değişken gibi,
kullandığımız Python sürümü hakkında bilgi veriyor. 

Ben yukarıdaki komutu Python3'te verdiğinizi varsaydım. Eğer yukarıdaki komutu
Python3 yerine Python2'de verseydik şöyle bir çıktı alacaktık:

.. parsed-literal::

    |version-info2|

`version_info` ve `version` değişkenlerinin verdikleri çıktının birbirlerinden
farklı yapıda olduğuna dikkat edin. `version` değişkeni, `version_info`
değişkeninden farklı olarak şöyle bir çıktı verir:

.. parsed-literal::

    |version3-string|

`version_info` değişkeninin verdiği çıktı bizim şu anda yazmak istediğimiz
programa daha uygun. Bunun neden böyle olduğunu biraz sonra siz de
anlayacaksınız.

Gördüğünüz gibi, `version_info` değişkeninin çıktısında `major` ve `minor` gibi
bazı değerler var. Çıktıdan da rahatlıkla anlayabileceğiniz gibi, `major`,
kullanılan Python serisinin ana sürüm numarasını; `minor` ise alt sürüm
numarasını verir. Çıktıda bir de `micro` adlı bir değer var. Bu da kullanılan
Python serisinin en alt sürüm numarasını verir.

Bu değere şu şekilde erişiyoruz::
    
    >>> sys.version_info.major

Öteki değerlere de aynı şekilde ulaşıyoruz::
    
    >>> sys.version_info.minor
    >>> sys.version_info.micro

İşte bu çıktılardaki `major` (ve yerine göre bununla birlikte `minor` ve
`micro`) değerini kullanarak, programımızın hangi Python sürümü ile
çalıştırılması gerektiğini kontrol edebiliriz. Şimdi programımızı yazalım::
    
    import sys
    
    _2x_metni = """
    Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
    Programı çalıştırabilmek için sisteminizde Python'ın 
    3.x sürümlerinden biri kurulu olmalı."""
    
    _3x_metni = "Programa hoşgeldiniz."
    
    if sys.version_info.major < 3:
        print(_2x_metni)
    else:
        print(_3x_metni)

Gelin isterseniz öncelikle bu kodları biraz inceleyelim.

İlk olarak modülümüzü içe aktarıyoruz. Bu modül içindeki araçları
kullanabilmemiz için bunu yapmamız şart::
    
    import sys

Ardından Python'ın 2.x sürümlerinden herhangi birini kullananlar için bir uyarı
metni oluşturuyoruz::
    
    _2x_metni = """
    Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
    Programı çalıştırabilmek için sisteminizde Python'ın 
    3.x sürümlerinden biri kurulu olmalı."""
    
Bildiğiniz gibi Python'da değişken adları bir sayıyla başlamaz. O yüzden
değişken isminin başına bir tane alt çizgi işareti koyduğumuza dikkat edin.

Bu da Python3 kullanıcıları için::
    
    _3x_metni = "Programa hoşgeldiniz."

Artık sürüm kontrolü kısmına geçebiliriz. Eğer major parametresinin değeri 3'ten
küçükse _2x_metnini yazdırıyoruz. Bunun dışındaki bütün durumlar için ise
_3x_metnini basıyoruz::

    if sys.version_info.major < 3:
        print(_2x_metni)
    else:
        print(_3x_metni)

Gördüğünüz gibi, kullanılan Python sürümünü kontrol etmek ve eğer program
istenmeyen bir Python sürümüyle çalıştırılıyorsa ne yapılacağını belirlemek son
derece kolay.

Yukarıdaki çok basit bir kod parçası olsa da bize Python programlama diline ve bu
dilin farklı sürümlerine dair son derece önemli bazı bilgiler veriyor.

Eğer bu programı Python'ın 3.x sürümlerinden biri ile çalıştırdıysanız şu
çıktıyı alacaksınız::
    
    Programa hoşgeldiniz.

Ama eğer bu programı Python'ın 2.x sürümlerinden biri ile çalıştırdıysanız,
beklentinizin aksine, şöyle bir hata mesajı alacaksınız::

      File "test.py", line 5
    SyntaxError: Non-ASCII character '\xc4' in file test.py on line 6, but no
    encoding declared; see http://www.python.org/peps/pep-0263.html for details    

Biz `_2x_metni` adlı değişkenin ekrana basılmasını beklerken Python bize bir
hata mesajı gösterdi. Aslında siz bu hata mesajına hiç yabancı değilsiniz. Bunu
daha önce de görmüştünüz. Hatırlarsanız önceki derslerimizde karakter
kodlamalarından bahsederken, Python'ın 2.x sürümlerinde öntanımlı karakter
kodlamasının ASCII olduğundan söz etmiştik. Bu yüzden programlarımızda Türkçe
karakterleri kullanırken bazı ilave işlemler yapmamız gerekiyordu.

Burada ilk olarak karakter kodlamasını `UTF-8` olarak değiştirmemiz gerekiyor.
Bunun nasıl yapılacağını biliyorsunuz. Programımızın ilk satırına şu kodu
ekliyoruz::
    
    # -*- coding: utf-8 -*-

Bu satır Python3 için gerekli değil. Çünkü Python3'te öntanımlı karakter
kodlaması zaten `UTF-8`. Ama Python2'de öntanımlı karakter kodlaması `ASCII`. O
yüzden Python2 kullanıcılarını da düşünerek `UTF-8` kodlamasını açıkça
belirtiyoruz. Böylece programımızın Python'ın 2.x sürümlerinde Türkçe
karakterler yüzünden çökmesini önlüyoruz.

Ama burada bir problem daha var. Programımız Türkçe karakterler yüzünden
çökmüyor çökmemesine ama, bu defa da Türkçe karakterleri düzgün göstermiyor::
    
    Python'Ä±n 2.x sÃ¼rÃ¼mlerinden birini kullanÄ±yorsunuz.
    ProgramÄ± Ã§alÄ±ÅŸtÄ±rabilmek iÃ§in sisteminizde Python'Ä±n
    3.x sÃ¼rÃ¼mlerinden biri kurulu olmalÄ±.
 
Programımızı Python'ın 2.x sürümlerinden biri ile çalıştıranların uyarı mesajını
düzgün bir şekilde görüntüleyebilmesini istiyorsanız, Türkçe karakterler içeren
karakter dizilerinin en başına bir 'u' harfi eklemelisiniz. Yani `_2x_metni`
adlı değişkeni şöyle yazmalısınız::
    
    _2x_metni = u"""
    Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
    Programı çalıştırabilmek için sisteminizde Python'ın 
    3.x sürümlerinden biri kurulu olmalı."""

Bu karakter dizisinin en başına bir 'u' harfi ekleyerek bu karakter dizisini
'unicode' olarak tanımlamış olduk. Eğer 'unicode' kavramını bilmiyorsanız endişe
etmeyin. İlerde bu kavramdan bolca söz edeceğiz. Biz şimdilik, içinde Türkçe
karakterler geçen karakter dizilerinin Python2 kullanıcıları tarafından düzgün
görüntülenebilmesi için başlarına bir 'u' harfi eklenmesi gerektiğini bilelim
yeter.

Eğer siz bir Windows kullanıcısıysanız ve bütün bu işlemlerden sonra bile Türkçe
karakterleri düzgün görüntüleyemiyorsanız, bu durum muhtemelen MS-DOS komut
satırının kullandığı yazı tipinin Türkçe karakterleri gösterememesinden
kaynaklanıyordur. Bu problemi çözmek için MS-DOS komut satırının başlık çubuğuna
sağ tıklayıp 'özellikler' seçeneğini seçerek yazı tipini 'Lucida Console' olarak
değiştirin. Bu işlemin ardından da komut satırında şu komutu verin::
    
    chcp 1254

Böylece Türkçe karakterleri düzgün görüntüleyebilirsiniz. 

.. note:: MS-DOS'taki Türkçe karakter problemi hakkında daha ayrıntılı bilgi
          için http://goo.gl/eRY1P adresindeki makalemizi inceleyebilirsiniz.

Şimdiye kadar anlattıklarımızdan öğrendiğiniz gibi, `sys` modülü içinde sürüm
denetlemeye yarayan iki farklı değişken var. Bunlardan biri `version`, öbürü ise
`version_info`. 

Python3'te bu değişkenlerin şu çıktıları verdiğiniz biliyoruz:

**version**:

.. parsed-literal::
    
    |version3-string|

**version_info**:

.. parsed-literal::

    |version-info3|

Gördüğünüz gibi, çıktıların hem yapıları birbirinden farklı, hem de verdikleri
bilgiler arasında bazı farklar da var. Mesela `version` değişkeni, kullandığımız
Python sürümünün hangi tarih ve saatte, hangi işletim sistemi üzerinde
derlendiği bilgisini de veriyor. Ancak kullanılan Python sürümünün ne olduğunu
tespit etmek konusunda `version_info` biraz daha pratik görünüyor. Bu değişkenin
bize `major`, `minor` ve `micro` gibi parametreler aracılığıyla sunduğu sayı
değerli verileri işleçlerle birlikte kullanarak bu sayılar üzerinde aritmetik
işlemler yapıp, kullanılan Python sürümünü kontrol edebiliyoruz.

`version` değişkeni bize bir karakter dizisi verdiği için, bu değişkenin
değerini kullanarak herhangi bir aritmetik işlem yapamıyoruz. Mesela
`version_info` değişkeniyle yukarıda yaptığımız büyüktür-küçüktür sorgulamasını
`version` değişkeniyle tabii ki yapamayız. 

Yukarıdaki örnekte seriler arası sürüm kontrolünü nasıl yapacağımızı gördük.
Bunun için kullandığımız kod şuydu::
    
    if sys.version_info.major < 3:
        ...

Burada kullanılan Python serisinin `3.x`'ten düşük olduğu durumları sorguladık.
Peki aynı serinin farklı sürümlerini denetlemek istersek ne yapacağız? Mesela
Python'ın `3.2` sürümünü sorgulamak istersek nasıl bir kod kullanacağız?

Bunun için şöyle bir şey yazabiliriz::
    
    if sys.version_info.major == 3 and sys.version_info.minor == 2:
        ...

Gördüğünüz gibi burada `version_info` değişkeninin hem `major` hem de `minor`
parametrelerini kullandık. Ayrıca hem ana sürüm, hem de alt sürüm için belli bir
koşul talep ettiğimizden ötürü `and` adlı Bool işlecinden de yararlandık. Çünkü
koşulun gerçekleşmesi, ana sürümün `3` **ve** alt sürümün `2` olmasına bağlı.

Yukarıdaki işlem için `version` değişkenini de kullanabilirdik. Dikkatlice
bakın::
    
    if "3.2" in sys.version:
        ...

Bildiğiniz gibi, `version` değişkeni Python'ın `3.x` sürümlerinde şuna benzer
bir çıktı veriyor:

.. parsed-literal::

    |version3-string|

İşte biz burada `in` işlecini kullanarak, `version` değişkeninin verdiği
karakter dizisi içinde '3.2' diye bir ifade aradık. 

Bu konuyu daha iyi anlamak için kendi kendinize bazı denemeler yapmanızı tavsiye
ederim. Ne kadar çok örnek kod yazarsanız, o kadar çok tecrübe kazanırsınız.

    


    



