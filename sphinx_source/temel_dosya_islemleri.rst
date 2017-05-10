.. meta::
   :description: Bu bölümde temel dosya işlemleri konusunu ayrıntılı bir şekilde inceleyeceğiz.
   :keywords: python, python3, dosyalar

.. highlight:: py3


**********************
Temel Dosya İşlemleri
**********************

Hatırlarsanız ``print()`` fonksiyonunu anlatırken, bu fonksiyonun `file` adlı
bir parametresi olduğundan söz etmiştik. Bu parametre yardımıyla ``print()``
fonksiyonunun çıktılarını bir dosyaya gönderebiliyorduk. Böylece ``print()``
fonksiyonunun bu özelliği sayesinde, Python'daki 'Dosya Girdi/Çıktısı' (*File
I/O*) konusuyla da ilk kez tanışmış olmuştuk.

Ayrıca ``print()`` fonksiyonu dışında, ``open()`` adlı başka bir fonksiyon
yardımıyla da dosyaları açabileceğimizi ve bu dosyaların üzerinde çeşitli
işlemleri gerçekleştirebileceğimizi öğrenmiştik. Ancak gerek ``print()``
fonksiyonunun `file` parametresi, gerekse ``open()`` fonksiyonuyla şimdiye kadar
yaptığımız örnekler aracılığıyla öğrendiklerimiz dosyalara ilişkin çok sınırlı
işlemleri yerine getirmemizi sağlıyordu.

İşte biz bu bölümde, dosya girdi/çıktısı konusuna ilişkin bildiklerimizi bir
adım öteye götüreceğiz ve gerçek anlamda dosyaları nasıl manipüle edeceğimizi
öğreneceğiz.

Programcılık maceramız boyunca dosyalarla bol bol muhatap olacaksınız. O yüzden
bu konuyu olabildiğince ayrıntılı ve anlaşılır bir şekilde anlatmaya
çalışacağız.

Dediğimiz gibi, biz esasında bu noktaya gelinceye kadar çeşitli fonksiyonlar ve
bunların birtakım parametreleri aracılığıyla dosya işlemlerinden az da olsa
zaten söz etmiştik. Dolayısıyla aslında tamamen yabancısı olduğunuz bir konuyla
karşı karşıya olmanız gibi bir durum söz konusu değil. Biz bu bölümde, zaten
aşina olduğumuz bir konuyu çok daha derinlemesine ele alacağız.

Python programlama dilinde dosyalarla uğraşırken bütün dosya işlemleri için
temel olarak tek bir fonksiyondan yararlanacağız. Bu fonksiyonu siz zaten
tanıyorsunuz. Fonksiyonumuzun adı ``open()``.

Dosya Oluşturmak
****************

Dediğimiz gibi, Python programlama dilinde dosya işlemleri için ``open()`` adlı
bir fonksiyondan yararlanacağız. İşte dosya oluşturmak için de bu fonksiyonu
kullanacağız. 

Önceki derslerimizde verdiğimiz örneklerden de bildiğiniz gibi, ``open()``
fonksiyonunu temel olarak şöyle kullanıyoruz::
    
    f = open(dosya_adı, kip)
    
.. note:: ``open()`` fonksiyonu `dosya_adı` ve `kip` dışında başka parametreler
          de alır. İlerleyen sayfalarda bu parametrelerden de söz edeceğiz. 

Mesela "tahsilat.txt" adlı bir dosyayı **yazma** kipinde açmak için şöyle bir
komut kullanıyoruz::
    
    tahsilat_dosyası = open("tahsilat_dosyası.txt", "w")

Burada 'tahsilat_dosyası.txt' ifadesi dosyamızın adını belirtiyor. `"w"` harfi
ise bu dosyanın yazma kipinde açıldığını söylüyor. 

Yukarıdaki komutu çalıştırdığınızda, o anda hangi dizin altında bulunuyorsanız
o dizin içinde `tahsilat_dosyası.txt` adlı boş bir dosyanın oluştuğunu
göreceksiniz. 

Bu arada, dosya adını yazarken, dosya adı ile birlikte o dosyanın hangi dizin
altında oluşturulacağını da belirleyebilirsiniz. Örneğin::
    
    dosya = open("/dosyayı/oluşturmak/istediğimiz/dizin/dosya_adı", "w")

Eğer dosya adını dizin belirtmeden yazarsanız, oluşturduğunuz dosya, o anda
hangi dizin altında bulunuyorsanız orada oluşacaktır.  

Ayrıca dosyayı barındıran dizin adlarını yazarken, dizinleri ayırmak için ters
taksim (`\\`) yerine düz taksim (`/`) kullanmaya dikkat edin. Aksi halde, dizin
adı oluşturmaya çalışırken yanlışlıkla kaçış dizileri oluşturabilirsiniz.
Esasında siz bu olguya hiç yabancı değilsiniz. Zira kaçış dizilerini anlatırken
şöyle bir örnek verdiğimizi hatırlıyor olmalısınız::
    
    print("C:\aylar\nisan\toplam masraf")

İşte eğer bu örnekte olduğu gibi ters taksim işaretleri ile oluşturulmuş dizin
adları kullanırsanız programınız hata verecektir::
    
    >>> open("C:\aylar\nisan\toplam masraf\masraf.txt", "w")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OSError: [Errno 22] Invalid argument: 'C:\x07ylar\nisan\toplam masraf\masraf.txt'
    
Bunun sebebi, bildiğiniz gibi, Python'ın `\\a`, `\\n` ve `\\t` ifadelerini birer
kaçış dizisi olarak algılamasıdır. Bu durumdan kaçabilmek için, dizin adlarını
ters taksim işareti ile ayırmanın dışında, `r` adlı kaçış dizisinden de
yararlanabilirsiniz::
    
    >>> open(r"C:\aylar\nisan\toplam masraf\masraf.txt", "w")

...veya ters taksim işaretlerini çiftleyebilirsiniz::
    
    >>> open("C:\\aylar\\nisan\\toplam masraf\\masraf.txt", "w")
    
Bu şekilde, eğer bilgisayarınızda `C:\\aylar\\nisan\\toplam masraf\\` adlı bir
dizin varsa, o dizin içinde `masraf.txt` adlı bir dosya oluşturulacaktır.
    
