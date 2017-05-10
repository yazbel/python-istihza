.. meta::
   :description: Bu bölümde hata yakalama konusunu inceleyeceğiz
   :keywords: python, hata, try, except, exception, error

.. highlight:: py3

**************
Hata Yakalama
**************

Şimdiye kadar yazdığımız bütün programlar, dikkat ettiyseniz tek bir ortak
varsayım üzerine kurulu. Buna göre biz, yazdığımız programın kullanıcı
tarafından nasıl kullanılmasını istiyorsak, her zaman o şekilde kullanılacağını
varsayıyoruz. Örneğin sayıları toplayan bir program yazdığımızda, kullanıcının
her zaman sayı değerli bir veri gireceğini düşünüyoruz. Ancak bütün iyi
niyetimize rağmen, yazdığımız programlarda işler her zaman beklediğimiz gibi
gitmeyebilir. Örneğin, dediğimiz gibi, yazdığımız programı, kullanıcının bir
sayı girmesi temeli üzerine kurgulamışsak, kullanıcının her zaman sayı değerli
bir veri gireceğinden emin olamayız

Mesela şöyle bir program yazdığımızı düşünün::

    veri1 = input("Karekökünü hesaplamak istediğiniz sayı: ")
    karekök = int(veri1) ** 0.5

    print(veri1, "sayısının karekökü: ", karekök) 
    
    veri2 = input("Karesini hesaplamak istediğiniz sayı: ")
    kare = int(veri2) ** 2
    
    print(veri2, "sayısının karesi: ", kare)

Bu kodlardaki sorunu anlamaya çalışmadan önce dilerseniz kodları şöyle bir
inceleyelim.

Gördüğünüz gibi, burada kullanıcının gireceği sayılara göre karekök ve kare alma
işlemleri yapıyoruz. Bu kodlarda gördüğümüz `**` işleci yardımıyla bir sayının
herhangi bir kuvvetini hesaplayabileceğimizi biliyorsunuz. Mesela 21\
:sup:`7`'nin kaç ettiğini hesaplamak için `**` işlecini kullanabiliyoruz::
    
    >>> 21 ** 7
    
    1801088541

Yine bildiğiniz gibi, bu işleçten, bir sayının karesini hesaplamak için de
yararlanabiliyoruz. Çünkü neticede bir sayının karesi, o sayının 2. kuvvetidir::
    
    >>> 12 ** 2
    
    144

Aynı şekilde, eğer bir sayının, 0.5'inci kuvvetini hesaplarsak o sayının
karekökünü bulmuş oluyoruz. (Bu bilgileri önceki konulardan hatırlıyor
olmalısınız)::
    
    >>> 144 ** 0.5
    
    12
    
Kodlarımızı incelediğimize göre, bu programdaki aksaklıkları irdelemeye
başlayabiliriz.

Bu program, kullanıcı sayı değerli bir veri girdiği müddetçe sorunsuz bir
şekilde çalışacaktır. Peki ya kullanıcı sayı değerli bir veri yerine başka bir
şey girerse ne olur?

Örneğin kullanıcı yukarıdaki programa bir sayı yerine, (bilerek veya bilmeyerek)
içinde harf barındıran bir veri girerse şuna benzer bir hata alır::
    
    Traceback (most recent call last):
      File "deneme.py", line 2, in <module>
        karekök = int(veri1) ** 0.5
    ValueError: invalid literal for int() with base 10: 'fds'

Yazdığınız programların bu tür hatalar vermesi normaldir. Ancak son kullanıcı
açısından düşündüğümüzde, kullanıcının yukarıdaki gibi bir hata mesajı görmesi
yerine, hatanın neden kaynaklandığını ya da neyi yanlış yaptığını daha açık bir
şekilde ifade eden bir mesaj alması çok daha mantıklı olacaktır. Zira yukarıdaki
hata mesajı programcılar açısından anlamlı olabilir, ancak son kullanıcı
açısından büsbütün anlaşılmazdır!

Dediğimiz gibi, programınızın çalışma esnasında bu tür hatalar vermesi normal.
Çünkü yapmaya çalıştığınız işlem, kullanıcının belli tipte bir veri girmesine
bağlı. Burada sizin bir programcı olarak göreviniz, yazdığınız programın çalışma
esnasında vermesi muhtemel hataları önceden kestirip, programınızda buna göre
bazı önlemler almanızdır. İşte biz de bu bölümde bu önlemleri nasıl alacağımızı
anlamaya çalışacağız.

Hata Türleri
*************

Biz bu bölümde hatalardan bahsedeceğimizi söylemiştik. Ancak her şeyden önce
'hata' kavramının çok boyutlu olduğunu hatırlatmakta fayda var. Özellikle
programcılık açısından hata kavramının ne anlama geldiğini biraz incelememiz
gerekiyor.

