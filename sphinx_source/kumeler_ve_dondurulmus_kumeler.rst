.. meta::
   :description: Bu bölümde kümeler ve dondurulmuş kümelerden söz edeceğiz.
   :keywords: python, küme, dondurulmuş küme
       
.. highlight:: py3

*******************************
Kümeler ve Dondurulmuş Kümeler
*******************************

Bu bölümde Python'daki iki veri tipini daha inceleyeceğiz. İnceleyeceğimiz veri
tiplerinin adı küme ve dondurulmuş küme.

Özellikle kümeleri öğrendiğimizde, bu veri tipinin kendine has birtakım
özellikleri sayesinde bunların kimi zaman hiç tahmin bile edemeyeceğimiz
yerlerde işimize yaradığını göreceğiz. Normalde uzun uzun kod yazmayı gerektiren
durumlarda kümeleri kullanmak, bir-iki satırla işlerimizi halletmemizi
sağlayabilir.

Bu bölümde kümeler dışında, bir de dondurulmuş kümelerden söz edeceğiz. Bu iki
veri tipi birbiriyle ilişkilidir. O yüzden bu iki veri tipini tek bölümde ele
alacağız. 

İsterseniz anlatmaya önce kümelerle başlayalım.

Kümeler
**********

Tıpkı listeler, demetler, karakter dizileri, sayılar ve dosyalar gibi kümeler de
Python'daki veri tiplerinden biridir. Adından da az çok tahmin edebileceğiniz
gibi kümeler, matematikten bildiğimiz "küme" kavramıyla sıkı sıkıya
bağlantılıdır. Bu veri tipi, matematikteki kümelerin sahip olduğu bütün
özellikleri taşır. Yani matematikteki kümelerden bildiğimiz kesişim, birleşim ve
fark gibi özellikler Python'daki kümeler için de geçerlidir.

Küme Oluşturmak
===============

Kümelerin bize sunduklarından faydalanabilmek için elbette öncelikle bir küme
oluşturmamız gerekiyor. Küme oluşturmak çok kolay bir işlemdir. Örneğin boş bir
kümeyi şöyle oluşturuyoruz::
    
    >>> boş_küme = set()

Listeler, demetler ve sözlüklerin aksine kümelerin ayırt edici bir işareti
yoktur. Küme oluşturmak için set() adlı özel bir fonksiyondan yararlanıyoruz.

Yukarıdaki boş veri tipinin bir küme olduğunu nasıl teyit edeceğinizi
biliyorsunuz::

    >>> type(boş_küme)
    
    <class 'set'>
    
Gördüğünüz gibi, Python programlama dilinde kümeler `set` ifadesiyle
gösteriliyor. 

Yukarıda boş bir küme oluşturduk. İçinde öğe de barındıran kümeleri ise şu
şekilde oluşturuyoruz::

	>>> küme = set(["elma", "armut", "kebap"])

Böylelikle, içinde öğe barındıran ilk kümemizi başarıyla oluşturduk. Dikkat
ederseniz, küme oluştururken listelerden faydalandık. Gördüğünüz gibi `set()`
fonksiyonu içindeki öğeler bir liste içinde yer alıyor. Dolayısıyla yukarıdaki
tanımlamayı şöyle de yapabiliriz::
    
	>>> liste = ["elma", "armut", "kebap"]
	>>> küme = set(liste)

Bu daha temiz bir görüntü oldu. Elbette küme tanımlamak için mutlaka liste
kullanmak zorunda değiliz. İstersek demetleri de küme haline getirebiliriz::
    
	>>> demet = ("elma", "armut", "kebap")
	>>> küme = set(demet)

Hatta ve hatta karakter dizilerinden dahi küme yapabiliriz::

	>>> kardiz = "Python Programlama Dili için Türkçe Kaynak"
	>>> küme = set(kardiz)

Kullandığımız karakter dizisinin böyle uzun olmasına da gerek yok. Tek
karakterlik dizilerden bile küme oluşturabiliriz::
    
	>>> kardiz = "a"
	>>> küme = set(kardiz)

Ama sayılardan küme oluşturamayız::

	>>> n = 10
	>>> küme = set(n)

	TypeError: 'int' object is not iterable

Peki sözlükleri kullanarak küme oluşturabilir miyiz? Elbette, neden olmasın? ::

    >>> bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux", 
    ... "dağıtım": "Ubuntu GNU/Linux"}
    
    >>> küme = set(bilgi)
	
Küme oluşturmanın son bir yönteminden daha söz edelim. En başta söylediğimiz
gibi, listeler, demetler, sözlükler ve karakter dizilerinin aksine kümelerin `[
]`, `( )`, `{ }`, `' '` gibi ayırt edici bir işareti yoktur. Ama eğer istersek
sözlükleri oluşturmak için kullandığımız özel işaretleri küme oluşturmak için de
kullanabiliriz. Dikkatlice bakın::

    >>> küme = {'Python', 'C++', 'Ruby', 'PHP'}
    
Gördüğünüz gibi, aslında sözlüklerin ayırt edici işareti olan süslü parantezleri
kullanarak ve öğeleri birbirinden virgülle ayırarak da küme adlı veri tipini
elde edebiliyoruz. Teyit edelim bunu::
    
    >>> type(küme)
    
    <class 'set'> 

