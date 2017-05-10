.. meta::
   :description: Bu bölümde listelerin ve demetlerin metotlarını inceleyeceğiz.
   :keywords: python, listeler, demetler, append, count, extend, index, insert, pop, remove, reverse, sort

.. highlight:: py3

**************************************
Listelerin ve Demetlerin Metotları
**************************************

Listelerin Metotları
**********************

Burada, geçen bölümde kaldığımız yerden devam edeceğiz listeleri anlatmaya.
Ağırlıklı olarak bu bölümde listelerin metotlarından söz edeceğiz. 'Metot'
kavramını karakter dizilerinden hatırlıyorsunuz. Karakter dizilerini anlatırken
bol miktarda metot görmüştük.

Python'da bütün veri tipleri bize birtakım metotlar sunar. Bu metotlar
yardımıyla, ilgili veri tipi üzerinde önemli değişiklikler veya sorgulamalar
yapabiliyoruz.

Hatırlarsanız bir veri tipinin hangi metotlara sahip olduğunu görmek için
``dir()`` fonksiyonundan yararlanıyorduk. Listelerde de durum farklı değil.
Dolayısıyla şu komut bize listelerin metotlarını sıralayacaktır::
    
    >>> dir(list)

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
     '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
     '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
     '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
     '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
     '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
     'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
     'remove', 'reverse', 'sort']

Gördüğünüz gibi, tıpkı karakter dizilerinde olduğu gibi, listelerin metotlarını
görmek için de ``dir()`` fonksiyonuna parametre olarak veri tipinin teknik adını
veriyoruz. Python'da listelerin teknik adı `list` olduğu için bu komutu
``dir(list)`` şeklinde kullanıyoruz. Elbette, eğer istersek, listelerin
metotlarını almak için herhangi bir listeyi de kullanabiliriz. Mesela boş bir
liste kullanalım::
    
    >>> dir([])

Bu komut da ``dir(list)`` ile aynı çıktıyı verecektir. Bu listede bizi
ilgilendiren metotlar ise şunlardır::
    
    >>> [i for i in dir(list) if not "_" in i]
    
    ['append', 'clear', 'copy', 'count', 'extend', 'index', 
     'insert', 'pop', 'remove', 'reverse', 'sort']

Metotlar, bir programcının hayatını önemli ölçüde kolaylaştıran araçlardır. Bu
yüzden, 'Listeler' konusunun ilk bölümünde öğrendiğimiz listeye öğe ekleme, öğe
çıkarma, öğe değiştirme, öğe silme gibi işlemleri orada anlattığımız yöntemlerle
değil, biraz sonra göreceğimiz metotlar aracılığıyla yapmayı tercih edeceğiz.
Ama tabii ki, metotları tercih edecek olmamız, birinci bölümde anlattığımız
yöntemleri bir kenara atmanızı gerektirmez. Unutmayın, bir dildeki herhangi bir
özelliği siz kullanmasanız bile, etrafta bu özelliği kullanan başka programcılar
var. Dolayısıyla en azından başkalarının yazdığı kodları anlayabilmek için dahi
olsa, kendinizin kullanmayacağınız yöntem ve yolları öğrenmeniz gerekir.

``append()`` metoduyla başlayalım...

append()
===========

*append* kelimesi İngilizcede 'eklemek, ilave etmek, iliştirmek' gibi anlamlara
gelir. ``append()`` metodunun görevi de kelime anlamıyla uyumludur. Bu metodu,
bir listeye öğe eklemek için kullanıyoruz. Mesela::
    
    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.append("erik")

Bu metot, yeni öğeyi listenin en sonuna ekler. Mesela yukarıdaki örnekte
`"erik"` adlı karakter dizisi listede `"çilek"` adlı karakter dizisinin sağına
eklendi.

Hatırlarsanız bir önceki bölümde listeye öğe ekleme işini `+` işleci ile de
yapabileceğimizi söylemiştik. Dolayısıyla, aslında yukarıdaki kodu şöyle de
yazabiliriz::
    
    >>> liste = ["elma", "armut", "çilek"]
    >>> liste = liste + ["erik"]
    >>> print(liste)
    
    ['elma', 'armut', 'çilek', 'erik']

Bu iki yöntem birbiriyle aynı sonucu verse de hem pratiklik hem de işleyiş
bakımından bu iki yöntemin birbirinden farklı olduğunu görüyoruz.

