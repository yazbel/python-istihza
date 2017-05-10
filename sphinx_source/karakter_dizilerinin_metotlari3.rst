.. meta::
   :description: Python 3.x'te karakter dizileri
   :keywords: python, string, karakter dizisi, metotlar

.. highlight:: py3

****************************************
Karakter Dizilerinin Metotları (Devamı)
****************************************

Karakter dizileri konusunun 4. bölümüne geldik. Bu bölümde de karakter
dizilerinin metotlarını incelemeye devam edeceğiz.

str.maketrans(), translate()
======================================

Bu iki metot birbiriyle bağlantılı olduğu ve genellikle birlikte kullanıldığı
için, bunları bir arada göreceğiz.

Dilerseniz bu iki metodun ne işe yaradığını anlatmaya çalışmak yerine bir örnek
üzerinden bu metotların görevini anlamayı deneyelim.

Şöyle bir vaka hayal edin: Bildiğiniz gibi, internet üzerinde bazen Türkçe
karakterleri kullanamıyoruz. Böyle durumlarda, elimizdeki bir metni, cümleyi
veya kelimeyi Türkçe karakter içermeyecek bir hale getirmemiz gerekebiliyor.
Örneğin şu cümleyi ele alalım:

    Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz.

İşte buna benzer bir cümleyi kimi zaman Türkçe karakterlerinden arındırmak
zorunda kalabiliyoruz. Eğer elinizde Türkçe yazılmış bir metin varsa ve sizin
amacınız bu metin içinde geçen Türkçeye özgü karakterleri noktasız benzerleriyle
değiştirmek ise ``str.maketrans()`` ve ``translate()`` metotlarından
yararlanabilirsiniz.

Örneğimiz şu cümle idi:

    Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz.

Amacımız bu cümleyi şu şekilde değiştirmek:

    Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.

Bunun için şöyle bir kod yazabilirsiniz::

    kaynak = "şçöğüıŞÇÖĞÜİ"
    hedef  = "scoguiSCOGUI"

    çeviri_tablosu = str.maketrans(kaynak, hedef)

    metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

    print(metin.translate(çeviri_tablosu))

Bu kodları çalıştırdığımızda şöyle bir çıktı elde ederiz::

    Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.

Gördüğünüz gibi, `"kaynak"` adlı karakter dizisi içinde belirttiğimiz bütün
harfler `"hedef"` adlı karakter dizisi içindeki harflerle tek tek değiştirildi.
Böylece Türkçeye özgü karakterleri ('şçöğüıŞÇÖĞÜİ') en yakın noktasız
benzerleriyle ('scoguiSCOGUI') değiştirmiş olduk.

Peki yukarıda nasıl bir süreç işledi de biz istediğimiz sonucu elde edebildik.
Dilerseniz yukarıdaki kodlara biraz daha yakından bakalım. Mesela
`çeviri_tablosu` adlı değişkenin çıktısına bakarak ``str.maketrans()`` metodunun
alttan alta neler karıştırdığını görelim::
    
    kaynak = "şçöğüıŞÇÖĞÜİ"
    hedef  = "scoguiSCOGUI"

    çeviri_tablosu = str.maketrans(kaynak, hedef)

    print(çeviri_tablosu)

Bu kodları çalıştırdığımızda şöyle bir çıktı alıyoruz::

    {214: 79, 231: 99, 220: 85, 199: 67, 304: 73, 305: 105, 
    286: 71, 246: 111, 351: 115, 252: 117, 350: 83, 287: 103}

Bu çıktı size tamamen anlamsız görünmüş olabilir. Ama aslında son derece anlamlı
ve bir o kadar da önemli bir çıktıdır bu. Gelin isterseniz bu çıktının yapısını
biraz inceleyelim. (Buna benzer bir çıktıyı ``sorted()`` metodunu incelerken de
görmüştük)

Gördüğünüz gibi, tamamen sayılardan oluşan bir çıktı bu. Burada birbirlerinden
virgül ile ayrılmış sayı çiftleri görüyoruz. Bu sayı çiftlerini daha net
görebilmek için bu çıktıyı derli toplu bir hale getirelim::
    
    {214: 79, 
     231: 99, 
     220: 85, 
     199: 67, 
     304: 73, 
     305: 105, 
     286: 71, 
     246: 111, 
     351: 115, 
     252: 117, 
     350: 83, 
     287: 103}

Bu şekilde sanırım çıktımız biraz daha anlam kazandı. Gördüğünüz gibi, iki nokta
üst üste işaretinin solunda ve sağında bazı sayılar var. Tahmin edebileceğiniz
gibi, soldaki sayılar sağdaki sayılarla ilişkili.

