.. meta::
   :description: Python 3.x'te karakter dizileri
   :keywords: python, string, karakter dizisi, metotlar

.. highlight:: py3

*************************************
Karakter Dizilerini Biçimlendirmek
*************************************

Bu bölüme gelinceye kadar, Python'da karakter dizilerinin biçimlendirilmesine
ilişkin epey söz söyledik. Ancak bu konu ile ilgili bilgilerimiz hem çok
dağınık, hem de çok yüzeysel. İşte bu bölümde amacımız, daha önce farklı
yerlerde dile getirdiğimiz bu önemli konuya ait bilgi kırıntılarını bir araya
toplayıp, karakter dizisi biçimlendirme konusunu, Python bilgimiz elverdiği
ölçüde ayrıntılı bir şekilde ele almak olacak.

Şu ana kadar yaptığımız örneklere bakarak, programlama maceranız boyunca
karakter dizileriyle bol bol haşır neşir olacağınızı anlamış olmalısınız. Bundan
sonra yazdığınız programlarda da karakter dizilerinin size pek çok farklı
biçimlerde geldiğine tanık olacaksınız. Farklı farklı biçimlerde elinize ulaşan
bu karakter dizilerini, muhtemelen, sadece alt alta ve rastgele bir şekilde
ekrana yazdırmakla yetinmeyeceksiniz. Bu karakter dizilerini, yazdığınız
programlarda kullanabilmek için, programınıza uygun şekillerde biçimlendirmeniz
gerekecek. Dilerseniz neden bahsettiğimizi daha net bir şekilde anlatabilmek
için çok basit bir örnek verelim.

Diyelim ki, yazdığınız bir programda kullanmak üzere, kullanıcıdan isim bilgisi
almanız gerekiyor. Programınızın işleyişi gereğince, eğer isim `5` karakterse
veya bundan küçükse ismin tamamı görüntülenecek, ama eğer isim `5` karakterden
büyükse `5` karakteri aşan kısım yerine üç nokta işareti koyulacak. Yani eğer
isim `Fırat` ise bu ismin tamamı görüntülenecek. Ama eğer isim mesela `Abdullah`
ise, o zaman bu isim `Abdul...` şeklinde görüntülenecek.

Bu amaca ulaşmak için ilk denememizi yapalım::

    isim = input("isminiz: ")

    if len(isim) <= 5:
        print(isim[:5])
    else:
        print(isim[:5], "...")

Buradan elde ettiğimiz çıktı ihtiyacımızı kısmen karşılıyor. Ama çıktı tam
istediğimiz gibi değil. Çünkü normalde isme bitişik olması gereken üç nokta
işareti, isimden bir boşluk ile ayrılmış. Yani biz şöyle bir çıktı isterken::
    
    Abdul...

Şöyle bir çıktı elde ediyoruz::

    Abdul ...

Bu sorunu şu şekilde halledebiliriz::

    isim = input("isminiz: ")

    if len(isim) <= 5:
        print(isim[:5])
    else:
        print(isim[:5] + "...")

veya::

    isim = input("isminiz: ")

    if len(isim) <= 5:
        print(isim[:5])
    else:
        print(isim[:5], "...", sep="")

Yukarıdaki gibi basit durumlarda klasik karakter dizisi birleştirme yöntemlerini
kullanarak işinizi halledebilirsiniz. Ama daha karmaşık durumlarda, farklı
kaynaklardan gelen karakter dizilerini ihtiyaçlarınıza göre bir araya getirmek,
karakter dizisi birleştirme yöntemleri ile pek mümkün olmayacak veya çok zor
olacaktır.

Mesela şöyle bir durum düşünün:

Yazdığınız programda kullanıcıya bir parola soruyorsunuz. Amacınız bu parolanın,
programınızda belirlediğiniz ölçütlere uyup uymadığını tespit etmek. Eğer
kullanıcı tarafından belirlenen parola uygunsa ona şu çıktıyı göstermek
istiyorsunuz (parolanın `b5tY6g` olduğunu varsayalım)::
    
    Girdiğiniz parola (b5tY6g) kurallara uygun bir paroladır!

Bu çıktıyı elde etmek için şöyle bir kod yazabilirsiniz::

    parola = input("parola: ")

    print("Girdiğiniz parola (" + parola + ") kurallara uygun bir paroladır!")

Gördüğünüz gibi, sadece karakter dizisi birleştirme yöntemlerini kullanarak
istediğimiz çıktıyı elde ettik, ama farkettiyseniz bu defa işler biraz da olsa
zorlaştı.

Bir de uzun ve karmaşık bir metnin içine dışarıdan değerler yerleştirmeniz
gereken şöyle bir metinle karşı karşıya olduğunuzu düşünün::

    Sayın .........
    
    .... tarihinde yapmış olduğunuz, ........ hakkındaki başvurunuz incelemeye alınmıştır. 
    
    Size .... işgünü içinde cevap verilecektir. 
    
    
    Saygılarımızla,
    
    ......

Böyle bir metin içine dışarıdan değer yerleştirmek için karakter dizisi
birleştirme yöntemlerine başvurmak işinizi epey zorlaştıracaktır.

İşte klasik karakter dizisi birleştirme işlemlerinin yetersiz kaldığı veya
işleri büsbütün zorlaştırdığı bu tür durumlarda Python'ın size sunduğu 'karakter
dizisi biçimlendirme' araçlarından yararlanabilirsiniz.

Bunun için biz bu bölümde iki farklı yöntemden söz edeceğiz:
    
#. `%` işareti ile biçimlendirme 
#. ``format()`` metodu ile biçimlendirme. 

`%` işareti ile biçimlendirme, karakter dizisi biçimlendirmenin eski yöntemidir.
Bu yöntem ağırlıklı olarak Python'ın 3.x sürümlerinden önce kullanılıyordu. Ama
Python'ın 3.x sürümlerinde de bu yöntemi kullanma imkanımız var. Her ne kadar bu
yöntem Python3'te geçerliliğini korusa da muhtemelen ileride dilden tamamen
kaldırılacak. Ancak hem etrafta bu yöntemle yazılmış eski programlar olması, hem
de bu yöntemin halen geçerliliğini koruması nedeniyle bu yöntemi (kendimiz
kullanmayacak bile olsak) mutlaka öğrenmemiz gerekiyor.

``format()`` metodu ise Python'ın 3.x sürümleri ile dile dahil olan bir
özelliktir. Python'ın 2.x sürümlerinde bu metodu kullanamazsınız. Dilin
geleceğinde bu metot olduğu için, yeni yazılan kodlarda ``format()`` metodunu
kullanmak daha akıllıca olacaktır.

Biz bu sayfalarda yukarıda adını andığımız her iki yöntemi de inceleyeceğiz. İlk
olarak `%` işareti ile biçimlendirmeden söz edelim.

% İşareti ile Biçimlendirme (Eski Yöntem)
*****************************************

Daha önce de söylediğimiz gibi, Python programlama dilinin 3.x sürümlerinden
önce, bir karakter dizisini biçimlendirebilmek için `%` işaretinden
yararlanıyorduk. Bununla ilgili basit bir örnek verelim::
    
    parola = input("parola: ")
    
    print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)

