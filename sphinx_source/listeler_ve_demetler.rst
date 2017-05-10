.. meta::
   :description: Bu bölümde listeler ve demetler konusunu ayrıntılı bir şekilde inceleyeceğiz.
   :keywords: python, python3, listeler, demetler, metot, append, extend, index, insert, delete, count,
              reverse, sort, pop, dir

.. highlight:: py3


************************
Listeler ve Demetler
************************

Bu bölüme gelene kadar yalnızca iki farklı veri tipi görmüştük. Bunlardan biri
karakter dizileri, öteki ise sayılardı. Ancak tabii ki Python'daki veri tipleri
yalnızca bu ikisiyle sınırlı değildir. Python'da karakter dizileri ve sayıların
dışında, başka amaçlara hizmet eden, başka veri tipleri de vardır. İşte biz bu
bölümde iki farklı veri tipi daha öğreneceğiz. Bu bölümde ele alacağımız veri
tiplerinin adı 'liste' (*list*) ve 'demet' (*tuple*).

Bu bölümde birer veri tipi olarak listeler ve demetlerden söz etmenin yanısıra
liste ve demetlerin metotlarından da bahsedeceğiz. Listelerle demetleri
öğrendikten sonra Python'daki hareket imkanınızın bir hayli genişlediğine tanık
olacaksınız.

Python programlama diline yeni başlayan biri, karakter dizilerini öğrendikten
sonra bu dilde her şeyi karakter dizileri yardımıyla halledebileceğini
zannedebilir. O yüzden yeni bir veri tipi ile karşılaştığında (örneğin listeler
veya demetler), bu yeni veri tipi ona anlamsız ve gereksizmiş gibi görünebilir.
Aslında daha önce de söylediğimiz gibi, bir programlama dilini yeni öğrenenlerin
genel sorunudur bu. Öğrenci, bir programlama dilini oluşturan minik parçaları
öğrenirken, öğrencinin zihni bu parçaların ne işine yarayacağı konusunda
şüpheyle dolar. Sanki gereksiz şeylerle vakit kaybediyormuş gibi hissedebilir.
En önemli ve en büyük programların, bu minik parçaların sistematik bir şekilde
birleştirilmesiyle ortaya çıkacak olması öğrencinin kafasına yatmayabilir.
Halbuki en karmaşık programların bile kaynak kodlarını incelediğinizde
görecekleriniz karakter dizileri, listeler, demetler, sayılar ve buna benzer
başka veri tiplerinden ibarettir. Nasıl en lezzetli yemekler birkaç basit
malzemenin bir araya gelmesi ile ortaya çıkıyorsa, en abidevi programlar da ilk
bakışta birbiriyle ilgisiz görünen çok basit parçaların incelikli bir şekilde
birleştirilmesinden oluşur.

O halde bu noktada, Python programlama diline yeni başlayan hemen herkesin
sorduğu o soruyu soralım kendimize: 'Neden farklı veri tipleri var? Bu veri
tiplerinin hepsine gerçekten ihtiyacım olacak mı?'

Bu soruyu başka bir soruyla cevaplamaya çalışalım: 'Acaba neden farklı giysi
tipleri var? Neden kot pantolon, kumaş pantolon, tişört, gömlek ve buna benzer
ayrımlara ihtiyaç duyuyoruz?' Bu sorunun cevabı çok basit: 'Çünkü farklı
durumlara farklı giysi türleri uygundur!'

Örneğin ev taşıyacaksanız, herhalde kumaş pantolon ve gömlek giymezsiniz
üzerinize. Buna benzer bir şekilde iş görüşmesine giderken de kot pantolon ve
tişört doğru bir tercih olmayabilir. İşte buna benzer sebeplerden, programlama
dillerinde de belli durumlarda belli veri tiplerini kullanmanız gerekir. Örneğin
bir durumda karakter dizilerini kullanmak uygunken, başka bir durumda listeleri
veya demetleri kullanmak daha mantıklı olabilir. Zira her veri tipinin kendine
has güçlü ve zayıf yanları vardır. Veri tiplerini ve bunların ayrıntılarını
öğrendikçe, hangi veri tipinin hangi sorun için daha kullanışlı olduğunu
kestirebilecek duruma geleceğinizden hiç kuşkunuz olmasın.

Biz bu bölümde listeleri ve demetleri olabildiğince ayrıntılı bir şekilde
inceleyeceğiz. O yüzden bu veri tiplerini incelerken konuyu birkaç farklı bölüme
ayıracağız.

Listeleri ve demetleri incelemeye listelerden başlayalım...

Listeler
***********

Giriş bölümünde de değindiğimiz gibi, listeler Python'daki veri tiplerinden
biridir. Tıpkı karakter dizileri ve sayılar gibi...

Liste Tanımlamak
====================

Listeleri tanımaya, bu veri tipini nasıl tanımlayacağımızı öğrenerek başlayalım.

Hatırlarsanız bir karakter dizisi tanımlayabilmek için şöyle bir yol
izliyorduk::

    >>> kardiz = "karakter dizisi"

Yani herhangi bir öğeyi karakter dizisi olarak tanımlayabilmek için yapmamız
gereken tek şey o öğeyi tırnak içine almaktı. Herhangi bir öğeyi (tek, çift veya
üç) tırnak içine aldığımızda karakter dizimizi tanımlamış oluyoruz. Liste
tanımlamak için de buna benzer bir şey yapıyoruz. Dikkatlice bakın::
    
    >>> liste = ["öğe1", "öğe2", "öğe3"]

Gördüğünüz gibi, liste tanımlamak da son derece kolay. Bir liste elde etmek
için, öğeleri birbirinden virgülle ayırıp, bunların hepsini köşeli parantezler
içine alıyoruz.

Karakter dizilerini anlatırken, herhangi bir nesnenin karakter dizisi olup
olmadığından emin olmak için ``type()`` fonksiyonundan yararlanabileceğimizi
söylemiştik. Eğer bir nesne ``type()`` fonksiyonuna `<class 'str'>` cevabı
veriyorsa o nesne bir karakter dizisidir. Listeler için de buna benzer bir
sorgulama yapabiliriz::
    
    >>> liste = ["öğe1", "öğe2", "öğe3"]
    >>> type(liste)
    
    <class 'list'>

Bu çıktıdan anlıyoruz ki, liste veri tipi ``type()`` fonksiyonuna `<class
'list'>` cevabı veriyor. Dolayısıyla, eğer bir nesne ``type()`` fonksiyonuna
`<class 'list'>` cevabı veriyorsa o nesnenin bir liste olduğunu rahatlıkla
söyleyebiliriz.

Yukarıda tanımladığımız `liste` adlı listeye baktığımızda dikkatimizi bir şey
çekiyor olmalı. Bu listeye şöyle bir baktığımızda, aslında bu listenin, içinde
üç adet karakter dizisi barındırdığını görüyoruz. Gerçekten de listeler, bir
veya daha fazla veri tipini içinde barındıran kapsayıcı bir veri tipidir. Mesela
şu listeye bir bakalım::
    
    >>> liste = ["Ahmet", "Mehmet", 23, 65, 3.2]

Gördüğünüz gibi, liste içinde hem karakter dizileri (`"Ahmet"`, `"Mehmet"`), hem
de sayılar (`23`, `65`, `3.2`) var.

Dahası, listelerin içinde başka listeler de bulunabilir::

    >>> liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]

Bu `liste` adlı değişkenin tipini sorgularsak şöyle bir çıktı alacağımızı
biliyorsunuz::
    
    >>> type(liste)
    
    <class 'list'>

Bir de şunu deneyelim::

    for öğe in liste:
        print("{} adlı öğenin veri tipi: {}".format(öğe, type(öğe)))

Bu kodları çalıştırdığımızda da şöyle bir çıktı alıyoruz::

    Ali adlı öğenin veri tipi: <class 'str'>
    Veli adlı öğenin veri tipi: <class 'str'>
    ['Ayşe', 'Nazan', 'Zeynep'] adlı öğenin veri tipi: <class 'list'>
    34 adlı öğenin veri tipi: <class 'int'>
    65 adlı öğenin veri tipi: <class 'int'>
    33 adlı öğenin veri tipi: <class 'int'>
    5.6 adlı öğenin veri tipi: <class 'float'>

Bu kodlar bize şunu gösteriyor: Farklı öğeleri bir araya getirip bunları köşeli
parantezler içine alırsak 'liste' adlı veri tipini oluşturmuş oluyoruz. Bu
listenin öğeleri farklı veri tiplerine ait olabilir. Yukarıdaki kodların da
gösterdiği gibi, liste içinde yer alan `"Ali"` ve `"Veli"` öğeleri birer
karakter dizisi; `['Ayşe', 'Nazan', 'Zeynep']` adlı öğe bir liste; `34`, `65` ve
`33` öğeleri birer tam sayı; `5.6` öğesi ise bir kayan noktalı sayıdır. İşte
farklı veri tiplerine ait bu öğelerin hepsi bir araya gelerek liste denen veri
tipini oluşturuyor. Yukarıdaki örnekten de gördüğünüz gibi, bir listenin içinde
başka bir liste de yer alabiliyor. Örneğin burada listemizin öğelerinden biri,
`['Ayşe', 'Nazan', 'Zeynep']` adlı başka bir listedir.

Hatırlarsanız karakter dizilerinin belirleyici özelliği tırnak işaretleri idi.
Yukarıdaki örneklerden de gördüğünüz gibi listelerin belirleyici özelliği de
köşeli parantezlerdir. Mesela::
    
    >>> karakter = ""

Bu boş bir karakter dizisidir. Şu ise boş bir liste::

    >>> liste = []

Tıpkı karakter dizilerinde olduğu gibi, listelerle de iki şekilde
karşılaşabilirsiniz:

    #. Listeyi kendiniz tanımlamış olabilirsiniz.
    
    #. Liste size başka bir kaynaktan gelmiş olabilir. 

Yukarıdaki örneklerde bir listeyi kendimizin nasıl tanımlayacağımızı öğrendik.
Peki listeler bize başka hangi kaynaktan gelebilir?

Hatırlarsanız karakter dizilerinin metotlarını sıralamak için ``dir()`` adlı bir
fonksiyondan yararlanmıştık.

Mesela karakter dizilerinin bize hangi metotları sunduğunu görmek için bu
fonksiyonu şöyle kullanmıştık::

    >>> dir(str)

Bu komut bize şu çıktıyı vermişti::

    ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
    '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
    '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
    '__subclasshook__', 'capitalize', 'center', 'count', 'encode', 'endswith',
    'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
    'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
    'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
    'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
    'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
    'title', 'translate', 'upper', 'zfill']

Artık bu çıktı size çok daha anlamlı geliyor olmalı. Gördüğünüz gibi çıktımız
köşeli parantezler arasında yer alıyor. Yani aslında yukarıdaki çıktı bir liste.
Dilerseniz bunu nasıl teyit edebileceğinizi biliyorsunuz::
    
    >>> komut = dir(str)
    >>> type(komut)
    
    <class 'list'>

Gördüğünüz gibi, tıpkı ``input()`` fonksiyonundan gelen verinin bir karakter
dizisi olması gibi, ``dir()`` fonksiyonundan gelen veri tipi de bir listedir.

``dir()`` fonksiyonu dışında, başka bir şeyin daha bize liste verdiğini
biliyoruz. Bu şey, karakter dizilerinin ``split()`` adlı metodudur::

    >>> kardiz = "İstanbul Büyükşehir Belediyesi"
    >>> kardiz.split()
    
    ['İstanbul', 'Büyükşehir', 'Belediyesi']

Görüyorsunuz, ``split()`` metodunun çıktısı da köşeli parantezler içinde yer
alıyor. Demek ki bu çıktı da bir listedir.

Peki bir fonksiyonun bize karakter dizisi mi, liste mi yoksa başka bir veri tipi
mi verdiğini bilmenin ne faydası var?

Her zaman söylediğimiz gibi, Python'da o anda elinizde olan verinin tipini
bilmeniz son derece önemlidir. Aksi halde o veriyi nasıl evirip çevireceğinizi,
o veriyle neler yapabileceğinizi bilemezsiniz. Mesela 'İstanbul Büyükşehir
Belediyesi' ifadesini ele alalım. Bu ifadeyle ilgili size şöyle bir soru
sorduğumu düşünün: 'Acaba bu ifadenin ilk harfini nasıl alırız?'

