.. meta::
   :description: Bu bölümde Python'daki koşul deyimlerinden söz edeceğiz.
   :keywords: python, if, elif, else
   
.. highlight:: python3

*****************
Koşullu Durumlar
*****************

Artık Python programlama dilinde belli bir noktaya geldik sayılır. Ama eğer
farkettiyseniz, yine de elimizi kolumuzu bağlayan, istediğimiz şeyleri yapmamıza
engel olan bir şeyler var. İşte bu bölümde, Python programlama dilinde hareket
alanımızı bir hayli genişletecek araçları tanıyacağız.

Aslında sadece bu bölümde değil, bu bölümü takip eden her bölümde, hareket
alanımızı kısıtlayan duvarları tek tek yıktığımıza şahit olacaksınız. Özellikle
bu bölümde inceleyeceğimiz 'koşullu durumlar' konusu, tabir yerindeyse,
Python'da boyut atlamamızı sağlayacak.

O halde hiç vakit kaybetmeden yola koyulalım...

Şimdiye kadar öğrendiğimiz Python bilgilerini kullanarak şöyle bir program
yazabileceğimizi biliyorsunuz::

    yaş = 15

    print("""Programa hoşgeldiniz!

    Programımızı kullanabilmek için en az
    13 yaşında olmalısınız.""")

    print("Yaşınız: ", yaş)

Burada yaptığımız şey çok basit. Öncelikle, değeri `15` olan, `yaş` adlı bir
değişken tanımladık. Daha sonra, programımızı çalıştıran kullanıcılar için bir
hoşgeldin mesajı hazırladık. Son olarak da `yaş` değişkeninin değerini ekrana
yazdırdık.

Bu programın özelliği tek sesli bir uygulama olmasıdır. Yani bu programda
kullanıcıyla herhangi bir etkileşim yok. Burada bütün değerleri/değişkenleri
programcı olarak kendimiz belirliyoruz. Bu programın ne kadar yavan olduğunu
herhalde söylemeye gerek yok.

Ancak yine önceki derslerde öğrendiğimiz ``input()`` fonksiyonu yardımıyla
yukarıdaki programın üzerindeki yavanlığı bir nebze de olsa atabilir, bu
programı rahatlıkla çok sesli bir hale getirebilir, yani kullanıcıyla etkileşim
içine girebiliriz.

Yukarıdaki tek sesli uygulamayı, ``input()`` fonksiyonunu kullanarak çok sesli
bir hale nasıl getireceğimizi gayet iyi bildiğinize eminim::

    print("""Programa hoşgeldiniz!
    
    Programımızı kullanabilmek için en az
    13 yaşında olmalısınız.""")
    
    print("Lütfen yaşınızı girin.\n")
    
    yaş = input("Yaşınız: \t")
    
    print("Yaşınız: ", yaş)

Tıpkı bir önceki uygulamada olduğu gibi, burada da yaptığımız şey çok basit. İlk
örnekte `yaş` değişkeninin değerini kendimiz elle yazmıştık. İkinci örnekte ise
bu `yaş` değişkenini kullanıcıdan alıyoruz ve tıpkı ilk örnekte olduğu gibi, bu
değişkenin değerini ekrana yazdırıyoruz.

Bu arada, yukarıdaki uygulamada yer verdiğimiz `\\n` ve `\\t` adlı kaçış
dizileri de artık sizin için oldukça tanıdık. `\\n` kaçış dizisi yardımıyla bir
alt satıra geçtiğimizi, `\\t` adlı kaçış dizisi yardımıyla da bir sekmelik
boşluk bıraktığımızı biliyorsunuz.

Gördüğünüz gibi, şu ana kadar öğrendiklerimizle ancak kullanıcıdan gelen yaş
bilgisini ekrana yazdırabiliyoruz. Öğrendiğimiz ``input()`` fonksiyonu bize
kullanıcıdan bilgi alma imkanı sağlıyor. Ama kullanıcıdan gelen bu bilgiyi
şimdilik ancak olduğu gibi kullanabiliyoruz. Yani mesela yukarıdaki örneği
dikkate alarak konuşacak olursak, kullanıcının yaşı eğer 13'ün üzerindeyse onu
programa kabul edecek, yok eğer 13 yaşın altındaysa da programdan atacak bir
mekanizma üretemiyoruz. Yapabildiğimiz tek şey, kullanıcının girdiği veriyi
ekrana yazdırmak.

Yukarıda verdiğimiz örneklerle nereye varmaya çalıştığımızı az çok tahmin
etmişsinizdir. Dikkat ederseniz yukarıda sözünü ettiğimiz şey koşullu bir durum.
Yani aslında yapmak istediğimiz şey, kullanıcının yaşını denetleyip, onun
programa kabul edilmesini 13 yaşından büyük olma koşuluna bağlamak.

İsterseniz tam olarak neden bahsettiğimizi anlayabilmek için, birkaç vaka örneği
verelim.

Diyelim ki Google'ın Gmail hizmeti aracılığıyla bir e.posta hesabı aldınız. Bu
hesaba gireceğiniz zaman Gmail size bir kullanıcı adı ve parola sorar. Siz de
kendinize ait kullanıcı adını ve parolayı sayfadaki kutucuklara yazarsınız. Eğer
yazdığınız kullanıcı adı ve parola doğruysa hesabınıza erişebilirsiniz. Ama eğer
kullanıcı adınız ve parolanız doğru değilse hesabınıza erişemezsiniz. Yani
e.posta hesabınıza erişmeniz, kullanıcı adı ve parolayı doğru girme koşuluna
bağlıdır.

