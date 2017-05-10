.. meta::
   :description: Bu bölümde kullanıcıdan nasıl veri alabileceğimizi öğreneceğiz.
   :keywords: python, input fonksiyonu, tip dönüştürme, int, float, str, complex, 
    eval, exec, format
   
.. highlight:: python3

******************************
Kullanıcıdan Bilgi Almak
******************************

Şimdiye kadar Python programlama dili ile ilgili epey bilgi edindik. Ama
muhtemelen buraya kadar öğrendiklerimiz sizi heyecanlandırmaktan bir hayli
uzaktı. Zira şu ana kadar hep tek yönlü bir programlama faaliyeti yürüttük.

Mesela şimdiye kadar öğrendiklerimizi kullanarak ancak şöyle bir program
yazabildik::

    isim = "Mübeccel"
    
    print("Merhaba", isim, end="!\n")

Bu programı çalıştırdığımızda şöyle bir çıktı alacağımızı biliyorsunuz::

    Merhaba Mübeccel!

Bu programın ne kadar sıkıcı olduğunu herhalde söylemeye gerek yok. Bu programda
`isim` değişkenini doğrudan kendimiz yazdığımız için programımız hiçbir koşulda
`Merhaba Mübeccel` dışında bir çıktı veremez. Çünkü bu program, tek yönlü bir
programlama faaliyetinin ürünüdür.

Halbuki bu değişkenin değerini kendimiz yazmasak, bu değeri kullanıcıdan alsak
ne hoş olurdu, değil mi?

Python'da kullanıcıdan herhangi bir veri alıp, yazdığımız programları tek
taraflı olmaktan kurtarmak için ``input()`` adlı bir fonksiyondan
faydalanıyoruz.

İşte biz bu bölümde, programcılık maceramızı bir üst seviyeye taşıyacak çok
önemli bir araç olan bu ``input()`` fonksiyonunu derinlemesine inceleyeceğiz.
Ama bu bölümde sadece bu fonksiyonu ele almayacağız elbette. Burada kullanıcıdan
veri almanın yanısıra, aldığımız bu veriyi nasıl dönüştüreceğimizi ve bu veriyi,
yazdığımız programlarda nasıl kullanacağımızı da derin derin inceleyeceğiz.

İlkin ``input()`` fonksiyonunu anlatarak yola koyulalım.

input() Fonksiyonu
*******************

``input()`` da daha önce öğrendiğimiz ``type()``, ``len()`` ve ``print()`` gibi
bir fonksiyondur. Esasında biz bu fonksiyonu ilk kez burada görmüyoruz. Windows
ve GNU/Linux kullanıcıları, yazdıkları bir programı çift tıklayarak
çalıştırabilmek için bu fonksiyonu kullandıklarını hatırlıyor olmalılar. Mesela
şu programı ele alalım::
    
    #!/usr/bin/env python3
    
    kartvizit = """
    İstihza Anonim Şirketi
    Fırat Özgül
    Tel: 0212 123 23 23
    Faks: 0212 123 23 24
    e.posta: kistihza@yahoo.com
    """

    print(kartvizit)

Bu programı yazıp kaydettikten sonra bu programın simgesi üzerine çift
tıkladığımızda siyah bir komut ekranının çok hızlı bir şekilde açılıp
kapandığını görürüz. Aslında programımız çalışıyor, ama programımız yapması
gereken işi yaptıktan hemen sonra kapandığı için biz program penceresini
görmüyoruz.

Programımızın çalıştıktan sonra hemen kapanmamasını sağlamak için son satıra bir
``input()`` fonksiyonu yerleştirmemiz gerektiğini biliyoruz::

    #!/usr/bin/env python3

    kartvizit = """
    İstihza Anonim Şirketi
    Fırat Özgül
    Tel: 0212 123 23 23
    Faks: 0212 123 23 24
    e.posta: kistihza@yahoo.com
    """

    print(kartvizit)

    input()

Bu sayede programımız kullanıcıdan bir giriş bekleyecek ve o girişi alana kadar
da kapanmayacaktır. Programı kapatmak için `Enter` düğmesine basabiliriz.

``input()`` bir fonksiyondur dedik. Henüz fonksiyon kavramının ayrıntılarını
öğrenmemiş olsak da, şimdiye kadar pek çok fonksiyon gördüğümüz için artık bir
fonksiyonla karşılaştığımızda bunun nasıl kullanılacağını az çok tahmin
edebiliyoruz. Tıpkı düşündüğünüz ve yukarıdaki örnekten de gördüğünüz gibi,
birer fonksiyon olan ``type()``, ``print()``, ``len()`` ve ``open()``
fonksiyonlarını nasıl kullanıyorsak ``input()`` fonksiyonunu da öyle
kullanacağız.

Dilerseniz lafı daha fazla uzatmadan örnek bir program yazalım::

    isim = input("İsminiz nedir? ")
    
    print("Merhaba", isim, end="!\n")

Bu programı kaydedip çalıştırdığınızda, sorulan soruya verdiğiniz cevaba göre
çıktı farklı olacaktır. Örneğin eğer bu soruya 'Niyazi' cevabını vermişseniz
çıktınız `Merhaba Niyazi!` şeklinde olacaktır.

Görüyorsunuz ya, tıpkı daha önce gördüğümüz fonksiyonlarda olduğu gibi,
``input()`` fonksiyonunda da parantez içine bir parametre yazıyoruz. Bu
fonksiyona verilen parametre, kullanıcıdan veri alınırken kullanıcıya sorulacak
soruyu gösteriyor. Gelin isterseniz bir örnek daha yapalım elimizin alışması
için::
    
    yaş = input("Yaşınız: ")
    
    print("Demek", yaş, "yaşındasın.")
    print("Genç mi yoksa yaşlı mı olduğuna karar veremedim.")

``input()`` fonksiyonunun ne kadar kullanışlı bir araç olduğu ortada. Bu
fonksiyon sayesinde, şimdiye kadar tek sesli bir şekilde yürüttüğümüz
programcılık faaliyetlerimizi çok sesli bir hale getirebileceğiz. Mesela önceki
bölümlerden birinde yazdığımız, daire alanı hesaplayan programı hatırlarsınız. O
zaman henüz dosyalarımızı kaydetmeyi ve ``input()`` fonksiyonunu öğrenmediğimiz
için o programı etkileşimli kabukta şu şekilde yazmıştık::
    
    >>> çap = 16
    >>> yarıçap = çap / 2
    >>> pi = 3.14159
    >>> alan = pi * (yarıçap * yarıçap)
    >>> alan
    
    201.06176

Ama artık hem dosyalarımızı kaydetmeyi biliyoruz, hem de ``input()``
fonksiyonunu öğrendik. Dolayısıyla yukarıdaki programı şu şekilde yazabiliriz::
    
    #Kullanıcıdan dairenin çapını girmesini istiyoruz.
    çap = input("Dairenin çapı: ")

    #Kullanıcının verdiği çap bilgisini kullanarak
    #yarıçapı hesaplayalım. Buradaki int() fonksiyonunu
    #ilk kez görüyoruz. Biraz sonra bunu açıklayacağız
    yarıçap = int(çap) / 2

    #pi sayımız sabit
    pi = 3.14159

    #Yukarıdaki bilgileri kullanarak artık 
    #dairenin alanını hesaplayabiliriz
    alan = pi * (yarıçap * yarıçap)

    #Son olarak, hesapladığımız alanı yazdırıyoruz
    print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")

Gördüğünüz gibi, ``input()`` fonksiyonunu öğrenmemiz sayesinde artık yavaş yavaş
işe yarar programlar yazabiliyoruz.

Ancak burada, daha önce öğrenmediğimiz bir fonksiyon dikkatinizi çekmiş olmalı.
Bu fonksiyonun adı ``int()``. Bu yeni fonksiyon dışında, yukarıdaki bütün
kodları anlayabilecek kadar Python bilgisine sahibiz.

``int()`` fonksiyonunun ne işe yaradığını anlamak için isterseniz ilgili satırı
``yarıçap = çap / 2`` şeklinde yazarak çalıştırmayı deneyin bu programı.

Dediğim gibi, eğer o satırdaki ``int()`` fonksiyonunu kaldırarak programı
çalıştırdıysanız şuna benzer bir hata mesajı almış olmalısınız::

    Traceback (most recent call last):
      File "deneme.py", line 8, in <module>
        yarıçap = çap / 2
    TypeError: unsupported operand type(s) for /: 'str' and 'int'

