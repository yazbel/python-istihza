.. meta::
   :description: Python 3.x'te karakter dizileri
   :keywords: python, string, karakter dizisi, metotlar, capitalize, center, 
              count, encode, endswith, expandtabs, find, format, format_map, 
              index, isalnum, isalpha, isdecimal, isdigit, isidentifier, islower, 
              isnumeric, isprintable, isspace, istitle, isupper, join, ljust, 
              lower, lstrip, maketrans, partition, replace, rfind, rindex, rjust, 
              rpartition, rsplit, rstrip, split, splitlines, startswith, strip, 
              swapcase, title, translate, upper, zfill

.. highlight:: py3

*****************
Karakter Dizileri
*****************

Buraya gelene kadar Python programlama diline ilişkin epey bilgi edindik. Artık
yazdığımız programlarda ``input()`` fonksiyonu sayesinde kullanıcıyla iletişim
kurabiliyor; ``if``, ``elif``, ``else`` deyimleri yardımıyla programlarımızın
karar vermesini sağlayabiliyor; işleçler ve döngüler yoluyla programlarımızı
istediğimiz sayıda çalıştırabiliyoruz. Eğer buraya kadar olan bölümleri
dikkatlice takip ettiyseniz, şu ana kadar öğrendiklerinize dayanarak, Python'ı
giriş düzeyinde bildiğinizi rahatlıkla iddia edebilirsiniz. Zira şimdiye kadar
öğrendiklerinizi kullanarak ufak tefek de olsa işe yarar programlar yazabilecek
durumdasınız.

Buraya kadar öğrendiğimiz bilgiler Python programlama dilinin temellerini
oluşturuyordu. Temel Python bilgilerini edindiğimize göre, artık başlangıç-orta
düzey arası konuları incelemeye başlayabileceğiz.

Bu bölümde, önceki derslerde üstünkörü bakıp geçtiğimiz bir konu olan karakter
dizilerini çok daha derinlemesine ele alacağız. Python programlama dili içindeki
önemi nedeniyle bu bölüm epey uzun olacak.

Aslında biz karakter dizisi kavramının ne olduğunu biliyoruz. Çok kaba bir
şekilde ifade etmek gerekirse, karakter dizileri, adından da anlaşılacağı gibi,
karakterlerin bir araya gelmesiyle oluşan bir dizidir. Karakter dizileri; tek,
çift veya üç tırnak içinde gösterilen, öteki veri tiplerinden de bu tırnaklar
aracılığıyla ayırt edilen özel bir veri tipidir. Teknik olarak ifade etmek
gerekirse, bir nesneyi ``type()`` fonksiyonu yardımıyla sorguladığımızda, eğer
`<class 'str'>` çıktısı alıyorsak bu nesne bir karakter dizisidir.

Her ne kadar ayrıntılarına girmemiş de olsak, dediğimiz gibi, biz karakter
dizilerini daha ilk bölümlerden bu yana her fırsatta kullanıyoruz. Dolayısıyla
bu veri tipinin ne olduğu konusunda bir sıkıntımız yok. Bu bölümde, şimdiye
kadar karakter dizileri ile ilgili öğrendiğimiz şeylere ek olarak, karakter
dizilerin metotlarından da söz edeceğiz.

Peki bu 'metot' denen şey de ne oluyor?

Kabaca ifade etmek gerekirse, metotlar Python'da nesnelerin niteliklerini
değiştirmemizi, sorgulamamızı veya bu nesnelere yeni özellikler katmamızı
sağlayan araçlardır. Metotlar sayesinde karakter dizilerini istediğimiz gibi
eğip bükebileceğiz.

Elbette bu bölümde bahsedeceğimiz tek şey karakter dizilerinin metotları
olmayacak. Bu bölümde aynı zamanda karakter dizilerinin yapısı ve özelliklerine
dair söyleyeceklerimiz de olacak.

Python'da şimdiye kadar yapabildiğimiz şeylerin sizi tatmin etmekten uzak
olduğunu, daha fazlasını yapabilmek için sabırsızlandığınızı tahmin
edebiliyorum. O halde ne duruyoruz, hiç vakit kaybetmeden yola koyulalım.

Karakter Dizilerinin Öğelerine Erişmek
**************************************

Python ile programlama yaparken karakter dizileri ile iki şekilde
karşılaşabilirsiniz: Birincisi, bir karakter dizisini doğrudan kendiniz
tanımlamış olabilirsiniz. İkincisi, karakter dizisi size başka bir kaynak
aracılığıyla gelmiş olabilir (mesela ``input()`` fonksiyonu yardımıyla
kullanıcıdan aldığınız bir veri).

Python'da kendi tanımladığınız ya da herhangi başka bir kaynaktan gelen karakter
dizilerine erişmenin birkaç farklı yolu vardır. Örneğin::

    >>> nesne = "karakter dizisi"

Burada değeri `"karakter dizisi"` olan `nesne` adlı bir değişken tanımladık.
Yazdığımız programlarda bu değişkene erişmek için, değişkenin adını kullanmamız
yeterlidir. Örneğin::
    
    >>> print(nesne)

Bu komut bize karakter dizisinin tamamını verecektir. 

Bir karakter dizisini yukarıda gördüğümüz gibi kendimiz tanımlayabiliriz. Bunun
dışında, mesela ``input()`` fonksiyonuyla kullanıcıdan aldığımız verilerin de
birer karakter dizisi olacağını biliyoruz::
    
    veri = input("Herhangi bir şey: ")

Tıpkı kendi tanımladığımız karakter dizilerinde olduğu gibi, kullanıcıdan gelen
karakter dizilerini de aşağıdaki komut yardımıyla ekranda görüntüleyebiliriz::
    
    print(veri)

Bu komut da bize `veri` değişkeninin tuttuğu karakter dizisinin tamamını
verecektir.

Ayrıca istersek bu karakter dizilerini bir ``for`` döngüsü içine alabilir,
böylece bu dizinin öğelerine tek tek de erişebiliriz::

    for karakter in nesne:
        print(karakter)

``for`` döngüsüyle elde ettiğimiz bu etkiyi şu kodlar yardımıyla da elde
edebileceğimizi gayet iyi biliyor olmalısınız::
    
    print(*nesne, sep="\n")

Önceki derslerde verdiğimiz örneklerden de bildiğiniz gibi, karakter dizilerinin
öğelerine yukarıdaki yöntemlerle tek tek erişebilmemiz sayesinde herhangi bir
işlemi karakter dizilerinin bütün öğelerine bir çırpıda uygulayabiliyoruz.
Mesela::
    
    nesne = "123456789"
    
    for n in nesne:
        print(int(n) * 2)

Burada `nesne` değişkeni içindeki sayı değerli karakter dizilerini `n` olarak
adlandırdıktan sonra, `n` değişkenlerinin her birini tek tek `2` sayısı ile
çarptık. Yani çarpma işlemini karakter dizisinin bütün öğelerine tek seferde
uygulayabildik. Bu arada, yukarıdaki örnekte `nesne` değişkeninin her bir
öğesini ``for`` döngüsü içinde ``int()`` fonksiyonu yardımıyla tam sayıya
çevirdiğimizi görüyorsunuz. Daha önce de defalarca söylediğimiz gibi, Python'da
o anda elinizde olan verinin tipini bilmeniz çok önemlidir. Eğer kendi
yazdığınız veya mesela ``input()`` fonksiyonundan gelen bir verinin karakter
dizisi olduğunu bilmezseniz yukarıdaki kodları şu şekilde yazma gafletine
düşebilirsiniz::
    
    nesne = "123456789"

    for n in nesne:
        print(n * 2)

Bu kodlar çalıştırıldıktan sonra hiç beklemediğiniz sonuçlar verecektir::

    11
    22
    33
    44
    55
    66
    77
    88
    99

Gördüğünüz gibi, aslında `nesne` içindeki öğeleri `2` ile çarpmak isterken, biz
her bir öğeyi iki kez ekrana yazdırmış olduk. Çünkü bildiğiniz gibi karakter
dizileri ile aritmetik işlemler yapamıyoruz. Eğer sayı değerli karakter dizileri
arasında aritmetik işlem yapacaksak öncelikle bu karakter dizilerini sayıya
çevirmemiz gerekir. Ayrıca gerçek bir program içinde yukarıdaki gibi bir durumun
ne kadar yıkıcı sonuçlar doğuracabileceğini düşünün. Yukarıdaki program çalışma
sırasında hiçbir hata vermeyeceği için, siz programınızın düzgün çalıştığını
zannederek hayatınıza devam edeceksiniz. Ama belki de yukarıdaki sinsi hata
yüzünden, programınızı kullanan bir şirket veri, zaman ve para kaybına
uğrayacak. 