Peki bütün bu sayılar ne anlama geliyor ve bu sayılar arasında ne tür bir ilişki
var?

Teknik olarak, bilgisayarların temelinde sayılar olduğunu duymuşsunuzdur.
Bilgisayarınızda gördüğünüz her karakter aslında bir sayıya karşılık gelir.
Zaten bilgisayarlar 'a', 'b', 'c', vb. kavramları anlayamaz. Bilgisayarların
anlayabildiği tek şey sayılardır. Mesela siz klavyeden 'a' harfini girdiğinizde
bilgisayar bunu `97` olarak algılar. Ya da siz 'i' harfi girdiğinizde,
bilgisayarın gördüğü tek şey `105` sayısıdır... Bu durumu Python'daki ``chr()``
adlı özel bir fonksiyon yardımıyla teyit edebiliriz. Dikkatlice inceleyin::
    
    >>> chr(97)
    
    'a'
    
    >>> chr(105)
    
    'i'
    
    >>> chr(65)
    
    'A'

Gördüğünüz gibi, gerçekten de her sayı bir karaktere karşılık geliyor.
İsterseniz bir de yukarıdaki sayı grubundaki sayıları denetleyelim::
    
    for i in 214, 231, 220, 199, 304, 305, 286, 246, 351, 252, 350, 287:
        print(i, chr(i))

Bu kodları çalıştırdığımızda şu çıktıyı elde ediyoruz::

    214 Ö
    231 ç
    220 Ü
    199 Ç
    304 İ
    305 ı
    286 Ğ
    246 ö
    351 ş
    252 ü
    350 Ş
    287 ğ

Bu çıktı sayesinde bazı şeyler zihninizde yavaş yavaş açıklığa kavuşuyor olmalı.
Bu çıktı mesela `214` sayısının 'Ö' harfine, `220` sayısının 'Ü' harfine, `305`
sayısının da 'ı' harfine karşılık geldiğini gösteriyor.

Burada iki nokta işaretinin sol tarafında kalan sayıların karakter
karşılıklarını gördük. Bir de iki nokta işaretinin sağ tarafında kalan sayılara
bakalım::

    for i in 79, 99, 85, 67, 73, 105, 71, 111, 115, 117, 83, 103:
        print(i, chr(i))

Bu da şu çıktıyı verdi::

    79  O
    99  c
    85  U
    67  C
    73  I
    105 i
    71  G
    111 o
    115 s
    117 u
    83  S
    103 g

Burada da mesela `79` sayısının 'O' harfine, `85` sayısının 'U' harfine, `105`
sayısının da 'i' harfine karşılık geldiğini görüyoruz.

Yukarıdaki ve yukarıdan bir önceki kodların çıktılarını bir araya getirirseniz
şöyle bir durumla karşı karşıya olduğunuzu görürsünüz::

    Ö   O
    ç   c
    Ü   U
    Ç   C   
    İ   I
    ı   i
    Ğ   G   
    ö   o
    ş   s
    ü   u
    Ş   S  
    ğ   g

Bütün bu söylediklerimizden şu sonuç çıkıyor: 

``çeviri_tablosu = str.maketrans(kaynak, hedef)`` satırı, `kaynak` ve `hedef`
olarak adlandırdığımız karakter dizilerini birleştirip, bu değişkenler içindeki
herbir karakteri birbiriyle eşleştiriyor. Yani aşağıdaki gibi bir işlem
yapıyor::
    
    çeviri_tablosu = {"Ö": "O",
                      "ç": "c",
                      "Ü": "U",
                      "Ç": "C",   
                      "İ": "I",
                      "ı": "i",
                      "Ğ": "G",
                      "ö": "o",
                      "ş": "s",
                      "ü": "u",
                      "Ş": "S",
                      "ğ": "g"}

Burada `çeviri_tablosu` değişkeni içinde gösterdiğimiz biçimin Python'daki adı
'sözlük'tür. Sözlükler de tıpkı karakter dizileri gibi bir veri tipidir. Bunları
da birkaç bölüm sonra ayrıntılı bir biçimde inceleyeceğiz. Biz burada, bazı
şeyleri anlamamızı kolaylaştıracağı için sözlük adlı veri tipini oldukça genel
bir biçimde sizlere tanıttık. Dediğim gibi, bu veri tipinin ayrıntılarını daha
sonra inceleyeceğiz, ama yine de şu noktada sözlükleri kenarından köşesinden de
olsa tanımamız bizim için faydalı olacaktır.