Ancak bu yapıyı kullanarak boş bir küme oluşturamazsınız::
    
    >>> küme = {}
    
Bu şekilde oluşturduğunuz şey bir küme değil, sözlük olacaktır::

    >>> type(küme)

    <class 'dict'>

Boş bir küme oluşturmak için ``set()`` fonksiyonunu kullanmanız gerektiğini
biliyorsunuz::

    >>> küme = set(küme)
    >>> type(küme)

    <class 'set'>    

Böylece kümeleri nasıl oluşturacağımızı öğrendik. Eğer oluşturduğunuz kümeyi
ekrana yazdırmak isterseniz, ne yapacağınızı biliyorsunuz. Tanımladığınız
``küme`` değişkenini kullanmanız yeterli olacaktır::
    
	>>> küme

	{'işletim sistemi', 'sistem çekirdeği', 'dağıtım'}

Bu arada, bir sözlüğü kümeye çevirdiğinizde, elbette sözlüğün yalnızca
anahtarları kümeye eklenecektir. Sözlüğün değerleri ise böyle bir işlemin
sonucunda ortadan kaybolur. 

Eğer bir sözlüğü kümeye çevirirken hem anahtarları hem de değerleri korumak
gibi bir niyetiniz varsa şöyle bir şey yazabilirsiniz:

Sözlüğümüz şu::
    
    >>> bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux", 
    ... "dağıtım": "Ubuntu GNU/Linux"}
    
Bu sözlükteki anahtar-değer çiftlerini bir küme içine, çift öğeli demetler
olarak yerleştirebiliriz::    

    >>> liste = [(anahtar, değer) for anahtar, değer in bilgi.items()]
    >>> küme = set(liste)

Gördüğünüz gibi, liste üreteçlerini kullanarak önce bir liste oluşturuyoruz. Bu
liste her bir anahtarı ve değeri tek tek bir demet içine yerleştiriyor. Daha
sonra da bu listeyi ``set()`` fonksiyonuna göndererek kümemizi oluşturuyoruz.
    
Kümelerin Yapısı
==================

Bir önceki başlık altında kümelerin nasıl tanımlanacağını inceledik. Gelin şimdi
de biraz kümelerin yapısından bahsedelim.

Örneğin şöyle bir küme tanımlayalım::

	>>> kardiz = "Python Programlama Dili"
	>>> küme = set(kardiz)
	>>> print(küme)
	
	{'g', 'D', 'a', ' ', 'o', 'n', 'm', 'l', 'i', 'h', 't', 'r', 'P', 'y'}

Burada bir şey dikkatinizi çekmiş olmalı. Bir öğeyi küme olarak tanımlayıp
ekrana yazdırdığımızda elde ettiğimiz çıktı, o öğe içindeki her bir alt öğeyi
tek bir kez içeriyor. Yani mesela "Python Programlama Dili" içinde iki adet "P"
karakteri var, ama çıktıda bu iki "P" karakterinin yalnızca biri görünüyor.
Buradan anlıyoruz ki, kümeler aynı öğeyi birden fazla tekrar etmez. Bu çok
önemli bir özelliktir ve pek çok yerde işimize yarar. Aynı durum karakter dizisi
dışında kalan öteki veri tipleri için de geçerlidir. Yani mesela eğer bir
listeyi küme haline getiriyorsak, o listedeki öğeler küme içinde yalnızca bir
kez geçecektir. Listede aynı öğeden iki-üç tane bulunsa bile, kümemiz bu öğeleri
teke indirecektir.

::

    >>> liste = ["elma", "armut", "elma", "kebap", "şeker", "armut",
    ... "çilek", "ağaç", "şeker", "kebap", "şeker"]
    
    >>> for i in set(liste):
    ...     print(i)
    ...
    ağaç
    elma
    şeker
    kebap
    çilek
    armut

Gördüğünüz gibi, liste içinde birden fazla bulunan öğeler, Python'daki kümeler
yardımıyla teke indirilebiliyor.

Öğrendiğimiz bu bilgi sayesinde, daha önce gördüğümüz `count()` metodunu da
kullanarak, şöyle bir kod yazabiliriz::

    >>> liste = ["elma", "armut", "elma", "kiraz",
    ... "çilek", "kiraz", "elma", "kebap"]

    >>> for i in set(liste):
    ...     print("{} listede {} kez geçiyor!".format(i, liste.count(i)))

    kebap listede 1 kez geçiyor!
    elma listede 3 kez geçiyor!
    kiraz listede 2 kez geçiyor!
    armut listede 1 kez geçiyor!
    çilek listede 1 kez geçiyor!

Burada ``set(liste)`` ifadesini kullanarak, liste öğelerini eşşiz ve benzersiz
bir hale getirdik.

Kümelerin önemli bir özelliği de, tıpkı sözlükler gibi, herhangi bir şekilde
'öğe sırası' kavramına sahip olmamasıdır.

Dikkatlice bakın::
    
    >>> arayüz_takımları = {'Tkinter', 'PyQT', 'PyGobject'}
    >>> arayüz_takımları
    
    {'PyGobject', 'PyQT', 'Tkinter'}
    