Yukarıdaki örneklerde bir şey daha dikkatinizi çekmiş olmalı: Gördüğünüz gibi,
karakter dizisinin öğelerine erişirken bu öğelerin tamamını elde ediyoruz.
Mesela ``print(nesne)`` komutunu verdiğimizde veya `nesne` değişkenini bir döngü
içine aldığımızda sonuç olarak elde ettiğimiz şey, ilgili karakter dizisinin
tamamıdır. Yani aslında karakter dizisinin hangi öğesine erişeceğimizi
seçemiyoruz. Peki ya biz bir karakter dizisinin öğelerinin tamamına değil de,
sadece tek bir öğesine erişmek istersek ne yapacağız? Mesela yukarıdaki örnekte
`nesne` adlı değişken içindeki sayıların tamamını değil de sadece tek bir
öğesini (veya belli bir ölçüte göre yalnızca bazı öğelerini) `2` ile çarpmak
istersek nasıl bir yol izleyeceğiz?

Python'da karakter dizilerinin içindeki öğelerin bir sırası vardır. Örneğin
`"Python"` dediğimizde, bu karakter dizisinin ilk öğesi olan `"P"` karakterinin
sırası `0`'dır. `"y"` karakteri ise `1.` sıradadır. Aynı şekilde devam edersek,
`"t"` karakteri `2.`, `"h"` karakteri `3.`, `"o"` karakteri `4.`, `"n"`
karakteri ise `5.` sırada yer alır.

Bu anlattığımız soyut durumu bir örnekle somutlaştırmaya çalışalım:

Dedik ki, `"Python"` gibi bir karakter dizisinin her bir öğesinin belli bir
sırası vardır. İşte eğer biz bu karakter dizisinin bütün öğelerini değil de,
sadece belli karakterlerini almak istersek, karakter dizisindeki öğelerin sahip
olduğu bu sıradan yararlanacağız.

Diyelim ki `"Python"` karakter dizisinin ilk karakterini almak istiyoruz. Yani
biz bu karakter dizisinin sadece `"P"` harfine ulaşmayı amaçlıyoruz.

Bu isteğimizi nasıl yerine getirebileceğimizi basit bir örnek üzerinde
göstermeye çalışalım::

    >>> kardiz = "Python"

Burada değeri `"Python"` olan `kardiz` adlı bir değişken tanımladık. Şimdi bu
karakter dizisinin ilk öğesine erişeceğiz::
    
    >>> kardiz[0]

    'P'

Burada yaptığımız işleme çok dikkat edin. Karakter dizisinin istediğimiz bir
öğesine ulaşmak için, ilgili öğenin sırasını köşeli parantezler içinde
belirttik. Biz bu örnekte karakter dizisinin ilk öğesine ulaşmak istediğimiz
için köşeli parantez içinde `0` sayısını kullandık.

Şimdi de, ilk verdiğimiz örnekteki `nesne` değişkeni içinde yer alan sayılar
arasından sadece birini `2` ile çarpmak istediğimizi düşünelim::

    >>> nesne = "123456789"
    >>> int(nesne[1]) * 2
    
    4

Burada da öncelikle `nesne` değişkeninin birinci sırasında yer alan öğeyi
(dikkat: sıfırıncı sırada yer alan öğeyi değil!) elde etmek için köşeli
parantezler içinde `1` sayısını kullandık. Daha sonra ``int()`` fonksiyonu
yardımıyla bu karakter dizisini tam sayıya çevirdik, ki bununla aritmetik işlem
yapabilelim... Son olarak da elimizdeki tam sayıyı `2` ile çarparak istediğimiz
sonuca ulaştık.

Elbette yukarıdaki kodları şöyle de yazabilirdik::

    >>> nesne = "123456789"
    >>> sayı = int(nesne[1])
    >>> sayı * 2
    
    4

Belki farkındasınız, belki de değilsiniz, ama aslında şu noktada karakter
dizilerinin çok önemli bir özelliği ile karşı karşıyayız. Gördüğünüz gibi,
yukarıda bahsettiğimiz sıra kavramı sayesinde Python'da karakter dizilerinin
bütün öğelerine tek tek ve herhangi bir sıra gözetmeksizin erişmemiz mümkün.
Mesela yukarıdaki ilk örnekte ``kardiz[0]`` gibi bir yapı kullanarak karakter
dizisinin sıfırıncı (yani ilk) öğesini, ``nesne[1]`` gibi bir yapı kullanarak da
karakter dizisinin birinci (yani aslında ikinci) öğesini alabildik.

Bu yapının mantığını kavramak için şu örnekleri dikkatlice inceleyin::

    >>> kardiz = "Python"
    
    >>> kardiz[0]
    
    'P'
    
    >>> kardiz[1]
    
    'y'
    
    >>> kardiz[3]
    
    'h'
    
    >>> kardiz[5]
    
    'n'
    
    >>> kardiz[2]
    
    't'
    
    >>> kardiz[4]
    
    'o'
    
    >>> nesne = "123456789"
    
    >>> nesne[0]
    
    '1'
    
    >>> nesne[1]
    
    '2'
    
    >>> nesne[2]
    
    '3'
    
    >>> nesne[3]
    
    '4'
    
    >>> nesne[4]
    
    '5'
    
    >>> nesne[5]
    
    '6'
    
    >>> nesne[6]
    
    '7'
    
    >>> nesne[7]
    
    '8'
    
    >>> nesne[8]
    
    '9'

Burada şöyle bir formül yazabiliriz::

    karakter_dizisi[öğe_sırası]

Bu formülü uygulayarak karakter dizilerinin her bir öğesine tek tek erişmemiz
mümkün. Burada çok önemli bir noktaya daha dikkatinizi çekmek isterim.
Yukarıdaki örneklerden de gördüğünüz gibi, Python'da öğe sıralaması `0`'dan
başlıyor. Yani bir karakter dizisinin ilk öğesinin sırası `0` oluyor. Python
programlama dilini özellikle yeni öğrenenlerin en sık yaptığı hatalardan biri de
bir karakter dizisinin ilk öğesine ulaşmak için `1` sayısını kullanmalarıdır.
Asla unutmayın, Python saymaya her zaman `0`'dan başlar. Dolayısıyla bir
karakter dizisinin ilk öğesinin sırası `0`'dır. Eğer ilk öğeye ulaşayım derken
`1` sayısını kullanırsanız ulaştığınız öğe ilk öğe değil, ikinci öğe olacaktır.
Bu ayrıntıyı gözden kaçırmamaya dikkat etmelisiniz.
   
Karakter dizilerinin öğelerine tek tek erişirken dikkat etmemiz gereken önemli
noktalardan biri de, öğe sırası belirtirken, karakter dizisinin toplam uzunluğu
dışına çıkmamaktır. Yani mesela `7` karakterlik bir karakter dizimiz varsa, bu
karakter dizisinin son öğesinin sırası `6` olacaktır. Çünkü biliyorsunuz, Python
saymaya `0`'dan başlıyor. Dolayısıyla ilk karakterin sırası `0` olacağı için,
`7` karakterlik bir karakter dizisinde son öğenin sırası `6` olacaktır.
Örneğin::
    
    >>> kardiz = "istihza"
    >>> len(kardiz)
    
    7

Gördüğünüz gibi, `"istihza"` adlı karakter dizisinin uzunluğu `7`. Yani bu
karakter dizisi içinde `7` adet karakter var. Bu karakter dizisini incelemeye
devam edelim::
    
    >>> kardiz[0]
    
    'i'

Dediğimiz gibi, karakter dizisinin ilk öğesinin sırası `0`. Dolayısıyla son
öğenin sırası `6` olacaktır::
    
    >>> kardiz[6]
    
    'a'

Bu durumu şöyle formüle edebiliriz::

    >>> kardiz[len(kardiz)-1]

Yani;

    Bir karakter dizisinin uzunluğunun `1` eksiği, o karakter dizisinin son
    öğesini verir.
    
Yukarıdaki formülü eğer şöyle yazsaydık hata alırdık::

    >>> kardiz[len(kardiz)]

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range

Çünkü ``len(kardiz)`` kodu bize karakter dizisinin uzunluğunu veriyor. Yani
yukarıdaki `"istihza"` karakter dizisini göz önüne alırsak, ``len(kardiz)``
çıktısı `7` olacaktır. Dolayısıyla `"istihza"` karakter dizisinin son öğesine
ulaşmak istersek bu değerin 1 eksiğini almamız gerekiyor. Yani
``len(kardiz)-1``.

Şu ana kadar öğe sırası olarak hep artı değerli sayılar kullandık. Ancak
istersek öğe sırası olarak eksi değerli sayıları da kullanabiliriz. Eğer bir
karakter dizisine öğe sırası olarak eksi değerli bir sayı verirsek Python o
karakter dizisini sondan başa doğru okumaya başlayacaktır. Yani::
    
    >>> kardiz[-1]
    
    'a'

