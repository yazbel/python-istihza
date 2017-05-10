.. meta:: :description: Bu bölümde Python'daki en önemli fonksiyonlardan biri olan 
           print() fonksiyonundan söz edeceğiz.  
          :keywords: print, fonksiyon, sep, end, file, flush, yıldızlı parametreler, 
           parametre
   
.. highlight:: py3

*******************
print() Fonksiyonu
*******************

Geçen bölümde bir yandan Python'ın etkileşimli kabuğunu yakından tanıyıp bu
vesileyle bazı önemli fonksiyon ve araçları öğrenirken, öbür yandan bu
öğrendiklerimizi kullanarak örnek programlar yazdık. Gördüğünüz gibi, azıcık bir
bilgiyle dahi az çok işe yarar programlar yazmak mümkün olabiliyor. Daha yararlı
programlar yazabilmek için henüz öğrenmemiz gereken pek çok şey var. İşte bu
bölümde, 'daha yararlı programlar yazmamızı' sağlayacak çok önemli bir araçtan
söz edeceğiz. Öneminden dolayı ayrıntılı bir şekilde anlatacağımız bu aracın adı
``print()`` fonksiyonu.

Elbette bu bölümde sadece ``print()`` fonksiyonundan bahsetmeyeceğiz. Bu bölümde
``print()`` fonksiyonunun yanısıra Python'daki bazı önemli temel konuları da ele
alacağız. Mesela bu bölümde Python'daki karakter dizilerine ve sayılara ilişkin
çok önemli bilgiler vereceğiz. Ayrıca ``print()`` fonksiyonu vesilesiyle
Python'daki 'fonksiyon' konusuna da sağlam bir giriş yapmış, bu kavram ile
ilgili ilk bilgilerimizi almış olacağız. Sözün özü, bu bölüm bizim için, deyim
yerindeyse, tam anlamıyla bir dönüm noktası olacak.

O halde isterseniz lafı daha fazla uzatmadan işe ``print()`` fonksiyonunun ne
olduğu ve ne işe yaradığını anlatarak başlayalım.

Nedir, Ne İşe Yarar?
*********************

Şimdiye kadar etkileşimli kabukta gerek karakter dizilerini gerekse sayıları
doğrudan ekrana yazdık. Yani şöyle bir şey yaptık::
    
    >>> "Python programlama dili"
    
    'Python programlama dili'
    
    >>> 6567
    
    6567

Etkileşimli kabuk da, ekrana yazdığımız bu karakter dizisi ve sayıyı doğrudan
bize çıktı olarak verdi. Ancak ilerde Python kodlarımızı bir dosyaya kaydedip
çalıştırdığımızda da göreceğiniz gibi, Python'ın ekrana çıktı verebilmesi için
yukarıdaki kullanım yeterli değildir. Yani yukarıdaki kullanım yalnızca
etkileşimli kabukta çalışır. Bu kodları bir dosyaya kaydedip çalıştırmak
istediğimizde hiçbir çıktı alamayız. Python'da yazdığımız şeylerin ekrana çıktı
olarak verilebilmesi için ``print()`` adlı özel bir fonksiyondan yararlanmamız
gerekir.

O halde gelin bu ``print()`` fonksiyonunun ne işe yaradığını ve nasıl
kullanıldığını anlamaya çalışalım:

``print()`` de tıpkı daha önce gördüğümüz ``type()``, ``len()`` ve ``pow()``
gibi bir fonksiyondur. Fonksiyonları ilerde daha ayrıntılı bir şekilde
inceleyeceğimizi söylemiştik hatırlarsanız. O yüzden fonksiyon kelimesine
takılarak, burada anlattığımız şeylerin kafanızı karıştırmasına, moralinizi
bozmasına izin vermeyin.

``print()`` fonksiyonunun görevi ekrana çıktı vermemizi sağlamaktır. Hemen
bununla ilgili bir örnek verelim::
    
    >>> print("Python programlama dili")
    
    Python programlama dili

Bildiğiniz gibi burada gördüğümüz `"Python programlama dili"` bir karakter
dizisidir. İşte ``print()`` fonksiyonunun görevi bu karakter dizisini ekrana
çıktı olarak vermektir. Peki bu karakter dizisini ``print()`` fonksiyonu olmadan
yazdığımızda da ekrana çıktı vermiş olmuyor muyuz? Aslında olmuyoruz. Dediğimiz
gibi, ilerde programlarımızı dosyalara kaydedip çalıştırdığımızda, başında
``print()`` olmayan ifadelerin çıktıda görünmediğine şahit olacaksınız.

Daha önce de dediğimiz gibi, etkileşimli kabuk bir test ortamı olması açısından
rahat bir ortamdır. Bu sebeple bu ortamda ekrana çıktı verebilmek için
``print()`` fonksiyonunu kullanmak zorunda değilsiniz. Yani başında ``print()``
olsa da olmasa da etkileşimli kabuk ekrana yazdırmak istediğiniz şeyi yazdırır.
Ama iyi bir alışkanlık olması açısından, ekrana herhangi bir şey
yazdıracağınızda ben size ``print()`` fonksiyonunu kullanmanızı tavsiye ederim.

``print()`` son derece güçlü bir fonksiyondur. Gelin isterseniz bu güçlü ve
faydalı fonksiyonu derin derin incelemeye koyulalım.

Nasıl Kullanılır?
*****************

Yukarıda verdiğimiz örnekte ilk gözümüze çarpan şey, karakter dizisini
``print()`` fonksiyonunun parantezleri içine yazmış olmamızdır. Biz bir
fonksiyonun parantezleri içinde belirtilen öğelere 'parametre' dendiğini geçen
bölümde öğrenmiştik. Tıpkı öğrendiğimiz öteki fonksiyonlar gibi, ``print()``
fonksiyonu da birtakım parametreler alır.

Bu arada ``print()`` fonksiyonunun parantezini açıp parametreyi yazdıktan sonra,
parantezi kapatmayı unutmuyoruz. Python programlama diline yeni başlayanların,
hatta bazen deneyimli programcıların bile en sık yaptığı hatalardan biri
açtıkları parantezi kapatmayı unutmalarıdır.

Elbette, eğer istersek burada doğrudan `"Python programlama dili"` adlı karakter
dizisini kullanmak yerine, önce bu karakter dizisini bir değişkene atayıp, sonra
da ``print()`` fonksiyonunun parantezleri içinde bu değişkeni kullanabiliriz.
Yani::

    >>> dil = "Python programlama dili"
    >>> print(dil)
    
    Python programlama dili

Bu arada, hem şimdi verdiğimiz, hem de daha önce yazdığımız örneklerde bir şey
dikkatinizi çekmiş olmalı. Şimdiye kadar verdiğimiz örneklerde karakter
dizilerini hep çift tırnakla gösterdik. Ama aslında tek seçeneğimiz çift tırnak
değildir. Python bize üç farklı tırnak seçeneği sunar:

#. Tek tırnak (' ')
#. Çift tırnak (" ")
#. Üç tırnak (""" """)

Dolayısıyla yukarıdaki örneği üç farklı şekilde yazabiliriz::

    >>> print('Python programlama dili')
    
    Python programlama dili
    
    >>> print("Python programlama dili")
    
    Python programlama dili
    
    >>> print("""Python programlama dili""")
    
    Python programlama dili

Gördüğünüz gibi çıktılar arasında hiçbir fark yok. 

Peki çıktılarda hiçbir fark yoksa neden üç farklı tırnak çeşidi var?

İsterseniz bu soruyu bir örnek üzerinden açıklamaya çalışalım. Diyelim ki ekrana
şöyle bir çıktı vermek istiyoruz::
    
    Python programlama dilinin adı "piton" yılanından gelmez

Eğer bu cümleyi çift tırnaklar içinde gösterirsek programımız hata verecektir::

    >>> print("Python programlama dilinin adı "piton" yılanından gelmez")

    File "<stdin>", line 1
      print("Python programlama dilinin adı "piton" yılanından gelmez")
                                                  ^
    SyntaxError: invalid syntax

Bunun sebebi, cümle içinde geçen 'piton' kelimesinin de çift tırnaklar içinde
gösterilmiş olmasıdır. Cümlenin, yani karakter dizisinin kendisi de çift tırnak
içinde gösterildiği için Python, karakter dizisini başlatan ve bitiren
tırnakların hangisi olduğunu ayırt edemiyor. Yukarıdaki cümleyi en kolay şu
şekilde ekrana yazdırabiliriz::
    
    >>> print('Python programlama dilinin adı "piton" yılanından gelmez')
    
    Python programlama dilinin adı "piton" yılanından gelmez

Burada karakter dizisini tek tırnak içine aldık. Karakter dizisi içinde geçen
'piton' kelimesi çift tırnak içinde olduğu için, karakter dizisini başlatıp
bitiren tırnaklarla 'piton' kelimesindeki tırnakların birbirine karışması gibi
bir durum söz konusu değildir.

Bir de şöyle bir örnek verelim: Diyelim ki aşağıdaki gibi bir çıktı elde etmek
istiyoruz::

    İstanbul'un 5 günlük hava durumu tahmini