Eğer bu ifade size ``input()`` fonksiyonundan gelmişse, yani bir karakter
dizisiyse uygulayacağınız yöntem farklı, ``split()`` metoduyla gelmişse, yani
liste ise uygulayacağınız yöntem farklı olacaktır.

Eğer bu ifade bir karakter dizisi ise ilk harfi şu şekilde alabilirsiniz::

    >>> kardiz = "İstanbul Büyükşehir Belediyesi"
    >>> kardiz[0]
    
    'İ'

Ama eğer bu ifade bir liste ise yukarıdaki yöntem size farklı bir sonuç verir::

    >>> liste = kardiz.split()
    >>> liste[0]
    
    'İstanbul'
    
Çünkü `"İstanbul Büyükşehir Belediyesi"` adlı karakter dizisinin ilk öğesi `"İ"`
karakteridir, ama `['İstanbul', 'Büyükşehir', 'Belediyesi']` adlı listenin ilk
öğesi `"İ"` karakteri değil, `"İstanbul"` kelimesidir.

Gördüğünüz gibi, bir nesnenin hangi veri tipine ait olduğunu bilmek o nesneyle
neleri nasıl yapabileceğimizi doğrudan etkiliyor. O yüzden programlama
çalışmalarınız esnasında veri tiplerine karşı her zaman uyanık olmalısınız.

.. note:: Python'da bir nesnenin hangi veri tipine ait olduğunu bilmenin neden
 bu kadar önemli olduğunu gerçek bir örnek üzerinde görmek isterseniz
 `istihza.com/forum/viewtopic.php?f=43&t=62
 <http://www.istihza.com/forum/viewtopic.php?f=43&t=62>`_ adresindeki tartışmayı
 inceleyebilirsiniz.

Her ne kadar karakter dizileri ve listeler iki farklı veri tipi olsa ve bu iki
veri tipinin birbirinden çok farklı yönleri ve yetenekleri olsa da, bu iki veri
tipi arasında önemli benzerlikler de vardır. Örneğin karakter dizilerini
işlerken öğrendiğimiz pek çok fonksiyonu listelerle birlikte de
kullanabilirsiniz. Mesela karakter dizilerini incelerken öğrendiğimiz ``len()``
fonksiyonu listelerin boyutunu hesaplamada da kullanılabilir::
    
    >>> diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
    >>> len(diller)
    
    5

Karakter dizileri karakterlerden oluşan bir veri tipi olduğu için ``len()``
fonksiyonu karakter dizisi içindeki karakterlerin sayısını veriyor. Listeler ise
başka veri tiplerini bir araya toplayan bir veri tipi olduğu için ``len()``
fonksiyonu liste içindeki veri tiplerinin sayısını söylüyor.

``len()`` fonksiyonu dışında, ``range()`` fonksiyonuyla listeleri de birlikte
kullanabilirsiniz. Mesela herhangi bir kaynaktan size şunlar gibi iki öğeli
listeler geliyor olabilir::
    
    [0, 10]
    [6, 60]
    [12, 54]
    [67, 99]

Bu iki öğeli listeleri tek bir liste içinde topladığımızı düşünürsek şöyle bir
kod yazabiliriz::
    
    sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
    
    for i in sayılar:
        print(*range(*i))

Eğer ilk bakışta bu kod gözünüze anlaşılmaz göründüyse bu kodu parçalara
ayırarak inceleyebilirsiniz.

Burada öncelikle bir ``for`` döngüsü oluşturduk. Bu sayede `sayılar` adlı
listedeki öğelerin üzerinden tek tek geçebileceğiz. Eğer döngü içinde sadece
öğeleri ekrana yazdırıyor olsaydık şöyle bir kodumuz olacaktı::
    
    for i in sayılar:
        print(i)

Bu kod bize şöyle bir çıktı verecektir::

    [0, 10]
    [6, 60]
    [12, 54]
    [67, 99]

``range()`` fonksiyonunun nasıl kullanıldığını hatırlıyorsunuz. Yukarıdaki
listelerde görünen ilk sayılar ``range()`` fonksiyonunun ilk parametresi, ikinci
sayılar ise ikinci parametresi olacak. Yani her döngüde şöyle bir şey elde
etmemiz gerekiyor::
    
    range(0, 10)
    range(6, 60)
    range(12, 54)
    range(67, 99)

Aslında kodlarımızı şöyle yazarak yukarıdaki çıktıyı elde edebilirdik::

    sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
    
    for i in sayılar:
        print(range(i[0], i[1]))

Yukarıdaki açıklamalarda gördüğünüz gibi, `i` değişkeninin çıktısı ikişer öğeli
bir liste oluyor. İşte burada yaptığımız şey, bu ikişer öğeli listelerin ilk
öğesini (``i[0]``) ``range()`` fonksiyonunun ilk parametresi, ikinci öğesini
(``i[1]``) ise ``range()`` fonksiyonunun ikinci parametresi olarak atamaktan
ibaret. Ancak ilk derslerimizden hatırlayacağınız gibi, bunu yapmanın daha kısa
bir yolu var. Bildiğiniz gibi, öğelerden oluşan dizileri ayrıştırmak için yıldız
işaretinden yararlanabiliyoruz. Dolayısıyla yukarıdaki kodları şöyle yazmak daha
pratik olabilir::
    
    sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]
    
    for i in sayılar:
        print(range(*i))

Gördüğünüz gibi, `i` değişkeninin soluna bir yıldız ekleyerek bu değişken
içindeki değerleri ayrıştırdık ve şöyle bir çıktı elde ettik::
    
    range(0, 10)
    range(6, 60)
    range(12, 54)
    range(67, 99)

Hatırlarsanız, ``range(0, 10)`` gibi bir kod yazdığımızda Python bize `0` ile
`10` arasındaki sayıları doğrudan göstermiyordu. Aralıktaki sayıları görmek için
``range()`` fonksiyonunun çıktısını bir döngü içine almalıyız::
    
    for i in range(0, 10):
        print(i)

``range(0, 10)`` çıktısını görmek için döngü kurmak yerine yine yıldız
işaretinden yararlanabiliyoruz. Örneğin::
    
    >>> print(*range(0, 10))
    
    0 1 2 3 4 5 6 7 8 9

Aynı şeyi yukarıdaki kodlara da uygularsak şöyle bir şey elde ederiz::

    sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]

    for i in sayılar:
        print(*range(*i))

Gördüğünüz gibi, yıldız işaretini hem `i` değişkenine, hem de ``range()``
fonksiyonuna ayrı ayrı uygulayarak istediğimiz sonucu elde ettik.

Bu arada, yukarıdaki örnek bize listeler hakkında önemli bir bilgi de verdi.
Karakter dizilerinin öğelerine erişmek için nasıl ``kardiz[öğe_sırası]`` gibi
bir formülden yararlanıyorsak, listelerin öğelerine erişmek için de aynı şekilde
``liste[öğe_sırası]`` gibi bir formülden yararlanabiliyoruz.

Listelerin öğelerine nasıl ulaşacağımızın ayrıntılarını biraz sonra göreceğiz.
Ama biz şimdi listelere ilişkin önemli bir fonksiyonu inceleyerek yolumuza devam
edelim.

list() Fonksiyonu
=====================

Yukarıdaki örneklerden de gördüğünüz gibi liste oluşturmak için öğeleri
belirleyip bunları köşeli parantezler içine almamız yeterli oluyor. Bu yöntemin
dışında, liste oluşturmanın bir yöntemi daha bulunur. Mesela elimizde şöyle bir
karakter dizisi olduğunu düşünelim::
    
    >>> alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

Sorumuz şu olsun: 'Acaba bu karakter dizisini listeye nasıl çeviririz?'

Karakter dizilerini anlatırken ``split()`` adlı bir metottan söz etmiştik. Bu
metot karakter dizilerini belli bir ölçüte göre bölmemizi sağlıyordu.
``split()`` metoduyla elde edilen verinin bir liste olduğunu biliyorsunuz.
Örneğin::
    
    >>> isimler = "ahmet mehmet cem"
    
    >>> isimler.split()

    ['ahmet', 'mehmet', 'cem']

Ancak ``split()`` metodunun bir karakter dizisini bölüp bize bir liste
verebilmesi için karakter dizisinin belli bir ölçüte göre bölünebilir durumda
olması gerekiyor. Mesela yukarıdaki `isimler` adlı karakter dizisi belli bir
ölçüte göre bölünebilir durumdadır. Neden? Çünkü karakter dizisi içindeki her
parça arasında bir boşluk karakteri var. Dolayısıyla ``split()`` metodu bu
karakter dizisini boşluklardan bölebiliyor. Aynı şey şu karakter dizisi için de
geçerlidir::
    
    >>> isimler = "elma, armut, çilek"

Bu karakter dizisini oluşturan her bir parça arasında bir adet virgül ve bir
adet boşluk karakteri var. Dolayısıyla biz bu karakter dizisini ``split()``
metodunu kullanarak "virgül + boşluk karakteri" ölçütüne göre bölebiliriz::
    
    >>> isimler.split(", ")
    
    ['elma', 'armut', 'çilek']

Ancak bölümün başında tanımladığımız `alfabe` adlı karakter dizisi biraz
farklıdır::
    
    >>> alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

Gördüğünüz gibi, bu karakter dizisi tek bir parçadan oluşuyor. Dolayısıyla bu
karakter dizisini öğelerine bölmemizi sağlayacak bir ölçüt yok. Yani bu karakter
dizisini şu şekilde bölemeyiz::
    
    >>> alfabe.split()
    
    ['abcçdefgğhıijklmnoöprsştuüvyz']

Elbette bu karakter dizisini isterseniz farklı şekillerde bölebilirsiniz.
Mesela::
    
    >>> alfabe.split("i")
    
    ['abcçdefgğhı', 'jklmnoöprsştuüvyz']

Gördüğünüz gibi, biz burada `alfabe` karakter dizisini "i" harfinden bölebildik.
Ama istediğimiz şey bu değil. Biz aslında şöyle bir çıktı elde etmek istiyoruz::
    
    ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 
     'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 
     'v', 'y', 'z']

Yani bizim amacımız, `alfabe` karakter dizisi içindeki her bir öğeyi birbirinden
ayırmak. İşte Türk alfabesindeki harflerden oluşan bu karakter dizisini,
``list()`` adlı bir fonksiyondan yararlanarak istediğimiz şekilde bölebiliriz::
    
    >>> harf_listesi = list(alfabe)
    >>> print(harf_listesi)
    
    ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 
     'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 
     'v', 'y', 'z']

Böylece ``list()`` fonksiyonu yardımıyla bu karakter dizisini tek hamlede
listeye çevirmiş olduk.

Peki bir karakter dizisini neden listeye çevirme ihtiyacı duyarız? Şu anda
listelerle ilgili pek çok şeyi henüz bilmediğimiz için ilk bakışta bu çevirme
işlemi gözünüze gereksizmiş gibi görünebilir, ama ilerleyen zamanda sizin de
göreceğiniz gibi, bazı durumlarda listeleri manipüle etmek karakter dizilerini
manipüle etmeye kıyasla çok daha kolaydır. O yüzden kimi zaman karakter
dizilerini listeye çevirmek durumunda kalabilirsiniz.

``list()`` fonksiyonunun yaptığı işi, daha önce öğrendiğimiz ``str()``,
``int()`` ve ``float()`` fonksiyonlarının yaptığı işle kıyaslayabilirsiniz.
``list()`` fonksiyonu da tıpkı ``str()``, ``int()`` ve ``float()`` fonksiyonları
gibi bir dönüştürme fonksiyonudur. Örneğin ``int()`` fonksiyonunu kullanarak
sayı değerli karakter dizilerini sayıya dönüştürebiliyoruz::
    
    >>> k = "123"
    >>> int(k)
    
    123

Bu dönüştürme işlemi sayesinde sayılar üzerinde aritmetik işlem yapma imkanımız
olabiliyor. İşte ``list()`` fonksiyonu da buna benzer bir amaca hizmet eder.
Mesela ``input()`` fonksiyonundan gelen bir karakter dizisi ile toplama çıkarma
yapabilmek için nasıl bu karakter dizisini önce sayıya dönüştürmemiz
gerekiyorsa, bazı durumlarda bu karakter dizisini (veya başka veri tiplerini)
listeye çevirmemiz de gerekebilir. Böyle bir durumda ``list()`` fonksiyonunu
kullanarak farklı veri tiplerini rahatlıkla listeye çevirebiliriz.