Pratiklik açısından bakarsak, ``append()`` metodununu kullanmanın `+` işlecini
kullanmaya kıyasla daha kolay olduğunu herhalde kimse reddetmeyecektir. Bu iki
yöntem işleyiş bakımından da birbirinden ayrılıyor. Zira `+` işlecini
kullandığımızda listeye yeni bir öğe eklerken aslında `liste` adlı başka bir
liste daha oluşturmuş oluyoruz. Hatırlarsanız önceki bölümlerde listelerin
değiştirilebilir (*mutable*) veri tipleri olduğunu söylemiştik. İşte
``append()`` metodu sayesinde listelerin bu özelliğinden sonuna kadar
yararlanabiliyoruz. `+` işlecini kullandığımızda ise, orijinal listeyi
değiştirmek yerine yeni bir liste oluşturduğumuz için, sanki listelere karakter
dizisi muamelesi yapmış gibi oluyoruz. Gördüğünüz gibi, listeye ``append()``
metodunu uyguladıktan sonra bunu bir değişkene atamamıza gerek kalmıyor.
``append()`` metodu orijinal liste üzerinde doğrudan değişiklik yapmamıza izin
verdiği için daha az kod yazmamızı ve programımızın daha performanslı
çalışmasını sağlıyor.

`+` işleci ile ``append()`` metodu işlev olarak birbirine benzese de bu iki
yöntem arasında önemli farklılıklar da vardır. Mesela şu örneğe bir göz atalım::
    
    işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
    platformlar = ["IPhone", "Android", "S60"]
    hepsi = işletim_sistemleri + platformlar
    print(hepsi)
    
    ['Windows', 'GNU/Linux', 'Mac OS X', 'IPhone', 'Android', 'S60']

Burada iki farklı listeyi, `+` işleci kullanarak birleştirdik. Aynı işi
``append()`` metoduyla şu şekilde yapabiliriz::
    
    işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
    platformlar = ["IPhone", "Android", "S60"]
    for i in platformlar:
        işletim_sistemleri.append(i)

    print(işletim_sistemleri)

Burada `platformlar` adlı liste üzerinde bir ``for`` döngüsü kurmamızın nedeni,
``append()`` metodunun yalnızca tek bir parametre alabilmesidir. Yani bu metodu
kullanarak bir listeye birden fazla öğe ekleyemezsiniz::
    
    >>> liste = [1, 2, 3]
    >>> liste.append(4, 5, 6)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: append() takes exactly one argument (3 given)

Bu sebeple, ekleyeceğiniz listenin öğeleri üzerinde bir ``for`` döngüsü kurmanız
gerekir::
    
    >>> liste = [1, 2, 3]
    >>> for i in [4, 5, 6]:
    ...     liste.append(i)
    ...
    >>> print(liste)
    
    [1, 2, 3, 4, 5, 6]

Bir listeye birden fazla öğe eklemek için aklınıza şöyle bir yöntem de gelmiş
olabilir::
    
    >>> liste = [1, 2, 3]
    >>> liste.append([4, 5, 6])

Ancak bu komutun çıktısı pek beklediğiniz gibi olmayabilir::

    >>> print(liste)
    
    [1, 2, 3, [4, 5, 6]]

Gördüğünüz gibi, ``[4, 5, 6]`` öğesi listeye tek parça olarak eklendi. Eğer
istediğiniz şey buysa ne âlâ! Ama değilse, ``for`` döngüsü ya da `+` işleci ile
istediğiniz çıktıyı elde edebilirsiniz.

Şöyle bir örnek daha düşünün: Diyelim ki kullanıcının girdiği bütün sayıları
birbiriyle çarpan bir uygulama yazmak istiyoruz. Bunun için şöyle bir kod
yazabiliriz::
    
    sonuç = 1

    while True:
        sayı = input("sayı (hesaplamak için q): ")
        if sayı == "q":
            break
        
        sonuç *= int(sayı)

    print(sonuç) 