Sözlüklerde karşılaştığımız durumun aynısının kümeler için de geçerli olduğuna
dikkatinizi çekmek isterim. Gördüğünüz gibi, `arayüz_takımları` adlı kümenin
öğeleri, öğe tanımlama sırasını çıktıda korumuyor. Biz 'Tkinter' öğesini kümenin
ilk sırasına yerleştirmiştik, ama bu öğe çıktıda en sona gitti... Aynen
sözlüklerde olduğu gibi, kümelerde de öğelerin tanımlanma sırasına bel
bağlayarak herhangi bir işlem yapamazsınız. Bu durumun bir yansıması olarak,
küme öğelerine sıralarına göre de erişemezsiniz::
    
    >>> arayüz_takımları[0]

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing    
    
Tıpkı hata mesajında da söylendiği gibi, küme adlı veri tipi açısından öğe
sırası diye bir kavram yoktur...    
        
Esasında tek bir küme pek bir işe yaramaz. Kümeler ancak birden fazla olduğunda
bunlarla yararlı işler yapabiliriz. Çünkü kümelerin en önemli özelliği, başka
kümelerle karşılaştırılabilme kabiliyetidir. Yani mesela kümelerin kesişimini,
birleşimini veya farkını bulabilmek için öncelikle elimizde birden fazla küme
olması gerekiyor. İşte biz de şimdi bu tür işlemleri nasıl yapacağımızı
öğreneceğiz. O halde hiç vakit kaybetmeden yolumuza devam edelim.

Küme Üreteçleri (*Set Comprehensions*)
=======================================

Bildiğiniz gibi liste üreteçleri, liste oluşturmanın kısa ve temiz bir yoludur.
Aynı şekilde sözlük üreteçleri de sözlük oluşturmanın kısa ve temiz bir yoludur. 

İşte liste üreteçlerini ve sözlük üreteçlerini kullanarak nasıl tek satırda ve
hızlı bir şekilde listeler ve sözlükler üretebiliyorsak, aynı şekilde küme
üreteçlerini kullanarak tek satırda ve hızlı bir şekilde kümeler de
üretebiliriz.

Örneğin elimizde şöyle bir liste olduğunu düşünelim::
    
    import random 
    
    liste = [random.randint(0, 10000) for i in range(1000)]    
    
Bu arada, buradaki `random` adlı modüle şimdilik takılmayın. Birkaç bölüm sonra
bu modülü inceleyeceğiz. Biz şimdilik `random`'un da tıpkı `sys` ve `os` gibi
bir modül olduğunu ve rastgele sayılar üretmemizi sağladığını bilelim yeter.
Yukarıdaki kodlarda da bu modül `0` ile `10000` arasında rstgele `1000` adet
sayı üretmemizi sağladı.

Şimdi amacımız bu liste içinde yer alan sayılardan, değeri `100`'den küçük
olanları bulmak. 

Bunun için şu kodları kullanabiliriz::
    
    import random 
    
    liste = [random.randint(0, 10000) for i in range(1000)]
    
    yüzden_küçük_sayılar = [i for i in liste if i < 100]
    print(yüzden_küçük_sayılar)
    
Ancak ortaya çıkan listede aynı sayılardan birkaç tane olabilir. İşte eğer
birbirinin aynı olmayan sayılardan oluşmuş bir listeyi hızlı ve pratik bir
şekilde elde etmek istiyorsanız küme üreteçlerini kullanabilirsiniz::
    
    import random 
    
    liste = [random.randint(0, 10000) for i in range(1000)]
    
    küme = {i for i in liste if i < 100}
    print(küme)
    
Gördüğünüz gibi, küme üreteçlerinin sözdizimi, liste ve sözlük üreteçlerinin
sözdizimine çok benziyor. 

Kümelerin Metotları
===================

Daha önceki veri tiplerinde olduğu gibi, kümelerin de metotları vardır. Artık
biz bir veri tipinin metotlarını nasıl listeleyeceğimizi çok iyi biliyoruz.
Nasıl liste için ``list()``; demet için ``tuple()``; sözlük için de ``dict()``
fonksiyonlarını kullanıyorsak, kümeler için de ``set()`` adlı fonksiyondan
yararlanacağız::
    
    >>> dir(set)

    ['__and__', '__class__', '__contains__', '__delattr__', '__doc__', 
    '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
    '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', 
    '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', 
    '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', 
    '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', 
    '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 
    'clear','copy', 'difference', 'difference_update', 'discard', 
    'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
    'issuperset', 'pop', 'remove', 'symmetric_difference', 
    'symmetric_difference_update', 'union', 'update']

Hemen işimize yarayacak metotları alalım::

    >>> for i in dir(set):
    ...     if "__" not in i:
    ...         print(i)
    ...
    add
    clear
    copy
    difference
    difference_update
    discard
    intersection
    intersection_update
    isdisjoint
    issubset
    issuperset
    pop
    remove
    symmetric_difference
    symmetric_difference_update
    union
    update