Gördüğünüz gibi programımız bölme işlemini yapamadı. Buradan anlıyoruz ki, bu
``int()`` fonksiyonu programımızdaki aritmetik işlemin düzgün bir şekilde
yapılabilmesini sağlıyor. Gelelim bu fonksiyonun bu işlevi nasıl yerine
getirdiğini incelemeye.

Tip Dönüşümleri
****************

Bir önceki bölümün sonunda verdiğimiz örnek programda ``int()`` adlı bir
fonksiyon görmüş, bu fonksiyonu anlatmayı o zaman ertelemiştik. Çok gecikmeden,
bu önemli fonksiyonun ne işe yaradığını öğrenmemiz gerekiyor. İsterseniz bir
örnek üzerinden gidelim.

Diyelim ki kullanıcıdan aldığı sayının karesini hesaplayan bir program yazmak
istiyoruz. Öncelikle şöyle bir şey deneyelim::

    sayı = input("Lütfen bir sayı girin: ")
    
    #Girilen sayının karesini bulmak için sayı değişkeninin 2.
    #kuvvetini alıyoruz. Aynı şeyi pow() fonksiyonu ile de 
    #yapabileceğimizi biliyorsunuz. Örn.: pow(sayı, 2)
    print("Girdiğiniz sayının karesi: ", sayı ** 2)

Bu kodları çalıştırdığımız zaman, programımız kullanıcıdan bir sayı girmesini
isteyecek, ancak kullanıcı bir sayı girip `Enter` tuşuna bastığında şöyle bir
hata mesajıyla karşılaşacaktır::
    
    Traceback (most recent call last):
      File "test.py", line 5, in <module>
        print("Girdiğiniz sayının karesi: ", sayı ** 2)
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Hata mesajına baktığınızda, 'TypeError' ifadesinden, bunun veri tipine ilişkin
bir hata olduğunu tahmin edebilirsiniz. Eğer İngilizce biliyorsanız yukarıdaki
hata mesajının anlamını rahatlıkla çıkarabilirsiniz. İngilizce bilmeseniz de en
sondaki 'str' ve 'int' kelimeleri size karakter dizisi ve sayı adlı veri
tiplerini hatırlatacaktır. Demek ki ortada veri tiplerini ilgilendiren bir sorun
var...

Peki burada tam olarak neler dönüyor?

Hatırlayacaksınız, geçen derslerden birinde ``len()`` fonksiyonunu anlatırken
şöyle bir şey söylemiştik:

    Biz henüz kullanıcıdan nasıl veri alacağımızı bilmiyoruz. Ama şimdilik şunu
    söyleyebiliriz: Python'da kullanıcıdan herhangi bir veri aldığımızda, bu
    veri bize bir karakter dizisi olarak gelecektir.
    
Gelin isterseniz yukarıda anlattığımız durumu teyit eden bir program yazalım::

    #Kullanıcıdan herhangi bir veri girmesini istiyoruz
    sayı = input("Herhangi bir veri girin: ")
    
    #Kullanıcının girdiği verinin tipini bir 
    #değişkene atıyoruz
    tip = type(sayı)

    #Son olarak kullanıcının girdiği verinin tipini
    #ekrana basıyoruz.
    print("Girdiğiniz verinin tipi: ", tip)

Bu programı çalıştırdığımızda ne tür bir veri girersek girelim, girdiğimiz
verinin tipi `str`, yani karakter dizisi olacaktır. Demek ki gerçekten de,
kullanıcıdan veri almak için kullandığımız ``input()`` fonksiyonu bize her
koşulda bir karakter dizisi veriyormuş.

Geçen derslerde şöyle bir şey daha söylemiştik:

    Python'da, o anda elinizde bulunan bir verinin hangi tipte olduğunu bilmek
    son derece önemlidir. Çünkü bir verinin ait olduğu tip, o veriyle neler
    yapıp neler yapamayacağınızı belirler.
    
Şu anda karşı karşıya olduğumuz durum da buna çok güzel bir örnektir. Eğer o
anda elimizde bulunan verinin tipini bilmezsek tıpkı yukarıda olduğu gibi, o
veriyi programımızda kullanmaya çalışırken programımız hata verir ve çöker.

Her zaman üstüne basa basa söylediğimiz gibi, aritmetik işlemler yalnızca
sayılarla yapılır. Karakter dizileri ile herhangi bir aritmetik işlem yapılamaz.
Dolayısıyla, ``input()`` fonksiyonundan gelen veri bir karakter dizisi olduğu
için ve biz de programımızda girilen sayının karesini hesaplamak amacıyla bu
fonksiyondan gelen verinin `2.` kuvvetini, yani karesini hesaplamaya
çalıştığımız için programımız hata verecektir.

Yukarıdaki programda neler olup bittiğini daha iyi anlayabilmek için Python'ın
etkileşimli kabuğunda şu işlemleri yapabiliriz::

    >>> "23" ** 2
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Gördüğünüz gibi, programımızdan aldığımız hata ile yukarıdaki hata tamamen aynı
(hata mesajlarında bizi ilgilendiren kısım en son satırdır). Tıpkı burada olduğu
gibi, hata veren programda da 'Lütfen bir sayı girin: ' sorusuna örneğin `23`
cevabını verdiğimizde programımız aslında ``"23" ** 2`` gibi bir işlem yapmaya
çalışıyor. Bir karakter dizisinin kuvvetini hesaplamak mümkün olmadığı, kuvvet
alma işlemi yalnızca sayılarla yapılabileceği için de hata vermekten başka
çaresi kalmıyor.

Ancak bazen öyle durumlarla karşılaşırsınız ki, programınız hiçbir hata vermez,
ama elde edilen sonuç aslında tamamen beklentinizin dışındadır. Mesela şu basit
örneği inceleyelim::
    
    sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
    sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")
    
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2) 

Bu kodları çalıştırdığımızda şöyle bir manzarayla karşılaşırız:

.. image:: ../images/sessions/output_int.png
    :align: center

``input()`` fonksiyonunun alttan alta neler çevirdiğini bu örnek yardımıyla çok
daha iyi anladığınızı zannediyorum. Gördüğünüz gibi yukarıdaki program herhangi
bir hata vermedi. Ama beklediğimiz çıktıyı da vermedi. Zira biz programımızın
iki sayıyı toplamasını istiyorduk. O ise kullanıcının girdiği sayıları yan yana
yazmakla yetindi. Yani bir aritmetik işlem yapmak yerine, verileri birbiriyle
bitiştirdi. Çünkü, dediğim gibi, ``input()`` fonksiyonunun kullanıcıdan aldığı
şey bir karakter dizisidir. Dolayısıyla bu fonksiyon yukarıdaki gibi bir durumla
karşılaştığı zaman karakter dizileri arasında bir birleştirme işlemi
gerçekleştirir. Tıpkı ilk derslerimizde etkileşimli kabukta verdiğimiz şu
örnekte olduğu gibi::
    
    >>> "23" + "23"
    
    2323

Bu son örnekten ayrıca şunu çıkarıyoruz: Yazdığınız bir programın herhangi bir
hata vermemesi o programın doğru çalıştığı anlamına gelmeyebilir. Dolayısıyla bu
tür durumlara karşı her zaman uyanık olmanızda fayda var.

Peki yukarıdaki gibi durumlarla karşılaşmamak için ne yapacağız?

İşte bu noktada devreye tip dönüştürücü adını verdiğimiz birtakım fonksiyonlar
girecek.

int() 
=========

Dediğimiz gibi, ``input()`` fonksiyonundan gelen veri her zaman bir karakter
dizisidir. Dolayısıyla bu fonksiyondan gelen veriyle herhangi bir aritmetik
işlem yapabilmek için öncelikle bu veriyi bir sayıya dönüştürmemiz gerekir. Bu
dönüştürme işlemi için ``int()`` adlı özel bir dönüştürücü fonksiyondan
yararlanacağız. Gelin isterseniz Python'ın etkileşimli kabuğunda bu fonksiyonla
bir kaç deneme yaparak bu fonksiyonun ne işe yaradığını ve nasıl kullanıldığını
anlamaya çalışalım. Zira etkileşimli kabuk bu tür deneme işlemleri için biçilmiş
kaftandır::
    
    >>> karakter_dizisi = "23"
    >>> sayı = int(karakter_dizisi)
    >>> print(sayı)

    23 