Dediğim gibi, yukarıda `çeviri_tablosu` adıyla gösterdiğimiz şey bir sözlüktür.
Bu sözlüğün nasıl çalıştığını görmek için şöyle bir kod yazalım::
    
    çeviri_tablosu = {"Ö": "O",
                      "ç": "c",
                      "Ü": "U",
                      "Ç": "C",   
                      "İ": "I",
                      "ı": "i",
                      "Ğ": "G",
                      "ö": "o",
                      "ş": "s",
                      "ü": "u",
                      "Ş": "S",
                      "ğ": "g"}

    print(çeviri_tablosu["Ö"])

Bu kodları bir dosyaya kaydedip çalıştırırsanız şöyle bir çıktı alırsınız::

    O

Gördüğünüz gibi, sözlük içinde geçen `"Ö"` adlı öğeyi parantez içinde
belirttiğimiz zaman, Python bize bu öğenin karşısındaki değeri veriyor. Sözlük
içinde `"Ö"` öğesinin karşılığı `"O"` harfi olduğu için de çıktımız `"O"`
oluyor. Bir de şunlara bakalım::
    
    çeviri_tablosu = {"Ö": "O",
                      "ç": "c",
                      "Ü": "U",
                      "Ç": "C",   
                      "İ": "I",
                      "ı": "i",
                      "Ğ": "G",
                      "ö": "o",
                      "ş": "s",
                      "ü": "u",
                      "Ş": "S",
                      "ğ": "g"}

    print(çeviri_tablosu["Ö"])
    print(çeviri_tablosu["ç"])
    print(çeviri_tablosu["Ü"])
    print(çeviri_tablosu["Ç"])
    print(çeviri_tablosu["İ"])
    print(çeviri_tablosu["ı"])
    print(çeviri_tablosu["Ğ"])
    print(çeviri_tablosu["ö"])
    print(çeviri_tablosu["Ş"])
    print(çeviri_tablosu["ğ"])

Bu kodları çalıştırdığımızda ise şöyle bir çıktı alıyoruz::

    O
    c
    U
    C
    I
    i
    G
    o
    S
    g

Gördüğünüz gibi, sözlük içinde iki nokta üst üste işaretinin sol tarafında
görünen öğeleri parantez içinde yazarak, iki nokta üst üste işaretinin sağ
tarafındaki değerleri elde edebiliyoruz.

Bütün bu anlattıklarımızdan sonra şu satırları gayet iyi anlamış olmalısınız::

    kaynak = "şçöğüıŞÇÖĞÜİ"
    hedef  = "scoguiSCOGUI"

    çeviri_tablosu = str.maketrans(kaynak, hedef)

Burada Python, `kaynak` ve `hedef` adlı değişkenler içindeki karakter dizilerini
birer birer eşleştirerek bize bir sözlük veriyor. Bu sözlükte::
    
    "ş" harfi "s" harfine; 
    "ç" harfi "c" harfine; 
    "ö" harfi "o" harfine;
    "ğ" harfi "g" harfine;
    "ü" harfi "u" harfine;
    "ı" harfi "i" harfine;
    "Ş" harfi "S" harfine;
    "Ç" harfi "C" harfine;
    "Ö" harfi "O" harfine;
    "Ğ" harfi "G" harfine;
    "Ü" harfi "U" harfine;
    "İ" harfi "I" harfine

karşılık geliyor...

Kodların geri kalanında ise şu satırları görmüştük::

    metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

    print(metin.translate(çeviri_tablosu))

Burada da orijinal metnimizi tanımladıktan sonra ``translate()`` adlı metot
yardımıyla, çeviri tablosundaki öğe eşleşmesi doğrultusunda metnimizi tercüme
ediyoruz. Bu kodlarda ``metin.translate(çeviri_tablosu)`` satırının yaptığı tek
şey `çeviri_tablosu` adlı sözlükteki eşleşme kriterlerini `metin` adlı karakter
dizisine uygulamaktan ibarettir.

Karakter dizilerinin bu ``maketrans()`` adlı metodu kullanım olarak gözünüze
öteki metotlardan farklı görünmüş olabilir. Daha açık bir dille ifade etmek
gerekirse, bu metodu bir karakter dizisi üzerine değil de `str` üzerine
uyguluyor olmamız, yani ``str.maketrans()`` yazıyor olmamız sizi şaşırtmış
olabilir. Eğer anlamanızı kolaylaştıracaksa;

::
    
    çeviri_tablosu = str.maketrans(kaynak, hedef)
    