Biz bu bölümde hataları üç farklı başlık altında ele alacağız:

#. Programcı Hataları (*Error*)

#. Program Kusurları (*Bug*)

#. İstisnalar (*Exception*)

Öncelikle programcı hatalarından bahsedelim.

Programcıdan kaynaklanan hatalar doğrudan doğruya programı yazan kişinin
dikkatsizliğinden ötürü ortaya çıkan bariz hatalardır. Örneğin şu kod bir
programcı hatası içerir::
    
    >>> print "Merhaba Python!"

Bu kodu çalıştırdığınızda şöyle bir hata mesajı görürsünüz::

    >>> print "Merhaba Python!"
    
    File "<stdin>", line 1
       print "Merhaba Python!"
                             ^
    SyntaxError: invalid syntax

Bu hata mesajında bizi ilgilendiren kısım son cümlede yer alıyor:
``SyntaxError``, yani Söz dizimi hatası.

Bu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından veya
en basit şekilde programcının yaptığı yazım hatalarından kaynaklanır.
Programcının hataları genellikle ``SyntaxError`` şeklinde ortaya çıkar. Bu
hatalar çoğunlukla programcı tarafından farkedilir ve program kullanıcıya
ulaşmadan önce programcı tarafından düzeltilir. Bu tür hataların tespiti diğer
hatalara kıyasla kolaydır. Çünkü bu tür hatalar programınızın çalışmasını
engellediği için bunları farketmemek pek mümkün değildir...

Program kusurları, başka bir deyişle *bug*'lar ise çok daha karmaşıktır. Kusurlu
programlar çoğu zaman herhangi bir hata vermeden çalışır. Ancak programın
ürettiği çıktılar beklediğiniz gibi değildir. Örneğin yazdığınız programda bir
formül hatası yapmış olabilirsiniz. Bu durumda programınız hiçbir şey yokmuş
gibi çalışır, ancak formül hatalı olduğu için hesaplamaların sonuçları
yanlıştır. Örneğin daha önceki derslerimizde yazdığımız şu program yukarıdaki
gibi bir kusur içerir::
    
    sayı1 = input("Toplama işlemi için ilk sayıyı girin: ")
    sayı2 = input("Toplama işlemi için ikinci sayıyı girin: ")

    print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

Bu programda kullanıcı veri girdiği zaman, programımız toplama işlemi değil
karakter dizisi birleştirme işlemi yapacaktır. Böyle bir program çalışma
sırasında hata vermeyeceği için buradaki sorunu tespit etmek, özellikle büyük
programlarda çok güçtür. Yani sizin düzgün çalıştığını zannettiğiniz program
aslında gizliden gizliye bir *bug* barındırıyor olabilir.

Aynı şekilde, mesela ``eval()`` fonksiyonunun dikkatsizce kullanıldığı
programlar da güvenlik açısından kusurludur. Yani bu tür programlar bir güvenlik
kusuru (*security bug* veya *security flaw*) barındırır.

Dediğimiz gibi, program kusurları çok boyutlu olup, burada anlattığımızdan çok
daha karmaşıktır.

Gelelim üçüncü kategori olan istisnalara (*exceptions*)...

İstisnalar, adından da az çok anlaşılacağı gibi, bir programın çalışması
sırasında ortaya çıkan, normalden farklı, istisnai durumlardır. Örneğin şu
programa bakalım::
    
    ilk_sayı = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    ilk_sayı = int(ilk_sayı)
    ikinci_sayı = int(ikinci_sayı)

    print(ilk_sayı, "/", ikinci_sayı, "=", ilk_sayı / ikinci_sayı) 

Burada ilk sayıyı ikinci sayıya bölen bir program yazdık. Bu program her türlü
bölme işlemini yapabilir. Ama burada hesaba katmamız gereken iki şey var:

#. Kullanıcı sayı yerine, sayı değerli olmayan bir veri tipi girebilir. Mesela
   ilk sayıya karşılık `23`, ikinci sayıya karşılık 'fdsfd' gibi bir şey yazabilir.

#. Kullanıcı bir sayıyı `0`'a bölmeye çalışabilir. Mesela ilk sayıya karşılık
   `23`, ikinci sayıya karşılık `0` yazabilir.

İlk durumda programımız şöyle bir hata verir::
    
    ilk sayı: 23
    ikinci sayı: fdsfd
    Traceback (most recent call last):
      File "deneme.py", line 5, in <module>
        ikinci_sayı = int(ikinci_sayı)
    ValueError: invalid literal for int() with base 10: 'fdsfd'