Burada öncelikle `"23"` adlı bir karakter dizisi tanımladık. Ardından da
``int()`` fonksiyonunu kullanarak bu karakter dizisini bir tamsayıya (*integer*)
dönüştürdük. İsminden de anlayacağınız gibi ``int()`` fonksiyonu İngilizce
*integer* (tamsayı) kelimesinin kısaltmasıdır ve bu fonksiyonun görevi bir
veriyi tamsayıya dönüştürmektir.

Ancak burada dikkat etmemiz gereken bir şey var. Herhangi bir verinin sayıya
dönüştürülebilmesi için o verinin sayı değerli bir veri olması gerekir. Örneğin
`"23"`, sayı değerli bir karakter dizisidir. Ama mesela `"elma"` sayı değerli
bir karakter dizisi değildir. Bu yüzden `"elma"` karakter dizisi sayıya
dönüştürülemez::
    
    >>> karakter_dizisi = "elma"
    >>> sayı = int(karakter_dizisi)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'elma'

Gördüğünüz gibi, sayı değerli olmayan bir veriyi sayıya dönüştürmeye
çalıştırdığımızda Python bize bir hata mesajı gösteriyor. Yazdığımız
programlarda bu duruma özellikle dikkat etmemiz gerekiyor.

Şimdi bu bölümün başında yazdığımız ve hata veren programımıza dönelim yine::

    sayı = input("Lütfen bir sayı girin: ")

    print("Girdiğiniz sayının karesi: ", sayı ** 2)

Bu kodların hata vereceğini biliyoruz. Ama artık, öğrendiğimiz ``int()``
dönüştürücüsünü kullanarak programımızı hata vermeyecek şekilde yeniden
yazabiliriz::
    
    veri = input("Lütfen bir sayı girin: ")

    #input() fonksiyonundan gelen karakter dizisini
    #sayıya dönüştürüyoruz.
    sayı = int(veri)

    print("Girdiğiniz sayının karesi: ", sayı ** 2)
    
Artık programımız hatasız bir şekilde çalışıyor. 

Bir de öteki örneğimizi ele alalım::

    sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
    sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")
    
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2) 

Bu kodların beklediğimiz çıktıyı vermeyeceğini biliyoruz. Ama eğer bu kodları
şöyle yazarsak işler değişir::
    
    v1 = input("Toplama işlemi için ilk sayıyı girin: ")
    v2 = input("Toplama işlemi için ikinci sayıyı girin: ")
    
    sayı1 = int(v1) #v1 adlı karakter dizisini sayıya dönüştürüyoruz.
    sayı2 = int(v2) #v2 adlı karakter dizisini sayıya dönüştürüyoruz.
    
    print(sayı1, "+", sayı2, "=", sayı1 + sayı2) 

Gördüğünüz gibi, ``input()`` fonksiyonundan gelen karakter dizilerini sayıya
dönüştürerek istediğimiz çıktıyı alabiliyoruz.

str()
===========

Python'daki tip dönüştürücüleri elbette sadece ``int()`` fonksiyonuyla sınırlı
değildir. Gördüğünüz gibi, ``int()`` fonksiyonu sayı değerli verileri (mesela
karakter dizilerini) tam sayıya dönüştürüyor. Bunun bir de tersi mümkündür. Yani
karakter dizisi olmayan verileri karakter dizisine dönüştürmemiz de mümkündür.
Bu işlem için ``str()`` adlı başka bir tip dönüştürücüden yararlanıyoruz::
    
    >>> sayı = 23
    >>> kardiz = str(sayı)
    >>> print(kardiz)
    
    23
    
    >>> print(type(kardiz))
    
    <class 'str'>

Gördüğünüz gibi, bir tam sayı olan `23`'ü ``str()`` adlı bir fonksiyondan
yararlanarak karakter dizisi olan `"23"` ifadesine dönüştürdük. Son satırda da,
elde ettiğimiz şeyin bir karakter dizisi olduğundan emin olmak için ``type()``
fonksiyonunu kullanarak verinin tipini denetledik.

Yukarıdaki örneklerden gördüğümüz gibi, aritmetik işlemler yapmak istediğimizde
karakter dizilerini sayıya çevirmemiz gerekiyor. Peki acaba hangi durumlarda
bunun tersini yapmamız, yani sayıları karakter dizilerine çevirmemiz gerekir?
Python bilginiz ve tecrübeniz arttıkça bunların hangi durumlar olduğunu kendiniz
de göreceksiniz. Mesela biz daha şimdiden, sayıları karakter dizisine çevirmemiz
gereken bir durumla karşılaştık. Hatırlarsanız, ``len()`` fonksiyonunu
anlatırken, bu fonksiyonun sayılarla birlikte kullanılamayacağını söylemiştik::
    
    >>> len(12343423432)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()

Peki ya yazdığınız programda bir sayının kaç haneden oluştuğunu hesaplamanız
gerekirse ne yapacaksınız? Yani mesela yukarıdaki sayının 11 haneli olduğunu
bilmeniz gerekiyorsa ne olacak?

İşte böyle bir durumda ``str()`` fonksiyonundan yararlanabilirsiniz::

    >>> sayı = 12343423432
    >>> kardiz = str(sayı)
    >>> len(kardiz)

    11

Bildiğiniz gibi, ``len()`` fonksiyonu, şu ana kadar öğrendiğimiz veri tipleri
içinde sadece karakter dizileri üzerinde işlem yapabiliyor. Biz de bu yüzden,
sayımızın kaç haneli olduğunu öğrenebilmek için, öncelikle bu sayıyı bir
karakter dizisine çeviriyoruz. Daha sonra da elde ettiğimiz bu karakter dizisini
``len()`` fonksiyonuna parametre olarak veriyoruz. Böylece sayının kaç haneli
olduğu bilgisini elde etmiş oluyoruz.

Bu arada elbette yukarıdaki işlemi tek satırda da halledebilirsiniz::

    >>> len(str(12343423432))
    
    11

Bu şekilde iç içe geçmiş fonksiyonlar yazdığımızda, Python fonksiyonları içten
dışa doğru tek tek değerlendirecektir. Mesela yukarıdaki örnekte Python önce
``str(12343423432)`` ifadesini değerlendirecek ve çıkan sonucu ``len()``
fonksiyonuna gönderecektir. İç içe geçmiş fonksiyonları yazarken dikkat etmemiz
gereken önemli bir nokta da, açtığımız her bir parantezi tek tek kapatmayı
unutmamaktır.

float()
============

Hatırlarsanız ilk bölümlerde sayılardan söz ederken tamsayıların (*integer*)
dışında kayan noktalı sayıların (*float*) da olduğundan söz etmiştik. İşte eğer
bir tamsayıyı veya sayı değerli bir karakter dizisini kayan noktalı sayıya
dönüştürmek istersek ``float()`` adlı başka bir dönüştürücüden yararlanacağız::
    
    >>> a = 23
    >>> type(a)
    
    <class 'int'>
    
    >>> float(a)
    
    23.0


Gördüğünüz gibi, `23` tamsayısı, ``float()`` fonksiyonu sayesinde `23.0`'a yani
bir kayan noktalı sayıya dönüştü.

Aynı şeyi, sayı değerli karakter dizileri üzerine uygulamak da mümkündür::

    >>> b = "23"
    >>> type(b)
    
    <class 'str'>
    
    >>> float(b)
    
    23.0
    
complex()
=============

Sayılardan söz ederken, eğer matematikle çok fazla içli dışlı değilseniz pek
karşılaşmayacağınız, 'karmaşık sayı' adlı bir sayı türünden de bahsetmiştik.
Karmaşık sayılar Python'da 'complex' ifadesiyle gösteriliyor. Mesela şunun bir
karmaşık sayı olduğunu biliyoruz::
    
    >>> 12+0j

Kontrol edelim::

    >>> type(12+0j)
    
    <class 'complex'>

İşte eğer herhangi bir sayıyı karmaşık sayıya dönüştürmeniz gerekirse
``complex()`` adlı bir fonksiyondan yararlanabilirsiniz. Örneğin::
    
    >>> complex(15)
    
    (15+0j)

Böylece Python'daki bütün sayı dönüştürücüleri öğrenmiş olduk.

Gelin isterseniz, bu bölümde anlattığımız konuları şöyle bir tekrar ederek
bilgilerimizi sağlamlaştırmaya çalışalım.

::

    >>> a = 56
    
Bu sayı bir tamsayıdır. İngilizce olarak ifade etmek gerekirse, *integer*. Bunun
bir tamsayı olduğunu şu şekilde teyit edebileceğimizi gayet iyi biliyorsunuz::
    
    >>> type(a)

    <class 'int'>
    