satırını şu şekilde de yazabilirsiniz::
    
    çeviri_tablosu = ''.maketrans(kaynak, hedef)
    
Yani ``maketrans()`` metodunu boş bir karakter dizisi üzerine de
uygulayabilirsiniz. Neticede ``maketrans()`` karakter dizilerinin bir metodudur.
Bu metot hangi karakter dizisi üzerine uygulandığıyla değil, parametre olarak
hangi değerleri aldığıyla (bizim örneğimizde `kaynak` ve `hedef`) ilgilenir.
Dolayısıyla bu metodu ilgili-ilgisiz her türlü karakter dizisine
uygulayabilirsiniz::
    
    çeviri_tablosu = 'mahmut'.maketrans(kaynak, hedef)
    çeviri_tablosu = 'zalim dünya!'.maketrans(kaynak, hedef)

Ama tabii dikkat dağıtmamak açısından en uygun hareket, bu karakter dizisini
`str` üzerine uygulamak olacaktır::
    
    çeviri_tablosu = str.maketrans(kaynak, hedef)
    
Bu küçük ayrıntıya da dikkati çektiğimize göre yolumuza devam edebiliriz... 
    
Yukarıda verdiğimiz örnek vasıtasıyla ``str.maketrans()`` ve ``translate()``
adlı metotları epey ayrıntılı bir şekilde incelemiş olduk. Dilerseniz pratik
olması açısından bir örnek daha verelim:

istihza.com sitemizin forum üyelerinden Barbaros Akkurt
http://www.istihza.com/forum/viewtopic.php?f=25&t=63 adresinde şöyle bir
problemden bahsediyor:

    Ben on parmak Türkçe F klavye kullanıyorum. Bunun için, bazı tuş
    kombinasyonları ile veya sistem tepsisi üzerindeki klavye simgesine
    tıklayarak Türkçe Q - Türkçe F değişimi yapıyorum. Bazen bunu yapmayı
    unutuyorum ve bir metne bakarak yazıyorsam gözüm ekranda olmuyor. Bir
    paragrafı yazıp bitirdikten sonra ekranda bir karakter salatası görünce çok
    bozuluyorum.
    
İşte böyle bir durumda yukarıdaki iki metodu kullanarak o karakter salatasını
düzeltebilirsiniz. Karakter salatamız şu olsun:

    Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?

Buna göre kodlarımızı yazmaya başlayabiliriz. Öncelikle metnimizi tanımlayalım::

    metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

Şimdi de sırasıyla q ve f klavye düzenlerini birer karakter dizisi haline getirelim::

    q_klavye_düzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
    f_klavye_düzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

Burada amacımız yanlışlıkla q klavye düzeninde yazıldığı için karman çorman bir
hale gelmiş metni düzgün bir şekilde f klavye düzenine dönüştürmek. Yani burada
çıkış noktamız (kaynağımız) `q_klavye_düzeni` iken, varış noktamız (hedefimiz)
`f_klavye_düzeni`. Buna göre çeviri tablomuzu oluşturabiliriz::
    
    çeviri_tablosu = str.maketrans(q_klavye_düzeni, f_klavye_düzeni)

Tıpkı bir önceki örnekte olduğu gibi, burada da `çeviri_tablosu` adlı değişkeni
``print()`` fonksiyonunu kullanarak yazdırırsanız şöyle bir çıktıyla
karşılaşırsınız::
    
    {231: 46, 
     287: 113, 
     44 : 120, 
     46 : 44, 
     305: 110, 
     246: 98, 
     351: 121, 
     97 : 117, 
     98 : 231, 
     99 : 118, 
     100: 101, 
     101: 287, 
     102: 97, 
     103: 252, 
     104: 116, 
     105: 351, 
     106: 107, 
     107: 109, 
     108: 108, 
     109: 115, 
     110: 122, 
     111: 104, 
     112: 112, 
     113: 102, 
     114: 305, 
     115: 105, 
     116: 111, 
     117: 114, 
     118: 99, 
     119: 103, 
     120: 246, 
     121: 100, 
     122: 106,
     252: 119}
    
Tahmin edebileceğiniz gibi, bu sözlükte iki nokta üst üste işaretinin solundaki
sayılar `q_klavye_düzeni` adlı değişken içindeki karakterleri; sağındaki sayılar
ise `f_klavye_düzeni` adlı değişken içindeki karakterleri temsil ediyor.