Bu programı çalıştırıp parola girdiğinizde, yazdığınız parola çıktıda parantez
içinde görünecektir.

Yukarıdaki yapıyı incelediğimizde iki nokta gözümüze çarpıyor:

#. İlk olarak, karakter dizisinin içinde bir `%` işareti ve buna bitişik
   olarak yazılmış bir `s` harfi görüyoruz.  
   
#. İkincisi, karakter dizisinin dışında `%parola` gibi bir ifade daha var.

Rahatlıkla tahmin edebileceğiniz gibi, bu ifadeler birbiriyle doğrudan
bağlantılıdır. Dilerseniz bu yapıyı açıklamaya geçmeden önce bir örnek daha
verelim. Bu örnek sayesinde benim açıklamama gerek kalmadan karakter dizisi
biçimlendirme mantığını derhal kavrayacağınızı zannediyorum::
    
    print("%s ve %s iyi bir ikilidir!" %("Python", "Django"))

Dediğim gibi, bu basit örnek karakter dizilerinin nasıl biçimlendirildiğini
gayet açık bir şekilde gösteriyor. Dilerseniz yapıyı şöyle bir inceleyelim:

#. Python'da `%s` yapısı, karakter dizisi içinde bir yer tutma vazifesi görür. 

#. `%s` yapısı bir anlamda değişkenlere benzer. Tıpkı değişkenlerde olduğu
   gibi, `%s` yapısının değeri değişebilir.

#. Bir karakter dizisi içindeki her `%s` ifadesi için, karakter dizisi
   dışında bu ifadeye karşılık gelen bir değer olmalıdır. Python, karakter
   dizisi içinde geçen her `%s` ifadesinin yerine, karakter dizisi dışındaki
   her bir değeri tek tek yerleştirir. Bizim örneğimizde karakter dizisi
   içindeki ilk `%s` ifadesinin karakter dizisi dışındaki karşılığı `"Python"`;
   karakter dizisi içindeki ikinci `%s` ifadesinin karakter dizisi dışındaki
   karşılığı ise `"Django"`'dur.

#. Eğer karakter dizisi içindeki `%s` işaretlerinin sayısı ile karakter
   dizisi dışında bu işaretlere karşılık gelen değerlerin sayısı birbirini
   tutmazsa Python bize bir hata mesajı gösterecektir. Mesela:    

   .. parsed-literal::

        >>> print("Benim adım %s, soyadım %s" %"istihza")
        
        Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
        TypeError: not enough arguments for format string

Gördüğünüz gibi bu kodlar hata verdi. Çünkü karakter dizisi içindeki iki adet
`%s` ifadesine karşılık, karakter dizisinin dışında tek bir değer var
(`"istihza"`). Halbuki bizim şöyle bir kod yazmamız gerekiyordu:

    .. parsed-literal::

        >>> isim = "istihza"
        >>> print("%s adlı kişinin mekanı www.%s.com adresidir." %(isim, isim))

Bu defa herhangi bir hata mesajı almadık. Çünkü bu kodlarda, olması gerektiği
gibi, karakter dizisi içindeki iki adet `%s` ifadesine karşılık, dışarıda da iki
adet değer var.

Eğer karakter dizisi içinde tek bir `%s` ifadesi varsa, karakter dizisi dışında
buna karşılık gelen değeri gösterirken, bu değeri parantez içine almamıza gerek
yok. Ama eğer karakter dizisi içinde birden fazla `%s` işareti varsa, bunlara
karşılık gelen değerleri parantez içinde gösteriyoruz. Mesela yukarıdaki parola
örneğinde, karakter dizisinin içinde tek bir `%s` ifadesi var. Dolayısıyla
karakter dizisi dışında bu ifadeye karşılık gelen `parola` değişkenini parantez
içine almıyoruz. Ama `"Python"` ve `"Django"` örneğinde karakter dizisi içinde
iki adet `%s` ifadesi yer aldığı için, karakter dizisi dışında bu ifadelere
karşılık gelen `"Python"` ve `"Django"` kelimelerini parantez içinde
gösteriyoruz.

Bütün bu anlattıklarımızı sindirebilmek için dilerseniz bir örnek verelim::

    kardiz = "istihza"

    for sıra, karakter in enumerate(kardiz, 1):
        print("%s. karakter: '%s'" %(sıra, karakter))

Gördüğünüz gibi, `"istihza"` adlı karakter dizisi içindeki her bir harfin
sırasını ve harfin kendisini uygun bir düzen içinde ekrana yazdırdık. Karakter
sırasının ve karakterin kendisinin cümle içinde geleceği yerleri `%s` işaretleri
ile gösteriyoruz. Python da her bir değeri, ilgili konumlara tek tek
yerleştiriyor.

Hatırlarsanız önceki derslerimizde basit bir hesap makinesi örneği vermiştik.
İşte şimdi öğrendiklerimizi o programa uygularsak karakter dizisi
biçimlendiricileri üzerine epey pratik yapmış oluruz::
    
    giriş = """
        (1) topla
        (2) çıkar
        (3) çarp
        (4) böl
        (5) karesini hesapla
        (6) karekök hesapla
        """
    print(giriş)

    a = 1

    while a == 1:
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

        if soru == "q":
            print("çıkılıyor...")
            a = 0

        elif soru == "1":
            sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
            sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
            
            #İlk %s'ye karşılık gelen değer   : sayı1
            #İkinci %s'ye karşılık gelen değer: sayı2
            #Üçüncü %s'ye karşılık gelen değer: sayı1 + sayı2
            print("%s + %s = %s" %(sayı1, sayı2, sayı1 + sayı2))
            
        elif soru == "2":
            sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
            sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
            print("%s - %s = %s" %(sayı3, sayı4, sayı3 - sayı4))

        elif soru == "3":
            sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
            sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
            print("%s x %s = %s" %(sayı5, sayı6, sayı5 * sayı6))

        elif soru == "4":
            sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
            sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
            print("%s / %s = %s" %(sayı7, sayı8, sayı7 / sayı8))

        elif soru == "5":
            sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
            
            #İlk %s'ye karşılık gelen değer   : sayı9
            #İkinci %s'ye karşılık gelen değer: sayı9 ** 2
            print("%s sayısının karesi = %s" %(sayı9, sayı9 ** 2))

        elif soru == "6":
            sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
            print("%s sayısının karekökü = %s" %(sayı10, sayı10 ** 0.5))

        else:
            print("Yanlış giriş.")
            print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

Bu arada, gördüğünüz gibi, Python'da biçim düzenleyici olarak kullanılan simge
aynı zamanda 'yüzde' (`%`) anlamına da geliyor. O halde size şöyle bir soru
sorayım: Acaba `0`'dan `100`'e kadar olan sayıların başına birer yüzde işareti
koyarak bu sayıları nasıl gösterirsiniz? `%0`, `%1`, `%10`, `%15` gibi... Önce
şöyle bir şey deneyelim::
    
    >>> for i in range(100):
    ...     print("%s" %i)
    ...

Bu kodlar tabii ki sadece `0`'dan `100`'e kadar olan sayıları ekrana dökmekle
yetinecektir. Sayıların başında `%` işaretini göremeyeceğiz.

Bir de şöyle bir şey deneyelim::

    >>> for i in range(100):
    ...     print("%%s" %i)
    ...
    Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
    TypeError: not all arguments converted during string formatting