Buradaki sorun, sayı değerli olmayan bir verinin, ``int()`` fonksiyonu
aracılığıyla sayıya çevrilmeye çalışılıyor olması.

İkinci durumda ise programımız şöyle bir hata verir::

    ilk sayı: 23
    ikinci sayı: 0
    Traceback (most recent call last):
      File "deneme.py", line 7, in <module>
        print(ilk_sayı, "/", ikinci_sayı, "=", ilk_sayı / ikinci_sayı)
    ZeroDivisionError: division by zero

Buradaki sorun ise, bir sayının `0`'a bölünmeye çalışılıyor olması. Matematikte
sayılar `0`'a bölünemez...

İşte bu iki örnekte gördüğümüz ``ValueError`` ve ``ZeroDivisionError`` birer
istisnadır. Yani kullanıcıların, kendilerinden sayı beklenirken sayı değerli
olmayan veri girmesi veya bir sayıyı 0'a bölmeye çalışması istisnai birer
durumdur ve yazdığımız programların *exception* (istisna) üretmesine yol açar.

Böylece hata (*error*), kusur (*bug*) ve istisna (*exception*) arasındaki
farkları şöyle bir gözden geçirmiş olduk. Yalnız burada şunu söylemekte yarar
var: Bu üç kavram arasındaki fark belli belirsizdir. Yani bu kavramların çoğu
yerde birbirlerinin yerine kullanıldığını da görebilirsiniz. Örneğin *exception*
kavramı için Türkçe'de çoğu zaman 'hata' kelimesini kullanıyoruz. Zaten dikkat
ederseniz bu bölümün başlığı da 'İstisna Yakalama' değil, 'Hata Yakalama'dır.
Aynı şekilde, İngilizcede de bu kavramların çoğu yerde birbirleri yerine
kullanıldığını görebilirsiniz. Dolayısıyla, konuya karşı özel bir ilginiz yoksa,
hata, kusur ve istisna kavramlarını birbirinden ayırmak için kendinizi
zorlamanıza gerek yok. Bu üç kavram çoğu zaman birbirinin yerine kullanılıyor da
olsa, aslında aralarında bazı farklar olduğunu öğrenmişseniz bu bölüm amacına
ulaşmış demektir.

Konuyla ilgili temel bilgileri edindiğimize göre asıl meseleye geçebiliriz... 

try... except...
*****************

Bir önceki bölümde hatalardan ve hataları yakalamaktan söz ettik. Peki bu
hataları nasıl yakalayacağız?

Python'da hata yakalama işlemleri için ``try... except...`` bloklarından
yararlanılır. Hemen bir örnek verelim::

    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ValueError:
        print("Lütfen sadece sayı girin!")

Biliyoruz ki, bir veriyi sayıya dönüştürmek istediğimizde eğer kullanıcı sayı
değerli bir veri yerine harf değerli bir veri girerse programımız çöker.
Dolayısıyla ``int(ilk_sayı)`` ve ``int(ikinci_sayı)`` kodları, kullanıcının
gireceği veri türüne göre hata üretme potansiyeline sahiptir. O yüzden, burada
hata vereceğini bildiğimiz o kodları ``try`` bloğu içine aldık.

Yine bildiğimiz gibi, veri dönüştürme işlemi sırasında kullanıcının uygun
olmayan bir veri girmesi halinde üretilecek hata bir ``ValueError``'dır.
Dolayısıyla ``except`` bloğu içine yazacağımız hata türünün adı da
``ValueError`` olacaktır. O yüzden ``ValueError`` adlı hatayı yakalayabilmek
için şu satırları yazdık::
    
    except ValueError:
        print("Lütfen sadece sayı girin!")

Burada bu kodlarla Python'a şu emri vermiş olduk:

    Eğer ``try`` bloğu içinde belirtilen işlemler sırasında bir ``ValueError``
    ile karşılaşırsan bunu görmezden gel ve normal şartlar altında kullanıcıya
    göstereceğin hata mesajını gösterme. Onun yerine kullanıcıya ``Lütfen sadece
    sayı girin!`` uyarısını göster. 
    
Yukarıda Türkçeye çevirdiğimiz emri Pythoncada nasıl ifade ettiğimize dikkat
edin. Temel olarak şöyle bir yapıyla karşı karşıyayız::
        
    try:
        hata verebileceğini bildiğimiz kodlar
    except HataAdı:
        hata durumunda yapılacak işlem

Gelin isterseniz bir örnek daha verelim. 

Hatırlarsanız bir sayının `0`'a bölünmesinin mümkün olmadığını, böyle bir
durumda programımızın hata vereceğini söylemiştik. Bu durumu teyit etmek için
etkileşimli kabukta şu kodu deneyebilirsiniz::

    >>> 2 / 0

