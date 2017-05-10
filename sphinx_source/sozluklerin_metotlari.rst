.. meta::
   :description: Python 3.x'te sözlükler adlı veri tipinin metotları
   :keywords: python, sözlük, sözlükler, dictionary, metotlar, get, items, keys,
    values

.. highlight:: py3

*********************
Sözlüklerin Metotları
*********************

Tıpkı öteki veri tiplerinde olduğu gibi, sözlüklerin de birtakım metotları
bulunur. Bu bölümde sözlüklerin şu metotlarını inceleyeceğiz:

#. ``clear()``
#. ``copy()``
#. ``fromkeys()``
#. ``get()``
#. ``items()``
#. ``keys()``
#. ``pop()``
#. ``popitem()``
#. ``setdefault()``
#. ``update()``
#. ``values()``

İlk olarak ``keys()`` metoduyla başlayalım.

keys()
*******

Sözlükleri tarif ederken, sözlüklerin anahtar-değer çiftlerinden oluşan bir veri
tipi olduğunu söylemiştik. Bir sözlüğü normal yollardan ekrana yazdırırsanız
size hem anahtarları hem de bunlara karşılık gelen değerleri verecektir. Ama
eğer bir sözlüğün sadece anahtarlarını almak isterseniz ``keys()`` metodundan
yararlanabilirsiniz::
    
    >>> sözlük = {"a": 0,
    ...           "b": 1,
    ...           "c": 2,
    ...           "d": 3}
    >>> print(sözlük.keys())
    
    dict_keys(['b', 'c', 'a', 'd'])
    
Gördüğünüz gibi, ``sözlük.keys()`` komutu bize bir `dict_keys` nesnesi veriyor.
Bu nesneyi programınızda kullanabilmek için isterseniz, bunu listeye, demete
veya karakter dizisine dönüştürebilirsiniz::
        
    >>> liste = list(sözlük.keys())
    >>> liste
    
    ['b', 'c', 'a', 'd']
    
    >>> demet = tuple(sözlük.keys())
    >>> demet
    
    ('b', 'c', 'a', 'd')

    >>> kardiz = "".join(sözlük.keys())
    >>> kardiz
    
    'bcad'
    
Son örnekte sözlük anahtarlarını karakter dizisine dönüştürmek için ``str()``
fonksiyonunu değil, karakter dizilerinin ``join()`` adlı metodunu kullandığımıza
dikkat edin. Çünkü ``tuple()`` ve ``list()`` fonksiyonlarının aksine ``str()``
fonksiyonu, sözlükteki anahtarların nasıl bir ölçüte göre karakter dizisine
çevrileceğine dair bir kural içermez. Zira siz bu sözlük anahtarlarını pek çok
farklı şekilde karakter dizisine çevirebilirsiniz. Örneğin öğeleri karakter
dizisi içine yerleştirirken öğelerin arasına virgül koymak isteyebilirsiniz::
    
    >>> kardiz = ', '.join(sözlük.keys())
    >>> kardiz
    
    'b, c, a, d'
    
Eğer sözlük anahtarlarını ``str()`` fonksiyonu yardımıyla karakter dizisine
dönüştürmeye kalkışırsanız beklemediğiniz bir çıktı alırsınız.    

values()
*********

``keys()`` metodu bir sözlüğün anahtarlarını veriyor. Bir sözlüğün değerlerini
ise ``values()`` metodu verir::
    
    >>> sözlük
    {'b': 1, 'c': 2, 'a': 0, 'd': 3}
    
    >>> print(sözlük.values())
    
    dict_values([1, 2, 0, 3])
    
Gördüğünüz gibi, bu metottan bir `dict_values` nesnesi alıyoruz. Tıpkı
``keys()`` metodunda olduğu gibi, ``values()`` metodunda da bu çıktıyı başka
veri tiplerine dönüştürme imkanına sahibiz::

    >>> liste = list(sözlük.values())
    >>> liste
    
    [1, 2, 0, 3]
    
    >>> demet = tuple(sözlük.values())
    >>> demet
    
    (1, 2, 0, 3)
    
Yalnız bu verileri karakter dizisine dönüştürmeye çalıştığınızda ufak bir
problemle karşılacaksınız::
    
    >>> kardiz = "".join(sözlük.values())
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sequence item 0: expected str instance, int found
    