Bu defa da hata mesajı aldık. Halbuki doğru cevap şu olmalıydı::

    >>> for i in range(100):
    ...     print("%%%s" %i)
    ...

Burada `%` işaretini arka arkaya iki kez kullanarak bir adet `%` işareti elde
ettik. Daha sonra da normal bir şekilde `%s` biçimini kullandık. Yani üç adet
'%' işaretini yan yana getirmiş olduk.

Bütün bu örneklerden sonra, karakter dizisi biçimlendiricilerinin işimizi ne
kadar kolaylaştırdığını görmüş olmalısınız. İstediğimiz etkiyi elde etmek için
karakter dizisi biçimlendiricilerini kullanmak, karakter dizilerini birleştirme
işlemlerinden yararlanmaya göre çok daha esnek bir yöntemdir. Hatta bazı
durumlarda karakter dizisi biçimlendiricilerini kullanmak makul tek yöntemdir.

Yukarıda verdiğimiz örnekler, `%s` ile biçimlendirme konusunun en temel
yönlerini gösteriyor. Ama aslında bu aracı kullanarak çok daha karmaşık
biçimlendirme işlemleri de yapabiliriz.

Yani yukarıdaki örneklerde `%s` yapısını en basit şekilde mesela şöyle
kullandık::

    >>> print("Karakter dizilerinin toplam %s adet metodu vardır" %len(dir(str)))

Ama eğer istersek bundan daha karmaşık biçimlendirme işlemleri de
gerçekleştirebiliriz. Şu örneğe bakın::
    
    >>> for i in dir(str):
    ...     print("%15s" %i)

Gördüğünüz gibi `%` ile `s` işaretleri arasına bir sayı yerleştirdik. Bu sayı,
biçimlendirilecek karakter dizisinin toplam kaç karakterlik yer kaplayacağını
gösteriyor. Durumu daha net görebilmeniz için şöyle bir örnek verelim::
    
    >>> print("|%15s|" %"istihza")

    |        istihza|

Karakter dizisinin başına ve sonuna eklediğimiz '|' işaretleri sayesinde
karakter dizisinin nasıl ve ne şekilde hizalandığını daha belirgin bir şekilde
görebiliyoruz. Aslında yukarıdaki örneğin yaptığı iş size hiç yabancı değil.
Aynı etkiyi, karakter dizisi metotlarından ``rjust()`` ile de yapabileceğimizi
biliyorsunuz::
    
    >>> print("istihza".rjust(15))

Aynen yukarıdaki çıktıyı ``rjust()`` metodunu kullanarak elde etmek için ise
şöyle bir şey yazabilirsiniz::
    
    >>> print("|%s|" %"istihza".rjust(15))
    
    |        istihza|

Yukarıdaki örnekte `"istihza"` karakter dizisini sağa doğru yasladık. Sola
yaslamak için ise negatif sayılardan yararlanabilirsiniz::
    
    >>> print("|%-15s|" %"istihza")

    |istihza        |

Tıpkı biraz önce verdiğimiz örnekteki gibi, aynı etkiyi ``ljust()`` metoduyla da
elde edebilirsiniz::
    
    >>> print("|%s|" %"istihza".ljust(15))
    
    |istihza        |

Gördüğünüz gibi, `%s` yapısını farklı şekillerde kullanarak epey karmaşık
çıktılar elde edebiliyoruz. Ama aslında karakter dizisi biçimlendiricilerini
kullanarak yapabileceklerimiz bunlarla da sınırlı değildir. Mesela size şöyle
bir soru sorduğumu düşünün: Acaba aşağıdaki içeriğe sahip bir `HTML` şablonunu
nasıl elde edebiliriz?

::

    <html>
        <head>
            <title> {{ sayfa başlığı }} </title>
        </head>

        <body>
            <h1> {{ birinci seviye başlık }} </h1>
            <p>Web sitemize hoşgeldiniz! Konumuz: {{ konu }}</p>
        </body>
    </html>

Burada bütün değişkenler tek bir değere sahip olacak. Örneğin değişkenimiz
`Python Programlama Dili` ise yukarıdaki şablon şöyle bir `HTML` sayfası
üretecek::
    
    <html>
        <head>
            <title> Python Programlama Dili </title>
        </head>

        <body>
            <h1> Python Programlama Dili </h1>
            <p>Web sitemize hoşgeldiniz! Konumuz: Python Programlama Dili</p>
        </body>
    </html>

Aklınıza ilk olarak şöyle bir çözüm gelmiş olabilir::

    sayfa = """
    <html>
        <head>
            <title> %s </title>
        </head>

        <body>
            <h1> %s </h1>
            <p>Web sitemize hoşgeldiniz! Konumuz: %s</p>
        </body>
    </html>
    """

    print(sayfa % ("Python Programlama Dili", 
                   "Python Programlama Dili", 
                   "Python Programlama Dili"))

Bu gayet makul ve doğru bir çözümdür. Ancak gördüğünüz gibi yukarıdaki kodlarda
bizi rahatsız eden bir nokta var. Bu kodlarda aynı karakter dizisini (`"Python
Programlama Dili"`) üç kez tekrar ediyoruz. En baştan beri söylediğimiz gibi,
kod yazarken tekrarlardan olabildiğince kaçınmaya çalışmamız programımızın
performansını artıracaktır. Burada da tekrardan kaçınmak amacıyla şöyle bir kod
yazmayı tercih edebiliriz. Dikkatlice inceleyin::
    
    sayfa = """
    <html>
        <head>
            <title> %(dil)s </title>
        </head>

        <body>
            <h1> %(dil)s </h1>
            <p>Web sitemize hoşgeldiniz! Konumuz: %(dil)s</p>
        </body>
    </html>
    """

    print(sayfa % {"dil": "Python Programlama Dili"})

Gördüğünüz gibi, yukarıdaki kodlar bizi aynı karakter dizisini tekrar tekrar
yazma zahmetinden kurtardı. Peki ama nasıl? Gelin isterseniz bu yapıyı daha iyi
anlayabilmek için daha basit bir örnek verelim::
    
    print("depoda %(miktar)s kilo %(ürün)s kaldı" %{"miktar": 25,
                                                    "ürün": "elma"})

Burada şöyle bir yapıyla karşı karşıyayız::

    "%(değişken_adı)s" % {"değişken_adı": "değişken_değeri"}
    
`{"değişken_adı": "değişken_değeri"}` yapısıyla önceki derslerimizde
karşılaşmıştınız. Dolayısıyla bu yapının temel olarak ne işe yaradığını
biliyorsunuz. Hatta bu yapının adının 'sözlük' olduğunu da öğrenmiştiniz. İşte
burada, sözlük adlı veri tipinden yararlanarak değişken adları ile değişken
değerlerini eşleştirdik. Böylece aynı şeyleri tekrar tekrar yazmamıza gerek
kalmadı. Ayrıca yukarıdaki örnekte değerleri sırasına göre değil, ismine göre
çağırdığımız için, karakter dizisi içindeki değerlerin sırasını takip etme
zahmetinden de kurtulmuş olduk.