Ya da şu vaka örneğini düşünelim: Diyelim ki Pardus'ta komut satırı aracılığıyla
güncelleme işlemi yapacaksınız. ``sudo pisi up`` komutunu verdiğiniz zaman
güncellemelerin listesi size bildirilecek, bu güncellemeleri yapmak isteyip
istemediğiniz sorulacaktır. Eğer evet cevabı verirseniz güncelleme işlemi
başlar. Ama eğer hayır cevabı verirseniz güncelleme işlemi başlamaz. Yani
güncelleme işleminin başlaması kullanıcının evet cevabı vermesi koşuluna
bağlıdır.

İşte bu bölümde biz bu tür koşullu durumlardan söz edeceğiz.

Koşul Deyimleri
****************

Hiç kuşkusuz, koşula bağlı durumlar Python'daki en önemli konulardan biridir.
Giriş bölümünde bahsettiğimiz koşullu işlemleri yapabilmek için 'koşul
deyimleri' adı verilen birtakım araçlardan yararlanacağız. Gelin şimdi bu
araçların neler olduğunu görelim.

.. highlight:: py3

if
=====

Python programlama dilinde koşullu durumları belirtmek için üç adet deyimden
yararlanıyoruz:

* ``if`` 
* ``elif`` 
* ``else`` 

İsterseniz önce ``if`` deyimi ile başlayalım...

Eğer daha önceden herhangi bir programlama dilini az da olsa kurcalama
fırsatınız olduysa, bir programlama dilinde ``if`` deyimlerinin ne işe
yaradığını az çok biliyorsunuzdur. Daha önceden hiç programcılık deneyiminiz
olmamışsa da ziyanı yok. Zira bu bölümde ``if`` deyimlerinin ne işe yaradığını
ve nerelerde kullanıldığını enine boyuna tartışacağız.

İngilizce bir kelime olan '*if*', Türkçede 'eğer' anlamına gelir. Anlamından da
çıkarabileceğimiz gibi, bu kelime bir koşul bildiriyor. Yani '*eğer bir şey
falanca ise...*' ya da '*eğer bir şey filanca ise...*' gibi... İşte biz
Python'da bir koşula bağlamak istediğimiz durumları ``if`` deyimi aracılığıyla
göstereceğiz.

Gelin isterseniz bu deyimi nasıl kullanacağımıza dair ufacık bir örnek vererek
işe başlayalım:

Öncelikle elimizde şöyle bir değişken olsun::
    
	n = 255

Yukarıda verdiğimiz değişkenin değerinin bir karakter dizisi değil, aksine bir
sayı olduğunu görüyoruz. Şimdi bu değişkenin değerini sorgulayalım::
    
	if n > 10:

Burada sayının 10'dan büyük olup olmadığına bakıyoruz.

Burada gördüğümüz `>` işaretinin ne demek olduğunu açıklamaya gerek yok sanırım.
Hepimizin bildiği 'büyüktür' işareti Python'da da aynen bildiğimiz şekilde
kullanılıyor. Mesela 'küçüktür' demek isteseydik, `<` işaretini kullanacaktık.
İsterseniz hemen şurada araya girip bu işaretleri yeniden hatırlayalım:

    +--------+-------------------+
    | İşleç  | Anlamı            |
    +========+===================+
    | >      | büyüktür          |
    +--------+-------------------+  
    | <      | küçüktür          |
    +--------+-------------------+
    | >=     | büyük eşittir     |
    +--------+-------------------+
    | <=     | küçük eşittir     |
    +--------+-------------------+
    | ==     | eşittir           |
    +--------+-------------------+
    | !=     | eşit değildir     |
    +--------+-------------------+

Gördüğünüz gibi hiçbiri bize yabancı gelecek gibi değil. Yalnızca en sondaki
'eşittir' (`==`) ve 'eşit değildir' (`!=`) işaretleri biraz değişik gelmiş
olabilir. Burada 'eşittir' işaretinin `=` olmadığına dikkat edin. Python'da `=`
işaretini değer atama işlemleri için kullanıyoruz. `==` işaretini ise iki adet
değerin birbirine eşit olup olmadığını denetlemek için... Mesela::

    >>> a = 26

Burada değeri `26` olan `a` adlı bir değişken belirledik. Yani `a` değişkenine
değer olarak `26` sayısını atadık. Ayrıca burada, değer atama işleminin ardından
`Enter` tuşuna bastıktan sonra Python hiçbir şey yapmadan bir alt satıra geçti.
Bir de şuna bakalım::

    >>> a == 26 
    
    True

Burada ise yaptığımız şey `a` değişkeninin değerinin `26` olup olmadığını
sorgulamak ``a == 26`` komutunu verdikten sonra Python bize `True` diye bir
çıktı verdi. Bu çıktının anlamını biraz sonra öğreneceğiz. Ama şimdi isterseniz
konuyu daha fazla dağıtmayalım. Biz şimdilik sadece `=` ve `==` işaretlerinin
birbirinden tamamen farklı anlamlara geldiğini bilelim yeter.

