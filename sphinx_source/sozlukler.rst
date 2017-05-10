.. meta::
   :description: Python 3.x'te sözlükler adlı veri tipi
   :keywords: python, sözlük, sözlükler, dictionary

.. highlight:: py3

**********
Sözlükler
**********

Şu ana kadar Python programlama dilinde veri tipi olarak karakter dizilerini,
sayıları, listeleri, demetleri ve dosyaları öğrendik. Yeni veri tipleri
öğrendikçe Python'daki hareket alanımızın da genişlediğini siz de
farketmişsinizdir. Bu bölümde yine Python'daki önemli veri tiplerinden birini
inceleyeceğiz. Bu defa inceleyeceğimiz veri tipinin adı sözlük. İngilizcede buna
*dictionary* diyorlar.

Sözlükler de, tıpkı daha önceki derslerimizde öğrendiğimiz karakter dizileri,
sayılar, listeler, demetler ve dosyalar gibi programlama maceramız boyunca
işlerimizi bir hayli kolaylaştıracak ve hareket imkanımızı genişletecek veri
tiplerinden biridir.

Öteki veri tiplerinde olduğu gibi, sözlüklerin de birtakım metotları vardır.
İşte bu bölümde hem genel olarak sözlüklerden söz edeceğiz, hem de bu veri
tipinin metotlarını en ince ayrıntısına kadar inceleyeceğiz.

Sözlük denen veri tipi Python programlama dilinin son derece kullanışlı ve işe
yarar araçlarından bir tanesidir. Programlama alanında ilerledikçe, bu veri
tipinin neler yapabileceğini görüp şaşıracağınızı rahatlıkla söyleyebilirim.

Esasında biz daha önceki derslerimizin birinde sözlük adlı bu veri tipinden
üstünkörü de olsa söz etmiştik. Yani aslında bu veri tipiyle tanışıklığımız
eskiye dayanıyor.

Hatırlayacaksınız, karakter dizilerinin ``str.maketrans()`` ve
``translate()`` adlı metotlarını anlatırken, Türkçeye özgü karakterleri ve
bunların noktasız karşılıklarını içeren `çeviri_tablosu` adını verdiğimiz şöyle
bir değişken tanımlamıştık::
    
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
  
    
Burada `çeviri_tablosu` değişkeni içinde gösterdiğimiz biçimin Python'daki
adının 'sözlük' olduğunu da ifade etmiştik. İşte bu bölümde, orada şöyle bir
değinip geçtiğimiz bu veri tipini çok daha ayrıntılı bir şekilde ele alma
imkanımız olacak.

Hem eski bilgilerimize dayanarak, hem de yukarıda anlattıklarımızdan yola
çıkarak sözlük veri tipinin ne olduğuna dair halihazırda kafamızda bir fikir
oluşmuş olduğunu söyleyebiliriz. 

Sözlükler öteki veri tiplerine kıyasla biraz farklı bir görünüşe sahip bir veri
tipidir. Biz birazdan sözlüklerin yapısını derinlemesine inceleyeceğiz.

Ancak sözlüklerin yapısını incelemeye geçmeden önce öğrenmemiz gereken bir şey
var. Tıpkı öteki veri tiplerinde olduğu gibi, sözlüklerle de çalışabilmek için
öncelikle bu veri tipini tanımlamış olmamız gerekiyor. O yüzden isterseniz
sözlüklerin yapısından söz etmeden önce bir sözlüğü nasıl tanımlayacağımızdan
bahsedelim.

Sözlük Tanımlamak
*******************

Dediğimiz gibi, karakter dizilerini anlatırken verdiğimiz sözlük örneği
sayesinde sözlüklerin neye benzediğini az çok biliyoruz. Gelin isterseniz
sözlüklerin nasıl tanımlandığını inceleyerek bu veri tipinin derinliklerine
doğru ilk kulaçlarımızı atalım.

Python programlama dilindeki sözlük veri tipi, gerçek hayatta 'sözlük' denince
aklınıza gelen şeye çok benzer. Mesela gerçek hayatta 'kitap' kelimesinin
İngilizce bir sözlükteki karşılığı *book* kelimesidir. Dolayısıyla 'kitap' ve
'*book*' kelimeleri arasındaki ilişkiyi herhalde şu şekilde temsil edebiliriz:

    kitap: book

Bu manzara bize 'kitap' kelimesinin karşılığının '*book*' olduğunu açık bir
şekilde gösteriyor. Eğer bu durumu Python'daki sözlük veri tipiyle göstermek
isteseydik şöyle bir şey yazacaktık::
    
    >>> kelimeler = {"kitap": "book"}