Böylece `%` yapısının tüm temel ayrıntılarını öğrenmiş olduk. Artık `%`
işaretinin başka yönlerini incelemeye başlayabiliriz.

Biçimlendirme Karakterleri
===========================

Biraz önce, Python'da eski usul karakter dizisi biçimlendirme yöntemi olan `%`
işareti üzerine en temel bilgileri edindik. Buraya kadar öğrendiklerimiz,
yazdığımız programlarda genellikle yolumuzu yordamımızı bulmamıza yetecektir.
Ama isterseniz şimdi karakter dizisi biçimlendirme konusunu biraz daha
derinlemesine ele alalım. Mesela Python'daki biçimlendirme karakterlerinin neler
olduğunu inceleyelim.

s
---

Önceki örneklerden de gördüğünüz gibi, Python'da biçim düzenleme işlemleri için
`%s` adlı bir yapıdan faydalanıyoruz. Bu yapıyı şöyle bir masaya yatırdığımızda
aslında bu yapının iki parçadan oluştuğunu görebiliriz. Bu parçalar `%` ve `s`
karakterleridir. Burada gördüğümüz parçalardan `%` sabit, `s` ise değişkendir.
Yani `%` sabit değerini bazı harflerle birlikte kullanarak, farklı karakter
dizisi biçimlendirme işlemleri gerçekleştirebiliriz.

Biz önceki sayfalarda verdiğimiz örneklerde bu simgeyi `s` harfiyle birlikte
kullandık. Örneğin::

    >>> print("Benim adım %s" %"istihza")

Bu kodlardaki `s` karakteri İngilizce *string*, yani 'karakter dizisi'
ifadesinin kısaltmasıdır. Esasında en yaygın çift de budur. Yani etraftaki
Python programlarında yaygın olarak `%s` yapısını görürüz. Ancak Python'da `%`
biçim düzenleyicisiyle birlikte kullanılabilecek tek karakter `s` değildir. Daha
önce de dediğimiz gibi, `s` karakteri *string*, yani 'karakter dizisi'
ifadesinin kısaltmasıdır. Yani aslında `%s` yapısı Python'da özel olarak
karakter dizilerini temsil eder.

Peki bu ne demek oluyor? 

Bir karakter dizisi içinde `%s` yapısını kullandığımızda, dışarıda buna karşılık
gelen değerin de bir karakter dizisi veya karakter dizisine çevrilebilecek bir
değer olması gerekir. Python'da her şey bir karakter dizisi olarak temsil
edilebilir. Dolayısıyla bütün işlemlerinizde `%` işaretini `s` karakteri ile
birlikte kullanabilirsiniz. Ama bazı özel durumlarda `%` işaretini `s` dışında
başka harflerle birlikte kullanmanız da gerekebilir.

Biz `%` yapısı ile ilgili verdiğimiz ilk örneklerde bu yapının `s` karakteri ile
birlikte kullanılışını gösteren pek çok örnek verdiğimiz için `%` ile `s`
birlikteliği üzerinde daha fazla durmayacağız. Bunun yerine, `%` ile birlikte
kullanılan öteki karakterleri inceleyeceğiz. O halde yola koyulalım.

d
---

Bir önceki başlıkta gördüğümüz `s` harfi nasıl karakter dizilerini temsil
ediyorsa, `d` harfi de sayıları temsil eder. İsterseniz küçük bir örnekle
açıklamaya çalışalım durumu::
    
    >>> print("Şubat ayı bu yıl %d gün çekiyor" %28)

    Şubat ayı bu yıl 28 gün çekiyor.

Gördüğünüz gibi, `%` işaretiyle birlikte bu defa `s` yerine `d` harfini
kullandık. Buna uygun olarak da dış tarafta `28` sayısını kullandık. Peki
yukarıdaki ifadeyi şöyle de yazamaz mıydık? ::
    
    >>> print("Şubat ayı bu yıl %s gün çekiyor" %28)

Elbette yazabilirdik. Bu kod da bize doğru çıktı verecektir. Çünkü daha önce de
dediğimiz gibi, `s` harfi karakter dizilerini ve karakter dizisine çevrilebilen
değerleri temsil eder. Python'da sayılar karakter dizisine çevrilebildiği için
`%s` gibi bir yapıyı hata almadan kullanabiliyoruz. Ama mesela şöyle bir şey
yazamayız::
    
    >>> print("Şubat ayı bu yıl %d gün çekiyor" %"yirmi sekiz")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: %d format: a number is required, not str

Gördüğünüz gibi bu defa hata aldık. Çünkü `d` harfi yalnızca sayı değerleri
temsil edebilir. Bu harfle birlikte karakter dizilerini kullanamayız.

Doğrusunu söylemek gerekirse, `d` harfi aslında tam sayı (*integer*) değerleri
temsil eder. Eğer bu harfin kullanıldığı bir karakter dizisinde değer olarak
mesela bir kayan noktalı sayı (*float*) verirsek, bu değer tamsayıya
çevrilecektir. Bunun ne demek olduğunu hemen bir örnekle görelim::
    
    >>> print("%d" %13.5)
    
    13

Gördüğünüz gibi, `%d` ifadesi, `13.5` sayısının ondalık kısmını çıktıda
göstermiyor. Çünkü `d` harfi sadece tamsayıları temsil etme işlevi görüyor.

Burada şöyle bir soru aklınıza gelmiş olabilir: 'Acaba `%d` ifadesi ile hiç
uğraşmasak, bunun yerine her yerde `%s` ifadesini kullansak olmaz mı?'.

Çoğu zaman olur, ama mesela şöyle bir durum düşünün: Yazdığınız programda
kullanıcıdan sadece tam sayı girmesini istiyor olabilirsiniz. Yani mesela
kullanıcının ondalık sayı girmesi halinde, siz bu sayının sadece tam sayı
kısmını almak istiyor olabilirsiniz. Örneğin kullanıcı `23.8` gibi bir sayı
girmişse, siz bu sayıda ihtiyacınız olan `23` kısmını almak isteyebilirsiniz.
İşte bu `%d` işaretinden yararlanarak, kullanıcının girdiği ondalık sayının
sadece tam sayı kısmını çekebilirsiniz::
    
    sayı = input("sayı: ")

    print("%d" %float(sayı))
    
Elbette Python'da bir ondalık sayının sadece taban kısmını almanın başka
yöntemleri de vardır. Ama yukarıda verdiğimiz örnek bir ondalık sayının sadece
tabanını almanın gayet basit ve etkili bir yoludur.

`%s` yapısını anlatırken gösterdiğimiz ileri düzey biçimlendirme tekniklerini
`%d` ile de kullanabilirsiniz. Örneğin::

    >>> print("|%7d|" %23)

    |     23|
    
    >>> print("|%-7d|" %23)
    
    |23     |

veya::

    >>> print("%(sayı)d" % {"sayı": 23})
    
    23

`%s` yapısına ek olarak, sayının kaplayacağı alandaki boşluklara birer `0` da
yerleştirebilirsiniz::
    
    >>> print("%05d" %23)

    00023

...veya::
    
    >>> print("%.5d" %23)
    
    00023

Hatta hem sayının kaplayacağı boşluk miktarını hem de bu boşlukların ne
kadarının `0` ile doldurulacağını da belirleyebilirsiniz::
    
    >>> print("%10.5d" %23)
    
         00023