Son olarak ``translate()`` metodu yardımıyla sözlükteki öğe eşleşmesini `metin`
adlı değişkenin üzerine uyguluyoruz::

    print(metin.translate(çeviri_tablosu))

Kodları topluca görelim::

    metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

    q_klavye_düzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
    f_klavye_düzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

    çeviri_tablosu = str.maketrans(q_klavye_düzeni, f_klavye_düzeni)

    print(metin.translate(çeviri_tablosu))

Ne elde ettiniz? 

Yukarıdaki iki örnekte de gördüğümüz gibi, ``str.maketrans()`` metodu kaynak ve
hedef karakter dizilerini alıp bunları birleştirerek bize bir sözlük veri
tipinde bir nesne veriyor. Yani tıpkı ``input()`` fonksiyonunun bize bir
karakter dizisi verdiği gibi, ``str.maketrans()`` metodu da bize bir sözlük
veriyor.

Eğer isterseniz, sözlüğü ``str.maketrans()`` metoduna oluşturtmak yerine,
kendiniz de bir sözlük oluşturarak ``str.maketrans()`` metoduna parametre olarak
atayabilirsiniz. Örneğin::
    
    metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

    sözlük = {"q": "f",
              "w": "g",
              "e": "ğ",
              "r": "ı",
              "t": "o",
              "y": "d",
              "u": "r",
              "ı": "n",
              "o": "h",
              "p": "p",
              "ğ": "q",
              "ü": "w",
              "a": "u",
              "s": "i",
              "d": "e",
              "f": "a",
              "g": "ü",
              "h": "t",
              "j": "k",
              "k": "m",
              "l": "l",
              "ş": "y",
              "i": "ş",
              ",": "x",
              "z": "j",
              "x": "ö",
              "c": "v",
              "v": "c",
              "b": "ç",
              "n": "z",
              "m": "s",
              "ö": "b",
              "ç": ".",
              ".": ","}

    çeviri_tablosu = str.maketrans(sözlük)
    print(metin.translate(çeviri_tablosu))

Burada birbiriyle eşleşecek karakterleri kendimiz yazıp bir sözlük oluşturduk ve
bunu parametre olarak doğrudan ``str.maketrans()`` metoduna verdik. Bu kodlarda
kaynak ve hedef diye iki ayrı karakter dizisi tanımlamak yerine tek bir sözlük
oluşturduğumuz için, ``str.maketrans()`` metodunu iki parametreyle değil, tek
parametreyle kullandığımıza dikkat edin. Ayrıca sözlüğü nasıl oluşturduğumuzu da
dikkatlice inceleyin.

Sözlükteki öğe çiftlerini böyle alt alta yazmamızın nedeni zorunluluk değil, bir
tercihtir. İstersek bu sözlüğü şöyle de tanımlayabilirdik::

    sözlük = {"q": "f", "w": "g", "e": "ğ", "r": "ı", "t": "o", "y": "d", "u": "r",
              "ı": "n", "o": "h", "p": "p", "ğ": "q", "ü": "w", "a": "u", "s": "i",
              "d": "e", "f": "a", "g": "ü", "h": "t", "j": "k", "k": "m", "l": "l",
              "ş": "y", "i": "ş", ",": "x", "z": "j", "x": "ö", "c": "v", "v": "c",
              "b": "ç", "n": "z", "m": "s", "ö": "b", "ç": ".", ".": ","}

Burada da öğe çiftlerini yan yana yazdık. Bu iki yöntemden hangisi size daha
okunaklı geliyorsa onu tercih edebilirsiniz.

Şimdi size bir soru sormama izin verin. Acaba aşağıdaki metin içinde geçen bütün
sesli harfleri silin desem, nasıl bir kod yazarsınız?

    Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
    tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
    isminin Python olmasına bakarak, bu programlama dilinin, adını piton
    yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
    dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
    The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
    Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
    gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
    figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
    diyebiliriz.
    