Burada aldığımız `<class int>` çıktısı, bize `a` değişkeninin tuttuğu sayının
bir tamsayı olduğunu söylüyor. 'int' ifadesi, *integer* (tamsayı) kelimesinin
kısaltmasıdır.

Bir de şu sayıya bakalım::

    >>> b = 34.5
    >>> type(b)

    <class 'float'>
    
Bu çıktı ise bize `34.5` sayısının bir kayan noktalı sayı olduğunu söylüyor.
*float* kelimesi *Floats* veya *Floating Point Number* ifadesinin kısaltmasıdır.
Yani 'kayan noktalı sayı' demektir.

Bu arada, bu ``type()`` adlı fonksiyonu sadece sayılara değil, başka şeylere de
uygulayabileceğimizi biliyorsunuz. Mesela bir örnek vermek gerekirse::

    >>> meyve = "karpuz"
    >>> type(meyve)

    <class 'str'>
    
Gördüğünüz gibi, ``type()`` fonksiyonu bize `meyve` adlı değişkenin değerinin
bir 'str' yani *string* yani karakter dizisi olduğunu bildirdi.

Bu veri tipleri arasında, bazı özel fonksiyonları kullanarak dönüştürme işlemi
yapabileceğimizi öğrendik. Mesela::

    >>> sayı = 45

`sayı` adlı değişkenin tuttuğu verinin değeri bir tamsayıdır. Biz bu tamsayıyı
kayan noktalı sayıya dönüştürmek istiyoruz. Yapacağımız işlem çok basit::
    
    >>> float(sayı)

    45.0
    
Gördüğünüz gibi, `45` adlı tamsayıyı, `45.0` adlı bir kayan noktalı sayıya
dönüştürdük. Şimdi ``type(45.0)`` komutu bize `<class ‘float'>` çıktısını
verecektir.

Eğer kayan noktalı bir sayıyı tamsayıya çevirmek istersek şu komutu veriyoruz.
Mesela kayan noktalı sayımız, `56.5` olsun::

    >>> int(56.5)

    56
    
Yukarıdaki örneği tabii ki şöyle de yazabiliriz::

    >>> a = 56.5
    >>> int(a)

    56
    
Dönüştürme işlemini sayılar arasında yapabileceğimiz gibi, sayılar ve karakter
dizileri arasında da yapabiliriz. Örneğin şu bir karakter dizisidir::
    
    >>> nesne = "45"

Yukarıdaki değeri tırnak içinde belirttiğimiz için bu değer bir karakter
dizisidir. Şimdi bunu bir tamsayıya çevireceğiz::
    
    >>> int(nesne)

    45
    
Dilersek, aynı karakter dizisini kayan noktalı sayıya da çevirebiliriz::

    >>> float(nesne)

    45.0
    
Hatta bir sayıyı karakter dizisine de çevirebiliriz. Bunun için *string*
(karakter dizisi) kelimesinin kısaltması olan `str` ifadesini kullanacağız::
    
    >>> s = 6547
    >>> str(s)

    '6547'
    
Bir örnek de kayan noktalı sayılarla yapalım::

    >>> s = 65.7
    >>> str(s)

    '65.7'
    
Yalnız şunu unutmayın: Bir karakter dizisinin sayıya dönüştürülebilmesi için o
karakter dizisinin sayı değerli olması lazım. Yani `"45"` değerini sayıya
dönüştürebiliriz. Çünkü `"45"` değeri, tırnaklardan ötürü bir karakter dizisi de
olsa, neticede sayı değerli bir karakter dizisidir. Ama mesela `"elma"` karakter
dizisi böyle değildir. Dolayısıyla, şöyle bir maceraya girişmek bizi hüsrana
uğratacaktır::
    
    >>> nesne = "elma"
    >>> int(nesne)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'elma'
    
Gördüğünüz gibi, Python böyle bir işlem denemesi karşısında hata veriyor...

Bu bölümde pek çok yeni şey öğrendik. Bu bölümün en önemli getirisi ``input()``
fonksiyonunu öğrenmemiz oldu. Bu fonksiyon sayesinde kullanıcıyla iletişim
kurmayı başardık. Artık kullanıcıdan veri alıp, bu verileri programlarımız
içinde işleyebiliyoruz.

Yine bu bölümde dikkatinizi çektiğimiz başka bir konu da sayılar ve karakter
dizileri arasındaki ilişkiydi. ``input()`` fonksiyonuyla elde edilen çıktının
bir karakter dizisi olduğunu öğrendik. Bildiğimiz gibi, aritmetik işlemler ancak
sayılar arasında yapılabilir. Dolayısıyla ``input()`` fonksiyonuyla gelen
karakter dizisini bir sayıyla çarpmaya kalkarsak hata alıyoruz. Burada yapmamız
gereken şey, elimizdeki verileri dönüştürmek. Yani ``input()`` fonksiyonundan
gelen karakter dizisini bir sayıyla çarpmak istiyorsak, öncelikle aldığımız
karakter dizisini sayıya dönüştürmemiz gerekiyor. Dönüştürme işlemleri için
kullandığımız fonksiyonlar şunlardı:

    ``int()``
        Sayı değerli bir karakter dizisini veya kayan noktalı sayıyı tamsayıya 
        (*integer*) çevirir.
        
    ``float()``
        Sayı değerli bir karakter dizisini veya tamsayıyı kayan noktalı sayıya 
        (*float*) çevirir.
        
    ``str()``
        Bir tamsayı veya kayan noktalı sayıyı karakter dizisine (*string*) çevirir.
    
    ``complex()``
        Herhangi bir sayıyı veya sayı değerli karakter dizisini karmaşık sayıya 
        (*complex*) çevirir.
        
Ayrıca bu bölümde öğrendiklerimiz, şöyle önemli bir tespitte bulunmamıza da
olanak tanıdı:

    Her tamsayı ve/veya kayan noktalı sayı bir karakter dizisine
    dönüştürülebilir. Ama her karakter dizisi tamsayıya ve/veya kayan noktalı
    sayıya dönüştürülemez.
    
Örneğin, `5654` gibi bir tamsayıyı veya `543.34` gibi bir kayan noktalı sayıyı
``str()`` fonksiyonu yardımıyla karakter dizisine dönüştürebiliriz::
    
    >>> str(5654)
    >>> str(543.34)
    
`"5654"` veya `"543.34"` gibi bir karakter dizisini ``int()`` veya ``float()``
fonksiyonu yardımıyla tamsayıya ya da kayan noktalı sayıya da dönüştürebiliriz::
    
    >>> int("5654")
    >>> int("543.34")

    >>> float("5654")
    >>> float("543.34")
    
Ama `"elma"` gibi bir karakter dizisini ne ``int()`` ne de ``float()``
fonksiyonuyla tamsayıya veya kayan noktalı sayıya dönüştürebiliriz! Çünkü
`"elma"` verisi sayı değerli değildir.

Bu bölümü kapatmadan önce, dilerseniz şimdiye kadar öğrendiklerimizi de içeren
örnek bir program yazalım. Bu program, Python maceramız açısından bize yeni
kapılar da açacak.

Önceki derslerimizin birinde verdiğimiz doğalgaz faturası hesaplayan programı
hatırlarsınız. İşte artık ``input()`` fonksiyonu sayesinde bu doğalgaz faturası
hesaplama programını da daha ilginç bir hale getirebiliriz::
    
    #Her bir ayın kaç gün çektiğini tanımlıyoruz
    ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
    nisan = haziran = eylül = kasım = 30
    şubat = 28

    #Doğalgazın vergiler dahil metreküp fiyatı
    birimFiyat = 0.79

    #Kullanıcı ayda ne kadar doğalgaz tüketmiş?
    aylıkSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: ")

    #Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
    dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
    (Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

    #Yukarıdaki input() fonksiyonundan gelen veriyi
    #Python'ın anlayabileceği bir biçime dönüştürüyoruz
    ay = eval(dönem)

    #Kullanıcının günlük doğalgaz sarfiyatı
    günlükSarfiyat = int(aylıkSarfiyat) / ay

    #Fatura tutarı
    fatura = birimFiyat * günlükSarfiyat * ay

    print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
    "tahmini fatura tutarı: \t", fatura, " TL", sep="")

Burada yine bilmediğimiz bir fonksiyonla daha karşılaştık. Bu fonksiyonun adı
``eval()``. Biraz sonra ``eval()`` fonksiyonunu derinlemesine inceleyeceğiz. Ama
bu fonksiyonu anlatmaya geçmeden önce dilerseniz yukarıdaki kodları biraz
didikleyelim.