Burada `23` sayısının toplam `10` boşlukluk bir yer kaplamasını ve bu `10` adet
boşluğun `5` tanesinin içine `0` sayılarının ve `23` sayısının sığdırılmasını
istedik.

Bir de şuna bakalım::

    >>> print("%010.d" %23)
    
    0000000023

Burada ise `23` sayısının toplam `10` boşlukluk bir yer kaplamasını ve bu `10`
adet boşluğa `23` sayısı yerleştirildikten sonra arta kalan kısmın `0` sayıları
ile doldurulmasını istedik.

Bu arada, son örnekte yaptığımız şeyi, daha önce öğrendiğimiz ``zfill()``
metoduyla da yapabileceğimizi biliyorsunuz::

    >>> "23".zfill(10)

    '0000000023'
    
Yukarıdaki kullanımlar ilk bakışta gözünüze karışık görünmüş olabilir. Ama eğer
yeterince pratik yaparsanız, aslında bu biçimlerin hiç de o kadar karmaşık
olmadığını anlarsınız. İsterseniz bu biçimlerle neler yapabileceğimizi şöyle bir
kısaca tarif edelim:

`d` harfi, `%` işaretiyle birlikte kullanıldığında sayıları temsil eder. Bu iki
karakterin en temel kullanımı şöyledir::

    >>> "%d" %10
    
    '10'

`d` harfi ile `%` işareti arasına bir pozitif veya negatif sayı getirerek,
temsil edilecek sayının toplam kaç boşluktan oluşan bir alan içine
yerleştirileceğini belirleyebiliyoruz::
    
    >>> "%5d" %10
    
    '   10'

Burada `10` sayısını toplam `5` boşlukluk bir alan içine yerleştirdik.
Gördüğünüz gibi, bir pozitif sayı kullandığımızda, sayımız kendisine ayrılan
alan içinde sağa yaslanıyor. Eğer bu sayıyı sola yaslamak istersek negatif
sayılardan yararlanabiliriz::
    
    >>> "%-5d" %10
    
    '10   '

Eğer sağa yasladığımız bir sayının sol tarafını sıfırla doldurmak istersek,
hizalama miktarını belirtmek için kullandığımız sayının soluna bir sıfır
ekleyebiliriz::
    
    >>> "%05d" %10
    
    '00010'

Aynı etkiyi şu şekilde de elde edebilirsiniz::

    >>> "%.5d" %10
    
    '00010'

Eğer nokta işaretinden önce bir sayı belirtirseniz, karakter dizisi o
belirttiğiniz sayı kadar sağa yaslanacaktır. Yani::
    
    >>> "%10.5d" %10
    
    '     00010'

... veya sola::

    >>> "%-10.5d" %10
    
    '00010     '

Her iki şekilde de, karakter dizisini toplam `10` boşluktan oluşan bir alan
içine yerleştirmiş olduk. Bu toplam alanın `5` boşlukluk kısmı sayının kendisi
ve sayının soluna gelecek `0`'lar arasında paylaştırıldı.

Gördüğünüz gibi, biçimlendirme mantığının aslında o kadar da korkulacak bir yanı
yok. Kendi kendinize yukarıdakilere benzer örnekler yaparak bu yapıyı daha iyi
bir şekilde anlamaya çalışabilirsiniz.

i
----

Bu harf de *integer*, yani 'tam sayı' kelimesinin kısaltmasıdır. Kullanım ve
işlev olarak, `d` harfinden hiç bir farkı yoktur.

o
------

Bu harf *octal* (sekizli) kelimesinin kısaltmasıdır. Adından da anlaşılacağı
gibi, sekizli düzendeki sayıları temsil eder. Dolayısıyla bu harfi kullanarak
onlu düzendeki bir sayıyı sekizli düzendeki karşılığına dönüştürebilirsiniz.
Örneğin::
    
    >>> print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10))
    
    10 sayısının sekizli düzendeki karşılığı 12 sayısıdır.

.. note:: `%d` yapısını anlatırken gösterdiğimiz ileri düzey biçimlendirme
          tekniklerinin tamamını `%o` ile de kullanabilirsiniz.
          
x 
------

Bu harf *hexadecimal*, yani onaltılı düzendeki sayıları temsil eder.
Dolayısıyla bu harfi kullanarak onlu düzendeki bir sayıyı onaltılı düzendeki
karşılığına çevirebilirsiniz::
    
    >>> print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20))
    
    20 sayısının onaltılı düzendeki karşılığı 14 sayısıdır.

Buradaki 'x' küçük harf olarak kullanıldığında, onaltılı düzende harfle
gösterilen sayılar da küçük harfle temsil edilecektir::
    
    >>> print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(10, 10))
    
    10 sayısının onaltılı düzendeki karşılığı a sayısıdır.

.. note:: `%d` yapısını anlatırken gösterdiğimiz ileri düzey biçimlendirme
          tekniklerinin tamamını `%x` ile de kullanabilirsiniz.

X 
------

Bu da tıpkı `x` harfinde olduğu gibi, onaltılı düzendeki sayıları temsil eder.
Ancak bunun farkı, harfle gösterilen onaltılı sayıları büyük harfle temsil
etmesidir::
    
    >>> print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." %(10, 10))
    
    10 sayısının onaltılı düzendeki karşılığı A sayısıdır.

.. note:: `%d` yapısını anlatırken gösterdiğimiz ileri düzey biçimlendirme
          tekniklerinin tamamını `%X` ile de kullanabilirsiniz.

f 
-----

Python'da karakter dizilerini biçimlendirirken `s` harfinden sonra en çok
kullanılan harf `f` harfidir. Bu harf İngilizce'deki *float*, yani 'kayan
noktalı sayı' kelimesinin kısaltmasıdır. Adından da anlaşılacağı gibi, karakter
dizileri içindeki kayan noktalı sayıları temsil etmek için kullanılır. ::
    
    >>> print("Dolar %f TL olmuş..." %1.4710)
    
    Dolar 1.471000 TL olmuş...

Bu çıktı sizi biraz şaşırtmış olabilir. Çünkü gördüğünüz gibi, çıktıda bizim
eklemediğimiz haneler var.

Python'da bir karakter dizisi içindeki sayıyı `%f` yapısı ile kayan noktalı
sayıya çevirdiğimizde noktadan sonra öntanımlı olarak `6` hane yer alacaktır.
Yani mesela::
    
    >>> print("%f" %10)
    
    10.000000

Gördüğünüz gibi, gerçekten de `10` tam sayısı `%f` yapısı ile kayan noktalı
sayıya dönüştürüldüğünde noktadan sonra `6` adet sıfıra sahip oluyor.

Başka bir örnek daha verelim::

    >>> print("%f"%23.6)
    
    23.600000

Bu örnek, `%f` yapısının, kayan noktalı sayıların noktadan sonraki hane sayısını
da `6`'ya tamamladığını gösteriyor. Ama elbette biz istersek, daha önce
öğrendiğimiz teknikleri kullanarak, noktadan sonra kaç hane olacağını
belirleyebiliriz::
    
    >>> print("%.2f" % 10)
    
    10.00

`%f` yapısında, `%` ile `f` arasına `.2` gibi bir ifade yerleştirerek noktadan
sonra `2` hane olmasını sağladık.