Burada, içeriği sözlük veri tipi olan `kelimeler` adlı bir değişken tanımladık.
Gördüğünüz gibi, listelere benzer bir şekilde sözlük veri tipi de içinde farklı
veri tiplerini barındıran, 'kapsayıcı' bir veri tipidir. Burada sözlüğümüz iki
adet karakter dizisinden oluşuyor.

Yukarıdaki sözlüğü nasıl tanımladığımıza çok dikkat edin. Nasıl ki listelerin
ayırt edici özelliği köşeli parantezlerdi, sözlüklerin ayırt edici özelliği de
küme parantezleridir.

Esasında sözlük dediğimiz şey en basit haliyle şöyle görünür::

    >>> sözlük = {}

Bu örnek boş bir sözlüktür. İsterseniz yukarıdaki veri tipinin gerçekten de bir
sözlük olduğunu kanıtlayalım::
    
    >>> type(sözlük)
    
    <class 'dict'>

Sözlüklerin Python programlama dilindeki teknik karşılığı ``dict`` ifadesidir.
``type(sözlük)`` sorgusu ``<class 'dict'>`` çıktısı verdiğine göre, `sözlük`
adlı değişkenin gerçekten de bir sözlük olduğunu söyleyebiliyoruz.

Yukarıda şöyle bir sözlük örneği verdiğimizi hatırlıyorsunuz::

    >>> kelimeler = {"kitap": "book"}

Python programlama diline özellikle yeni başlayanlar, sözlüklerin görünüşü
nedeniyle bir sözlükteki öğe sayısı konusunda tereddüte kapılabilir, örneğin
yukarıdaki sözlüğün `2` öğeden oluştuğu yanılgısına düşebilir. O halde bu
noktada size şöyle bir soru sormama izin verin: Acaba bu sözlükte kaç öğe var?
Hemen bakalım::
    
    >>> len(kelimeler)
    
    1

Demek ki elimizdeki veri tipi bir adet öğeye sahip bir sözlükmüş. Gördüğünüz
gibi, ``"kitap": "book"`` ifadesi tek başına bir öğe durumundadır. Yani burada
`"kitap"` karakter dizisini ayrı, `"book"` karakter dizisini ayrı bir öğe olarak
almıyoruz. Bu ikisi tek bir sözlük öğesi oluşturuyor. Hatırlarsanız, listelerde
öğeleri birbirinden ayırmak için virgül işaretlerinden yararlanıyorduk.
Sözlüklerde de birden fazla öğeyi birbirinden ayırmak için virgül işaretlerinden
yararlanacağız::
    
    >>> kelimeler = {"kitap": "book", "bilgisayar": "computer"}

Bir önceki örnek tek öğeliydi. Bu sözlük ise `2` öğeye sahiptir::

    >>> len(kelimeler)
    
    2

İlk derslerimizden bu yana sürekli olarak vurguladığımız gibi, Python
programlama dilinde doğru kod yazmak kadar okunaklı kod yazmak da çok önemlidir.
Mesela bir sözlüğü şöyle tanımladığımızda kodlarımızın pek okunaklı olmayacağını
söyleyebiliriz::
    
    sözlük = {"kitap": "book", "bilgisayar": "computer", "programlama": "programming", 
    "dil": "language", "defter": "notebook"}

Teknik olarak baktığımızda bu kodlarda hiçbir problem yok. Ancak sözlükleri
böyle sağa doğru uzayacak şekilde tanımladığımızda okunaklılığı azaltmış
oluyoruz. Bu yüzden yukarıdaki sözlüğü şöyle yazmayı tercih edebiliriz::
    
     sözlük = {"kitap"      : "book", 
               "bilgisayar" : "computer", 
               "programlama": "programming", 
               "dil"        : "language", 
               "defter"     : "notebook"}

Bu şekilde sözlükteki öğeler arasındaki ilişki daha belirgin, yazdığınız kodlar
da daha okunaklı bir hale gelecektir.

Python'da bir sözlük oluşturmanın başka yolları da olmakla birlikte, en temel
sözlük oluşturma yöntemi yukarıdaki örneklerde gösterdiğimiz gibidir. Biz
ilerleyen sayfalarda sözlük oluşturmanın farklı yöntemlerini de ele alacağız.
Ancak şimdilik 'sözlük tanımlama' konusunu burada noktalayıp sözlüklerle ilgili
önemli bir konuya daha değinelim.

Sözlük Öğelerine Erişmek
************************

Yukarıdaki örneklerden bir sözlüğün en basit şekilde nasıl tanımlanacağını
öğrendik. Peki tanımladığımız bir sözlüğün öğelerine nasıl erişeceğiz?