Böylece Python programlama dilinde boş bir dosyanın nasıl oluşturulacağını
öğrenmiş olduk. O halde gelin isterseniz şimdi bu dosyanın içini nasıl
dolduracağımızı öğrenelim. 

Dosyaya Yazmak
***************

Bir dosyayı, yukarıda gösterdiğimiz şekilde yazma kipinde açtığımız zaman,
Python bizim için içi boş bir dosya oluşturacaktır. Peki biz bu dosyanın içini
nasıl dolduracağız? 

Python programlama dilinde, ``open()`` fonksiyonu ile yazma kipinde açtığımız
bir dosyaya bir veri yazabilmek için dosyaların ``write()`` adlı
metodundan yararlanacağız. 

Siz aslında bu metodun da nasıl kullanılacağını çok iyi biliyorsunuz::
    
    dosya.write(yazılacak_şeyler)

Gelin bu formülü somutlaştıracak bir örnek verelim. Mesela yukarıda
oluşturduğumuz tahsilat dosyasının içine bazı veriler girelim.

Önce dosyamızı nasıl oluşturacağımızı hatırlayalım::
    
    ths = open("tahsilat_dosyası.txt", "w")

Şimdi de bu dosyaya şu bilgileri girelim::
    
    ths.write("Halil Pazarlama: 120.000 TL")
    
Yani programımız şöyle görünsün::
    
    ths = open("tahsilat_dosyası.txt", "w")
    ths.write("Halil Pazarlama: 120.000 TL")

Bu komutları verdiğinizde, `tahsilat_dosyası.txt` adlı dosyanın içine şu
bilgilerin işlendiğini göreceksiniz::
    
    Halil Pazarlama: 120.000 TL
    
Eğer dosyayı açtığınızda bu bilgi yerine hâlâ boş bir dosya görüyorsanız, sebebi
tamponda tutulan verilerin henüz dosyaya işlenmemiş olmasıdır. 

.. note:: Bu konuyu ``print()`` fonksiyonunun `flush` adlı parametresini
          incelerken öğrendiğimizi hatırlıyor olmalısınız.
          
Eğer durum böyleyse, dosyanızı kapatmanız gerekiyor. Bunu ``close()`` adlı başka
bir metotla yapabildiğimizi biliyorsunuz::
    
    ths.close()
    
Bu arada, bu söylediklerimizden, eğer yazdığınız bilgiler zaten dosyaya
işlenmişse dosyayı kapatmanıza gerek olmadığı anlamını çıkarmayın. Herhangi bir
şekilde açtığınız dosyaları kapatmanız, özellikle dosyanın açılmasıyla birlikte
kullanılmaya başlayan ve arka planda çalışan kaynakların serbest bırakılması
açısından büyük önem taşıyor. O yüzden açtığımız dosyaların tamamını programın
işleyişi sona erdiğinde kapatmayı unutmuyoruz. Yani yukarıdaki programı tam
olarak şöyle yazıyoruz::
    
    ths = open("tahsilat_dosyası.txt", "w")
    ths.write("Halil Pazarlama: 120.000 TL"),
    ths.close()
    
Bu kodlarda sırasıyla şu işlemleri gerçekleştirdik:

#. `tahsilat_dosyası` adlı bir dosyayı yazma kipinde açarak, bu adda bir
   dosya oluşturulmasını sağladık,
  
#. ``write()`` metodunu kullanarak bu dosyaya bazı bilgiler girdik,

#. Dosyamıza yazdığımız bilgilerin dosyaya işlendiğinden emin olmak ve
   işletim sisteminin dosyanın açılması ve dosyaya veri işlenmesi için devreye
   soktuğu bütün kaynakları serbest bırakmak için ``close()`` metoduyla
   programımızı kapattık. 
    
Bu arada, bu başlığı kapatmadan önce önemli bir bilgi daha verelim. Python'da
bir dosyayı `"w"` kipinde açtığımızda, eğer o adda bir dosya ilgili dizin içinde
zaten varsa, Python bu dosyayı sorgusuz sualsiz silip, yerine aynı adda başka
bir boş dosya oluşturacaktır. Yani mesela yukarıda `tahsilat_dosyası.txt` adlı
dosyayı oluşturup içine bir şeyler yazdıktan sonra bu dosyayı yine `"w"` kipinde
açmaya çalışırsanız, Python bu dosyanın bütün içeriğini silip, yine
`tahsilat_dosyası.txt` adını taşıyan başka bir dosya oluşturacaktır. O yüzden
dosya işlemleri sırasında bu `"w"` kipini kullanırken dikkat ediyoruz ve disk
üzerinde var olan dosyalarımızı yanlışlıkla silmiyoruz. 

Böylece bir dosyanın nasıl oluşturulacağını, nasıl açılacağını ve içine birtakım
bilgilerin nasıl girileceğini kabataslak da olsa öğrenmiş olduk. Şimdi de
dosyaları nasıl **okuyacağımızı** öğrenelim.

Dosya Okumak
************

Bir önceki başlıkta dosyaların içine bilgi girme işleminin Python programlama
dilinde nasıl yapıldığını inceledik. Elbette bir dosyaya yazabilmenin yanısıra,
bilgisayarınızda halihazırda var olan bir dosyayı okumak da isteyeceksiniz. Peki
bunu nasıl yapacaksınız? 

Python'da bir dosyayı okumak için yukarıda anlattığımız yazma yöntemine benzer
bir yöntem kullanacağız. Bildiğiniz gibi, bir dosyayı yazma kipinde açmak için
`"w"` harfini kullanıyoruz. Bir dosyayı okuma kipinde açmak için ise `"r"`
harfini kullanacağız. 

Mesela, bilgisayarımızda var olan `fihrist.txt` adlı dosyayı okumak üzere
açalım::
    
    fihrist = open("fihrist.txt", "r")
    
Bir dosyayı ``open()`` fonksiyonu yardımıyla açarken kip parametresi için `"r"`
harfini kullanırsak, Python o dosyayı okuma yetkisiyle açacaktır. Yalnız burada
şöyle bir özellik var: Eğer bir dosyayı okuma kipinde açacaksanız, bu `"r"`
harfini hiç belirtmeseniz de olur. Yani şu komut bilgisayarımızdaki
`fihrist.txt` adlı dosyayı okuma kipinde açacaktır::
    
    fihrist = open("fihrist.txt")