.. note:: Daha önce gösterdiğimiz ileri düzey biçimlendirme tekniklerini `%f`
          ile de kullanabilirsiniz.

c 
-----

Bu harf de Python'daki önemli karakter dizisi biçimlendiricilerinden biridir. Bu
harf tek bir karakteri temsil eder::
    
    >>> print("%c" %"a")
    
    a

Ama::

    >>> print("%c" %"istihza")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: %c requires int or char

Gördüğünüz gibi, `c` harfi sadece tek bir karakteri kabul ediyor. Karakter
sayısı birden fazla olduğunda bu komut hata veriyor.

`c` harfinin bir başka özelliği de ASCII tablosunda sayılara karşılık gelen
karakterleri de gösterebilmesidir::

    >>> print("%c" %65)
    
    A

ASCII tablosunda 65 sayısı 'A' harfine karşılık geldiği için yukarıdaki komutun
çıktısı 'A' harfini gösteriyor. Eğer isterseniz `c` harfini kullanarak bütün
ASCII tablosunu ekrana dökebilirsiniz::
    
    >>> for i in range(128):
    ...     print("%s ==> %c" %(i, i))

.. note:: `%s` yapısını anlatırken gösterdiğimiz ileri düzey biçimlendirme
          tekniklerinin tamamını `%c` ile de kullanabilirsiniz.

Böylece Python'da `%` işareti kullanarak nasıl biçimlendirme yapabileceğimizi
öğrenmiş olduk. Dilerseniz pratik olması açısından, karakter dizisi
biçimlendiricilerinin kullanımını gösteren bir örnek vererek bu bölümü
noktalayalım.

Dikkatlice inceleyin::

    for sıra, karakter in enumerate(dir(str)):
        if sıra % 3 == 0:
            print("\n", end="")
        print("%-20s" %karakter, end="")

Burada, gördüğünüz gibi, karakter dizisi metotlarını bir tablo görünümü içinde
ekrana yazdırdık. Şu satırlar yardımıyla tablodaki sütun sayısını `3` olarak
belirledik::
    
    if sıra % 3 == 0:
        print("\n", end="")

Burada modülüs işlecini nasıl kullandığımıza çok dikkat edin. `sıra`
değişkeninin değerini `3`'e böldüğümüzde kalan değerin `0` olduğu her sayıda
satır başına geçiyoruz. Böylece her `3.` sütunda bir satır aşağı geçilmiş
oluyor.

Bununla ilgili bir örnek daha verelim::

    for i in range(20):
        print("%5d%5o%5x" %(i, i, i))

Burada `0`'dan `20`'ye kadar olan sayıların onlu, sekizli ve onaltılı düzendeki
karşılıklarını bir tablo görünümü içinde ekrana çıktı verdik. Bu arada, eğer
isterseniz yukarıdaki kodları şöyle de yazabileceğinizi biliyorsunuz::
    
    for i in range(20):
        print("%(deger)5d%(deger)5o%(deger)5x" %({"deger": i}))

Burada da, tablomuzu biçimlendirmek için 'sözlük' adını verdiğimiz yapıdan
yararlandık.

format() Metodu ile Biçimlendirme (Yeni Yöntem)
*************************************************

En başta da söylediğimiz gibi, `%` işaretini kullanarak karakter dizisi
biçimlendirme eskide kalmış bir yöntemdir. Bu yöntem ağırlıklı olarak Python'ın
2.x sürümlerinde kullanılıyordu. Her ne kadar bu yöntemi Python'ın 3.x
sürümlerinde de kullanmak mümkün olsa da yeni yazılan kodlarda bu yöntem yerine
biraz sonra göreceğimiz ``format()`` metodunu kullanmak çok daha akıllıca
olacaktır. Çünkü muhtemelen `%` ile biçimlendirme yöntemi, ileriki bir Python
sürümünde dilden tamamen kaldırılacak. Bu yüzden bu eski metoda fazla bel
bağlamamak gerekiyor.

Daha önceki derslerimizde verdiğimiz örnekler sayesinde ``format()`` metodunun
temel olarak nasıl kullanılacağını biliyoruz. Ama isterseniz biz yine de
bütünlük açısından ``format()`` metodunun temel kullanımını burada tekrar ele
alalım.

``format()`` metodunu en basit şekilde şöyle kullanıyoruz::

    >>> print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))
    
    Django ve Python iyi bir ikilidir!

Gördüğünüz gibi, eski yöntemdeki `%` işaretine karşılık, yeni yöntemde `{}`
işaretini kullanıyoruz.

Çok basit bir örnek daha verelim::

    isim = input("İsminiz: ")
    print("Merhaba {}. Nasılsın?".format(isim))

Elbette bu örneği şu şekilde de yazabilirdik::

    isim = input("İsminiz: ")
    print("Merhaba", isim + ".", "Nasılsın?")

Burada ``format()`` metodunu ve biçim düzenleyicileri hiç kullanmadan, sadece
karakter dizilerini birleştirerek istediğimiz çıktıyı elde ettik. Ama siz de
görüyorsunuz; karakter dizilerini birleştirmekle uğraşacağımıza ``format()``
metodunu kullanmak hem daha pratiktir, hem de bu şekilde yazdığımız kodlar daha
okunaklı olur.

Yukarıdaki örnekte ``format()`` metodunu tek bir parametre ile birlikte
kullandık (`isim`). Bu parametre (tıpkı eski `%` işaretinde olduğu gibi),
karakter dizisi içindeki `{}` işaretine karşılık geliyor.

Bu konuyu daha iyi anlayabilmek için bir örnek daha verelim::

    kalkış       = input("Kalkış yeri: ")
    varış        = input("Varış yeri: ")
    isim_soyisim = input("İsim ve soyisim: ")
    bilet_sayısı = input("Bilet sayısı: ")

    print("""{} noktasından {} noktasına, 14:30 hareket saatli 
    sefer için {} adına {} adet bilet ayrılmıştır!""".format(kalkış, 
                                                             varış, 
                                                             isim_soyisim, 
                                                             bilet_sayısı)) 

Gördüğünüz gibi, `{}` işaretleri karakter dizisi içinde bir 'yer tutma' görevi
görüyor. Tutulan bu yerlere nelerin geleceğini ``format()`` metodunun
parametreleri vasıtasıyla belirliyoruz.

Elbette eğer isterseniz yukarıdaki örneği şu şekilde de yazabilirsiniz::

    kalkış       = input("Kalkış yeri: ")
    varış        = input("Varış yeri: ")
    isim_soyisim = input("İsim ve soyisim: ")
    bilet_sayısı = input("Bilet sayısı: ")

    metin = "{} noktasından {} noktasına, 14:30 hareket saatli \
    sefer için {} adına {} adet bilet ayrılmıştır!"

    print(metin.format(kalkış, varış, isim_soyisim, bilet_sayısı)) 

Ancak yaygın olarak kullanılan yöntem, karakter dizisini herhangi bir değişkene
atamadan, doğrudan ``format()`` metoduna bağlamaktır. Elbette hangi yöntem
kolayınıza geliyorsa onu tercih etmekte özgürsünüz. Ama özellikle
biçimlendirilecek karakter dizisinin çok uzun olduğu durumlarda, yukarıdaki
gibi, karakter dizisini önce bir değişkene atayıp, sonra da bu değişken üzerine
``format()`` metodunu uygulamak daha mantıklı olabilir.