Gördüğünüz gibi `-1` sayısı karakter dizisini tersten okuyup, sondan başa doğru
ilk öğeyi veriyor. Dolayısıyla, yukarıda anlattığımız ``len(kardiz)-1``
yönteminin yanısıra, `-1` sayısını kullanarak da karakter dizilerinin son
karakterini elde edebiliyoruz. Bir de şuna bakalım::
    
    >>> kardiz[-2]
    
    'z'

Dediğimiz gibi, eksi değerli sayılar karakter dizisindeki karakterleri sondan
başa doğru elde etmemizi sağlar. Dolayısıyla `-2` sayısı, karakter dizisinde
sondan bir önceki karakteri verecektir.

Karakter dizilerinin öğelerine tek tek erişmek amacıyla öğe sırası belirtirken,
karakter dizisinin toplam uzunluğu dışına çıkmamamız gerektiğini söylemiştik.
Peki karakter dizisinin uzunluğunu aşan bir sayı verirsek ne olur? Ne olacağını
yukarıdaki örneklerden birinde görmüştük aslında. Ama konunun öneminden dolayı
bir kez daha tekrar edelim.

::

    >>> kardiz = "istihza"
    >>> kardiz[7]
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range
    
...veya::

    >>> kardiz[-8]
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: string index out of range

Eğer karakter dizisinin uzunluğunu aşan bir sayı belirtirsek Python bize
``IndexError`` türünde bir hata mesajı verecektir.

Gördüğünüz gibi, ``kardiz[0]``, ``kardiz[1]``, ``kardiz[2]``, vb. komutlarla
karakter dizisinin öğelerine erişebiliyoruz. Burada öğe sıralarını tek tek
yazmak yerine ``range()`` fonksiyonunu kullanarak da öğelere tek tek
erişebilirsiniz::
    
    for i in range(7):
        print(kardiz[i])

Bu kodlarda, ``kardiz[0]``, ``kardiz[1]``, ``kardiz[2]`` şeklinde öğe sıralarını
tek tek elle yazmak yerine, ``range(7)`` aralığındaki sayıları bir `for`
döngüsüne alıyoruz. Böylece Python ``kardiz[öğe_sırası]`` gibi bir yapı içinde
`öğe_sırası` yerine ``range(7)`` aralığındaki bütün sayıları (yani `0`, `1`,
`2`, `3`, `4`, `5`, `6` sayılarını) tek tek uyguluyor.

Burada aklınıza hemen şöyle bir soru gelmiş olabilir: 

    Biz kendi tanımladığımız karakter dizisinin uzunluğunun toplam `7` karakter
    olduğunu bildiğimiz için yukarıdaki örnekte ``range()`` fonksiyonunu
    ``range(7)`` şeklinde kullanabildik. Ama başka kaynaktan gelen bir karakter
    dizisinin uzunluğunu nasıl bileceğiz?
    
Aslında bu sorunun cevabı çok basit. Uzunluğunu bilmediğiniz karakter dizileri
için ``range()`` fonksiyonuyla birlikte ``len()`` fonksiyonundan
yararlanabilirsiniz. Nasıl mı? Hemen bir örnek verelim::
    
    for karakter in range(len(kardiz)):
        print(kardiz[karakter])

Burada ``range()`` fonksiyonuna verdiğimiz `len(kardiz)` parametresine
dikkatlice bakın. Biz `kardiz` adlı değişkenin tuttuğu karakter dizisinin `7`
karakterden oluştuğunu biliyoruz. Ama eğer bu karakter dizisini biz
belirlememişsek, karakter dizisinin tam olarak kaç karakterden oluşacağını
bilemeyiz. Bu kodlarda ``len(kardiz)`` ifadesini kullanarak, sabit bir değer
belirlemekten kaçınmış oluyoruz. Böylece, mesela kullanıcıdan aldığımız bir
karakter dizisinin kaç karakterden oluştuğunu belirleme görevini Python'a
bırakmış oluyoruz. Karakter dizisinin uzunluğu ne ise (``len(kardiz)``), Python
``range()`` fonksiyonuna o sayıyı parametre olarak kendisi atayacaktır.

Yukarıdaki durumu daha iyi anlayabilmek için bir örnek daha verelim. Diyelim ki
kullanıcıya ismini sorup, kendisine şöyle bir çıktı vermek istiyorsunuz::
    
    isminizin 1. harfi ...
    isminizin 2. harfi ...
    isminizin 3. harfi ...
    ...

Bunu yapabilmek için şöyle bir uygulama yazabilirsiniz::

    isim = input("isminiz: ")

    for i in range(len(isim)):
        print("isminizin {}. harfi: {}".format(i, isim[i]))

Gördüğünüz gibi, kullanıcının girdiği kelimenin uzunluğu kaç ise o sayı otomatik
olarak ``range()`` fonksiyonuna atanıyor. Diyelim ki kullanıcı Ferhat ismini
girmiş olsun. Bu kelimede toplam `6` karakter var. Dolayısıyla Python ``for``
satırını şöyle yorumlayacaktır::
    
    for i in range(6):
        ...

Python ``for`` döngüsünün ilk turunda şöyle bir işlem gerçekleştirir::

    print("isminizin {}. harfi: {}".format(0, isim[0]))

İkinci turda ise şöyle bir işlem::

    print("isminizin {}. harfi: {}".format(1, isim[1]))
    
.. figure:: ../images/misc/string_index.png
   :target: _images/string_index.png
   :align: right
   :figwidth: 300px
   :width: 300px
   :height: 159px
   
   Annenizin kızlık soyadının 0. harfi [`kaynak <http://pic.twitter.com/u1IE6Mma>`_]     

Bu döngü `6` sayısına gelene kadar devam eder. Burada `i` adlı değişkenin
değerinin her döngüde nasıl değiştiğine dikkat edin. Python `i` adını verdiğimiz
değişkene, ``for`` döngüsünün her turunda sırasıya `0`, `1`, `2`, `3`, `4` ve
`5` sayılarını atayacağı için `isim` adlı değişkenin öğeleri
``isim[öğe_sırası]`` formülü sayesinde tek tek ekrana dökülecektir.

Yalnız bu kodların çıktısında iki nokta dikkatinizi çekmiş olmalı. Birincisi,
`isminizin 0. harfi f` gibi bir çıktıyı kullanıcılarınız yadırgayabilir. Çünkü
'`0.` harf' çok yapay duran bir ifade. Onun yerine ilk harfi '1. harf' olarak
adlandırmamız çok daha mantıklı olacaktır. Bunun için kodlarınıza şu basit
eklemeyi yapabilirsiniz::
    
    isim = input("isminiz: ")

    for i in range(len(isim)):
        print("isminizin {}. harfi: {}".format(i+1, isim[i]))

Burada ilk `i` değişkeninin değerini `1` sayı artırdık. Böylece `0` sayısı
`1`'e, `1` sayısı `2`'ye, `2` sayısı `3`'e... dönüşmüş oldu. Bu şekilde
kullanıcılarınıza çok daha doğal görünen bir çıktı verebilmiş oluyorsunuz. Eğer
bu işlemi yapmazsanız, kullanıcılarınızın 'doğal görünmeyen' bir çıktı
almalarının yanısıra, programınızın verdiği çıktı kimi durumlarda epey yanıltıcı
da olabilir...


Karakter Dizilerini Dilimlemek
*******************************

Bir önceki bölümde bir karakter dizisinin istediğimiz öğesini, o öğenin sırasını
belirterek nasıl elde edebileceğimizi gördük. Bu bölümde de benzer bir şey
yapacağız. Ama burada yapacağımız şey, bir önceki bölümde yaptığımız işleme göre
biraz daha kapsamlı bir işlem olacak.

Bu bölümde karakter dizilerini 'dilimlemekten' söz edeceğiz. Peki 'dilimlemek'
derken neyi kastediyoruz? Aslında burada gerçek anlamda 'karpuz gibi
dilimlemekten' söz ediyoruz... Şu örnek, ne demek istediğimizi daha net ortaya
koyacaktır::
    
    >>> site = "www.istihza.com"
    >>> site[4:11]
    
    'istihza'
    
    >>> site[12:16]
    
    'com'
    
    >>> site[0:3]
    
    'www'

Gördüğünüz gibi, karakter dizisine köşeli parantez içinde bazı değerler vererek
bu karakter dizisini dilim dilim ayırdık. Peki bunu nasıl yaptık? Yukarıdaki
örneklerde şöyle bir yapı gözümüze çarpıyor::
    
    karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası]

Bu formülü çok basit bir örneğe uygulayalım::

    >>> karakter_dizisi = "istanbul"
    >>> karakter_dizisi[0:3]
    
    'ist'

Burada alacağımız ilk öğenin sıra numarası `0`. Yani `"istanbul"` karakter
dizisindeki 'i' harfi. Alacağımız son öğenin sıra numarasının 1 fazlası ise `3`.
Yani `2.` sıradaki 't' harfi. İşte ``karakter_dizisi[0:3]`` dediğimizde, Python
`0.` öğe ile `3.` öğe arasında kalan bütün öğeleri bize verecektir. Bizim
örneğimizde bu aralıktaki öğeler 'i', 's' ve 't' harfleri. Dolayısıyla Python
bize 'istanbul' kelimesindeki 'ist' kısmını dilimleyip veriyor.