Gördüğünüz gibi kümelerin epey metodu var. Bu arada ``if "__" not in i``
satırında "_" yerine "__" kullandığımıza dikkat edin. Neden? Çünkü eğer sadece
"_" kullanırsak `symmetric_difference` ve `symmetric_difference_update`
metotları çıktımızda yer almayacaktır.

Unutmadan söyleyelim: Kümeler de, tıpkı listeler ve sözlükler gibi,
değiştirilebilir bir veri tipidir.

clear()
^^^^^^^^^^^^

Kümelerle ilgili olarak inceleyeceğimiz ilk metot `clear()`. Bu metodu daha önce
sözlükleri çalışırken de görmüştük. Sözlüklerde bu metodun görevi sözlüğün içini
boşaltmak idi. Burada da aynı vazifeyi görür::
    
    >>> km = set("adana")
    >>> for i in km:
    ...     print(i)
    ...
    a
    d
    n

    >>> km.clear()
    >>> km
    set()


Burada önce "km" adlı bir küme oluşturduk. Daha sonra da `clear()` metodunu
kullanarak bu kümenin bütün öğelerini sildik. Artık elimizde boş bir küme var.
    
copy()
^^^^^^^^^^^

Listeler ve sözlükleri incelerken ``copy()`` adlı bir metot öğrenmiştik. Bu
metot aynı zamanda kümelerle birlikte de kullanılabilir. Üstelik işlevi de
aynıdır::
    
    >>> km = set("kahramanmaraş")
    >>> yedek = km.copy()
    >>> yedek
    
    {'a', 'r', 'h', 'k', 'm', 'ş', 'n'}
    
    >>> km
    
    {'a', 'h', 'k', 'm', 'n', 'r', 'ş'}

Burada bir şey dikkatinizi çekmiş olmalı. "km" adlı kümeyi "yedek" adıyla
kopyaladık, ama bu iki kümenin çıktılarına baktığımız zaman öğe sıralamasının
birbirinden farklı olduğunu görüyoruz. Biliyorsunuz, tıpkı sözlüklerde olduğu
gibi, kümeler de sırasız veri tipleridir. Bu yüzden, elde ettiğimiz çıktıda
öğeler rastgele diziliyor. Dolayısıyla öğelere sıralarına göre erişemiyoruz.
Aynen sözlüklerde olduğu gibi...
    
add()
^^^^^^^^^^

Kümelerden bahsederken, bunların değiştirilebilir bir veri tipi olduğunu
söylemiştik. Dolayısıyla kümeler, üzerlerinde değişiklik yapmamıza müsaade eden
metotlar da içerir. Örneğin `add()` bu tür metotlardan biridir. *Add* kelimesi
Türkçe'de "eklemek" anlamına gelir. Adından da anlaşılacağı gibi, bu metot
yardımıyla kümelerimize yeni öğeler ilave edebileceğiz. Hemen bunun nasıl
kullanıldığına bakalım::
    
	>>> küme = set(["elma", "armut", "kebap"])
	>>> küme.add("çilek")
	>>> print(küme)

	{'elma', 'armut', 'kebap', 'çilek'}

Gördüğünüz gibi, `add()` metodunu kullanarak, kümemize `çilek` adlı yeni bir öğe
ekledik. Eğer kümede zaten varolan bir öğe eklemeye çalışırsak kümede herhangi
bir değişiklik olmayacaktır. Çünkü, daha önce de söylediğimiz gibi, kümeler her
bir öğeyi tek bir sayıda barındırır.

Eğer bir kümeye birden fazla öğeyi aynı anda eklemek isterseniz `for`
döngüsünden yararlanabilirsiniz::

    >>> yeni = [1,2,3]
    >>> for i in yeni:
    ...     küme.add(i)
    ...
    
    >>> küme
    
    {1, 2, 3, 'elma', 'kebap', 'çilek', 'armut'}

Burada ``yeni`` adlı listeyi kümeye `for` döngüsü ile ekledik. Ama bu işlemi
yapmanın başka bir yolu daha vardır. Bu işlem için Python'da ayrı bir metot
bulunur. Bu metodun adı `update()` metodudur. Sırası gelince bu metodu da
göreceğiz.

Bu arada, yeri gelmişken kümelerin önemli bir özelliğinden daha söz edelim. Bir
kümeye herhangi bir öğe ekleyebilmemiz için, o öğenin değiştirilemeyen
(*immutable*) bir veri tipi olması gerekiyor. Bildiğiniz gibi Python'daki şu
veri tipleri değiştirilemeyen veri tipleridir:

#. Demetler
#. Sayılar
#. Karakter Dizileri

Şu veri tipleri ise değiştirilebilen veri tipleridir:

#. Listeler
#. Sözlükler
#. Kümeler

Dolayısıyla bir kümeye ancak şu veri tiplerini ekleyebiliriz:

#. Demetler
#. Sayılar
#. Karakter Dizileri

Şu kodları dikkatlice inceleyin:

Önce boş bir küme oluşturalım::
    
    >>> küme = set()
    
Bu kümeye bir demet ekleyelim::
    
    >>> l = (1,2,3)
    >>> küme.add(l)
    >>> küme
    
    {(1, 2, 3)}
    