Aklınıza ilk olarak şöyle bir kod yazmak gelebilir::

    metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
    programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
    Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
    piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
    programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
    programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
    Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
    her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
    bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
    diyebiliriz."""

    sesli_harfler = "aeıioöuüAEIİOÖUÜ"

    yeni_metin = ""

    for i in metin:
        if not i in sesli_harfler:
            yeni_metin += i
        
    print(yeni_metin)

Burada öncelikle `metin` adlı bir değişken tanımlayarak metnimizi bu değişken
içine yerleştirdik. Ardından da Türkçedeki sesli harfleri içeren bir karakter
dizisi tanımladık.

Daha sonra da `yeni_metin` adlı boş bir karakter dizisi oluşturduk. Bu karakter
dizisi, orijinal metnin, sesli harfler ayıklandıktan sonraki halini
barındıracak. Biliyorsunuz, karakter dizileri değiştirilemeyen (*immutable*) bir
veri tipidir. Dolayısıyla bir karakter dizisi içinde yaptığımız değişiklikleri
koruyabilmek için bu değişiklikleri başka bir değişken içinde tutmamız
gerekiyor.

Bu kodların ardından bir `for` döngüsü tanımlıyoruz. Buna göre, metin içinde
geçen her bir karaktere tek tek bakıyoruz (``for i in metin:``) ve bu
karakterler arasında, `sesli_harfler` değişkeni içinde geçmeyenleri, yani bütün
sessiz harfleri (``if not i in sesli_harfler:``) tek tek `yeni_metin` adlı
değişkene yolluyoruz (``yeni_metin += i``).

Son olarak da `yeni_metin` adlı karakter dizisini ekrana basıyoruz. Böylece
orijinal metin içindeki bütün sesli harfleri ayıklamış oluyoruz.

Yukarıdaki, gayet doğru ve geçerli bir yöntemdir. Böyle bir kod yazmanızın
hiçbir sakıncası yok. Ama eğer isterseniz aynı işi ``str.maketrans()`` ve
``translate()`` metotları yardımıyla da halledebilirsiniz::
    
    metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
    programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
    Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
    piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
    programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
    programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
    Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
    her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
    bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
    diyebiliriz."""
    
    silinecek = "aeıioöuüAEIİOÖUÜ"

    çeviri_tablosu = str.maketrans('', '', silinecek)

    print(metin.translate(çeviri_tablosu))

Burada da öncelikle metnimizi bir karakter dizisi içine yerleştirdik. Daha sonra
da şu kodu yazdık::
    
    silinecek = "aeıioöuüAEIİOÖUÜ"

Bu kodlar yardımıyla, metin içinden çıkarmak istediğimiz harfleri tek tek
belirledik.

Ardından ``str.maketrans()`` fonksiyonumuzu yazarak çeviri tablosunu oluşturduk.
Burada ilk iki parametrenin boş birer karakter dizisi olduğuna dikkat ediyoruz.
İlk iki parametreyi bu şekilde yazmamızın nedeni şu: Biz orijinal metin içindeki
herhangi bir şeyi değiştirmek istemiyoruz. Bizim amacımız orijinal metin
içindeki sesli harfleri silmek. Tabii o iki parametreyi yazmasak da olmaz. O
yüzden o iki parametrenin yerine birer tane boş karakter dizisi yerleştiriyoruz.

Bu noktada `çeviri_tablosu` adlı değişkeni yazdırarak neler olup bittiğini daha
net görebilirsiniz::

    {214: None, 
     97 : None, 
     101: None, 
     65 : None, 
     105: None, 
     111: None, 
     304: None, 
     305: None, 
     220: None, 
     117: None, 
     246: None, 
     73 : None, 
     79 : None, 
     252: None, 
     85 : None,
     69 : None}

Gördüğünüz gibi, `silinecek` adlı değişken içindeki bütün karakterler ``None``
değeriyle eşleşiyor... ``None`` 'hiç, sıfır, yokluk' gibi anlamlara gelir.
Dolayısıyla Python, iki nokta üst üste işaretinin sol tarafındaki karakterlerle
karşılaştığında bunların yerine birer adet 'yokluk' koyuyor! Yani sonuç olarak
bu karakterleri metinden silmiş oluyor...