Yukarıdaki işlevlerinin dışında, ``list()`` fonksiyonu boş bir liste oluşturmak
için de kullanılabilir::

    >>> li = list()
    >>> print(li)
    
    []

Yukarıdaki kodlardan gördüğünüz gibi, boş bir liste oluşturmak için ``liste =
[]`` koduna alternatif olarak ``list()`` fonksiyonundan da yararlanabilirsiniz.

``list()`` fonksiyonunun önemli bir görevi de ``range()`` fonksiyonunun, sayı
aralığını ekrana basmasını sağlamaktır. Bildiğiniz gibi, ``range()`` fonksiyonu
tek başına bir sayı aralığını ekrana dökmez. Bu fonksiyon bize yalnızca şöyle
bir çıktı verir::
    
    >>> range(10)
    
    range(0, 10)

Bu sayı aralığını ekrana dökmek için ``range()`` fonksiyonu üzerinde bir ``for``
döngüsü kurmamız gerekir::
    
    >>> for i in range(10):
    ...     print(i)
    ...
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

Bu bölümde verdiğimiz örneklerde aynı işi şöyle de yapabileceğimizi
öğrenmiştik::
    
    >>> print(*range(10))
    
    0 1 2 3 4 5 6 7 8 9

Bu görevi yerine getirmenin üçüncü bir yolu da ``list()`` fonksiyonunu
kullanmaktır::
    
    >>> list(range(10))
    
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Aslında burada yaptığımız şey ``range(10)`` ifadesini bir listeye dönüştürmekten
ibarettir. Burada `range` türünde bir veriyi `list` türünde bir veriye
dönüştürüyoruz::
    
    >>> type(range(10))
    
    <class 'range'>
    
    >>> li = list(range(10))
    >>> type(li)
    
    <class 'list'>

Gördüğünüz gibi, yukarıdaki üç yöntem de aralıktaki sayıları ekrana döküyor.
Yalnız dikkat ederseniz bu üç yöntemin çıktıları aslında görünüş olarak
birbirlerinden ince farklarla ayrılıyor. Yazdığınız programda nasıl bir çıktıya
ihtiyacınız olduğuna bağlı olarak yukarıdaki yöntemlerden herhangi birini tercih
edebilirsiniz.

Böylece Python'da listelerin ne olduğunu ve bu veri tipinin nasıl
oluşturulacağını öğrenmiş olduk. O halde bir adım daha atarak listelerin başka
özelliklerine değinelim.

Listelerin Öğelerine Erişmek
===============================

Tıpkı karakter dizilerinde olduğu gibi, listelerde de her öğenin bir sırası
vardır. Hatırlarsanız karakter dizilerinin öğelerine şu şekilde ulaşıyorduk::
    
    >>> kardiz = "python"
    >>> kardiz[0]
    
    'p'

Bu bölümdeki birkaç örnekte de gördüğünüz gibi, listelerin öğelerine ulaşırken
de aynı yöntemi kullanabiliyoruz::
    
    >>> meyveler = ["elma", "armut", "çilek", "kiraz"]
    >>> meyveler[0]
    
    'elma'

Yalnız yöntem aynı olsa da yukarıdaki iki çıktı arasında bazı farklar olduğunu
da gözden kaçırmayın. Bir karakter dizisinin `0.` öğesini aldığımızda o karakter
dizisinin ilk karakterini almış oluyoruz. Bir listenin `0.` öğesini aldığımızda
ise o listenin ilk öğesini almış oluyoruz.

Sayma yöntemi olarak ise karakter dizileri ve listelerde aynı mantık geçerli.
Hem listelerde hem de karakter dizilerinde Python saymaya `0`'dan başlıyor. Yani
karakter dizilerinde olduğu gibi, listelerde de ilk öğenin sırası `0`.

Eğer bu listenin öğelerinin hepsine tek tek ulaşmak isterseniz ``for``
döngüsünden yararlanabilirsiniz::

    meyveler = ["elma", "armut", "çilek", "kiraz"]

    for meyve in meyveler:
        print(meyve)

Bu listedeki öğeleri numaralandırmak da mümkün::

    meyveler = ["elma", "armut", "çilek", "kiraz"]

    for öğe_sırası in range(len(meyveler)):
        print("{}. {}".format(öğe_sırası, meyveler[öğe_sırası]))

...veya ``enumerate()`` fonksiyonunu kullanarak şöyle bir şey de yazabiliriz::

    for sıra, öğe in enumerate(meyveler, 1):
        print("{}. {}".format(sıra, öğe))

Dediğimiz gibi, liste öğelerine ulaşmak için kullandığımız yöntem, karakter
dizilerinin öğelerine ulaşmak için kullandığımız yöntemle aynı. Aslında karakter
dizileri ile listeler arasındaki benzerlik bununla sınırlı değildir.
Benzerlikleri birkaç örnek üzerinde gösterelim::
    
    >>> meyveler = ["elma", "armut", "çilek", "kiraz"]
    >>> meyveler[-1]
    
    'kiraz'

Karakter dizilerinde olduğu gibi, öğe sırasını eksi değerli bir sayı
yaptığımızda liste öğeleri sondan başa doğru okunuyor. Dolayısıyla
``meyveler[-1]`` komutu bize `meyveler` adlı listenin son öğesini veriyor.

::

    >>> meyveler[0:2]
    
    ['elma', 'armut']

Karakter dizileri konusunu işlerken öğrendiğimiz dilimleme yöntemi listeler için
de aynen geçerlidir. Orada öğrendiğimiz dilimleme kurallarını listelere de
uygulayabiliyoruz. Örneğin liste öğelerini ters çevirmek için şöyle bir kod
yazabiliyoruz::

    >>> meyveler[::-1]

    ['kiraz', 'çilek', 'armut', 'elma']

Bu bölümün başında da söylediğimiz gibi, liste adlı veri tipi, içinde başka bir
liste de barındırabilir. Buna şöyle bir örnek vermiştik::
    
    >>> liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]

Bu listedeki öğeler şunlardır::

    Ali
    Veli
    ['Ayşe', 'Nazan', 'Zeynep']
    34
    65
    33
    5.6

Gördüğünüz gibi, bu liste içinde `['Ayşe', 'Nazan', 'Zeynep']` gibi bir liste
daha var. Bu liste ana listenin öğelerinden biridir ve bu da öteki öğeler gibi
tek öğelik bir yer kaplar. Yani::
    
    >>> len(liste)
    
    7

Bu çıktıdan anlıyoruz ki, listemiz toplam `7` öğeden oluşuyor. Listenin `2.`
sırasında yer alan listenin kendisi üç öğeden oluştuğu halde bu öğe ana liste
içinde sadece tek öğelik bir yer kaplıyor. Yani `2.` sıradaki listenin öğeleri
tek tek sayılmıyor. Peki böyle bir liste içindeki gömülü listenin öğelerini elde
etmek istersek ne yapacağız? Yani mesela içe geçmiş listenin tamamını değil de,
örneğin sadece `"Ayşe"` öğesini almak istersek ne yapmamız gerekiyor? Dikkatlice
bakın::
    
    >>> liste[2][0]
    
    'Ayşe'
    
"Nazan" öğesini almak için::

    >>> liste[2][1]
    
    'Nazan'

"Zeynep" öğesini almak için::

    >>> liste[2][2]
    
    'Zeynep'
    
Gördüğünüz gibi, iç içe geçmiş listelerin öğelerini almak oldukça basit.
Yapmamız gereken tek şey, gömülü listenin önce ana listedeki konumunu, ardından
da almak istediğimiz öğenin gömülü listedeki konumunu belirtmektir.

İstersek gömülü listeyi ayrı bir liste olarak da alabiliriz::

    >>> yeni_liste = liste[2]
    >>> yeni_liste
    
    ['Ayşe', 'Nazan', 'Zeynep']
    
Böylece bu listenin öğelerine normal bir şekilde ulaşabiliriz::

    >>> yeni_liste[0]
    
    'Ayşe'
    
    >>> yeni_liste[1]
    
    'Nazan'
    
    >>> yeni_liste[2]
    
    'Zeynep'

Eğer bir listenin öğelerine erişmeye çalışırken, varolmayan bir sıra sayısı
belirtirseniz Python size bir hata mesajı gösterecektir::
    
    >>> liste = range(10)
    >>> print(len(liste))
    
    10

Burada ``range()`` fonksiyonundan yararlanarak `10` öğeli bir liste tanımladık.
Bu listenin son öğesinin şu formüle göre bulunabileceğini karakter dizileri
konusundan hatırlıyor olmalısınız::
    
    >>> liste[len(liste)-1]
    
    9

Demek ki bu listenin son öğesi `9` sayısı imiş... Bir de şunu deneyelim::

    >>> liste[10]
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: range object index out of range

Gördüğünüz gibi, listemizde `10.` öğe diye bir şey olmadığı için Python bize
`IndexError` tipinde bir hata mesajı gösteriyor. Çünkü bu listenin son öğesinin
sırası ``len(liste)-1``, yani `9`'dur.

Listelerin Öğelerini Değiştirmek
==================================

Hatırlarsanız karakter dizilerinden söz ederken bunların değiştirilemez
(*immutable*) bir veri tipi olduğunu söylemiştik. Bu özellikten ötürü, bir
karakter dizisi üzerinde değişiklik yapmak istediğimizde o karakter dizisini
yeniden oluşturuyoruz. Örneğin::
    
    >>> kardiz = "istihza"
    >>> kardiz = "İ" + kardiz[1:]
    >>> kardiz

    'İstihza'

Listeler ise değiştirilebilen (*mutable*) bir veri tipidir. Dolayısıyla listeler
üzerinde doğrudan değişiklik yapabiliriz. Bir liste üzerinde değişiklik
yapabilmek için o listeyi yeniden tanımlamamıza gerek yok. Şu örneği dikkatlice
inceleyin::
    
    >>> renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
    >>> print(renkler)
    
    ['kırmızı', 'sarı', 'mavi', 'yeşil', 'beyaz']
    
    >>> renkler[0] = "siyah"
    >>> print(renkler)
    
    ['siyah', 'sarı', 'mavi', 'yeşil', 'beyaz']

Liste öğelerini nasıl değiştirdiğimize çok dikkat edin. Yukarıdaki örnekte
`renkler` adlı listenin `0.` öğesini değiştirmek istiyoruz. Bunun için şöyle bir
formül kullandık::
    
    renkler[öğe_sırası] = yeni_öğe

Örnek olması açısından, aynı listenin 2. sırasındaki `"mavi"` adlı öğeyi `"mor"`
yapalım bir de::
    
    >>> renkler[2] = "mor"
    >>> print(renkler)
    
    ['siyah', 'sarı', 'mor', 'yeşil', 'beyaz']

Gördüğünüz gibi, listeler üzerinde değişiklik yapmak son derece kolay. Sırf bu
özellik bile, neden bazı durumlarda listelerin karakter dizileri yerine tercih
edilebileceğini gösterecek güçtedir.

Liste öğelerini değiştirmeye çalışırken, eğer var olmayan bir sıra numarasına
atıfta bulunursanız Python size ``IndexError`` tipinde bir hata mesajı
gösterecektir::
    
    >>> renkler[10] = "pembe"

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list assignment index out of range

Sıra numaralarını kullanarak listeler üzerinde daha ilginç işlemler de
yapabilirsiniz. Mesela şu örneğe bakın::
    
    >>> liste = [1, 2, 3]
    >>> liste[0:len(liste)] = 5, 6, 7
    >>> print(liste)
    
    [5, 6, 7]

Burada `liste` adlı listenin bütün öğelerini bir çırpıda değiştirdik. Peki bunu
nasıl yaptık?

Yukarıdaki örneği şu şekilde yazarsak biraz daha açıklayıcı olabilir::

    >>> liste[0:3] = 5, 6, 7

Bu kodlarla yaptığımız şey, listenin `0.` ve `3.` öğesi arasında kalan bütün
öğelerin yerine `5`, `6` ve `7` öğelerini yerleştirmekten ibarettir.