Burada kullanıcı her döngüde bir sayı girecek ve programımız girilen bu sayıyı
`sonuç` değişkeninin o anki değeriyle çarparak yine `sonuç` değişkenine
gönderecek. Böylece kullanıcı tarafından girilen bütün sayıların çarpımını elde
etmiş olacağız. Kullanıcının 'q' harfine basmasıyla birlikte de `sonuç`
değişkeninin değeri ekranda görünecek. Yalnız burada birkaç sorun var. Diyelim
ki kullanıcı hiçbir sayı girmeden 'q' harfine basarsa, `sonuç` değişkeninin `1`
olan değeri ekranda görünecek ve bu şekilde kullanıcı yanlış bir sonuç elde
etmiş olacak. Ayrıca çarpma işlemi için en az `2` adet sayı gerekiyor.
Dolayısıyla kullanıcı `2`'den az sayı girerse de programımız yanlış sonuç
verecektir. Kullanıcının yeterli miktarda sayı girip girmediğini tespit
edebilmek için yine listelerden ve listelerin ``append()`` metodundan
yararlanabiliriz::
    
    kontrol = []
    sonuç = 1

    while True:
        sayı = input("sayı (hesaplamak için q): ")
        if sayı == "q":
            break
        kontrol.append(sayı)
        sonuç *= int(sayı)

    if len(kontrol) < 2:
        print("Yeterli sayı girilmedi!")
    else:
        print(sonuç) 

Burada önceki koda ilave olarak, `kontrol` adlı boş bir liste tanımladık. Bu
liste kullanıcının girdiği sayıları depolayacak. Bir önceki örnekte kullanıcının
girdiği sayıları hiçbir yerde depolamadık. Orada yaptığımız şey her döngüde
kullanıcı tarafından girilen sayıyı `sonuç` değişkeninin değeriyle çarpıp yine
`sonuç` değişkenine göndermekti. Dolayısıyla kullanıcı tarafından girilen
sayılar bir yerde tutulmadığı için kaybolup gidiyordu. Burada ise `kontrol` adlı
liste, kullanıcı tarafından girilen sayıları tuttuğu için, bu sayıları daha
sonra istediğimiz gibi kullanabilme imkanına kavuşuyoruz.

Ayrıca bu ikinci kodlarda `kontrol` değişkeninin boyutuna bakarak kullanıcının
`2`'den az sayı girip girmediğini denetliyoruz. Eğer `kontrol` listesinin
uzunluğu `2`'den azsa kullanıcı çarpma işlemi için yeterli sayı girmemiş
demektir. Böyle bir durumda çarpma işlemini yapmak yerine, kullanıcıya 'Yeterli
sayı girilmedi!' şeklinde bir uyarı mesajı gösteriyoruz.

``append()`` metodu listelerin en önemli metotlarından biridir. Hem kendi
yazdığınız, hem de başkalarının yazdığı programlarda ``append()`` metodunu sıkça
göreceksiniz. Dolayısıyla listelerin hiçbir metodunu bilmeseniz bile
``append()`` metodunu öğrenmelisiniz.

extend()
==========

*extend* kelimesi İngilizcede 'genişletmek, yaymak' gibi anlamlara gelir. İşte
``extend()`` adlı metot da kelime anlamına uygun olarak listeleri 'genişletir'.

Şöyle bir düşündüğünüzde ``extend()`` metodunun ``append()`` metoduyla aynı işi
yaptığını zannedebilirsiniz. Ama aslında bu iki metot işleyiş olarak birbirinden
çok farklıdır.

``append()`` metodunu kullanarak yazdığımız şu koda dikkatlice bakın::

    li1 = [1, 3, 4]
    li2 = [10, 11, 12]
    li1. append(li2)

    print(li1)

``append()`` metodunu anlatırken söylediğimiz gibi, bu metot bir listeye her
defasında sadece tek bir öğe eklenmesine izin verir. Yukarıda olduğu gibi, eğer
bu metodu kullanarak bir listeye yine bir liste eklemeye çalışırsanız,
eklediğiniz liste tek bir öğe olarak eklenecektir. Yani yukarıdaki kodlar size
şöyle bir çıktı verecektir::
    
    [1, 3, 4, [10, 11, 12]]

Gördüğünüz gibi, `[10, 11, 12]` listesi öteki listeye tek bir liste halinde
eklendi. İşte ``extend()`` metodu bu tür durumlarda işinize yarayabilir. Mesela
yukarıdaki örneği bir de ``extend()`` metodunu kullanarak yazalım::
    
    li1 = [1, 3, 4]
    li2 = [10, 11, 12]
    li1. extend(li2)

    print(li1)

Bu defa şöyle bir çıktı alıyoruz::

    [1, 3, 4, 10, 11, 12]