Bunun sebebi, sözlükteki değerlerin `int` tipinde olmasıdır. Bildiğiniz gibi,
sadece aynı tip verileri birbiriyle birleştirebiliriz. Eğer birleştirmek
istediğimiz veriler birbirinden farklı tipte ise, bunları birleştirmeden önce
bir dönüştürme işlemi yapmamız gerekir::
    
    >>> kardiz = "".join([str(i) for i in sözlük.values()])
    >>> kardiz
    
    '1203'

Gördüğünüz gibi, sözlükteki değerlerin her birini, tek bir liste üreteci içinde
karakter dizisine dönüştürdük ve ortaya çıkan listeyi karakter dizilerinin
``join()`` metodu yardımıyla, öğelerin arasında hiçbir boşluk bırakmadan
`kardiz` adlı bir karakter dizisi içine yerleştirdik. Elbette eğer isteseydik bu
öğelerin her birinin arasına bir virgül de koyabilirdik::
    
    >>> kardiz = ", ".join([str(i) for i in sözlük.values()])
    >>> kardiz
    
    '1, 2, 0, 3'
    
items()
********

Bu metot, bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı
sağlar::
    
    >>> sözlük.items()
    
    dict_items([('a', 0), ('c', 2), ('b', 1)])
    
Gördüğünüz gibi, tek bir liste içinde iki öğeli demetler halinde hem anahtarları
hem de değerleri görebiliyoruz. Bu metot sıklıkla ``for`` döngüleri ile birlikte
kullanılarak bir sözlüğün anahtar ve değerlerinin manipüle edilebilmesini
sağlar::
    
    >>> for anahtar, değer in sözlük.items():
    ...     print("{} = {}".format(anahtar, değer))
    ...
    a = 0
    c = 2
    b = 1

get()
******    

Bu metot sözlüklerin en kullanışlı metotlarından biridir. Bu metot pek çok
durumda işinizi bir hayli kolaylaştırır.

Diyelim ki şöyle bir program yazdık::

	#!/usr/bin/env python3.0

	ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

	sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

	print(ing_sözlük[sorgu])

Bu programı çalıştırdığımızda eğer kullanıcı "ing_sözlük" adıyla belirttiğimiz
sözlük içinde bulunan kelimelerden birini yazarsa, o kelimenin karşılığını
alacaktır. Diyelim ki kullanıcımız soruya "dil" diye cevap verdi. Bu durumda
ekrana "dil" kelimesinin sözlükteki karşılığı olan "language" yazdırılacaktır.
Peki ya kullanıcı sözlükte tanımlı olmayan bir kelime yazarsa ne olacak? Öyle
bir durumda programımız hata verecektir. Programımız için doğru yol, hata
vermektense, kullanıcıyı kelimenin sözlükte olmadığı konusunda
bilgilendirmektir. Bunu klasik bir yaklaşımla şu şekilde yapabiliriz::
    
	ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

	sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

	if sorgu not in ing_sözlük:
	    print("Bu kelime veritabanımızda yoktur!")
	    
	else:
	    print(ing_sözlük[sorgu])

Ama açıkçası bu pek verimli bir yaklaşım sayılmaz. Yukarıdaki yöntem yerine
sözlüklerin ``get()`` metodundan faydalanabiliriz. Bakalım bunu nasıl
yapıyoruz::
    
	ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

	sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

	print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))

Gördüğünüz gibi, burada çok basit bir metot yardımıyla bütün dertlerimizi
hallettik. Sözlüklerin ``get()`` adlı metodu, parantez içinde iki adet argüman
alır. Birinci argüman sorgulamak istediğimiz sözlük öğesidir. İkinci argüman ise
bu öğenin sözlükte bulunmadığı durumda kullanıcıya hangi mesajın gösterileceğini
belirtir. Buna göre, yukarıda yaptığımız şey, önce "sorgu" değişkenini sözlükte
aramak, eğer bu öğe sözlükte bulunamıyorsa da kullanıcıya, "Bu kelime
veritabanımızda yoktur!" cümlesini göstermekten ibarettir...

Gelin isterseniz bununla ilgili bir örnek daha yapalım.

