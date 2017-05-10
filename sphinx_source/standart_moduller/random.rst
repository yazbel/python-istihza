.. meta::
   :description: Bu bölümde random modülünü inceleyeceğiz. 
   :keywords: python, modül, import, random

.. highlight:: py3

random Modülü
***************

Eğer yazdığınız programlarda, belirli bir aralıkta rastgele sayıların
üretilmesine ihtiyaç duyarsanız Python'ın standart kütüphanesinde bulunan
``random`` adlı bir modülü kullanabilirsiniz.

Tıpkı öteki modüllerde olduğu gibi, ``random`` modülü de birtakım faydalı
nitelik ve fonksiyonları barındırır. Biz bu bölümde, bu nitelik ve fonksiyonlar
arasında en sık kullanılanları inceleyeceğiz.

Elbette bu modülü kullanabilmek için öncelikle modülümüzü içe aktarmamız
gerekiyor::
    
    import random
    
Bu işlemin ardından, bu modülün bize sunduğu bütün işlevlerden yararlanabiliriz.

random()
=========

``random`` modülünün ``random()`` adlı fonksiyonunu kullanarak, `0.0` ile `1.0`
arasında rastgele bir kayan noktalı sayı üretebilirsiniz::
    
    >>> random.random()
    
    0.8064301704207291
    
``random()`` fonksiyonu, kendisini her çalıştırışınızda farklı bir kayan noktalı
sayı üretecektir::
    
    >>> random.random()

    0.6825988062501599
    
Üretilen sayıların 0 ile 1 arasında olduğunu özellikle dikkatinizi çekmek
isterim. 

Mesela bu fonksiyonu kullanarak, 0 ile 1 arası 10 tane sayı üretelim. Bu
sayıları gösterirken de noktadan sonra yalnızca dört basamak görüntülenmesine
izin verelim::
    
    >>> for i in range(10):
    ...     print("{:.4f}".format(random.random()))
    ...
    0.3094
    0.5277
    0.1588
    0.2832
    0.8742
    0.9989
    0.6847
    0.5672
    0.5529
    0.9717

uniform()
==========

Biraz önce gördüğümüz ``random()`` fonksiyonu, dikkat ederseniz herhangi bir
parametre almıyordu. Çünkü bu fonksiyonun tek görevi 0 ile 1 arası sayılar
üretmektir. Peki ya biz üreteceğimiz sayıların farklı bir aralıkta olmasını
istersek ne yapacağız? 

İşte, belirli bir aralıkta kayan noktalı sayılar üretmek istediğimizde,
``random()`` yerine ``uniform()`` adlı bir fonksiyon kullanacağız. Dikkatlice
inceleyim::
    
    >>> random.uniform(0.5, 1.5)
    
Bu kod, her çalıştırılışında `0.5` ile `1.5` arası rastgele bir kayan noktalı
sayı üretecektir::
    
    >>> random.uniform(0.5, 1.5)
    
    0.9624863371746406
    
    >>> random.uniform(0.5, 1.5)
    
    0.900446344810926
   

randint()
==========

Şimdiye kadar öğrendiğimiz ``random()`` ve ``uniform()`` fonksiyonları bize
yalnızca kayan noktalı sayılar üretme imkanı veriyordu. Ancak elbette biz kimi
durumlarda kayan noktalı sayılar yerine tam sayılar üretmek de isteyebiliriz.
İşte böyle bir durumda, ``random`` modülünün ``randint()`` adlı başka bir
fonksiyonunu kullanabiliriz. 

Mesela `45` ile `500` arasında rastgele bir sayı üretmek isterseniz,
``randint()`` fonksiyonunu şu şekilde kullanabilirsiniz::
    
    >>> random.randint(45, 500)
    
Bu fonksiyon, her çalıştırılışında `45` ile `500` arasında rastgele bir tam sayı
üretecektir.

choice()
========

``random`` modülünün ``choice()`` adlı fonksiyonunu kullanarak, dizi niteliği
taşıyan veri tiplerinden rastgele öğeler seçebiliriz. Bu tanım biraz anlaşılmaz
gelmiş olabilir. O yüzden bunu bir örnekle açıklayalım.

Diyelim ki elimizde şöyle bir liste var::
    
    >>> liste = ['ali', 'veli', 'ahmet', 
    ... 'mehmet', 'celal', 'selin', 'nihat']
    
Bildiğiniz gibi, listeler, dizi niteliği taşıyan veri tipleridir. Dolayısıyla
``choice()`` fonksiyonunu kullanarak bu diziden rastgele bir öğe seçebiliriz::
    
    >>> liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat']
    
    >>> random.choice(liste)
    
    'ali'
    
    >>> random.choice(liste)
    
    'mehmet'
    
    >>> random.choice(liste)
    
    'selin'
    
Tıpkı bu örnekte olduğu gibi, karakter dizileri de dizi niteliği taşıyan bir
veri tipi olduğu için, ``choice()`` fonksiyonuna cevap verir::
    
    >>> kardiz = 'istihza'
    >>> random.choice(kardiz)
    
    'i'
    
Peki acaba bu 'i' harfi karakter dizisinin başındaki 'i' harfi mi, yoksa
ortasındaki 'i' harfi mi? Sizce bunu nasıl anlayabiliriz?