Bu bilgileri kullanarak şöyle bir uygulama yazalım::

    site1 = "www.google.com"
    site2 = "www.istihza.com"
    site3 = "www.yahoo.com"
    site4 = "www.gnu.org"

    for isim in site1, site2, site3, site4:
        print("site: ", isim[4:-4])

Bu örnek Python'da dilimleme işlemlerinin yapısı ve özellikleri hakkında bize
epey bilgi veriyor. Gördüğünüz gibi, hem artı hem de eksi değerli sayıları
kullanabiliyoruz. Önceki bölümden hatırlayacağınız gibi, eğer verilen sayı eksi
değerliyse Python karakter dizisini sağdan sola (yani sondan başa doğru)
okuyacaktır. Yukarıdaki örnekte ``isim[4:-4]`` yapısını kullanarak, `site1`,
`site2`, `site3`, `site4` adlı karakter dizilerini, ilk dört ve son dört
karakterler hariç olacak şekilde dilimledik. Böylece elimizde ilk dört ve son
dört karakter arasındaki bütün karakterler kalmış oldu. Yani `"google"`,
`"istihza"`, `"yahoo"` ve `"gnu"`.

Bütün bu anlattıklarımızı daha iyi anlayabilmek için bir örnek daha verelim::

    ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
    ata2 = "Ağa güçlü olunca  kul suçlu olur!"
    ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
    ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
    ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

Burada beş adet atasözü verdik. Bizim görevimiz, bu atasözlerinin sonunda
bulunan ünlem işaretlerini ortadan kaldırmak::
    
    for ata in ata1, ata2, ata3, ata4, ata5:
        print(ata[0:-1])

Burada yaptığımız şey şu: `ata1`, `ata2`, `ata3`, `ata4` ve `ata5` adlı
değişkenlerin her birini `ata` olarak adlandırdıktan sonra `ata` adlı değişkenin
en başından en sonuna kadar olan kısmı dilimleyip aldık. Yani ``ata[0]`` ile
``ata[-1]`` arasında kalan bütün karakterleri elde etmiş olduk. Peki bu ünlem
işaretlerini kaldırdıktan sonra bunların yerine birer nokta koymak istersek ne
yapacağız?

O da çok basit bir işlem::

    for ata in ata1, ata2, ata3, ata4, ata5:
        print(ata[0:-1] + ".") 

Gördüğünüz gibi, son karakter olan ünlem işaretini attıktan sonra onun yerine
bir nokta işareti koymak için yaptığımız tek şey, dilimlediğimiz karakter
dizisine, artı işareti (`+`) yardımıyla bir `.` karakteri eklemekten ibarettir.

Böylece karakter dizilerini nasıl dilimleyeceğimizi öğrenmiş olduk. Bu konuyu
kapatmadan önce dilimlemeye ilişkin bazı ayrıntılardan söz edelim. Diyelim ki
elimizde şöyle bir karakter dizisi var::
    
    >>> kardiz = "Sana Gül Bahçesi Vadetmedim"

Bu karakter dizisi içinden sadece 'Sana' kısmını dilimlemek için şöyle bir şey
yazabileceğimizi biliyorsunuz::
    
    >>> kardiz[0:4]
    
    'Sana'

Burada `0.` karakterden `4.` karaktere kadar olan kısmı dilimlemiş oluyoruz.
Python bize bu tür durumlarda şöyle bir kolaylık sağlar: Eğer karakter dizisi
içinden alınan ilk karakterin sırasını gösteren sayı `0` ise, bu sayıyı
belirtmesek de olur. Yani ``kardiz[0:4]`` kodunu şöyle de yazabiliriz::
    
    >>> kardiz[:4]
    
    'Sana'

Gördüğünüz gibi, ilk sıra sayısını yazmazsak Python ilk sayıyı `0` kabul ediyor.

Şimdi de aynı karakter dizisi içindeki 'Vadetmedim' kısmını dilimlemeye
çalışalım::

    >>> kardiz[17:27]
    
    'Vadetmedim'

Burada da `17.` karakter ile `27.` karakter arasında kalan bütün karakterleri
dilimledik. Tıpkı, alacağımız ilk karakterin sırası `0` olduğunda bu sayıyı
belirtmemize gerek olmadığı gibi, alacağımız son karakterin sırası karakter
dizisinin sonuncu karakterine denk geliyorsa o sayıyı da yazmamıza gerek yok.
Yani yukarıdaki ``kardiz[17:27]`` kodunu şöyle de yazabiliriz::
    
    >>> kardiz[17:]
    
    'Vadetmedim'

Python'daki bu dilimleme özelliğini kullanarak karakter dizilerini istediğiniz
gibi eğip bükebilir, evirip çevirebilirsiniz.

Python'daki bu dilimleme yapısı ilk bakışta gözünüze biraz karmaşıkmış gibi
görünebilir. Ama aslında hiç de öyle değildir. Bu yapının mantığını bir kez
kavradıktan sonra kodlarınızı hatasız bir şekilde yazabilirsiniz.

Dilimleme yapısını daha iyi anlayabilmek için kendi kendinize bazı denemeler
yapmanızı tavsiye ederim. Bu yapının nasıl çalıştığını anlamanın en iyi yolu bol
bol örnek kod yazmaktır.

Karakter Dizilerini Ters Çevirmek
*********************************

Eğer amacınız bir karakter dizisini ters çevirmek, yani karakter dizisi içindeki
her bir öğeyi tersten yazdırmaksa biraz önce öğrendiğimiz dilimleme yöntemini
kullanabilirsiniz. Dikkatlice bakın::
    
    >>> kardiz[::-1]
    
    'midemtedaV iseçhaB lüG anaS'

Gördüğünüz gibi, `"Sana Gül Bahçesi Vadetmedim"` adlı karakter dizisi içindeki
bütün karakterler sondan başa doğru ekrana dizildi.

Aslında bu komutla Python'a şöyle bir emir vermiş oluyoruz: 

    `kardiz` değişkeni içindeki bütün karakterleri, en son karakterden ilk
    karaktere kadar sondan başa doğru tek tek ekrana yazdır!
    
Bildiğiniz gibi, eğer almak istediğimiz karakter, dizi içindeki ilk karakterse
bu karakterin dizi içindeki sırasını belirtmemize gerek yok. Aynı şekilde, eğer
almak istediğimiz karakter, dizi içindeki son karakterse, bu karakterin de dizi
içindeki sırasını belirtmemize gerek yok. İşte yukarıdaki örnekte bu kuraldan
yararlandık.

Eğer bir karakter dizisinin tamamının değil de, sadece belli bir kısmının ters
çevrilmiş halini elde etmek istiyorsanız elbette yapmanız gereken şey, almak
istediğiniz ilk ve son karakterlerin sırasını parantez içinde belirtmek
olacaktır. Mesela yukarıdaki karakter dizisinde sadece 'Gül' kelimesini ters
çevirmek istersek şöyle bir şey yazabiliriz::
    
    >>> kardiz[7:4:-1]

    'lüG'

Yukarıdaki örnek, karakter dizisi dilimlemeye ilişkin olarak bize bazı başka
ipuçları da veriyor. Gördüğünüz gibi, köşeli parantez içinde toplam üç adet
parametre kullanabiliyoruz. Yani formülümüz şöyle::
    
    kardiz[ilk_karakter:son_karakter:atlama_sayısı]

Bir örnek verelim::

    >>> kardiz = "istanbul"
    >>> kardiz[0:8:1]
    
    'istanbul'

Burada `"istanbul"` adlı karakter dizisinin bütün öğelerini birer birer ekrana
döktük. Bir de şuna bakalım::
    
    >>> kardiz[0:8:2]
    
    'itnu'

Burada ise `"istanbul"` adlı karakter dizisinin bütün öğelerini ikişer ikişer
atlayarak ekrana döktük. Yani bir karakter yazıp bir karakter atladık (**i**\ s\
**t**\ a\ **n**\ b\ **u**\l).

Python'ın kuralları gereğince yukarıdaki kodu şöyle yazabileceğimizi de
biliyorsunuz::

    >>> kardiz[::2]
    
    'itnu'

Eğer karakter dizisini ters çevirmek istiyorsak, yukarıdaki örneği eksi değerli
bir atlama sayısı ile yazmamız gerekir::
    
    >>> kardiz = "istanbul"
    >>> kardiz[::-1]
    
    'lubnatsi'
    
    >>> kardiz[::-2]
    
    'lbas'

Dediğimiz gibi, yukarıdaki yöntemi kullanarak karakter dizilerini ters
çevirebilirsiniz. Ama eğer isterseniz ``reversed()`` adlı bir fonksiyondan da
yararlanabiliriz.