Dolayısıyla bir dosyayı açarken kip belirtmediğimizde Python bizim o dosyayı
okuma kipinde açmak istediğimizi varsayacaktır. 

Hatırlarsanız, `"w"` kipiyle açtığımız bir dosyaya yazmak için ``write()`` adlı
bir metottan yararlanıyorduk. `"r"` kipiyle açtığımız bir dosyayı okumak için
ise ``read()``, ``readline()`` ve ``readlines()`` adlı üç farklı metottan
yararlanacağız. 

Yukarıdaki üç metot da Python'da dosya okuma işlemlerini gerçekleştirmemizi
sağlar. Peki bu metotların üçü de aynı işi yapıyorsa neden tek bir metot değil
de üç farklı metot var? 

Bu metotların üçü de dosya okumaya yarasa da, verdikleri çıktılar birbirinden
farklıdır. O yüzden farklı amaçlar için farklı metodu kullanmanız gereken
durumlarla karşılaşabilirsiniz. 

Bu metotlar arasındaki farkı anlamanın en kolay yolu bu üç metodu sırayla
kullanıp, çıktıları incelemektir. 

Öncelikle içeriği şu olan, `fihrist.txt` adlı bir dosyamızın olduğunu
varsayalım::
    
    Ahmet Özbudak : 0533 123 23 34
    Mehmet Sülün  : 0532 212 22 22
    Sami Sam      : 0542 333 34 34
    
Şimdi bir dosya açıp şu kodları yazalım::
    
    fihrist = open("fihrist.txt")
    print(fihrist.read())

Bu kodları çalıştırdığımızda, eğer kullandığınız işletim sistemi GNU/Linux ise
muhtemelen şu çıktıyı elde edeceksiniz::
    
    Ahmet Özbudak : 0533 123 23 34
    Mehmet Sülün  : 0532 212 22 22
    Sami Sam      : 0542 333 34 34
    
Ama eğer bu kodları Windows'ta çalıştırdıysanız Türkçe karakterler bozuk çıkmış
olabilir. Bu durumu şimdilik görmezden gelin. Birazdan bu durumun nedenini
açıklayacağız.

Yukarıda elde ettiğimiz şey bir karakter dizisidir bunu şu şekilde teyit
edebileceğinizi biliyorsunuz::
    
    fihrist = open("fihrist.txt")
    print(type(fihrist.read()))

Gördüğünüz gibi, ``read()`` metodu bize, dosyanın bütün içeriğini bir karakter
dizisi olarak veriyor. Bir de şuna bakalım::

    fihrist = open("fihrist.txt")
    print(fihrist.readline())
    
Burada da ``readline()`` metodunu kullandık. Bu kodlar bize şöyle bir çıktı
veriyor::
    
    Ahmet Özbudak : 0533 123 23 34
    
``read()`` metodu bize dosya içeriğinin tamamını veriyordu. Gördüğünüz gibi
``readline()`` metodu tek bir satır veriyor. Yani bu metot yardımıyla dosyaları
satır satır okuyabiliyoruz. 

Bu metodun işleyiş tarzını daha iyi görebilmek için bu kodları dosyaya yazıp
çalıştırmak yerine etkileşimli kabuk üzerinden de çalıştırabilirsiniz::
    
    >>> fihrist = open("fihrist.txt", "r")
    >>> print(fihrist.readline())
    
    Ahmet Özbudak : 0533 123 23 34
    
    >>> print(fihrist.readline())
    
    Mehmet Sülün  : 0532 212 22 22
    
    >>> print(fihrist.readline())
    
    Sami Sam      : 0542 333 34 34

Gördüğünüz gibi, ``readline()`` metodu gerçekten de dosyayı satır satır okuyor. 

Son satırı da okuduktan sonra, ``readline()`` metodunu tekrar çalıştırırsak ne
olur peki? Bakalım::
    
    >>> print(fihrist.readline())
    
Gördüğünüz gibi, bu defa hiçbir çıktı almadık. Çünkü dosyada okunacak satır
kalmadı. Bu yüzden de Python bize boş bir çıktı verdi. Bu durumu daha net görmek
için kodu etkileşimli kabukta ``print()`` olmadan yazabilirsiniz::
    
    >>> fihrist.readline()
    
    ''
    
Gerçekten de elimizdeki şey boş bir karakter dizisi... Demek ki bir dosya
tamamen okunduktan sonra, Python otomatik olarak tekrar dosyanın başına
dönmüyor. Böyle bir durumda dosyanın başına nasıl geri döneceğimizi
inceleyeceğiz, ama isterseniz biz başka bir konuyla devam edelim.

.. note:: Bir dosyanın tamamı okunduktan sonra otomatik olarak başa sarılmaması
          özelliği sadece ``readline()`` metodu için değil, öteki bütün dosya okuma
          metotları için de geçerlidir. Yani bir dosyayı ``read()``, ``readline()`` veya
          ``readlines()`` metotlarından herhangi biri ile okuduğunuzda imleç başa dönmez. 

Dediğimiz ve gösterdiğimiz gibi, ``read()`` ve ``readline()`` metotları bize bir
karakter dizisi döndürüyor. Bu iki metot arasındaki fark ise, ``read()``
metodunun dosyanın tamamını önümüze sererken, ``readline()`` metodunun dosyayı
satır satır okuyup, her defasında tek bir satırı önümüze sürmesidir. Bir de
``readlines()`` metodunun ne yaptığına bakalım... 

Şu kodları yazalım::
    
    fihrist = open("fihrist.txt")
    print(fihrist.readlines())

Bu kodları yazdığımızda şuna benzer bir çıktı alacağız:: 
    
    ['Ahmet Özbudak : 0533 123 23 34\n', 'Mehmet Sülün  : 0532 212 22 22\n', 
     'Sami Sam      : 0542 333 34 34']
     