Verdiğimiz bu örneği, her zaman olduğu gibi, ``format()`` metoduna başvurmadan
yazmak da mümkündür::

    kalkış       = input("Kalkış yeri: ")
    varış        = input("Varış yeri: ")
    isim_soyisim = input("İsim ve soyisim: ")
    bilet_sayısı = input("Bilet sayısı: ")

    print(kalkış, "noktasından", varış, "noktasına, 14:30 hareket saatli \
    sefer için", isim_soyisim, "adına", bilet_sayısı, "adet bilet ayrılmıştır!") 

Tıpkı daha önce verdiğimiz örnekte olduğu gibi, burada da ``format()`` metodunu
kullanmak karakter dizilerini birleştirme yöntemine göre daha mantıklı ve kolay
görünüyor. Ayrıca bir karakter dizisi karmaşıklaştıkça bu karakter dizisini
sadece karakter dizisi birleştirme yöntemleriyle biçimlendirmeye çalışmak bir
süre sonra tam bir eziyet halini alabilir. O yüzden, 'Ben ``format()`` metodunu
öğrenmesem de olur,' diye düşünmeyin sakın. Mesela şöyle bir programı
``format()`` metodu kullanmadan yazmaya çalışmak hiç akıl kârı değildir::
    
    kodlama  = "utf-8"
    site_adı = "Python Programlama Dili"
    dosya    = open("deneme.html", "w", encoding=kodlama)
    içerik   = """
    <html>

    <head> 
        <meta http-equiv="Content-Type" content="text/html; charset={}" /> 
        <title>{}</title>
    </head> 

    <body>
        <h1>istihza.com web sitesine hoş geldiniz!</h1>
        <p><b>{}</b> için bir Türkçe belgelendirme projesi...</p>
    </body>

    </html>
    """

    print(içerik.format(kodlama, site_adı, site_adı), file=dosya)

    dosya.close()

Burada şu satırın bir kısmı hariç bütün kodları anlayabilecek düzeydesiniz::
    
    dosya  = open("deneme.html", "w", encoding=kodlama)

Bu kodlarla, `deneme.html` adlı bir dosya oluşturduğumuzu biliyorsunuz. Daha
önceki derslerimizde birkaç kez gördüğümüz ``open()`` fonksiyonu Python'da dosya
oluşturmamıza imkan veriyor. Bu fonksiyon içinde kullandığımız üç parametrenin
ilk ikisi size tanıdık gelecektir. İlk parametre dosyanın adını, ikinci
parametre ise bu dosyanın hangi kipte açılacağını gösteriyor. Burada
kullandığımız `"w"` parametresi `deneme.html` adlı dosyanın yazma kipinde
açılacağını gösteriyor. Bu fonksiyona atadığımız `encoding` parametresi ise
oluşturulacak dosyanın kodlama biçimini gösteriyor. Bu da Türkçe karakterlerin
dosyada düzgün görüntülenebilmesi açısından önem taşıyor.

Küme parantezlerini, yukarıdaki örneklerde görüldüğü şekilde içi boş olarak
kullanabilirsiniz. Böyle bir durumda Python, karakter dizisi içindeki küme
parantezleriyle, karakter dizisi dışındaki değerleri teker teker ve sırasıyla
eşleştirecektir. Ama isterseniz küme parantezleri içine birer sayı yazarak,
karakter dizisi dışındaki değerlerin hangi sırayla kullanılacağını
belirleyebilirsiniz. Örneğin::
    
    >>> "{0} {1}".format("Fırat", "Özgül")
    
    'Fırat Özgül'

Küme parantezleri içinde sayı kullanabilme imkanı sayesinde değerlerin sırasını
istediğiniz gibi düzenleyebilirsiniz::
    
    >>> "{1} {0}".format("Fırat", "Özgül")
    
    'Özgül Fırat'

Hatta bu özellik sayesinde değerleri bir kez yazıp, birden fazla sayıda tekrar
edebilirsiniz::
    
    >>> "{0} {1} ({1} {0})".format("Fırat", "Özgül")
    
    'Fırat Özgül (Özgül Fırat)'

Dolayısıyla, `{}` işaretleri içinde öğelerin sırasını da belirterek, biraz önce
verdiğimiz `HTML` sayfası örneğini şu şekilde yazabilirsiniz::
    
    kodlama  = "utf-8"
    site_adı = "Python Programlama Dili"
    dosya    = open("deneme.html", "w", encoding=kodlama)
    içerik   = """
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset={0}" />
        <title>{1}</title>
    </head>

    <body>
        <h1>istihza.com web sitesine hoş geldiniz!</h1>
        <p><b>{1}</b> için bir Türkçe belgelendirme projesi...</p>
    </body>

    </html>
    """

    print(içerik.format(kodlama, site_adı), file=dosya)

    dosya.close()

Gördüğünüz gibi, öğelerin sıra numarasını belirtmemiz sayesinde, karakter dizisi
içinde iki kez ihtiyaç duyduğumuz `site_adı` adlı değişkeni ``format()`` metodu
içinde iki kez yazmak zorunda kalmadık.

Yukarıdaki örnekler bize, ``format()`` metodunun parametrelerine sıra numarasına
göre erişebileceğimizi gösteriyor. Biz aynı zamanda bu metodun parametrelerine
isme göre de erişebiliriz. Çok basit bir örnek::
    
    print("{dil} dersleri".format(dil="python"))

Bu yöntemi kullanarak, aynı değişkeni birkaç farklı yerde kullanabilirsiniz::

    sayfa = """
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>{konu}</title>
    </head>

    <body>
        <h1>istihza.com web sitesine hoş geldiniz!</h1>
        <p><b>{konu}</b> için bir Türkçe belgelendirme projesi...</p>
    </body>

    </html>
    """

    print(sayfa.format(konu="Python Programlama Dili"))

``format()`` metodunun yetenekleri yukarıda gösterdiğimiz şeylerle sınırlı
değildir. Tıpkı eski biçimlendirme yönteminde olduğu gibi, `{}` işaretleri
arasında bazı sayılar kullanarak, karakter dizileri üzerinde hizalama işlemleri
de yapabiliriz.

Dikkatlice bakın::

    >>> print("{:>15}".format("istihza"))
    
            istihza

Bu gösterim gözünüze oldukça yabancı ve karışık gelmiş olabilir. Ama aslında hiç
de öyle anlaşılmaz bir yanı yoktur bu kodların. Gördüğünüz gibi, burada
öncelikle `:` adlı bir işaretten yararlanıyoruz. Bu işaretin ardından `>` adlı
başka bir işaret görüyoruz. Son olarak da `15` sayısını kullanıyoruz.

`:` işareti, bir biçimlendirme işlemi yapacağımızı gösteriyor. `>` işareti ise
bu biçimlendirmenin bir hizalama işlemi olacağını haber veriyor. En sondaki `15`
sayısı ise bu hizalama işleminin 15 karakterlik bir alan ile ilgili olduğunu
söylüyor. Bu şekilde karakter dizisini `15` karakterlik bir alan içine
yerleştirip karakter dizisini sağa yasladık. Yukarıdaki çıktıyı daha iyi
anlayabilmek için kodları şöyle de yazabilirsiniz::
    
    >>> print("|{:>15}|".format("istihza"))

    |       istihza|
    