Karakter dizilerinden hatırlayacağınız gibi, eğer sıra numarası bir karakter
dizisinin ilk öğesine karşılık geliyorsa o sıra numarasını belirtmeyebiliriz.
Aynı şekilde eğer sıra numarası bir karakter dizisinin son öğesine karşılık
geliyorsa o sıra numarasını da belirtmeyebiliriz. Bu kural listeler için de
geçerlidir. Dolayısıyla yukarıdaki örneği şöyle de yazabilirdik::
    
    >>> liste[:] = 5, 6, 7

Sıra numaralarını kullanarak gerçekten son derece enteresan işlemler
yapabilirsiniz. Sıra numaraları ile neler yapabileceğinizi görmek için kendi
kendinize ve hayal gücünüzü zorlayarak bazı denemeler yapmanızı tavsiye ederim.

Listeye Öğe Eklemek
======================

Listeler büyüyüp küçülebilen bir veri tipidir. Yani Python'da bir listeye
istediğiniz kadar öğe ekleyebilirsiniz. Diyelim ki elimizde şöyle bir liste
var::
    
    >>> liste = [2, 4, 5, 7]

Bu listeye yeni bir öğe ekleyebilmek için şöyle bir kod yazabiliriz::

    >>> liste + [8]
    
    [2, 4, 5, 7, 8]
    
Bu örnek, bize listeler hakkında önemli bir bilgi veriyor. Python'da `+` işareti
kullanarak bir listeye öğe ekleyecekseniz, eklediğiniz öğenin de liste olması
gerekiyor. Mesela bir listeye doğrudan karakter dizilerini veya sayıları
ekleyemezsiniz::
    
    >>> liste + 8
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate list (not "int") to list
    
    >>> liste + "8"
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate list (not "str") to list

Listelere `+` işareti ile ekleyeceğiniz öğelerin de bir liste olması gerekiyor.
Aksi halde Python bize bir hata mesajı gösteriyor.

Listeleri Birleştirmek
=========================

Bazı durumlarda elinize farklı kaynaklardan farklı listeler gelebilir. Böyle bir
durumda bu farklı listeleri tek bir liste halinde birleştirmeniz gerekebilir.
Tıpkı karakter dizilerinde olduğu gibi, listelerde de birleştirme işlemleri için
`+` işlecinden yararlanabilirsiniz.

Diyelim ki elimizde şöyle iki adet liste var::

    >>> derlenen_diller = ["C", "C++", "C#", "Java"]
    >>> yorumlanan_diller = ["Python", "Perl", "Ruby"]

Bu iki farklı listeyi tek bir liste haline getirmek için şöyle bir kod
yazabiliriz::
    
    >>> programlama_dilleri = derlenen_diller + yorumlanan_diller
    
    ['C', 'C++', 'C#', 'Java', 'Python', 'Perl', 'Ruby']
    
Bu işlemin sonucunu görelim::

    >>> print(programlama_dilleri)

Gördüğünüz gibi, `derlenen_diller` ve `yorumlanan_diller` adlı listelerin
öğelerini `programlama_dilleri` adlı tek bir liste içinde topladık.

Programcılık maceranız boyunca listeleri birleştirmenizi gerektiren pek çok
farklı durumla karşılaşabilirsiniz. Örneğin şöyle bir durum düşünün: Diyelim ki
kullanıcı tarafından girilen sayıların ortalamasını hesaplayan bir program
yazmak istiyorsunuz. Bunun için şöyle bir kod yazabilirsiniz::
    
    sayılar = 0

    for i in range(10):
        sayılar += int(input("not: "))

    print(sayılar/10)

Bu program kullanıcının `10` adet sayı girmesine izin verip, program çıkışında,
girilen sayıların ortalamasını verecektir.

Peki girilen sayıların ortalaması ile birlikte, hangi sayıların girildiğini de
göstermek isterseniz nasıl bir kod yazarsınız?

Eğer böyle bir şeyi karakter dizileri ile yazmaya kalkışırsanız epey eziyet
çekersiniz. Ama şöyle bir kod yardımıyla istediğiniz şeyi basit bir şekilde elde
edebilirsiniz::
    
    sayılar = 0
    notlar = []

    for i in range(10):
        veri = int(input("{}. not: ".format(i+1)))
        sayılar += veri
        notlar += [veri]

    print("Girdiğiniz notlar: ", *notlar)
    print("Not ortalamanız: ", sayılar/10)

Burada kullanıcıdan gelen verileri her döngüde tek tek `notlar` adlı listeye
gönderiyoruz. Böylece programın sonunda, kullanıcıdan gelen veriler bir liste
halinde elimizde bulunmuş oluyor.

Bu arada, yukarıdaki kodlarda dikkatinizi bir şey çekmiş olmalı. Kullanıcıdan
gelen verileri `notlar` adlı listeye gönderirken şöyle bir kod yazdık::
    
    notlar += [veri]

Buradaki ``[veri]`` ifadesine dikkat edin. Bu kod yardımıyla kullanıcıdan gelen
`veri` adlı değişkeni liste haline getiriyoruz. Bu yöntem bizim için yeni bir
şey. Peki neden burada ``list()`` fonksiyonundan yararlanmadık?

Bunu anlamak için ``list()`` fonksiyonunun çalışma mantığını anlamamız
gerekiyor.

Elinizde şöyle bir karakter dizisi olduğunu düşünün::

    >>> alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

Diyelim ki siz bu karakter dizisindeki bütün öğeleri tek tek bir listeye atmak
istiyorsunuz. Bu iş için ``list()`` fonksiyonunu kullanabileceğimizi daha önce
söylemiştik::
    
    >>> liste = list(alfabe)

Peki ``list()`` fonksiyonu bu karakter dizisinin öğelerini listeye atarken nasıl
bir yöntem izliyor?

Aslında ``list()`` fonksiyonunun yaptığı iş şuna eşdeğerdir::

    liste = []
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

    for harf in alfabe:
        liste += harf

    print(liste)

``list()`` fonksiyonu da tam olarak böyle çalışır. Yani bir karakter dizisi
üzerinde döngü kurarak, o karakter dizisinin her bir öğesini tek tek bir listeye
atar.

``for`` döngülerini işlerken, bu döngünün sayılar üzerinde çalışmayacağını
söylemiştik. Çünkü sayılar, karakter dizilerinin aksine, üzerinde döngü
kurulabilen bir veri tipi değildir. Bunu bir örnek üzerinde tekrar görelim::
    
    >>> for i in 12345:
    ...     print(i)
    ...

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not iterable

Gördüğünüz gibi, `12345` sayısı üzerinde döngü kuramıyoruz. Aynı hata mesajını
``list()`` fonksiyonunda da görürsünüz::
    
    >>> list(12345)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not iterable

Dediğimiz gibi, tıpkı ``for`` döngüsünde olduğu gibi, ``list()`` fonksiyonu da
ancak, üzerinde döngü kurulabilen nesneler üzerinde çalışabilir. Mesela::
    
    >>> list("12345")
    
    ['1', '2', '3', '4', '5']
        
Bu bilgilerin ışığında, yukarıda yazdığımız kodların şu şekilde yazılması
halinde Python'ın bize hata mesajı göstereceğini söyleyebiliriz::
    
    notlar = []
    
    for i in range(10):
        veri = int(input("{}. not: ".format(i+1)))
        notlar += list(veri)

    print("Girdiğiniz notlar: ", *notlar)

Kullanıcıdan gelen `veri` değerini ``int()`` fonksiyonuyla sayıya
dönüştürdüğümüz için ve sayılar da üzerinde döngü kurulabilen bir veri tipi
olmadığı için ``list()`` fonksiyonuna parametre olarak atanamaz.

Peki kullanıcıdan gelen `veri` değerini sayıya dönüştürmeden, karakter dizisi
biçiminde ``list()`` fonksiyonuna parametre olarak verirsek ne olur? Bu durumda
``list()`` fonksiyonu çalışır, ama istediğimiz gibi bir sonuç vermez. Şu kodları
dikkatlice inceleyin::
    
    notlar = []

    for i in range(10):
        veri = input("{}. not: ".format(i+1))
        notlar += list(veri)

    print("Girdiğiniz notlar: ", *notlar)

Bu kodları çalıştırdığınızda, tek haneli sayılar düzgün bir şekilde listeye
eklenir, ancak çift ve daha fazla haneli sayılar ise listeye parça parça
eklenir. Örneğin `234` sayısını girdiğinizde listeye `2`, `3` ve `4` sayıları
tek tek eklenir. Çünkü, yukarıda da dediğim gibi, ``list()`` fonksiyonu, aslında
karakter dizileri üzerine bir ``for`` döngüsü kurar. Yani::
    
    >>> for i in "234":
    ...     print(i)
    
    2
    3
    4

Dolayısıyla listeye `234` sayısı bir bütün olarak değil de, parça parça
eklendiği için istediğiniz sonucu alamamış olursunuz.

Peki bu sorunun üstesinden nasıl geleceğiz? Aslında bu sorunun çözümü çok
basittir. Eğer bir verinin listeye parça parça değil de, bir bütün olarak
eklenmesini istiyorsanız `[]` işaretlerinden yararlanabilirsiniz. Tıpkı şu
örnekte olduğu gibi::
    
    liste = []

    while True:
        sayı = input("Bir sayı girin: (çıkmak için q) ")

        if sayı == "q":
            break
        
        sayı = int(sayı)

        if sayı not in liste:
            liste +=  [sayı]
            print(liste)
        else:
            print("Bu sayıyı daha önce girdiniz!")

Gördüğünüz gibi, kullanıcı tarafından aynı verinin birden fazla girilmesini
önlemek için de listelerden yararlanabiliyoruz.

Yalnız burada şunu söyleyelim: Gerçek programlarda listelere öğe eklemek veya
listeleri birleştirmek gibi işlemler için yukarıdaki gibi `+` işlecinden
yararlanmayacağız. Yukarıda gösterdiğimiz yöntem de doğru olmakla birlikte, bu
iş için genellikle liste metotlarından yararlanılır. Bu metotları birazdan
göreceğiz.

Listeden Öğe Çıkarmak
======================

Bir listeden öğe silmek için `del` adlı ifadeden yararlanabilirsiniz. Örneğin::

    >>> liste = [1, 5, 3, 2, 9]
    >>> del liste[-1]
    >>> liste
    
    [1, 5, 3, 2]

Listeleri Silmek
===================

Python'da listeleri tamamen silmek de mümkündür. Örneğin::

    >>> liste = [1, 5, 3, 2, 9]
    >>> del liste
    >>> liste 

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'liste' is not defined

Listeleri Kopyalamak
=======================

Diyelim ki, yazdığınız bir programda, varolan bir listeyi kopyalamak, yani aynı
listeden bir tane daha üretmek istiyorsunuz. Mesela elimizde şöyle bir liste
olsun::
    
    >>> li1 = ["elma", "armut", "erik"]

Amacımız bu listeden bir tane daha oluşturmak. İlk olarak aklınıza şöyle bir
yöntem gelmiş olabilir::
    
    >>> li2 = li1

Gerçekten de bu yöntem bize aynı öğelere sahip iki liste verdi::

    >>> print(li1)
    
    ["elma", "armut", "erik"]
    
    >>> print(li2)
    
    ["elma", "armut", "erik"]

Gelin şimdi ilk listemiz olan `li1` üzerinde bir değişiklik yapalım. Mesela bu
listenin `"elma"` olan ilk öğesini `"karpuz"` olarak değiştirelim::
    
    >>> li1[0] = "karpuz"
    >>> print(li1)
    
    ["karpuz", "armut", "erik"]

Gördüğünüz gibi, `li1` adlı listenin ilk öğesini başarıyla değiştirdik. Şimdi şu
noktada, `li2` adlı öbür listemizin durumunu kontrol edelim::
    
    >>> print(li2)
    
    ["karpuz", "armut", "erik"]

O da ne! Biz biraz önce `li1` üzerinde değişiklik yapmıştık, ama görünüşe göre
bu değişiklikten `li2` de etkilenmiş. Muhtemelen beklediğiniz şey bu değildi.
Yani siz `li2` listesinin içeriğinin aynı kalıp, değişiklikten yalnızca `li1`
listesinin etkilenmesini istiyordunuz. Biraz sonra bu isteğinizi nasıl yerine
getirebileceğinizi göstereceğiz. Ama önce dilerseniz, bir liste üzerindeki
değişiklikten öteki listenin de neden etkilendiğini anlamaya çalışalım.