Eğer bu karakter dizisini tek tırnak işaretleri içinde belirtirseniz Python size
bir hata mesajı gösterecektir::
    
    >>> print('İstanbul'un 5 günlük hava durumu tahmini')
    
    File "<stdin>", line 1
      print('İstanbul'un 5 günlük hava durumu tahmini')
                        ^
    SyntaxError: invalid syntax

Bu hatanın sebebi 'İstanbul'un' kelimesi içinde geçen kesme işaretidir. Tıpkı
bir önceki örnekte olduğu gibi, Python karakter dizisini başlatan ve bitiren
tırnakların hangisi olduğunu kestiremiyor. Python, karakter dizisinin en
başındaki tek tırnak işaretinin ardından 'İstanbul'un' kelimesi içindeki kesme
işaretini görünce karakter dizisinin burada sona erdiğini zannediyor. Ancak
karakter dizisini soldan sağa doğru okumaya devam edince bir yerlerde bir
terslik olduğunu düşünüyor ve bize bir hata mesajı göstermekten başka çaresi
kalmıyor. Yukarıdaki karakter dizisini en kolay şöyle tanımlayabiliriz::
    
    >>> print("İstanbul'un 5 günlük hava durumu tahmini")
    
    İstanbul'un 5 günlük hava durumu tahmini

Burada da, karakter dizisi içinde geçen kesme işaretine takılmamak için karakter
dizimizi çift tırnak işaretleri içine alıyoruz.

Yukarıdaki karakter dizilerini düzgün bir şekilde çıktı verebilmek için üç
tırnak işaretlerinden de yararlanabiliriz::
    
    >>> print("""Python programlama dilinin adı "piton" yılanından gelmez""")
    
    Python programlama dilinin adı "piton" yılanından gelmez
    
    >>> print("""İstanbul'un 5 günlük hava durumu tahmini""")
    
    İstanbul'un 5 günlük hava durumu tahmini

Bütün bu örneklerden sonra kafanızda şöyle bir düşünce uyanmış olabilir:

    Görünüşe göre üç tırnak işaretiyle her türlü karakter dizisini hatasız bir
    şekilde ekrana çıktı olarak verebiliyoruz. O zaman ben en iyisi bütün
    karakter dizileri için üç tırnak işaretini kullanayım!
    
Elbette, eğer isterseniz **pek çok karakter dizisi için** üç tırnak işaretini
kullanabilirsiniz. Ancak Python'da karakter dizileri tanımlanırken genellikle
tek tırnak veya çift tırnak işaretleri kullanılır. Üç tırnak işaretlerinin asıl
kullanım yeri ise farklıdır. Peki nedir bu üç tırnak işaretlerinin asıl kullanım
yeri?

Üç tırnak işaretlerini her türlü karakter dizisiyle birlikte kullanabiliyor
olsak da, bu tırnak tipi çoğunlukla sadece birden fazla satıra yayılmış karakter
dizilerini tanımlamada kullanılır. Örneğin şöyle bir ekran çıktısı vermek
istediğinizi düşünün::
    
    [H]=========HARMAN========[-][o][x]
    |                                 |
    |     Programa Hoşgeldiniz!       |
    |           Sürüm 0.8             |
    |    Devam etmek için herhangi    |
    |       bir düğmeye basın.        |
    |                                 |
    |=================================|

Böyle bir çıktı verebilmek için eğer tek veya çift tırnak kullanmaya
kalkışırsanız epey eziyet çekersiniz. Bu tür bir çıktı vermenin en kolay yolu üç
tırnakları kullanmaktır::
    
    >>> print("""
    ... [H]=========HARMAN========[-][o][x]
    ... |                                 |
    ... |     Programa Hoşgeldiniz!       |
    ... |           Sürüm 0.8             |
    ... |    Devam etmek için herhangi    |
    ... |       bir düğmeye basın.        |
    ... |                                 |
    ... |=================================|
    ... """)
    
Burada bazı şeyler dikkatinizi çekmiş olmalı. Gördüğünüz gibi, üç tırnaklı yapı
öteki tırnak tiplerine göre biraz farklı davranıyor. Şimdi şu örneğe bakın::
    
    >>> print("""Game Over!
    ...

Buraya çok dikkatli bakın. Karakter dizisine üç tırnakla başladıktan sonra,
kapanış tırnağını koymadan `Enter` tuşuna bastığımızda `>>>` işareti `...`
işaretine dönüştü. Python bu şekilde bize, 'yazmaya devam et!' demiş oluyor. Biz
de buna uyarak yazmaya devam edelim::
    
    >>> print("""Game Over!
    ... Insert Coin!""")
    
    Game Over!
    Insert Coin!

Kapanış tırnağı koyulmadan `Enter` tuşuna basıldığında `>>>` işaretinin `...`
işaretine dönüşmesi üç tırnağa özgü bir durumdur. Eğer aynı şeyi tek veya çift
tırnaklarla yapmaya çalışırsanız programınız hata verir::
    
    >>> print("Game Over!
    
    File "<stdin>", line 1
      print("Game Over!
                      ^
    SyntaxError: EOL while scanning string literal

...veya::

    >>> print('Game Over!

    File "<stdin>", line 1
      print("Game Over!
                      ^
    SyntaxError: EOL while scanning string literal  

Üç tırnak işaretlerinin tırnak kapanmadan `Enter` tuşuna basıldığında hata
vermeme özelliği sayesinde, bu tırnak tipi özellikle birden fazla satıra
yayılmış karakter dizilerinin gösterilmesi için birebirdir.

Gelin isterseniz üç tırnak kullanımına ilişkin bir örnek daha verelim::

    >>> print("""Python programlama dili Guido Van Rossum 
    ... adlı Hollandalı bir programcı tarafından 90’lı 
    ... yılların başında geliştirilmeye başlanmıştır. Çoğu
    ... insan, isminin "Python" olmasına bakarak, bu programlama 
    ... dilinin, adını piton yılanından aldığını düşünür. 
    ... Ancak zannedildiğinin aksine bu programlama dilinin 
    ... adı piton yılanından gelmez.""")
    
    Python programlama dili Guido Van Rossum
    adlı Hollandalı bir programcı tarafından 90'lı
    yılların başında geliştirilmeye başlanmıştır. Çoğu
    insan, isminin "Python" olmasına bakarak, bu programlama
    dilinin, adını piton yılanından aldığını düşünür.
    Ancak zannedildiğinin aksine bu programlama dilinin
    dı piton yılanından gelmez.

Elbette eğer istersek bu metni önce bir değişkene atamayı da tercih edebiliriz::
    
    >>> python_hakkinda = """Python programlama dili Guido Van Rossum 
    ... adlı Hollandalı bir programcı tarafından 90’lı 
    ... yılların başında geliştirilmeye başlanmıştır. Çoğu
    ... insan, isminin "Python" olmasına bakarak, bu programlama 
    ... dilinin, adını piton yılanından aldığını düşünür. 
    ... Ancak zannedildiğinin aksine bu programlama dilinin 
    ... adı piton yılanından gelmez."""
    >>> print(python_hakkinda)
    
    Python programlama dili Guido Van Rossum
    adlı Hollandalı bir programcı tarafından 90'lı
    yılların başında geliştirilmeye başlanmıştır. Çoğu
    insan, isminin "Python" olmasına bakarak, bu programlama
    dilinin, adını piton yılanından aldığını düşünür.
    Ancak zannedildiğinin aksine bu programlama dilinin
    dı piton yılanından gelmez.

Siz yukarıdaki çıktıyı tek veya çift tırnak kullanarak nasıl ekrana
yazdırabileceğinizi düşünedurun, biz önemli bir konuya geçiş yapalım!

Bir Fonksiyon Olarak print()
*****************************

``print()`` ifadesinin bir fonksiyon olduğunu söylemiştik hatırlarsanız.
Dediğimiz gibi, fonksiyonlarla ilgili ayrıntılı açıklamaları ilerleyen derslerde
vereceğiz. Ancak şimdi dilerseniz bundan sonra anlatacaklarımızı daha iyi
kavrayabilmemiz için, fonksiyonlar hakkında bilmemiz gereken bazı temel şeyleri
öğrenmeye çalışalım.

Gördüğünüz gibi, ``print()`` fonksiyonunu şöyle kullanıyoruz::

    >>> print("Aramak istediğiniz kelimeyi yazın: ")

Burada ``print()`` bir fonksiyon, `"Aramak istediğiniz kelimeyi yazın:"` adlı
karakter dizisi ise bu fonksiyonun parametresidir. Daha önce ``len()`` adlı
başka bir fonksiyon daha öğrenmiştik hatırlarsanız. Onu da şöyle kullanıyorduk::
    
    >>> len("elma")

Burada da ``len()`` bir fonksiyon, `"elma"` adlı karakter dizisi ise bu
fonksiyonun parametresidir. Aslında biçim olarak ``print()`` ve ``len()``
fonksiyonlarının birbirinden hiçbir farkı olmadığını görüyorsunuz.

Daha önce söylediğimiz ve bu örneklerden de anladığımız gibi, bir fonksiyonun
parantezleri içinde belirtilen öğelere parametre adı veriliyor. Mesela aşağıdaki
örnekte ``print()`` fonksiyonunu tek bir parametre ile kullanıyoruz::
    
    >>> print('En az 8 haneli bir parola belirleyin.')

``print()`` fonksiyonu, tıpkı ``pow()`` fonksiyonu gibi, birden fazla parametre alabilir::

    >>> print('Fırat', 'Özgül')
      
    Fırat Özgül

Bu örnekte bizim için çıkarılacak çok dersler var. Bir defa burada ``print()``
fonksiyonunu iki farklı parametre ile birlikte kullandık. Bunlardan ilki `Fırat`
adlı bir karakter dizisi, ikincisi ise `Özgül` adlı başka bir karakter dizisi.
Python'ın bu iki karakter dizisini nasıl birleştirdiğine dikkat edin.
``print()`` fonksiyonu bu iki karakter dizisini çıktı olarak verirken aralarına
da birer boşluk yerleştirdi. Ayrıca, geçen derste de vurguladığımız gibi,
parametrelerin birbirinden virgül ile ayrıldığını da gözden kaçırmıyoruz.

Gelin bununla ilgili bir iki örnek daha verelim elimizin alışması için::

    >>> print("Python", "Programlama", "Dili")
    
    Python Programlama Dili
    
    >>> print('Fırat', 'Özgül', 'Adana', 1980)
    
    Fırat Özgül Adana 1980

Bu arada dikkatinizi önemli bir noktaya çekmek istiyorum. Yukarıdaki örneklerde
bazen tek tırnak, bazen de çift tırnak kullandık. Daha önce de söylediğimiz
gibi, hangi tırnak tipini kullandığımız önemli değildir. Python hangi tırnak
tipini kullandığımızdan ziyade, tırnak kullanımında tutarlı olup olmadığımızla
ilgilenir. Yani Python için önemli olan, karakter dizisini hangi tırnakla
başlatmışsak, o tırnakla bitirmemizdir. Yani şu tip kullanımlar geçerli
değildir::
    
    >>> print("karakter dizisi')
    
    >>> print('karakter dizisi")

Karakter dizisini tanımlamaya başlarken kullandığımız tırnak tipi ile karakter
dizisini tanımlamayı bitirirken kullandığımız tırnak tipi birbirinden farklı
olduğu için bu iki kullanım da hata verecektir.

print() Fonksiyonunun Parametreleri
************************************

Şimdiye kadar verdiğimiz örneklerde belki çok da belli olmuyordur, ama aslında
``print()`` fonksiyonu son derece güçlü bir araçtır. İşte şimdi biz bu
fonksiyonun gücünü gözler önüne seren özelliklerini incelemeye başlayacağız. Bu
bölümü dikkatle takip etmeniz, ilerde yapacağımız çalışmaları daha rahat
anlayabilmeniz açısından büyük önem taşır.

sep
========

``print()`` fonksiyonu ile ilgili olarak yukarıda verdiğimiz örnekleri
incelediğimizde, bu fonksiyonun kendine özgü bir davranış şekli olduğunu
görüyoruz. Mesela bir önceki bölümde verdiğimiz şu örneğe bakalım::
    
    >>> print('Fırat', 'Özgül')
          
    Fırat Özgül

Burada ``print()`` fonksiyonunu iki farklı parametre ile birlikte kullandık. Bu
fonksiyon, kendisine verdiğimiz bu parametreleri belli bir düzene göre
birbiriyle birleştirdi. Bu düzen gereğince ``print()``, kendisine verilen
parametreleri birleştirirken, parametreler arasına bir boşluk yerleştiriyor.
Bunu daha net görmek için şöyle bir örnek daha verelim::
    
    >>> print("Python", "PHP", "C++", "C", "Erlang")
    
    Python PHP C++ C Erlang

Gördüğünüz gibi, ``print()`` fonksiyonu gerçekten de, kendisine verilen
parametreleri birleştirirken, parametrelerin her biri arasına bir boşluk
yerleştiriyor. Halbuki bu boşluğu biz talep etmedik! Python bize bu boşluğu
eşantiyon olarak verdi. Çoğu durumda istediğimiz şey bu olacaktır, ama bazı
durumlarda bu boşluğu istemeyebiliriz. Örneğin::
    
    >>> print("http://", "www.", "istihza.", "com")
    
    http:// www. istihza. com

Ya da boşluk karakteri yerine daha farklı bir karakter kullanmak istiyor da
olabiliriz. Peki böyle bir durumda ne yapmamız gerekir?

İşte bu noktada bazı özel araçlardan yararlanarak ``print()`` fonksiyonunun
öntanımlı davranış kalıpları üzerinde değişiklikler yapabiliriz.

Peki nedir ``print()`` fonksiyonunu özelleştirmemizi sağlayacak bu araçlar?

Hatırlarsanız, Python'da fonksiyonların parantezleri içindeki değerlere
parametre adı verildiğini söylemiştik. Mesela ``print()`` fonksiyonunu bir ya da
daha fazla parametre ile birlikte kullanabileceğimizi biliyoruz::
    
    >>> print("Mehmet", "Öz", "İstanbul", "Çamlıca", 156, "/", 45)

    Mehmet Öz İstanbul Çamlıca 156 / 45

``print()`` fonksiyonu içinde istediğimiz sayıda karakter dizisi ve/veya sayı
değerli parametre kullanabiliriz.

Fonksiyonların bir de daha özel görünümlü parametreleri vardır. Mesela
``print()`` fonksiyonunun `sep` adlı özel bir parametresi bulunur. Bu parametre
``print()`` fonksiyonunda görünmese bile her zaman oradadır. Yani diyelim ki
şöyle bir kod yazdık::
    
    >>> print("http://", "www.", "google.", "com")

Burada herhangi bir `sep` parametresi görmüyoruz. Ancak Python yukarıdaki kodu
aslında şöyle algılar::
    
    >>> print("http://", "www.", "google.", "com", sep=" ")

*sep* ifadesi, İngilizcede *separator* (ayırıcı, ayraç) kelimesinin
kısaltmasıdır. Dolayısıyla ``print()`` fonksiyonundaki bu `sep` parametresi,
ekrana basılacak öğeler arasına hangi karakterin yerleştirileceğini gösterir. Bu
parametrenin öntanımlı değeri bir adet boşluk karakteridir (`" "`). Yani siz bu
özel parametrenin değerini başka bir şeyle değiştirmezseniz, Python bu
parametrenin değerini bir adet boşluk karakteri olarak alacak ve ekrana
basılacak öğeleri birbirinden birer boşlukla ayıracaktır. Ancak eğer biz
istersek bu `sep` parametresinin değerini değiştirebiliriz. Böylece Python,
karakter dizilerini birleştirirken araya boşluk değil, bizim istediğimiz başka
bir karakteri yerleştirebilir. Gelin şimdi bu parametrenin değerini nasıl
değiştireceğimizi görelim::
    
    >>> print("http://", "www.", "istihza.", "com", sep="")
    
    http://www.istihza.com

Gördüğünüz gibi, karakter dizilerini başarıyla birleştirip, geçerli bir internet
adresi elde ettik.

Burada yaptığımız şey aslında çok basit. Sadece `sep` parametresinin 'bir adet
boşluk karakteri' olan öntanımlı değerini silip, yerine 'boş bir karakter
dizisi' değerini yazdık. Bu iki kavramın birbirinden farklı olduğunu
söylediğimizi hatırlıyorsunuz, değil mi?

Gelin bir örnek daha yapalım::

    >>> print("T", "C", sep=".")
    
    T.C

Burada Python'a şöyle bir emir vermiş olduk:

    `"T"` ve `"C"` karakter dizilerini birbiriyle birleştir! Bunu yaparken de bu
    karakter dizilerinin arasına nokta işareti yerleştir!
    
`sep` parametresinin öteki parametrelerden farkı her zaman ismiyle birlikte
kullanılmasıdır. Zaten teknik olarak da bu tür parametrelere 'isimli
parametreler' adı verilir. Örneğin::
    
    >>> print("Adana", "Mersin", sep="-")
    
    Adana-Mersin

Eğer burada `sep` parametresinin ismini belirtmeden, doğrudan parametrenin
değerini yazarsak, bu değerin öteki parametrelerden hiçbir farkı kalmayacaktır::
    
    >>> print("Adana", "Mersin", "-")
    
    Adana Mersin -
    
Gelin isterseniz bu parametreyle ilgili bir örnek daha yapalım:

'Bir mumdur iki mumdur...' diye başlayan türküyü biliyorsunuzdur. Şimdi bu
türküyü Python'la nasıl yazabileceğimizi görelim!

::

    >>> print("bir", "iki", "üç", "dört", "on dört", sep="mumdur")
    
    birmumdurikimumdurüçmumdurdörtmumduron dört

Burada bir terslik olduğu açık! Karakter dizileri birbirlerine sıkışık düzende
birleştirildi. Bunların arasında birer boşluk olsa tabii daha iyi olurdu. Ancak
biliyorsunuz `sep` parametresinin öntanımlı değerini silip, yerine `"mumdur"`
değerini yerleştirdiğimiz için, Python'ın otomatik olarak yerleştirdiği boşluk
karakteri kayboldu. Ama eğer istersek o boşluk karakterlerini kendimiz de
ayarlayabiliriz::
    
    >>> print("bir", "iki", "üç", "dört", "on dört", sep=" mumdur ")
    
    bir mumdur iki mumdur üç mumdur dört mumdur on dört

Gördüğünüz gibi, `sep` parametresine verdiğimiz `"mumdur"` değerinin sağında ve
solunda birer boşluk bırakarak sorunumuzu çözebildik. Bu sorunu çözmenin başka
bir yolu daha var. Hatırlarsanız etkileşimli kabukta ilk örneklerimizi verirken
karakter dizilerini birleştirmek için `+` işaretinden de yararlanabileceğimizi
söylemiştik. Dolayısıyla `sep` parametresini şöyle de yazabiliriz::
    
    >>> print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")

Burada da, `"mumdur"` adlı karakter dizisinin başında ve sonunda birer boşluk
bırakmak yerine, gerekli boşlukları `+` işareti yardımıyla bu karakter dizisine
birleştirdik. Hatta istersek `+` işlecini kullanmak zorunda olmadığımızı dahi
biliyorsunuz::
    
    >>> print("bir", "iki", "üç", "dört", "on dört", sep=" " "mumdur" " ")

Ama gördüğünüz gibi bir problemimiz daha var. Türkünün sözleri şu şekilde
olmalıydı:

    bir mumdur iki mumdur üç mumdur dört mumdur on dört mumdur

Ama sondaki 'mumdur' kelimesi yukarıdaki çıktıda yok. Normal olan da bu aslında.
`sep` parametresi, karakter dizilerinin **arasına** bir değer yerleştirir.
Karakter dizilerinin son tarafıyla ilgilenmez. Bu iş için ``print()`` fonksiyonu
başka bir parametreye sahiptir.

Bu arada, yukarıdaki örneklerde hep karakter dizilerini kullanmış olmamız sizi
yanıltmasın. `sep` parametresi yalnızca karakter dizilerinin değil sayıların
arasına da istediğiniz bir değerin yerleştirilmesini sağlayabilir. Mesela::
    
    >>> print(1, 2, 3, 4, 5, sep="-")
    
    1-2-3-4-5

Ancak `sep` parametresine değer olarak yalnızca karakter dizilerini ve `None`
adlı özel bir sözcüğü verebiliriz. (`None` sözcüğünden ileride söz edeceğiz)::
    
    >>> print(1, 2, 3, 4, 5, sep=0)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: sep must be None or a string, not int

Gördüğünüz gibi, `sep` parametresine bir sayı olan `0` değerini veremiyoruz.

Peki bu parametreye `None` değeri verirsek ne olur? Bu parametreye `None` değeri
verildiğinde, ``print()`` fonksiyonu bu parametre için öntanımlı değeri (yani
bir adet boşluk) kullanır::
    
    >>> print('a', 'b', sep=None)
    
    a b
    
Eğer amacınız parametreleri birbirine bitiştirmekse, yani `sep` parametresinin
öntanımlı değeri olan boşluk karakterini ortadan kaldırmaksa, `sep`
parametresine boş bir karakter dizisi vermeniz gerektiğini biliyorsunuz::
    
    >>> print('a', 'b', sep='')
    
    ab
    
``print()`` fonksiyonunun `sep` parametresini bütün ayrıntılarıyla
incelediğimize göre, bu fonksiyonun bir başka özel parametresinden söz
edebiliriz.

end
=======

Bir önceki bölümde şöyle bir laf etmiştik:

    ``print()`` fonksiyonun `sep` adlı özel bir parametresi bulunur. Bu
    parametre ``print()`` fonksiyonunda görünmese bile her zaman oradadır.
    
Aynı bu şekilde, ``print()`` fonksiyonunun `end` adlı özel bir parametresi daha
bulunur. Tıpkı `sep` parametresi gibi, `end` parametresi de ``print()``
fonksiyonunda görünmese bile her zaman oradadır.

Bildiğiniz gibi, `sep` parametresi ``print()`` fonksiyonuna verilen parametreler
birleştirilirken araya hangi karakterin gireceğini belirliyordu. `end`
parametresi ise bu parametrelerin sonuna neyin geleceğini belirler.

``print()`` fonksiyonu öntanımlı olarak, parametrelerin sonuna 'satır başı
karakteri' ekler. Peki bu satır başı karakteri (veya 'yeni satır karakteri')
denen şey de ne oluyor?

Dilerseniz bunu bir örnek üzerinde görelim. 

Şöyle bir kodumuz olsun::

    >>> print("Pardus ve Ubuntu birer GNU/Linux dağıtımıdır.")

Bu kodu yazıp `Enter` tuşuna bastığımız anda ``print()`` fonksiyonu iki farklı
işlem gerçekleştirir:

#. Öncelikle karakter dizisini ekrana yazdırır.
#. Ardından bir alt satıra geçip bize `>>>` işaretini gösterir. 

İşte bu ikinci işlem, karakter dizisinin sonunda bir adet satır başı karakteri
olmasından, daha doğrusu ``print()`` fonksiyonunun, satır başı karakterini
karakter dizisinin sonuna eklemesinden kaynaklanır. Bu açıklama biraz kafa
karıştırıcı gelmiş olabilir. O halde biraz daha açıklayalım. Şu örneğe bakın::
    
    >>> print("Pardus\nUbuntu")
    
    Pardus
    Ubuntu

Burada `"Pardus"` ve `"Ubuntu"` karakter dizilerinin tam ortasında çok özel bir
karakter dizisi daha görüyorsunuz. Bu karakter dizisi şudur: `\\n`. İşte bu özel
karakter dizisine satır başı karakteri (*newline*) adı verilir. Bu karakterin
görevi, karakter dizisini, bulunduğu noktadan bölüp, karakter dizisinin geri
kalanını bir alt satıra geçirmektir. Zaten çıktıda da bu işlevi yerine
getirdiğini görüyorsunuz. Karakter dizisi `"Pardus"` kısmından sonra ikiye
bölünüyor ve bu karakter dizisinin geri kalan kısmı olan `"Ubuntu"` karakter
dizisi bir alt satıra yazdırılıyor. Bunu daha iyi anlamak için bir örnek daha
verelim::
    
    >>> print("birinci satır\nikinci satır\nüçüncü satır")
    
    birinci satır
    ikinci satır
    üçüncü satır

Peki size bir soru sorayım: Acaba yukarıdaki kodları daha verimli bir şekilde
nasıl yazabiliriz?

Evet, doğru tahmin ettiniz... Tabii ki `sep` parametresini kullanarak::
    
    >>> print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")
    
    birinci satır
    ikinci satır
    üçüncü satır

Burada yaptığımız şey çok basit. `sep` parametresinin değerini `\\n`, yani yeni
satır karakteri (veya satır başı karakteri) olarak değiştirdik. Böylece karakter
dizileri arasına birer `\\n` karakteri yerleştirerek her bir karakter dizisinin
farklı satıra yazdırılmasını sağladık.

İşte `end` parametresinin öntanımlı değeri de bu `\\n` karakteridir ve bu
parametre ``print()`` fonksiyonunda görünmese bile her zaman oradadır.

Yani diyelim ki şöyle bir kod yazdık::

    >>> print("Bugün günlerden Salı")

Burada herhangi bir `end` parametresi görmüyoruz. Ancak Python yukarıdaki kodu
aslında şöyle algılar::
    
    >>> print("Bugün günlerden Salı", end="\n")

Biraz önce de dediğimiz gibi, bu kodu yazıp `Enter` tuşuna bastığımız anda
``print()`` fonksiyonu iki farklı işlem gerçekleştirir:

#. Öncelikle karakter dizisini ekrana yazdırır.
#. Ardından bir alt satıra geçip bize `>>>` işaretini gösterir. 

Bunun ne demek olduğunu anlamak için `end` parametresinin değerini değiştirmemiz
yeterli olacaktır::
    
    >>> print("Bugün günlerden Salı", end=".")
    
    Bugün günlerden Salı.>>>

Gördüğünüz gibi, `end` parametresinin öntanımlı değeri olan `\\n` karakterini
silip yerine `.` (nokta) işareti koyduğumuz için, komutu yazıp `Enter` tuşuna
bastığımızda ``print()`` fonksiyonu satır başına geçmedi. Yeni satıra geçebilmek
için `Enter` tuşuna kendimiz basmalıyız. Elbette, eğer yukarıdaki kodları şöyle
yazarsanız, ``print()`` fonksiyonu hem karakter dizisinin sonuna nokta
ekleyecek, hem de satır başına geçecektir::
    
    >>> print("Bugün günlerden Salı", end=".\n")
    
    Bugün günlerden Salı.

Şimdi bu öğrendiklerimizi türkümüze uygulayalım::

    >>> print("bir", "iki", "üç", "dört", "on dört",
    ... sep=" mumdur ", end=" mumdur\n")
    
.. note:: Burada kodlarımızın sağa doğru çirkin bir şekilde uzamasını engellemek
 için `"on dört"` karakter dizisini yazıp virgülü koyduktan sonra `Enter` tuşuna
 basarak bir alt satıra geçtik. Bir alt satıra geçtiğimizde `>>>` işaretinin
 `...` işaretine dönüştüğüne dikkat edin. Python'da doğru kod yazmak kadar,
 yazdığımız kodların düzgün görünmesi de önemlidir. O yüzden yazdığımız her bir
 kod satırının mümkün olduğunca 79 karakteri geçmemesini sağlamalıyız. Eğer
 yazdığınız bir satır 79 karakteri aşıyorsa, aşan kısmı yukarıda gösterdiğimiz
 şekilde alt satıra alabilirsiniz.

`end` parametresi de, tıpkı `sep` parametresi gibi, her zaman ismiyle birlikte
kullanılması gereken bir parametredir. Yani eğer `end` parametresinin ismini
belirtmeden sadece değerini kullanmaya çalışırsak Python ne yapmaya
çalıştığımızı anlayamaz.

Yine tıpkı `sep` parametresi gibi, `end` parametresinin değeri de sadece bir
karakter dizisi veya `None` olabilir::
    
    >>> print(1, 2, 3, 4, 5, end=0)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: end must be None or a string, not int

Gördüğünüz gibi, `end` parametresine bir sayı olan `0` değerini veremiyoruz.

Eğer bu parametreye `None` değeri verirsek, tıpkı `sep` parametresinde olduğu
gibi, ``print()`` fonksiyonu bu parametre için öntanımlı değeri (yani satır başı
karakteri) kullanır::
    
    >>> print('a', 'b', end=None)
    
    a b
    
Eğer amacınız yeni satıra geçilmesini engellemekse, yani `end` parametresinin
öntanımlı değeri olan `\\n` kaçış dizisini ortadan kaldırmaksa, `end`
parametresine boş bir karakter dizisi vermelisiniz::
    
    >>> print('a', 'b', end='')
    
    a b>>>
    
file
=======

.. note:: Burada henüz öğrenmediğimiz bazı şeyler göreceksiniz. Hiç endişe
 etmeyin. Bunları ilerde bütün ayrıntılarıyla öğreneceğiz. Şimdilik konu hakkında
 biraz olsun fikir sahibi olmanızı sağlayabilirsek kendimizi başarılı sayacağız.

``print()`` fonksiyonunun `sep` ve `end` dışında üçüncü bir özel parametresi
daha bulunur. Bu parametrenin adı `file`'dır. Görevi ise, ``print()``
fonksiyonuna verilen karakter dizisi ve/veya sayıların, yani parametrelerin
nereye yazılacağını belirtmektir.

Bu parametrenin öntanımlı değeri `sys.stdout`'tur. Peki bu ne anlama geliyor?
`sys.stdout`, 'standart çıktı konumu' anlamına gelir. Peki 'standart çıktı
konumu' ne demek?

Standart çıktı konumu; bir programın, ürettiği çıktıları verdiği yerdir. Aslında
bu kavramın ne demek olduğu adından da anlaşılıyor:

    standart çıktı konumu = çıktıların standart olarak verildiği konum. 

Mesela Python öntanımlı olarak, ürettiği çıktıları ekrana verir. Eğer o anda
etkileşimli kabukta çalışıyorsanız, Python ürettiği çıktıları etkileşimli kabuk
üzerinde gösterir. Eğer yazdığınız bir programı komut satırında
çalıştırıyorsanız, üretilen çıktılar komut satırında görünür. Dolayısıyla
Python'ın standart çıktı konumu etkileşimli kabuk veya komut satırıdır. Yani
``print()`` fonksiyonu yardımıyla bastığınız çıktılar etkileşimli kabukta ya da
komut satırında görünecektir.

Şimdi bu konuyu daha iyi anlayabilmek için birkaç örnek yapalım.

Normal şartlar altında ``print()`` fonksiyonunun çıktısını etkileşimli kabukta
görürüz::
    
    >>> print("Ben Python, Monty Python!")
    
    Ben Python, Monty Python!

Ama eğer istersek ``print()`` fonksiyonunun, çıktılarını ekrana değil, bir
dosyaya yazdırmasını da sağlayabiliriz. Mesela biz şimdi ``print()``
fonksiyonunun `deneme.txt` adlı bir dosyaya çıktı vermesini sağlayalım.

Bunun için sırasıyla şu kodları yazalım::

    >>> dosya = open("deneme.txt", "w")
    >>> print("Ben Python, Monty Python!", file=dosya)
    >>> dosya.close()

Herhangi bir çıktı almadınız, değil mi? Evet. Çünkü yazdığımız bu kodlar
sayesinde ``print()`` fonksiyonu, çıktılarını `deneme.txt` adlı bir dosyaya
yazdırdı.

Gelin isterseniz yukarıdaki kodları satır satır inceleyelim:

\1. Öncelikle `deneme.txt` adlı bir dosya oluşturduk ve bu dosyayı `dosya` adlı
bir değişkene atadık. Burada kullandığımız ``open()`` fonksiyonuna çok
takılmayın. Bunu birkaç bölüm sonra inceleyeceğiz. Biz şimdilik bu şekilde dosya
oluşturulduğunu bilelim yeter. Bu arada ``open`` fonksiyonunun da biçim olarak
``type()``, ``len()``, ``pow()`` ve ``print()`` fonksiyonlarına ne kadar
benzediğine dikkat edin. Gördüğünüz gibi ``open()`` fonksiyonu da tıpkı
``type()``, ``len()``, ``pow()`` ve ``print()`` fonksiyonları gibi birtakım
parametreler alıyor. Bu fonksiyonun ilk parametresi `"deneme.txt"` adlı bir
karakter dizisi. İşte bu karakter dizisi bizim oluşturmak istediğimiz dosyanın
adını gösteriyor. İkinci parametre ise `"w"` adlı başka bir karakter dizisi. Bu
da `deneme.txt` dosyasının yazma kipinde (modunda) açılacağını gösteriyor. Ama
dediğim gibi, siz şimdilik bu ayrıntılara fazla takılmayın. İlerleyen derslerde,
bu konuları adınızı bilir gibi bileceğinizden emin olabilirsiniz.

\2. Oluşturduğumuz bu `deneme.txt` adlı dosya, o anda bulunduğunuz dizin içinde
oluşacaktır. Bu dizinin hangisi olduğunu öğrenmek için şu komutları
verebilirsiniz::
    
    >>> import os
    >>> os.getcwd()

Bu komutun çıktısında hangi dizinin adı görünüyorsa, `deneme.txt` dosyası da o
dizinin içindedir. Mesela bendeki çıktı |lin_home|\ `/Desktop`. Demek ki
oluşturduğum `deneme.txt` adlı dosya masaüstündeymiş. Ben bu komutları Ubuntu
üzerinde verdim. Eğer Windows üzerinde verseydim şuna benzer bir çıktı
alacaktım: |win_home|\ `\\Desktop`

\3. Ardından da normal bir şekilde ``print()`` fonksiyonumuzu çalıştırdık. Ama
gördüğünüz gibi ``print()`` fonksiyonu bize herhangi bir çıktı vermedi. Çünkü,
daha önce de söylediğimiz gibi, ``print()`` fonksiyonunu biz ekrana değil,
dosyaya çıktı verecek şekilde ayarladık. Bu işlemi, `file` adlı bir parametreye,
biraz önce tanımladığımız `dosya` değişkenini yazarak yaptık.

\4. Son komut yardımıyla da, yaptığımız değişikliklerin dosyada görünebilmesi
için ilk başta açtığımız dosyayı kapatıyoruz.

Şimdi `deneme.txt` adlı dosyayı açın. Biraz önce ``print()`` fonksiyonuyla
yazdırdığımız `"Ben Python, Monty Python!"` karakter dizisinin dosyaya işlenmiş
olduğunu göreceksiniz.

Böylece ``print()`` fonksiyonunun standart çıktı konumunu değiştirmiş olduk.
Yani ``print()`` fonksiyonunun `file` adlı parametresine farklı bir değer
vererek, ``print()`` fonksiyonunun etkileşimli kabuğa değil dosyaya yazmasını
sağladık.

Tıpkı `sep` ve `end` parametreleri gibi, `file` parametresi de, siz görmeseniz
bile her zaman ``print()`` fonksiyonunun içinde vardır. Yani diyelim ki şöyle
bir komut verdik::
    
    >>> print("Tahir olmak da ayıp değil", "Zühre olmak da")

Python bu komutu şöyle algılar::

    >>> print("Tahir olmak da ayıp değil", "Zühre olmak da", 
    ... sep=" ", end="\n", file=sys.stdout)

Yani kendisine parametre olarak verilen değerleri ekrana yazdırırken sırasıyla
şu işlemleri gerçekleştirir:

    #. Parametrelerin arasına birer boşluk koyar (``sep=" "``), 
    #. Ekrana yazdırma işlemi bittikten sonra parametrelerin sonuna satır başı
       karakteri ekler (``end="\n"``)
    #. Bu çıktıyı standart çıktı konumuna gönderir (``file=sys.stdout``).

İşte biz burada `file` parametresinin değeri olan standart çıktı konumuna başka
bir değer vererek bu konumu değiştiriyoruz.

Gelin isterseniz bununla ilgili bir örnek daha yapalım. Mesela kişisel
bilgilerimizi bir dosyaya kaydedelim. Öncelikle bilgileri kaydedeceğimiz dosyayı
oluşturalım::
    
    >>> f = open("kişisel_bilgiler.txt", "w")
    
Bu kodlarla, `kişisel_bilgiler.txt` adını taşıyan bir dosyayı yazma kipinde
(`w`) açmış ve bu dosyayı `f` adlı bir değişkene atamış olduk. Şimdi bilgileri
yazmaya başlayabiliriz::
    
    >>> print("Fırat Özgül", file=f)
    >>> print("Adana", file=f)
    >>> print("Ubuntu", file=f)

İşimiz bittiğinde dosyayı kapatmayı unutmuyoruz. Böylece bütün bilgiler dosyaya
yazılmış oluyor::
    
    >>> f.close()

Oluşturduğumuz `kişisel_bilgiler.txt` adlı dosyayı açtığımızda, ``print()``
fonksiyonuna verdiğimiz parametrelerin dosyaya yazdırıldığını görüyoruz.

En başta da söylediğim gibi, bu bölümde henüz öğrenmediğimiz bazı şeylerle
karşılaştık. Eğer yukarıda verilen örnekleri anlamakta zorlandıysanız hiç endişe
etmenize gerek yok. Birkaç bölüm sonra burada anlattığımız şeyler size çocuk
oyuncağı gibi gelecek...

flush
=========

Şimdiye kadar ``print()`` fonksiyonunun `sep`, `end` ve `file` adlı özel
birtakım parametreleri olduğunu öğrendik. ``print()`` fonksiyonunun bunların
dışında başka bir özel parametresi daha bulunur. Bu parametrenin adı `flush`.
İşte şimdi biz ``print()`` fonksiyonunun bu `flush` adlı parametresinden söz
edeceğiz.

Bildiğiniz gibi, ``print()`` gibi bir komut verdiğimizde Python, yazdırmak
istediğimiz bilgiyi standart çıktı konumuna gönderir. Ancak Python'da bazı
işlemler standart çıktı konumuna gönderilmeden önce bir süre tamponda bekletilir
ve daha sonra bekleyen bu işlemler topluca standart çıktı konumuna gönderilir.
Peki ilk başta çok karmaşıkmış gibi görünen bu ifade ne anlama geliyor?

Aslında siz bu olguya hiç yabancı değilsiniz. `file` parametresini anlatırken
verdiğimiz şu örneği tekrar ele alalım::

    >>> f = open("kişisel_bilgiler.txt", "w")
    
Bu komutla `kişisel_bilgiler.txt` adlı bir dosyayı yazma kipinde açtık. Şimdi bu
dosyaya bazı bilgiler ekleyelim::
    
    >>> print("Fırat Özgül", file=f)

Bu komutla `kişisel_bilgiler.txt` adlı dosyaya 'Fırat Özgül' diye bir satır
eklemiş olduk.

Şimdi bilgisayarınızda oluşan bu `kişisel_bilgiler.txt` dosyasını açın.
Gördüğünüz gibi dosyada hiçbir bilgi yok. Dosya şu anda boş görünüyor. Halbuki
biz biraz önce bu dosyaya 'Fırat Özgül' diye bir satır eklemiştik, değil mi?

Python bizim bu dosyaya eklemek istediğimiz satırı tampona kaydetti. Dosyaya
yazma işlemleri sona erdiğinde ise Python, tamponda bekleyen bütün bilgileri
standart çıktı konumuna (yani bizim durumumuzda `f` adlı değişkenin tuttuğu
`kişisel_bilgiler.txt` adlı dosyaya) boşaltacak.

Dosyaya başka bilgiler de yazalım::

    >>> print("Adana", file=f)
    >>> print("Ubuntu", file=f)

Dosyaya yazacağımız şeyler bu kadar. Artık yazma işleminin sona erdiğini
Python'a bildirmek için şu komutu veriyoruz::
    
    >>> f.close()

Böylece dosyamızı kapatmış olduk. Şimdi `kişisel_bilgiler.txt` adlı dosyaya çift
tıklayarak dosyayı tekrar açın. Orada 'Fırat Özgül', 'Adana' ve 'Ubuntu'
satırlarını göreceksiniz.

Gördüğünüz gibi, gerçekten de Python dosyaya yazdırmak istediğimiz bütün
verileri önce tamponda bekletti, daha sonra dosya kapatılınca tamponda bekleyen
bütün verileri dosyaya boşalttı. İşte `flush` parametresi ile, bahsettiğimiz bu
boşaltma işlemini kontrol edebilirsiniz. Şimdi dikkatlice inceleyin::
    
    >>> f = open("kişisel_bilgiler.txt", "w")

Dosyamızı oluşturduk. Şimdi bu dosyaya bazı bilgiler ekleyelim::
    
    >>> print("Merhaba Dünya!", file=f, flush=True)

Gördüğünüz gibi, burada `flush` adlı yeni bir parametre kullandık. Bu
parametreye verdiğimiz değer `True`. Şimdi dosyaya çift tıklayarak dosyayı açın.
Gördüğünüz gibi, henüz dosyayı kapatmadığımız halde bilgiler dosyaya yazıldı. Bu
durum, tahmin edebileceğiniz gibi, `flush` parametresine `True` değeri vermemiz
sayesindedir. Bu parametre iki değer alabilir: `True` ve `False`. Bu
parametrenin öntanımlı değeri `False`'tur. Yani eğer biz bu parametreye herhangi
bir değer belirtmezsek Python bu parametrenin değerini `False` olarak kabul
edecek ve bilgilerin dosyaya yazılması için dosyanın kapatılmasını
bekleyecektir. Ancak bu parametreye `True` değerini verdiğimizde ise veriler
tamponda bekletilmeksizin standart çıktı konumuna gönderilecektir.

Yazdığınız bir programda, yapmak istediğiniz işin niteliğine göre, bir dosyaya
yazmak istediğiniz bilgilerin bir süre tamponda bekletilmesini veya hiç
bekletilmeden doğrudan dosyaya yazılmasını isteyebilirsiniz. İhtiyacınıza bağlı
olarak da `flush` parametresinin değerini `True` veya `False` olarak
belirleyebilirsiniz.

Birkaç Pratik Bilgi
********************

Buraya gelene kadar ``print()`` fonksiyonu ve bu fonksiyonun parametreleri
hakkında epey söz söyledik. Dilerseniz şimdi de, programcılık maceranızda
işinize yarayacak, işlerinizi kolaylaştıracak bazı ipuçları verelim.

Yıldızlı Parametreler
========================

Şimdi size şöyle bir soru sormama izin verin: Acaba aşağıdaki gibi bir çıktıyı
nasıl elde ederiz?

::

    L.i.n.u.x

Aklınıza hemen şöyle bir cevap gelmiş olabilir::

    >>> print("L", "i", "n", "u", "x", sep=".")
    
    L.i.n.u.x

Yukarıdaki, gerçekten de doğru bir çözümdür. Ancak bu soruyu çözmenin çok daha
basit bir yolu var. Şimdi dikkatle bakın::
    
    >>> print(*"Linux", sep=".")
    
    L.i.n.u.x
    
Konuyu açıklamaya geçmeden önce bir örnek daha verelim::

    >>> print(*"Galatasaray")
    
    G a l a t a s a r a y

Burada neler döndüğünü az çok tahmin ettiğinizi zannediyorum. Son örnekte de
gördüğünüz gibi, `"Galatasaray"` karakter dizisinin başına eklediğimiz yıldız
işareti; `"Galatasaray"` karakter dizisinin her bir öğesini parçalarına
ayırarak, bunları tek tek ``print()`` fonksiyonuna yolluyor. Yani sanki
``print()`` fonksiyonunu şöyle yazmışız gibi oluyor::
    
    >>> print("G", "a", "l", "a", "t", "a", "s", "a", "r", "a", "y")
    
    G a l a t a s a r a y

Dediğimiz gibi, bir fonksiyona parametre olarak verdiğimiz bir karakter
dizisinin başına eklediğimiz yıldız işareti, bu karakter dizisini tek tek
öğelerine ayırıp, bu öğeleri yine tek tek ve sanki her bir öğe ayrı bir
parametreymiş gibi o fonksiyona gönderdiği için doğal olarak yıldız işaretini
ancak, birden fazla parametre alabilen fonksiyonlara uygulayabiliriz.

Örneğin ``len()`` fonksiyonu sadece tek bir parametre alabilir::
    
    >>> len("Galatasaray")
    
    11

Bu fonksiyonu birden fazla parametre ile kullanamayız::

    >>> len("Galatasaray", "Fenerbahçe", "Beşiktaş")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: len() takes exactly one argument (3 given)

Hata mesajında da söylendiği gibi, ``len()`` fonksiyonu yalnızca tek bir
parametre alabilirken, biz `3` parametre vermeye çalışmışız...

Dolayısıyla yıldızlı parametreleri ``len()`` fonksiyonuna uygulayamayız::

    >>> len(*"Galatasaray")

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: len() takes exactly one argument (11 given)

Bir parametrenin başına yıldız eklediğimizde, o parametreyi oluşturan bütün
öğeler tek tek fonksiyona gönderildiği için, sanki ``len()`` fonksiyonuna `1`
değil de, `11` ayrı parametre vermişiz gibi bir sonuç ortaya çıkıyor.

Yıldızlı parametreleri bir fonksiyona uygulayabilmemiz için o fonksiyonun birden
fazla parametre alabilmesinin yanısıra, yapısının da yıldızlı parametre almaya
uygun olması gerekir. Mesela ``open()``, ``type()`` ve biraz önce bahsettiğimiz
``len()`` fonksiyonlarının yapısı yıldızlı parametre almaya uygun değildir.
Dolayısıyla yıldızlı parametreleri her fonksiyonla birlikte kullanamayız, ama
``print()`` fonksiyonu yıldızlı parametreler için son derece uygun bir
fonksiyondur::
    
    >>> print(*"Galatasaray")
    
    G a l a t a s a r a y

    >>> print(*"TBMM", sep=".")
    
    T.B.M.M
    
    >>> print(*"abcçdefgğh", sep="/")
    
    a/b/c/ç/d/e/f/g/ğ/h
    
Bu örneklerden de gördüğünüz gibi, ``print()`` fonksiyonuna verdiğimiz bir
parametrenin başına yıldız eklediğimizde, o parametre tek tek parçalarına
ayrılıp ``print()`` fonksiyonuna gönderildiği için, sonuç olarak `sep`
parametresinin karakter dizisi öğelerine tek tek uygulanmasını sağlamış
oluyoruz.

Hatırlarsanız `sep` parametresinin öntanımlı değerinin bir adet boşluk karakteri
olduğunu söylemiştik. Yani aslında Python yukarıdaki ilk komutu şöyle görüyor::
    
    >>> print(*"Galatasaray", sep=" ")

Dolayısıyla, yıldız işareti sayesinde `"Galatasaray"` adlı karakter dizisinin
her bir öğesinin arasına bir adet boşluk karakteri yerleştiriliyor. Bir sonraki
`"TBMM"` karakter dizisinde ise, `sep` parametresinin değerini nokta işareti
olarak değiştirdiğimiz için `"TBMM"` karakter dizisinin her bir öğesinin arasına
bir adet nokta işareti yerleştiriliyor. Aynı şekilde `"abcçdefgğh"` karakter
dizisinin her bir öğesini tek tek ``print()`` fonksiyonuna yollayarak, `sep`
parametresine verdiğimiz `/` işareti yardımıyla her öğenin arasına bu `/`
işaretini yerleştirebiliyoruz.

Yıldızlı parametrelerle ilgili tek kısıtlama, bunların sayılarla birlikte
kullanılamayacak olmasıdır::
    
    >>> print(*2345)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: print() argument after * must be a sequence, not int

Çünkü yıldızlı parametreler ancak ve ancak dizi özelliği taşıyan veri tipleriyle
birlikte kullanılabilir. Mesela karakter dizileri bu türden bir veri tipidir.
İlerde dizi özelliği taşıyan ve bu sayede yıldızlı parametrelerle birlikte
kullanılabilecek başka veri tiplerini de öğreneceğiz.
    
Yukarıda verdiğimiz örnekler bize yıldızlı parametrelerin son derece kullanışlı
araçlar olduğunu gösteriyor. İleride de bu parametrelerden bol bol
yararlanacağız. Biz şimdi bu konuyu burada kapatıp başka bir şeyden söz edelim.

sys.stdout'u Kalıcı Olarak Değiştirmek
======================================

Önceki başlıklar altında verdiğimiz örneklerden de gördüğünüz gibi, ``print()``
fonksiyonunun `file` parametresi yardımıyla Python'ın standart çıktı konumunu
geçici olarak değiştirebiliyoruz. Ama bazı durumlarda, yazdığınız programlarda,
o programın işleyişi boyunca standart dışı bir çıktı konumu belirlemek
isteyebilirsiniz. Yani standart çıktı konumunu geçici olarak değil, kalıcı
olarak değiştirmeniz gerekebilir. Mesela yazdığınız programda bütün çıktıları
bir dosyaya yazdırmayı tercih edebilirsiniz. Elbette bu işlemi her defasında
`file` parametresini, çıktıları yazdırmak istediğiniz dosyanın adı olarak
belirleyerek yapabilirsiniz. Tıpkı şu örnekte olduğu gibi::
    
    >>> f = open("dosya.txt", "w")
    >>> print("Fırat Özgül", file=f)
    >>> print("Adana", file=f)
    >>> print("Ubuntu", file=f)
    >>> f.close()

Gördüğünüz gibi, her defasında `file` parametresine `f` değerini vererek işimizi
hallettik. Ama bunu yapmanın daha pratik bir yöntemi var. Dilerseniz yazdığınız
programın tüm işleyişi boyunca çıktıları başka bir konuma yönlendirebilirsiniz.
Bunun için hem şimdiye kadar öğrendiğimiz, hem de henüz öğrenmediğimiz bazı
bilgileri kullanacağız.

İlk önce şöyle bir kod yazalım::

    >>> import sys

Bu kod yardımıyla `sys` adlı özel bir 'modülü' programımıza dahil etmiş, yani
içe aktarmış olduk. Peki 'modül' nedir, 'içe aktarmak' ne demek?

Aslında biz bu 'modül' ve 'içe aktarma' kavramlarına hiç de yabancı değiliz.
Önceki derslerde, pek üzerinde durmamış da olsak, biz Python'daki birkaç modülle
zaten tanışmıştık. Mesela `os` adlı bir modül içindeki ``getcwd()`` adlı bir
fonksiyonu kullanarak, o anda hangi dizinde bulunduğumuzu öğrenebilmiştik::
        
    >>> import os
    >>> os.getcwd()
        
Aynı şekilde `keyword` adlı başka bir modül içindeki `kwlist` adlı değişkeni
kullanarak, hangi kelimelerin Python'da değişken adı olarak kullanılamayacağını
da listeleyebilmiştik::
        
    >>> import keyword
    >>> keyword.kwlist

İşte şimdi de, `os` ve `keyword` modüllerine ek olarak `sys` adlı bir modülden
söz ediyoruz. Gelin isterseniz öteki modülleri şimdilik bir kenara bırakıp, bu
`sys` denen modüle dikkatimizi verelim.

Dediğimiz gibi, `sys` modülü içinde pek çok önemli değişken ve fonksiyon
bulunur. Ancak bir modül içindeki değişken ve fonksiyonları kullanabilmek için o
modülü öncelikle programımıza dahil etmemiz, yani içe aktarmamız gerekiyor. Bunu
``import`` komutuyla yapıyoruz::
    
    >>> import sys

Artık `sys` modülü içindeki bütün fonksiyon ve değişkenlere ulaşabileceğiz. 

`sys` modülü içinde bulunan pek çok değişken ve fonksiyondan biri de `stdout`
adlı değişkendir. Bu değişkenin değerine şöyle ulaşabilirsiniz::
    
    >>> sys.stdout

Bu komut şuna benzer bir çıktı verir::
    
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1254'>

Bu çıktıdaki `name='<stdout>'` kısmına dikkat edin. Bu ifadeye birazdan geri
döneceğiz. Biz şimdi başka bir şeyden söz edelim.

Hatırlarsanız etkileşimli kabuğu nasıl kapatabileceğimizi anlatırken,
etkileşimli kabuktan çıkmanın bir yolunun da şu komutları vermek olduğunu
söylemiştik::
    
    >>> import sys; sys.exit()

Bu komutu tek satırda yazmıştık, ama istersek şöyle de yazabiliriz elbette::

    >>> import sys
    >>> sys.exit()
    
Dedik ya, `sys` modülü içinde pek çok değişken ve fonksiyon bulunur. Nasıl
`stdout` `sys` modülü içindeki değişkenlerden biri ise, ``exit()`` de `sys`
modülü içinde bulunan fonksiyonlardan biridir.

Biz 'modüller' konusunu ilerleyen derslerde ayrıntılı bir şekilde inceleyeceğiz.
Şimdilik modüllere ilişkin olarak yalnızca şunları bilelim yeter:

\1. Python'da modüller ``import`` komutu ile içe aktarılır. Örneğin `sys`
adlı modülü içe aktarmak için ``import sys`` komutunu veriyoruz.

\2. Modüller içinde pek çok faydalı değişken ve fonksiyon bulunur. İşte bir
modülü içe aktardığımızda, o modül içindeki bu değişken ve fonksiyonları
kullanma imkanı elde ederiz.

\3. `sys` modülü içindeki değişkenlere bir örnek `stdout`; fonksiyonlara
örnek ise ``exit()`` fonksiyonudur. Bir modül içindeki bu değişken ve
fonksiyonlara 'modül_adı.değişken_ya_da_fonksiyon' formülünü kullanarak
erişebiliriz. Örneğin:
    
    .. parsed-literal::
    
        >>> sys.stdout
        >>> sys.exit()
    
\4. Hatırlarsanız bundan önce de, ``open()`` fonksiyonu ile dosya oluşturmayı
anlatırken, oluşturulan dosyanın hangi dizinde olduğunu bulabilmek amacıyla, o
anda içinde bulunduğumuz dizini tespit edebilmek için şu kodları kullanmıştık:

    .. parsed-literal::
    
        >>> import os
        >>> os.getcwd()
    
Burada da `os` adlı başka bir modül görüyoruz. İşte `os` da tıpkı `sys` gibi
bir modüldür ve tıpkı `sys` modülünde olduğu gibi, `os` modülünün de içinde
pek çok yararlı değişken ve fonksiyon bulunur. ``getcwd()`` adlı fonksiyon
da `os` modülü içinde yer alan ve o anda hangi dizin altında bulunduğumuzu
gösteren bir fonksiyondur. Elbette, yine tıpkı `sys` modülünde olduğu gibi,
`os` modülü içindeki bu yararlı değişken ve fonksiyonları kullanabilmek için
de öncelikle bu `os` modülünü içe aktarmamız, yani programımıza dahil
etmemiz gerekiyor. `os` modülünü ``import`` komutu aracılığıyla uygun bir
şekilde içe aktardıktan sonra, modül içinde yer alan ``getcwd()`` adlı
fonksiyona yine 'modül_adı.fonksiyon' formülünü kullanarak erişebiliyoruz. 

Modüllere ilişkin şimdilik bu kadar bilgi yeter. Modülleri bir kenara bırakıp
yolumuza devam edelim...

Eğer ``sys.exit()`` komutunu verip etkileşimli kabuktan çıktıysanız, etkileşimli
kabuğa tekrar girin ve `sys` modülünü yeniden içe aktarın::
    
    >>> import sys

.. note:: Bir modülü aynı etkileşimli kabuk oturumu içinde bir kez içe aktarmak
 yeterlidir. Bir modülü bir kez içe aktardıktan sonra, o oturum süresince bu
 modül içindeki değişken ve fonksiyonları kullanmaya devam edebilirsiniz. Ama
 tabii ki etkileşimli kabuğu kapatıp tekrar açtıktan sonra, bir modülü
 kullanabilmek için o modülü tekrar içe aktarmanız gerekir.

Şimdi şu kodu yazın::

    >>> f = open("dosya.txt", "w")

Bu kodun anlamını biliyorsunuz. Burada `dosya.txt` adlı bir dosyayı yazma
kipinde açmış olduk. Tahmin edebileceğiniz gibi, çıktılarımızı ekran yerine bu
dosyaya yönlendireceğiz.

Şimdi de şöyle bir kod yazalım::

    >>> sys.stdout = f

Bildiğiniz gibi, `sys.stdout` değeri Python'ın çıktıları hangi konuma vereceğini
belirliyor. İşte biz burada `sys.stdout`'un değerini biraz önce oluşturduğumuz
`f` adlı dosya ile değiştiriyoruz. Böylece Python bütün çıktıları `f` değişkeni
içinde belirttiğimiz `dosya.txt` adlı dosyaya gönderiyor.

Bu andan sonra yazacağınız her şey `dosya.txt` adlı dosyaya gidecektir::

    >>> print("deneme metni", flush=True)

Gördüğünüz gibi, burada `file` parametresini kullanmadığımız halde çıktılarımız
ekrana değil, `dosya.txt` adlı bir dosyaya yazdırıldı. Peki ama bu nasıl oldu?
Aslında bunun cevabı çok basit: Biraz önce ``sys.stdout = f`` komutuyla
`sys.stdout`'un değerini `f` değişkeninin tuttuğu dosya ile değiştirdik. Bu
işlemi yapmadan önce ``sys.stdout``'un değeri şuydu hatırlarsanız::
    
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1254'>

Ama ``sys.stdout = f`` komutundan sonra her şey değişti. Kontrol edelim::

    >>> print(sys.stdout, flush=True)

Elbette bu komuttan herhangi bir çıktı almadınız. Çıktının ne olduğunu görmek
için `dosya.txt` adlı dosyayı açın. Orada şu satırı göreceksiniz::
    
    <_io.TextIOWrapper name='dosya.txt' mode='w' encoding='cp1254'>

Gördüğünüz gibi, özgün `stdout` çıktısındaki `name='<stdout>'` değeri
`name='dosya.txt'` olmuş. Dolayısıyla artık bütün çıktılar `dosya.txt` adlı
dosyaya gidiyor...

Bu arada, yukarıdaki çıktıda görünen `name`, `mode` ve `encoding` değerlerine şu
şekilde ulaşabilirsiniz:

    >>> sys.stdout.name
    >>> sys.stdout.mode
    >>> sys.stdout.encoding

Burada ``sys.stdout.name`` komutu standart çıktı konumunun o anki adını
verecektir. ``sys.stdout.mode`` komutu ise standart çıktı konumunun hangi kipe
sahip olduğunu gösterir. Standart çıktı konumu genellikle yazma kipinde (`w`)
bulunur. ``sys.stdout.encoding`` kodu ise standart çıktı konumunun sahip olduğu
kodlama biçimini gösterir. Kodlama biçimi, standart çıktı konumuna
yazdıracağınız karakterlerin hangi kodlama biçimi ile kodlanacağını belirler.
Kodlama biçimi Windows'ta genellikle 'cp1254', GNU/Linux'ta ise 'utf-8'dir. Eğer
bu kodlama biçimi yanlış olursa, mesela dosyaya yazdıracağınız karakterler
içindeki Türkçe harfler düzgün görüntülenemez. Eğer burada söylediklerimiz size
şu anda anlaşılmaz geliyorsa, söylediklerimizi dikkate almadan yolunuza devam
edebilirsiniz. Birkaç bölüm sonra bu söylediklerimiz size daha fazla şey ifade
etmeye başlayacak nasıl olsa.

Peki standart çıktı konumunu eski haline döndürmek isterseniz ne yapacaksınız?
Bunun için etkileşimli kabuktan çıkıp tekrar girebilirsiniz. Etkileşimli kabuğu
tekrar açtığınızda her şeyin eski haline döndüğünü göreceksiniz. Aynı şekilde,
eğer bu kodları bir program dosyasına yazmış olsaydınız, programınız
kapandığında her şey eski haline dönecekti.

Peki standart çıktı konumunu, etkileşimli kabuktan çıkmadan veya programı
kapatmadan eski haline döndürmenin bir yolu var mı? Elbette var. Dikkatlice
bakın::
    
    >>> import sys
    >>> f = open("dosya.txt", "w")
    >>> sys.stdout, f = f, sys.stdout
    >>> print("deneme", flush=True)
    >>> f, sys.stdout = sys.stdout, f
    >>> print("deneme")
    
    deneme
    
.. warning:: Eğer yukarıdaki kodları çalıştıramıyorsanız, aynı etkileşimli kabuk
 oturumunda önceden verdiğiniz kodlar bu kodların doğru çıktı vermesini
 engelliyor olabilir. Bu sorunu aşmak için, etkileşimli kabuğu kapatıp tekrar
 açın ve yukarıdaki komutları tekrar verin.

Aslında burada anlayamayacağınız hiçbir şey yok. Burada yaptığımız şeyi geçen
bölümlerde değişkenlerin değerini nasıl takas edeceğimizi anlatırken de
yapmıştık. Hatırlayalım::
    
    >>> osman = "Araştırma Geliştirme Müdürü"
    >>> mehmet = "Proje Sorumlusu"
    >>> osman, mehmet = mehmet, osman

Bu kodlarla Osman ve Mehmet'in unvanlarını birbiriyle takas etmiştik. İşte
yukarıda yaptığımız şey de bununla aynıdır. ``sys.stdout, f = f, sys.stdout``
dediğimizde `f` değerini `sys.stdout`'a, `sys.stdout`'un değerini ise `f`'ye
vermiş oluyoruz. ``f, sys.stdout = sys.stdout, f`` dediğimizde ise, bu işlemin
tam tersini yaparak her şeyi eski haline getirmiş oluyoruz.

Python'ın bize sunduğu bu kolaylıktan faydalanarak değişkenlerin değerini
birbiriyle kolayca takas edebiliyoruz. Eğer böyle bir kolaylık olmasaydı
yukarıdaki kodları şöyle yazabilirdik::
    
    >>> import sys
    >>> f = open("dosya.txt", "w")
    >>> özgün_stdout = sys.stdout
    >>> sys.stdout = f
    >>> print("deneme", flush=True)
    >>> sys.stdout = özgün_stdout
    >>> print("deneme")
    
    deneme

Gördüğünüz gibi, `sys.stdout`'un değerini kaybetmemek için, `sys.stdout`
değerini `f` adlı dosyaya göndermeden önce şu kod yardımıyla yedekliyoruz::
    
    >>> özgün_stdout = sys.stdout

`sys.stdout`'un özgün değerini `özgün_stdout` değişkenine atadığımız için, bu
değere sonradan tekrar ulaşabileceğiz. Zaten yukarıdaki kodlardan da gördüğünüz
gibi, `sys.stdout`'un özgün değerine dönmek istediğimizde şu kodu yazarak
isteğimizi gerçekleştirebiliyoruz::
    
    >>> sys.stdout = özgün_stdout

Böylece `stdout` değeri eski haline dönmüş oluyor ve bundan sonra yazdırdığımız
her şey yeniden ekrana basılmaya başlıyor.

...ve böylece uzun bir bölümü daha geride bıraktık. Bu bölümde hem ``print()``
fonksiyonunu bütün ayrıntılarıyla incelemiş olduk, hem de Python programlama
diline dair başka çok önemli kavramlardan söz ettik. Bu bakımdan bu bölüm bize
epey şey öğretti. Artık öğrendiğimiz bu bilgileri de küfemize koyarak başımız
dik bir şekilde yola devam edebiliriz.