Gördüğünüz gibi, ``extend()`` metodu tam da kelime anlamına uygun olarak listeyi
yeni öğelerle genişletti.

Hatırlarsanız ``append()`` metodunu anlatırken şöyle bir örnek vermiştik::

    işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
    platformlar = ["IPhone", "Android", "S60"]
    hepsi = işletim_sistemleri + platformlar
    print(hepsi)

Burada `+` işlecini kullanarak `işletim_sistemleri` ve `platformlar` adlı
listeleri birleştirerek `hepsi` adlı tek bir liste elde ettik. Aynı etkiyi
``append()`` metodunu kullanarak şu şekilde elde edebileceğimizi de söylemiştik
orada::
    
    işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
    platformlar = ["IPhone", "Android", "S60"]
    for i in platformlar:
        işletim_sistemleri.append(i)

    print(işletim_sistemleri)

Esasında, ``append()`` metodunu kullanmaya kıyasla, burada `+` işlecini
kullanmak sanki daha pratikmiş gibi görünüyor. Bir de şuna bakın::
    
    işletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
    platformlar = ["IPhone", "Android", "S60"]
    işletim_sistemleri.extend(platformlar)
    print(işletim_sistemleri) 

Gördüğünüz gibi, bu örnekte ``extend()`` metodunu kullanmak ``append()``
metodunu kullanmaya göre daha pratik ve makul. Çünkü bir listeye tek tek öğe
eklemek açısından ``append()`` metodu daha uygundur, ama eğer yukarıda olduğu
gibi bir listeye başka bir liste ekleyeceksek ``extend()`` metodunu kullanmayı
tercih edebiliriz.

insert()
===========

Bildiğiniz gibi, `+` işleci, ``append()`` ve ``extend()`` metotları öğeleri
listenin sonuna ekliyor. Peki biz bir öğeyi listenin sonuna değil de, liste
içinde başka bir konuma eklemek istersek ne yapacağız? İşte bunun için
``insert()`` adlı başka bir metottan yararlanacağız.

*insert* kelimesi 'yerleştirmek, sokmak' gibi anlamlara gelir. ``insert()``
metodu da bu anlama uygun olarak, öğeleri listenin istediğimiz bir konumuna
yerleştirir. Dikkatlice inceleyin::
    
    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.insert(0, "erik")
    >>> print(liste)
    
    ['erik', 'elma', 'armut', 'çilek']

Gördüğünüz gibi ``insert()`` metodu iki parametre alıyor. İlk parametre, öğenin
hangi konuma yerleştirileceğini, ikinci parametre ise yerleştirilecek öğenin ne
olduğunu gösteriyor. Yukarıdaki örnekte `"erik"` öğesini listenin `0.` konumuna,
yani listenin en başına yerleştiriyoruz.

``ìnsert()`` metodu özellikle dosya işlemlerinde işinize yarar. Diyelim ki
elimizde içeriği şöyle olan `deneme.txt` adlı bir dosya var::

    Ahmet Özkoparan
    Mehmet Veli
    Serdar Güzel
    Zeynep Güz

Bizim amacımız, 'Ahmet Özkoparan' satırından sonra 'Ferhat Yaz' diye bir satır
daha eklemek. Yani dosyamızı şu hale getirmek istiyoruz::
    
    Ahmet Özkoparan
    Ferhat Yaz
    Mehmet Veli
    Serdar Güzel
    Zeynep Güz

Biz henüz Python'da dosya işlemlerinin nasıl yapılacağını öğrenmedik. Ama
hatırlarsanız bundan önceki bölümlerde birkaç yerde ``open()`` adlı bir
fonksiyondan bahsetmiş ve bu fonksiyonun dosya işlemlerinde kullanıldığını
söylemiştik. Mesela yukarıda bahsettiğimiz `deneme.txt` adlı dosyayı açmak için
``open()`` fonksiyonunu şu şekilde kullanabiliriz::
    
    f = open("deneme.txt", "r")

Burada `deneme.txt` adlı dosyayı okuma modunda açmış olduk. Şimdi dosya
içeriğini okuyalım::
    
    içerik = f.readlines()

Bu satır sayesinde dosya içeriğini bir liste halinde alabildik. Eğer yukarıdaki
kodlara şu eklemeyi yaparsanız, dosya içeriğini görebilirsiniz::
    
    print(içerik)
    
    ['Ahmet Özkoparan\n', 'Mehmet Veli\n', 'Serdar Güzel\n', 'Zeynep Güz\n', '\n']