Diyelim ki bir havadurumu programı yazmak istiyoruz. Bu programda kullanıcı bir
şehir adı girecek. Program da girilen şehre ait havadurumu bilgilerini ekrana
yazdıracak. Bu programı klasik yöntemle şu şekilde yazabiliriz::
    
	#!/usr/bin/env python3

	soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")

	if soru == "istanbul":
	    print("gök gürültülü ve sağanak yağışlı")

	elif soru == "ankara":
	    print("açık ve güneşli")

	elif soru == "izmir":
	    print("bulutlu")

	else:
	    print("Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır.")

Yukarıdaki, gayet geçerli bir yöntemdir. Ama biz istersek bu kodları "get"
metodu yardımıyla çok daha verimli ve sade bir hale getirebiliriz::
    
	#!/usr/bin/env python3

	soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")

	cevap = {"istanbul": "gök gürültülü ve sağanak yağışlı", 
                 "ankara": "açık ve güneşli", "izmir": "bulutlu"}

	print(cevap.get(soru, "Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır."))
    
clear()
********

Sözlüklerin, inceleyeceğimiz ilk metodu ``clear()``. Bu kelime İngilizce'de
"temizlemek" anlamına gelir. Görevi sözlükteki öğeleri temizlemektir. Yani içi
dolu bir sözlüğü bu metot yardımıyla tamamen boşaltabiliriz::
    
	>>> lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu", 
    ... "üçüncü": "Adana Gençlerbirliği"}

İsterseniz sözlüğümüzü boşaltmadan önce bu sözlükle biraz çalışalım:

Sözlüğümüzün öğelerine şöyle ulaşıyoruz::

	>>> lig

	{'şampiyon': 'Adana Demirspor', 'ikinci': 'Mersin İdman Yurdu', 
     'üçüncü': 'Adana Gençlerbirliği'}

Eğer bu sözlüğün öğelerine tek tek erişmek istersek şöyle yapıyoruz::

	>>> lig["şampiyon"]

	'Adana Demirspor'

	>>> lig["üçüncü"]

	'Adana Gençlerbirliği'

Şimdi geldi bu sözlüğün bütün öğelerini silmeye::

	>>> lig.clear()

Şimdi sözlüğümüzün durumunu tekrar kontrol edelim::

	>>> lig

	{}

Gördüğünüz gibi artık "lig" adlı sözlüğümüz bomboş. ``clear()`` metodunu
kullanarak bu sözlüğün bütün öğelerini sildik. Ama tabii ki bu şekilde sözlüğü
silmiş olmadık. Boş da olsa bellekte hâlâ "lig" adlı bir sözlük duruyor. Eğer
siz "lig"i ortadan kaldırmak isterseniz "del" adlı bir parçacıktan yararlanmanız
gerekir::
    
	>>> del lig

Kontrol edelim::

	>>> lig

	NameError: name 'lig' is not defined

Gördüğünüz gibi artık "lig" diye bir şey yok... Bu sözlüğü bellekten tamamen
kaldırdık.

``clear()`` adlı metodun ne olduğunu ve ne işe yaradığını gördüğümüze göre başka
bir metoda geçebiliriz.

copy()
*******

Diyelim ki elimizde şöyle bir sözlük var::

	>>> hava_durumu = {"İstanbul": "yağmurlu", "Adana": "güneşli", ... "İzmir": "bulutlu"}

Biz bu sözlüğü kopyalamak istiyoruz. Hemen şöyle bir şey deneyelim::

	>>> yedek_hava_durumu = hava_durumu

Artık elimizde aynı sözlükten iki tane var::

	>>> hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'İzmir': 'bulutlu'}

	>>> yedek_hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'İzmir': 'bulutlu'}

Şimdi hava_durumu adlı sözlüğe bir öğe ekleyelim::

	>>> hava_durumu["Mersin"] = "sisli"

	>>> hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'Mersin': 'sisli', 'İzmir': 'bulutlu'}

Şimdi bir de yedek_hava_durumu adlı sözlüğün durumuna bakalım::

	>>> yedek_hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'Mersin': 'sisli', 'İzmir': 'bulutlu'}