Bir sayı ekleyelim::
    
    >>> l = 45
    >>> küme.add(l)
    >>> küme
    
    {45, (1, 2, 3)}
    
Bir karakter dizisi ekleyelim::
    
    >>> l = 'Jacques Derrida'
    >>> küme.add(l)
    >>> küme
    
    {'Jacques Derrida', 45, (1, 2, 3)}

Yukarıdakiler, değiştirilemeyen veri tipleri olduğu için kümelere eklenebilir. 

Bir de şunlara bakalım:

Kümemize bir liste eklemeye çalışalım::
    
    >>> l = [1,2,3]
    >>> küme.add(l)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

Kümemize bir sözlük eklemeye çalışalım::
    
    >>> l = {"a": 1, "b": 2, "c": 3}
    >>> küme.add(l)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'dict'
    
Kümemize bir küme eklemeye çalışalım::
    
    >>> l = {1, 2, 3}
    >>> küme.add(l)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'set'

Gördüğünüz gibi, tıpkı sözlüklerde olduğu gibi, bir kümeye herhangi bir veri
ekleyebilmemiz için o verinin 'değiştirilemeyen' bir veri tipi olması gerekiyor.

difference()
^^^^^^^^^^^^^^^^^

Bu metot iki kümenin farkını almamızı sağlar. Örneğin::

	>>> k1 = set([1, 2, 3, 5])
	>>> k2 = set([3, 4, 2, 10])

	>>> k1.difference(k2)
	
	{1, 5}

Demek ki k1'in k2'den farkı buymuş. Peki k2'nin k1'den farkını bulmak istersek
ne yapacağız? ::
    
	>>> k2.difference(k1)

	{10, 4}

Gördüğünüz gibi, birinci kullanımda, k1'de bulunup k2'de bulunmayan öğeleri elde
ediyoruz. İkinci kullanımda ise bunun tam tersi. Yani ikinci kullanımda k2'de
bulunup k1'de bulunmayan öğeleri alıyoruz.

İsterseniz uzun uzun `difference()` metodunu kullanmak yerine sadece eksi (-)
işaretini kullanarak da aynı sonucu elde edebilirsiniz::

	>>> k1 - k2

...veya... ::

	>>> k2 - k1

Hayır, "*madem eksi işaretini kullanabiliyoruz, o halde artı işaretini de
kullanabiliriz!*" gibi bir fikir doğru değildir.

difference_update()
^^^^^^^^^^^^^^^^^^^^^^^^

Bu metot, `difference()` metodundan elde edilen sonuca göre bir kümenin
güncellenmesini sağlar. Yani?
Hemen bir örnek verelim::

	>>> k1 = set([1, 2, 3])
	>>> k2 = set([1, 3, 5])
	>>> k1.difference_update(k2)
	>>> print(k1)

	{2}

	>>> print(k2)

	{1, 3, 5}

Gördüğünüz gibi, bu metot k1'in k2'den farkını aldı ve bu farkı kullanarak k1'i
yeniden oluşturdu. k1 ile k2 arasındaki tek fark `2` adlı öğe idi. Dolayısıyla
`difference_update()` metodunu uyguladığımızda k1'in öğelerinin silinip
yerlerine `2` adlı öğenin geldiğini görüyoruz.

discard()
^^^^^^^^^^^^^^

Bir önceki bölümde öğrendiğimiz `add()` metodu yardımıyla, önceden
oluşturduğumuz bir kümeye yeni öğeler ekleyebiliyorduk. Bu bölümde öğreneceğimiz
`discard()` metodu ise kümeden öğe silmemizi sağlayacak::
    
    >>> hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
    >>> hayvanlar.discard("kedi")
    >>> print(hayvanlar)

    {'kuş', 'inek', 'deve', 'köpek', 'at'}

Eğer küme içinde bulunmayan bir öğe silmeye çalışırsak hiç bir şey olmaz. Yani
hata mesajı almayız::
    
	>>> hayvanlar.discard("yılan")

Burada etkileşimli kabuk sessizce bir alt satıra geçecektir. Bu metodun en
önemli özelliği budur. Yani olmayan bir öğeyi silmeye çalıştığımızda hata
vermemesi.

remove()
^^^^^^^^^^^^^

Bu metot da bir önceki bölümde gördüğümüz `discard()` metoduyla aynı işlevi
yerine getirir. Eğer bir kümeden öğe silmek istersek `remove()` metodunu da
kullanabiliriz::
    
	>>> hayvanlar.remove("köpek")

Peki `discard()` varken `remove()` metoduna ne gerek var? Ya da tersi. 

Bu iki metot aynı işlevi yerine getirse de aralarında önemli bir fark vardır.
Hatırlarsanız `discard()` metoduyla, kümede olmayan bir öğeyi silmeye çalışırsak
herhangi bir hata mesajı almayacağımızı söylemiştik. Eğer `remove()` metodunu
kullanarak, kümede olmayan bir öğeyi silmeye çalışırsak, `discard()` metodunun
aksine, hata mesajı alırız::
    
	>>> hayvanlar.remove("fare")

	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'fare'