Gördüğünüz gibi, dosya içeriği basit bir listeden ibaret. Dolayısıyla listelerle
yapabildiğimiz her şeyi `içerik` adlı değişkenle de yapabiliriz. Yani bu listeye
öğe ekleyebilir, listeden öğe çıkarabilir ya da bu listeyi başka bir liste ile
birleştirebiliriz.

Dosya içeriğini bir liste olarak aldığımıza göre şimdi bu listeye `"Ahmet
Özkoparan"` öğesinden sonra `"Ferhat Yaz"` öğesini ekleyelim. Dikkatlice bakın::
    
    içerik.insert(1, "Ferhat Yaz\n")

Dediğimiz gibi, ``f.readlines()`` satırı bize dosya içeriğini bir liste olarak
verdi. Amacımız `"Ahmet Özkoparan"` öğesinden sonra `"Ferhat Yaz"` öğesini
eklemek. Bunun için, liste metotlarından biri olan ``insert()`` metodunu
kullanarak listenin `1.` sırasına `"Ferhat Yaz"` öğesini ekledik. Burada
`"Ferhat Yaz"` öğesine `\n` adlı satır başı karakterini de ilave ettiğimize
dikkat edin. Bu eklemeyi neden yaptığımızı anlamak için satır başı karakterini
çıkarmayı deneyebilirsiniz.

`içerik` adlı değişkenin değerini istediğimiz biçime getirdiğimize göre bu
listeyi tekrar `deneme.txt` adlı dosyaya yazabiliriz. Ama bunun için öncelikle
`deneme.txt` adlı dosyayı yazma modunda açmamız gerekiyor. Python'da dosyalar ya
okuma ya da yazma modunda açılabilir. Okuma modunda açılan bir dosyaya
yazılamaz. O yüzden dosyamızı bir de yazma modunda açmamız gerekiyor::
    
    g = open("deneme.txt", "w")

``open()`` fonksiyonunun ilk parametresi dosya adını gösterirken, ikinci
parametresi dosyanın hangi modda açılacağını gösteriyor. Biz burada `deneme.txt`
adlı dosyayı yazma modunda açtık. Buradaki `"w"` parametresi İngilizcede
'yazmak' anlamına gelen *write* kelimesinin ilk harfidir. Biraz önce ise
`deneme.txt` dosyasını `"r"`, yani okuma (*read*) modunda açmıştık.

Dosyamız artık üzerine yazmaya hazır. Dikkatlice bakın::

    g.writelines(içerik)

Burada, biraz önce istediğimiz biçime getirdiğimiz `içerik` adlı listeyi doğruda
dosyaya yazdık. Bu işlem için ``writelines()`` adlı özel bir metottan
yararlandık. Bu metotları birkaç bölüm sonra ayrıntılı olarak inceleyeceğiz. Biz
şimdilik sadece sonuca odaklanalım.

Yapmamız gereken son işlem, açık dosyaları kapatmak olmalı::

    f.close()
    g.close()

Şimdi kodlara topluca bir bakalım::

    f = open("deneme.txt", "r")
    içerik = f.readlines()
    içerik.insert(1, "Ferhat Yaz\n")

    g = open("deneme.txt", "w")
    g.writelines(içerik)
    
    f.close()
    g.close()

Gördüğünüz gibi yaptığımız işlem şu basamaklardan oluşuyor:

    #. Öncelikle dosyamızı okuma modunda açıyoruz (``f = open("deneme.txt", "r")``)
    
    #. Ardından dosya içeriğini bir liste olarak alıyoruz (``içerik = f.readlines()``)
    
    #. Aldığımız bu listenin `2.` sırasına `"Ferhat Yaz"` öğesini ekliyoruz
       (``içerik.insert(1, "Ferhat Yaz\n")``)
    
    #. Listeyi istediğimiz şekle getirdikten sonra bu defa dosyamızı yazma
       modunda açıyoruz (``g = open("deneme.txt", "w")``)
    
    #. Biraz önce düzenlediğimiz listeyi dosyaya yazıyoruz (``g.writelines(içerik)``)
    
    #. Son olarak da, hem yaptığımız değişikliklerin etkin hale gelebilmesi 
       hem de işletim sisteminin programımıza tahsis ettiği kaynakların serbest
       kalması için dosyalarımızı kapatıyoruz (``f.close()`` ve ``g.close()``)
    