Gördüğünüz gibi, bu defa karakter dizisi yerine bir liste ile karşılaşıyoruz.
Demek ki ``read()`` ve ``readline()`` metotları çıktı olarak bize bir karakter
dizisi verirken, ``readlines()`` metodu liste veriyormuş. Bunun neden önemli bir
bilgi olduğunu artık gayet iyi biliyor olmanız lazım. Zira bir verinin tipi, o
veriyle neler yapıp neler yapamayacağımızı doğrudan etkiler...

Dosyaları Otomatik Kapatma
****************************

Daha önce de söylediğimiz gibi, bir dosyayı açıp bu dosya üzerinde gerekli
işlemleri yaptıktan sonra bu dosyayı açık bırakmamak büyük önem taşır.
Dolayısıyla üzerinde işlem yaptığımız bütün dosyaları, işimiz bittikten sonra,
mutlaka kapatmalıyız. Çünkü bir dosya açıldığında işletim sistemi, sistem
kaynaklarının bir kısmını bu dosyaya ayırır. Eğer dosyayı açık bırakırsak,
sistem kaynaklarını gereksiz yere meşgul etmiş oluruz. Ancak farklı sebeplerden,
dosyalar açıldıktan sonra kapanmayabilir. Örneğin açtığınız dosyayı kapatmayı
unutmuş olabilirsiniz. Yani programınızın hiçbir yerinde ``close()`` metodunu
kullanmamışsınızdır. Bunun dışında, programınızdaki bir hata da dosyaların
kapanmasını engelleyebilir. Örneğin bir dosya açıldıktan sonra programda
beklenmeyen bir hata gerçekleşirse, programınız asla ``close()`` satırına
ulaşamayabilir. Bu durumda da açılan dosya kapanmadan öylece bekler.

Bu tür durumlara karşı iki seçeneğiniz var:

    #. ``try... except... finally...`` bloklarından yararlanmak
    #. ``with`` adlı bir deyimi kullanmak
    
Birinci yöntemden daha önce de bahsettiğimizi hatırlıyorsunuz. Hata yakalama
bölümünü anlatırken bununla ilgili şöyle bir örnek vermiştik::
    
    try:
        dosya = open("dosyaadı", "r")
        ...burada dosyayla bazı işlemler yapıyoruz...
        ...ve ansızın bir hata oluşuyor...
    except IOError:
        print("bir hata oluştu!")
    finally:
        dosya.close()
        
Bu yöntem gayet uygun ve iyi bir yöntemdir. Ancak Python bize bu tür durumlar
için çok daha pratik bir yöntem sunar. Dikkatlice bakın::
    
    with open("dosyaadı", "r") as dosya:
        print(dosya.read())
        
Dosyalarımızı bu şekilde açıp üzerlerinde işlemlerimizi yaptığımızda Python
dosyayı bizim için kendisi kapatacaktır. Bu şekilde bizim ayrıca bir ``close()``
satırı yazmamıza gerek yok. ``with`` deyimini kullanmamız sayesinde, dosya
açıldıktan sonra arada bir hata oluşsa bile Python dosyayı sağsalim kapatıp
sistem kaynaklarının israf edilmesini önleyecektir. 

Dosyayı İleri-Geri Sarmak
**************************

Dosya okumak için kullanılan metotları anlatırken, dosya bir kez okunduktan
sonra imlecin otomatik olarak dosyanın başına dönmediğini görmüştük. Yani mesela
``read()`` metoduyla dosyayı bir kez okuduktan sonra, dosyayı tekrar okumak
istersek elde edeceğimiz şey boş bir karakter dizisi olacaktır. Çünkü dosya
okunduktan sonra okunacak başka bir satır kalmamış, imleç dosya sonuna ulaşmış
ve otomatik olarak da başa dönmemiştir. Bu olguyu etkileşimli kabuk üzerinde
daha net bir şekilde görebileceğinizi biliyorsunuz. 

Peki dosyayı tamamen okuduktan sonra tekrar başa dönmek istersek ne yapacağız? 
Bir dosya tamamen okunduktan sonra tekrar başa dönmek için dosyaların ``seek()``
adlı bir metodundan yararlanacağız. 

Mesela şu örneklere bakalım. Bu örnekleri daha iyi anlamak için bunları
Python'ın etkileşimli kabuğunda çalıştırmanızı tavsiye ederim::
    
    >>> f = open("python.txt")
    >>> f.read()
    
    'Bu programlama dili Guido Van Rossum adlı Hollandalı bir
    programcı\ntarafından 90’lı yılların başında geliştirilmeye başlanmıştır.
    Çoğu insan,\nisminin Python olmasına aldanarak, bu programlama dilinin,
    adını piton\nyılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
    programlama dilinin\nadı piton yılanından gelmez. Guido Van Rossum bu
    programlama dilini, The Monty\nPython adlı bir İngiliz komedi grubunun,
    Monty Python’s Flying Circus adlı\ngösterisinden esinlenerek adlandırmıştır.
    Ancak her ne kadar gerçek böyle olsa\nda, Python programlama dilinin pek çok
    yerde bir yılan figürü ile temsil\nedilmesi neredeyse bir gelenek halini
    almıştır.\n' 
    
Burada ``open()`` fonksiyonunu kullanarak `python.txt` adlı bir dosyayı açıp,
``read()`` metodu yardımıyla da bu dosyanın içeriğini okuduk. Bu noktada dosyayı
tekrar okumaya çalışırsak elde edeceğimiz şey boş bir karakter dizisi
olacaktır::
    
    >>> f.read()
    
    ''
    
Çünkü dosya bir kez tamamen okunduktan sonra imleç otomatik olarak başa
dönmüyor. Dosyayı tekrar okumak istiyorsak, bunu başa bizim sarmamız lazım. İşte
bunun için ``seek()`` metodunu kullanacağız::
    
    >>> f.seek(0)