Gördüğünüz gibi, hava_durumu adlı sözlüğe yaptığımız ekleme yedek_hava_durumu
adlı sözlüğü de etkiledi. Hatırlarsanız buna benzer bir durumla daha önce
listeleri anlatırken de karşılaşmıştık. Çünkü varolan bir sözlüğü veya listeyi
başka bir değişkene atadığımızda aslında yaptığımız şey bir kopyalama işleminden
ziyade bellekteki aynı nesneye gönderme yapan iki farklı isim belirlemekten
ibaret. Yani sözlüğümüzü bellekteki bir nesne olarak düşünürsek, bu nesneye
atıfta bulunan, "hava_durumu" ve "yedek_hava_durumu" adlı iki farklı isim
belirlemiş oluyoruz. Eğer istediğimiz şey bellekteki nesneden iki adet
oluşturmak ve bu iki farklı nesneyi iki farklı isimle adlandırmak ise yukarıdaki
yöntemi kullanmak istemediğiniz sonuçlar doğurabilir. Yani amacınız bir sözlüğü
yedekleyip orijinal sözlüğü korumaksa ve yukarıdaki yöntemi kullandıysanız, hiç
farkında olmadan orijinal sözlüğü de değiştirebilirsiniz. İşte böyle durumlarda
imdadımıza sözlüklerin "copy" metodu yetişecek. Bu metodu kullanarak varolan bir
sözlüğü gerçek anlamda kopyalayabilir, yani yedekleyebiliriz... ::

	>>> hava_durumu = {"İstanbul": "yağmurlu", "Adana": "güneşli", ... "İzmir": "bulutlu"}

Şimdi bu sözlüğü yedekliyoruz. Yani kopyalıyoruz::

	>>> yedek_hava_durumu = hava_durumu.copy()

Bakalım hava_durumu adlı sözlüğe ekleme yapınca yedek_hava_durumu adlı sözlüğün
durumu ne oluyor? ::

	>>> hava_durumu["Mersin"] = "sisli"

	>>> hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'Mersin': 'sisli', 'İzmir':
	'bulutlu'}

yedek_hava_durumu adlı sözlüğe bakalım::

	>>> yedek_hava_durumu

	{'İstanbul': 'yağmurlu', 'Adana': 'güneşli', 'İzmir': 'bulutlu'}

Gördüğünüz gibi bu defa sözlüklerin birinde yapılan değişiklik öbürünü
etkilemedi... copy metodu sağolsun!...

fromkeys()
************

``fromkeys()`` metodu öteki metotlardan biraz farklıdır. Bu metot mevcut sözlük
üzerinde işlem yapmaz. ``fromkeys()``'in görevi yeni bir sözlük oluşturmaktır.
Bu metot yeni bir sözlük oluştururken listeler veya demetlerden yararlanır.
Şöyle ki::

	>>> elemanlar = "Ahmet", "Mehmet", "Can"

	>>> adresler = dict.fromkeys(elemanlar, "Kadıköy")

	>>> adresler

	{'Ahmet': 'Kadıköy', 'Mehmet': 'Kadıköy', 'Can': 'Kadıköy'}

Gördüğünüz gibi öncelikle "elemanlar" adlı bir demet tanımladık. Daha sonra da
"adresler" adlı bir sözlük tanımlayarak, ``fromkeys()`` metodu yardımıyla
anahtar olarak "elemanlar" demetindeki öğelerden oluşan, değer olarak ise
"Kadıköy"ü içeren bir sözlük meydana getirdik.

En başta tanımladığımız "elemanlar" demeti liste de olabilirdi. Hatta tek başına
bir karakter dizisi dahi yazabilirdik oraya...

pop()
******

Bu metodu listelerden hatırlıyoruz. Bu metot listelerle birlikte
kullanıldığında, listenin en son öğesini silip, silinen öğeyi de ekrana
basıyordu. Eğer bu metodu bir sıra numarası ile birlikte kullanırsak, listede o
sıra numarasına karşılık gelen öğe siliniyor ve silinen bu öğe ekrana
basılıyordu. Bu metodun sözlüklerdeki kullanımı da az çok buna benzer. Ama
burada farkı olarak, ``pop`` metodunu argümansız bir şekilde kullanamıyoruz.
Yani ``pop`` metodunun parantezi içinde mutlaka bir sözlük öğesi belirtmeliyiz::

	>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"), 
	... "içecekler": ("su", "kola", "ayran")}

	>>> sepet.pop("meyveler")