Bu kod şöyle bir hata mesajı verecektir::

    >>> 2 / 0

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

Daha önce de söylediğimiz gibi, bu hata mesajında bizi ilgilendiren kısım
``ZeroDivisionError``. Demek ki bir sayı `0`'a bölündüğünde Python
``ZeroDivisionError`` veriyormuş. O halde şöyle bir kod yazabiliriz::

    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")

Gördüğünüz gibi, Python'ın ``ZeroDivisionError`` vereceğini bildiğimiz durumlara
karşı bu hata türünü yakalama yoluna gidiyoruz. Böylece kullanıcıya anlamsız ve
karmaşık hata mesajları göstermek ve daha da kötüsü, programımızın çökmesine
sebep olmak yerine daha anlaşılır mesajlar üretiyoruz.

Yukarıdaki kodlarda özellikle bir nokta dikkatinizi çekmiş olmalı: Dikkat
ederseniz yukarıdaki kodlar aslında bir değil iki farklı hata üretme
potansiyeline sahip. Eğer kullanıcı sayı değerli veri yerine harf değerli bir
veri girerse ``ValueError``, eğer bir sayıyı `0`'a bölmeye çalışırsa da
``ZeroDivisionError`` hatası alıyoruz. Peki aynı kodlarda iki farklı hata türünü
nasıl yakalayacağız?

Çok basit::
    
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
    except ValueError:
        print("Lütfen sadece sayı girin!")

Gördüğünüz gibi çözüm gayet mantıklı. Birden fazla hata türü üreteceğini
bildiğimiz kodları yine tek bir ``try`` bloğu içine alıyoruz. Hata türlerini ise
ayrı ``except`` blokları içinde ele alıyoruz.

Bir program yazarken, en iyi yaklaşım, yukarıda yaptığımız gibi, her hata türü
için kullanıcıya ayrı bir uyarı mesajı göstermektir. Böylece kullanıcılarımız
bir hatayla karşılaştıklarında sorunu nasıl çözebilecekleri konusunda en azından
bir fikir sahibi olabilirler.