Hatırlarsanız, listelerin değiştirilebilir (*mutable*) bir veri tipi olduğunu
söylemiştik. Listeler bu özellikleriyle karakter dizilerinden ayrılıyor. Zira
biraz önce `li1` ve `li2` üzerinde yaptığımız işlemin bir benzerini karakter
dizileri ile yaparsak farklı bir sonuç alırız. Dikkatlice bakın::
    
    >>> a = "elma"

Burada, değeri `"elma"` olan `a` adlı bir karakter dizisi tanımladık. Şimdi bu
karakter dizisini kopyalayalım::
    
    >>> b = a

    >>> a
    
    'elma'
    
    >>> b
    
    'elma'

Böylece aynı değere sahip iki farklı karakter dizimiz olmuş oldu. 

Şimdi `a` adlı
karakter dizisi üzerinde değişiklik yapalım. Ama biz biliyoruz ki, bir karakter
dizisini değiştirmenin tek yolu, o karakter dizisini yeniden tanımlamaktır::
    
    >>> a = "E" + a[1:]
    
    >>> a
    
    'Elma'
    
Burada yaptığımız şeyin bir 'değişiklik' olmadığına dikkatinizi çekmek isterim.
Çünkü aslında biz burada varolan `a` adlı değişken üzerinde bir değişiklik
yapmak yerine, yine `a` adı taşıyan başka bir değişken oluşturuyoruz.

Peki bu 'değişiklikten' öbür karakter dizisi etkilendi mi?

::

    >>> b
    
    'elma'

Gördüğünüz gibi, bu değişiklik öteki karakter dizisini etkilememiş. Bunun
sebebinin, karakter dizilerinin değiştirilemeyen (*immutable*) bir veri tipi
olması olduğunu söylemiştik.

Gelin isterseniz bu olgunun derinlerine inelim biraz...

Yukarıda `a` ve `b` adlı iki değişken var. Bunların kimliklerini kontrol
edelim::

    >>> id(a)
    
    15182784
    
    >>> id(b)
    
    15181184

Gördüğünüz gibi, bu iki değişken farklı kimlik numaralarına sahip. Bu durumu şu
şekilde de teyit edebileceğimizi biliyorsunuz::
    
    >>> id(a) == id(b)
    
    False

Demek ki gerçekten de ``id(a)`` ile ``id(b)`` birbirinden farklıymış. Yani
aslında biz aynı nesne üzerinde bir değişiklik yapmak yerine, farklı bir nesne
oluşturmuşuz.

Bu sonuç bize, bu iki karakter dizisinin bellekte farklı konumlarda saklandığını
gösteriyor. Dolayısıyla Python, bir karakter dizisini kopyaladığımızda bellekte
ikinci bir nesne daha oluşturuyor. Bu nedenle birbirinden kopyalanan karakter
dizilerinin biri üzerinde yapılan herhangi bir işlem öbürünü etkilemiyor. Ama
listelerde (ve değiştirilebilir bütün veri tiplerinde) durum farklı. Şimdi şu
örneklere dikkatlice bakın::
    
    >>> liste1 = ["ahmet", "mehmet", "özlem"]

Bu listeyi kopyalayalım::

    >>> liste2 = liste1

Elimizde aynı öğelere sahip iki liste var::
    
    >>> liste1
    
    ['ahmet', 'mehmet', 'özlem']
    
    >>> liste2
    
    ['ahmet', 'mehmet', 'özlem']

Bu listelerin kimlik numaralarını kontrol edelim::

    >>> id(liste1)
    
    14901376
    
    >>> id(liste2)
    
    14901376
    
    >>> id(liste1) == id(liste2)
    
    True
    
Gördüğünüz gibi, `liste1` ve `liste2` adlı listeler aynı kimlik numarasına
sahip. Yani bu iki nesne birbiriyle aynı. Dolayısıyla birinde yaptığınız
değişiklik öbürünü de etkiler. Eğer birbirinden kopyalanan listelerin birbirini
etkilemesini istemiyorsanız, önünüzde birkaç seçenek var.

İlk seçeneğe göre şöyle bir kod yazabilirsiniz:

Önce özgün listemizi oluşturalım::
    
    >>> liste1 = ["ahmet", "mehmet", "özlem"]
    
Şimdi bu listeyi kopyalayalım::
    
    >>> liste2 = liste1[:]
    
Burada `liste1`'i kopyalarken, listeyi baştan sona dilimlediğimize dikkat edin. 
    
Bakalım `liste1`'deki değişiklik öbürünü de etkiliyor mu::
    
    >>> liste1[0] = "veli"
    >>> liste1
    
    ['veli', 'mehmet', 'özlem']
    
    >>> liste2
    
    ['ahmet', 'mehmet', 'özlem']
    
Gördüğünüz gibi, `liste1`'de yaptığımız değişiklik `liste2`'ye yansımadı. Demek
ki yöntemimiz işe yaramış. 

Aynı işi yapmak için kullanabileceğimiz ikinci yöntem ise ``list()``
fonksiyonunu kullanmaktır:

Önce özgün listemizi görelim::
    
    >>> liste1 = ["ahmet", "mehmet", "özlem"]
    
Şimdi bu listeyi kopyalayalım::
    
    >>> liste2 = list(liste1)
    
Artık elimizde birbirinin kopyası durumunda iki farklı liste var::
    
    >>> liste2
    
    ['ahmet', 'mehmet', 'özlem']
    
    >>> liste1
    
    ['ahmet', 'mehmet', 'özlem']

Şimdi `liste2` üzerinde bir değişiklik yapalım::
    
    >>> liste2[0] = 'veli'
    
`liste2`'yi kontrol edelim::
    
    >>> liste2

    ['veli', 'mehmet', 'özlem']
    
Bakalım `liste1` bu değişiklikten etkilenmiş mi::

    >>> liste1

    ['ahmet', 'mehmet', 'özlem']    
    
Gördüğünüz gibi, her şey yolunda. Dilerseniz bu nesnelerin birbirinden farklı
olduğunu ``id()`` fonksiyonu aracılığıyla teyit edebileceğinizi biliyorsunuz.

Listeleri kopyalamanın üçüncü bir yöntemi daha var. Bu yöntemi de bir sonraki
bölümde liste metotlarını incelerken ele alacağız.

Liste Üreteçleri (List Comprehensions)
=======================================

Şimdi Python'daki listelere ilişkin çok önemli bir konuya değineceğiz. Bu
konunun adı 'liste üreteçleri'. İngilizce'de buna "*List Comprehension*" adı
veriliyor.

Adından da anlaşılacağı gibi, liste üreteçlerinin görevi liste üretmektir. Basit
bir örnek ile liste üreteçleri konusuna giriş yapalım::

    liste = [i for i in range(1000)]

Burada 0'dan 1000'e kadar olan sayıları tek satırda bir liste haline getirdik.
Bu kodların söz dizimine çok dikkat edin. Aslında yukarıdaki kod şu şekilde de
yazılabilir::
    
    liste = []

    for i in range(1000):
        liste += [i]

Burada önce `liste` adlı boş bir liste tanımladık. Daha sonra 0 ile 1000
aralığında bütün sayıları bu boş listeye teker teker gönderdik. Böylece elimizde
0'dan 1000'e kadar olan sayıları tutan bir liste olmuş oldu. Aynı iş için liste
üreteçlerini kullandığımızda ise bu etkiyi çok daha kısa bir yoldan halletmiş
oluyoruz. Liste üreteçlerini kullandığımız kodu tekrar önümüze alalım::
    
    liste = [i for i in range(1000)]

Gördüğünüz gibi, burada önceden boş bir liste tanımlamamıza gerek kalmadı.
Ayrıca bu kodlarda ``for`` döngüsünün parantezler içine alınarak nasıl
sadeleştirildiğine de dikkatinizi çekmek isterim. Şu kod::
    
    for i in range(1000):
        liste += [i]

Liste üreteçlerini kullandığımızda şu koda dönüşüyor::

    [i for i in range(1000)]

Pek çok durumda liste üreteçleri öbür seçeneklere kıyasla bir alternatif olma
işlevi görür. Yani liste üreteçleri ile elde edeceğiniz sonucu başka araçlarla
da elde edebilirsiniz. Mesela yukarıdaki kodların yaptığı işlevi yerine getirmek
için başka bir seçenek olarak ``list()`` fonksiyonundan da yararlanabileceğimizi
biliyorsunuz::
    
    liste = list(range(1000))

Bu basit örneklerde liste üreteçlerini kullanmanın erdemi pek göze çarpmıyor.
Ama bazı durumlarda liste üreteçleri öteki alternatiflere kıyasla çok daha
pratik bir çözüm sunar. Böyle durumlarda başka seçeneklere başvurup yolunuzu
uzatmak yerine liste üreteçlerini kullanarak işinizi kısa yoldan
halledebilirsiniz.

Örneğin 0 ile 1000 arasındaki çift sayıları listelemek için liste üreteçlerini
kullanmak, alternatiflerine göre daha makul bir tercih olabilir::
    
    liste = [i for i in range(1000) if i % 2 == 0]

Aynı işi ``for`` döngüsü ile yapmak için şöyle bir kod yazmamız gerekir::

    liste = []
    for i in range(1000):
        if i % 2 == 0:
            liste += [i]

Gördüğünüz gibi, liste üreteçleri bize aynı işi daha kısa bir yoldan halletme
imkanı tanıyor. Bu arada ``for`` döngüsünün ve bu döngü içinde yer alan `if`
deyiminin liste üreteçleri içinde nasıl göründüğüne dikkat ediyoruz.

Liste üreteçleri ile ilgili bir örnek daha verelim. Mesela elinizde şöyle bir
liste olduğunu düşünün::

    liste = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]

Burada iç içe geçmiş 4 adet liste var. Bu listenin bütün öğelerini tek bir
listeye nasıl alabiliriz? Yani şöyle bir çıktıyı nasıl elde ederiz?

::

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

``for`` döngülerini kullanarak şöyle bir kod yazabiliriz::

    liste = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]

    tümü = []

    for i in liste:
        for z in i:
            tümü += [z]

    print(tümü)
    
Liste üreteçleri ise daha kısa bir çözüm sunar::

    liste = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]]

    tümü = [z for i in liste for z in i]
    print(tümü)

Bu liste üreteci gerçekten de bize kısa bir çözüm sunuyor, ama bu tip iç içe
geçmiş ``for`` döngülerinden oluşan liste üreteçlerinde bazen okunaklılık sorunu
ortaya çıkabilir. Yani bu tür iç içe geçmiş ``for`` döngülerinden oluşan liste
üreteçlerini anlamak, alternatif yöntemlere göre daha zor olabilir.

Bazı durumlarda ise liste üreteçleri bir sorunun çözümü için tek makul yol
olabilir. Diyelim ki bir X.O.X Oyunu (*Tic Tac Toe*) yazıyorsunuz. Bu oyunda
oyuncular oyun tahtası üzerine X veya O işaretlerinden birini yerleştirecek.
Oyuncunun bu oyunu kazanabilmesi için, X veya O işaretlerinden birisinin oyun
tahtası üzerinde belli konumlarda bulunması gerekiyor. Yani mesela X işaretinin
oyunu kazanabilmesi için bu işaretin oyun tahtası üzerinde şu şekilde bir
dizilime sahip olması gerekir::
    
     O   X   O

    ___  X   O

    ___  X  ___


Bu dizilime göre oyunu X işareti kazanır. Peki X işaretinin, oyunu kazanmasını
sağlayacak bu dizilime ulaştığını nasıl tespit edeceksiniz?