Hemen basit bir örnek verelim. Daha önce tanımladığımız şu sözlüğe bir bakalım
mesela::

     sözlük = {"kitap"      : "book", 
               "bilgisayar" : "computer", 
               "programlama": "programming", 
               "dil"        : "language", 
               "defter"     : "notebook"}

Bu sözlükte birtakım Türkçe kelimeler ve bunların İngilizce karşılıkları var.
Şimdi mesela bu sözlükteki 'kitap' adlı öğeye erişelim::
    
    print(sözlük["kitap"])

Bu kodları çalıştırdığımızda şöyle bir çıktı alırız::

    book

Yukarıdaki örnekten anladığımız gibi, sözlük öğelerine erişmek için şöyle bir
formül kullanıyoruz::
    
    sözlük[sözlük_öğesinin_adı]

Aynı şekilde `sözlük` değişkeni içindeki 'bilgisayar' öğesinin karşılığını almak
istersek şöyle bir kod yazıyoruz::
    
    print(sözlük["bilgisayar"])

Bu da bize `"computer"` çıktısını veriyor.

Karakter dizilerini anlatırken verdiğimiz `çeviri_tablosu` adlı sözlüğe ve orada
anlattıklarımıza geri dönelim şimdi. Artık sözlük adlı veri tipiyle iyiden iyiye
tanıştığımıza göre, orada anlattıklarımız zihninizde daha net bir hale gelmiş
olmalı.

Oradaki tablomuz şöyleydi::

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

Mesela bu sözlükteki `"Ö"` öğesinin karşılığını elde etmek için şöyle bir kod
yazdığımızı gayet iyi hatırlıyorsunuz::
    
    print(çeviri_tablosu["Ö"])

Bu kodları bir dosyaya kaydedip çalıştırdığımızda şöyle bir çıktı alıyorduk::

    O

Gördüğünüz gibi sözlükteki `"Ö"` adlı öğeyi parantez içinde belirttiğimiz zaman,
Python bize bu öğenin karşısındaki değeri veriyor. Dolayısıyla sözlük içinde
`"Ö"` öğesinin karşılığı `"O"` harfi olduğu için de çıktımız `"O"` oldu.

Sözlüğün öteki öğelerini ise şu şekilde alabiliyoruz::

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

Ancak kod tekrarından kaçınmak için yukarıdaki kodları şu şekilde sadeleştirme
imkanımızın da olduğunu biliyorsunuz::
    
    for i in çeviri_tablosu:
        print(çeviri_tablosu[i])

Gördüğünüz gibi, sözlük içinde iki nokta üst üste işaretinin sol tarafında
görünen öğeleri köşeli parantez içinde yazarak, iki nokta üst üste işaretinin
sağ tarafındaki değerleri elde edebiliyoruz.

Eğer bir sözlük içinde bulunmayan bir öğeye erişmeye çalışırsak Python bize
``KeyError`` tipinde bir hata mesajı verecektir. Mesela yukarıdaki sözlüğü temel
alacak olursak şöyle bir sorgu hata verecektir::
    
    >>> print(çeviri_tablosu["Z"])

    Traceback (most recent call last):
      File "deneme.py", line 14, in <module>
        print(çeviri_tablosu["Z"])
    KeyError: 'Z'

Sözlükte `"Z"` kaydı bulunmadığı için doğal olarak Python'ın bize bir hata
mesajı göstermekten başka çaresi kalmıyor.

Sözlükler ile ilgili epey bilgi edindik. Dilerseniz bu öğrendiklerimizi örnek
bir uygulama üzerinde somutlaştırmaya çalışalım. Mesela Python'daki sözlükleri
kullanarak basit bir telefon defteri uygulaması yazalım::
    
    telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                       "mehmet su": "0543 543 42 42",
                       "seda naz" : "0533 533 33 33",
                       "eda ala"  : "0212 212 12 12"}

    kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

    cevap = "{} adlı kişinin telefon numarası: {}"

    print(cevap.format(kişi, telefon_defteri[kişi]))

Burada öncelikle isimler ve telefon numaralarından oluşan, sözlük veri tipinde
bir telefon defteri oluşturduk::
    
    telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                       "mehmet su": "0543 543 42 42",
                       "seda naz" : "0533 533 33 33",
                       "eda ala"  : "0212 212 12 12"}

Bu kodlarda bilmediğimiz hiçbir şey yok. Sözlüklere dair öğrendiklerimizi
kullanarak oluşturduğumuz oldukça basit bir sözlüktür bu.

Daha sonra kullanıcıdan, telefon numarasını öğrenmek için bir kişi adı girmesini
istiyoruz. Bunu da şu kodlar yardımıyla yapıyoruz::

    kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