Burada ``insert()`` metodunun bize nasıl kolaylık sağladığına dikkat edin.
``insert()`` metodu da listelerin önemli metotlarından biridir ve dediğimiz
gibi, özellikle dosyaları manipüle ederken epey işimize yarar.

remove()
==========

Bu metot listeden öğe silmemizi sağlar. Örneğin::

    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.remove("elma")
    >>> liste
    
    ['armut', 'çilek']

reverse()
===========

Daha önce verdiğimiz örneklerde, liste öğelerini ters çevirmek için dilimleme
yöntemini kullanabileceğimizi öğrenmiştik::
    
    >>> meyveler = ["elma", "armut", "çilek", "kiraz"]
    >>> meyveler[::-1]
    
    ['kiraz', 'çilek', 'armut', 'elma']


Eğer istersek, bu iş için, karakter dizilerini incelerken öğrendiğimiz
``reversed()`` fonksiyonunu da kullanabiliriz::
    
    >>> reversed(meyveler)

Bu komut bize şu çıktıyı verir::

    <list_reverseiterator object at 0x00DC9810>

Demek ki ``reversed()`` fonksiyonunu bir liste üzerine uyguladığımızda
'list_reverseiterator' adı verilen bir nesne elde ediyoruz. Bu nesnenin
içeriğini görmek için birkaç farklı yöntemden yararlanabiliriz. Örneğin::
    
    >>> print(*reversed(meyveler))
    
    kiraz çilek armut elma

... veya::

    >>> print(list(reversed(meyveler)))
    
    ['kiraz', 'çilek', 'armut', 'elma']

... ya da::

    >>> for i in reversed(meyveler):
    ...     print(i)
    ...
    kiraz
    çilek
    armut
    elma

Gördüğünüz gibi, Python'da bir listeyi ters çevirmenin pek çok yöntemi var.
Dilerseniz şimdi bu yöntemlere bir tane daha ekleyelim.

Python'da listelerin öğelerini ters çevirmek için yukarıdaki yöntemlere ek
olarak listelerin ``reverse()`` metodunu da kullanabilirsiniz::
    
    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.reverse()
    >>> liste
    
    ['çilek', 'armut', 'elma']

İhtiyacınız olan çıktının türüne ve şekline göre yukarıdaki yöntemlerden
herhangi birini tercih edebilirsiniz.

pop()
=======

Tıpkı ``remove()`` metodu gibi, bu metot da bir listeden öğe silmemizi sağlar::

    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.pop()

Ancak bu metot, ``remove()`` metodundan biraz farklı davranır. ``pop()``
metodunu kullanarak bir liste öğesini sildiğimizde, silinen öğe ekrana
basılacaktır. Bu metot parametresiz olarak kullanıldığında listenin son öğesini
listeden atar. Alternatif olarak, bu metodu bir parametre ile birlikte de
kullanabilirsiniz. Örneğin::
    
    >>> liste.pop(0)

Bu komut listenin `0.` öğesini listeden atar ve atılan öğeyi ekrana basar.

sort()
=======

Yine listelerin önemli bir metodu ile karşı karşıyayız. ``sort()`` adlı bu
önemli metot bir listenin öğelerini belli bir ölçüte göre sıraya dizmemizi
sağlar. Basit bir örnek verelim. Diyelim ki elimizde şöyle bir liste var::
    
    üyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 
              'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem', 
              'Sinem', 'Tayfun', 'Tuna', 'Tolga']

Bu listedeki isimleri mesela alfabe sırasına dizmek için ``sort()`` metodunu
kullanabiliriz::
    
    >>> üyeler.sort()
    >>> print(üyeler)

    ['Abdullah', 'Ahmet', 'Ceylan', 'Kadir', 'Kamil', 'Kemal', 'Mahmut', 
     'Mehmet', 'Selin', 'Senem', 'Seyhan', 'Sinem', 'Tayfun', 'Tolga', 
     'Tuna', 'Zeynep']

Bu metot elbette yalnızca harfleri alfabe sırasına dizmek için değil sayıları
sıralamak için de kullanılabilir::
    
    >>> sayılar = [1, 0, -1, 4, 10, 3, 6]
    >>> sayılar.sort()
    >>> print(sayılar)
    
    [-1, 0, 1, 3, 4, 6, 10]