Ne diyorduk?

::

	if n > 10:

Bu ifadeyle Python'a şöyle bir şey demiş oluyoruz:

	Eğer `n` sayısının değeri 10'dan büyükse...

Burada kullandığımız işaretlere dikkat edin. En sonda bir adet `:` işaretinin
olduğunu gözden kaçırmıyoruz. Bu tür işaretler Python için çok önemlidir.
Bunları yazmayı unutursak Python gözümüzün yaşına bakmayacaktır.

Dedik ki, ``if n > 10:`` ifadesi, 'eğer n değişkeninin değeri 10'dan büyükse...'
anlamına gelir. Bu ifadenin eksik olduğu apaçık ortada. Yani belli ki bu
cümlenin bir de devamı olması gerekiyor. O halde biz de devamını getirelim::
    
	if n > 10:
	    print("sayı 10'dan büyüktür!")

Burada çok önemli bir durumla karşı karşıyayız. Dikkat ederseniz, ikinci satırı
ilk satıra göre girintili yazdık. Elbette bunu şirinlik olsun diye yapmadık.
Python programlama dilinde girintiler çok büyük önem taşır. Hatta ne kadarlık
bir girinti verdiğiniz bile önemlidir. Eğer Python kodlarına duyarlı bir metin
düzenleyici kullanıyorsanız, kullandığınız metin düzenleyici çoğu durumda sizin
yerinize uygun bir şekilde girintilemeyi yapacaktır. Mesela IDLE adlı geliştirme
ortamını kullananlar, ilk satırdaki `:` işaretini koyup `Enter` tuşuna
bastıklarında otomatik olarak girinti verildiğini farkedeceklerdir. Eğer
kullandığınız metin düzenleyici, satırları otomatik olarak girintilemiyorsa
sizin bu girintileme işlemini elle yapmanız gerekecektir. Yalnız elle
girintilerken, ne kadar girinti vereceğimize dikkat etmeliyiz. Genel kural
olarak `4` boşlukluk bir girintileme uygun olacaktır. Girintileme işlemini
klavyedeki sekme (`Tab`) tuşuna basarak da yapabilirsiniz. Ama aynı program
içinde sekmelerle boşlukları karıştırmayın. Yani eğer girintileme işlemini
klavyedeki boşluk (`Space`) tuşuna basarak yapıyorsanız, program boyunca aynı
şekilde yapın. (Ben size girinti verirken `Tab` tuşu yerine `Space` tuşunu
kullanmanızı tavsiye ederim). Kısaca söylemek gerekirse; Python'da girintileme
ve girintilemede tutarlılık çok önemlidir. Özellikle büyük programlarda,
girintilemeler açısından tutarsızlık gösterilmesi programın çalışmamasına sebep
olabilir.

.. note:: Python'da girintileme konusuyla ilgili daha ayrıntılı bilgi için:
          http://www.istihza.com/blog/python-ve-metin-duzenleyiciler.html/

Eğer yukarıdaki ``if`` bloğunu bir metin düzenleyici içine değil de doğrudan
etkileşimli kabuğa yazmışsanız bazı şeyler dikkatinizi çekmiş olmalı.
Etkileşimli kabukta ``if sayı > 10:`` satırını yazıp `Enter` tuşuna bastığınızda
şöyle bir görüntüyle karşılaşmış olmalısınız::
    
	>>> if n > 10:
	...

Dikkat ederseniz, `>>>` işareti, `...` işaretine dönüştü. Eğer bu noktada
herhangi bir şey yazmadan `Enter` tuşuna basacak olursanız Python size şöyle bir
hata mesajı verecektir::
    
	File "<stdin>", line 2
	    ^
	IndentationError: expected an indented block

Hata mesajında da söylendiği gibi, Python bizden girintilenmiş bir blok
beklerken, biz onun bu beklentisini karşılamamışız. Dolayısıyla bize yukarıdaki
hata mesajını göstermiş. `...` işaretini gördükten sonra yapmamız gereken şey,
dört kez boşluk (`Space`) tuşuna basarak girinti oluşturmak ve ``if`` bloğunun
devamını yazmak olmalıydı. Yani şöyle::
    
	>>> if n > 10:
	...      print("sayı 10'dan büyüktür!")
	...

Gördüğünüz gibi, ``print()`` fonksiyonunu yazıp `Enter` tuşuna bastıktan sonra
yine `...` işaretini gördük. Python burada bizden yeni bir satır daha bekliyor.
Ama bizim yazacak başka bir kodumuz olmadığı için tekrar `Enter` tuşuna
basıyoruz ve nihai olarak şöyle bir görüntü elde ediyoruz::
    
	>>> if n > 10:
	...      print("sayı 10'dan büyüktür!")
	...
	sayı 10'dan büyüktür!
	>>>

Demek ki `250` sayısı `10`'dan büyükmüş! Ne büyük bir buluş! Merak etmeyin, daha
çok şey öğrendikçe daha mantıklı programlar yazacağız. Burada amacımız işin
temelini kavramak. Bunu da en iyi, (çok mantıklı olmasa bile) basit programlar
yazarak yapabiliriz.