Ardından da telefon defterinde sorgulama yapacak olan kullanıcıya göstereceğimiz
cevap için bir şablon oluşturuyoruz::

    cevap = "{} adlı kişinin telefon numarası: {}"

Mesela kullanıcı `"ahmet öz"` ismini sorgulamışsa ona şöyle bir cevap
vereceğiz::
    
    "ahmet öz adlı kişinin telefon numarası 0532 532 32 32"

Eğer aranan isim telefon defterinde varsa, bir önceki adımda tanımladığımız
cevap şablonuna göre kullanıcıyı bilgilendiriyoruz. Ama eğer eğer isim defterde
yoksa, programımız hata veriyor. Bunu önlemek için şöyle bir kod
yazabilirsiniz::
    
    telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                       "mehmet su": "0543 543 42 42",
                       "seda naz" : "0533 533 33 33",
                       "eda ala"  : "0212 212 12 12"}

    kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

    if kişi in telefon_defteri:
        cevap = "{} adlı kişinin telefon numarası: {}"
        print(cevap.format(kişi, telefon_defteri[kişi]))
    else:
        print("Aradığınız kişi telefon rehberinde yok!")

Gördüğünüz gibi, ``if kişi in telefon_defteri`` satırı yardımıyla öncelikle
aranan ismin sözlükte olup olmadığını denetledik. Eğer aranan isim sözlükte yer
alıyorsa bu telefon numarasını kullanıcılarımıza gösteriyoruz. Aksi durumda
aranan kişinin telefon rehberinde olmadığı konusunda kullanıcılarımızı
bilgilendiriyoruz.

Gördüğünüz gibi, sözlükler gerçekten de bize Python programlama maceramızda
yepyeni olanakların kapısını açabilecek kadar güçlü bir veri tipi. Bu veri
tipini programlarınızda bolca kullanacaksınız.

Yukarıda verdiğimiz telefon defteri uygulamasına şöyle bir baktığınızda bu
uygulamanın aslında geliştirilmeye bir hayli açık olduğu dikkatinizi çekmiştir.
Mesela biz bu uygulamada sadece kendi tanımladığımız bir telefon defteri
üzerinden sorgulama yapmaya izin verdik. Örneğin kullanıcı bu telefon defterine
kendi isim-telefon çiftlerini giremiyor. Bu veri tipini etkili bir şekilde
kullanmamızı sağlayacak araçlardan henüz yoksun olduğumuz için yukarıda
tanımladığımız uygulama çok basit kaldı. O halde, sözlük veri tipini daha
verimli ve etkili bir biçimde kullanabilmek için hiç vakit kaybetmeden bu veri
tipinin derinliklerine doğru yol almaya devam edelim.

Sözlüklerin Yapısı
******************

Yukarıdaki örneklerden, Python'da bir sözlüğün nasıl tanımlanacağını ve bir
sözlüğün öğelerine nasıl erişileceğini öğrendik. Gelin isterseniz şimdi sözlük
veri tipinin yapısına ilişkin bazı ayrıntıları inceleyelim.

Mesela şu örneği tekrar önümüze alalım::

    sözlük = {"kitap": "book"}

Burada iki nokta üst üste işaretinden önce ve sonra birer tane karakter dizisi
görüyoruz. Bu karakter dizileri `"kitap"` ve `"book"`. Dediğimiz gibi, sözlükler
de tıpkı listeler gibi, farklı veri tiplerinin bir araya gelmesi ile oluşan
birleşik/kapsayıcı bir veri tipidir. Dolayısıyla bir sözlük içinde sadece
karakter dizilerini değil, başka veri tiplerini de görebilirsiniz. İlerleyen
sayfalarda sözlüklere ilişkin daha karmaşık örnekler verdiğimizde sözlüklerin
hangi veri tiplerini içerebileceğini de göreceğiz.

Ne dedik? Sözlük içinde iki nokta üst üste işaretinin solunda ve sağında
`"kitap"` ve `"book"` adlı karakter dizileri var. Teknik olarak, iki nokta üst
üste işaretinin solundaki karakter dizisine 'anahtar' (*key*), sağındaki
karakter dizisine ise 'değer' (*value*) adı verilir. Bu bilgilere bakarak sözlük
için şöyle bir tanım verebiliriz:

    Sözlükler; anahtar ve değer çiftlerinin birbirleriyle eşleştirildiği bir
    veri tipidir. Dolayısıyla sözlükler bu anahtar ve değer çiftleri arasında
    birebir ilişki kurar.
    