Bunun için öncelikle oyun tahtası üzerinde hangi dizilim şekillerinin galibiyeti
getireceğini gösteren bir liste hazırlayabilirsiniz. Mesela yukarıdaki gibi 3x3
boyutundaki bir oyun tahtasında X işaretinin oyunu kazanabilmesi için şu
dizilimlerden herhangi birine sahip olması gerekir::
    
    [0, 0], [1, 0], [2, 0]
     
     X  ___  ___
      
     X  ___  ___
     
     X  ___  ___
     
     
    [0, 1], [1, 1], [2, 1]
     
     ___  X  ___
     
     ___  X  ___
     
     ___  X  ___
     
     
    [0, 2], [1, 2], [2, 2]
     
     ___  ___  X
     
     ___  ___  X
     
     ___  ___  X

    [0, 0], [0, 1], [0, 2]

     X    X    X
    ___  ___  ___

    ___  ___  ___
    

    [1, 0], [1, 1], [1, 2]

    ___  ___  ___

     X    X    X
    ___  ___  ___
    
    
    [2, 0], [2, 1], [2, 2]

    ___  ___  ___
    
    ___  ___  ___

     X    X    X
     
    
    [0, 0], [1, 1], [2, 2]
     
     X   ___  ___
     
     ___  X   ___
      
     ___  ___  X
     
     
     [0, 2], [1, 1], [2, 0]
     
     ___  ___  X
     
     ___  X  ___
     
     X  ___  ___

Aynı dizilimler O işareti için de geçerlidir. Dolayısıyla bu kazanma ölçütlerini
şöyle bir liste içinde toplayabilirsiniz::
    
    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]] 

Oyun sırasında X veya O işaretlerinin aldığı konumu bu kazanma ölçütleri ile
karşılaştırarak oyunu kimin kazandığını tespit edebilirsiniz. Yani
`kazanma_ölçütleri` adlı liste içindeki, iç içe geçmiş listelerden herhangi biri
ile oyunun herhangi bir aşamasında tamamen eşleşen işaret, oyunu kazanmış
demektir.

Bir sonraki bölümde bu bahsettiğimiz X.O.X Oyununu yazacağız. O zaman bu sürecin
nasıl işlediğini daha ayrıntılı bir şekilde inceleyeceğiz. Şimdilik yukarıdaki
durumu temsil eden basit bir örnek vererek liste üreteçlerinin kullanımını
incelemeye devam edelim.

Örneğin elinizde, yukarıda bahsettiğimiz kazanma ölçütlerini temsil eden şöyle
bir liste olduğunu düşünün::

    liste1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12],
              [13, 14, 15],
              [16, 17, 18],
              [19, 20, 21],
              [22, 23, 24],
              [25, 26, 27],
              [28, 29, 30],
              [31, 32, 33]]

Bir de şöyle bir liste::

    liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33, 
              22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44, 
              59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51, 
              89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71, 
              16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20, 
              33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78, 
              34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64, 
              26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35, 
              72, 38, 100, 52, 16, 49, 79]

Burada amacınız `liste1` içinde yer alan iç içe geçmiş listelerden hangisinin
`liste2` içindeki sayıların alt kümesi olduğunu, yani `liste2` içindeki
sayıların, `liste1` içindeki üçlü listelerden hangisiyle birebir eşleştiğini
bulmak. Bunun için şöyle bir kod yazabiliriz::
    
    for i in liste1:
        ortak = [z for z in i if z in liste2]
        if len(ortak) == len(i):
            print(i)

Bu kodlar ilk bakışta gözünüze çok karmaşık gelmiş olabilir. Ama aslında hiç de
karmaşık değildir bu kodlar. Şimdi bu kodları Türkçe'ye çevirelim:

\1. satır: `liste1` adlı listedeki her bir öğeye `i` adını verelim 

\2. satır: `i` içindeki, `liste2`'de de yer alan her bir öğeye de `z` adını verelim ve 
bunları `ortak` adlı bir listede toplayalım. 

\3. satır: eğer `ortak` adlı listenin uzunluğu `i` değişkeninin uzunluğu ile aynıysa

\4. satır: `i`'yi ekrana basalım ve böylece alt kümeyi bulmuş olalım.

Eğer bu satırları anlamakta zorluk çekiyorsanız okumaya devam edin. Biraz sonra
vereceğimiz örnek programda da bu kodları görecek ve bu kodların ne işe
yaradığını orada daha iyi anlayacaksınız.

Örnek Program: X.O.X Oyunu
============================

Şu ana kadar Python programlama dili hakkında epey bilgi edindik. Buraya kadar
öğrendiklerimizi kullanarak işe yarar programlar yazabiliyoruz. Belki
farkındasınız, belki de değilsiniz, ama özellikle listeler konusunu öğrenmemiz
bize çok şey kazandırdı.

Bir önceki bölümde, bir X.O.X Oyunu yazacağımızdan söz etmiş ve bu oyunun
Python'la nasıl yazılabileceğine dair bazı ipuçları da vermiştik. İşte bu
bölümde, Python programlama dilinde şimdiye kadar öğrendiklerimizi kullanarak bu
oyunu yazacağız.

Yazacağımız oyunun İngilizce adı *Tic Tac Toe*. Bu oyunun ne olduğunu ve
kurallarını bir önceki bölümde kabataslak bir şekilde vermiştik. Eğer isterseniz
oyun kurallarına `wikipedia.org/wiki/Çocuk_oyunları#X_O_X_OYUNU
<http://tr.wikipedia.org/wiki/Çocuk_oyunları#X_O_X_OYUNU>`_ adresinden de
bakabilirsiniz.

Oyunu ve kurallarını bildiğinizi varsayarak kodlamaya başlayalım.

Burada ilk yapmamız gereken şey, üzerinde oyun oynanacak tahtayı çizmek olmalı.
Amacımız şöyle bir görüntü elde etmek::

    ___ ___ ___

    ___ ___ ___

    ___ ___ ___

Bu tahtada oyuncu soldan sağa ve yukarıdan aşağıya doğru iki adet konum bilgisi
girecek ve oyunu oynayan kişinin gireceği bu konumlara "X" ve "O" harfleri
işaretlenecek.

Böyle bir görüntü oluşturmak için pek çok farklı yöntem kullanılabilir. Ama
oyuncunun her konum bilgisi girişinde, X veya O işaretini tahta üzerinde
göstereceğimiz için tahta üzerinde oyun boyunca sürekli birtakım değişiklikler
olacak. Bildiğiniz gibi karakter dizileri, üzerinde değişiklik yapmaya müsait
bir veri tipi değil. Böyle bir görev için listeler daha uygun bir araç
olacaktır. O yüzden tahtayı oluşturmada listeleri kullanmayı tercih edeceğiz.

::

    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]


Gördüğünüz gibi, burada iç içe geçmiş üç adet listeden oluşan bir liste var.
``print(tahta)`` komutunu kullanarak bu listeyi ekrana yazdırırsanız listenin
yapısı daha belirgin bir şekilde ortaya çıkacaktır::
    
    [['___', '___', '___'], ['___', '___', '___'], ['___', '___', '___']]

Oyun tahtasını oluşturduğumuza göre, şimdi yapmamız gereken şey bu oyun
tahtasını düzgün bir şekilde oyuncuya göstermek olmalı. Dediğimiz gibi, oyuncu
şöyle bir çıktı görmeli::

    ___ ___ ___

    ___ ___ ___

    ___ ___ ___

Bu görüntüyü elde etmek için şu kodları yazıyoruz::

    print("\n"*15)

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)

Bu kodlarda bilmediğiniz hiçbir şey yok. Burada gördüğünüz her şeyi önceki
derslerde öğrenmiştiniz.

Yukarıdaki kodları yazarken tamamen, elde etmek istediğimiz görüntüye
odaklanıyoruz. Mesela ``print("\n"*15)`` kodunu yazmamızın nedeni, oyun tahtası
için ekranda boş bir alan oluşturmak. Bu etkiyi elde etmek için 15 adet yeni
satır karakteri bastık ekrana. Bu kodla elde edilen etkiyi daha iyi görebilmek
için bu kodu programdan çıkarmayı deneyebilirsiniz.

Alttaki satırda ise bir ``for`` döngüsü tanımladık. Bu döngünün amacı `tahta`
adlı listedeki "__" öğelerini düzgün bir şekilde oyuncuya gösterebilmek. Oyun
tahtasının, ekranı (yaklaşık olarak da olsa) ortalamasını istiyoruz. O yüzden,
tahta öğelerine soldan girinti verebilmek için ``print()`` fonksiyonunun ilk
parametresini ``"\t".expandtabs(30)`` şeklinde yazdık. Karakter dizilerinin
``expandtabs()`` adlı metodunu önceki derslerimizden hatırlıyor olmalısınız. Bu
metodu kullanarak sekme (``TAB``) karakterlerini genişletebiliyorduk. Burada da
"\\t" karakterini bu metot yardımıyla genişleterek liste öğelerini sol baştan
girintiledik.

``print()`` fonksiyonunun ikinci parametresi ise ``*i``. Bu parametrenin ne iş
yaptığını anlamak için şöyle bir kod yazalım::

    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    for i in tahta:
        print(i)

Bu kodları çalıştırdığımızda şöyle bir çıktı elde ederiz::

    ['___', '___', '___']
    ['___', '___', '___']
    ['___', '___', '___']

Gördüğünüz gibi, iç içe geçmiş üç adet listeden oluşan `tahta` adlı liste
içindeki bu iç listeler ekrana döküldü. Bir de şuna bakın::
    
    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    for i in tahta:
        print(*i)

Bu kodlar çalıştırıldığında şu çıktıyı verir:: 

    ___ ___ ___
    ___ ___ ___
    ___ ___ ___

Bu defa liste yapısını değil, listeyi oluşturan öğelerin kendisini görüyoruz.
Yıldız işaretinin, birlikte kullanıldığı öğeler üzerinde nasıl bir etkiye sahip
olduğunu yine önceki derslerimizden hatırlıyorsunuz. Mesela şu örneğe bakın::
    
    kardiz = "istihza"

    for i in kardiz:
        print(i, end=" ")
    print()

Bu kodlar şu çıktıyı veriyor::

    i s t i h z a

Aynı çıktıyı basitçe şu şekilde de elde edebileceğimizi biliyorsunuz::

    kardiz = "istihza"
    print(*kardiz)

İşte oyun tahtasını ekrana dökmek için kullandığımız kodda da benzer bir şey
yaptık. Yıldız işareti yardımıyla, `tahta` adlı listeyi oluşturan iç içe geçmiş
listeleri liste dışına çıkarıp düzgün bir şekilde kullanıcıya gösterdik.

``print()`` fonksiyonu içindeki son parametremiz şu: ``end="\n"*2``

Bu parametrenin ne işe yaradığını kolaylıkla anlayabildiğinizi zannediyorum. Bu
parametre de istediğimiz çıktıyı elde etmeye yönelik bir çabadan ibarettir.
`tahta` adlı liste içindeki iç içe geçmiş listelerin her birinin sonuna ikişer
adet "\\n" karakteri yerleştirerek, çıktıdaki satırlar arasında yeterli miktarda
aralık bıraktık. Eğer oyun tahtasındaki satırların biraz daha aralıklı olmasını
isterseniz bu parametredeki 2 çarpanını artırabilirsiniz. Mesela: ``end="\n"*3``

Şimdi yapmamız gereken şey, oyundaki kazanma ölçütlerini belirlemek.
Hatırlarsanız bu konuya bir önceki bölümde değinmiştik. O yüzden aşağıda
söyleyeceklerimizin bir bölümüne zaten aşinasınız. Burada önceden söylediğimiz
bazı şeylerin yeniden üzerinden geçeceğiz.

Dediğim gibi, kodların bu bölümünde, hangi durumda oyunun biteceğini ve
kazananın kim olacağını tespit edebilmemiz gerekiyor. Mesela oyun sırasında
şöyle bir görüntü ortaya çıkarsa hemen oyunu durdurup "O KAZANDI!" gibi bir
çıktı verebilmemiz lazım::
    
     O   O   O

    ___  X   X

    ___ ___ ___

Veya şöyle bir durumda "X KAZANDI!" diyebilmeliyiz::

     X   O  ___

     X   O   O

     X  ___ ___

Yukarıdaki iki örnek üzerinden düşünecek olursak, herhangi bir işaretin şu
konumlarda bulunması o işaretin kazandığını gösteriyor::
    
    yukarıdan aşağıya 0; soldan sağa 0 
    yukarıdan aşağıya 1; soldan sağa 0 
    yukarıdan aşağıya 2; soldan sağa 0 

veya::

    yukarıdan aşağıya 0; soldan sağa 0 
    yukarıdan aşağıya 0; soldan sağa 1 
    yukarıdan aşağıya 0; soldan sağa 2