Şimdi metin düzenleyicimizi açarak daha mantıklı şeyler yazmaya çalışalım. Zira
yukarıdaki örnekte değişkeni kendimiz belirlediğimiz için, bu değişkenin
değerini ``if`` deyimleri yardımıyla denetlemek pek akla yatkın görünmüyor. Ne
de olsa değişkenin değerinin ne olduğunu biliyoruz. Dolayısıyla bu değişkenin
`10` sayısından büyük olduğunu da biliyoruz! Bunu ``if`` deyimiyle kontrol etmek
çok gerekli değil. Ama şimdi daha makul bir iş yapacağız. Değişkeni biz
belirlemek yerine kullanıcıya belirleteceğiz::

	sayı = int(input("Bir sayı giriniz: "))

	if sayı > 10:
	    print("Girdiğiniz sayı 10'dan büyüktür!")

	if sayı < 10:
	    print("Girdiğiniz sayı 10'dan küçüktür!")

	if sayı == 10:
	    print("Girdiğiniz sayı 10'dur!")

Gördüğünüz gibi, art arda üç adet ``if`` bloğu kullandık. Bu kodlara göre, eğer
kullanıcının girdiği sayı `10`'dan büyükse, ilk ``if`` bloğu işletilecek; eğer
sayı `10`'dan küçükse ikinci ``if`` bloğu işletilecek; eğer sayı 10'a eşit ise
üçüncü ``if`` bloğu işletilecektir. Peki ya kullanıcı muziplik yapıp sayı yerine
harf yazarsa ne olacak? Böyle bir ihtimal için programımıza herhangi bir
denetleyici yerleştirmedik. Dolayısıyla eğer kullanıcı sayı yerine harf girerse
programımız hata verecek, yani çökecektir. Bu tür durumlara karşı nasıl önlem
alacağımızı ilerleyen derslerimizde göreceğiz. Biz şimdilik bildiğimiz yolda
yürüyelim.

Yukarıdaki örnekte ``input()`` ile gelen karakter dizisini, ``int()`` fonksiyonu
yardımıyla bir sayıya dönüştürdüğümüze dikkat edin. Kullanıcıdan gelen veriyi
büyüklük-küçüklük ölçütüne göre inceleyeceğimiz için, gelen veriyi bir sayıya
dönüştürmemiz gerekiyor. Bunu da ``int()`` fonksiyonu ile yapabileceğimizi
biliyorsunuz.

Elbette yukarıdaki dönüştürme işlemini şöyle de yapabilirdik::

    sayı = input("Bir sayı giriniz: ")    
    sayı = int(sayı)

Burada önce ``input()`` fonksiyonuyla veriyi aldık, daha sonra bu veriyi ayrı
bir yerde sayıya dönüştürüp tekrar `sayı` adlı değişkene atadık.

``if`` deyimlerini kullanıcı adı veya parola denetlerken de kullanabiliriz.
Mesela şöyle bir program taslağı yazabiliriz::

	print("""
	Dünyanın en gelişmiş e.posta hizmetine 
	hoşgeldiniz. Yalnız hizmetimizden   
	yararlanmak için önce sisteme giriş    
	yapmalısınız.                        
	""")

	parola = input("Parola: ")

	if parola == "12345678":
	    print("Sisteme Hoşgeldiniz!") 

Gördüğünüz gibi, programın başında üç tırnak işaretlerinden yararlanarak uzun
bir metni kullanıcıya gösterdik. Bu bölümü, kendiniz göze hoş gelecek bir
şekilde süsleyebilirsiniz de. Eğer kullanıcı, kendisine parola sorulduğunda
cevap olarak `"12345678"` yazarsa kullanıcıyı sisteme alıyoruz.

Yukarıdaki örnekte, kullanıcının girdiği parola `"12345678"` ise kendisine
`"Sisteme Hoşgeldiniz!"` mesajını gösteriyoruz. Mantık olarak bunun tersini
yapmak da mümkündür. Yani::
    
    if parola != "12345678":
        print("Ne yazık ki yanlış parola girdiniz!")

Burada ise bir önceki örneğin mantığını ters çevirdik. Önceki örnekte `parola`
değişkeni `"12345678"` adlı karakter dizisine eşitse (``if parola ==
"12345678"``) bir işlem yapıyorduk. Yukarıdaki örnekte ise `parola` değişkeni
`"12345678"` adlı karakter dizisine eşit değilse (``if parola != "12345678"``)
bir işlem yapıyoruz.

Bu iki örneğin de aslında aynı kapıya çıktığını görüyorsunuz. Tek değişiklik,
kullanıcıya gösterilen mesajlardadır.

Böylece Python'daki koşullu durumlar üzerindeki incelememizin ilk ve en önemli
aşamasını geride bırakmış olduk. Dikkat ettiyseniz ``if`` deyimi sayesinde
programlarımıza karar vermeyi öğrettik. Bu deyim yardımıyla, kullanıcıdan
aldığımız herhangi bir verinin niteliği üzerinde kapsamlı bir karar verme işlemi
yürütebiliyoruz. Yani artık programlarımız kullanıcıdan alınan veriyi olduğu
gibi kabul etmekle yetinmiyor. Kullanıcının girdiği verinin ne olduğuna bağlı
olarak programlarımızın farklı işlemler yapmasını da sağlayabiliyoruz.