İlk satırların ne işe yaradığını zaten biliyorsunuz. Bir yıl içindeki bütün
ayların kaç gün çektiğini gösteren değişkenlerimizi tanımladık. Burada her bir
değişkeni tek tek tanımlamak yerine değişkenleri topluca tanımladığımıza dikkat
edin. İsteseydik tabii ki yukarıdaki kodları şöyle de yazabilirdik::
    
    #Her bir ayın kaç gün çektiğini tanımlıyoruz
    ocak    = 31
    şubat   = 28
    mart    = 31
    nisan   = 30
    mayıs   = 31
    haziran = 30
    temmuz  = 31
    ağustos = 31
    eylül   = 30
    ekim    = 31
    kasım   = 30
    aralık  = 31

    #Doğalgazın vergiler dahil m3 fiyatı
    birimFiyat = 0.79

    #Kullanıcı ayda ne kadar doğalgaz tüketmiş?
    aylıkSarfiyat = input("Aylık doğalgaz sarfiyatınızı m3 olarak giriniz: ")

    #Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
    dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
    (Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

    #Yukarıdaki input() fonksiyonundan gelen veriyi
    #Python'ın anlayabileceği bir biçime dönüştürüyoruz
    ay = eval(dönem)

    #Kullanıcının günlük doğalgaz sarfiyatı
    günlükSarfiyat = int(aylıkSarfiyat) / ay

    #Fatura tutarı
    fatura = birimFiyat * günlükSarfiyat * ay

    print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
    "tahmini fatura tutarı: \t", fatura, " TL", sep="")
    
Ama tabii ki, değişkenleri tek tek tanımlamak yerine topluca tanımlamak, daha az
kod yazmanızı sağlamasının yanısıra, programınızın çalışma performansı açısından
da daha iyidir. Yani değişkenleri bu şekilde tanımladığınızda programınız daha
hızlı çalışır.

Programımızı incelemeye devam edelim...

Değişkenleri tanımladıktan sonra doğalgazın vergiler dahil yaklaşık birim
fiyatını da bir değişken olarak tanımladık. `0.79` değerini zaten birkaç bölüm
önce hesaplayıp bulduğumuz için, aynı işlemleri tekrar programımıza eklememize
gerek yok. Doğrudan nihai değeri programımıza yazsak yeter...

Birim fiyatı belirledikten sonra kullanıcıya aylık doğalgaz sarfiyatını
soruyoruz. Kullanıcının bu değeri m\ :sup:`3` olarak girmesini bekliyoruz.
Elbette bu veriyi kullanıcıdan alabilmek için ``input()`` fonksiyonunu
kullanıyoruz.

Daha sonra kullanıcıya hangi aya ait doğalgaz faturasını ödemek istediğini
soruyoruz. Bu bilgi, bir sonraki satırda günlük doğalgaz sarfiyatını hesaplarken
işimize yarayacak. Çünkü kullanıcının girdiği ayın çektiği gün sayısına bağlı
olarak günlük sarfiyat değişecektir. Günlük sarfiyatı hesaplamak için aylık
sarfiyatı, ilgili ayın çektiği gün sayısına bölüyoruz. Bu arada bir önceki
satırda `dönem` değişkenini ``eval()`` adlı bir fonksiyonla birlikte
kullandığımızı görüyorsunuz. Bunu biraz sonra inceleyeceğiz. O yüzden bu
satırları atlayıp son satıra gelelim.

Son satırda ``print()`` fonksiyonunu kullanarak, kullanıcıdan aldığımız verileri
düzgün bir şekilde kendisine gösteriyoruz. Programımız kullanıcıya günlük
doğalgaz sarfiyatını ve ay sonunda karşılaşacağı tahmini fatura tutarını
bildiriyor. ``print()`` fonksiyonu içinde kullandığımız kaçış dizilerine
özellikle dikkatinizi çekmek istiyorum. Burada düzgün bir çıktı elde etmek için
`\\t` ve `\\n` adlı kaçış dizilerinden nasıl yararlandığımızı görüyorsunuz. Bu
kaçış dizilerinin buradaki işlevini tam olarak anlayabilmek için, bu kodları bir
de bu kaçış dizileri olmadan yazmayı deneyebilirsiniz.

Bu bilgileri, önemlerinden ötürü aklımızda tutmaya çalışalım. Buraya kadar
anlatılan konular hakkında zihnimizde belirsizlikler varsa veya bazı noktaları
tam olarak kavrayamadıysak, şimdiye kadar öğrendiğimiz konuları tekrar gözden
geçirmemiz bizim için epey faydalı olacaktır. Zira bundan sonraki bölümlerde,
yeni bilgilerin yanısıra, buraya kadar öğrendiğimiz şeyleri de yoğun bir şekilde
pratiğe dökeceğiz. Bundan sonraki konuları takip edebilmemiz açısından, buraya
kadar verdiğimiz temel bilgileri iyice sindirmiş olmak işimizi bir hayli
kolaylaştıracaktır.

eval() ve exec() Fonksiyonları
******************************

Bir önceki bölümün son örnek programında ``eval()`` adlı bir fonksiyonla
karşılaşmıştık. İşte şimdi bu önemli fonksiyonun ne işe yaradığını anlamaya
çalışacağız. Ancak ``eval()`` fonksiyonunu anlatmaya başlamadan önce şu uyarıyı
yapalım:

.. raw:: html 

    <div class="raw">eval() ŞEYTANİ GÜÇLERİ OLAN BİR FONKSİYONDUR!</div>
    
.. raw:: latex

    \begin{center}{\color{red}\textbf{eval() ŞEYTANİ GÜÇLERİ OLAN BİR FONKSİYONDUR!}}\end{center}

Bunun neden böyle olduğunu hem biz anlatacağız, hem de zaten bu fonksiyonu
tanıdıkça neden ``eval()``'e karşı dikkatli olmanız gerektiğini kendiniz de
anlayacaksınız.

Dilerseniz işe basit bir ``eval()`` örneği vererek başlayalım::

    print("""
    Basit bir hesap makinesi uygulaması.

    İşleçler: 

        +   toplama
        -   çıkarma
        *   çarpma
        /   bölme

    Yapmak istediğiniz işlemi yazıp ENTER
    tuşuna basın. (Örneğin 23 ve 46 sayılarını
    çarpmak için 23 * 46 yazdıktan sonra
    ENTER tuşuna basın.)
    """)

    veri = input("İşleminiz: ")
    hesap = eval(veri)

    print(hesap)

İngilizcede *evaluate* diye bir kelime bulunur. Bu kelime, 'değerlendirmeye tabi
tutmak, işleme sokmak, işlemek' gibi anlamlar taşır. İşte ``eval()``
fonksiyonundaki *eval* kelimesi bu *evaluate* kelimesinin kısaltmasıdır. Yani bu
fonksiyonun görevi, kendisine verilen karakter dizilerini değerlendirmeye tabi
tutmak ya da işlemektir. Peki bu tam olarak ne anlama geliyor?

Aslında yukarıdaki örnek programı çalıştırdığımızda bu sorunun yanıtını kendi
kendimize verebiliyoruz. Bu programı çalıştırarak, `"İşleminiz: "` ifadesinden
sonra, örneğin, ``45 * 76`` yazıp `Enter` tuşuna basarsak programımız bize
`3420` çıktısı verecektir. Yani programımız hesap makinesi işlevini yerine
getirip `45` sayısı ile `76` sayısını çarpacaktır. Dolayısıyla, yukarıdaki
programı kullanarak her türlü aritmetik işlemi yapabilirsiniz. Hatta bu program,
son derece karmaşık aritmetik işlemlerin yapılmasına dahi müsaade eder.

Peki programımız bu işlevi nasıl yerine getiriyor? İsterseniz kodların üzerinden
tek tek geçelim.

Öncelikle programımızın en başına kullanım kılavuzuna benzer bir metin
yerleştirdik ve bu metni ``print()`` fonksiyonu yardımıyla ekrana bastık.

Daha sonra kullanıcıdan alacağımız komutları `veri` adlı bir değişkene atadık.
Tabii ki kullanıcıyla iletişimi her zaman olduğu gibi ``input()`` fonksiyonu
yardımıyla sağlıyoruz.