Mesela yukarıdaki örnekte `"kitap"` öğesi anahtar, `"book"` öğesi ise değerdir.
İşte sözlük dediğimiz şey, bu anahtar ve değer çifti arasında birebir ilişki
kuran bir veri tipidir. Yani sözlük adlı veri tipi, bir anahtarı bir değerle
eşleştirme görevi görür.

Sözlüklerin bu özelliğini, sözlük öğelerine erişirken gayet net bir şekilde
görebiliyoruz.

Yukarıdaki örneklerde tanımladığımız sözlüklerde sadece karakter dizilerini
kullandık. Ama aslında sözlükler farklı veri tiplerinden oluşabilir. Mesela::
    
    sözlük = {"sıfır": 0,
              "bir"  : 1, 
              "iki"  : 2,
              "üç"   : 3,
              "dört" : 4,
              "beş"  : 5}

Burada sözlük içinde hem sayıları hem de karakter dizilerini kullandık. Aynı
şekilde sözlük içinde listelere de yer verebiliriz::
    
    sözlük = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
              "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
              "Seda Bayrak"    : ["İskenderun", "Doktor", 30]}

Mesela bu sözlükte `"Seda Bayrak"` adlı kişinin bilgilerine ulaşmak istersek
şöyle bir kod yazabiliriz::
    
    print(sözlük["Seda Bayrak"])

Bu kod bize şöyle bir çıktı verecektir::

    ['İskenderun', 'Doktor', 30]

Gördüğünüz gibi, sözlük içinde `"Seda Bayrak"` adlı öğenin karşısındaki bilgi
listesine ulaşabildik.

İstersek sözlükleri, içlerinde başka sözlükleri barındıracak şekilde de
tanımlayabiliriz::

    kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                                   "Meslek"  : "Öğretmen",
                                   "Yaş"     : 34},
                                  
               "Mehmet Yağız"   : {"Memleket": "Adana",
                                   "Meslek"  : "Mühendis",
                                   "Yaş"     : 40},
                
               "Seda Bayrak"    : {"Memleket": "İskenderun",
                                   "Meslek"  : "Doktor",
                                   "Yaş"     : 30}}

Böylece şöyle kodlar yazabiliriz::

    print(kişiler["Mehmet Yağız"]["Memleket"])
    print(kişiler["Seda Bayrak"]["Yaş"])
    print(kişiler["Ahmet Özkoparan"]["Meslek"])

Yukarıdaki yapının benzerini listeler konusundan hatırlıyor olmalısınız. İç içe
geçmiş listelerin öğelerine ulaşırken de buna benzer bir sözdiziminden
yararlanıyorduk. Örneğin::
    
    liste = [["Ahmet", "Mehmet", "Ayşe"],
             ["Sedat", "Serkan", "Selin"],
             ["Zeynep", "Nur", "Eda"]]

Burada bir liste içinde iç içe geçmiş üç farklı liste ile karşı karşıyayız.
Mesela ilk listenin ilk öğesi olan `"Ahmet"` adlı öğeye erişmek istersek şöyle
bir kod yazmamız gerekiyor::
    
    print(liste[0][0])

İşte iç içe geçmiş sözlüklerin öğelerine ulaşmak için de buna benzer bir kod
yazmamız gerekiyor. Örneğin `kişiler` adlı sözlükteki `"Mehmet Yağız"` adlı
kişinin yaşına ulaşmak istersek şöyle bir şey yazacağız::
    
    print(kişiler["Mehmet Yağız"]["Yaş"])

Gelin isterseniz `kişiler` adlı sözlüğü kullanarak basit bir irtibat listesi
uygulaması yazalım. Böylece sözlüklere elimizi alıştırmış oluruz::
    
    kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                                   "Meslek"  : "Öğretmen",
                                   "Yaş"     : 34},
                                  
               "Mehmet Yağız"   : {"Memleket": "Adana",
                                   "Meslek"  : "Mühendis",
                                   "Yaş"     : 40},
                
               "Seda Bayrak"    : {"Memleket": "İskenderun",
                                   "Meslek"  : "Doktor",
                                   "Yaş"     : 30}}

    isim = "Hakkında ayrıntılı bilgi edinmek \
    istediğiniz kişinin adını girin: "

    arama = input(isim)

    ayrıntı = input("Memleket/Meslek/Yaş? ")

    print(kişiler[arama][ayrıntı]) 

Tıpkı bir önceki telefon defteri uygulamamız gibi, bu irtibat listesi uygulaması
da geliştirilmeye açıktır. Ancak henüz bu iki uygulamayı geliştirmemizi
sağlayacak bilgilerden yoksunuz. Bu uygulamaları istediğimiz kıvama sokabilmek
için sözlüklere dair öğrenmemiz gereken başka şeyler de var.