Daha önce de söylediğimiz gibi, ``if`` deyimi dışında Python'da koşullu
durumları ifade etmek için kullandığımız, ``elif`` ve ``else`` adlı iki deyim
daha vardır. Bunlar ``if`` ile birlikte kullanılırlar. Gelin isterseniz bu iki
deyimden, adı ``elif`` olana bakalım.

.. highlight:: py3

elif
=======

Python'da, ``if`` deyimleriyle birlikte kullanılan ve yine koşul belirten bir
başka deyim de ``elif`` deyimidir. Buna şöyle bir örnek verebiliriz::
    
	yaş = int(input("Yaşınız: "))

	if yaş == 18:
	    print("18 iyidir!")

	elif yaş < 0:
	    print("Yok canım, daha neler!...")

	elif yaş < 18:
	    print("Genç bir kardeşimizsin!")

	elif yaş > 18:
	    print("Eh, artık yaş yavaş yavaş kemale eriyor!")

Yukarıdaki örneği şöyle yazmayı da deneyebilirsiniz::

	yaş = int(input("Yaşınız: "))

	if yaş == 18:
	    print("18 iyidir!")

	if yaş < 0:
	    print("Yok canım, daha neler!...")

	if yaş < 18:
	    print("Genç bir kardeşimizsin!")

	if yaş > 18:
	    print("Eh, artık yaş yavaş yavaş kemale eriyor!")

Bu iki programın da aynı işlevi gördüğünü düşünebilirsiniz. Ancak ilk bakışta
pek belli olmasa da, aslında yukarıdaki iki program birbirinden farklı
davranacaktır. Örneğin ikinci programda eğer kullanıcı eksi değerli bir sayı
girerse hem ``if yaş < 0`` bloğu, hem de ``if yaş < 18`` bloğu çalışacaktır.
İsterseniz yukarıdaki programı çalıştırıp, cevap olarak eksi değerli bir sayı
verin. Ne demek istediğimiz gayet net anlaşılacaktır.

Bu durum ``if`` ile ``elif`` arasındaki çok önemli bir farktan kaynaklanır. Buna
göre ``if`` bize olası bütün sonuçları listeler, ``elif`` ise sadece doğru olan
ilk sonucu verir. Bu soyut tanımlamayı biraz daha somutlaştıralım::
    
	a = int(input("Bir sayı giriniz: "))

	if a < 100:
	    print("verdiğiniz sayı 100'den küçüktür.")

	if a < 50:
	    print("verdiğiniz sayı 50'den küçüktür.")

	if a == 100:
	    print("verdiğiniz sayı 100'dür.")

	if a > 100:
	    print("verdiğiniz sayı 100'den büyüktür.")

	if a > 150:
	    print("verdiğiniz sayı 150'den büyüktür.")

.. highlight:: none

Yukarıdaki kodları çalıştırdığımızda, doğru olan bütün sonuçlar listelenecektir.
Yani mesela kullanıcı `40` sayısını girmişse, ekrana verilecek çıktı şöyle
olacaktır::
    
	verdiğiniz sayı 100'den küçüktür.
	verdiğiniz sayı 50'den küçüktür.

.. highlight:: py3

Burada `40` sayısı hem `100`'den, hem de `50`'den küçük olduğu için iki sonuç da
çıktı olarak verilecektir. Ama eğer yukarıdaki kodları şöyle yazarsak::
    
	a = int(input("Bir sayı giriniz: "))

	if a < 100:
	    print("verdiğiniz sayı 100'den küçüktür.")

	elif a < 50:
	    print("verdiğiniz sayı 50'den küçüktür.")

	elif a == 100:
	    print("verdiğiniz sayı 100'dür.")

	elif a > 150:
	    print("verdiğiniz sayı 150'den büyüktür.")

	elif a > 100:
	    print("verdiğiniz sayı 100'den büyüktür.")

.. highlight:: none

Kullanıcının `40` sayısını girdiğini varsaydığımızda, bu defa programımımız
yalnızca şu çıktıyı verecektir::
    
	verdiğiniz sayı 100'den küçüktür.

Gördüğünüz gibi, ``elif`` deyimlerini kullandığımız zaman, ekrana yalnızca doğru
olan ilk sonuç veriliyor. Yukarıda `40` sayısı hem `100`'den hem de `50`'den
küçük olduğu halde, Python bu sayının `100`'den küçük olduğunu görür görmez
sonucu ekrana basıp, öteki koşul bloklarını incelemeyi bırakıyor. ``if``
deyimlerini arka arkaya sıraladığımızda ise, Python bütün olasılıkları tek tek
değerlendirip, geçerli olan bütün sonuçları ekrana döküyor.

Bir sonraki bölümde ``else`` deyimini öğrendiğimiz zaman, ``elif``'in tam olarak
ne işe yaradığını çok daha iyi anlamanızı sağlayacak bir örnek vereceğiz.

.. note:: Şimdiye kadar verdiğimiz örneklerden de rahatlıkla anlayabileceğiniz
          gibi, ilk koşul bloğunda asla ``elif`` deyimi kullanılamaz. Bu deyimin
          kullanılabilmesi için kendisinden önce en az bir adet ``if`` bloğu olmalıdır.
          Yani Python'da koşullu durumları ifade ederken ilk koşul bloğumuz her zaman
          ``if`` deyimi ile başlamalıdır.