Ardından, kullanıcıdan gelen veriyi ``eval()`` fonksiyonu yardımıyla
değerlendirmeye tabi tutuyoruz. Yani kullanıcının girdiği komutları işleme
sokuyoruz. Örneğin, kullanıcı ``46 / 2`` gibi bir veri girdiyse, biz ``eval()``
fonksiyonu yardımıyla bu ``46 / 2`` komutunu işletiyoruz. Bu işlemin sonucunu da
`hesap` adlı başka bir değişken içinde depoluyoruz.

Eğer burada ``eval()`` fonksiyonunu kullanmazsak, programımız, kullanıcının
girdiği ``45 * 76`` komutunu hiçbir işleme sokmadan dümdüz ekrana basacaktır.
Yani::
    
    print("""
    Basit bir hesap makinesi uygulaması.

    İşleçler:

        +   toplama
        -   çıkarma
        *   çarpma
        /   bölme

    Yapmak istediğiniz işlemi yazıp ENTER
    tuşuna basın. (Örneğin 23 ve 46 sayılarını
    çarpmak için 23 * 46 yazdıktan sonra
    ENTER tuşuna basın.)
    """)

    veri = input("İşleminiz: ")

    print(veri)

Eğer programımızı yukarıdaki gibi, ``eval()`` fonksiyonu olmadan yazarsak,
kullanıcımız ``45 * 76`` gibi bir komut girdiğinde alacağı cevap dümdüz bir `45
* 76` çıktısı olacaktır. İşte ``eval()`` fonksiyonu, kullanıcının girdiği her
veriyi bir Python komutu olarak algılar ve bu veriyi işleme sokar. Yani ``45 *
76`` gibi bir şey gördüğünde, bu şeyi doğrudan ekrana yazdırmak yerine, işlemin
sonucu olan `3420` sayısını verir.

``eval()`` fonksiyonunun, yukarıda anlattığımız özelliklerini okuduktan sonra,
'Ne güzel bir fonksiyon! Her işimi görür bu!' dediğinizi duyar gibiyim. Ama
aslında durum hiç de öyle değil. Neden mi?

Şimdi yukarıdaki programı tekrar çalıştırın ve `"İşleminiz: "` ifadesinden sonra
şu cevabı verin::

    print("Merhaba Python!")

Bu komut şöyle bir çıktı vermiş olmalı::

    Merhaba Python!
    None

.. note:: Buradaki `None` değerini görmezden gelin. Bunu fonksiyonlar konusunu
          anlatırken inceleyeceğiz.

Gördüğünüz gibi, yazdığımız program, kullanıcının girdiği Python komutunun
işletilmesine sebep oldu. Bu noktada, 'Eee, ne olmuş!' demiş olabilirsiniz.
Gelin bir de şuna bakalım. Şimdi programı tekrar çalıştırıp şu cevabı verin::
    
    open("deneme.txt", "w")

Bu cevap, bilgisayarınızda `deneme.txt` adlı bir dosya oluşturulmasına sebep
oldu. Belki farkındasınız, belki farkında değilsiniz, ama aslında şu anda kendi
yazdığınız program sizin kontrolünüzden tamamen çıktı. Siz aslında bir hesap
makinesi programı yazmıştınız. Ama ``eval()`` fonksiyonu nedeniyle kullanıcıya
rastgele Python komutlarını çalıştırma imkanı verdiğiniz için programınız sadece
aritmetik işlemleri hesaplamak için kullanılmayabilir. Böyle bir durumda kötü
niyetli (ve bilgili) bir kullanıcı size çok büyük zarar verebilir. Mesela
kullanıcının, yukarıdaki programa şöyle bir cevap verdiğini düşünün::
    
    __import__("os").system("dir")

Burada anlamadığınız şeyleri şimdilik bir kenara bırakıp, bu komutun sonuçlarına
odaklanın. Gördüğünüz gibi, yukarıdaki programa bu cevabı vererek mevcut dizin
altındaki bütün dosyaları listeleyebildik. Yani programımız bir anda amacını
aştı. Artık bu aşamadan sonra bu programı şeytani bir amaca yönelik olarak
kullanmak tamamen programı kullanan kişiye kalmış... Bu programın, bir web
sunucusu üzerinde çalışan bir uygulama olduğunu ve bu programı kullananların
yukarıdaki gibi masumane bir şekilde dizin içindeki dosyaları listeleyen bir
komut yerine, dizin içindeki dosyaları ve hatta sabit disk üzerindeki her şeyi
silen bir komut yazdığını düşünün... Yanlış yazılmış bir program yüzünden bütün
verilerinizi kaybetmeniz işten bile değildir. (Bahsettiğim o, 'bütün sabit diski
silen komutu' kendi sisteminizde vermemeniz gerektiğini söylememe gerek yok,
değil mi?)

Eğer *SQL Injection* kavramını biliyorsanız, yukarıdaki kodların yol açtığı
güvenlik açığını gayet iyi anlamış olmalısınız. Zaten internet üzerinde yaygın
bir şekilde kullanılan ve web sitelerini hedef alan *SQL Injection* tarzı
saldırılar da aynı mantık üzerinden gerçekleştiriliyor. *SQL Injection*
metoduyla bir web sitesine saldıran *cracker*'lar, o web sitesini programlayan
kişinin (çoğunlukla farkında olmadan) kullanıcıya verdiği rastgele SQL komutu
işletme yetkisini kötüye kullanarak gizli ve özel bilgileri ele
geçirebiliyorlar. Örneğin *SQL Injection* metodu kullanılarak, bir web sitesine
ait veritabanının içeriği tamamen silinebilir. Aynı şekilde, yukarıdaki
``eval()`` fonksiyonu da kullanıcılarınıza rastgele Python komutlarını
çalıştırma yetkisi verdiği için kötü niyetli bir kullanıcının programınıza
sızmasına yol açabilecek potansiyele sahiptir.

Peki ``eval()`` fonksiyonunu asla kullanmayacak mıyız? Elbette kullanacağız. Bu
fonksiyonun kullanımını gerektiren durumlarla da karşılaşabilirsiniz. Ama şunu
asla aklınızdan çıkarmayın: ``eval()`` fonksiyonu her ne kadar son derece
yetenekli ve güçlü bir araç da olsa yanlış ellerde yıkıcı sonuçlar doğurabilir.
Program yazarken, eğer ``eval()`` kullanmanızı gerektiren bir durumla karşı
karşıya olduğunuzu düşünüyorsanız, bir kez daha düşünün. ``eval()`` ile elde
edeceğiniz etkiyi muhtemelen başka ve çok daha iyi yöntemlerle de elde
edebilirsiniz. Üstelik performans açısından ``eval()`` pek iyi bir tercih
değildir, çünkü bu fonksiyon (çoğu durumda farketmeseniz de) aslında yavaş
çalışır. O yüzden, ``eval()`` fonksiyonunu kullanacağınız zaman, bunun artı ve
eksilerini çok iyi tartın: Bu fonksiyonu kullanmak size ne kazandırıyor, ne
kaybettiriyor?

Ayrıca ``eval()`` fonksiyonu kullanılacağı zaman, kullanıcıdan gelen veri bu
fonksiyona parametre olarak verilmeden önce sıkı bir kontrolden geçirilir. Yani
kullanıcının girdiği veri ``eval()`` aracılığıyla doğrudan değerlendirmeye tabi
tutulmaz. Araya bir kontrol mekanizması yerleştirilir. Örneğin, yukarıdaki hesap
makinesi programında kullanıcının gireceği verileri sadece sayılar ve işleçlerle
sınırlandırabilirsiniz. Yani kullanıcınızın, izin verilen değerler harici bir
değer girmesini engelleyebilirsiniz. Bu durumu somutlaştırmak için şöyle bir
diyagram çizebiliriz:

.. image:: ../images/misc/eval_yanlis.png
    :align: center
    :width: 50%

Yukarıdaki diyagram ``eval()`` fonksiyonunun yanlış uygulanış biçimini
gösteriyor. Gördüğünüz gibi, veri doğrudan ``eval()`` fonksiyonuna gidiyor ve
çıktı olarak veriliyor. Böyle bir durumda, ``eval()`` fonksiyonu kullanıcıdan
gelen verinin ne olduğuna bakmadan, veriyi doğrudan komut olarak değerlendirip
işleteceği için programınızı kullanıcının insafına terketmiş oluyorsunuz.

Aşağıdaki diyagram ise ``eval()`` fonksiyonunun doğru uygulanış biçimini
gösteriyor:

.. image:: ../images/misc/eval_dogru.png
    :align: center
    :width: 75%