Bu kodlarda iki nokta üst üste işaretinin solundaki karakterlerin ``None`` ile
eşleşmesini sağlayan şey, ``str.maketrans()`` metoduna verdiğimiz üçüncü
parametredir. Eğer o parametreyi yazmazsak, yani kodlarımızı şu şekle getirirsek
`çeviri_tablosu` değişkeninin çıktısı farklı olacaktır::
    
    metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
    programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
    Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
    piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
    programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
    programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
    Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
    her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
    bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
    diyebiliriz."""
    
    silinecek = "aeıioöuüAEIİOÖUÜ"

    çeviri_tablosu = str.maketrans('', '')

    print(çeviri_tablosu)

Bu kodları çalıştırdığımızda şöyle bir çıktı alırız::

    {}

Gördüğünüz gibi, elde ettiğimiz şey boş bir sözlüktür. Sözlük boş olduğu, yani
değiştirilecek herhangi bir karakter olmadığı için bu kodlar orijinal metin
üzerinde herhangi bir değişiklik yapmaz.

İsterseniz üçüncü parametrenin ne işe yaradığını ve nasıl çalıştığını daha iyi
anlayabilmek için daha basit bir örnek verelim::

    metin = "Cem Yılmaz"

    kaynak = "CY"
    hedef  = "cy"
    silinecek = "eıa "

    çeviri_tablosu = str.maketrans(kaynak, hedef, silinecek)

    print(metin.translate(çeviri_tablosu))
    
Burada 'C' ve 'Y' harflerini sırasıyla 'c' ve 'y' harfleriyle eşleştirdik. Bu
nedenle orijinal metin içindeki 'C' ve 'Y' harfleri yerlerini sırasıyla 'c' ve
'y' harflerine bıraktı. Silinecek karakterler olarak ise 'e', 'ı', 'a' ve boşluk
karakterlerini seçtik. Böylece 'Cem Yılmaz' adlı orijinal metin içindeki boşluk
karakteri de silinerek, bu metin 'cmylmz' karakter dizisine dönüştü.

isalpha()
=============

Bu metot yardımıyla bir karakter dizisinin 'alfabetik' olup olmadığını
denetleyeceğiz. Peki 'alfabetik' ne demek?

Eğer bir karakter dizisi içinde yalnızca alfabe harfleri ('a', 'b', 'c' gibi...)
varsa o karakter dizisi için 'alfabetik' diyoruz. Bir örnekle bunu
doğrulayalım::
    
	>>> a = "kezban"
	>>> a.isalpha()

	True

Ama::

	>>> b = "k3zb6n"
	>>> b.isalpha()

	False


isdigit()
=============

Bu metot da ``isalpha()`` metoduna benzer. Bunun yardımıyla bir karakter
dizisinin sayısal olup olmadığını denetleyebiliriz. Sayılardan oluşan karakter
dizilerine 'sayı değerli karakter dizileri' adı verilir. Örneğin şu bir 'sayı
değerli karakter dizisi'dir::
    
	>>> a = "12345"

Metodumuz yardımıyla bunu doğrulayabiliriz::

	>>> a.isdigit()

	True

Ama şu karakter dizisi sayısal değildir::

	>>> b = "123445b"

Hemen kontrol edelim::

	>>> b.isdigit()

	False
	
isalnum()
=============

Bu metot, bir karakter dizisinin 'alfanümerik' olup olmadığını denetlememizi
sağlar. Peki 'alfanümerik' nedir?

Daha önce bahsettiğimiz metotlardan hatırlayacaksınız:

Alfabetik karakter dizileri, alfabe harflerinden oluşan karakter dizileridir.

Sayısal karakter dizileri, sayılardan oluşan karakter dizileridir.

Alfanümerik karakter dizileri ise bunun birleşimidir. Yani sayı ve harflerden
oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir. Örneğin şu
karakter dizisi alfanümerik bir karakter dizisidir::
    
	>>> a = "123abc"

İsterseniz hemen bu yeni metodumuz yardımıyla bunu doğrulayalım::

	>>> a.isalnum()

	True

Eğer denetleme sonucunda `True` alıyorsak, o karakter dizisi alfanümeriktir. Bir
de şuna bakalım::
    
	>>> b = "123abc>"
	>>> b.isalnum()

	False

`b` değişkeninin tuttuğu karakter dizisinde alfanümerik karakterlerin yanısıra
(`"123abc"`), alfanümerik olmayan bir karakter dizisi de bulunduğu için (`">"`),
``b.isalnum()`` şeklinde gösterdiğimiz denetlemenin sonucu `False` (yanlış)
olarak görünecektir.

Dolayısıyla, bir karakter dizisi içinde en az bir adet alfanümerik olmayan bir
karakter dizisi bulunursa (bizim örneğimizde ``">"``), o karakter dizisi
alfanümerik olmayacaktır.

isdecimal()
=================

Bu metot yardımıyla bir karakter dizisinin ondalık sayı cinsinden olup
olmadığını denetliyoruz. Mesela aşağıdaki örnek ondalık sayı cinsinden bir
karakter dizisidir::
    
    >>> a = "123"
    >>> a.isdecimal()
    
    True

Ama şu ise kayan noktalı (*floating-point*) sayı cinsinden bir karakter dizisidir::

    >>> a = "123.3"
    >>> a.isdecimal()
    
    False
    
Dolayısıyla ``a.isdecimal()`` komutu `False` çıktısı verir...


isidentifier()
====================

*Identifier* kelimesi Türkçede 'tanımlayıcı' anlamına gelir. Python'da
değişkenler, fonksiyon ve modül adlarına 'tanımlayıcı' denir. İşte başlıkta
gördüğümüz ``isidentifier()`` metodu, neyin tanımlayıcı olup neyin tanımlayıcı
olamayacağını denetlememizi sağlar. Hatırlarsanız değişkenler konusundan
bahsederken, değişken adı belirlemenin bazı kuralları olduğunu söylemiştik. Buna
göre, örneğin, değişken adları bir sayı ile başlayamıyordu. Dolayısıyla şöyle
bir değişken adı belirleyemiyoruz::
    
    >>> 1a = 12

Dediğimiz gibi, değişkenler birer tanımlayıcıdır. Dolayısıyla bir değişken
adının geçerli olup olmadığını ``isidentifier()`` metodu yardımıyla
denetleyebiliriz::
    
    >>> "1a".isidentifier()
    
    False

Demek ki ``"1a"`` ifadesini herhangi bir tanımlayıcı adı olarak kullanamıyoruz.
Yani bu ada sahip bir değişken, fonksiyon adı veya modül adı oluşturamıyoruz.
Ama mesela ``"liste1"`` ifadesi geçerli bir tanımlayıcıdır. Hemen denetleyelim::
    
    >>> "liste1".isidentifier()
    
    True

isnumeric()
==================

Bu metot bir karakter dizisinin nümerik olup olmadığını denetler. Yani bu metot
yardımıyla bir karakter dizisinin sayı değerli olup olmadığını
denetleyebiliriz::
    
    >>> "12".isnumeric()
    
    True
    
    >>> "dasd".isnumeric()
    
    False

isspace()
==============

Bu metot yardımıyla bir karakter dizisinin tamamen boşluklardan oluşup
oluşmadığını denetleyebiliriz. Eğer karakter dizimiz boşluklardan oluşuyorsa bu
metot `True` çıktısı verecek, ama eğer karakter dizimizin içinde bir tane bile
boşluk harici karakter varsa bu metot `False` çıktısı verecektir::
    
    >>> a = " "
    >>> a.isspace()
    
    True
    
    >>> a = "              "
    >>> a.isspace()
    
    True
    
    >>> a = "" #karakter dizimiz tamamen boş. İçinde boşluk karakteri bile yok...
    >>> a.isspace() 
    
    False
    
    >>> a = "fd"
    >>> a.isspace()
    
    False


isprintable()
==================

Hatırlarsanız önceki derslerimizde `\\n`, `\\t`, `\\r` ve buna benzer
karakterlerden söz etmiştik. Örneğin `\\n` karakterinin 'satır başı' anlamına
geldiğini ve bu karakterin görevinin karakter dizisini bir alt satıra almak
olduğunu söylemiştik. Örnek verelim::
    
    >>> print("birinci satır\nikinci satır")
    
    birinci satır
    ikinci satır

Bu örnekte `\\n` karakterinin öteki karakterlerden farklı olduğunu görüyorsunuz.
Mesela `"b"` karakteri komut çıktısında görünüyor. Ama `\\n` karakteri çıktıda
görünmüyor. `\\n` karakteri elbette yukarıdaki kodlar içinde belli bir işleve
sahip. Ancak karakter dizisindeki öteki karakterlerden farklı olarak `\\n`
karakteri ekranda görünmüyor. İşte Python'da bunun gibi, ekranda görünmeyen
karakterlere 'basılmayan karakterler' (*non-printing characters*) adı verilir.
'b', 'c', 'z', 'x', '=', '?', '!' ve benzeri karakterler ise 'basılabilen
karakterler' (*printable characters*) olarak adlandırılır. İşte başlıkta
gördüğünüz ``isprintable()`` metodu da karakterlerin bu yönünü sorgular. Yani
bir karakterin basılabilen bir karakter mi yoksa basılmayan bir karakter mi
olduğunu söyler bize. Örneğin::
    
    >>> karakter = "a"
    >>> karakter.isprintable()
    
    True

Demek ki `"a"` karakteri basılabilen bir karaktermiş. Bir de şuna bakalım::

    >>> karakter = "\n"
    >>> karakter.isprintable()
    
    False

Demek ki `\\n` karakteri gerçekten de basılamayan bir karaktermiş. 

Basılamayan karakterlerin listesini görmek için http://www.asciitable.com/
adresini ziyaret edebilirsiniz. Listedeki ilk `32` karakter (`0`'dan başlayarak
`32`'ye kadar olan karakterler) ve listedeki `127.` karakter basılamayan
karakterlerdir.