Gelelim bu fonksiyonun nasıl kullanılacağına... Önce şöyle bir deneme yapalım::

    >>> reversed("Sana Gül Bahçesi Vadetmedim")

    <reversed object at 0x00E8E250>

Gördüğünüz gibi, bu fonksiyonu düz bir şekilde kullandığımızda bize bir
'reversed' nesnesi vermekle yetiniyor. Buna benzer bir olguyla ``range()``
fonksiyonunda da karşılaşmıştık::
    
    >>> range(10)
    
    range(0, 10)

Hatırlarsanız, ``range(10)`` gibi bir komutun içeriğini görebilmek için bu komut
üzerinde bir ``for`` döngüsü kurmamız gerekiyordu::
    
    for i in range(10):
        print(i)

...veya::

    print(*range(10))

Aynı durum ``reversed()`` fonksiyonu için de geçerlidir::

    for i in reversed("Sana Gül Bahçesi Vadetmedim"):
        print(i, end="")

...veya::

    print(*reversed("Sana Gül Bahçesi Vadetmedim"), sep="") 

Dilimleme veya ``reversed()`` fonksiyonunu kullanma yöntemlerinden hangisi
kolayınıza geliyorsa onu tercih edebilirsiniz.

Karakter Dizilerini Alfabe Sırasına Dizmek
******************************************

Python'da karakter dizilerinin öğelerine tek tek ulaşma, öğeleri dilimleme ve
ters çevirmenin yanısıra, bu öğeleri alfabe sırasına dizmek de mümkündür. Bunun
için ``sorted()`` adlı bir fonksiyondan yararlanacağız::
    
    >>> sorted("kitap")
    
    ['a', 'i', 'k', 'p', 't']

Nasıl ``input()`` fonksiyonu çıktı olarak bir karakter dizisi ve ``len()``
fonksiyonu bir sayı veriyorsa, ``sorted()`` fonksiyonu da bize çıktı olarak,
birkaç bölüm sonra inceleyeceğimiz 'liste' adlı bir veri tipi verir.

Ama tabii eğer isterseniz bu çıktıyı alıştığınız biçimde alabilirsiniz::

    print(*sorted("kitap"), sep="")

...veya::

    for i in sorted("kitap"):
        print(i, end="")

Bir örnek daha verelim::

    >>> sorted("elma")
    
    ['a', 'e', 'l', 'm']

Gördüğünüz gibi, ``sorted()`` fonksiyonunu kullanmak çok kolay, ama aslında bu
fonksiyonun önemli bir problemi var. Dikkatlice bakın::
    
    >>> sorted("çiçek")

    ['e', 'i', 'k', 'ç', 'ç']

Burada Türkçe bir karakter olan 'ç' harfinin düzgün sıralanamadığını görüyoruz.
Bu sorun bütün Türkçe karakterler için geçerlidir.

Bu sorunu aşmak için şöyle bir yöntem deneyebilirsiniz::

    >>> import locale
    >>> locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için
    >>> locale.setlocale(locale.LC_ALL, "tr_TR") #GNU/Linux için
    >>> sorted("çiçek", key=locale.strxfrm)
    
    ['ç', 'ç', 'e', 'i', 'k']

Burada ``locale`` adlı bir modülden yararlandık. ``locale`` de tıpkı ``sys``,
``os`` ve ``keyword`` gibi bir modül olup, içinde pek çok değişken ve fonksiyon
barındırır.

``locale`` modülü bize belli bir dilin kendine has özelliklerine göre
programlama yapma imkanı verir. Örneğin bu modülünün içinde yer alan
fonksiyonlardan biri olan ``setlocale()`` fonksiyonunu kullanarak, programımızda
öntanımlı dil ayarlarına uygun bir şekilde programlama yapma olanağı sağlarız.

Bu modülü ilerleyen derslerde daha ayrıntılı bir şekilde inceleyeceğiz. O yüzden
``locale`` modülünü bir kenara bırakıp yolumuza devam edelim.

Yukarıdaki örnekte Türkçe karakterleri doğru sıralayabilmek için ``sorted()``
fonksiyonunu nasıl kullandığımıza dikkat edin::

    >>> sorted("çiçek", key=locale.strxfrm)

Burada ``sorted()`` metodunun `key` adlı özel bir parametresine `locale.strxfrm`
değerini vererek Türkçeye duyarlı bir sıralama yapılmasını sağladık. Yukarıdaki
yöntem pek çok durumda işinize yarar. Ancak bu yöntem tek bir yerde işe yaramaz.
Dikkatlice bakın::

    >>> sorted("afgdhkıi", key=locale.strxfrm)
    
    ['a', 'd', 'f', 'g', 'h', 'i', 'ı', 'k']

Gördüğünüz gibi, bu yöntem 'i' harfini 'ı' harfinden önce getiriyor. Halbuki
Türk alfabesine göre bunun tersi olmalıydı. Buna benzer problemlerle İngiliz
alfabesi dışındaki pek çok alfabede karşılaşırsınız. Dolayısıyla bu sadece
Türkçeye özgü bir sorun değil. 

Bu soruna karşı şöyle bir kod da yazabilirsiniz::
    
    >>> harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    >>> çevrim = {i: harfler.index(i) for i in harfler}
    >>> sorted("afgdhkıi", key=çevrim.get)

    ['a', 'd', 'f', 'g', 'h', 'ı', 'i', 'k']

Gördüğünüz gibi burada ilk iş olarak Türk alfabesindeki bütün harfleri `harfler`
adlı bir değişkene atadık. Daha sonra ise şöyle bir kod yazdık::
    
    >>> çevrim = {i: harfler.index(i) for i in harfler}

Burada henüz öğrenmediğimiz bir yapı var, ama ne olup bittiğini daha iyi anlamak
için bu `çevrim` değişkeninin içeriğini kontrol etmeyi deneyebilirsiniz::
    
    >>> print(çevrim)

    {'ğ': 8, 'ı': 10, 'v': 26, 'g': 7, 'ş': 22, 'a': 0, 'c': 2, 'b': 1, 'e': 5, 
    'd': 4, 'ç': 3, 'f': 6, 'i': 11, 'h': 9, 'k': 13, 'j': 12, 'm': 15, 'l': 14, 
    'o': 17, 'n': 16, 'p': 19, 's': 21, 'r': 20, 'u': 24, 't': 23, 'ö': 18, 
    'y': 27, 'z': 28, 'ü': 25}

Bu çıktıya dikkatlice bakarsanız, her bir harfin bir sayıya karşılık gelecek
şekilde birbiriyle eşleştirildiğini göreceksiniz. Mesela 'ğ' harfi `8` ile, 'f'
harfi `6` ile eşleşmiş. Yine dikkatlice bakarsanız, biraz önce bize sorun
çıkaran 'ı' harfinin `10`, 'i' harfinin ise `11` ile eşleştiğini göreceksiniz.
Evet, doğru tahmin ettiniz. Harfleri sayılarla eşleştirerek, Python'ın harfler
yerine sayıları sıralamasını sağlayacağız. Bunu da yine `key` parametresini
kullanarak yapıyoruz::
    
    >>> sorted("afgdhkıi", key=çevrim.get)

Bu yapıyı daha iyi anlayabilmek için kendi kendinize bazı denemeler yapın. Eğer
burada olan biteni anlamakta zorlanıyorsanız hiç endişe etmeyin. Bir-iki bölüm
sonra bunları da kolayca anlayabilecek duruma geleceksiniz. Bizim burada bu
bilgileri vermekteki amacımız, Python'ın Türkçe harflerle sıralama işlemini
sorunsuz bir şekilde yapabileceğini göstermektir. Bu esnada bir-iki yeni bilgi
kırıntısı da kapmanızı sağlayabildiysek kendimizi başarılı sayacağız.

Karakter Dizileri Üzerinde Değişiklik Yapmak
*********************************************

Bu kısımda karakter dizilerinin çok önemli bir özelliğinden söz edeceğiz.
Konumuz karakter dizileri üzerinde değişiklik yapmak. İsterseniz neyle karşı
karşıya olduğumuzu anlayabilmek için çok basit bir örnek verelim.

Elimizde şöyle bir karakter dizisi olduğunu düşünün::

    >>> meyve = "elma"

Amacımız bu karakter dizisinin ilk harfini büyütmek olsun. 

Bunun için dilimleme yönteminden yararlanabileceğimizi biliyorsunuz::

    >>> "E" + meyve[1:]
    
    'Elma'

Burada "E" harfi ile, `meyve` değişkeninin ilk harfi dışında kalan bütün
harfleri birleştirdik.

Bir örnek daha verelim. 

Elimizde şöyle dört adet internet sitesi adresi olsun::

    site1 = "www.google.com"
    site2 = "www.istihza.com"
    site3 = "www.yahoo.com"
    site4 = "www.gnu.org"