Gördüğünüz gibi, ``sort()`` metodu öğeleri artan sıralamaya tabi tutuyor. Yani
öğeler 'a, b, c' veya 1, 2, 3 şeklinde sıralanıyor. Bunun tersini yapmak da
mümkündür. Yani istersek Python'ın sıralama işlemini 'c, b, a' şeklinde
yapmasını da sağlayabiliriz. Bunun için ``sort()`` metodunun `reverse`
parametresini kullanacağız::
    
    >>> üyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep', 
                  'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem', 
                 'Sinem', 'Tayfun', 'Tuna', 'Tolga']
    
    >>> üyeler.sort(reverse=True)

Gördüğünüz gibi ``sort()`` metodunun `reverse` adlı bir parametresine verdiğimiz
`True` değeri sayesinde liste öğelerini ters sıraladık. Bu parametrenin
öntanımlı değeri `False`'tur. Yani ``sort()`` metodu öntanımlı olarak öğeleri
artıra artıra sıralar. Öğeleri azalta azalta sıralamak için `reverse`
parametresinin `False` olan öntanımlı değerini `True` yapmamız yeterli
olacaktır.

Gelin isterseniz ``sort()`` metodunu kullanarak bir örnek daha verelim. Elimizde
şöyle bir liste olsun::

    >>> isimler = ["Ahmet", "Işık", "İsmail", "Çiğdem", "Can", "Şule"]

Bu listedeki isimleri alfabe sırasına dizelim::

    >>> isimler.sort()
    >>> isimler
    
    ['Ahmet', 'Can', 'Işık', 'Çiğdem', 'İsmail', 'Şule']

Gördüğünüz gibi, çıktı pek beklediğimiz gibi değil. Tıpkı karakter dizilerini
anlatırken öğrendiğimiz ``sorted()`` fonksiyonunda olduğu gibi, listelerin
``sort()`` metodu da Türkçe karakterleri düzgün sıralayamaz. Eğer Türkçe
karakterleri sıralamamız gereken bir program yazıyorsak bizim ``sort()``
metodunun işleyişine müdahale etmemiz gerekir. Temel olarak, ``sorted()``
fonksiyonunu anlatırken söylediklerimiz burada da geçerlidir. Orada
bahsettiğimiz ``locale`` modülü burada da çoğu durumda işimizi halletmemizi
sağlar. Ama ``sorted()`` fonksiyonunu anlatırken de söylediğimiz gibi,
``locale`` modülü burada da 'i' ve 'ı' harflerini düzgün sıralayamaz. Türkçe
harflerin tamamını düzgün sıralayabilmek için şöyle bir kod yazabiliriz::
    
    harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    çevrim = {harf: harfler.index(harf) for harf in harfler}

           
    isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]

    isimler.sort(key=lambda x: çevrim.get(x[0]))

    print(isimler)

Bu kodların bir kısmını anlayabiliyor, bir kısmını ise anlayamıyor
olabilirsiniz. Çünkü burada henüz işlemediğimiz konular var. Zamanı geldiğinde
bu kodların tamamını anlayabilecek duruma geleceksiniz. Siz şimdilik sadece bu
kodlardan ne çıkarabildiğinize bakın yeter. Zaten bizim buradaki amacımız,
``sort()`` metodunun Türkçe harfleri de düzgün bir şekilde sıralayabileceğini
göstermekten ibarettir.

Bu arada ufak bir uyarı yapmadan geçmeyelim: Yukarıdaki kodlar da esasında
Türkçe kelimeleri tam anlamıyla düzgün bir şekilde sıralamak için yeterli değil.
'Gömülü Fonksiyonlar' konusunu incelerken, yeri geldiğinde bu konuya tekrar
değinip, Türkçe kelimelerin nasıl doğru, tam ve eksiksiz bir biçimde
sıralanacağını da tüm ayrıntılarıyla inceleyeceğiz. 

index()
=========

Karakter dizileri konusunu anlatırken bu veri tipinin ``index()`` adlı bir
metodu olduğundan söz etmiştik hatırlarsanız. İşte liste veri tipinin de
``index()`` adında ve karakter dizilerinin ``index()`` metoduyla aynı işi yapan
bir metodu bulunur. Bu metot bir liste öğesinin liste içindeki konumunu söyler
bize::
    
    >>> liste = ["elma", "armut", "çilek"]
    >>> liste.index("elma")
    
    0