Sözlüklerin öteki veri tiplerinden önemli bir farkı, sözlük içinde yer
alan öğelerin herhangi bir sıralama mantığına sahip olmamasıdır. Yani sözlükteki
öğeler açısından 'sıra' diye bir kavram yoktur. 

Örneğin bir liste, demet veya karakter dizisi içindeki öğelere; bu öğelerin o
liste, demet veya karakter dizisi içindeki sıralarına göre erişebilirsiniz::
    
    >>> liste = ["Ahmet", "Mehmet", "Zeynep"]
    >>> liste[0]
    
    'Ahmet'
    
    >>> liste[-1]
    
    'Zeynep'
    
Ancak sözlükler açısından böyle bir şey söz konusu değildir::

    >>> sözlük = {'elma': 'apple',
    ...           'armut': 'pear',
    ...           'çilek': 'strawberry'}
    >>> sözlük[0]
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 0
    
Gördüğünüz gibi, sözlükler üzerinde sıralamaya dayalı bir sorgulama yapmaya
çalıştığımızda Python bize bir hata mesajı gösteriyor.

Bu durumun etkilerini şurada da görebilirsiniz:

Dikkatlice bakın::
    
    >>> sözlük = {'a': '0', 'b': '1', 'c': '2'}
    >>> sözlük
    
    {'a': '0', 'c': '2', 'b': '1'}
    
Bu çıktıyı iyi inceleyin. Göreceğiniz gibi, çıktıda görünen öğeler bizim sözlüğü
tanımladığımız sıradaki gibi değil. Biz sözlüğü 'a', 'b' ve 'c' şeklinde
sıralayarak tanımladık, ama çıktı 'a', 'c' ve 'b' şeklinde oldu. O yüzden
sözlükler üzerinde çalışırken öğelerin sırasına dayalı herhangi bir işlem yapmak
hiç mantıklı değildir. Çünkü sözlükteki öğeleri tanımlarken kullandığınız
sıralama düzeninin çıktıda da aynen korunacağının herhangi bir garantisi
bulunmaz.

Sözlüklere Öğe Eklemek
***********************

Tıpkı listeler gibi, sözlükler de büyüyüp küçülebilen bir veri tipidir. Yani bir
sözlüğü ilk kez tanımladıktan sonra istediğimiz zaman bu sözlüğe yeni öğeler
ekleyebilir veya varolan öğeleri çıkarabiliriz. Biz şimdi bir sözlüğe nasıl öğe
ekleyeceğimizi inceleyeceğiz.

Diyelim ki elimizde şöyle boş bir sözlük var::

    >>> sözlük = {}

Bu listeye öğe eklemek için şöyle bir formül kullanacağız::

    >>> sözlük[anahtar] = değer

Bu formülü bir örnek üzerinden somutlaştıralım::

    >>> sözlük["Ahmet"] = "Adana"

Böylece sözlüğe, anahtarı `"Ahmet"`, değeri ise `"Adana"` olan bir öğe eklemiş
olduk. Sözlüğümüzün son durumunu kontrol edelim::
    
    >>> print(sözlük)
    
    {'Ahmet': 'Adana'}

Gördüğünüz gibi, "Ahmet" öğesi sözlüğe eklendi. Artık bu öğeye normal yollardan
ulaşabiliriz::
    
    >>> print(sözlük["Ahmet"])
    
    Adana

Elimiz alışsın diye sözlüğe öğe eklemeye devam edelim::

    >>> sözlük["Mehmet"] = "İstanbul"
    >>> sözlük
    
    {'Ahmet': 'Adana', 'Mehmet': 'İstanbul'}
    
    >>> sözlük["Seda"] = "Mersin"
    >>> sözlük
    
    {'Ahmet': 'Adana', 'Mehmet': 'İstanbul', 'Seda': 'Mersin'}
    
    >>> sözlük["Eda"] = "Tarsus"
    >>> sözlük
    
    {'Ahmet': 'Adana', 'Eda': 'Tarsus', 'Mehmet': 'İstanbul', 'Seda': 'Mersin'}
     
Özellikle son çıktıya dikkatlice bakın. Sözlüğe en son `"Eda"` öğesini
eklemiştik. Ama sözlüğü ekrana bastığımızda bu öğenin sözlüğün sonuna değil
ortasına bir yere yerleştiğini görüyoruz. Bu durumun, sözlüklerin sırasız bir
veri tipi olmasından kaynaklandığını biliyorsunuz.

Gelin pratik olması açısından birkaç örnek daha verelim.