Bu iki metot arasındaki bu fark önemli bir farktır. Bazen yazdığınız
programlarda, duruma göre her iki özelliğe de ihtiyacınız olabilir.

intersection()
^^^^^^^^^^^^^^^^^^^^

*intersection* kelimesi Türkçe'de "kesişim" anlamına gelir. Adından da
anladığımız gibi, `intersection()` metodu bize iki kümenin kesişim kümesini
verecektir::
    
	>>> k1 = set([1, 2, 3, 4])
	>>> k2 = set([1, 3, 5, 7])
	>>> k1.intersection(k2)

	{1, 3}

Gördüğünüz gibi, bu metot bize k1 ve k2'nin kesişim kümesini veriyor.
Dolayısıyla bu iki küme arasındaki ortak elemanları bulmuş oluyoruz.

Hatırlarsanız, `difference()` metodunu anlatırken, `difference()` kelimesi
yerine "-" işaretini de kullanabileceğimiz, söylemiştik. Benzer bir durum
`intersection()` metodu için de geçerlidir. İki kümenin kesişimini bulmak için
"&" işaretinden yararlanabiliriz::
    
	>>> k1 & k2

	{1, 3}

Python programcıları genellikle uzun uzun *intersection* yazmak yerine "&"
işaretini kullanırlar...

İsterseniz bu metot için örnek bir program verelim. Böylece gerçek hayatta bu
metodu nasıl kullanabileceğimizi görmüş oluruz::

    tr = "şçöğüıŞÇÖĞÜİ"

    parola = input("Sisteme giriş için bir parola belirleyin: ")

    if set(tr) & set(parola):
        print("Parolanızda Türkçe harfler kullanmayın!")

    else:
        print("Parolanız kabul edildi!")
        
Burada eğer kullanıcı, parola belirlerken içinde Türkçe bir harf geçen bir
kelime yazarsa programımız kendisini Türkçe harf kullanmaması konusunda
uyaracaktır. Bu kodlarda kümeleri nasıl kullandığımıza dikkat edin. Programda
asıl işi yapan kısım şu satırdır::
    
    if set(tr) & set(parola):
        print("Parolanızda Türkçe harfler kullanmayın!")

Burada aslında şöyle bir şey demiş oluyoruz:

    *Eğer set(tr) ve set(parola) kümelerinin kesişim kümesi boş değilse,
    kullanıcıya "Parolanızda Türkçe harfler kullanmayın!" uyarısını göster!*
    
``set(tr)`` ve ``set(parola)`` kümelerinin kesişim kümesinin boş olmaması,
kullanıcının girdiği kelime içindeki harflerden en az birinin ``tr`` adlı
değişken içinde geçtiği anlamına gelir. Burada basitçe, ``tr`` değişkeni ile
``parola`` değişkeni arasındaki ortak öğeleri sorguluyoruz. Eğer kullanıcı
herhangi bir Türkçe harf içermeyen bir kelime girerse ``set(tr)`` ve
``set(parola)`` kümelerinin kesişim kümesi boş olacaktır. İsterseniz küçük bir
deneme yapalım::
    
	>>> tr = "şçöğüıŞÇÖĞÜİ"
	>>> parola = "çilek"
	>>> set(tr) & set(parola)

	{'ç'}

Burada kullanıcının "çilek" adlı kelimeyi girdiğini varsayıyoruz. Böyle bir
durumda ``set(tr)`` ve ``set(parola)`` kümelerinin kesişim kümesi "ç" harfini
içerecek, dolayısıyla da programımız kullanıcıya uyarı mesajı gösterecektir.
Eğer kullanıcımız "kalem" gibi Türkçe harf içermeyen bir kelime girerse::
   
	>>> tr = "şçöğüıŞÇÖĞÜİ"
	>>> parola = "kalem"
	>>> set(tr) & set(parola)

	set()

Gördüğünüz gibi, elde ettiğimiz küme boş. Dolayısıyla böyle bir durumda
programımız kullanıcıya herhangi bir uyarı mesajı göstermeyecektir.

`intersection()` metodunu pek çok yerde kullanabilirsiniz. Hatta iki dosya
arasındaki benzerlikleri bulmak için dahi bu metottan yararlanabilirsiniz.
İlerde dosya işlemleri konusunu işlerken bu metottan nasıl yararlanabileceğimizi
de anlatacağız.

intersection_update()
^^^^^^^^^^^^^^^^^^^^^^^^^^

Hatırlarsanız `difference_update()` metodunu işlerken şöyle bir şey demiştik:

*Bu metot, difference() metodundan elde edilen sonuca göre bir kümenin
güncellenmesini sağlar.*

İşte `intersection_update` metodu da buna çok benzer bir işlevi yerine getirir.
Bu metodun görevi, `intersection()` metodundan elde edilen sonuca göre bir
kümenin güncellenmesini sağlamaktır::
    
	>>> k1 = set([1, 2, 3])
	>>> k2 = set([1, 3, 5])
	>>> k1.intersection_update(k2)
	>>> print(k1)

	{1, 3}

	>>> print(k2)

	{1, 3, 5}

Gördüğünüz gibi, `intersection_update()` metodu k1'in bütün öğelerini sildi ve
yerlerine k1 ve k2'nin kesişim kümesinin elemanlarını koydu.