Burada ise, veri ``eval()`` fonksiyonuna ulaşmadan önce kontrolden geçiriliyor.
Eğer veri ancak kontrol aşamasından geçerse ``eval()`` fonksiyona ulaşabilecek
ve oradan da çıktı olarak verilebilecektir. Böylece kullanıcıdan gelen komutları
süzme imkanına sahip oluyoruz.

Gördüğünüz gibi, Python ``eval()`` gibi bir fonksiyon yardımıyla karakter
dizileri içinde geçen Python kodlarını ayıklayıp bunları çalıştırabiliyor. Bu
sayede, mesela bize ``input()`` fonksiyonu aracılığıyla gelen bir karakter
dizisi içindeki Python kodlarını işletme imkanına sahip olabiliyoruz. Bu
özellik, dikkatli kullanıldığında, işlerinizi epey kolaylaştırabilir.

Python'da ``eval()`` fonksiyonuna çok benzeyen ``exec()`` adlı başka bir
fonksiyon daha bulunur. ``eval()`` ile yapamadığımız bazı şeyleri ``exec()`` ile
yapabiliriz. Bu fonksiyon yardımıyla, karakter dizileri içindeki çok kapsamlı
Python kodlarını işletebilirsiniz.

Örneğin ``eval()`` fonksiyonu bir karakter dizisi içindeki değişken tanımlama
işlemini yerine getiremez. Yani ``eval()`` ile şöyle bir şey yapamazsınız::
    
    >>> eval("a = 45")

Ama ``exec()`` ile böyle bir işlem yapabilirsiniz::

    >>> exec("a = 45")

Böylece `a` adlı bir değişken tanımlamış olduk. Kontrol edelim::

    >>> print(a)
    
    45

``eval()`` ve ``exec()`` fonksiyonları özellikle kullanıcıdan alınan verilerle
doğrudan işlem yapmak gereken durumlarda işinize yarar. Örneğin bir hesap
makinesi yaparken ``eval()`` fonksiyonundan yararlanabilirsiniz.

.. highlight:: python3

Aynı şekilde mesela insanlara Python programlama dilini öğreten bir program
yazıyorsanız ``exec()`` fonksiyonunu şöyle kullanabilirsiniz::
    
    d1 = """

    Python'da ekrana çıktı verebilmek için print() adlı bir 
    fonksiyondan yararlanıyoruz. Bu fonksiyonu şöyle kullanabilirsiniz:

    >>> print("Merhaba Dünya")

    Şimdi de aynı kodu siz yazın!

    >>> """

    girdi = input(d1)

    exec(girdi)

    d2 = """

    Gördüğünüz gibi print() fonksiyonu, kendisine
    parametre olarak verilen değerleri ekrana basıyor. 

    Böylece ilk dersimizi tamamlamış olduk. Şimdi bir 
    sonraki dersimize geçebiliriz."""

    print(d2)

Burada ``exec()`` ile yaptığımız işi ``eval()`` ile de yapabiliriz. Ama mesela
eğer bir sonraki derste 'Python'da değişkenler' konusunu öğretecekseniz,
``eval()`` yerine ``exec()`` fonksiyonunu kullanmak durumunda kalabilirsiniz.

``eval()`` fonksiyonunu anlatırken güvenlik ile ilgili olarak söylediğimiz her
şey ``exec()`` fonksiyonu için de geçerlidir. Dolayısıyla bu iki fonksiyonu çok
dikkatli bir şekilde kullanmanız ve bu fonksiyonların doğurduğu güvenlik
açığının bilincinde olmanız gerekiyor.

Henüz Python bilgilerimiz çok kısıtlı olduğu için ``eval()`` ve ``exec()``
fonksiyonlarını bütün ayrıntılarıyla inceleyemiyoruz. Ama bilgimiz arttıkça bu
fonksiyonların ne kadar güçlü (ve tehlikeli) araçlar olduğunu siz de
göreceksiniz.

format() Metodu
***************

Python programlama dili içindeki çok temel bazı araçları incelediğimize göre, bu
noktada Python'daki küçük ama önemli bir konuya değinelim bu bölümü kapatmadan
önce.

İnternette dolaşırken mutlaka şuna benzer bir sayfayla karşılaşmış olmalısınız:

.. image:: ../images/misc/unknown_url.png
    :align: center
    :width: 75%

Burada belli ki adres çubuğuna `fdkgd.com <http://www.fdkgd.com>`_ diye bir URL
yazmışız, ama böyle bir internet adresi olmadığı için, kullandığımız internet
tarayıcısı bize şöyle bir mesaj vermiş::
    
    Hata! Google Chrome fdkgd.com sitesini bulamadı

Şimdi de `dadasdaf.com <http://dadasdaf.com/>`_ adresini arayalım...

Yine böyle bir adres olmadığı için, bu defa tarayıcımız bize şöyle bir uyarı
gösterecek::
    
    Hata! Google Chrome dadasdaf.com sitesini bulamadı

Gördüğünüz gibi, hata mesajlarında değişen tek yer, aradığımız sitenin adresi.
Yani internet tarayıcımız bu hata için şöyle bir taslağa sahip::
    
    Hata! Google Chrome ... sitesini bulamadı

Burada `...` ile gösterdiğimiz yere, bulunamayan URL yerleştiriliyor. Peki böyle
bir şeyi Python programlama dili ile nasıl yapabiliriz?

Çok basit::

    #Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
    url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

    #Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
    print("Hata! Google Chrome", url, "sitesini bulamadı")

Gördüğünüz gibi, şimdiye kadar öğrendiğimiz bilgileri kullanarak böyle bir
programı rahatlıkla yazabiliyoruz.

Peki ya biz kullanıcının girdiği internet adresini mesela tırnak içinde
göstermek istersek ne olacak? Yani örneğin şöyle bir çıktı vermek istersek::
    
    Hata! Google Chrome 'fdsfd.com' sitesini bulamadı

Bunun için yine karakter dizisi birleştirme yönteminden yararlanabilirsiniz::

    #Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
    url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

    #Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
    print("Hata! Google Chrome", "'" + url + "'", "sitesini bulamadı")

Burada, `+` işaretlerini kullanarak, kullanıcının girdiği adresin sağına ve
soluna birer tırnak işaretini nasıl yerleştirdiğimize dikkat edin.

Gördüğünüz gibi bu yöntem işe yarıyor, ama ortaya çıkan karakter dizisi de
oldukça karmaşık görünüyor. İşte bu tür 'karakter dizisi biçimlendirme'
işlemleri için Python bize çok faydalı bir araç sunuyor. Bu aracın adı
``format()``.

Bu aracı şöyle kullanıyoruz::

    #Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
    url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

    #Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
    print("Hata! Google Chrome {} sitesini bulamadı".format(url))

Bir de bulunamayan internet adresini tırnak içine alalım::

    print("Hata! Google Chrome '{}' sitesini bulamadı".format(url))

Görüyorsunuz ya, biraz önce karakter dizisi birleştirme yöntemini kullanarak
gerçekleştirdiğimiz işlemi, çok daha basit bir yolla gerçekleştirme imkanı
sunuyor bize bu ``format()`` denen araç...

Peki ``format()`` nasıl çalışıyor? 

Bunu anlamak için şu basit örneklere bir bakalım::

    >>> print("{} ve {} iyi bir ikilidir".format("Python", "Django"))
    
    'Python ve Django iyi bir ikilidir'

    >>> print("{} {}'yi seviyor!".format("Ali", "Ayşe"))
    
    'Ali Ayşe'yi seviyor!'
    
    >>> print("{} {} yaşında bir {}dur".format("Ahmet", "18", "futbolcu"))
    
    'Ahmet 18 yaşında bir futbolcudur'

Elbette bu örnekleri şöyle de yazabilirdik::

    >>> metin = "{} ve {} iyi bir ikilidir"
    >>> metin.format("Python", "Django")
    
    'Python ve Django iyi bir ikilidir'

    >>> metin = "{} {}'yi seviyor!"
    >>> metin.format("Ali", "Ayşe")
    
    'Ali Ayşe'yi seviyor!'
    
    >>> metin = "{} {} yaşında bir {}dur"
    >>> metin.format("Ahmet", "18", "futbolcu")
    
    'Ahmet 18 yaşında bir futbolcudur'

Burada taslak metni doğrudan ``format()`` metoduna parametre olarak vermeden
önce bir değişkene atadık. Böylece bu metni daha kolay bir şekilde
kullanabildik.