Bu komut, sözlükteki "meyveler" anahtarını silecek ve sildiği bu öğenin değerini
ekrana basacaktır. Eğer silmeye çalıştığımız anahtar sözlükte yoksa Python bize
bir hata mesajı gösterecektir::

	>>> sepet.pop("tatlılar")

	KeyError: 'tatlılar'

Bir program yazarken böyle bir durumla karşılaşmak istemeyiz çoğu zaman. Yani
bir sözlük içinde arama yaparken, aranan öğenin sözlükte bulunmadığı bir durumda
kullanıcıya mekanik ve anlamsız bir hata göstermek yerine, daha anlaşılır bir
mesaj iletmeyi tercih edebiliriz. Hatırlarsanız sözlüklerin ``get()`` metodunu
kullanarak benzer bir şey yapabiliyorduk. Şu anda incelemekte olduğumuz
``pop()`` metodu da bize böyle bir imkan verir. Bakalım::

	>>> sepet.pop("tatlılar", "Silinecek öğe yok!")

Böylelikle sözlükte bulunmayan bir öğeyi silmeye çalıştığımızda Python bize bir
hata mesajı göstermek yerine, "Silinecek öğe yok!" şeklinde daha anlamlı bir
mesaj verecektir...

popitem()
**********

``popitem()`` metodu da bir önceki bölümde öğrendiğimiz ``pop()`` metoduna
benzer. Bu iki metodun görevleri hemen hemen aynıdır. Ancak ``pop()`` metodu
parantez içinde bir parametre alırken, ``popitem()`` metodunun parantezi boş,
yani parametresiz olarak kullanılır. Bu metot bir sözlükten rastgele öğeler
silmek için kullanılır. Daha önce de pek çok kez söylediğimiz gibi, sözlükler
sırasız veri tipleridir. Dolayısıyla ``popitem()`` metodunun öğeleri silerken
kullanabileceği bir sıra kavramı yoktur. Bu yüzden bu metot öğeleri rastgele
silmeyi tercih eder... ::

	>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}

	>>> sepet.popitem()

Bu komut sözlükten rastgele bir anahtarı, değerleriyle birlikte sözlükten
silecektir. Eğer sözlük boşsa bu metot bize bir hata mesajı gösterir.

setdefault()
*************

Bu metot epey enteresan, ama bir o kadar da yararlı bir araçtır... Bu metodun
ne işe yaradığını doğrudan bir örnek üzerinde görelim::

	>>> sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}

	>>> sepet.setdefault("içecekler", ("su", "kola"))

Bu komut yardımıyla sözlüğümüz içinde "içecekler" adlı bir anahtar oluşturduk.
Bu anahtarın değeri ise `("su", "kola")` oldu... Bir de şuna bakalım::

	>>> sepet.setdefault("meyveler", ("erik", "çilek")) 
	
	('elma', 'armut')

Gördüğünüz gibi, sözlükte zaten "meyveler" adlı bir anahtar bulunduğu için,
Python aynı adı taşıyan ama değerleri farklı olan yeni bir "meyveler" anahtarı
oluşturmadı. Demek ki bu metot yardımıyla bir sözlük içinde arama yapabiliyor,
eğer aradığımız anahtar sözlükte yoksa, ``setdefault()`` metodu içinde
belirttiğimiz özellikleri taşıyan yeni bir anahtar-değer çifti
oluşturabiliyoruz.

update()
********

İnceleyeceğimiz son metot ``update()`` metodu... Bu metot yardımıyla
oluşturduğumuz sözlükleri yeni verilerle güncelleyeceğiz. Diyelim ki elimizde
şöyle bir sözlük var::

	>>> stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}

Stoğumuzda 5 adet elma, 10 adet armut, 6 kutu peynir, 15 adet de sosis var.
Diyelim ki daha sonraki zamanlarda bu stoğa mal giriş-çıkışı oldu ve stoğun son
hali şöyle::

	>>> yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

Yapmamız gereken şey, stoğumuzu yeni bilgilere göre güncellemek olacaktır. İşte
bu işlemi ``update()`` metodu ile yapabiliriz::

	>>> stok.update(yeni_stok)

	>>> print(stok)

	{'peynir': 8, 'elma': 3, 'sucuk': 6, 'sosis': 4, 'armut': 20}

Böylelikle malların son miktarlarına göre stok bilgilerimizi güncellemiş
olduk...