Dediğimiz gibi, her hata için ayrı bir mesaj göstermek en iyisidir. Ama tabii
dilerseniz hata türlerini gruplayıp hepsi için tek bir hata mesajı göstermeyi de
tercih edebilirsiniz. Bunu nasıl yapacağımızı görelim::
    
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except (ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")

Gördüğünüz gibi, burada ``ValueError`` ve ``ZeroDivisionError`` adlı hata
türlerini tek bir parantez içinde topladık. Burada dikkat edeceğimiz nokta, bu
hata türlerini gruplarken bunları parantez içine almak ve birbirlerinden
virgülle ayırmaktır.

Bu arada, gördüğünüz gibi yukarıdaki programlar sadece bir kez çalışıp
kapanıyor. Ama biz bu programları tekrar tekrar nasıl çalıştırabileceğimizi
gayet iyi biliyoruz::
    
    while True:
        ilk_sayı = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")
        
        if ilk_sayı == "q":
            break
        
        ikinci_sayı = input("ikinci sayı: ")

        try:
            sayı1 = int(ilk_sayı)
            sayı2 = int(ikinci_sayı)
            print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
        except (ValueError, ZeroDivisionError):
            print("Bir hata oluştu!")
            print("Lütfen tekrar deneyin!")

Python'da hata yakalamanın en yaygın yolu yukarıda gösterdiğimiz gibi kodları
``try... except`` blokları içine almaktır. Programcılık maceranızın büyük
bölümünde bu yapıyı kullanacaksınız. Ama bazen, karşı karşıya olduğunuz duruma
veya ihtiyacınıza göre ``try... except`` bloklarının farklı varyasyonlarını
kullanmanız gerekebilir. İşte şimdi biz de bu farklı varyasyonların neler
olduğunu incelemeye çalışacağız.

try... except... as...
***********************

Bildiğiniz gibi, Python bir programın çalışması esnasında hata üretirken çıktıda
hata türünün adıyla birlikte kısa bir hata açıklaması veriyor. Yani mesela şöyle
bir çıktı üretiyor::
    
    ValueError: invalid literal for int() with base 10: 'f'

Burada 'ValueError' hata türünün adı, 'invalid literal for int() with base 10:
'f'' ise hatanın açıklamasıdır. Eğer istersek, yazdığımız programda bu hata
açıklamasına erişebiliriz. Dikkatlice bakın::
    
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ValueError as hata:
        print(hata)

Bu programı çalıştırıp sayı değerli olmayan bir veri girersek hata çıktısı şöyle
olacaktır::
    
    invalid literal for int() with base 10: 'f'

Gördüğünüz gibi, bu defa çıktıda hata türünün adı (``ValueError``) görünmüyor.
Onun yerine sadece hata açıklaması var.

Diyelim ki kullanıcıya olası bir hata durumunda hem kendi yazdığınız hata
mesajını, hem de özgün hata mesajını göstermek istiyorsunuz. İşte yukarıdaki
yapı böyle durumlarda işe yarayabilir::
    
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except ValueError as hata:
        print("Sadece sayı girin!")
        print("orijinal hata mesajı: ", hata)

Bu arada, biraz önce yaptığımız gibi, hata türlerini grupladığınızda da bu
yöntemi kullanabilirsiniz::
    
    ilk_sayı    = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")

    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı: ", hata)

Burada ``except falancaHata as filanca`` yapısını kullanarak ``falancaHata``'yı
`filanca` olarak isimlendiriyor ve daha sonra bu ismi istediğimiz gibi
kullanabiliyoruz. Böylece bütün hata türleri için hem kendi yazdığınız mesajı
görüntüleyebiliyor, hem de özgün hata mesajını da çıktıya eklediğimiz için,
kullanıcıya hata hakkında en azından bir fikir sahibi olma imkanı vermiş
oluyoruz.

try... except... else...
*************************

Daha önce de dediğimiz gibi, Python'da hata yakalama işlemleri için çoğunlukla
``try... except...`` bloklarını bilmek yeterli olacaktır. İşlerimizin büyük
kısmını sadece bu blokları kullanarak halledebiliriz. Ancak Python bize bu
konuda, zaman zaman işimize yarayabilecek başka araçlar da sunmaktadır. İşte
``try... except... else...`` blokları da bu araçlardan biridir. Bu bölümde
kısaca bu blokların ne işe yaradığından söz edeceğiz.

Öncelikle ``try... except... else...`` bloğunun ne işe yaradığına bakalım.
Esasında biz bu ``else`` deyimini daha önce de 'koşullu ifadeler' konusunu
işlerken görmüştük. Buradaki kullanımı da zaten hemen hemen aynıdır. Diyelim ki
elimizde şöyle bir şey var::
    
	try:
	    bölünen = int(input("bölünecek sayı: "))
	    bölen = int(input("bölen sayı: "))
	    print(bölünen/bölen)
	except ValueError:
	    print("hata!")

Burada eğer kullanıcı sayı yerine harf girerse ``ValueError`` hatası alırız. Bu
hatayı ``except ValueError:`` ifadesiyle yakalıyoruz ve hata verildiğinde
kullanıcıya bir mesaj göstererek programımızın çökmesini engelliyoruz. Ama
biliyoruz ki, bu kodları çalıştırdığımızda Python'ın verebileceği tek hata
``ValueError`` değildir. Eğer kullanıcı bir sayıyı 0'a bölmeye çalışırsa Python
``ZeroDivisionError`` adlı hatayı verecektir. Dolayısıyla bu hatayı da yakalamak
için şöyle bir şey yazabiliriz::
    
	try:
	    bölünen = int(input("bölünecek sayı: "))
	    bölen = int(input("bölen sayı: "))
	    print(bölünen/bölen)
	except ValueError:
	    print("Lütfen sadece sayı girin!")
	except ZeroDivisionError:
	    print("Bir sayıyı 0'a bölemezsiniz!")

Bu şekilde hem ``ValueError`` hatasını hem de ``ZeroDivisionError`` hatasını
yakalamış oluruz. Bu kodların özelliği, ``except...`` bloklarının tek bir
``try...`` bloğunu temel almasıdır. Yani biz burada bütün kodlarımızı tek bir
``try...`` bloğu içine tıkıştırıyoruz. Bu blok içinde gerçekleşen hataları da
daha sonra tek tek ``except...`` blokları yardımıyla yakalıyoruz. Ama eğer biz
istersek bu kodlarda verilebilecek hataları gruplamayı da tercih edebiliriz::
    
    try:
        bölünen = int(input("bölünecek sayı: "))
        bölen = int(input("bölen sayı: "))
    except ValueError:
        print("Lütfen sadece sayı girin!")
    else:
        try:
            print(bölünen/bölen)
        except ZeroDivisionError:
            print("Bir sayıyı 0'a bölemezsiniz!")

Burada yaptığımız şey şu: İlk ``try... except...`` bloğu yardımıyla öncelikle
``int(input())`` fonksiyonu ile kullanıcıdan gelecek verinin sayı olup
olmadığını denetliyoruz. Ardından bir ``else...`` bloğu açarak, bunun içinde
ikinci ``try... except...`` bloğumuzu devreye sokuyoruz. Burada da bölme
işlemini gerçekleştiriyoruz. Kullanıcının bölme işlemi sırasında `0` sayısını
girmesi ihtimaline karşı da ``except ZeroDivisionError`` ifadesi yardımıyla
olası hatayı göğüslüyoruz. Bu şekilde bir kodlamanın bize getireceği avantaj,
hatalar üzerinde belli bir kontrol sağlamamıza yardımcı olmasıdır. Yukarıdaki
kodlar sayesinde hatalara bir nevi 'teker teker gelin!' mesajı vermiş oluyoruz.
Böylelikle her blok içinde sadece almayı beklediğimiz hatayı karşılıyoruz.
Mesela yukarıda ilk ``try...`` bloğu içindeki dönüştürme işlemi yalnızca
``ValueError`` hatası verebilir. ``else:`` bloğundan sonraki ``try...`` bloğunda
yer alan işlem ise ancak ``ZeroDivisionError`` verecektir. Biz yukarıda
kullandığımız yapı sayesinde her bir hatayı tek tek ve yeri geldiğinde
karşılıyoruz. Bu durumun aksine, bölümün ilk başında verdiğimiz ``try...
except`` bloğunda hem ``ValueError`` hem de ``ZeroDivisionError`` hatalarının
gerçekleşme ihtimali bulunuyor. Dolayısıyla biz orada bütün hataları tek bir
``try...`` bloğu içine sıkıştırmış oluyoruz. İşte ``else:`` bloğu bu sıkışıklığı
gidermiş oluyor. Ancak sizi bir konuda uyarmak isterim: Bu yapı, her akla
geldiğinde kullanılacak bir yapı değildir. Büyük programlarda bu tarz bir
kullanım kodlarınızın darmadağın olmasına, kodlarınız üzerindeki denetimi
tamamen kaybetmenize de yol açabilir. Sonunda da elinizde bölük pörçük bir kod
yığını kalabilir. Zaten açıkça söylemek gerekirse ``try... except... else...``
yapısının çok geniş bir kullanım alanı yoktur. Bu yapı ancak çok nadir
durumlarda kullanılmayı gerektirebilir. Dolayısıyla bu üçlü yapıyı hiç
kullanmadan bir ömrü rahatlıkla geçirebilirsiniz.

try... except... finally...
*****************************

``try... except... else...`` yapılarının dışında, Python'ın bize sunduğu bir
başka yapı da ``try... except... finally...`` yapılarıdır. Bunu şöyle
kullanıyoruz::
    
	try:
	    ...bir takım işler...
	except birHata:
	    ...hata alınınca yapılacak işlemler...
	finally:
	    ...hata olsa da olmasa da yapılması gerekenler...

``finally..`` bloğunun en önemli özelliği, programın çalışması sırasında
herhangi bir hata gerçekleşse de gerçekleşmese de işletilecek olmasıdır. Eğer
yazdığınız programda mutlaka ama mutlaka işletilmesi gereken bir kısım varsa, o
kısmı ``finally...`` bloğu içine yazabilirsiniz.

``finally...`` bloğu özellikle dosya işlemlerinde işimize yarayabilir. Henüz
Python'da dosyalarla nasıl çalışacağımızı öğrenmedik, ama ben şimdilik size en
azından dosyalarla çalışma prensibi hakkında bir şeyler söyleyeyim.

Genel olarak Python'da dosyalarla çalışabilmek için öncelikle bilgisayarda
bulunan bir dosyayı okuma veya yazma kipinde açarız. Dosyayı açtıktan sonra bu
dosyayla ihtiyacımız olan birtakım işlemler gerçekleştiririz. Dosyayla işimiz
bittikten sonra ise dosyamızı mutlaka kapatmamız gerekir. Ancak eğer dosya
üzerinde işlem yapılırken bir hata ile karşılaşılırsa dosyamızı kapatma işlemini
gerçekleştirdiğimiz bölüme hiç ulaşılamayabilir. İşte ``finally...`` bloğu böyle
bir durumda işimize yarayacaktır::

	try:
	    dosya = open("dosyaadı", "r")
	    ...burada dosyayla bazı işlemler yapıyoruz...
	    ...ve ansızın bir hata oluşuyor...
	except IOError:
	    print("bir hata oluştu!")
	finally:
	    dosya.close()

Burada ``finally...`` bloğu içine yazdığımız ``dosya.close()`` ifadesi dosyamızı
güvenli bir şekilde kapatmaya yarıyor. Bu blok, yazdığımız program hata verse de
vermese de işletilecektir.

raise
******

Bazen, yazdığımız bir programda, kullanıcının yaptığı bir işlem normal şartlar
altında hata vermeyecek olsa bile biz ona 'Python tarzı' bir hata mesajı
göstermek isteyebiliriz. Böyle bir durumda ihtiyacımız olan şey Python'ın bize
sunduğu ``raise`` adlı deyimdir. Bu deyim yardımıyla duruma özgü hata mesajları
üretebiliriz. Bir örnek verelim::
    
	bölünen = int(input("bölünecek sayı: "))

	if bölünen == 23:
	    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

	bölen = int(input("bölen sayı: "))
	print(bölünen/bölen)

Burada eğer kullanıcı `23` sayısını girerse, kullanıcıya bir hata mesajı
gösterilip programdan çıkılacaktır. Biz bu kodlarda ``Exception`` adlı genel
hata mesajını kullandık. Burada ``Exception`` yerine her istediğimizi yazamayız.
Yazabileceklerimiz ancak Python'da tanımlı hata mesajları olabilir. Örneğin
``NameError``, ``TypeError``, ``ZeroDivisionError``, ``IOError``, vb...

Bir örnek verelim::

    tr_karakter = "şçğüöıİ"

    parola = input("Parolanız: ")

    for i in parola:
        if i in tr_karakter:
            raise TypeError("Parolada Türkçe karakter kullanılamaz!")
        else:
            pass

    print("Parola kabul edildi!")

Bu kodlar çalıştırıldığında, eğer kullanıcı, içinde Türkçe karakter geçen bir
parola yazarsa kendisine ``TypeError`` tipinde bir hata mesajı gösteriyoruz.
Eğer kullanıcının parolası Türkçe karakter içermiyorsa hiçbir şey yapmadan
geçiyoruz ve bir sonraki satırda kendisine 'Parola kabul edildi!' mesajını
gösteriyoruz.

``raise`` deyimini, bir hata mesajına ek olarak bir işlem yapmak istediğimizde
de kullanabiliriz. Örneğin::
    
	try:
	    bölünen = int(input("bölünecek sayı: "))
	    bölen = int(input("bölen sayı: "))
	    print(bölünen/bölen)
	except ZeroDivisionError:
	    print("bir sayıyı 0'a bölemezsiniz")
	    raise

Burada, eğer kullanıcı bir sayıyı `0`'a bölmeye çalışırsa, normal bir şekilde
``ZeroDivisionError`` hatası verilecek ve programdan çıkılacaktır. Ama bu hata
mesajıyla birlikte kullanıcıya 'bir sayıyı 0'a bölemezsiniz,' uyarısını da
gösterme imkanını elde edeceğiz. Yani burada ``except ZeroDivisionError``
bloğunu herhangi bir hatayı engellemek için değil, hataya ilave bilgi eklemek
için kullanıyoruz. Bunu yapmamızı sağlayan şey tabii ki bu kodlar içinde görünen
``raise`` adlı deyimdir...

Bütün Hataları Yakalamak
*************************

Şimdiye kadar yaptığımız bütün örneklerde ``except...`` bloğunu bir hata mesajı
adıyla birlikte kullandık. Yani örneklerimiz şuna benziyordu::

	try:
	    ....birtakım işler...
	except ZeroDivisionError:
	    ...hata mesajı...

Yukarıdaki kod yardımıyla sadece ``ZeroDivisionError`` adlı hatayı
yakalayabiliriz. Eğer yazdığımız program başka bir hata daha veriyorsa, o hata
mesajı yukarıdaki blokların kapsamı dışında kalacaktır. Ama eğer istersek
yukarıdaki kodu şu şekilde yazarak olası bütün hataları yakalayabiliriz::
    
	try:
	    ....birtakım işler...
	except:
	    ...hata mesajı...

Gördüğünüz gibi, burada herhangi bir hata adı belirtmedik. Böylece Python,
yazdığımız programda hangi hata oluşursa oluşsun hepsini yakalayabilecektir.

Bu yöntem gözünüze çok pratik görünmüş olabilir, ama aslında hiç de öyle
sayılmaz. Hatta oldukça kötü bir yöntem olduğunu söyleyebiliriz bunun. Çünkü bu
tarz bir kod yazımının bazı dezavantajları vardır. Örneğin bu şekilde bütün hata
mesajlarını aynı kefeye koyarsak, programımızda ne tür bir hata oluşursa
oluşsun, kullanıcıya hep aynı mesajı göstermek zorunda kalacağız. Bu da,
herhangi bir hata durumunda kullanıcıyı ne yapması gerektiği konusunda doğru
düzgün bilgilendiremeyeceğimiz anlamına geliyor. Yani kullanıcı bir hataya sebep
olduğunda tersliğin nereden kaynaklandığını tam olarak kestiremeyecektir.

Ayrıca, eğer kendimiz bir program geliştirirken sürekli olarak bu tarz bir
yazımı benimsersek, kendi kodlarımızdaki hataları da maskelemiş oluruz.
Dolayısıyla, Python yukarıdaki geniş kapsamlı ``except...`` bloğu nedeniyle
programımızdaki bütün hataları gizleyeceği için, programımızdaki potansiyel
aksaklıkları görme imkanımız olmaz. Dolayısıyla bu tür bir yapıdan olabildiğince
kaçınmakta fayda var. Ancak elbette böyle bir kod yazmanızı gerektiren bir
durumla da karşılaşabilirsiniz. Örneğin::
    
    try:
        birtakım kodlar
    except ValueError:
        print("Yanlış değer")
    except ZeroDivisionError:
        print("Sıfıra bölme hatası")
    except:
        print("Beklenmeyen bir hata oluştu!")

Burada olası bütün hata türlerini yakaladıktan sonra, bunların dışında bizim o
anda öngöremediğimiz bir hatanın oluşması ihtimaline karşı ``except:`` kodunu
kullanarak kullanıcıya genel bir hata mesajı göstermeyi tercih edebiliriz.
Böylece beklenmeyen bir hata meydana gelmesi durumunda da programımız çökmek
yerine çalışmaya devam edebilecektir.

Örnek Uygulama
***************

Hata yakalama konusunu bütün ayrıntılarıyla inceledik. Gelin şimdi isterseniz
ufak bir örnek yapalım. 

Hatırlarsanız bir kaç bölüm önce şöyle bir uygulama yazmıştık::
    
    import sys
    
    _2x_metni = """
    Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
    Programı çalıştırabilmek için sisteminizde Python'ın
    3.x sürümlerinden biri kurulu olmalı."""
    
    _3x_metni = "Programa hoşgeldiniz."
    
    if sys.version_info.major < 3:
        print(_2x_metni)
    else:
        print(_3x_metni)
        
Bu programın ne iş yaptığını biliyorsunuz. Bu program yardımıyla,
kullanıcılarımızın bilgisayarlarındaki Python sürümünü kontrol edip,
programımızın kullanılan sürüme göre tepki vermesini sağlıyoruz. 

Ancak burada çok ciddi bir problem var. Python'ın 2.7 öncesi sürümlerinde `sys`
modülünün ``version_info()`` metodu farklı çıktılar verir. Mesela Python'ın 2.7
öncesi sürümlerinde ``version_info()`` metodunun `major`, `minor` veya `micro`
gibi nitelikleri bulunmaz. Bu nitelikler Python programlama diline 2.7 sürümüyle
birlikte geldi. Dolayısıyla yukarıdaki programı Python'ın 2.7 öncesi
sürümlerinden biriyle çalıştıran kullanıcılarınız istediğiniz çıktıyı
alamayacak, Python bu kullanıcalara şuna benzer bir hata mesajı göstererek
programın çökmesine sebep olacaktır::

    AttributeError: 'tuple' object has no attribute 'major'
    
Python'ın 2.7 öncesi sürümlerinin kurulu olduğu bilgisayarlarda da programınızın
en azından çökmemesi ve makul bir çıktı verebilmesi için yukarıdaki kodlar şöyle
yazabilirsiniz::
    
    import sys
    
    _2x_metni = """
    Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
    Programı çalıştırabilmek için sisteminizde Python'ın
    3.x sürümlerinden biri kurulu olmalı."""
    
    _3x_metni = "Programa hoşgeldiniz."
    
    try:
        if sys.version_info.major < 3:
            print(_2x_metni)
        else:
            print(_3x_metni)
    except AttributeError:
        print(_2x_metni)
        
Gördüğünüz gibi, ``AttributeError`` adlı hatayı vereceğini bildiğimiz kısmı bir
``try... except`` bloğu içine aldık. Eğer programımız ``AttributeError``
hatasını veriyorsa, programımızın çalıştırıldığı sistem Python'ın 2.7 sürümünden
daha düşük bir sürümü kullanıyor demektir. O yüzden kullanıcıya `_2x_metni`'ni
gösteriyoruz.

Elbette yukarıdaki programı yazmanın çok daha düzgün yolları vardır. Ama biz
hata yakalama yöntemlerinin buna benzer durumlarda da bir alternatif olarak
kullanılabileceğini bilelim. Ayrıca, dediğimiz gibi, ``try... except`` blokları
yukarıdaki sorunun çözümü için en uygun araçlar olmasa da, bazı durumlarda
hatayı önlemenin makul tek yoludur. 