Gördüğünüz gibi, karakter dizimiz, kendisine ayrılan `15` karakterlik alan
içinde sağa yaslanmış vaziyette duruyor.

Eğer aynı karakter dizisini sola yaslamak isterseniz şöyle bir şey
yazabilirsiniz::

    >>> print("|{:<15}|".format("istihza"))

    |istihza        |

Bu defa `<` adlı işaretten yararlandığımıza dikkat edin.

Yukarıdaki yöntemi kullanarak, karakter dizilerini sola veya sağa yaslamanın
yanısıra, kendilerine ayrılan alan içinde ortalayabilirsiniz de::
    
    >>> print("|{:^15}|".format("istihza"))
    
    |    istihza    |

Gördüğünüz gibi, python3 ile gelen ``format()`` metodunu hizalama işlemleri için
kullanırken üç farklı işaretten yararlanıyoruz:

    +-----+-----------------------------------+
    | `>` |  sağa yaslama                     |
    +-----+-----------------------------------+
    | `<` |  sola yaslama                     |
    +-----+-----------------------------------+
    | `^` |  ortalama                         |
    +-----+-----------------------------------+

Yukarıdaki işaretler, yaptıkları işi çağrıştırdıkları için, bunları akılda
tutmak çok zor olmasa gerek. Mesela örnek olması açısından, eski biçimlendirme
yönteminin son kısmında verdiğimiz şu örneği::
    
    for sıra, karakter in enumerate(dir(str)):
        if sıra % 3 == 0:
            print("\n", end="")
        print("%-20s" %karakter, end="")

... bir de yeni ``format()`` metoduyla yazalım::

    for sıra, karakter in enumerate(dir(str)):
        if sıra % 3 == 0:
            print("\n", end="")
        print("{:<20}".format(karakter), end="")

Bu örneği inceleyerek, eski ile yeni yöntem arasında nelerin değiştiğini, neyin
neye karşılık geldiğini görebilirsiniz.

Biçimlendirme Karakterleri
=============================

Hatırlarsanız Python2'de geçerli olan eski biçimlendirme yönteminde `%`
karakteri ile bazı harfleri birlikte kullanarak karakter dizileri üzerinde
biçimlendirme ve dönüştürme işlemleri yapabiliyorduk. Aynı şey Python3 ile
birlikte gelen bu ``format()`` metodu için de geçerlidir. Yani benzer harfleri
kullanarak ``format()`` metodu ile de karakter dizileri üzerinde biçimlendirme
ve dönüştürme işlemleri yapabiliriz.

``format()`` metodu ile birlikte şu harfleri kullanabiliyoruz:

s
-----

Bu harf karakter dizilerini temsil eder. 

Yalnız bu biçimlendirici karakterlerin `{}` işaretleri içindeki kullanımı ilk
bakışta gözünüze biraz karışık gelebilir::
    
    >>> print("{:s}".format("karakter dizisi"))
    
    karakter dizisi

Bu arada, harfleri `{}` yapısının içinde nasıl kullandığımıza dikkat edin.
Gördüğünüz gibi biçimlendirme karakterini kullanırken, karakterin sol tarafına
bir adet `:` işareti de yerleştiriyoruz. Bir örnek verelim::
    
    print("{:s} ve {:s} iyi bir ikilidir!".format("Python", "Django")) 

Yalnız, `s` harfi karakter dizilerini temsil ettiği için, `{}` işaretleri
arasında bu harfi kullandığımızda, ``format()`` metodunun alabileceği
parametreyi karakter dizisiyle sınırlandırmış oluruz. Dolayısıyla bu harfi
kullandıktan sonra ``format()`` metodu içinde sadece karakter dizilerini
kullanabiliriz. Eğer sayı kullanırsak Python bize bir hata mesajı
gösterecektir::
    
    >>> print("{:s}".format(12))
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Unknown format code 's' for object of type 'int'

Bu yüzden, eğer amacınız ``format()`` metoduna parametre olarak karakter dizisi
vermekse, `{}` işaretleri içinde herhangi bir harf kullanmamak daha akıllıca
olabilir::
    
    print("{} ve {} iyi bir ikilidir!".format("Python", "Django"))

c
------

Bu harf `0` ile `256` arası sayıların ASCII tablosundaki karşılıklarını temsil
eder::
    
    >>> print("{:c}".format(65))

    A

d
------

Bu harf sayıları temsil eder::

    >>> print("{:d}".format(65))
    
    65
    
Eğer sayı dışında bir değer kullanırsanız Python size bir hata mesajı gösterir::
    
    >>> print("{:d}".format("65"))

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Unknown format code 'd' for object of type 'str'

o
-----

Bu harf onlu düzendeki sayıları sekizli düzendeki karşılıklarına çevirir::

    >>> print("{:o}".format(65))

    101

x
-----

Bu harf onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir::

    >>> print("{:x}".format(65))

    41


X
-----

Tıpkı `x` harfinde olduğu gibi, bu harf de onlu düzendeki sayıları onaltılı
düzendeki karşılıklarına çevirir::
    
    >>> "{:X}".format(65)
    
    '41'

Peki `x` ile `X` harfi arasında ne fark var? Fark şudur: `x`; onaltılı düzende
harfle gösterilen sayıları küçük harf şeklinde temsil eder. `X` işareti bu
sayıları büyük harf şeklinde temsil eder. Bu ikisi arasındaki farkı daha net
görmek için şöyle bir kod yazabilirsiniz::
    
    >>> for i in range(20):
    ...     print("{:x}{:10X}".format(i, i))
    ...
    0         0
    1         1
    2         2
    3         3
    4         4
    5         5
    6         6
    7         7
    8         8
    9         9
    a         A
    b         B
    c         C
    d         D
    e         E
    f         F
    10        10
    11        11
    12        12
    13        13

Gördüğünüz gibi gerçekten de `x` harfi onaltılı düzende harflerle gösterilen
sayıları küçük harf olarak; `X` harfi ise büyük harf olarak temsil ediyor.

b
---

Bu işaret, onlu düzendeki sayıları ikili düzendeki karşılıklarına çevirir::
    
    >>> "{:b}".format(2)
    
    '10'

f
---

Bu işaret, eski biçimlendirme yöntemini anlatırken gösterdiğimiz `f` işaretiyle
benzer bir işleve sahiptir::
    
    print("{:.2f}".format(50))
    
    50.00


,
---

`:` işaretini `,` işareti (basamak ayracı) ile birlikte kullanarak, sayıları
basamaklarına ayırabilirsiniz::
    
    >>> "{:,}".format(1234567890)
    
    '1,234,567,890'

Böylece Python'da karakter dizisi biçimlendirmenin hem eski hem de yeni
yöntemini, şu ana kadarki Python bilgimiz elverdiği ölçüde ayrıntılı bir şekilde
incelemiş olduk. Buradaki bilgileri kullanarak bol bol örnek yapmak bu konuyu
daha iyi anlamanıza yardımcı olacaktır.