Bizim amacımız bu adreslerin her birinin baş tarafına `http://` ifadesini
eklemek. Bunun için de yine karakter dizisi birleştirme işlemlerinden
yararlanabiliriz. Dikkatlice inceleyin::
    
    site1 = "www.google.com"
    site2 = "www.istihza.com"
    site3 = "www.yahoo.com"
    site4 = "www.gnu.org"

    for i in site1, site2, site3, site4:
        print("http://", i, sep="")

Eğer `www.` kısımlarını atmak isterseniz karakter dizisi birleştirme işlemleri
ile birlikte dilimleme yöntemini de kullanmanız gerekir::
    
    for i in site1, site2, site3, site4:
        print("http://", i[4:], sep="")

Belki farkındayız, belki de değiliz, ama aslında yukarıdaki örnekler karakter
dizileri hakkında bize çok önemli bir bilgi veriyor. Dikkat ettiyseniz
yukarıdaki örneklerde karakter dizileri üzerinde bir değişiklik yapmışız gibi
görünüyor. Esasında öyle de denebilir. Ancak burada önemli bir ayrıntı var.
Yukarıdaki örneklerde gördüğümüz değişiklikler kalıcı değildir. Yani aslında bu
değişikliklerin orijinal karakter dizisi üzerinde hiçbir etkisi yoktur. Gelin
isterseniz bunu teyit edelim::
    
    >>> kardiz = "istihza"
    >>> "İ" + kardiz[1:]
    
    'İstihza'

Dediğimiz gibi, sanki burada `"istihza"` karakter dizisini `"İstihza"` karakter
dizisine çevirmişiz gibi duruyor. Ama aslında öyle değil::
    
    >>> print(kardiz)
    
    istihza
    
Gördüğünüz gibi, `kardiz` değişkeninin orijinalinde hiçbir değişiklik yok.
Ayrıca burada ``"İ" + kardiz[1:]`` satırı ile elde ettiğiniz sonuca tekrar
ulaşmanızın imkanı yok. Bu değişiklik kaybolmuş durumda. Peki bunun sebebi
nedir?

Bunun nedeni, karakter dizilerinin değiştirilemeyen (*immutable*) bir veri tipi
olmasıdır. Python'da iki tür veri tipi bulunur: değiştirilemeyen veri tipleri
(*immutable datatypes*) ve değiştirilebilen veri tipleri (*mutable datatypes*).
Bizim şimdiye kadar gördüğümüz veri tipleri (sayılar ve karakter dizileri),
değiştirilemeyen veri tipleridir. Henüz değiştirilebilen bir veri tipi görmedik.
Ama birkaç bölüm sonra değiştirilebilen veri tiplerini de inceleyeceğiz.

Neyse... Dediğimiz gibi, karakter dizileri üzerinde yaptığımız değişikliklerin
kalıcı olmamasını nedeni, karakter dizilerinin değiştirilemeyen bir veri tipi
olmasıdır. Python'da bir karakter dizisini bir kez tanımladıktan sonra bu
karakter dizisi üzerinde artık değişiklik yapamazsınız. Eğer bir karakter dizisi
üzerinde değişiklik yapmanız gerekiyorsa, yapabileceğiniz tek şey o karakter
dizisini yeniden tanımlamaktır. Mesela yukarıdaki örnekte `kardiz` değişkeninin
tuttuğu karakter dizisini değiştirmek isterseniz şöyle bir kod yazabilirsiniz::
    
    >>> kardiz = "İ" + kardiz[1:]
    >>> print(kardiz)

    İstihza

Burada yaptığımız şey `kardiz` değişkeninin değerini değiştirmek değildir. Biz
burada aslında bambaşka bir `kardiz` değişkeni daha tanımlıyoruz. Yani ilk
`kardiz` değişkeni ile sonraki `kardiz` değişkeni aynı şeyler değil. Bunu teyit
etmek için önceki derslerimizde gördüğümüz ``id()`` fonksiyonundan
yararlanabilirsiniz::
    
    >>> kardiz = "istihza"
    >>> id(kardiz)
    
    3075853248
    
    >>> kardiz = "İ" + kardiz[1:]
    >>> id(kardiz)
    
    3075853280

Gördüğünüz gibi, ilk `kardiz` değişkeni ile sonraki `kardiz` değişkeni farklı
kimlik numaralarına sahip. Yani bu iki değişken bellek içinde farklı adreslerde
tutuluyor. Daha doğrusu, ikinci `kardiz`, ilk `kardiz`'i silip üzerine yazıyor.

Her ne kadar ``kardiz = "İ" + kardiz[1:]`` kodu `kardiz`'in değerini aslında
değiştirmiyor olsa da, sanki `kardiz` değişkeninin tuttuğu karakter dizisi
değişiyormuş gibi bir etki elde ediyoruz. Bu da bizi memnun etmeye yetiyor...

Yukarıdaki örnekte karakter dizisinin baş kısmı üzerinde değişiklik yaptık. Eğer
karakter dizisinin ortasında kalan bir kısmı değiştirmek isterseniz de şöyle bir
şey yazabilirsiniz::
    
    >>> kardiz = "istihza"
    >>> kardiz = kardiz[:3] + "İH" + kardiz[5:]
    >>> kardiz
    
    'istİHza'

Gördüğünüz gibi, yukarıdaki kodlarda karakter dizilerini dilimleyip
birleştirerek, yani bir bakıma kesip biçerek istediğimiz çıktıyı elde ettik.