Gördüğünüz gibi ``seek()`` metodunu bir parametre ile birlikte kullandık. Bu
metoda verdiğimiz parametre, dosya içinde kaçıncı bayt konumuna gideceğimizi
gösteriyor. Biz burada `0` sayısını kullanarak dosyanın ilk baytına, yani en
başına dönmüş olduk. Artık dosyayı tekrar okuyabiliriz::
    
    >>> f.read()

    'Bu programlama dili Guido Van Rossum adlı Hollandalı bir
    programcı\ntarafından 90’lı yılların başında geliştirilmeye başlanmıştır.
    Çoğu insan,\nisminin Python olmasına aldanarak, bu programlama dilinin,
    adını piton\nyılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
    programlama dilinin\nadı piton yılanından gelmez. Guido Van Rossum bu
    programlama dilini, The Monty\nPython adlı bir İngiliz komedi grubunun,
    Monty Python’s Flying Circus adlı\ngösterisinden esinlenerek adlandırmıştır.
    Ancak her ne kadar gerçek böyle olsa\nda, Python programlama dilinin pek çok
    yerde bir yılan figürü ile temsil\nedilmesi neredeyse bir gelenek halini
    almıştır.\n'
    
Elbette ``seek()`` metodunu kullanarak istediğiniz bayt konumuna dönebilirsiniz.
Mesela eğer dosyanın `10.` baytının bulunduğu konuma dönmek isterseniz bu metodu
şöyle kullanabilirsiniz::
    
    >>> f.seek(10)
    
Eğer o anda dosyanın hangi bayt konumunda bulunduğunuzu öğrenmek isterseniz de
``tell()`` adlı başka bir metottan yararlanabilirsiniz. Bu metodu parametresiz
olarak kullanıyoruz::
    
    >>> f.tell()
    
    20
    
Bu çıktıya göre o anda dosyanın `20.` baytının üzerindeyiz...

Bu arada, dosya içinde bulunduğumuz konumu baytlar üzerinden tarif etmemizi
biraz yadırgamış olabilirsiniz. Acaba neden karakter değil de bayt? Biraz sonra
bu konuya geleceğiz. Biz şimdilik önemli başka bir konuya değinelim.

Dosyalarda Değişiklik Yapmak
********************************

Buraya kadar, Python'da bir dosyanın nasıl oluşturulacağını, boş bir dosyaya
nasıl veri girileceğini ve varolan bir dosyadan nasıl veri okunacağını öğrendik.
Ama varolan ve içi halihazırda dolu bir dosyaya nasıl veri ekleneceğini
bilmiyoruz. İşte şimdi bu işlemin nasıl yapılacağını tartışacağız. 

Ancak burada önemli bir ayrıntıya dikkatinizi çekmek istiyorum. Dosyaların
neresinde değişiklik yapmak istediğiniz büyük önem taşır. Unutmayın, dosyaların
başında, ortasında ve sonunda değişiklik yapmak birbirlerinden farklı kavramlar
olup, birbirinden farklı işlemlerin uygulanmasını gerektirir.

Biz bu bölümde dosyaların baş tarafına, ortasına ve sonuna nasıl veri eklenip
çıkarılacağını ayrı ayrı tartışacağız. 

Dosyaların Sonunda Değişiklik Yapmak
====================================

Daha önce de söylediğimiz gibi, Python'da bir dosyayı açarken, o dosyayı hangi
kipte açacağımızı belirtmemiz gerekiyor. Yani eğer bir dosyayı okumak istiyorsak
dosyayı `"r"` kipinde, yazmak istiyorsak da `"w"` kipinde açmamız gerekiyor.
Bildiğiniz gibi `"w"` kipi dosya içeriğini tamamen siliyor. 

Eğer bir dosyayı **tamamen silmeden**, o dosyaya ekleme yapmak veya o dosyada
herhangi bir değişiklik yapmak istiyorsak, dosyamızı buraya kadar öğrendiğimiz
iki kipten daha farklı bir kiple açmamız gerekiyor. Şimdi öğreneceğimiz bu yeni
kipin adı `"a"`. Yani Python'da içi boş olmayan bir dosyada değişiklik
yapabilmek için `"a"` adlı bir kipten yararlanacağız::
    
    f = open(dosya_adı, "a")
    
Örneğin yukarıda verdiğimiz `fihrist.txt` adlı dosyayı bu kipte açalım ve
dosyaya yeni bir girdi ekleyelim::
    
    with open("fihrist.txt", "a") as f:
        f.write("Selin Özden\t: 0212 222 22 22")
        
Gördüğünüz gibi, dosyaya yeni eklediğimiz girdiler otomatik olarak dosyanın
sonuna ilave ediliyor. Burada şu noktaya dikkat etmeniz lazım. Dosyanın sonunda
bir satır başı karakterinin (`\\n`) bulunup bulunmamasına bağlı olarak, dosyaya
eklediğiniz yeni satırlar düzgün bir şekilde bir alt satıra geçebileceği gibi,
dosyanın son satırının yanına da eklenebilir. Dolayısıyla duruma göre yukarıdaki
satırı şu şekilde yazmanız gerekebilir::
    
    with open("fihrist.txt", "a") as f:
        f.write("\nSelin Özden\t: 0212 222 22 22")
        
Burada bir alt satıra geçebilmek için 'Selin' ifadesinden önce bir satır başı
karakteri eklediğimize dikkat edin. Ayrıca eğer bu satırdan sonra bir başka
satır daha ekleyecekseniz, ilgili satırın sonuna da bir satır başı karakteri
koymanız gerekebilir::
    
    with open("fihrist.txt", "a") as f:
        f.write("Selin Özden\t: 0212 222 22 22\n")
        
Karşı karşıya olduğunuz duruma göre, satır başı karakterlerine ihtiyacınız olup
olmadığını ve ihtiyacınız varsa bunları nereye yerleştireceğinizi kendiniz
değerlendirmelisiniz.    

Dosyaların Başında Değişiklik Yapmak
======================================

Bir önceki bölümde dosya sonuna nasıl yeni satır ekleyeceğimizi öğrendik. Ama
siz programcılık maceranız sırasında muhtemelen dosyaların sonuna değil de, en
başına ekleme yapmanız gereken durumlarla da karşılaşacaksınız. Python'da bu işi
yapmak da çok kolaydır.

Örnek olması açısından, `fihrist.txt` adlı dosyanın içeriğini ele alalım::
    
    Ahmet Özbudak : 0533 123 23 34
    Mehmet Sülün  : 0532 212 22 22
    Sami Sam      : 0542 333 34 34
    Selin Özden   : 0212 222 22 22
    