isdisjoint()
^^^^^^^^^^^^^^^^^

Bu metodun çok basit bir görevi vardır. `isdisjoint()` metodunu kullanarak iki
kümenin kesişim kümesinin boş olup olmadığı sorgulayabilirsiniz. Hatırlarsanız
aynı işi bir önceki bölümde gördüğümüz `intersection()` metodunu kullanarak da
yapabiliyorduk. Ama eğer hayattan tek beklentiniz iki kümenin kesişim kümesinin
boş olup olmadığını, yani bu iki kümenin ortak eleman içerip içermediğini
öğrenmekse, basitçe `isdisjoint()` metodundan yararlanabilirsiniz::
    
	>>> a = set([1, 2, 3])
	>>> b = set([2, 4, 6])
	>>> a.isdisjoint(b)

	False

Gördüğünüz gibi, ``a`` ve ``b`` kümesinin kesişimi boş olmadığı için, yani bu
iki küme ortak en az bir öğe barındırdığı için, `isdisjoint()` metodu ``False``
çıktısı veriyor. Burada temel olarak şu soruyu sormuş oluyoruz:

*a ve b ayrık kümeler mi?*

Python da bize cevap olarak, "*Hayır değil,*" anlamına gelen ``False`` çıktısını
veriyor... Çünkü ``a`` ve ``b`` kümelerinin ortak bir elemanı var (`2`).

Bir de şuna bakalım::

	>>> a = set([1, 3, 5])
	>>> b = set([2, 4, 6])
	>>> a.isdisjoint(b)

	True

Burada ``a`` ve ``b`` kümeleri ortak hiç bir elemana sahip olmadığı için "Doğru"
anlamına gelen ``True`` çıktısını elde ediyoruz.

issubset()
^^^^^^^^^^^^^^^

Bu metot yardımıyla, bir kümenin bütün elemanlarının başka bir küme içinde yer
alıp yer almadığını sorgulayabiliriz. Yani bir kümenin, başka bir kümenin alt
kümesi olup olmadığını bu metot yardımıyla öğrenebiliriz. Eğer bir küme başka
bir kümenin alt kümesi ise bu metot bize ``True`` değerini verecek; eğer değilse
``False`` çıktısını verecektir::
    
	>>> a = set([1, 2, 3])
	>>> b = set([0, 1, 2, 3, 4, 5])
	>>> a.issubset(b)

	True

Bu örnekte ``True`` çıktısını aldık, çünkü a kümesinin bütün öğeleri ``b``
kümesi içinde yer alıyor. Yani ``a``, ``b``'nin alt kümesidir.

issuperset()
^^^^^^^^^^^^^^^^^

Bu metot, bir önceki bölümde gördüğümüz `issubset()` metoduna benzer. Matematik
derslerinde gördüğümüz "kümeler" konusunda hatırladığınız "b kümesi a kümesini
kapsar" ifadesini bu metotla gösteriyoruz. Önce bir önceki derste gördüğümüz
örneğe bakalım::
    
	>>> a = set([1, 2, 3])
	>>> b = set([0, 1, 2, 3, 4, 5])
	>>> a.issubset(b)

	True

Buradan, "a kümesi b kümesinin alt kümesidir," sonucuna ulaşıyoruz. Bir de şuna
bakalım::
    
	>>> a = set([1, 2, 3])
	>>> b = set([0, 1, 2, 3, 4, 5])
	>>> b.issuperset(a)

	True

Burada ise, "b kümesi a kümesini kapsar," sonucunu elde ediyoruz. Yani ``b``
kümesi ``a`` kümesinin bütün elemanlarını içinde barındırıyor.
    
union()
^^^^^^^^^^^^

`union()` metodu iki kümenin birleşimini almamızı sağlar. Hemen bir örnek
verelim::
    
	>>> a = set([2, 4, 6, 8])
	>>> b = set([1, 3, 5, 7])
	>>> a.union(b)

	{1, 2, 3, 4, 5, 6, 7, 8}

Önceki bölümlerde gördüğümüz bazı metotlarda olduğu gibi, `union()` metodu da
bir kısayola sahiptir. `union()` metodu yerine "|" işaretini de kullanabiliriz::
    
	>>> a | b

`union()` metodu yerine, bu metodun kısayolu olan "|" işareti Python
programcıları tarafından daha sık kullanılır.

update()
^^^^^^^^^^^^^

Hatırlarsanız `add()` metodunu anlatırken şöyle bir örnek vermiştik::

    >>> küme = set(["elma", "armut", "kebap"])
    >>> yeni = [1, 2, 3]

    >>> for i in yeni:
    ...     küme.add(i)
    ...
    >>> küme
    
    {1, 2, 3, 'elma', 'armut', 'kebap'}

Bu örneği verdikten sonra da şöyle bir şey demiştik:

"Burada ``yeni`` adlı listeyi kümeye `for` döngüsü ile ekledik. Ama bu işlemi
yapmanın başka bir yolu daha vardır. Bu işlem için Python'da ayrı bir metot
bulunur."