Bu örneklerin, ``format()`` denen aracı anlamak konusunda size epey fikir
verdiğini zannediyorum. Ama isterseniz bu aracın ne olduğunu ve nasıl
çalıştığını daha ayrıntılı olarak incelemeye geçmeden önce başka bir örnek daha
verelim.

Varsayalım ki kullanıcıdan aldığı bilgiler doğrultusunda, özel bir konu üzerine
dilekçe oluşturan bir program yazmak istiyorsunuz.

Dilekçe taslağımız şu şekilde olsun::

                                                            tarih: 

    T.C.
    ... ÜNİVERSİTESİ
    ... Fakültesi Dekanlığına


    Fakülteniz ..........Bölümü ......... numaralı öğrencisiyim. Ekte sunduğum 
    belgede belirtilen mazeretim gereğince ....... Eğitim-Öğretim Yılı  ......... 
    yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

        Bilgilerinizi ve gereğini arz ederim.
        
        İmza
        
    Ad-Soyadı       :
    T.C. Kimlik No. : 
    Adres           :
    Tel.            :
    Ekler           :

Amacınız bu dilekçedeki boşluklara gelmesi gereken bilgileri kullanıcıdan alıp,
eksiksiz bir dilekçe ortaya çıkarmak.

Kullanıcıdan bilgi alma kısmı kolay. ``input()`` fonksiyonunu kullanarak gerekli
bilgileri kullanıcıdan alabileceğimizi biliyorsunuz::
    
    tarih           = input("tarih: ")
    üniversite      = input("üniversite adı: ")
    fakülte         = input("fakülte adı: ")
    bölüm           = input("bölüm adı: ")
    öğrenci_no      = input("öğrenci no. :")
    öğretim_yılı    = input("öğretim yılı: ")
    yarıyıl         = input("yarıyıl: ")
    ad              = input("öğrencinin adı: ")
    soyad           = input("öğrencinin soyadı: ")
    tc_kimlik_no    = input("TC Kimlik no. :")
    adres           = input("adres: ")
    tel             = input("telefon: ")
    ekler           = input("ekler: ")

Bilgileri kullanıcıdan aldık. Peki ama bu bilgileri dilekçe taslağı içindeki
boşluklara nasıl yerleştireceğiz?

Şu ana kadar öğrendiğimiz ``print()`` fonksiyonunu ve `\\t` ve `\\n` gibi kaçış
dizilerini kullanarak istediğiniz çıktıyı elde etmeyi deneyebilirsiniz. Ama
denediğinizde siz de göreceksiniz ki, bu tür yöntemleri kullanarak yukarıdaki
dilekçe taslağını doldurmak inanılmaz zor ve vakit alıcı olacaktır. Halbuki
bunların hiçbirine gerek yok. Çünkü Python bize bu tür durumlarda kullanılmak
üzere çok pratik bir araç sunuyor. Şimdi çok dikkatlice inceleyin şu kodları::
    
    dilekçe = """
                                                        tarih: {}


    T.C.
    {} ÜNİVERSİTESİ
    {} Fakültesi Dekanlığına


    Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede
    belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı  {}.
    yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

        Bilgilerinizi ve gereğini arz ederim.

            İmza

    Ad              : {}
    Soyad           : {}
    T.C. Kimlik No. : {}
    Adres           : {}
    Tel.            : {}
    Ekler           : {}
    """


    tarih           = input("tarih: ")
    üniversite      = input("üniversite adı: ")
    fakülte         = input("fakülte adı: ")
    bölüm           = input("bölüm adı: ")
    öğrenci_no      = input("öğrenci no. :")
    öğretim_yılı    = input("öğretim yılı: ")
    yarıyıl         = input("yarıyıl: ")
    ad              = input("öğrencinin adı: ")
    soyad           = input("öğrencinin soyadı: ")
    tc_kimlik_no    = input("TC Kimlik no. :")
    adres           = input("adres: ")
    tel             = input("telefon: ")
    ekler           = input("ekler: ")

    print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
                         öğrenci_no, öğretim_yılı, yarıyıl,
                         ad, soyad, tc_kimlik_no,
                         adres, tel, ekler))

Bu kodlara (ve bundan önceki örneklere) bakarak birkaç tespitte bulunalım:

    #. Taslak metinde kullanıcıdan alınacak bilgilerin olduğu yerlere birer `{}` 
       işareti yerleştirdik. 
    
    #. Taslaktaki eksiklikleri tamamlayacak verileri ``input()`` fonksiyonu 
       yardımıyla kullanıcıdan tek tek aldık.
    
    #. Son olarak, ``print()`` fonksiyonu yardımıyla metni tam bir şekilde ekrana 
       çıktı olarak verdik. 

Şimdi son tespitimizi biraz açıklayalım. Gördüğünüz gibi, ``print()`` fonksiyonu
içinde ``dilekçe.format()`` gibi bir yapı var. Burada `dilekçe` değişkenine
nokta işareti ile bağlanmış ``format()`` adlı, fonksiyon benzeri bir araç
görüyoruz. Bu araca teknik dilde 'metot' adı verilir. ``format()`` metodunun
parantezleri içinde ise, kullanıcıdan alıp birer değişkene atadığımız veriler
yer alıyor.

Dilerseniz yukarıda olan biteni daha net anlayabilmek için bu konunun başına
verdiğimiz örneklere geri dönelim.

İlk olarak şöyle bir örnek vermiştik::

    #Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
    url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

    #Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
    print("Hata! Google Chrome {} sitesini bulamadı".format(url))

Burada kullanıcının gireceği internet adresinin yerini tutması için `{}`
işaretlerinden yararlanarak şöyle bir karakter dizisi oluşturduk::
    
    "Hata! Google Chrome {} sitesini bulamadı"
    
Gördüğünüz gibi, `{}` işareti karakter dizisi içinde URL'nin geleceği yeri
tutuyor. Bu `{}` işaretinin yerine neyin geleceğini ``format()`` metodunun
parantezleri içinde belirtiyoruz. Dikkatlice bakın::
    
    print("Hata! Google Chrome {} sitesini bulamadı".format(url))

Elbette eğer istersek yukarıdaki örneği şöyle de yazabilirdik::

    url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

    #Kullanıcıya gösterilecek hata için bir taslak metin oluşturuyoruz
    hata_taslağı = "Hata! Google Chrome {} sitesini bulamadı"

    print(hata_taslağı.format(url))

Burada hata metnini içeren karakter dizisini doğrudan ``format()`` metoduna
bağlamak yerine, bunu bir değişkene atayıp, ``format()`` metodunu bu değişkene
bağladık.

Bunun dışında şu örnekleri de vermiştik::

    >>> metin = "{} ve {} iyi bir ikilidir"
    >>> metin.format("Python", "Django")
    
    'Python ve Django iyi bir ikilidir

    >>> metin = "{} {}'yi seviyor!"
    >>> metin.format("Ali", "Ayşe")
    
    'Ali Ayşe'yi seviyor!'
    
    >>> metin = "{} {} yaşında bir {}dur"
    >>> metin.format("Ahmet", "18", "futbolcu")
    
    'Ahmet 18 yaşında bir futbolcudur'

Burada da, gördüğüz gibi, öncelikle bir karakter dizisi tanımlıyoruz. Bu
karakter dizisi içindeki değişken değerleri ise `{}` işaretleri ile
gösteriyoruz. Daha sonra ``format()`` metodunu alıp bu karakter dizisine
bağlıyoruz. Karakter dizisi içindeki `{}` işaretleri ile gösterdiğimiz yerlere
gelecek değerleri de ``format()`` metodunun parantezleri içinde gösteriyoruz.
Yalnız burada şuna dikkat etmemiz lazım: Karakter dizisi içinde kaç tane `{}`
işareti varsa, ``format()`` metodunun parantezleri içinde de o sayıda değer
olması gerekiyor.

Bu yapının, yazdığımız programlarda işimizi ne kadar kolaylaştıracağını tahmin
edebilirsiniz. Kısa karakter dizilerinde pek belli olmayabilir, ama özellikle
çok uzun ve boşluklu karakter dizilerini biçimlendirirken ``format()`` metodunun
hayat kurtardığına kendiniz de şahit olacaksınız.

İlerleyen derslerimizde ``format()`` metodunu ve karakter dizisi biçimlendirme
konusunu çok daha ayrıntılı bir şekilde inceleyeceğiz. Ancak yukarıda verdiğimiz
bilgiler ``format()`` metodunu verimli bir şekilde kullanabilmenizi sağlamaya
yetecek düzeydedir.