Dosya içeriği bu. Eğer bu dosyayı `"a"` kipi ile açtıktan sonra doğrudan
``write()`` metodunu kullanarak bir ekleme yaparsak, yeni değer dosyanın sonuna
eklenecektir. Ama biz mesela şu veriyi::
    
    Sedat Köz     : 0322 234 45 45
    
'Ahmet Özbudak : 0533 123 23 34' girdisinin hemen üstüne, yani dosyanın sonuna
değil de en başına eklemek istersek ne yapacağız?

Öncelikle şu kodları deneyelim::
    
    with open("fihrist.txt", "r") as f:
        veri = f.read()
        f.seek(0) #Dosyayı başa sarıyoruz
        f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
        
Bu kodları bir dosyaya kaydedip çalıştırdığımızda Python bize şu hatayı
verecektir::
    
    istihza@netbook:~/Desktop$ python3 deneme.py 
    Traceback (most recent call last):
      File "deneme.py", line 4, in <module>
        f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
    io.UnsupportedOperation: not writable
    
Bu hatayı almamızın sebebi dosyayı 'okuma' kipinde açmış olmamız. Çünkü bir
dosyayı okuma kipinde açtığımızda o dosya üzerinde yalnızca okuma işlemleri
yapabiliriz. Dosyaya yeni veri ekleme kısmına gelindiğinde, dosya yalnızca okuma
yetkisine sahip olduğu için, Python bize yukarıdaki hata mesajını verecek,
dosyanın 'yazılamaz' olduğundan şikayet edecektir.

Peki dosyayı `"w"` karakteri yardımıyla yazma kipinde açarsak ne olur? O zaman
da şu meş'um hatayı alırız::
        
    istihza@netbook:~/Desktop$ python3 deneme.py 
    Traceback (most recent call last):
      File "deneme.py", line 2, in <module>
        veri = f.read()
    io.UnsupportedOperation: not readable
    
Gördüğünüz gibi, bu kez de dosyanın okunamadığına ilişkin bir hata alıyoruz.
Çünkü biz bu kez de dosyayı 'yazma' kipinde açtık. Ancak burada şöyle bir durum
var. Bildiğiniz gibi, bir dosyayı `"w"` kipi ile açtığımızda, Python bize hiçbir
şey sormadan varolan içeriği silecektir. Burada da yukarıda yazdığımız kodlar
yüzünden dosya içeriğini kaybettik. Unutmayın, dosya okuma-yazma işlemleri belli
bir takım riskleri içinde barındırır. O yüzden bu tür işlemleri yaparken
fazladan dikkat göstermeliyiz. 

Yukarıda da gördüğümüz gibi, dosyamızı `"r"` veya `"w"` kiplerinde açmak işe
yaramadı. Peki ne yapacağız? Bunun cevabı çok basit: Dosyamızı hem okuma hem de
yazma kipinde açacağız. Bunun için de farklı bir kip kullanacağız. Dikkatlice
bakın::
    
    with open("fihrist.txt", "r+") as f:
        veri = f.read()
        f.seek(0) #Dosyayı başa sarıyoruz
        f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
        
Burada `"r+"` adlı yeni bir kip kullandığımıza dikkat edin. `"+"` işareti bir
dosyayı hem okuma hem de yazma kipinde açmamıza yardımcı olur. İşte bu işareti
`"r"` kipiyle birlikte `"r+"` şeklinde kullanarak dosyamızı hem okuma hem de
yazma kipinde açmayı başardık. Artık ilgili dosya üzerinde hem okuma hem de
yazma işlemlerini aynı anda gerçekleştirebiliriz.

Yukarıdaki kodlarda ilk satırın ardından şöyle bir kod yazdık::
    
    veri = f.read()
    
Böylece dosyanın bütün içeriğini `veri` adlı bir değişkene atamış olduk. Peki bu
işlemi yapmazsak ne olur? Yani mesela şöyle bir kod yazarsak::
    
    with open("fihrist.txt", "r+") as f:
        f.seek(0)
        f.write("Sedat Köz\t: 0322 234 45 45\n")
        
Bu şekilde 'Sedat Köz\\t: 0322 234 45 45\\n' satırı, dosyadaki ilk satırı silip
onun yerine geçecektir. Çünkü `f.seek(0)` ile dosyanın başına dönüp o noktaya,
yani dosyanın ilk satırına bir veri ekledikten sonra Python öbür satırları
otomatik olarak bir alt satıra kaydırmaz. Bunun yerine ilk satırdaki verileri
silip onun yerine, yeni eklenen satırı getirir. Eğer yapmak istediğiniz şey
buysa ne âlâ. Bu kodları kullanabilirsiniz. Ama bizim istediğimiz şey bu değil.
O yüzden `veri = f.read()` satırını kullanarak dosya içeriğini bir değişken
içinde depoluyoruz ve böylece bu verileri kaybetmemiş oluyoruz. 

Bu satırın ardından gelen `f.seek(0)` satırının ne işe yaradığını biliyorsunuz.
Biz yeni veriyi dosyanın en başına eklemek istediğimiz için, doğal olarak bu kod
yardımıyla dosyanın en başına sarıyoruz. Böylece şu kod::
    
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
    
Sedat Köz\\t: 0322 234 45 45\\n' satırını dosyanın en başına ekliyor. Ayrıca
burada, biraz önce `veri` değişkenine atadığımız dosya içeriğini de yeni
eklediğimiz satırın hemen arkasına ilave ettiğimize dikkat edin. Eğer bunu
yapmazsanız, elinizde sadece Sedat Köz'ün iletişim bilgilerini barındıran bir
dosya olacaktır... 

Dosyaların Ortasında Değişiklik Yapmak
======================================

Gördüğünüz gibi, Python'da bir dosyanın en sonuna ve en başına veri eklemek çok
zor değil. Birkaç satır yardımıyla bu işlemleri rahatlıkla yapabiliyoruz. Peki
ya bir dosyanın en başına veya en sonuna değil de rastgele bir yerine ekleme
yapmak istersek ne olacak? 