``elif``'i de incelediğimize göre, koşul bildiren deyimlerin sonuncusuna göz
atabiliriz: ``else``

.. highlight:: py3

else
======

Şimdiye kadar Python'da koşul bildiren iki deyimi öğrendik. Bunlar ``if`` ve
``elif`` idi. Bu bölümde ise koşul deyimlerinin sonuncusu olan ``else`` deyimini
göreceğiz. Öğrendiğimiz şeyleri şöyle bir gözden geçirecek olursak, temel olarak
şöyle bir durumla karşı karşıya olduğumuzu görürüz::
    
	if falanca:
	    bu işlemi yap

	if filanca:
	    şu işlemi yap

Veya şöyle bir durum::

	if falanca:
	    bu işlemi yap

	elif filanca:
	    şu işlemi yap

``if`` ile ``elif`` arasındaki farkı biliyoruz. Eğer ``if`` deyimlerini art arda
sıralayacak olursak, Python doğru olan bütün sonuçları listeleyecektir. Ama eğer
``if`` deyiminden sonra ``elif`` deyimini kullanırsak, Python doğru olan ilk
sonucu listelemekle yetinecektir.

Bu bölümde göreceğimiz ``else`` deyimi, yukarıdaki tabloya bambaşka bir boyut
kazandırıyor. Dikkat ederseniz şimdiye kadar öğrendiğimiz deyimleri
kullanabilmek için ilgili bütün durumları tanımlamamız gerekiyordu. Yani::
    
	eğer böyle bir durum varsa:
	    bunu yap

	eğer şöyle bir durum varsa:
	    şunu yap

	eğer filancaysa:
	    şöyle git

	eğer falancaysa:
	    böyle gel

gibi...

Ancak her durum için bir ``if`` bloğu yazmak bir süre sonra yorucu ve sıkıcı
olacaktır. İşte bu noktada devreye ``else`` deyimi girecek. ``else``'in anlamı
kabaca şudur:

	Eğer yukarıdaki koşulların hiçbiri gerçekleşmezse...

Gelin isterseniz bununla ilgili şöyle bir örnek verelim::

	soru = input("Bir meyve adı söyleyin bana:")

	if soru == "elma":
	    print("evet, elma bir meyvedir...")

	elif soru == "karpuz":
	    print("evet, karpuz bir meyvedir...")

	elif soru == "armut":
	    print("evet, armut bir meyvedir...")

	else:
	    print(soru, "gerçekten bir meyve midir?")

Eğer kullanıcı soruya 'elma', 'karpuz' veya 'armut' cevabı verirse, `evet, ...
bir meyvedir` çıktısı verilecektir. Ama eğer kullanıcı bu üçü dışında bir cevap
verirse, `... gerçekten bir meyve midir?` çıktısını görürüz. Burada ``else``
deyimi, programımıza şu anlamı katıyor:

	Eğer kullanıcı yukarıda belirlenen meyve adlarından hiç birini girmez, bunların yerine bambaşka bir şey yazarsa, o zaman ``else`` bloğu içinde belirtilen işlemi gerçekleştir.

Dikkat ederseniz yukarıdaki kodlarda ``if`` deyimlerini art arda sıralamak
yerine ilk ``if``'ten sonra ``elif`` ile devam ettik. Peki şöyle bir şey
yazarsak ne olur? ::
    
	soru = input("Bir meyve adı söyleyin bana:")

	if soru == "elma":
	    print("evet, elma bir meyvedir...")

	if soru == "karpuz":
	    print("evet, karpuz bir meyvedir...")

	if soru == "armut":
	    print("evet, armut bir meyvedir...")

	else:
	    print(soru, "gerçekten bir meyve midir?")

Bu kodlar beklediğiniz sonucu vermeyecektir. İsterseniz yukarıdaki kodları
çalıştırıp ne demek istediğimizi daha iyi anlayabilirsiniz. Eğer yukarıda olduğu
gibi ``if`` deyimlerini art arda sıralar ve son olarak da bir ``else`` bloğu
tanımlarsak, ekrana ilk bakışta anlamsız gibi görünen bir çıktı verilecektir::
    
    evet, elma bir meyvedir...
    elma gerçekten bir meyve midir?

Burada olan şey şu: 

Soruya 'elma' cevabını verdiğimizi düşünelim. Bu durumda, Python ilk olarak ilk
``if`` bloğunu değerlendirecek ve soruya verdiğimiz cevap 'elma' olduğu için
`evet, elma bir meyvedir...` çıktısını verecektir.

``if`` ile ``elif`` arasındaki farkı anlatırken, hatırlarsanız art arda gelen ``if`` bloklarında Python'ın olası bütün sonuçları değerlendireceğini söylemiştik. İşte burada da böyle bir durum söz konusu. Gördüğünüz gibi, ilk ``if`` bloğundan sonra yine bir ``if`` bloğu geliyor. Bu nedenle Python olası bütün sonuçları değerlendirebilmek için blokları okumaya devam edecek ve sorunun cevabı 'karpuz' olmadığı için ikinci ``if`` bloğunu atlayacaktır. 