Mesela ilk örnekte `kardiz` değişkeninin ilk karakteri dışında kalan kısmını
(``kardiz[1:]``) "İ" harfi ile birleştirdik (``"İ" + kardiz[1:]"``).

İkinci örnekte ise `kardiz` değişkeninin ilk üç karakterine "İH" ifadesini
ekledik ve sonra buna `kardiz` değişkeninin `5.` karakterinden sonraki kısmını
ilave ettik.

Karakter dizileri üzerinde değişiklik yapmanızın hangi durumlarda gerekli
olacağını gösteren bir örnek daha verip bu konuyu kapatalım.

Diyelim ki, bir kelime içindeki sesli ve sessiz harfleri birbirinden ayırmanız
gereken bir program yazıyorsunuz. Yani mesela amacınız 'istanbul' kelimesi
içinde geçen 'i', 'a' ve 'u' harflerini bir yerde, 's', 't', 'n', 'b' ve 'l'
harflerini ise ayrı bir yerde toplamak. Bunun için şöyle bir program
yazabilirsiniz::
    
    sesli_harfler = "aeıioöuü"
    sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
    
    sesliler = ""
    sessizler = ""
    
    kelime = "istanbul"
    
    for i in kelime:
        if i in sesli_harfler:
            sesliler += i
        else:
            sessizler += i

    print("sesli harfler: ", sesliler)
    print("sessiz harfler: ", sessizler)

Burada öncelikle şu kodlar yardımıyla Türkçedeki sesli ve sessiz harfleri
belirliyoruz::
    
    sesli_harfler = "aeıioöuü"
    sessiz_harfler = "bcçdfgğhjklmnprsştvyz" 

Ardından da, sesli ve sessiz harflerini ayıklayacağımız kelimedeki sesli harfler
ve sessiz harfler için boş birer karakter dizisi tanımlıyoruz::
    
    sesliler = ""
    sessizler = ""
    
Programımız içinde ilgili harfleri, o harfin ait olduğu değişkene atayacağız. 

Kelimemiz `"istanbul"`::

    kelime = "istanbul"

Şimdi bu kelime üzerinde bir ``for`` döngüsü kuruyoruz ve kelime içinde geçen
herbir harfe tek tek bakıyoruz. Kelime içinde geçen harflerden, `sesli_harfler`
değişkeninde tanımlı karakter dizisinde geçenleri `sesliler` adlı değişkene
atıyoruz. Aksi durumda ise, yani kelime içinde geçen harflerden,
`sessiz_harfler` değişkeninde tanımlı karakter dizisinde geçenleri, `sessizler`
adlı değişkene gönderiyoruz::

    for i in kelime:
        if i in sesli_harfler:
            sesliler += i
        else:
            sessizler += i

Bunun için ``for`` döngüsü içinde basit bir 'if-else' bloğu tanımladığımızı
görüyorsunuz. Ayrıca bunu yaparken, `sesliler` ve `sessizler` adlı değişkenlere,
``for`` döngüsünün her bir dönüşünde yeni bir harf gönderip, bu değişkenleri,
döngünün her dönüşünde yeni baştan tanımladığımıza dikkat edin. Çünkü, dediğimiz
gibi, karakter dizileri değiştirilemeyen veri tipleridir. Bir karakter dizisi
üzerinde değişiklik yapmak istiyorsak, o karakter dizisini baştan tanımlamamız
gerekir.

Üç Önemli Fonksiyon
*******************

Karakter dizilerinin temel özellikleri hakkında söyleyeceklerimizin sonuna
geldik sayılır. Biraz sonra karakter dizilerinin çok önemli bir parçası olan
metotlardan söz edeceğiz. Ama isterseniz metotlara geçmeden önce, çok önemli üç
fonksiyondan söz edelim. Bu fonksiyonlar sadece karakter dizileri ile değil,
başka veri tipleri ile çalışırken de işlerimizi bir hayli kolaylaştıracak.

dir()
=========

İlk olarak ``dir()`` adlı özel bir fonksiyondan söz edeceğiz. Bu metot bize
Python'daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek.
Mesela karakter dizilerinin bize hangi metotları sunduğunu görmek için bu
fonksiyonu şöyle kullanabiliriz::
    
    >>> dir(str)
    
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

İngilizcede 'karakter dizisi'nin karşılığının *string*, bu kelimenin
kısaltmasının da 'str' olduğunu hatırlıyor olmalısınız. İşte ``dir()``
fonksiyonuna parametre olarak bu 'str' kelimesini verdiğimizde, Python bize
karakter dizilerinin bütün metotlarını listeliyor.

Karakter dizileri dışında, şimdiye kadar öğrendiğimiz başka bir veri tipi de
sayılar. Biz Python'da sayıların tam sayılar (*integer*), kayan noktalı sayılar
(*float*) ve karmaşık sayılar (*complex*) olarak üçe ayrıldığını da biliyoruz.
Örnek olması açısından ``dir()`` fonksiyonunu bir de sırasıyla, tam sayılar,
kayan noktalı sayılar ve karmaşık sayılar üzerinde de uygulayalım::
    
    >>> dir(int)    
    
    >>> dir(float)

    >>> dir(complex)
   
Gördüğünüz gibi, ``dir()`` fonksiyonunu kullanmak için, metotlarını listelemek
istediğimiz nesneyi alıp ``dir()`` fonksiyonuna parametre olarak veriyoruz.
Örneğin yukarıda karakter dizileri için `str`; tam sayılar için `int`; kayan
noktalı sayılar için `float`; karmaşık sayılar için ise `complex`
parametrelerini kullandık.

``dir()`` fonksiyonunu kullanabilmek için tek yöntemimiz, sorgulamak istediğimiz
nesnenin adını kullanmak değil. Mesela karakter dizilerinin metotlarını
sorgulamak için 'str' kelimesini kullanabileceğimiz gibi, herhangi bir karakter
dizisini de kullanabiliriz. Yani::
    
    >>> dir("")

Burada ``dir()`` fonksiyonuna parametre olarak boş bir karakter dizisi verdik.
Bu kodun ``dir(str)`` kodundan hiçbir farkı yoktur. Bu komut da bize karakter
dizilerinin metotlarını listeler.

Aynı etkiyi dilersek şöyle de elde edebiliriz::

    >>> a = "karakter"
    >>> dir(a)
    
Karakter dizilerinin metotlarını listelemek için, siz hangi yöntem kolayınıza
geliyorsa onu kullanabilirsiniz. Bu satırların yazarı genellikle şu yöntemi
kullanıyor::
    
    >>> dir("")

``dir("")`` komutunun çıktısından da göreceğiniz gibi, karakter dizilerinin epey
metodu var. Metot listesi içinde bizi ilgilendirenler başında veya sonunda `_`
işareti olmayanlar. Yani şunlar::
    
    >>> for i in dir(""):
    ...     if "_" not in i[0]:
    ...         print(i)
    ...

Bu arada bu metotları listelemek için nasıl bir kod kullandığımıza dikkat edin::
    
    for i in dir(""):
        if "_" not in i[0]:
            print(i)

Burada ``dir("")`` komutunun içerdiği her bir metoda tek tek bakıyoruz. Bu
metotlar içinde, ilk harfi `_` karakteri olmayan bütün metotları listeliyoruz.
Böylece istediğimiz listeyi elde etmiş oluyoruz. İsterseniz ilgilendiğimiz
metotların sayısını da çıktıya ekleyebiliriz::
    
    sayaç = 0

    for i in dir(""):
        if "_" not in i[0]:
            sayaç += 1
            print(i)
        
    print("Toplam {} adet metot ile ilgileniyoruz.".format(sayaç))

Burada da, ilk karakteri `_` olmayan her bir metot için `sayaç` değişkeninin
değerini `1` artırıyoruz. Böylece programın sonunda `sayaç` değişkeni
ilgilendiğimiz metot sayısını göstermiş oluyor.

Eğer her metodun soluna, sıra numarasını da eklemek isterseniz elbette şöyle bir
kod da yazabilirsiniz::

    sayaç = 0

    for i in dir(""):
        if "_" not in i[0]:
            sayaç += 1
            print(sayaç, i)

    print("Toplam {} adet metot ile ilgileniyoruz.".format(sayaç))

Bu noktada bir parantez açalım. Yukarıdaki yöntemi kullanarak metotları
numaralandırabilirsiniz. Ama aslında Python bize numaralandırma işlemleri için
özel bir fonksiyon sunar. Şimdi isterseniz bu özel fonksiyonu inceleyelim.

enumerate()
===============

Eğer yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız
gerekiyorsa Python'ın size sunduğu çok özel bir fonksiyondan
yararlanabilirsiniz. Bu fonksiyonun adı ``enumerate()``.

Gelelim bu fonksiyonun nasıl kullanılacağına... Önce şöyle bir deneme yapalım::

    >>> enumerate("istihza")
    
    <enumerate object at 0x00E3BC88>

Tıpkı ``reversed()`` fonksiyonunun bir 'reversed' nesnesi vermesi gibi, bu
fonksiyonun da bize yalnızca bir 'enumerate' nesnesi verdiğini görüyorsunuz.

``reversed()`` fonksiyonunu kullanabilmek için şöyle bir kod yazmıştık::

    >>> print(*reversed("istihza"))

``enumerate()`` için de benzer bir şeyi deneyebiliriz::

    >>> print(*enumerate("istihza"))

Burada şu çıktıyı aldık::

    (0, 'i') (1, 's') (2, 't') (3, 'i') (4, 'h') (5, 'z') (6, 'a')

*Enumerate* kelimesi İngilizcede 'numaralamak, numaralandırmak' gibi anlamlara
gelir. Dolayısıyla ``enumerate()`` fonksiyonu, kendisine parametre olarak
verilen değer hakkında bize iki farklı bilgi verir: Bir öğe ve bu öğeye ait bir
sıra numarası. Yukarıdaki çıktıda gördüğünüz şey de işte her bir öğenin kendisi
ve o öğeye ait bir sıra numarasıdır.

Yukarıdaki çıktıyı daha iyi anlayabilmek için bir ``for`` döngüsü kullanmak daha
açıklayıcı olabilir::

    >>> for i in enumerate("istihza"):
    ...     print(i)
    ...
    (0, 'i')
    (1, 's')
    (2, 't')
    (3, 'i')
    (4, 'h')
    (5, 'z')
    (6, 'a')

Gördüğünüz gibi, gerçekten de bu fonksiyon bize bir öğe (mesela 'i' harfi) ve bu
öğeye ait bir sıra numarası (mesela `0`) veriyor.

Hatırlarsanız, ``enumerate()`` fonksiyonunu öğrenmeden önce, ``dir("")``
komutundan elde ettiğimiz çıktıları şu şekilde numaralandırabileceğimizi
söylemiştik::
    
    sayaç = 0

    for i in dir(""):
        if "_" not in i[0]:
            sayaç += 1
            print(sayaç, i)

Ama artık ``enumerate()`` fonksiyonunu öğrendiğimize göre, aynı işi çok daha
verimli bir şekilde gerçekleştirebiliriz::
    
    for sıra, metot in enumerate(dir("")):
        print(sıra, metot)

``enumerate()`` metodunun verdiği her bir çıktının iki öğeli olduğunu biliyoruz
(öğenin kendisi ve o öğenin sıra numarası). Yukarıdaki kodlar yardımıyla, bu
öğelerin her birini ayrı bir değişkene (`sıra` ve `metot`) atamış oluyoruz.
Böylece bu çıktıyı manipüle etmek bizim için daha kolay oluyor. Mesela bu
özelliği kullanarak metot ve sıra numarasının yerlerini değiştirebiliriz::
    
    >>> for sıra, metot in enumerate(dir("")):
    ...     print(metot, sıra)
    ...
    __add__ 0
    __class__ 1
    __contains__ 2
    __delattr__ 3
    __doc__ 4
    __eq__ 5
    __format__ 6
    __ge__ 7
    
    (...)

Pratik olması açısından şöyle bir örnek daha verelim::

    >>> for sıra, metot in enumerate(dir("")):
    ...     print(sıra, metot, len(metot))
    ...
    0 __add__ 7
    1 __class__ 9
    2 __contains__ 12
    3 __delattr__ 11
    4 __doc__ 7
    5 __eq__ 6
    
    (...)

Burada, ``dir("")`` ile elde ettiğimiz metotların sırasını (`sıra`), bu
metotların adlarını (`metot`) ve her bir metodun kaç karakterden oluştuğunu
(``len(metot)``) gösteren bir çıktı elde ettik.

Bu arada, gördüğünüz gibi, ``enumerate()`` fonksiyonu numaralandırmaya `0`'dan
başlıyor. Elbette eğer isterseniz bu fonksiyonun numaralandırmaya kaçtan
başlayacağını kendiniz de belirleyebilirsiniz. Dikkatlice bakın::
    
    >>> for sıra, harf in enumerate("istihza", 1):
    ...     print(sıra, harf)
    ...
    1 i
    2 s
    3 t
    4 i
    5 h
    6 z
    7 a

Burada 'istihza' kelimesi içindeki harfleri numaralandırdık. Bunu yaparken de
numaralandırmaya `1`'den başladık. Bunun için ``enumerate()`` fonksiyonuna
ikinci bir parametre verdiğimize dikkat edin.

``enumerate()`` fonksiyonunu da incelediğimize göre önemli bir başka
fonksiyondan daha söz edebiliriz.

help()
============

Python'la ilgili herhangi bir konuda yardıma ihtiyacınız olduğunda, internetten
araştırma yaparak pek çok ayrıntılı belgeye ulaşabilirsiniz. Ama eğer herhangi
bir nesne hakkında hızlı bir şekilde ve İngilizce olarak yardım almak isterseniz
``help()`` adlı özel bir fonksiyondan yararlanabilirsiniz.

Bu fonksiyonu iki farklı şekilde kullanıyoruz. Birinci yöntemde, etkileşimli
kabuğa ``help()`` yazıp `Enter` düğmesine basıyoruz::

    >>> help()

    Welcome to Python 3.3!  This is the interactive help utility.
    
    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/3.3/tutorial/.
    
    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".
    
    To get a list of available modules, keywords, or topics, type "modules",
    "keywords", or "topics".  Each module also comes with a one-line summary
    of what it does; to list the modules whose summaries contain a given word
    such as "spam", type "modules spam".

    help>

.. highlight:: none

Gördüğünüz gibi, Python bu komutu verdiğimizde özel bir yardım ekranı açıyor
bize. Bu ekranda `>>>` yerine `help>` ifadesinin olduğuna dikkat edin. Mesela
``dir()`` fonksiyonu hakkında bilgi almak için `help>` ifadesinden hemen sonra,
hiç boşluk bırakmadan, şu komutu verebiliriz::
    
    help> dir

Bu komut bize şu çıktıyı veriyor::
    
    Help on built-in function dir in module builtins:

    dir(...)
        dir([object]) -> list of strings

        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
          for a module object: the module's attributes.
          for a class object:  its attributes, and recursively the attributes of its bases.
          for any other object: its attributes, its class's attributes, and 
          recursively the attributes of its class's base classes.

Gördüğünüz gibi, ``dir()`` fonksiyonunun ne işe yaradığı ve nasıl kullanıldığı
konusunda ayrıntılı bir bilgi ediniyoruz. Bu arada, hakkında bilgi almak
istediğimiz fonksiyonu parantezsiz yazdığımıza dikkat edin.

Örnek olması açısından mesela bir de ``len()`` fonksiyonu hakkında bilgi
edinelim::

    help> len

    Help on built-in function len in module builtins:

    len(...)
        len(object) -> integer

        Return the number of items of a sequence or mapping.

'help' ekranından çıkmak için `Enter` düğmesine basabilir veya ``quit`` komutu
verebilirsiniz.

En başta da dediğimiz gibi Python'da etkileşimli kabuk üzerinde İngilizce yardım
almak için iki farklı yöntem kullanabiliyoruz. Bu yöntemlerden ilkini yukarıda
anlattık. İkincisi ise doğrudan etkileşimli kabukta şu komutu kullanmaktır:
(Mesela ``dir()`` fonksiyonu hakkında yardım alalım...)

::

    >>> help(dir)
    
    Help on built-in function dir in module builtins:

    dir(...)
        dir([object]) -> list of strings

        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
          for a module object: the module's attributes.
          for a class object:  its attributes, and recursively the attributes of its bases.
          for any other object: its attributes, its class's attributes, and 
          recursively the attributes of its class's base classes.

Gördüğünüz gibi, 'help' ekranını açmadan, doğrudan etkileşimli kabuk üzerinden
de ``help()`` fonksiyonunu herhangi bir fonksiyon gibi kullanıp, hakkında yardım
almak istediğimiz nesneyi ``help()`` fonksiyonunun parantezleri içine parametre
olarak yazabiliyoruz.

.. highlight:: py3

Böylece ``dir()``, ``enumerate()`` ve ``help()`` adlı üç önemli fonksiyonu da
geride bırakmış olduk. Dilerseniz şimdi karakter dizilerine dair birkaç ufak not
düşelim. 

Notlar
********

Hatırlarsanız döngüleri anlatırken şöyle bir örnek vermiştik::
    
    tr_harfler = "şçöğüİı"
    a = 0

    while a < len(tr_harfler):
        print(tr_harfler[a], sep="\n")
        a += 1
        
Bu kodların ``for`` döngüsü ile yazılabilecek olan şu kodlara alternatif
olduğundan söz etmiştik::
    
    tr_harfler = "şçöğüİı"
    
    for tr_harf in tr_harfler:
        print(tr_harf)
        
Yukarıdaki ``while`` örneğini verirken, henüz karakter dizilerinin öğelerine tek
tek nasıl erişebileceğimizi öğrenmemiştik. Ama artık bu konuyu da öğrendiğimiz
için yukarıdaki ``while`` döngüsünü rahatlıkla anlayabiliyoruz::
    
    while a < len(tr_harfler):
        print(tr_harfler[a], sep="\n")
        a += 1
        
Burada yaptığımız şey şu: `a` değişkeninin değeri `tr_harfler` değişkeninin
uzunluğundan (``len(tr_harfler)``) küçük olduğu müddetçe `a` değişkeninin
değerini `1` sayı artırıp yine `a` değişkenine gönderiyoruz (``a += 1``).

``while`` döngüsünün her dönüşünde de, `a` değişkeninin yeni değeri yardımıyla
`tr_harfler` adlı karakter dizisinin öğelerine tek tek ve sırayla erişiyoruz
(``print(tr_hafler[a])``).

Yine hatırlarsanız, önceki derslerimizde `sys` adlı bir modül içindeki `version`
adlı bir değişkenden söz etmiştik. Bu değişken bize kullandığımız Python'ın
sürümünü bir karakter dizisi olarak veriyordu::
    
    >>> import sys
    >>> sys.version
    
Buradan şu çıktıyı alıyoruz:

.. parsed-literal::
    
    |version3-string|
    
Bu çıktıda, kullandığımız Python sürümünün dışında başka birtakım bilgiler de
var. İşte biz eğer istersek, bu bölümde öğrendiğimiz bilgileri kullanarak bu
karakter dizisinin istediğimiz kısmını, mesela sadece sürüm bilgisini karakter
dizisinin içinden dilimleyip alabiliriz::
    
    >>> sys.version[:5]
    
.. parsed-literal::
    
    |version3| 
    
Elbette, yukarıdaki karakter dizisini elde etmek için, kullanması ve yönetmesi
daha kolay bir araç olan `version_info` değişkeninden de yararlanabilirdiniz::
    
    >>> '{}.{}.{}'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

.. parsed-literal::

    |version3|
    
Ancak burada şöyle bir sorun olduğunu biliyorsunuz: Python'ın 2.7 öncesi
sürümlerinde `version_info`'nun `major`, `minor` ve `micro` gibi nitelikleri
yok. Dolayısıyla 2.7 öncesi sürümlerde `version_info`'yu kullanırken hata
almamak için ``try... except`` bloklarından yararlanabileceğimizi görmüştük.
Ancak `version_info`'yu bütün Python sürümlerinde güvenli bir şekilde
kullanmanın başka bir yöntemi daha var. Dikkatlice bakın::
    
    >>> major = sys.version_info[0]
    >>> minor = sys.version_info[1]
    >>> micro = sys.version_info[2]
    
    >>> print(major, minor, micro, sep=".")

.. parsed-literal::

    |py3|

Bu yöntem bütün Python sürümlerinde çalışır. Dolayısıyla, farklı Python
sürümlerinde çalışmasını tasarladığınız programlarınızda sürüm kontrolünü
`sys.version_info`'nun `major`, `minor` veya `micro` nitelikleri ile yapmak
yerine yukarıdaki yöntemle yapabilirsiniz::
    
    if sys.version_info[1] < 3:
        print("Kullandığınız Python sürümü eski!")

Gördüğünüz gibi, karakter dizisi dilimleme işlemleri pek çok farklı kullanım
alanına sahip. Programlama maceranız boyunca karakter dizilerinin bu
özelliğinden bol bol yararlanacağınızdan hiç kuşkunuz olmasın.