Hatırlarsanız, Python'da her veri tipinin farklı özellikleri olduğundan, her
veri tipinin farklı açılardan birbirlerine karşı üstünlükleri ya da zayıflıkları
olduğundan söz etmiştik. Dediğimiz gibi, Python'da bazı işler için bazı veri
tiplerini kullanmak daha pratik ve avantajlı olabilir. Örneğin karakter dizileri
değiştirilemeyen veri tipleri olduğu için, mesela bir metinde değişiklik
yapmamız gereken durumlarda, eğer mümkünse listeleri kullanmak daha mantıklı
olabilir. Zira bildiğiniz gibi, karakter dizilerinin aksine listeler
değiştirilebilir veri tipleridir. 

Önceki sayfalarda bir dosyayı okurken üç farklı metottan yararlanabileceğimizi
öğrenmiştik. Bu metotların ``read()``, ``readline()`` ve ``readlines()`` adlı
metotlar olduğunu biliyorsunuz. Bu üç metottan ``read()`` adlı olanı bize çıktı
olarak bir karakter dizisi veriyor. ``readline()`` metodu ise dosyaları satır
satır okuyor ve bize yine bir karakter dizisi veriyor. Sonuncu metot olan
``readlines()`` ise bize bir liste veriyor. ``readline()`` metodundan
farklı olarak ``readlines()`` metodu dosyanın tamamını bir çırpıda okuyor.

Bu üç metot arasından, adı ``readlines()`` olanının, dosyaların herhangi bir
yerinde değişiklik yapmak konusunda bize yardımcı olabileceğini tahmin etmiş
olabilirsiniz. Çünkü dediğimiz gibi ``readlines()`` metodu bize bir dosyanın
içeriğini liste halinde veriyor. Bildiğiniz gibi listeler, üzerinde değişiklik
yapılabilen veri tipleridir. Listelerin bu özelliğinden yararlanarak, dosyaların
herhangi bir yerinde yapmak istediğimiz değişiklikleri rahatlıkla yapabiliriz.
Şimdi dikkatlice bakın şu kodlara::
    
    with open("fihrist.txt", "r+") as f:
        veri = f.readlines()
        veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
        f.seek(0)
        f.writelines(veri)
        
Bu kodları bir dosyaya kaydedip çalıştırdıysanız, istediğimiz işlemi başarıyla
yerine getirdiğini görmüşsünüzdür. Peki ama bu kodlar nasıl çalışıyor? 

Yukarıdaki kodlarda dikkatimizi çeken pek çok özellik var. İlk olarak gözümüze
çarpan şey, dosyayı `"r+"` kipinde açmış olmamız. Bu şekilde dosyayı hem okuma
hem de yazma kipinde açmış oluyoruz. Çünkü dosyada aynı anda hem okuma hem de
yazma işlemleri gerçekleştireceğiz.

Daha sonra şöyle bir satır yazdık::
    
    veri = f.readlines()
    
Bu sayede dosyadaki bütün verileri bir liste olarak almış olduk. Liste adlı veri
tipi ile ne yapabiliyorsak, bu şekilde aldığımız dosya içeriği üzerinde de aynı
şeyleri yapabiliriz. Bizim amacımız bu listenin `2.` sırasına yeni bir satır
eklemek. Bu işlemi listelerin ``insert()`` adlı metodu yardımıyla rahatlıkla
yapabiliriz::
    
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    
Bu şekilde liste üzerinde istediğimiz değişiklikleri yaptıktan sonra tekrar
dosyanın başına dönmemiz lazım. Çünkü ``readlines()`` metoduyla dosyayı bir kez
tam olarak okuduktan sonra imleç o anda dosyanın en sonunda bulunuyor. Eğer
dosyanın en başına dönmeden herhangi bir yazma işlemi gerçekleştirirsek, yazılan
veriler dosyanın sonuna eklenecektir. Bizim yapmamız gereken şey dosyanın en
başına sarıp, değiştirilmiş verilerin dosyaya yazılmasını sağlamak olmalı. Bunu
da şu satır yardımıyla yapıyoruz::
    
    f.seek(0)
    
Son olarak da bütün veirleri dosyaya yazıyoruz::
    
    f.writelines(veri)
    
Şimdiye kadar dosyaya yazma işlemleri için ``write()`` adlı bir metottan
yararlanmıştık. Burada ise ``writelines()`` adlı başka bir metot görüyoruz. Peki
bu iki metot arasındaki fark nedir? 

``write()`` metodu bir dosyaya yalnızca karakter dizilerini yazabilir. Bu metot
yardımıyla dosyaya liste tipinde herhangi bir veri yazamazsınız. Eğer mutlaka
``write()`` metodunu kullanmak isterseniz, liste üzerinde bir ``for`` döngüsü
kurmanız gerekir. O zaman yukarıdaki kodları şöyle yazmanız gerekir::
    
    with open("fihrist.txt", "r+") as f:
        veri = f.readlines()
        veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
        f.seek(0)
        for öğe in veri:
            f.write(öğe)
            
``writelines()`` adlı metot ise bize dosyaya liste tipinde verileri yazma imkanı
verir. Dolayısıyla herhangi bir döngü kurmak zorunda kalmadan listeleri
dosyalarımıza yazabiliriz.

Böylece Python'da dosyaların herhangi bir yerine nasıl yazabileceğimizi öğrenmiş
olduk. Bu arada eğer isteseydik yukarıdaki kodları şöyle de yazabilirdik::
    
    with open("fihrist.txt", "r") as f:
        veri = f.readlines()
        
    with open("fihrist.txt", "w") as f:
        veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
        f.writelines(veri) 
        
Bir önceki kodlardan farklı olarak bu kodlarda dosyamızı önce okuma kipinde açıp
verileri `veri` adlı bir değişken içinde sakladık. Ardından aynı dosyayı bir kez
de yazma kipinde açarak, gerekli değişiklikleri liste üzerinde
gerçekleştirdikten sonra bütün verileri dosyaya yazdık. 