Sonraki blok yine bir ``if`` bloğu olduğu için Python kodları okumaya devam
ediyor. Ancak sorunun cevabı 'armut' da olmadığı için, Python sonraki ``if``
bloğunu da geçiyor ve böylece ``else`` bloğuna ulaşıyor.

Yukarıda verdiğimiz örnekteki gibi art arda ``if`` deyimlerinin sıralanıp en
sona ``else`` deyiminin yerleştirildiği durumlarda ``else`` deyimi sadece bir
önceki ``if`` deyimini dikkate alarak işlem yapar. Yani yukarıdaki örnekte
kullanıcının verdiği cevap 'armut' olmadığı için ``else`` deyiminin olduğu blok
çalışmaya başlar. Yukarıdaki örneğe 'armut' cevabını verirseniz ne demek
istediğimi biraz daha iyi anlayabilirsiniz. 'armut' cevabı verilmesi durumunda
sadece ``if soru == "armut"`` ifadesinin olduğu blok çalışır, ``else`` bloğu ise
çalışmaz. Çünkü dediğim gibi, eğer ``else`` bloğundan önce art arda gelen ``if``
blokları varsa, ``else`` deyimi yalnızca kendisinden önceki son ``if`` bloğunu
dikkate alır ve sanki yukarıdaki örnek şöyleymiş gibi davranır::
    
	if soru == "armut":
	    print("evet, armut bir meyvedir...")

	else:
	    print(soru, "gerçekten bir meyve midir?")

Bu tür durumlarda ``else`` deyimi bir önceki ``if`` bloğundan önce gelen bütün
``if`` bloklarını görmezden gelir ve böylece şu anlamsız görünen çıktı elde
edilir::
    
    evet, elma bir meyvedir...
    elma gerçekten bir meyve midir?

Sözün özü, kullanıcının cevabı 'elma' olduğu için, yukarıdaki çıktıda yer alan
ilk cümle ilk ``if`` bloğunun çalışması sonucu ekrana basılıyor. İkinci cümle
ise ``else`` bloğundan bir önceki ``if`` bloğu kullanıcının cevabıyla uyuşmadığı
için ekrana basılıyor.

Yalnız bu dediğimizden, ``else`` ifadesi ``if`` ile birlikte kullanılmaz, anlamı
çıkarılmamalı. Mesela şöyle bir örnek yapılabilir::
    
	soru = input("Programdan çıkmak istediğinize emin misiniz? \
	Eminseniz 'e' harfine basın : ")

	if soru == "e":
	    print("Güle güle!")

	else:
	    print("Peki, biraz daha sohbet edelim!")

Burada eğer kullanıcının cevabı 'e' ise ``if`` bloğu işletilecek, eğer cevap 'e'
dışında herhangi bir şey ise ``else`` bloğu çalışacaktır. Gayet mantıklı bir
süreç. Ama eğer yukarıdaki örneğe bir ``if`` bloğu daha eklerseniz işler
beklediğiniz gibi gitmez::
    
    soru = input("Programdan çıkmak istediğinize emin misiniz? \
    Eminseniz 'e' harfine basın : ")

    if soru == "e":
        print("Güle güle!")

    if soru == "b":
        print("Kararsız kaldım şimdi!")

    else:
        print("Peki, biraz daha sohbet edelim!")

Bu soruya 'e' cevabı verdiğimizi düşünelim. Bu cevap ilk ``if`` bloğuyla
uyuşuyor ve böylece ekrana `Güle güle!` çıktısı veriliyor. İlk ``if`` bloğundan
sonra tekrar bir ``if`` bloğu daha geldiği için Python bütün olasılıkları
değerlendirmek amacıyla blokları okumaya devam ediyor ve cevap 'b' olmadığı için
ikinci ``if`` bloğunu atlıyor ve böylece ``else`` bloğuna ulaşıyor. Bir önceki
örnekte de söylediğimiz gibi, ``else`` bloğu art arda gelen ``if`` blokları
gördüğünde sadece bir önceki ``if`` bloğunu dikkate aldığı ve kullanıcının
cevabı da 'b' olmadığı için ekrana `Peki, biraz daha sohbet edelim!` çıktısını
veriyor ve ilk bakışta tuhaf görünen şöyle bir çıktı üretiyor::
    
    Güle güle!
    Peki, biraz daha sohbet edelim!

Dolayısıyla, eğer programınızda bir ``else`` bloğuna yer verecekseniz, ondan
önce gelen koşullu durumların ilkini ``if`` ile sonrakileri ise ``elif`` ile
bağlayın. Yani::
    
    if koşul_1:
        sonuç_1
    
    elif koşul_2:
        sonuç_2
        
    elif koşul_3:
        sonuç_3
    
    else:
        sonuç_4

Ama eğer ``else`` bloğundan önce sadece tek bir koşul bloğu yer alacaksa bunu
``if`` ile bağlayın. Yani::
    
    if koşul_1:
        sonuç_1
    
    else:
        sonuç_2
        
Programlarımızın doğru çalışması ve istediğimiz sonucu verebilmesi için bu tür
ayrıntılara olabildiğince dikkat etmemiz gerekiyor. Neticede koşullu durumlar
mantıkla ilgilidir. Dolayısıyla koşullu durumlarla muhatap olurken mantığınızı
hiçbir zaman devre dışı bırakmamalısınız.