Elimizde şöyle bir sözlük olsun::
    
    >>> personel = {"Mehmet Öz": "AR-GE Müdürü",
    ...             "Samet Söz": "Genel Direktör",
    ...             "Sedat Gün": "Proje Müdürü"}
    
Şimdi bu sözlüğe ``"Turgut Özben": "Mühendis"`` anahtar-değer çiftini
ekleyelim::

    >>> personel["Turgut Özben"] = "Mühendis"    

Sözlüğümüzün son halini görelim::
    
    >>> print(personel)

    {'Samet Söz': 'Genel Direktör', 'Mehmet Öz': 'AR-GE Müdürü', 'Turgut Özben': 
    'Mühendis', 'Sedat Gün': 'Proje Müdürü'}
    
Gördüğünüz gibi eklemek istediğimiz öğe sözlüğe eklenmiş. Ancak bu öğenin
sözlüğün en sonuna değil, sözlük içine rastgele bir şekilde yerleştirildiğine
dikkatinizi çekmek isterim. Çünkü, dediğimiz gibi, sözlükler sırasız bir veri
tipidir.   

Gelin bu konuyu daha iyi anlamak için bir örnek daha verelim. 

Önce `notlar` adında boş bir sözlük tanımlayalım::
    
    >>> notlar = {}
    
Bu sözlüğe öğrencilerin sınavdan aldıkları notları ekleyeceğiz::
    
    >>> notlar["Ahmet"] = 45
    >>> notlar["Mehmet"] = 77
    >>> notlar["Seda"] = 98
    >>> notlar["Deniz"] = 95
    >>> notlar["Ege"] = 95
    >>> notlar["Zeynep"] = 100
    
Sözlüğümüzün son halini görelim::
    
    >>> print(notlar)
    
    {'Seda': 98, 'Ege': 95, 'Mehmet': 77, 'Zeynep': 100, 'Deniz': 95, 'Ahmet': 45}
    
Bu noktada sözlüklerin önemli bir özelliğinden bahsetmemiz uygun olacak. Bir
sözlüğe değer olarak bütün veri tiplerini verebiliriz. Yani:: 

    >>> sözlük = {}
    >>> sözlük = {'a': 1}
    >>> sözlük = {'a': (1,2,3)}
    >>> sözlük = {'a': 'kardiz'}
    >>> sözlük = {'a': [1,2,3]}
    
Gördüğünüz gibi, sözlükler değer olarak her türlü veri tipini kabul ediyor. Ama
durum sözlük anahtarları açısından böyle değildir. Yani sözlüklere anahtar
olarak her veri tipini atayamayız. Bir değerin 'anahtar' olabilmesi için, o
öğenin değiştirilemeyen (*immutable*) bir veri tipi olması gerekir. Python'da
şimdiye kadar öğrendiğimiz şu veri tipleri değiştirilemeyen veri tipleridir:

#. Demetler
#. Sayılar
#. Karakter Dizileri

Şu veri tipleri ise değiştirilebilen veri tipleridir:

#. Listeler
#. Sözlükler

Dolayısıyla bir sözlüğe ancak şu veri tiplerini ekleyebiliriz:

#. Demetler
#. Sayılar
#. Karakter Dizileri

Şu kodları dikkatlice inceleyin:

Önce boş bir sözlük oluşturalım::
    
    >>> sözlük = {}
    
Bu sözlüğe anahtar olarak bir demet ekleyelim::
    
    >>> l = (1,2,3)
    >>> sözlük[l] = 'falanca'
    >>> sözlük
    
    {(1, 2, 3): 'falanca'}
    
Bir sayı ekleyelim::
    
    >>> l = 45
    >>> sözlük[l] = 'falanca'
    >>> sözlük
    
    {45: 'falanca', (1, 2, 3): 'falanca'}
    
Bir karakter dizisi ekleyelim::
    
    >>> l = 'kardiz'
    >>> sözlük[l] = 'falanca'
    >>> sözlük
    
    {'kardiz': 'falanca', 45: 'falanca', (1, 2, 3): 'falanca'}

Yukarıdakiler, değiştirilemeyen veri tipleri olduğu için sözlüklere anahtar
olarak eklenebildi. 

Bir de şunlara bakalım:

Sözlüğümüze anahtar olarak bir liste eklemeye çalışalım::
    
    >>> l = [1,2,3]
    >>> sözlük[l] = 'falanca'
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

Kümemize bir sözlük eklemeye çalışalım::
    
    >>> l = {"a": 1, "b": 2, "c": 3}
    >>> sözlük[l] = 'falanca'
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'dict'
    