Unutmayın, Python'da herhangi bir işlemi pek çok farklı şekilde
gerçekleştirebilirsiniz. Biz yukarıda olası yöntemlerden bazılarını ele aldık.
Zaten bütün yöntemleri tek tek göstermemiz pek mümkün olmazdı. Siz dosyalara
ilişkin bilgilerinizi ve farklı araçları kullanarak aynı işlemleri çok daha
farklı şekillerde de yapabilirsiniz. Yani karşı karşıya olduğunuz duruma
değerlendirip, yukarıdaki kodlardan uygun olanını veya kendi bulduğunuz bambaşka
bir yöntemi kullanabilirsiniz.

Bu arada, aslında yukarıdaki kodlarda uyguladığımız yöntem biraz güvensiz. Çünkü
aynı dosyayı hem okuyup hem de bu dosyaya yeni veri ekliyoruz. Eğer bu
işlemlerin herhangi bir aşamasında bir hata oluşursa, bütün değişiklikleri
dosyaya işleyemeden dosya içeriğini tümden kaybedebiliriz. Bu tür risklere karşı
en uygun çözüm, okuma ve yazma işlemlerini ayrı dosyalar üzerinde
gerçekleştirmektir. Bunun nasıl yapılacağından biraz sonra söz edeceğiz. Biz
şimdi başka bir konuya değinelim.

Dosyaya Erişme Kipleri
**********************

Dosyalar konusunu anlatırken yukarıda verdiğimiz örneklerden de gördüğünüz gibi,
Python'da dosyalara erişimin türünü ve niteliğini belirleyen bazı kipler var. Bu
kipler dosyaların açılırken hangi yetkilere sahip olacağını veya olmayacağını
belirliyor. Gelin isterseniz bu kipleri tek tek ele alalım. 

=========  =====================================================================
**Kip**         **Açıklaması**
---------  ---------------------------------------------------------------------
``"r"``     Bu öntanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi 
            kullanabilmemiz için, ilgili dosyanın disk üzerinde halihazırda var olması
            gerekir. Eğer bu kipte açılmak istenen dosya mevcut değilse Python bize bir 
            hata mesajı gösterecektir. Dediğimiz gibi, bu öntanımlı kiptir. Dolayısıyla
            dosyayı açarken herhangi bir kip belirtmezsek Python dosyayı bu kipte açmak
            istediğimizi varsayacaktır.
            
``"w"``     Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten
            disk üzerinde varsa, Python hiçbir şey sormadan dosya içeriğini silecektir.
            Eğer belirttiğiniz adda bir dosya diskte yoksa, Python o adda bir dosyayı 
            otomatik olarak oluşturur. 
            
``"a"``     Bu kip dosyayı yazma yetkisiyle açar. Eğer dosya zaten disk üzerinde
            mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir
            dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer
            belirttiğiniz adda bir dosya yoksa Python otomatik olarak o adda bir dosyayı
            sizin için oluşturacaktır.
            
``"x"``     Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya
            zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir
            hata mesajı gösterir. Zaten bu kipin `"w"` kipinden farkı, varolan dosyaları
            silmemesidir. Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip
            yardımıyla o ada sahip bir dosya oluşturabilirsiniz.
            
``"r+"``    Bu kip, bir dosyayı hem yazma hem de okuma yetkisiyle açar. Bu kipi
            kullanabilmeniz için, belirttiğiniz dosyanın disk üzerinde mevcut olması
            gerekir.
            
``"w+"``    Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya
            mevcutsa içerik silinir, eğer dosya mevcut değilse oluşturulur.
            
``"a+"``    Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya zaten
            disk üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte
            açtığınız bir dosyaya eklediğiniz veriler varolan verilere ilave edilir.
            Eğer belirttiğiniz adda bir dosya yoksa Python otomatik olarak o adda bir
            dosyayı sizin için oluşturacaktır.
            
``"x+"``    Bu kip dosyayı hem okuma hem de yazma yetkisiyle açar. Eğer belirttiğiniz
            adda bir dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek
            yerine size bir hata mesajı gösterir. Zaten bu kipin `"w+"` kipinden farkı,
            varolan dosyaları silmemesidir. Eğer belirttiğiniz adda bir dosya diskte
            yoksa, bu kip yardımıyla o ada sahip bir dosya oluşturup bu dosyayı hem
            okuma hem de yazma yetkisiyle açabilirsiniz.
            
``"rb"``    Bu kip, metin dosyaları ile ikili (*binary*) dosyaları ayırt eden
            sistemlerde ikili dosyaları okuma yetkisiyle açmak için kullanılır. `"r"`
            kipi için söylenenler bu kip için de geçerlidir.
            
``"wb"``    Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları yazma yetkisiyle açmak için kullanılır. `"w"` kipi için
            söylenenler bu kip için de geçerlidir.
            
``"ab"``    Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları yazma yetkisiyle açmak için kullanılır. `"a"` kipi için
            söylenenler bu kip için de geçerlidir.
            
``"xb"``    Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları yazma yetkisiyle açmak için kullanılır. `"x"` kipi için
            söylenenler bu kip için de geçerlidir.
            
``"rb+"``   Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. `"r+"`
            kipi için söylenenler bu kip için de geçerlidir.
            
``"wb+"``   Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. `"w+"`
            kipi için söylenenler bu kip için de geçerlidir.
            
``"ab+"``   Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. `"a+"`
            kipi için söylenenler bu kip için de geçerlidir.
            
``"xb+"``   Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili
            dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. `"x+"`
            kipi için söylenenler bu kip için de geçerlidir.
=========  =====================================================================
    
Bütün bu tabloya baktığınızda ilk bakışta sanki bir sürü farklı erişim kipi
olduğunu düşünmüş olabilirsiniz. Ama aslında tabloyu biraz daha incelerseniz,
temel olarak `"r"`, `"w"`, `"a"`, "`x`" ve `"b"` kiplerinin olduğunu, geri kalan
kiplerin ise bunların kombinasyonlarından oluştuğunu göreceksiniz.

Daha önce de söylediğimiz gibi, dosya işlemlerini pek çok farklı yöntemle
gerçekleştirebilirsiniz. Yukarıdaki tabloyu dikkatlice inceleyerek, yapmak
istediğiniz işleme uygun kipi rahatlıkla seçebilirsiniz. 

Bu arada, yukarıdaki tabloda değindiğimiz ikili (*binary*) dosyalardan henüz söz
etmedik. Bir sonraki bölümde bu dosya türünü de ele alacağız.