Karakter dizilerinin ``index()`` metoduyla ilgili söylediğimiz her şey
listelerin ``index()`` metodu için de geçerlidir.

count()
===========

Karakter dizileri ile listelerin ortak metotlarından biri de ``count()``
metodudur. Tıpkı karakter dizilerinde olduğu gibi, listelerin ``count()`` metodu
da bir öğenin o veri tipi içinde kaç kez geçtiğini söyler::
    
    >>> liste = ["elma", "armut", "elma", "çilek"]
    >>> liste.count("elma")
    
    2

Karakter dizilerinin ``count()`` metoduyla ilgili söylediğimiz her şey
listelerin ``count()`` metodu için de geçerlidir.

copy()
========

Hatırlarsanız, geçen bölümde, listeleri, birbirlerini etkilemeyecek şekilde
kopyalamak için şu iki yöntemi kullanmıştık::
    
    >>> liste1 = ["ahmet", "mehmet", "özlem"]
    >>> liste2 = liste1[:]
    
ve::
    
    >>> liste2 = list(liste1)
    
İşte aynı iş için yukarıdakilere ek olarak ``copy()`` adlı bir metottan da
yararlanabiliriz. Dikkatlice bakın::
    
    >>> liste2 = liste1.copy()
    
Hangi yöntemi seçeceğiniz size kalmış...

clear()
=======

Listelerle ilgili olarak ele alacağımız son metodun adı ``clear()``. Bu metodun
görevi bir listenin içeriğini silmektir. 

Diyelim ki elimizde şöyle bir liste var::
    
    >>> liste = [1, 2, 3, 5, 10, 20, 30, 45]
    
Bu listenin içini boşaltmak için ``clear()`` metodunu kullanabiliriz::
    
    >>> liste.clear()
    >>> liste
    
    []
    
Bu metodun ``del`` sözcüğünden farklı olduğunu dikkat edin. ``clear()`` metodu
listenin içeriğini boşaltırken, ``del`` sözcüğü listeyi olduğu gibi ortadan
kaldırır.

Demetlerin Metotları
**********************

Listelerin metotlarını incelediğimize göre, artık demetlerin metotlarına
bakabiliriz. 

Geçen bölümde de söylediğimiz gibi, listeler ve demetler birbirine benzer.
Aralarındaki en önemli fark, listelerin değiştirilebilir bir veri tipi iken,
demetlerin değiştirilemez bir veri tipi olmasıdır. Elbette bu fark, iki veri
tipinin metotlarında da kendini gösterir. Demetler üzerinde değişiklik
yapamadığımız için, bu veri tipi değişiklik yapmaya yarayan metotlara sahip
değildir. 

Demetlerin hangi metotları olduğunu şu komutla görebilirsiniz::
    
    >>> dir(tuple)
    
Gördüğünüz gibi, bu veri tipinin bizi ilgilendiren iki metodu var:

#. ``index()``
#. ``count()``

index()
=========

Listeler ve karakter dizileri konusunu anlatırken bu veri tiplerinin ``index()``
adlı bir metodu olduğundan söz etmiştik hatırlarsanız. İşte demet veri tipinin
de ``index()`` adında ve listelerle karakter dizilerinin ``index()`` metoduyla
aynı işi yapan bir metodu bulunur. Bu metot bir demet öğesinin demet içindeki
konumunu söyler bize::
    
    >>> demet = ("elma", "armut", "çilek")
    >>> demet.index("elma")
    
    0

Listelerin ve karakter dizilerinin ``index()`` metoduyla ilgili söylediğimiz her
şey demetlerin ``index()`` metodu için de geçerlidir.

count()
===========

Karakter dizileri, listeler ve demetlerin ortak metotlarından biri de
``count()`` metodudur. Tıpkı karakter dizileri ve listelerde olduğu gibi,
demetlerin ``count()`` metodu da bir öğenin o veri tipi içinde kaç kez geçtiğini
söyler::
    
    >>> demet = ("elma", "armut", "elma", "çilek")
    >>> demet.count("elma")
    
    2

Karakter dizilerinin ve listelerin ``count()`` metoduyla ilgili söylediğimiz her
şeydemetlerin ``count()`` metodu için de geçerlidir.