Sözlüklerle çalışırken sözlüklerin bu özelliğine karşı uyanık olmalıyız.
    
Sözlük Öğeleri Üzerinde Değişiklik Yapmak
*****************************************

Sözlükler değiştirilebilir veri tipleridir. Dolayısıyla sözlükler üzerinde
rahatlıkla istediğimiz değişikliği yapabiliriz. 

Sözlükler üzerinde değişiklik yapma işlemi, biraz önce öğrendiğimiz, sözlüklere
yeni öğe ekleme işlemiyle aynıdır. Dikkatlice bakın::
    
    >>> notlar = {'Seda': 98, 'Ege': 95, 'Mehmet': 77, 
    ... 'Zeynep': 100, 'Deniz': 95, 'Ahmet': 45}

Sözlüğümüz bu. Şimdi bu sözlükteki 'Ahmet' adlı kişinin `45` olan notunu `65`
olarak değiştirelim::
    
    >>> notlar["Ahmet"] = 65
    >>> print(notlar)

    {'Seda': 98, 'Ege': 95, 'Mehmet': 77, 'Zeynep': 100, 'Deniz': 95, 'Ahmet': 65}
    
Gördüğünüz gibi Ahmet'in notu `65` olarak değişmiş...    

Sözlük Üreteçleri (*Dictionary Comprehensions*)
************************************************

Hatırlarsanız listeleri anlatırken liste üreteçleri adı bir kavramdan söz
etmiştik. Liste üreteçlerini kullanarak tek satırda ve hızlı bir şekilde
listeler oluşturabiliyorduk. Aynı şey sözlükler için de geçerlidir. Tıpkı liste
üreteçlerinde olduğu gibi, sözlük üreteçleri sayesinde tek satırda ve hızlı bir
şekilde sözlükler üretebiliriz.

Örneğin elimizde, Türkçe alfabedeki harfleri içeren `harfler` adlı şöyle bir
liste olduğunu düşünün::
    
    >>> harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
    
Amacımız bu harflerin her birine bir numara vermek. Yani nihai olarak şöyle bir
sözlük elde etmek istiyoruz::
    
    {'ğ': 8, 
     'v': 26, 
     'ş': 22, 
     'u': 24, 
     't': 23, 
     'ö': 18, 
     'ı': 10, 
     'p': 19, 
     's': 21, 
     'r': 20, 
     'ü': 25, 
     'y': 27, 
     'ç': 3, 
     'z': 28, 
     'e': 5, 
     'd': 4, 
     'g': 7, 
     'f': 6, 
     'a': 0, 
     'c': 2, 
     'b': 1, 
     'm': 15, 
     'l': 14, 
     'o': 17, 
     'n': 16, 
     'i': 11, 
     'h': 9, 
     'k': 13, 
     'j': 12}
     
Bunun için birkaç farklı yöntemden yararlanabiliriz. Örneğin::
    
    >>> sözlük = {}
    >>> for i in harfler:
    ...     sözlük[i] = harfler.index(i)
    
veya::

    >>> sözlük = {}
    >>> for i in range(len(harfler)):
    ...     sözlük[harfler[i]] = i    

İşte bu işlemleri sözlük üreteçlerini kullanarak çok daha hızlı ve pratik bir
şekilde halledebiliriz. Dikkatlice bakın::
    
    >>> sözlük = {i: harfler.index(i) for i in harfler}
    
Bir örnek daha verelim. Diyelim ki elinizde şöyle bir isim listesi var::

    isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
    
Amacınız, bu isimleri ve her bir ismin kaç harften oluştuğunu gösteren bir
sözlük elde etmek. Yani nihai olarak şöyle bir şey olsun istiyorsunuz elinizde::
    
    {'zeynep': 6, 
     'cem': 3, 
     'abdullah': 8, 
     'ahmet': 5, 
     'mehmet': 6, 
     'fırat': 5, 
     'selma': 5}   
     
İşte bu görev için de sözlük üreteçlerinden yararlanabilirsiniz::     

    >>> isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
    >>> sözlük = {i: len(i) for i in isimler}
    >>> sözlük
    
    {'zeynep': 6, 'cem': 3, 'abdullah': 8, 'ahmet': 5, 'mehmet': 6, 'fırat': 5, 'selma': 5}
    
Bildiğiniz gibi sözlükler, her biri birbirinden `:` işareti ile ayrılan birtakım
anahtar-değer çiftlerinden oluşuyor. İşte yukarıdaki sözlük üreteci yapısında
biz `:` işaretinin sol tarafına `isimler` adlı listedeki her bir öğeyi; sağ
tarafına da bu öğelerin uzunluklarını bir çırpıda ekliyoruz.

   