Bir önceki bölümde ``elif`` deyiminin tam olarak ne işe yaradığını anlamamızı
sağlayacak bir örnek vereceğimizi söylemiştik. Şimdi bu örneğe bakalım::
    
	boy = int(input("boyunuz kaç cm?"))

	if boy < 170:
	    print("boyunuz kısa")

	elif boy < 180:
	    print("boyunuz normal")

	else:
	    print("boyunuz uzun")

Yukarıda yedi satırla hallettiğimiz işi sadece ``if`` deyimleriyle yapmaya
çalışırsanız bunun ne kadar zor olduğunu göreceksiniz. Diyelim ki kullanıcı
'165' cevabını verdi. Python bu `165` sayısının `170`'ten küçük olduğunu görünce
`boyunuz kısa` cevabını verecek, öteki satırları değerlendirmeyecektir. `165`
sayısı, ``elif`` ile gösterdiğimiz koşullu duruma da uygun olduğu halde (``165 <
180``), koşul ilk blokta karşılandığı için ikinci blok değerlendirmeye
alınmayacaktır.

Kullanıcının '175' cevabını verdiğini varsayalım: Python `175` sayısını görünce
önce ilk koşula bakacak, verilen `175` sayısının ilk koşulu karşılamadığını
görecektir (``175 > 170``). Bunun üzerine Python kodları incelemeye devam edecek
ve ``elif`` bloğunu değerlendirmeye alacaktır. `175` sayısının `180`'den küçük
olduğunu görünce de çıktı olarak `boyunuz normal` cevabını verecektir.

Peki ya kullanıcı '190' cevabını verirse ne olacak? Python yine önce ilk ``if``
bloğuna bakacak ve `190` cevabının bu bloğa uymadığını görecektir. Dolayısıyla
ilk bloğu bırakıp ikinci bloğa bakacaktır. `190` cevabının bu bloğa da
uymadığını görünce, bir sonraki bloğu değerlendirmeye alacaktır. Bir sonraki
blokta ise ``else`` deyimimiz var. Bu bölümde öğrendiğimiz gibi, ``else``
deyimi, 'eğer kullanıcının cevabı yukarıdaki koşulların hiçbirine uymazsa bu
bloğu çalıştır,' anlamına geliyor. Kullanıcının girdiği `190` cevabı ne birinci
ne de ikinci bloktaki koşula uyduğu için, normal bir şekilde ``else`` bloğu
işletilecek, dolayısıyla da ekrana `boyunuz uzun` çıktısı verilecektir.

Böylece Python'da ``if``, ``elif`` ve ``else`` deyimlerini incelemiş olduk.
Ancak tabii ki bu deyimlerle işimiz henüz bitmedi. Elimizdeki bilgiler şimdilik
bu deyimleri ancak bu kadar incelememize yetiyor, ama ilerleyen sayfalarda bazı
başka araçları da bilgi dağarcığımıza kattıktan sonra bu deyimlerin daha farklı
yönlerini öğrenme imkanına kavuşacağız.

Örnek Uygulama
*****************

Önceki derslerimizde ``len()`` fonksiyonunu anlatırken şöyle bir program
tasarısından bahsetmiştik hatırlarsanız:

    Diyelim ki sisteme kayıt için kullanıcı adı ve parola belirlenmesini isteyen
    bir program yazıyorsunuz. Yazacağınız bu programda, belirlenebilecek
    kullanıcı adı ve parolanın toplam uzunluğu `40` karakteri geçmeyecek.
    
O zaman henüz koşullu durumları öğrenmemiş olduğumuz için, yukarıda
bahsettiğimiz programın ancak şu kadarlık kısmını yazabilmiştik::
    
    kullanıcı_adı = input("Kullanıcı adınız: ")
    parola        = input("Parolanız       : ")
    
    toplam_uzunluk = len(kullanıcı_adı) + len(parola)

Burada yapabildiğimiz tek şey, kullanıcıdan kullanıcı adı ve parola bilgilerini
alıp, bu bilgilerin karakter uzunluğunu ölçebilmekti. Ama artık koşullu
durumları öğrendiğimize göre bu programı eksiksiz olarak yazabiliriz. Şu kodları
dikkatlice inceleyin::
    
    kullanıcı_adı = input("Kullanıcı adınız: ")
    parola        = input("Parolanız       : ")
    
    toplam_uzunluk = len(kullanıcı_adı) + len(parola)
    
    mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"
    
    print(mesaj.format(toplam_uzunluk))
    
    if toplam_uzunluk > 40:
        print("Kullanıcı adınız ile parolanızın ", 
              "toplam uzunluğu 40 karakteri geçmemeli!")
    else:
        print("Sisteme hoşgeldiniz!")

Burada öncelikle kullanıcıdan kullanıcı adı ve parola bilgilerini alıyoruz. Daha
sonra da kullanıcıdan gelen bu bilgilerin toplam karakter uzunluğunu
hesaplıyoruz. Bunun için ``len()`` fonksiyonundan yararlanmamız gerektiğini
hatırlıyor olmalısınız.

Eğer toplam uzunluk 40 karakterden fazla ise, ``if`` bloğunda verilen mesajı
gösteriyoruz. Bunun dışındaki bütün durumlarda ise ``else`` bloğunu devreye
sokuyoruz.