İşte bizim yapmamız gereken şey, bir işaretin oyun tahtası üzerinde hangi
konumlarda bulunması halinde oyunun biteceğini tespit etmek. Yukarıdaki
örnekleri göz önüne alarak bunun için şöyle bir liste hazırlayabiliriz::
    
    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 0], [0, 1], [0, 2]]]

Burada iki adet listeden oluşan, `kazanma_ölçütleri` adlı bir listemiz var.
Liste içinde, her biri üçer öğeden oluşan şu listeleri görüyoruz::
    
    [[0, 0], [1, 0], [2, 0]]
    [[0, 0], [0, 1], [0, 2]]

Bu listeler de kendi içinde ikişer öğeli bazı listelerden oluşuyor. Mesela ilk
liste içinde şu listeler var::
    
    [0, 0], [1, 0], [2, 0]

İkinci liste içinde ise şu listeler::

    [0, 0], [0, 1], [0, 2]

Burada her bir liste içindeki ilk sayı oyun tahtasında yukarıdan aşağıya doğru
olan düzlemi; ikinci sayı ise soldan sağa doğru olan düzlemi gösteriyor.

Tabii ki oyun içindeki tek kazanma ölçütü bu ikisi olmayacak. Öteki kazanma
ölçütlerini de tek tek tanımlamalıyız::

    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]

İşte X veya O işaretleri `kazanma_ölçütleri` adlı listede belirtilen
koordinatlarda bulunduğunda, ilgili işaretin oyunu kazandığını ilan edip oyundan
çıkabileceğiz.

Yukarıdaki açıklamalardan da anlayacağınız gibi, X ve O işaretlerinin oyun
tahtasındaki konumu, oyunun gidişatı açısından önem taşıyor. O yüzden şu şekilde
iki farklı liste daha tanımlamamızda fayda var::
    
    x_durumu = []
    o_durumu = []

Bu değişkenler sırasıyla X işaretinin ve O işaretinin oyun içinde aldıkları
konumları kaydedecek. Bu konumlarla, bir önceki adımda tanımladığımız kazanma
ölçütlerini karşılaştırarak oyunu kimin kazandığını tespit edebileceğiz.

Gördüğünüz gibi, oyunda iki farklı işaret var: X ve O. Dolayısıyla oynama sırası
sürekli olarak bu iki işaret arasında değişmeli. Mesela oyuna 0 işareti ile
başlanacaksa, 0 işaretinin yerleştirilmesinden sonra sıranın X işaretine geçmesi
gerekiyor. X işareti de yerleştirildikten sonra sıra tekrar 0 işaretine geçmeli
ve oyun süresince bu böyle devam edebilmeli.

Bu sürekliliği sağlamak için şöyle bir kod yazabiliriz::

    sıra = 1
    
    while True:
        if sıra % 2 == 0:
            işaret = "X".center(3)
        else:
            işaret = "O".center(3) 
        
        sıra += 1
        
        print()
        print("İŞARET: {}\n".format(işaret))

Burada sayıların tek veya çift olma özelliğinden yararlanarak X ve O işaretleri
arasında geçiş yaptık. Önce `sıra` adlı bir değişken tanımlayıp bunun değerini 1
olarak belirledik. `while` döngüsünde ise bu değişkenin değerini her defasında 1
artırdık. Eğer sayının değeri çiftse işaret X; tekse O olacak. Bu arada X ve O
adlı karakter dizilerini, ``center()`` metodu yardımıyla ortaladığımıza dikkat
edin.

Yukarıdaki kodları bu şekilde çalıştırdığınızda X ve O harflerinin çok hızlı bir
şekilde ekrandan geçtiğini göreceksiniz. Eğer ekranda son hız akıp giden bu
verileri yavaşlatmak ve neler olup bittiğini daha net görmek isterseniz
yukarıdaki kodları şöyle yazabilirsiniz::
    
    from time import sleep

    sıra = 1

    while True:
        if sıra % 2 == 0:
            işaret = "X".center(3)
        else:
            işaret = "O".center(3) 
        sıra += 1
        
        print()
        print("İŞARET: {}\n".format(işaret)) 
        sleep(0.3)

Bu kodlarda henüz öğrenmediğimiz parçalar var. Ama şimdilik bu bilmediğiniz
parçalara değil, sonuca odaklanın. Burada yaptığımız şey, `while` döngüsü içinde
her bir ``print()`` fonksiyonu arasına 0.3 saniyelik duraklamalar eklemek.
Böylece programın akışı yavaşlamış oluyor. Biz de `işaret` değişkeninin her
döngüde bir X, bir O oluşunu daha net bir şekilde görebiliyoruz.

.. note:: Asıl program içinde X ve O karakterlerinin geçişini özellikle
          yavaşlatmamıza gerek kalmayacak. Programın ilerleyen satırlarında ``input()``
          fonksiyonu yardımıyla kullanıcıdan veri girişi isteyeceğimiz için X ve O'ların
          akışı zaten doğal olarak duraklamış olacak.

`while` döngümüzü yazmaya devam edelim::

        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break

        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break
        
        x = int(x)-1
        y = int(y)-1

Burada X veya O işaretlerini tahta üzerinde uygun yerlere yerleştirebilmek için
kullanıcının konum bilgisi girmesini istiyoruz. `x` değişkeni yukarıdan aşağıya
doğru olan düzlemdeki konumu, `y` değişkeni ise soldan sağa doğru olan
düzlemdeki konumu depolayacak. Oyunda kullanıcının girebileceği değerler 1, 2
veya 3 olacak. Mesela oyuncu O işareti için yukarıdan aşağıya 1; soldan sağa 2
değerini girmişse şöyle bir görüntü elde edeceğiz::
    
    ___  O  ___

    ___ ___ ___

    ___ ___ ___

Burada ``ljust()`` metotlarını, kullanıcıya gösterilecek verinin düzgün bir
şekilde hizalanması amacıyla kullandık.

Eğer kullanıcı `x` veya `y` değişkenlerinden herhangi birine "q" cevabı verirse
oyundan çıkıyoruz.

Yukarıdaki kodların son iki satırında ise kullanıcıdan gelen karakter dizilerini
birer sayıya dönüştürüyoruz. Bu arada, bildiğiniz gibi Python saymaya 0'dan
başlıyor. Ama insanlar açısından doğal olan saymaya 1'den başlamaktır. O yüzden
mesela kullanıcı 1 sayısını girdiğinde Python'ın bunu 0 olarak algılamasını
sağlamamız gerekiyor. Bunun için x ve y değerlerinden 1 çıkarıyoruz.

Kullanıcıdan gerekli konum bilgilerini aldığımıza göre, bu bilgilere dayanarak X
ve O işaretlerini oyun tahtası üzerine yerleştirebiliriz. Şimdi şu kodları
dikkatlice inceleyin::
    
        print("\n"*15)

        if tahta[x][y] == "___":
            tahta[x][y] = işaret
            if işaret == "X".center(3):
                x_durumu += [[x, y]]
            elif işaret == "O".center(3):
                o_durumu += [[x, y]]
            sıra += 1
        else:
            print("\nORASI DOLU! TEKRAR DENEYİN\n")

Burada öncelikle `15` adet satır başı karakteri basıyoruz. Böylece oyun tahtası
için ekranda boş bir alan oluşturmuş oluyoruz. Bu satır tamamen güzel bir
görüntü elde etmeye yönelik bir uygulamadır. Yani bu satırı yazmasanız da
programınız çalışır. Veya siz kendi zevkinize göre daha farklı bir görünüm elde
etmeye çalışabilirsiniz.

İkinci satırda gördüğümüz ``if tahta[x][y] == "___":`` kodu, oyun tahtası
üzerindeki bir konumun halihazırda boş mu yoksa dolu mu olduğunu tespit etmemizi
sağlıyor. Amacımız oyuncunun aynı konuma iki kez giriş yapmasını engellemek.
Bunun için tahta üzerinde x ve y konumlarına denk gelen yerde "___" işaretinin
olup olmadığına bakmamız yeterli olacaktır. Eğer bakılan konumda "___" işareti
varsa orası boş demektir. O konuma işaret koyulabilir. Ama eğer o konumda "___"
işareti yoksa X veya O işaretlerinden biri var demektir. Dolayısıyla o konuma
işaret koyulamaz. Böyle bir durumda kullanıcıya "ORASI DOLU! TEKRAR DENEYİN"
uyarısını gösteriyoruz.

Oyun tahtası üzerinde değişiklik yapabilmek için nasıl bir yol izlediğimize
dikkat edin::

        tahta[x][y] = işaret

Mesela oyuncu yukarıdan aşağıya 1; soldan sağa 2 sayısını girmişse, kullanıcıdan
gelen sayılardan 1 çıkardığımız için, Python yukarıdaki kodu şöyle
değerlendirecektir::
    
        tahta[0][1] = işaret
    
Yani `tahta` adlı liste içindeki ilk listenin ikinci sırasına ilgili işaret
yerleştirilecektir.

Ayrıca yukarıdaki kodlarda şu satırları da görüyoruz::

            if işaret == "X".center(3):
                x_durumu += [[x, y]]
            elif işaret == "O".center(3):
                o_durumu += [[x, y]]

Eğer işaret sırası X'te ise oyuncunun girdiği konum bilgilerini `x_durumu` adlı
değişkene, eğer işaret sırası O'da ise konum bilgilerini `o_durumu` adlı
değişkene yolluyoruz. Oyunu hangi işaretin kazandığını tespit edebilmemiz
açısından bu kodlar büyük önem taşıyor. `x_durumu` ve `o_durumu` değişkenlerini
`kazanma_ölçütleri` adlı liste ile karşılaştırarak oyunu kimin kazandığına karar
vereceğiz.

Bu arada, oyunun en başında tanımladığımız `sıra` adlı değişkeni ``if`` bloğu
içinde artırdığımıza dikkat edin. Bu sayede, kullanıcının yanlışlıkla aynı
konuma iki kez işaret yerleştirmeye çalışması halinde işaret sırası
değişmeyecek. Yani mesela o anda sıra X'te ise ve oyuncu yanlış bir konum
girdiyse sıra yine X'te olacak. Eğer `sıra` değişkenini ``if`` bloğu içine
yazmazsak, yanlış konum girildiğinde işaret sırası O'a geçecektir.

İsterseniz şimdiye kadar yazdığımız kodları şöyle bir topluca görelim::

    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    print("\n"*15)

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)

    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]

    x_durumu = []
    o_durumu = []

    sıra = 1
    while True:
        if sıra % 2 == 0:
            işaret = "X".center(3)
        else:
            işaret = "O".center(3)
            
        print()
        print("İŞARET: {}\n".format(işaret))
        
        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        
        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break
        
        x = int(x)-1
        y = int(y)-1
        
        print("\n"*15)
        
        if tahta[x][y] == "___":
            tahta[x][y] = işaret
            if işaret == "X".center(3):
                x_durumu += [[x, y]]
            elif işaret == "O".center(3):
                o_durumu += [[x, y]]
            sıra += 1
        else:
            print("\nORASI DOLU! TEKRAR DENEYİN\n")

Gördüğünüz gibi epey kod yazmışız. Kodlarımızı topluca incelediğimize göre
yazmaya devam edebiliriz::
    
    for i in tahta:
         print("\t".expandtabs(30), *i, end="\n"*2)

Bu kodların ne işe yaradığınız biliyorsunuz. Oyun tahtasının son durumunu
kullanıcıya göstermek için kullanıyoruz bu kodları.

Sıra geldi oyunun en önemli kısmına. Bu noktada oyunu kimin kazandığını
belirlememiz gerekiyor. Dikkatlice inceleyin::

    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit() 

Bu kodları anlayabilmek için en iyi yol uygun yerlere ``print()`` fonksiyonları
yerleştirerek çıktıları incelemektir. Mesela bu kodları şöyle yazarak `o` ve `x`
değişkenlerinin değerlerini izleyebilirsiniz::
    
    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        print("o: ", o)
        print("x: ", x)
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()

Bu kodlar içindeki en önemli öğeler `o` ve `x` adlı değişkenlerdir. Burada,
`o_durumu` veya `x_durumu` adlı listelerdeki değerlerle `kazanma_ölçütleri` adlı
listedeki değerleri karşılaştırarak, ortak değerleri `o` veya `x` değişkenlerine
yolluyoruz. Eğer ortak öğe sayısı 3'e ulaşırsa (``if len(o) == len(i):`` veya
``if len(x) == len(i):``), bu sayıyı yakalayan ilk işaret hangisiyse oyunu o
kazanmış demektir.