shuffle()
===========

``shuffle()`` fonksiyonunu kullanarak, dizi niteliği taşıyan veri tiplerindeki
öğeleri karıştırabilirsiniz (yani öğelerin sırasını karışık bir hale
getirebilirsiniz). Mesela::
    
    >>> l = list(range(10))
    
10 öğeli bir listemiz var. Bu listedeki öğeler `0`'dan `10`'a kadar düzgün bir
şekilde sıralanmış::
    
    >>> l
    
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
Şimdi biz ``shuffle()`` fonksiyonunu kullanarak öğeleri karıştıracağız::
    
    >>> random.shuffle(l)
    >>> l
    
    [8, 0, 7, 9, 1, 4, 6, 5, 3, 2]
    
Burada dikkat etmemiz gereken önemli nokta, ``shuffle()`` fonksiyonunun, özgün
listenin kendisi üzerinde değişiklik yapıyor oluşudur. Yani liste üzerinde
``shuffle()`` metodunu uyguladıktan sonra artık özgün listeyi kaybediyoruz.
Dolayısıyla elimizde artık öğeleri 0'dan 10'a kadar düzgün bir şekilde
sıralanmış liste yok. Onun yerine, öğeleri karıştırılmış bir liste var elimizde.

Liste üzerine ``shuffle()`` fonksiyonunu her uygulayışınızda özgün listenin
öğeleri bir daha karıştırılacaktır.

Peki size bir soru...

Elinizde şöyle bir liste var:

    arkadaşlar = ['ali', 'veli', 'mehmet', 'ahmet', 'serkan', 'selin']
    
Görevimiz bu listenin öğelerini karıştırmak. Ama biz aynı zamanda özgün
`arkadaşlar` listesindeki öğe sıralamasını da kaybetmek istemiyoruz. Bunu nasıl
başarabiliriz?

randrange()
=============

``randrange()`` fonksiyonu, yukarıda öğrendiğimiz ``randint()`` fonksiyonu ile
aynı işi yapar. Yani her iki fonksiyon da, belli bir aralıkta rastgele
tamsayılar üretir. Ancak aralarında iki ufak fark bulunur. 

İlk önce birincisine bakalım...

Dikkatlice inceleyin:

    >>> random.randrage(10)
    
    5
    
Gördüğünüz gibi, ``randrange()`` fonksiyonunu tek parametre ile
kullanabiliyoruz. Yukarıdaki komutu eğer ``randint()`` ile yazmak istersek şunu
yapmamız gerekir::
    
    >>> random.randint(0, 10)
    
``randrange()`` fonksiyonundan farklı olarak, ``randint()`` fonksiyonunu iki
parametre ile kullanmamız gerekir. Eğer bu fonksiyona tek parametre verirsek
hata alırız::
    
    >>> random.randint(10)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: randint() missing 1 required positional argument: 'b'

Elbette, eğer istersek ``randrange()`` fonksiyonunu da çift parametre ile
kullanarak, farklı bir sayı aralığı belirtme imkanına sahibiz::
    
    >>> random.randrange(10, 500)
    
Bu komut, `10` ile `500` arası rastgele tam sayılar üretecektir. Ayrıca bu komut
şununla da eşdeğerdir::
    
    >>> random.randint(10, 500)
    
Bu iki fonksiyon arasındaki ikinci fark ise, rastgele sayı üretilecek aralığın
son değeridir. Bu muğlak ifadeyi bir örnekle anlaşılır hale getirmeye
çalışalım::
    
    >>> random.randrange(10, 20)
    
Bu komut, `10` ile `20` arasında rastgele bir sayı üretir. Üretilecek en düşük
sayı `10` iken, en büyük sayı ise `19` olacaktır. `20` sayısı asla üretilmez. 

Bir de şuna bakalım::
    
    >>> random.randint(10, 20)
    
Burada da yime `10` ile `20` arasında rastgele bir sayı üretilir. Tıpkı
``randrange()`` metodunda olduğu gibi, üretilecek en düşük sayı `10`'dur. Ancak
en büyük sayı `20` olacaktır.

Bu iki fonksiyonu kullanırken bu farklılığa dikkat etmemiz gerekir. Aksi halde
yazdığımız programlar hatalı çalışabilir.

Peki size bir soru: Acaba ``randint()`` ile ``randrange()`` arasındaki bu farkı
nasıl kanıtlarsınız?


sample()
==========

'Sample' kelimesi 'numune' anlamına gelir. İşte kelimenin bu anlamına paralel
olarak ``sample()`` fonksiyonu da, dizi niteliği taşıyan veri tiplerinden belli
sayıda numune alınabilmesini sağlar. Bakınız::
    
    >>> liste = range(100)
    
100 öğeli bir liste oluşturduk. Şimdi bu listeden 5 tane rastgele numune
alalım::
    
    >>> random.sample(liste, 5)
    
    [56, 74, 2, 3, 80]
    
Gördüğünüz gibi, ``sample()`` fonksiyonunun ilk parametresi numune alınacak
diziyi, ikinci parametresi ise bu diziden kaç tane numune alınacağını
gösteriyor.