İşte bu metodu öğrenmenin vakti geldi. Metodumuzun adı `update()`. Bu metot, bir
kümeyi güncellememizi sağlar. İsterseniz yukarıdaki örneği, bu metodu kullanarak
tekrar yazalım::
    
	>>> küme = set(["elma", "armut", "kebap"])
	>>> yeni = [1, 2, 3]
	>>> küme.update(yeni)
	>>> print(küme)

	{1, 2, 3, 'elma', 'armut', 'kebap'}

Gördüğünüz gibi, `for` döngüsünü kullanmaya gerek kalmadan aynı sonucu elde
edebildik.

symmetric_difference()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Daha önceki bölümlerde `difference()` metodunu kullanarak iki küme arasındaki
farklı öğeleri bulmayı öğrenmiştik. Örneğin elimizde şöyle iki küme var
diyelim::
    
	>>> a = set([1, 2, 5])
	>>> b = set([1, 4, 5])

Eğer ``a`` kümesinin ``b`` kümesinden farkını bulmak istersek şöyle yapıyoruz::

	>>> a.difference(b)

	{2}

Demek ki ``a`` kümesinde bulunup ``b`` kümesinde bulunmayan öğe `2` imiş.

Bir de `b` kümesinde bulunup `a` kümesinde bulunmayan öğelere bakalım::

	>>> b.difference(a)

	{4}

Bu da bize "4" çıktısını verdi. Demek ki bu öğe ``b`` kümesinde bulunuyor, ama
``a`` kümesinde bulunmuyormuş. Peki ya kümelerin ikisinde de bulunmayan öğeleri
aynı anda nasıl alacağız? işte bu noktada yardımımıza `symmetric_difference()`
adlı metot yetişecek::
    
	>>> a.symmetric_difference(b)

	{2, 4}

Böylece iki kümede de bulunmayan öğeleri aynı anda almış olduk.

symmetric_difference_update()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Daha önce `difference_update` ve `intersection_update` gibi metotları
öğrenmiştik. `symmetric_difference_update()` metodu da bunlara benzer bir işlevi
yerine getirir::
    
	>>> a = set([1,2, 5])
	>>> b = set([1,4, 5])
	>>> a.symmetric_difference_update(b)
	>>> print(a) 

	{2, 4}

Gördüğünüz gibi, a kümesinin eski öğeleri gitti, yerlerine
`symmetric_difference()` metoduyla elde edilen çıktı geldi. Yani ``a`` kümesi,
`symmetric_difference()` metodunun sonucuna göre güncellenmiş oldu...

pop()
^^^^^^^^^^

İnceleyeceğimiz son metot `pop()` metodu olacak. Gerçi bu metot bize hiç yabancı
değil. Bu metodu listeler konusundan hatırlıyoruz. Orada öğrendiğimize göre, bu
metot listenin bir öğesini silip ekrana basıyordu. Aslında buradaki fonksiyonu
da farklı değil. Burada da kümelerin öğelerini silip ekrana basıyor::
    
	>>> a = set(["elma", "armut", "kebap"])
	>>> a.pop()

	'elma'

Peki bu metot hangi ölçüte göre kümeden öğe siliyor? Herhangi bir ölçüt yok. Bu
metot, küme öğelerini tamamen rastgele siliyor.

Böylelikle Python'da Listeler, Demetler, Sözlükler ve Kümeler konusunu bitirmiş
olduk. Bu konuları sık sık tekrar etmek, hiç olmazsa arada sırada göz gezdirmek
bazı şeylerin zihnimizde yer etmesi açısından oldukça önemlidir.

Dondurulmuş Kümeler (Frozenset)
********************************

Daha önce de söylediğimiz gibi, kümeler üzerinde değişiklik yapabiliyoruz. Zaten
kümelerin `add()` ve `remove()` gibi metotlarının olması bu durumu teyit ediyor.
Ancak kimi durumlarda, öğeleri üzerinde değişiklik yapılamayan kümelere de
ihtiyaç duyabilirsiniz. Hatırlarsanız listeler ve demetler arasında da buna
benzer bir ilişki var. Demetler çoğu zaman, üzerinde değişiklik yapılamayan bir
liste gibi davranır. İşte Python aynı imkanı bize kümelerde de sağlar. Eğer
öğeleri üzerinde değişiklik yapılamayan bir küme oluşturmak isterseniz `set()`
yerine `frozenset()` fonksiyonunu kullanabilirsiniz. Dilerseniz hemen bununla
ilgili bir örnek verelim::
    
    >>> dondurulmuş = frozenset(["elma", "armut", "ayva"])
    
Dondurulmuş kümeleri bu şekilde oluşturuyoruz. Şimdi bu dondurulmuş kümenin
metotlarına bakalım::
    
    >>> dir(dondurulmuş)
    
    ['__and__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', 
     '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
     '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
     '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__',
     '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
     '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection',
     'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']

Gördüğünüz gibi, `add()`, `remove()`, `update()` gibi, değişiklik yapmaya
yönelik metotlar listede yok.

Dondurulmuş kümeler ile normal kümeler arasında işlev olarak hiçbir fark yoktur.
Bu ikisi arasındaki fark, listeler ile demetler arasındaki fark gibidir.