Kodlarımızın son hali şöyle oldu::

    tahta = [["___", "___", "___"],
             ["___", "___", "___"],
             ["___", "___", "___"]]

    print("\n"*15)

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)

    kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                         [[0, 1], [1, 1], [2, 1]],
                         [[0, 2], [1, 2], [2, 2]],
                         [[0, 0], [0, 1], [0, 2]],
                         [[1, 0], [1, 1], [1, 2]],
                         [[2, 0], [2, 1], [2, 2]],
                         [[0, 0], [1, 1], [2, 2]],
                         [[0, 2], [1, 1], [2, 0]]]

    x_durumu = []
    o_durumu = []

    sıra = 1
    while True:
        if sıra % 2 == 0:
            işaret = "X".center(3)
        else:
            işaret = "O".center(3)
            
        print()
        print("İŞARET: {}\n".format(işaret))
        
        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
        if x == "q":
            break
        
        y = input("soldan sağa [1, 2, 3]: ".ljust(30))
        if y == "q":
            break
        
        x = int(x)-1
        y = int(y)-1
        
        print("\n"*15)
        
        if tahta[x][y] == "___":
            tahta[x][y] = işaret
            if işaret == "X".center(3):
                x_durumu += [[x, y]]
            elif işaret == "O".center(3):
                o_durumu += [[x, y]]
            sıra += 1
        else:
            print("\nORASI DOLU! TEKRAR DENEYİN\n")
        
        for i in tahta:
             print("\t".expandtabs(30), *i, end="\n"*2)

        for i in kazanma_ölçütleri:
            o = [z for z in i if z in o_durumu]
            x = [z for z in i if z in x_durumu]
            
            if len(o) == len(i):
                print("O KAZANDI!")
                quit()
            if len(x) == len(i):
                print("X KAZANDI!")
                quit()
                
Gördüğünüz gibi, sadece şu ana kadar öğrendiğimiz bilgileri kullanarak bir oyun
yazabilecek duruma geldik. Burada küçük parçaları birleştirerek bir bütüne nasıl
ulaştığımızı özellikle görmenizi isterim. Dikkat ederseniz, yukarıdaki programda
sadece karakter dizileri, sayılar, listeler ve birkaç fonksiyon var. Nasıl
sadece 7 nota ile müzik şaheserleri meydana getirilebiliyorsa, yalnızca 4-5 veri
tipi ile de dünyayı ayağa kaldıracak programlar da yazılabilir.

Listeleri temel olarak incelediğimize göre biraz da demetlerden söz edebiliriz. 

Demetler
**********

Demetler, özellikle görünüş olarak listelere çok benzeyen bir veri tipidir. Bu
veri tipi de, tıpkı listeler gibi, farklı veri tiplerini içinde barındıran
kapsayıcı bir veri tipidir.

Demet Tanımlamak
================

Demet tanımlamanın birkaç farklı yolu vardır. Nasıl karakter dizilerinin ayırt
edici özelliği tırnak işaretleri, listelerin ayırt edici özelliği ise köşeli
parantez işaretleri ise, demetlerin ayırt edici özelliği de normal parantez
işaretleridir. Dolayısıyla bir demet tanımlamak için normal parantez
işaretlerinden yararlanacağız::
    
    >>> demet = ("ahmet", "mehmet", 23, 45)
    
    >>> type(demet)
    
    <class 'tuple'>

Gördüğünüz gibi, karakter dizilerinin ``type()`` sorgusuna `str`, listelerin ise
`list` cevabı vermesi gibi, demetler de ``type()`` sorgusuna `tuple` cevabı
veriyor.

Yalnız, dediğimiz gibi Python'da demet tanımlamanın birden fazla yolu vardır.
Mesela yukarıdaki demeti şöyle de tanımlayabiliriz::
    
    >>> demet = "ahmet", "mehmet", 23, 45
    
Gördüğünüz gibi, parantez işaretlerini kullanmadan, öğeleri yalnızca virgül
işareti ile ayırdığımızda da elde ettiğimiz şey bir demet oluyor. 

Demet oluşturmak için ``tuple()`` adlı bir fonksiyondan da yararlanabilirsiniz.
Bu fonksiyon, liste oluşturan ``list()`` fonksiyonuna çok benzer::
    
    >>> tuple('abcdefg')
    
    ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    
Bu fonksiyonu kullanarak başka veri tiplerini demete dönüştürebilirsiniz::
    
    >>> tuple(["ahmet", "mehmet", 34, 45])
    
    ('ahmet', 'mehmet', 34, 45)
    
Burada, `["ahmet", "mehmet", 34, 45]` adlı bir listeyi ``tuple()`` fonksiyonu
yardımıyla demete dönüştürdük.

Tek Öğeli bir Demet Tanımlamak
===============================

Tek öğeli bir karakter dizisi oluşturabilmek için şu yolu izliyorduk
hatırlarsanız::
    
    >>> kardiz = 'A'
    
Bu tek öğeli bir karakter dizisidir. Bir de tek öğeli bir liste tanımlayalım::
    
    >>> liste = ['ahmet']
    
Bu da tek öğeli bir listedir. Gelin bir de tek öğeli bir demet oluşturmaya
çalışalım::
    
    >>> demet = ('ahmet')
    
Bu şekilde tek öğeli bir demet oluşturduğunuzu zannediyorsunuz, ama aslında
oluşturduğunuz şey basit bir karakter dizisinden ibaret! Gelin kontrol edelim::
    
    >>> type(demet)
    
    <class 'str'>
    
Python programlama dilinde tek öğeli bir demet oluşturma işlemi biraz
'tuhaf'tır. Eğer tek öğeye sahip bir demet oluşturacaksak şöyle bir şey
yazmalıyız::
    
    >>> demet = ('ahmet',)
    
veya::

    >>> demet = 'ahmet',

Gördüğünüz gibi, tek öğeli bir demet tanımlarken, o tek öğenin yanına bir tane
virgül işareti yerleştiriyoruz. Böylece demet tanımlamak isterken, yanlışlıkla
alelade bir şekilde 'ahmet' adlı bir karakter dizisini 'demet' adlı bir
değişkene atamamış oluyoruz...

Demetlerin Öğelerine Erişmek
============================

Eğer bir demet içinde yer alan herhangi bir öğeye erişmek isterseniz, karakter
dizileri ve listelerden hatırladığınız yöntemi kullanabilirsiniz::
    
    >>> demet = ('elma', 'armut', 'kiraz')
    >>> demet[0]
    
    'elma'
    
    >>> demet[-1]
    
    'kiraz'
    
    >>> demet[:2]
    
    ('elma', 'armut')
    
Gördüğünüz gibi, daha önce öğrendiğimiz indeksleme ve dilimleme kuralları aynen
demetler için de geçerli.

Demetlerle Listelerin Birbirinden Farkı
========================================

En başta da söylediğimiz gibi, demetlerle listeler birbirine çok benzer. Ama
demetlerle listelerin birbirinden çok önemli bazı farkları da vardır. Bu iki
veri tipi arasındaki en önemli fark, listelerin değiştirilebilir (*mutable*) bir
veri tipi iken, demetlerin değiştirilemez (*immutable*) bir veri tipi olmasıdır.
Yani tıpkı karakter dizileri gibi, demetler de bir kez tanımlandıktan sonra
bunların üzerinde değişiklik yapmak mümkün değildir::
    
    >>> demet = ('elma', 'armut', 'kiraz')
    >>> demet[0] = 'karpuz'
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    
Gördüğünüz gibi, demetin herhangi bir öğesini değiştirmeye çalıştığımızda Python
bize bir hata mesajı gösteriyor. 
    
Bu bakımdan, eğer programın akışı esnasında üzerinde değişiklik yapmayacağınız
veya değişiklik yapılmasını istemediğiniz birtakım veriler varsa ve eğer siz bu
verileri liste benzeri bir taşıyıcı içine yerleştirmek istiyorsanız, listeler
yerine demetleri kullanabilirsiniz. Ayrıca demetler üzerinde işlem yapmak
listelere kıyasla daha hızlıdır. Dolayısıyla, performans avantajı nedeniyle de
listeler yerine demetleri kullanmak isteyebilirsiniz. 

Tahmin edebileceğiniz gibi, tıpkı karakter dizilerinde olduğu gibi, önceden
tanımlanmış bir demetin üzerinde değişiklik yapabilmek için, örneğin bir demetle
başka bir demeti birleştirmek için o demeti yeniden tanımlamak da mümkündür::
    
    >>> demet = ('ahmet', 'mehmet')
    >>> demet = demet + ('selin',)
    
Eğer sadece ``demet + ('selin',)`` demiş olsaydık özgün demet üzerinde herhangi
bir değişiklik yapmış olmayacaktık. Siz bu olguya karakter dizilerinden de
aşinasınız. O yüzden, özgün demet üzerinde herhangi bir değişiklik yapabilmek
için, daha doğrusu özgün demet üzerinde bir değişiklik yapmış gibi görünebilmek
için, özgün demeti sıfırdan tanımlamamız gerekiyor...
    
Burada ayrıca 'ahmet' ve 'mehmet' öğelerinden oluşan bir demete 'selin' öğesini
nasıl eklediğimize de dikkat edin. Asla unutmamalısınız: Python programlama
dilinde sadece aynı tür verileri birbiriyle birleştirebilirsiniz. Mesela
yukarıdaki örnekte 'selin' adlı öğeyi `demet` adlı demete bir karakter dizisi
olarak ekleyemezsiniz::
    
    >>> demet = demet + 'selin'
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can only concatenate tuple (not "str") to tuple

Bu arada, yukarıdaki kodu şöyle yazdığınızda da aslında bir demetle karakter
dizisini birleştirmeye çalışıyor olduğunuza dikkat edin::
    
    >>> demet = demet + ('selin')
    
Hatırlarsanız, tek öğeli bir demet tanımlayabilmek için parantez içindeki tek
öğenin yanına bir virgül işareti yerleştirmemiz gerekiyordu. Aksi halde demet
değil, karakter dizisi tanımlamış oluyorduk. Zaten bir Python programcısı
olarak, demetler üzerinde çalışırken en sık yapacağınız hata da demet
tanımlamaya çalışırken yanlışlıkla karakter dizisi tanımlamak olacaktır.
    
Dediğimiz ve yukarıda da örneklerle gösterdiğimiz gibi, bir demeti yeni baştan
tanımlayarak da o demet üzerinde değişiklik yapmış etkisi elde edebilirsiniz.
Ancak elbette bir araya topladığınız veriler üzerinde sık sık değişiklikler
yapacaksanız demetler yerine listeleri tercih etmelisiniz.

Demetlerin Kullanım Alanı
==========================

Demetleri ilk öğrendiğinizde bu veri tipi size son derece gereksizmiş gibi
gelebilir. Ama aslında oldukça yaygın kullanılan bir veri tipidir bu. Özellikle
programların ayar (*conf*) dosyalarında bu veri tipi sıklıkla kullanılır.
Örneğin Python tabanlı bir web çatısı (*framework*) olan Django'nun
`settings.py` adlı ayar dosyasında pek çok değer bir demet olarak saklanır.
Mesela bir Django projesinde web sayfalarının şablonlarını (*template*) hangi
dizin altında saklayacağınızı belirlediğiniz ayar şöyle görünür::
    
    TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates',)
    
Burada, şablon dosyalarının hangi dizinde yer alacağını bir demet içinde
gösteriyoruz. Bu demet içine birden fazla dizin adı yazabilirdik. Ama biz bütün
şablon dosyalarını tek bir dizin altında tutmayı tercih ettiğimiz için tek öğeli
bir demet tanımlamışız. Bu arada, daha önce de söylediğimiz gibi, demetlerle
ilgili en sık yapacağınız hata, tek öğeli demet tanımlamaya çalışırken aslında
yanlışlıkla bir karakter dizisi tanımlamak olacaktır. Örneğin yukarıdaki
`TEMPLATE_DIRS` değişkenini şöyle yazsaydık::
    
    TEMPLATE_DIRS = ('/home/projects/djprojects/blog/templates')
    
Aslında bir demet değil, alelade bir karakter dizisi tanımlamış olurduk...


