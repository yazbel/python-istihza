.. meta::
   :description: Bu bölümde döngülerden bahsedeceğiz.
   :keywords: python, döngüler, loops, for, while
   
.. highlight:: python3

*****************
Döngüler (Loops)
*****************

Şimdiye kadar öğrendiklerimiz sayesinde Python'la ufak tefek programlar
yazabilecek düzeye geldik. Mesela öğrendiğimiz bilgiler yardımıyla bir önceki
bölümde çok basit bir hesap makinesi yazabilmiştik. Yalnız o hesap makinesinde
farkettiyseniz çok önemli bir eksiklik vardı. Hesap makinemizle hesap yaptıktan
sonra programımız kapanıyor, yeni hesap yapabilmek için programı yeniden
başlatmamız gerekiyordu.

Hesap makinesi programındaki sorun, örneğin, aşağıdaki program için de
geçerlidir::

    tuttuğum_sayı = 23

    bilbakalım = int(input("Aklımdan bir sayı tuttum. Bil bakalım kaç tuttum? "))

    if bilbakalım == tuttuğum_sayı:
        print("Tebrikler! Bildiniz...")

    else:
        print("Ne yazık ki tuttuğum sayı bu değildi...")
    
Burada `tuttuğum_sayı` adlı bir değişken belirledik. Bu değişkenin değeri `23`.
Kullanıcıdan tuttuğumuz sayıyı tahmin etmesini istiyoruz. Eğer kullanıcının
verdiği cevap `tuttuğum_sayı` değişkeninin değeriyle aynıysa (yani `23` ise),
ekrana 'Tebrikler!...' yazısı dökülecektir. Aksi halde 'Ne yazık ki...' cümlesi
ekrana dökülecektir.

Bu program iyi, hoş, ama çok önemli bir eksiği var. Bu programı yalnızca bir kez
kullanabiliyoruz. Yani kullanıcı yalnızca bir kez tahminde bulunabiliyor. Eğer
kullanıcı bir kez daha tahminde bulunmak isterse programı yeniden çalıştırması
gerekecek. Bunun hiç iyi bir yöntem olmadığı ortada. Halbuki yazdığımız bir
program, ilk çalışmanın ardından kapanmasa, biz bu programı tekrar tekrar
çalıştırabilsek, programımız sürekli olarak başa dönse ve program ancak biz
istediğimizde kapansa ne iyi olurdu değil mi? Yani mesela yukarıdaki örnekte
kullanıcı bir sayı tahmin ettikten sonra, eğer bu sayı bizim tuttuğumuz sayıyla
aynı değilse, kullanıcıya tekrar tahmin etme fırsatı verebilsek çok hoş
olurdu...

Yukarıda açıklamaya çalıştığımız süreç, yani bir sürecin tekrar tekrar devam
etmesi Python'da 'döngü' (*loop*) olarak adlandırılır.

İşte bu bölümde, programlarımızın sürekli olarak çalışmasını nasıl
sağlayabileceğimizi, yani programlarımızı bir döngü içine nasıl sokabileceğimizi
öğreneceğiz.

Python'da programlarımızı tekrar tekrar çalıştırabilmek için döngü adı verilen
bazı ifadelerden yararlanacağız. 

Python'da iki tane döngü bulunur: ``while`` ve ``for``

Dilerseniz işe ``while`` döngüsü ile başlayalım.

while Döngüsü
******************

İngilizce bir kelime olan *while*, Türkçede '... iken, ... olduğu sürece' gibi
anlamlara gelir. Python'da ``while`` bir döngüdür. Bir önceki bölümde
söylediğimiz gibi, döngüler sayesinde programlarımızın sürekli olarak
çalışmasını sağlayabiliriz.

Bu bölümde Python'da ``while`` döngüsünün ne olduğunu ve ne işe yaradığını
anlamaya çalışacağız. Öncelikle ``while`` döngüsünün temellerini kavrayarak işe
başlayalım.

Basit bir ``while`` döngüsü kabaca şuna benzer::

	a = 1

	while a == 1:

Burada `a` adlı bir değişken oluşturduk. Bu değişkenin değeri `1`. Bir sonraki
satırda ise ``while a == 1:`` gibi bir ifade yazdık. En başta da söylediğimiz
gibi *while* kelimesi, '... iken, olduğu sürece' gibi anlamlar taşıyor. Python
programlama dilindeki anlamı da buna oldukça yakındır. Burada ``while a == 1``
ifadesi programımıza şöyle bir anlam katıyor:

    `a` değişkeninin değeri `1` olduğu sürece...

Gördüğünüz gibi cümlemiz henüz eksik. Yani belli ki bunun bir de devamı olacak.
Ayrıca ``while`` ifadesinin sonundaki `:` işaretinden anladığımız gibi, bundan
sonra gelecek satır girintili yazılacak. Devam edelim::
    
	a = 1

	while a == 1:
	    print("bilgisayar çıldırdı!")

Burada Python'a şu emri vermiş olduk:

	`a` değişkeninin değeri `1` olduğu sürece, ekrana 'bilgisayar çıldırdı!'
	yazısını dök!
	
Bu programı çalıştırdığımızda Python verdiğimiz emre sadakatle uyacak ve `a`
değişkeninin değeri `1` olduğu müddetçe de bilgisayarımızın ekranına 'bilgisayar
çıldırdı!' yazısını dökecektir. Programımızın içinde `a` değişkeninin değeri `1`
olduğu ve bu değişkenin değerini değiştirecek herhangi bir şey bulunmadığı için
Python hiç sıkılmadan ekrana 'bilgisayar çıldırdı!' yazısını basmaya devam
edecektir. Eğer siz durdurmazsanız bu durum sonsuza kadar devam edebilir. Bu
çılgınlığa bir son vermek için klavyenizde `Ctrl+C` veya `Ctrl+Z` tuşlarına
basarak programı durmaya zorlayabilirsiniz.

Burada programımızı sonsuz bir döngüye sokmuş olduk (*infinite loop*). Esasında
sonsuz döngüler genellikle bir program hatasına işaret eder. Yani çoğu durumda
programcının arzu ettiği şey bu değildir. O yüzden doğru yaklaşım, döngüye
soktuğumuz programlarımızı durduracak bir ölçüt belirlemektir. Yani öyle bir kod
yazmalıyız ki, `a` değişkeninin `1` olan değeri bir noktadan sonra artık `1`
olmasın ve böylece o noktaya ulaşıldığında programımız dursun. Kullanıcının
`Ctrl+C` tuşlarına basarak programı durdurmak zorunda kalması pek hoş olmuyor.
Gelin isterseniz bu soyut ifadeleri biraz somutlaştıralım.

Öncelikle şu satırı yazarak işe başlıyoruz::

	a = 1

Burada normal bir şekilde `a` değişkenine `1` değerini atadık. Şimdi devam
ediyoruz::
    
	a = 1

	while a < 10:

``while`` ile verdiğimiz ilk örnekte ``while a == 1`` gibi bir ifade
kullanmıştık. Bu ifade;

    `a`'nın değeri `1` olduğu müddetçe... 
    
gibi bir anlama geliyordu. 
    
``while a < 10`` ifadesi ise;

    `a`'nın değeri `10`'dan küçük olduğu müddetçe...

anlamına gelir. İşte burada programımızın sonsuz döngüye girmesini engelleyecek
bir ölçüt koymuş olduk. Buna göre, `a` değişkeninin şimdiki değeri `1`'dir. Biz,
`a`'nın değeri `10`'dan küçük olduğu müddetçe bir işlem yapacağız. Devam
edelim::
    
	a = 1

	while a < 10:
	    print("bilgisayar yine çıldırdı!")

Ne oldu? İstediğimizi elde edemedik, değil mi? Programımız yine sonsuz döngüye
girdi. Bu sonsuz döngüyü kırmak için `Ctrl+C` (veya `Ctrl+Z`)'ye basmamız
gerekecek yine...

Sizce buradaki hata nereden kaynaklandı? Yani neyi eksik yaptık da programımız
sonsuz döngüye girmekten kurtulamadı? Aslında bunun cevabı çok basit. Biz
yukarıdaki kodları yazarak Python'a şu emri vermiş olduk:

	`a`'nın değeri `10`'dan küçük olduğu müddetçe ekrana 'bilgisayar yine
	çıldırdı!' yazısını bas!

`a` değişkeninin değeri `1`. Yani `10`'dan küçük. Dolayısıyla Python'ın ekrana o
çıktıyı basmasını engelleyecek herhangi bir şey yok... 

Şimdi bu problemi nasıl aşacağımızı görelim::

	a = 1

	while a < 10: 
	    a += 1 
	    print("bilgisayar yine çıldırdı!")

Burada ``a += 1`` satırını ekledik kodlarımızın arasına. `+=` işlecini
anlatırken söylediğimiz gibi, bu satır, `a` değişkeninin değerine her defasında
`1` ekliyor ve elde edilen sonucu tekrar `a` değişkenine atıyor. En sonunda
`a`'nın değeri `10`'a ulaşınca da, Python ekrana 'bilgisayar yine çıldırdı!'
cümlesini yazmayı bırakıyor. Çünkü ``while`` döngüsü içinde belirttiğimiz ölçüte
göre, programımızın devam edebilmesi için `a` değişkeninin değerinin `10`'dan
küçük olması gerekiyor. `a`'nın değeri `10`'a ulaştığı anda bu ölçüt
bozulacaktır. Gelin isterseniz bu kodları Python'ın nasıl algıladığına bir
bakalım:

#. Python öncelikle ``a = 1`` satırını görüyor ve `a`'nın değerini `1`
   yapıyor. 

#. Daha sonra `a`'nın değeri `10`'dan küçük olduğu müddetçe...
   (``while a < 10``) satırını görüyor. 

#. Ardından `a`'nın değerini, `1` artırıyor (``a += 1``) ve `a`'nın değeri `2`
   oluyor.

#. `a`'nın değeri (yani `2`) `10`'dan küçük olduğu için Python ekrana ilgili
   çıktıyı veriyor.

#. İlk döngüyü bitiren Python başa dönüyor ve `a`'nın değerinin `2` olduğunu
   görüyor. 

#. `a`'nın değerini yine `1` artırıyor ve `a`'yı `3` yapıyor. 

#. `a`'nın değeri hâlâ `10`'dan küçük olduğu için ekrana yine ilgili çıktıyı
   veriyor. 

#. İkinci döngüyü de bitiren Python yine başa dönüyor ve `a`'nın
   değerinin `3` olduğunu görüyor. 

#. Yukarıdaki adımları tekrar eden Python, `a`'nın değeri `9` olana kadar
   ilerlemeye devam ediyor.

#. `a`'nın değeri `9`'a ulaştığında Python `a`'nın değerini bir kez daha
   artırınca bu değer `10`'a ulaşıyor.

#. Python `a`'nın değerinin artık `10`'dan küçük olmadığını görüyor ve
   programdan çıkıyor.

Yukarıdaki kodları şöyle yazarsak belki durum daha anlaşılır olabilir::

	a = 1

	while a < 10:
	    a += 1
	    print(a)

Burada Python'un arkada ne işler çevirdiğini daha net görebiliyoruz. Kodlarımız
içine eklediğimiz ``while`` döngüsü sayesinde Python her defasında `a`
değişkeninin değerini kontrol ediyor ve bu değer `10`'dan küçük olduğu müddetçe
`a` değişkeninin değerini `1` artırıp, yeni değeri ekrana basıyor. Bu değişkenin
değeri `10`'a ulaştığında ise, bu değerin artık `10`'dan küçük olmadığını
anlayıp bütün işlemleri durduruyor.

Gelin isterseniz bu ``while`` döngüsünü daha önce yazdığımız hesap makinemize
uygulayalım::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

    anahtar = 1

    while anahtar == 1:
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
        
        if soru == "q":
            print("çıkılıyor...")
            anahtar = 0

        elif soru == "1":
            sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
            sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
            print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

        elif soru == "2":
            sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
            sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
            print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

        elif soru == "3":
            sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
            sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
            print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

        elif soru == "4":
            sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
            sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
            print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

        elif soru == "5":
            sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
            print(sayı9, "sayısının karesi =", sayı9 ** 2)

        elif soru == "6":
            sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
            print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

        else:
            print("Yanlış giriş.") 
            print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

Burada ilave olarak şu satırları görüyorsunuz::

    anahtar = 1

    while anahtar == 1:
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
        
        if soru == "q":
            print("çıkılıyor...")
            anahtar = 0

Bu kodlarda yaptığımız şey aslında çok basit. Öncelikle değeri `1` olan
`anahtar` adlı bir değişken tanımladık. Bir alt satırda ise, programımızın
sürekli olarak çalışmasını sağlayacak olan ``while`` döngümüzü yazıyoruz.
Programımız, `anahtar` değişkeninin değeri `1` olduğu müddetçe çalışmaya devam
edecek. Daha önce de dediğimiz gibi, eğer bu `anahtar` değişkeninin değerini
programın bir noktasında değiştirmezsek programımız sonsuza kadar çalışmaya
devam edecektir. Çünkü biz programımızı `anahtar` değişkeninin değeri `1` olduğu
sürece çalışmaya ayarladık. İşte programımızın bu tür bir sonsuz döngüye
girmesini önlemek için bir ``if`` bloğu oluşturuyoruz. Buna göre, eğer kullanıcı
klavyede `q` tuşuna basarsa programımız önce `çıkılıyor...` çıktısı verecek,
ardından da `anahtar` değişkeninin `1` olan değerini `0` yapacaktır. Böylece
artık `anahtar`'ın değeri `1` olmayacağı için programımız çalışmaya son
verecektir.

Buradaki mantığın ne kadar basit olduğunu görmenizi isterim. Önce bir değişken
tanımlıyoruz, ardından bu değişkenin değeri aynı kaldığı müddetçe programımızı
çalışmaya ayarlıyoruz. Bu döngüyü kırmak için de başta tanımladığımız o
değişkene başka bir değer atıyoruz. Burada `anahtar` değişkenine atadığımız `1`
ve `0` değerleri tamamen tesadüfidir. Yani siz bu değerleri istediğiniz gibi
değiştirebilirsiniz. Mesela yukarıdaki kodları şöyle de yazabilirsiniz::
    
    anahtar = "hoyda bre!"
    
    #anahtar'ın değeri 'hoyda bre!' olduğu müddetçe aşağıdaki bloğu 
    #çalıştırmaya devam et.
    while anahtar == "hoyda bre!": 
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
    
        if soru == "q":
            print("çıkılıyor...")
            anahtar = "dur yolcu!" 
            #anahtar'ın değeri artık 'hoyda bre!' değil, 'dur yolcu' 
            #olduğu için döngüden çık ve böylece programı sona erdirmiş ol.

Gördüğünüz gibi, amaç herhangi bir değişkene herhangi bir değer atamak ve o
değer aynı kaldığı müddetçe programın çalışmaya devam etmesini sağlamak.
Kurduğumuz bu döngüyü kırmak için de o değişkene herhangi başka bir değer
atamak...

Yukarıda verdiğimiz son örnekte önce `anahtar` adlı bir değişken atayıp,
``while`` döngüsünün işleyişini bu değişkenin değerine göre yapılandırdık. Ama
aslında yukarıdaki kodları çok daha basit bir şekilde de yazabiliriz. Dikkatlice
bakın::
    
    while True:
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
        
        if soru == "q":
            print("çıkılıyor...")
            break

Bu yapıyı hesap makinemize uygulayalım::

    giriş = """
    (1) topla
    (2) çıkar
    (3) çarp
    (4) böl
    (5) karesini hesapla
    (6) karekök hesapla
    """

    print(giriş)

    while True:
        soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
        
        if soru == "q":
            print("çıkılıyor...")
            break

        elif soru == "1":
            sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
            sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
            print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

        elif soru == "2":
            sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
            sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
            print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

        elif soru == "3":
            sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
            sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
            print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

        elif soru == "4":
            sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
            sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
            print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

        elif soru == "5":
            sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
            print(sayı9, "sayısının karesi =", sayı9 ** 2)

        elif soru == "6":
            sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
            print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

        else:
            print("Yanlış giriş.") 
            print("Aşağıdaki seçeneklerden birini giriniz:", giriş)

Bu yapı sayesinde `anahtar` gibi bir değişken atama zorunluluğundan kurtulmuş
olduk. Yukarıdaki kodların nasıl çalıştığını açıklayalım:

`while True` ifadesi şöyle bir anlama gelir:

    `True` olduğu müddetçe... 
    
Peki ne `True` olduğu müddetçe? Burada neyin `True` olması gerektiğini
belirtmediğimiz için, aslında bu kod parçası şu anlama geliyor:

    Aksi belirtilmediği sürece çalışmaya devam et!

Eğer yukarıdaki açıklamayı biraz bulanık bulduysanız şu örneği
inceleyebilirsiniz::
    
    while True:
        print("Bilgisayar çıldırdı!")

Bu kodları çalıştırdığınızda ekrana sürekli olarak `Bilgisayar çıldırdı!`
çıktısı verilecektir. Bu döngüden çıkabilmek için `Ctrl+C` tuşlarına basmanız
gerekiyor. Yukarıdaki kodların sonsuz döngüye girmesinin sorumlusu `while True`
satırıdır. Çünkü burada biz Python'a;

    Aksi belirtilmediği sürece çalışmaya devam et!

emri veriyoruz. Python da bu emrimizi sadakatle yerine getiriyor. Böyle bir
durumda sonsuz döngüyü engellemek için programımızın bir yerinde Python'a bu
döngüden çıkmasını sağlayacak bir emir vermemiz gerekiyor. Biz hesap makinesi
programımızda bu döngüyü şu şekilde kırdık::
    
    if soru == "q":
        print("çıkılıyor...")
        break

Dikkat ederseniz burada ``break`` adlı yeni bir araç görüyoruz. Bu aracın tam
olarak ne işe yaradığını ilerleyen sayfalarda inceleyeceğiz. Şimdilik yalnızca
şunu bilelim: *break* kelimesi İngilizce'de 'kırmak, koparmak, bozmak' gibi
anlamlara gelir. Bu aracın yukarıdaki görevi döngüyü 'kırmak'tır. Dolayısıyla
kullanıcı klavyede `q` tuşuna bastığında, ``while True`` ifadesi ile çalışmaya
başlayan döngü kırılacak ve programımız sona erecektir.

Bu yapıyı daha iyi anlayabilmek için şöyle basit bir örnek daha verelim::

    #Aksi belirtilmediği sürece kullanıcıya
    #aşağıdaki soruyu sormaya devam et!
    while True: 
        soru = input("Nasılsınız, iyi misiniz?")
        
        #Eğer kullanıcı 'q' tuşuna basarsa...
        if soru == "q": 
            break #döngüyü kır ve programdan çık.

Görüyorsunuz, aslında mantık gayet basit: 

    Bir döngü oluştur ve bu döngüden çıkmak istediğinde, programın bir yerinde
    bu döngüyü sona erdirecek bir koşul meydan getir.
    
Bu mantığı yukarıdaki örneğe şu şekilde uyguladık: 

    `while True:` ifadesi yardımıyla bir döngü oluştur ve kullanıcı bu döngüden
    çıkmak istediğinde (yani `q` tuşuna bastığında), döngüyü kır ve programı
    sona erdir.
    
Gelin isterseniz bu konuyu daha net kavramak için bir örnek daha verelim::

    tekrar = 1

    while tekrar <= 3:
        tekrar += 1
        input("Nasılsınız, iyi misiniz?")

Burada programımız kullanıcıya üç kez 'Nasılsınız, iyi misiniz?' sorusunu
soracak ve ardından kapanacaktır. Bu kodlarda ``while`` döngüsünü nasıl
kullandığımıza dikkat edin. Aslında programın mantığı çok basit:

#. Öncelikle değeri `1` olan `tekrar` adlı bir değişken tanımlıyoruz.

#. Bu değişkenin değeri `3`'e eşit veya `3`'ten küçük olduğu müddetçe (``while
   tekrar <= 3``) değişkenin değerine `1` ekliyoruz (``tekrar += 1``).

#. Başka bir deyişle ``bool(tekrar <= 3)`` ifadesi `True` olduğu müddetçe
   değişkenin değerine `1` ekliyoruz.

#. `tekrar` değişkenine her `1` ekleyişimizde kullanıcıya 'Nasılsınız, iyi
   misiniz?' sorusunu soruyoruz (``input("Nasılsınız, iyi misiniz?")``).

#. `tekrar` değişkeninin değeri `3`'ü aştığında ``bool(tekrar <= 3)`` ifadesi
   artık `False` değeri verdiği için programımız sona eriyor. 
   
Yukarıdaki uygulamada Python'ın alttan alta neler çevirdiğini daha iyi görmek
için bu uygulamayı şöyle yazmayı deneyin::
    
    tekrar = 1

    while tekrar <= 3:
        print("tekrar: ", tekrar)
        tekrar += 1
        input("Nasılsınız, iyi misiniz?")
        print("bool değeri: ", bool(tekrar <= 3))

Daha önce de dediğimiz gibi, bir Python programının nasıl çalıştığını anlamanın
en iyi yolu, program içinde uygun yerlere ``print()`` fonksiyonları
yerleştirerek arka planda hangi kodların hangi çıktıları verdiğini izlemektir.
İşte yukarıda da bu yöntemi kullandık. Yani `tekrar` değişkenininin değerini ve
``bool(tekrar <= 3)`` ifadesinin çıktısını ekrana yazdırarak arka tarafta neler
olup bittiğini canlı canlı görme imkanına kavuştuk.

Yukarıdaki programı çalıştırdığımızda şuna benzer çıktılar görüyoruz::

    tekrar:  1
    Nasılsınız, iyi misiniz? evet
    bool değeri:  True
    tekrar:  2
    Nasılsınız, iyi misiniz? evet
    bool değeri:  True
    tekrar:  3
    Nasılsınız, iyi misiniz? evet
    bool değeri:  False

Gördüğünüz gibi, `tekrar` değişkeninin değeri her döngüde `1` artıyor. ``tekrar
<= 3`` ifadesinin bool değeri, `tekrar` adlı değişkenin değeri `3`'ü aşana kadar
hep `True` olacaktır. Bu değişkenin değeri `3`'ü aştığı anda ``tekrar <= 3``
ifadesinin bool değeri `False`'a dönüyor ve böylece ``while`` döngüsü sona
eriyor.

Peki size şöyle bir soru sorsam: Acaba ``while`` döngüsünü kullanarak `1`'den
`100`'e kadar olan aralıktaki çift sayıları nasıl bulursunuz?

Çok basit::

    a = 0

    while a < 100:
        a += 1
        if a % 2 == 0:
            print(a)

Gördüğünüz gibi, ``while`` döngüsünün içine bir adet ``if`` bloğu yerleştirdik.

Yukarıdaki kodları şu şekilde Türkçeye çevirebiliriz:

    `a` değişkeninin değeri `100`'den küçük olduğu müddetçe `a` değişkeninin
    değerini `1` artır. Bu değişkenin değerini her artırışında yeni değerin
    `2`'ye tam bölünüp bölünmediğini kontrol et. Eğer ``a modülüs 2`` değeri `0`
    ise (``if a % 2 == 0``), yani `a`'nın değeri bir çift sayı ise, bu değeri
    ekrana yazdır.
    
Gördüğünüz gibi, ``while`` döngüsü son derece kullanışlı bir araçtır. Üstelik
kullanımı da son derece kolaydır. Bu döngüyle bol bol pratik yaparak bu döngüyü
rahatça kullanabilecek duruma gelebilirsiniz.

En başta da söylediğimiz gibi, Python'da ``while`` dışında bir de ``for``
döngüsü vardır. En az ``while`` kadar önemli bir döngü olan ``for`` döngüsünün
nasıl kullanıldığını anlamaya çalışalım şimdi de.

for Döngüsü
****************

Etrafta yazılmış Python programlarının kaynak kodlarını incelediğinizde, içinde
``for`` döngüsü geçmeyen bir program kolay kolay bulamazsınız. Belki ``while``
döngüsünün kullanılmadığı programlar vardır. Ancak ``for`` döngüsü Python'da o
kadar yaygındır ve o kadar geniş bir kullanım alanına sahiptir ki, hemen hemen
bütün Python programları bu ``for`` döngüsünden en az bir kez yararlanır. 

Peki nedir bu ``for`` döngüsü denen şey?

``for`` da tıpkı ``while`` gibi bir döngüdür. Yani tıpkı ``while`` döngüsünde
olduğu gibi, programlarımızın birden fazla sayıda çalışmasını sağlar. Ancak
``for`` döngüsü ``while`` döngüsüne göre biraz daha yeteneklidir. ``while``
döngüsü ile yapamayacağınız veya yaparken çok zorlanacağınız şeyleri ``for``
döngüsü yardımıyla çok kolay bir şekilde halledebilirsiniz. 

Yalnız, söylediğimiz bu cümleden, ``for`` döngüsünün ``while`` döngüsüne bir
alternatif olduğu sonucunu çıkarmayın. Evet, ``while`` ile yapabildiğiniz bir
işlemi ``for`` ile de yapabilirsiniz çoğu zaman, ama bu döngülerin, belli
vakalar için tek seçenek olduğu durumlar da vardır. Zira bu iki döngünün çalışma
mantığı birbirinden farklıdır.

Şimdi gelelim ``for`` döngüsünün nasıl kullanılacağına...

Dikkatlice bakın::

    tr_harfler = "şçöğüİı"
    
    for harf in tr_harfler:
        print(harf)

Burada öncelikle `tr_harfler` adlı bir değişken tanımladık. Bu değişken Türkçeye
özgü harfleri tutuyor. Daha sonra bir ``for`` döngüsü kurarak, `tr_harfler` adlı
değişkenin her bir öğesini tek tek ekrana yazdırdık.

Peki bu ``for`` döngüsünü nasıl kurduk? 

``for`` döngülerinin söz dizimi şöyledir::

    for değişken_adı in değişken:
        yapılacak_işlem

Bu söz dizimini Türkçe olarak şöyle ifade edebiliriz::

    değişken içindeki herbir öğeyi değişken_adı olarak adlandır:
        ve bu öğelerle bir işlem yap.

Bu soyut yapıları kendi örneğimize uygulayarak durumu daha net anlamaya
çalışalım::
    
    tr_harfler adlı değişken içindeki herbir öğeyi harf olarak adlandır:
        ve harf olarak adlandırılan bu öğeleri ekrana yazdır.

Yukarıdaki örnekte bir ``for`` döngüsü yardımıyla `tr_harfler` adlı değişken
içindeki herbir öğeyi ekrana yazdırdık. Esasında ``for`` döngüsünün
yeteneklerini düşündüğümüzde bu örnek pek heyecan verici değil. Zira aynı işi
aslında ``print()`` fonksiyonu ile de yapabilirdik::
    
    tr_harfler = "şçöğüİı"
    print(*tr_harfler, sep="\n")

Aslında bu işlemi ``while`` ile de yapmak mümkün (Bu kodlardaki, henüz
öğrenmediğimiz kısmı şimdilik görmezden gelin)::

    tr_harfler = "şçöğüİı"
    a = 0

    while a < len(tr_harfler):
        print(tr_harfler[a], sep="\n")
        a += 1

``while`` döngüsü kullanıldığında işi uzattığımızı görüyorsunuz. Dediğimiz gibi,
``for`` döngüsü ``while`` döngüsüne göre biraz daha yeteneklidir ve ``while``
ile yapması daha zor (veya uzun) olan işlemleri ``for`` döngüsü ile çok daha
kolay bir şekilde yapabiliriz. Ayrıca ``for`` döngüsü ile ``while`` döngüsünün
çalışma mantıkları birbirinden farklıdır. ``for`` döngüsü, üzerinde döngü
kurulabilecek veri tiplerinin herbir öğesinin üzerinden tek tek geçer ve bu
öğelerin herbiri üzerinde bir işlem yapar. ``while`` döngüsü ise herhangi bir
ifadenin bool değerini kontrol eder ve bu değerin bool değeri `False` olana
kadar, belirlenen işlemi yapmayı sürdürür.

Bu arada, biraz önce 'üzerinde döngü kurulabilecek veri tipleri' diye bir
kavramdan söz ettik. Örneğin karakter dizileri, üzerinde döngü kurulabilecek bir
veri tipidir. Ama sayılar öyle değildir. Yani sayılar üzerinde döngü kuramayız.
Mesela::
    
    >>> sayılar = 123456789
    >>> for sayı in sayılar:
    ...     print(sayı)
    ...
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not iterable

Buradaki hata mesajından da göreceğiniz gibi `int` (tam sayı) türündeki nesneler
üzerinde döngü kuramıyoruz. Hata mesajında görünen *not iterable* (üzerinde
döngü kurulamaz) ifadesiyle kastedilen de budur.

Gelin isterseniz ``for`` döngüsü ile bir örnek daha vererek durumu iyice
anlamaya çalışalım::

    sayılar = "123456789"
    
    for sayı in sayılar:
        print(int(sayı) * 2)

Burada `sayılar` adlı değişkenin herbir öğesini `sayı` olarak adlandırdıktan
sonra, ``int()`` fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve
herbir öğeyi `2` ile çarptık.

``for`` döngüsünün mantığını az çok anlamış olmalısınız. Bu döngü bir değişken
içindeki herbir öğeyi tek tek ele alıp, iki nokta üst üste işaretinden sonra
yazdığımız kod bloğunu bu öğelere tek tek uyguluyor.

*for* kelimesi İngilizcede 'için' anlamına gelir. Döngünün yapısı içinde geçen
`in` ifadesini de tanıyorsunuz. Biz bu ifadeyi 'Aitlik İşleçleri' konusunu
işlerken de görmüştük. Hatırlarsanız `in` işleci bir öğenin bir veri tipi içinde
bulunup bulunmadığını sorguluyordu. Mesela::
    
    >>> a = "istihza.com"
    >>> "h" in a
    
    True

`"h"` öğesi `"istihza.com"` adlı karakter dizisi içinde geçtiği için ``"h" in
a`` kodu `True` çıktısı veriyor. Bir de şuna bakın::
    
    >>> "b" in a
    
    False

`"b"` öğesi `"istihza.com"` karakter dizisi içinde bulunmuyor. Dolayısıyla ``"b"
in a`` sorgulaması `False` çıktısı veriyor.

*in* kelimesi İngilizcede 'içinde' anlamına geliyor. Dolayısıyla ``for falanca
in filanca:`` yazdığımızda aslında şöyle bir şey demiş oluyoruz:

    `filanca` içinde `falanca` adını verdiğimiz herbir öğe için...
    
Yani şu kod::
    
    for s in "istihza":
        print(s)

Şu anlama geliyor:

    `"istihza"` karakter dizisi içinde `s` adını verdiğimiz herbir öğe için:
        `s` öğesini ekrana basma işlemi gerçekleştir!
        
Ya da şu kod::

    sayılar = "123456789"
    
    for i in sayılar:
        if int(i) > 3:
            print(i)

Şu anlama geliyor:

    `sayılar` değişkeni içinde `i` adını verdiğimiz herbir öğe için:
        eğer sayıya dönüştürülmüş `i` değeri `3`'ten büyükse:
            `i` öğesini ekrana basma işlemi gerçekleştir!

Yukarıdaki temsili kodların Türkçesi bozuk olsa da ``for`` döngüsünün çalışma
mantığını anlamaya yardımcı olacağını zannediyorum. Ama yine de, eğer bu
döngünün mantığını henüz kavrayamadıysanız hiç endişe etmeyin. Zira bu döngüyü
oldukça sık bir biçimde kullanacağımız için, siz istemeseniz de bu döngü
kafanızda yer etmiş olacak.

Bu ``for`` döngüsünü biraz daha iyi anlayabilmek için son bir örnek yapalım::

    tr_harfler = "şçöğüİı"

    parola = input("Parolanız: ")

    for karakter in parola:
        if karakter in tr_harfler:
            print("parolada Türkçe karakter kullanılamaz")

Bu program, kullanıcıya bir parola soruyor. Eğer kullanıcının girdiği parola
içinde Türkçe karakterlerden herhangi biri varsa kullanıcıyı Türkçe karakter
kullanmaması konusunda uyarıyor. Buradaki ``for`` döngüsünü nasıl kurduğumuzu
görüyorsunuz. Aslında burada şu Türkçe cümleyi Pythonca'ya çevirmiş olduk:

    `parola` değişkeni içinde `karakter` adını verdiğimiz herbir öğe için:
        eğer `karakter` değişkeni `tr_harfler` adlı değişken içinde geçiyorsa:
            'parolada Türkçe karakter kullanılamaz' uyarısını göster!

Burada kullandığımız ``for`` döngüsü sayesinde kullanıcının girdiği `parola`
adlı değişken içindeki bütün karakterlere tek tek bakıp, eğer bakılan karakter
`tr_harfler` adlı değişken içinde geçiyorsa kullanıcıyı uyarıyoruz.

Aslında ``for`` döngüsüyle ilgili söyleyeceklerimiz bu kadar değil. Ama henüz bu
döngüyle kullanılan önemli araçları tanımıyoruz. Gerçi zaten bu döngüyü bundan
sonra sık sık kullandığımızı göreceksiniz.

Gelin isterseniz yeni bir konuya geçmeden önce döngülerle ilgili ufak bir örnek
verelim:

Örneğin kullanıcıya bir parola belirletirken, belirlenecek parolanın `8`
karakterden uzun, `3` karakterden kısa olmamasını sağlayalım::
    
    while True:
        parola = input("Bir parola belirleyin: ")

        if not parola:
            print("parola bölümü boş geçilemez!")

        elif len(parola) > 8 or len(parola) < 3:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")
            
        else:
            print("Yeni parolanız", parola)
            break

Burada öncelikle, programınızın sürekli olarak çalışmasını sağlamak için bir
``while`` döngüsü oluşturduk. Buna göre, aksi belirtilmedikçe (``while True``)
programımız çalışmaya devam edecek.

``while`` döngüsünü kurduktan sonra kullanıcıya bir parola soruyoruz (``parola =
input("Bir parola belirleyin: ")``)

Eğer kullanıcı herhangi bir parola belirlemeden doğrudan `Enter` tuşuna basarsa,
yani `parola` değişkeninin bool değeri `False` olursa (``if not parola``),
kullanıcıya 'parola bölümü boş geçilemez!' uyarısı veriyoruz.

Eğer kullanıcı tarafından belirlenen parolanın uzunluğu `8` karakterden fazlaysa
ya da `3` karakterden kısaysa, 'parola 8 karakterden uzun 3 karakterden kısa
olmamalı' uyarısı veriyoruz.

Yukarıdaki koşullar harici durumlar için ise (``else``), belirlenen yeni
parolayı kullanıcıya gösterip döngüden çıkıyoruz (``break``).

Bu arada, hatırlarsanız ``eval()`` fonksiyonunu anlatırken şöyle bir örnek
vermiştik::

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

Bu programdaki eksiklikleri ve riskleri biliyorsunuz. Böyle bir program
yazdığınızda, ``eval()`` fonksiyonunu kontrolsüz bir şekilde kullandığınız için
önemli bir güvenlik açığına sebep olmuş oluyorsunuz. Gelin isterseniz bu derste
öğrendiğimiz bilgileri de kullanarak yukarıdaki ``eval()`` fonksiyonu için basit
bir kontrol mekanizması kuralım::
    
    izinli_karakterler = "0123456789+-/*= "

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

    while True:
        veri = input("İşleminiz: ")
        if veri == "q":
            print("çıkılıyor...")
            break
    
        for s in veri:
            if s not in izinli_karakterler:
                print("Neyin peşindesin?!")
                quit()
                
        hesap = eval(veri)
    
        print(hesap)

Burada öncelikle programımızı bir ``while`` döngüsü içine aldık. Böylece
programımızın ne zaman sona ereceğini kendimiz belirleyebileceğiz. Buna göre
eğer kullanıcı klavyede 'q' tuşuna basarsa ``while`` döngüsü sona erecek.

Bu programda bizi özellikle ilgilendiren kısım şu::

    izinli_karakterler = "0123456789+-/*= "

    for s in veri:
        if s not in izinli_karakterler:
            print("Neyin peşindesin?!")
            quit()
            
    hesap = eval(veri)

Gördüğünüz gibi, ilk olarak `izinli_karakterler` adlı bir değişken tanımladık.
Program içinde kullanılmasına izin verdiğimiz karakterleri bu değişken içine
yazıyoruz. Buna göre kullanıcı yalnızca `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`,
`8` ve `9` sayılarını, `+`, `-`, `/`, `*` ve `=` işleçlerini, ayrıca boşluk
karakterini (' ') kullanabilecek.

Kullanıcının girdiği veri üzerinde bir ``for`` döngüsü kurarak, veri içindeki
her bir karakterin `izinli_karakterler` değişkeni içinde yer alıp almadığını
denetliyoruz. İzin verilen karakterler dışında herhangi bir karakterin girilmesi
`Neyin peşindesin?!` çıktısının verilip programdan tamamen çıkılmasına
(``quit()``) yol açacaktır.

Eğer kullanıcı izinli karakterleri kullanarak bir işlem gerçekleştirmişse
``hesap = eval(veri)`` kodu aracılığıyla, kullanıcının yaptığı işlemi ``eval()``
fonksiyonuna gönderiyoruz.

Böylece ``eval()`` fonksiyonunu daha güvenli bir hale getirebilmek için basit
bir kontrol mekanizmasının nasıl kurulabileceğini görmüş olduk. Kurduğumuz
kontrol mekanizmasının esası, kullanıcının girebileceği veri türlerini
sınırlamaya dayanıyor. Böylece kullanıcı mesela şöyle tehlikeli bir komut
giremiyor::

    __import__("os").system("dir")

Çünkü bu komutu yazabilmesi için gereken karakterler `izinli_karakterler`
değişkeni içinde tanımlı değil. Kullanıcı yalnızca basit bir hesap makinesinde
kullanılabilecek olan sayıları ve işleçleri girebiliyor.

İlgili Araçlar
***************

Elbette döngüler tek başlarına bir şey ifade etmezler. Döngülerle işe yarar
kodlar yazabilmemiz için bazı araçlara ihtiyacımız var. İşte bu bölümde
döngüleri daha verimli kullanmamızı sağlayacak bazı fonksiyon ve deyimlerden söz
edeceğiz. İlk olarak ``range()`` adlı bir fonksiyondan bahsedelim.

range Fonksiyonu
=================

*range* kelimesi İngilizcede 'aralık' anlamına gelir. Biz Python'da ``range()``
fonksiyonunu belli bir aralıkta bulunan sayıları göstermek için kullanıyoruz.
Örneğin::
    
    >>> for i in range(0, 10):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

Gördüğünüz gibi, ``range(0, 10)`` kodu sayesinde ve ``for`` döngüsünü de
kullanarak, `0` ile `10` (`10` hariç) aralığındaki sayıları ekrana yazdırdık.

Yukarıdaki kodda ``range()`` fonksiyonuna `0` ve `10` olmak üzere iki adet
parametre verdiğimizi görüyorsunuz. Burada `0` sayısı, aralıktaki ilk sayıyı,
`10` sayısı ise aralıktaki son sayıyı gösteriyor. Yani ``range()`` fonksiyonunun
formülü şöyledir::

    range(ilk_sayı, son_sayı)

Bu arada, ``range(ilk_sayı, son_sayı)`` kodunun verdiği çıktıya ilk_sayının
dahil olduğuna, ama son_sayının dahil olmadığına dikkat edin.

Eğer ``range()`` fonksiyonunun ilk parametresi `0` olacaksa, bu parametreyi
belirtmesek de olur. Yani mesela `0`'dan `10`'a kadar olan sayıları
listeleyeceksek ``range()`` fonksiyonunu şöyle yazmamız yeterli olacaktır::

    >>> for i in range(10): 
    ...     print(i)

``range()`` fonksiyonunun `ilk_sayı` parametresi verilmediğinde Python ilk
parametreyi `0` olarak alır. Yani ``range(10)`` gibi bir kodu Python ``range(0,
10)`` olarak algılar. Elbette, eğer aralıktaki ilk sayı `0`'dan farklı olacaksa
bu sayıyı açık açık belirtmek gerekir::

    >>> for i in range(3, 20): 
    ...     print(i)

Burada `3`'ten itibaren `20`'ye kadar olan sayılar ekrana dökülecektir.

Hatırlarsanız, biraz önce, kullanıcının `3` karakterden kısa, `8` karakterden
uzun parola belirlemesini engelleyen bir uygulama yazmıştık. O uygulamayı
``range()`` fonksiyonunu kullanarak da yazabiliriz::
    
    while True:
        parola = input("parola belirleyin: ")
        
        if not parola:
            print("parola bölümü boş geçilemez!")
        
        elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter
            #aralığında ise...
            print("Yeni parolanız", parola)
            break
        
        else:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

Bu fonksiyonu kullanarak bir döngünün kaç kez çalışacağını da
belirleyebilirsiniz. Aşağıdaki kodları dikkatlice inceleyin::

    for i in range(3):
        parola = input("parola belirleyin: ")
        if i == 2:
            print("parolayı 3 kez yanlış girdiniz.",
            "Lütfen 30 dakika sonra tekrar deneyin!")
        
        elif not parola:
            print("parola bölümü boş geçilemez!")
        
        elif len(parola) in range(3, 8):
            print("Yeni parolanız", parola)
            break
        
        else:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

Burada ``if i == 2`` kodu sayesinde ``for`` döngüsü içinde belirttiğimiz `i`
adlı değişkenin değeri `2` olduğu anda 'parolayı 3 kez yanlış girdiniz...'
uyarısı gösterilecektir. Daha önce de birkaç yerde ifade ettiğimiz gibi, eğer
yukarıdaki kodların çalışma mantığını anlamakta zorlanıyorsanız, programın uygun
yerlerine ``print()`` fonksiyonu yerleştirerek arka planda Python'ın neler
çevirdiğini daha net görebilirsiniz. Örneğin::
    
    for i in range(3):
        print(i)
        parola = input("parola belirleyin: ")
        if i == 2:
            print("parolayı 3 kez yanlış girdiniz.",
            "Lütfen 30 dakika sonra tekrar deneyin!")
        
        elif not parola:
            print("parola bölümü boş geçilemez!")
        
        elif len(parola) in range(3, 8):
            print("Yeni parolanız", parola)
            break
        
        else:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

Gördüğünüz gibi, `i` değişkeninin başlangıçtaki değeri `0`. Bu değer her döngüde
`1` artıyor ve bu değişkenin değeri `2` olduğu anda ``if i == 2`` bloğu devreye
giriyor.

``range()`` fonksiyonunun yetenekleri yukarıda anlattıklarımızla sınırlı
değildir. Bu fonksiyonun bazı başka maharetleri de bulunur. Hatırlarsanız
yukarıda bu fonksiyonun formülünü şöyle vermiştik::
    
    range(ilk_sayı, son_sayı)

Buna göre ``range()`` fonksiyonu iki parametre alıyor. Ama aslında bu
fonksiyonun üçüncü bir parametresi daha vardır. Buna göre formülümüzü
güncelleyelim::
    
    range(ilk_sayı, son_sayı, atlama_değeri)

Formüldeki son parametre olan `atlama_değeri`, aralıktaki sayıların kaçar kaçar
ilerleyeceğini gösterir. Yani::
    
    >>> for i in range(0, 10, 2):
    ...     print(i)
    ...
    
    0
    2
    4
    6
    8

Gördüğünüz gibi, son parametre olarak verdiğimiz `2` sayısı sayesinde `0`'dan
`10`'a kadar olan sayılar ikişer ikişer atlayarak ekrana dökülüyor.

Bu arada, bir şey dikkatinizi çekmiş olmalı:

``range()`` fonksiyonu üç farklı parametre alan bir fonksiyon. Eğer ilk
parametre `0` olacaksa bu parametreyi belirtmek zorunda olmadığımızı biliyoruz.
Yani::
    
    >>> range(10)

Python bu kodu ``range(0, 10)`` olarak algılayıp buna göre değerlendiriyor.
Ancak eğer ``range()`` fonksiyonunda üçüncü parametreyi de kullanacaksak, yani
``range(0, 10, 2)`` gibi bir komut vereceksek, üç parametrenin tamamını da
belirtmemiz gerekiyor. Eğer burada bütün parametreleri belirtmezsek Python hangi
sayının hangi parametreye karşılık geldiğini anlayamaz. Yani mesela `0`'dan
`10`'a kadar olan sayıları ikişer ikişer atlayarak ekrana dökmek için şöyle bir
şey yazmaya çalıştığımızı düşünün::
    
    >>> for i in range(10, 2):
    ...     print(i)

Burada Python ne yapmaya çalıştığınızı anlayamaz. Parantez içinde ilk değer
olarak `10`, ikinci değer olarak ise `2` yazdığınız için, Python bu `10`
sayısını başlangıç değeri; `2` sayısını ise bitiş değeri olarak algılayacaktır.
Dolayısıyla da Python bu durumda sizin `10`'dan `2`'ye kadar olan sayıları
listelemek istediğinizi zannedecek, ``range()`` fonksiyonuyla bu şekilde geriye
doğru sayamayacağımız için de boş bir çıktı verecektir. Bu yüzden, Python’un
şaşırmaması için yukarıdaki örneği şu şekilde yazmalıyız::
    
    >>> for i in range(0, 10, 2):
    ...     print(i)

Kısacası, eğer ``range()`` fonksiyonunun kaçar kaçar sayacağını da belirtmek
istiyorsak, parantez içinde, gerekli bütün parametreleri belirtmeliyiz.

Gördüğünüz gibi, ``range()`` fonksiyonunu kullanarak belirli bir aralıktaki
sayıları alabiliyoruz. Peki bu sayıları tersten alabilir miyiz? Elbette::
    
    >>> for i in range(10, 0, -1):
    ...     print(i)
    ...
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

Burada ``range()`` fonksiyonunu nasıl yazdığımıza çok dikkat edin. Sayıları
tersten alacağımız için, ilk parametre 10, ikinci parametre ise `0`. Üçüncü
parametre olarak ise eksi değerli bir sayı veriyoruz. Eğer sayıları hem tersten,
hem de mesela 3'er 3'er atlayarak yazmak isterseniz şöyle bir komut
verebilirsiniz::
    
    >>> for i in range(10, 0, -3):
    ...     print(i)
    ...
    10
    7
    4
    1

Bu arada, etkileşimli kabukta ``range(10)`` gibi bir komut verdiğinizde
`range(0, 10)` çıktısı aldığınızı görüyorsunuz. Bu çıktı, verdiğimiz komutun `0`
ile `10` arası sayıları elde etmemizi sağlayacağını belirtiyor, ama bu sayıları
o anda bize göstermiyor. Daha önce verdiğimiz örneklerden de anlaşılacağı gibi,
`0`-`10` aralığındaki sayıları görebilmek için ``range(10)`` ifadesi üzerinde
bir ``for`` döngüsü kurmamız gerekiyor. ``range(10)`` ifadesinin taşıdığı
sayıları görebilmek için ``for`` döngüsü kurmak tek seçenek değildir. Bu işlem
için yıldızlı parametrelerden de yararlanabiliriz. ``print()`` fonksiyonunu
incelediğimiz derste yıldızlı parametrelerin nasıl kullanıldığını göstermiştik.
Dilerseniz şimdi bu parametre tipini ``range()`` fonksiyonuna nasıl
uygulayabileceğimizi görelim::
    
    >>> print(*range(10))
    
    0 1 2 3 4 5 6 7 8 9

``print()`` fonksiyonunun `sep` parametresi yardımıyla bu çıktıyı istediğiniz
gibi düzenleyebileceğinizi biliyorsunuz. Mesela çıktıdaki sayıları
birbirlerinden virgülle ayırmak için şöyle bir komut verebiliyoruz::
    
    >>> print(*range(10), sep=", ")

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
Böylece ``range()`` fonksiyonunu enine boyuna incelemiş ve bu fonksiyonun ne işe
yaradığını, nasıl kullanılacağını anlamamızı sağlayan örnekler vermiş olduk.
Artık başka bir konuyu geçebiliriz.

pass Deyimi
============

*pass* kelimesi İngilizcede 'geçmek, pas geçmek' gibi anlamlara gelir.
Python'daki kullanımı da bu anlama oldukça yakındır. Biz bu deyimi Pyhon’da
'görmezden gel, hiçbir şey yapma' anlamında kullanacağız.

Dilerseniz ``pass`` deyimini tarif etmeye çalışmak yerine bu deyimi bir örnek
üzerinde açıklamaya çalışalım.

Hatırlarsanız yukarıda şöyle bir örnek vermiştik::

    while True:
        parola = input("parola belirleyin: ")
        
        if not parola:
            print("parola bölümü boş geçilemez!")
        
        elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter
            #aralığında ise...
            print("Yeni parolanız", parola)
            break
        
        else:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

Burada mesela eğer kullanıcı parolayı boş bırakırsa 'parola bölümü boş
geçilemez!' uyarısı gösteriyoruz. Şimdi o ``if`` bloğunu şöyle yazdığımızı
düşünün::
    
    while True:
        parola = input("parola belirleyin: ")
        
        if not parola:
            pass
            
        elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter
            #aralığında ise...
            print("Yeni parolanız", parola)
            break
        
        else:
            print("parola 8 karakterden uzun 3 karakterden kısa olmamalı") 

Burada, eğer kullanıcı parolayı boş bırakırsa programımız hiçbir şey yapmadan
yoluna devam edecektir. Yani burada ``pass`` deyimi yardımıyla programımıza şu
emri vermiş oluyoruz:

    Eğer kullanıcı parolayı boş geçerse görmezden gel. Hiçbir şey yapmadan
    yoluna devam et!
    
Başka bir örnek daha verelim::

    while True:
        sayı = int(input("Bir sayı girin: "))
        
        if sayı == 0:
            break
        
        elif sayı < 0:
            pass
        
        else:
            print(sayı)

Burada eğer kullanıcı `0` sayısını girerse programımız sona erer (``break``
deyimini biraz sonra inceleyeceğiz). Eğer kullanıcı `0`'dan küçük bir sayı
girerse, yani kullanıcının girdiği sayı eksi değerli ise, ``pass`` deyimininin
etkisiyle programımız hiçbir şey yapmadan yoluna devam eder. Bu koşulların
dışındaki durumlarda ise programımız kullanıcının girdiği sayıları ekrana
yazdıracaktır.

Yukarıda anlatılan durumların dışında, ``pass`` deyimini kodlarınız henüz taslak
aşamasında olduğu zaman da kullanabilirsiniz. Örneğin, diyelim ki bir kod
yazıyorsunuz. Programın gidişatına göre, bir noktada yapmanız gereken bir işlem
var, ama henüz ne yapacağınıza karar vermediniz. Böyle bir durumda ``pass``
deyiminden yararlanabilirsiniz. Mesela birtakım ``if`` deyimleri yazmayı
düşünüyor olun::
    
    if .....:
        böyle yap
        
    elif .....:
        şöyle yap
        
    else:
        pass
        
Burada henüz ``else`` bloğunda ne yapılacağına karar vermemiş olduğunuz için,
oraya bir ``pass`` koyarak durumu şimdilik geçiştiriyorsunuz. Program son haline
gelene kadar oraya bir şeyler yazmış olacaksınız.

Sözün özü, ``pass`` deyimlerini, herhangi bir işlem yapılmasının gerekli
olmadığı durumlar için kullanıyoruz. İlerde işe yarar programlar yazdığınızda,
bu ``pass`` deyiminin göründüğünden daha faydalı bir araç olduğunu
anlayacaksınız.

break Deyimi
==============

Python’da ``break`` özel bir deyimdir. Bu deyim yardımıyla, devam eden bir
süreci kesintiye uğratabiliriz. Bu deyimin kullanıldığı basit bir örnek
verelim::
    
    >>> while True:
    ...     parola = input("Lütfen bir parola belirleyiniz:")
    ...     if len(parola) < 5:
    ...         print("Parola 5 karakterden az olmamalı!")
    ...     else:
    ...         print("Parolanız belirlendi!")
    ...         break

    
Burada, eğer kullanıcının girdiği parolanın uzunluğu `5` karakterden azsa,
`Parola 5 karakterden az olmamalı!` uyarısı gösterilecektir. Eğer kullanıcı `5`
karakterden uzun bir parola belirlemişse, kendisine 'Parolanız belirlendi!'
mesajını gösterip, ``break`` deyimi yardımıyla programdan çıkıyoruz.

Gördüğünüz gibi, ``break`` ifadesinin temel görevi bir döngüyü sona erdirmek.
Buradan anlayacağımız gibi, ``break`` ifadesinin her zaman bir döngü içinde yer
alması gerekiyor. Aksi halde Python bize şöyle bir hata verecektir::

    SyntaxError: 'break' outside loop

Yani::

    SözDizimiHatası: ``break`` döngü dışında ..

continue Deyimi
====================

``continue`` ilginç bir deyimdir. İsterseniz ``continue`` deyimini anlatmaya
çalışmak yerine bununla ilgili bir örnek verelim::
    
    while True:
        s = input("Bir sayı girin: ")
        if s == "iptal":
            break
        
        if len(s) <= 3:
            continue
        
        print("En fazla üç haneli bir sayı girebilirsiniz.")

Burada eğer kullanıcı klavyede `iptal` yazarsa programdan çıkılacaktır. Bunu; ::

	if s == "iptal":
	    break

satırıyla sağlamayı başardık.

Eğer kullanıcı tarafından girilen sayı üç haneli veya daha az haneli bir sayı
ise, ``continue`` ifadesinin etkisiyle::

	>>> print("En fazla üç haneli bir sayı girebilirsiniz.")

satırı es geçilecek ve döngünün en başına gidilecektir.

Eğer kullanıcının girdiği sayıdaki hane üçten fazlaysa ekrana::

	En fazla üç haneli bir sayı girebilirsiniz.

cümlesi yazdırılacaktır.

Dolayısıyla buradan anladığımıza göre, ``continue`` deyiminin görevi kendisinden
sonra gelen her şeyin es geçilip döngünün başına dönülmesini sağlamaktır. Bu
bilgiye göre, yukarıdaki programda eğer kullanıcı, uzunluğu üç karakterden az
bir sayı girerse ``continue`` deyiminin etkisiyle programımız döngünün en başına
geri gidiyor. Ama eğer kullanıcı, uzunluğu üç karakterden fazla bir sayı
girerse, ekrana 'En fazla üç haneli bir sayı girebilirsiniz,' cümlesinin
yazdırıldığını görüyoruz.

Örnek Uygulamalar
******************

Python programlama dilinde döngülerin neye benzediğini öğrendik. Bu bölünde
ayrıca döngülerle birlikte kullanabileceğimiz başka araçları da tanıdık. Şimdi
dilerseniz bu öğrendiklerimizi pekiştirmek için birkaç ufak çalışma yapalım.

Karakter Dizilerinin İçeriğini Karşılaştırma
================================================

Diyelim ki elinizde şöyle iki farklı metin var::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

Siz burada, `ilk_metin` adlı değişken içinde bulunan, ama `ikinci_metin` adlı
değişken içinde bulunmayan öğeleri ayıklamak istiyorsunuz. Yani bu iki metnin
içeriğini karşılaştırıp, farklı öğeleri bulmayı amaçlıyorsunuz. Bu işlem için,
bu bölümde öğrendiğimiz döngülerden ve daha önce öğrendiğimiz başka araçlardan
yararlanabilirsiniz. Şimdi dikkatlice bakın::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

    for s in ilk_metin:
        if not s in ikinci_metin:
            print(s)

Bu kodları bir dosyaya kaydedip çalıştırdığımızda şu çıktıyı alıyoruz::
    
    a
    a
    ş
    ş
    a
    
Demek ki `ilk_metin` adlı değişkende olup da `ikinci_metin` adlı değişkende
olmayan öğeler bunlarmış... 

Bu kodlarda anlayamayacağınız hiçbir şey yok. Ama dilerseniz biz yine de bu
kodları tek tek inceleyelim. 

İlk olarak değişkenlerimizi tanımladık::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"  

Amacımız `ilk_metin`'de olan, ama `ikinci_metin`'de olmayan öğeleri görmek.
Bunun için `ilk_metin`'deki öğeleri **tek tek** `ikinci_metin`'deki öğelerle
karşılaştırmamız gerekiyor. Tahmin edebileceğiniz gibi, bir metnin bütün
öğelerine tek tek bakabilmenin en iyi yolu ``for`` döngülerini kullanmaktır. O
halde döngümüzü yazalım::
    
    for s in ilk_metin: #ilk_metin'deki, 's' adını verdiğimiz bütün öğeler için
        if not s in ikinci_metin: #eğer 's' adlı bu öğe ikinci_metin'de yoksa
            print(s) #'s' adlı öğeyi ekrana bas
   
Gördüğünüz gibi, döngüleri (``for``), bool işleçlerini (`not`) ve aitlik
işleçlerini (`in`) kullanarak, istediğimiz şeyi rahatlıkla yapabiliyoruz. Burada
kullandığımız ``if`` deyimi, bir önceki satırda ``for`` döngüsü ile üzerinden
geçtiğimiz öğeleri süzmemizi sağlıyor. Burada temel olarak şu üç işlemi
yapıyoruz:

#. `ilk_metin` içindeki bütün öğelerin üzerinden geçiyoruz,
#. Bu öğeleri belli bir ölçüte göre süzüyoruz,
#. Ölçüte uyan öğeleri ekrana basıyoruz.

Elbette yukarıda yaptığımız işlemin tersini yapmak da mümkündür. Biz yukarıdaki
kodlarda `ilk_metin`'de olan, ama `ikinci_metin`'de olmayan öğeleri süzdük. Eğer
istersek `ikinci_metin`'de olan, ama `ilk_metin`'de olmayan öğeleri de
süzebiliriz. Mantığımız yine aynı::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
    
    for s in ikinci_metin: #ikinci_metin'deki, 's' adını verdiğimiz bütün öğeler için
        if not s in ilk_metin: #eğer 's' adlı bu öğe ilk_metin'de yoksa
            print(s) #'s' adlı öğeyi ekrana bas

Bu da bize şu çıktıyı veriyor::    
           
    u
    ı
    o
    r
    y
    e
    u
    ı
    r
    u
    e
    e
    e
    u

Gördüğünüz gibi, yaptığımız tek şey, `ilk_metin` ile `ikinci_metin`'in yerlerini
değiştirmek oldu. Kullandığımız mantık ise değişmedi.

Bu arada, yukarıdaki çıktıda bizi rahatsız eden bir durum var. Çıktıda bazı
harfler birbirini tekrar ediyor. Aslında temel olarak sadece şu harfler var::
    
    u
    ı
    o
    r
    y
    e
 
Ama metin içinde bazı harfler birden fazla sayıda geçtiği için, doğal olarak
çıktıda da bu harfler birden fazla sayıda görünüyor. Ama tabii ki, eğer biz
istersek farklı olan her harften yalnızca bir tanesini çıktıda görmeyi de tercih
edebiliriz. Bunun için şöyle bir kod yazabiliriz::

    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
    
    fark = ""
    
    for s in ikinci_metin:
        if not s in ilk_metin:
            if not s in fark:
                fark += s
    print(fark)

Burada da anlayamayacağımız hiçbir şey yok. Bu kodlardaki bütün parçaları
tanıyoruz. Herzamanki gibi öncelikle değişkenlerimizi tanımladık::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
    
Daha sonra `fark` adlı boş bir karakter dizisi tanımlıyoruz. Metinler içindeki
farklı karakter dizilerini `fark` adlı bu karakter dizisi içinde depolayacağız. 

Ardından da ``for`` döngümüzü yazıyoruz::

    for s in ikinci_metin:      # ikinci_metin'de 's' dediğimiz bütün öğeler için
        if not s in ilk_metin:  # eğer 's' ilk_metin'de yoksa
            if not s in fark:   # eğer 's' fark'ta da yoksa
                fark += s       # bu öğeyi fark değişkenine ekle
    print(fark)                 # fark değişkenini ekrana bas
    
Uyguladığımız mantığın ne kadar basit olduğunu görüyorsunuz. Bu kodlarda basitçe
şu işlemleri yapıyoruz:

#. `ikinci_metin` değişkeni içindeki bütün öğelerin üzerinden tek tek geç,
#. Eğer bu değişkendeki herhangi bir öğe `ilk_metin`'de ve `fark`'ta yoksa o
   öğeyi `fark`'a ekle.
#. Son olarak da `fark`'ı ekrana bas.

Bu kodlarda dikkatimizi çeken ve üzerinde durmamız gereken bazı noktalar var.
Burada özellikle `fark` değişkenine öğe ekleme işlemini nasıl yaptığımıza dikkat
edin. 

Python programlama dilinde önceden oluşturduğumuz bir karakter dizisini başka
bir karakter dizisi ile birleştirdiğimizde bu işlem ilk oluşturduğumuz karakter
dizisini etkilemez. Yani::
    
    >>> a = 'istihza'
    >>> a + '.com'
    
    'istihza.com'

Burada sanki `a` adlı özgün karakter dizisini değiştirmişiz ve 'istihza.com'
değerini elde etmişiz gibi görünüyor. Ama aslında `a`'nın durumunda hiçbir
değişiklik yok::
    
    >>> a
    
    'istihza'

Gördüğünüz gibi, `a` değişkeninin değeri hâlâ `'istihza'`. Bu durumun nedeni,
birleştirme işlemlerinin bir değiştirme işlemi olmamasıdır. Yani mesela iki
karakter dizisini birleştirdiğinizde birleşen karakter dizileri üzerinde
herhangi bir değişiklik olmaz. Bu durumda yapabileceğimiz tek şey, karakter
dizisine eklemek istediğimiz öğeyi de içeren yeni bir karakter dizisi
oluşturmaktır. Yani::
    
    >>> a = 'istihza'
    >>> a = a + '.com'
    >>> print(a)
    
    istihza.com

Burada sanki değeri `'istihza'` olan `a` adlı bir değişkene `'.com'` değerini
eklemişiz gibi görünüyor, ama aslında biz burada `a` değişkenini yok edip,
`'istihza.com'` değerini içeren, `a` adlı başka bir değişken tanımladık. Bu
durumu nasıl teyit edeceğinizi biliyorsunuz::
    
    >>> a = 'istihza'
    >>> id(a)
    
    15063200
    
    >>> a = a + '.com'
    >>> id(a)
    
    15067960
    
Burada ``id()`` fonksiyonunu kullanarak karakter dizilerinin kimliklerini
sorguladık. Gördüğünüz gibi, isimleri aynı da olsa, aslında ortada iki farklı
`a` değişkeni var. Kimlik numaralarının farklı olmasından anladığımıza göre, ilk
başta tanımladığımız `a` değişkeni ile ``a = a + '.com'`` satırıyla
oluşturduğumuz `a` değişkeni birbirinden farklı. 

Bu arada, eğer istersek yukarıdaki değer atama işlemini, önceki bölümlerde
öğrendiğimiz değer atama işleçleri yardımıyla kısaltabileceğimizi de
biliyorsunuz::
    
    >>> a += '.com'
    
İşte `ilk_metin` ile `ikinci_metin` değişkenleri arasındaki farklı harfleri
yalnızca birer kez yazdırmak için kullandığımız kodlarda da yukarıdaki işlemi
yaptık::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
    
    fark = ''
    
    for s in ikinci_metin:
        if not s in ilk_metin:
            if not s in fark:
                fark += s
    print(fark)

Gördüğünüz gibi, önce boş bir `fark` değişkeni oluşturduk. Daha sonra bu
değişkene ``for`` döngüsü içinde yeni değerler atayabilmek (daha doğrusu
atarmış gibi yapmak) için ``fark += s`` gibi bir kod kullandık. Böylece `for`
döngüsünün her dönüşünde `s` adını verdiğimiz herbir öğeyi tek tek `fark`
değişkenine yolladık. Böylece program sonunda elimizde, farklı öğeleri yalnızca
birer kez içeren `fark` adlı bir değişken olmuş oldu. Dediğimiz gibi, ilk başta
tanımladığımız boş `fark` değişkeni ile, program sonunda farklı değerleri içeren
`fark` değişkeni aslında aynı değil. Yani biz ilk `fark` değişkenine döngünün
her dönüşünde yeni bir öğe eklemek yerine, döngünün her dönüşünde yeni bir
`fark` değişkeni oluşturmuş oluyoruz. Ama programın sonunda sanki `fark`
değişkenine her defasında yeni bir değer atamışız gibi görünüyor ve bu da bizim
işimizi görmemize yetiyor...

Programın başındaki ve sonundaki `fark` değişkenlerinin aslında birbirinden
farklı olduğunu teyit etmek için şu kodları kullanabilirsiniz::
    
    ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
    ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
    
    fark = ""
    print("fark'ın ilk tanımlandığı zamanki kimlik numarası: ", id(fark))
    
    for s in ikinci_metin:
        if not s in ilk_metin:
            if not s in fark:
                fark += s
    
    print("fark'ın program sonundaki kimlik numarası: ", id(fark))

Gördüğünüz gibi, gerçekten de ortada iki farklı `fark` değişkeni var. Bu durumu
``id()`` fonksiyonu yardımıyla doğrulayabiliyoruz.

Peki bu bilginin bize ne faydası var?

Şimdilik şu kadarını söyleyelim: Eğer o anda muhatap olduğunuz bir veri tipinin
mizacını, huyunu-suyunu bilmezseniz yazdığınız programlarda çok kötü
sürprizlerle karşılaşabilirsiniz. Birkaç bölüm sonra başka veri tiplerini de
öğrendikten sonra bu durumu daha ayrıntılı bir şekilde inceleyeceğiz.

Bu arada, tahmin edebileceğiniz gibi yukarıdaki ``for`` döngüsünü şöyle de
yazabilirdik::

    for s in ikinci_metin:
        if not s in ilk_metin and not s in fark:
            fark += s

Burada iki farklı ``if`` deyimini iki farklı satırda yazmak yerine, bu deyimleri
`and` işleci ile birbirine bağladık.

Bu örnek ile ilgili söyleyeceklerimiz şimdilik bu kadar. Gelin biz şimdi
isterseniz bilgilerimizi pekiştirmek için başka bir örnek daha yapalım.

Dosyaların İçeriğini Karşılaştırma
==================================

Bir önceki örnekte karakter dizilerinin içeriğini nasıl karşılaştırabileceğimizi
gösteren bir örnek vermiştik. Şimdi de, gerçek hayatta karşınıza çıkması daha
olası bir durum olması bakımından, dosyaların içeriğini nasıl
karşılaştıracağımıza dair bir örnek verelim.

Esasında karakter dizilerinin içeriğini birbirleriyle nasıl karşılaştırıyorsak,
dosyaların içeriğini de benzer şekilde karşılaştırabiliriz. Mesela içeriği şu
olan `isimler1.txt` adlı bir dosyamız olduğunu varsayalım::
    
    Ahmet
    Mehmet
    Sevgi
    Sinan
    Deniz
    Ege
    Efe
    Ferhat
    Fırat
    Zeynep
    Hazan
    Mahmut
    Celal
    Cemal
    Özhan
    Özkan

Yine içeriği şu olan bir de `isimler2.txt` adlı başka bir dosya daha olduğunu
düşünelim::
    
    Gürsel
    Mehmet
    Sevgi
    Sami
    Deniz
    Ege
    Efe
    Ferhat
    Fırat
    Tülay
    Derya
    Hazan
    Mahmut
    Tezcan
    Cemal
    Özhan
    Özkan
    Özcan
    Dilek

Amacımız bu iki dosyanın içeriğini karşılaştırıp, farklı öğeleri ortaya sermek.
Dediğimiz gibi, bir önceki örnekte izlediğimiz yolu burada da takip edebiliriz.
Dikkatlice bakın::
    
    d1 = open("isimler1.txt") # dosyayı açıyoruz
    d1_satırlar = d1.readlines() # satırları okuyoruz
    
    d2 = open("isimler2.txt")
    d2_satırlar = d2.readlines()
    
    for i in d2_satırlar:
        if not i in d1_satırlar:
            print(i)
            
    d1.close()
    d2.close()
            
Gerçekten de mantığın bir önceki örnekle tamamen aynı olduğunu görüyorsunuz. Biz
henüz Python'da dosyaların nasıl işleneceğini öğrenmedik, ama daha önce
gördüğümüz ``open()`` fonksiyonu yardımıyla en azından dosyaları açabilecek
kadar biliyoruz dosya işlemlerinin nasıl yürütüleceğini... 

Burada farklı olarak ``readlines()`` adlı bir metot görüyoruz. Biz burada bu
metodun ayrıntılarına inmeyeceğiz, ama şimdilik dosya içeriğinin satırlar
halinde okunmasını sağladığını bilelim yeter.

Bu arada, eğer çıktıda Türkçe karakterleri düzgün görüntüleyemiyorsanız
``open()`` fonksiyonunun `encoding` adlı bir parametresi vasıtasıyla içeriği
`UTF-8` olarak kodlayabilirsiniz::
    
    d1 = open("isimler1.txt", encoding="utf-8") # dosyayı açıyoruz
    d1_satırlar = d1.readlines() # satırları okuyoruz
    
    d2 = open("isimler2.txt", encoding="utf-8")
    d2_satırlar = d2.readlines()
    
    for i in d2_satırlar:
        if not i in d1_satırlar:
            print(i)
            
    d1.close()
    d2.close()
            
Bu şekilde Türkçe karakterleri düzgün bir şekilde görüntüleyebiliyor olmanız
lazım. Eğer Windows'ta Türkçe karakterleri hala düzgün görüntüleyemiyorsanız
`encoding` parametresinde 'utf-8' yerine 'cp1254' adlı dil kodlamasını
kullanmayı deneyebilirsiniz::
    
    encoding = "cp1254"

Yukarıdaki örneklerde bir içerik karşılaştırması yapıp, **farklı** öğeleri
ayıkladık. Aynı şekilde **benzer** öğeleri ayıklamak da mümkündür. Bu işlemin
nasıl yapılacağını az çok tahmin ettiğinizi zannediyorum::
    
    d1 = open("isimler1.txt") 
    d1_satırlar = d1.readlines()
    
    d2 = open("isimler1.txt")
    d2_satırlar = d2.readlines()
    
    for i in d2_satırlar:
        if i in d1_satırlar:
            print(i)
            
    d1.close()
    d2.close()

Burada bir öncekinden farklı olarak ``if not i in d2_satırlar`` kodu yerine,
doğal olarak, ``if i in d2_satırlar`` kodunu kullandığımıza dikkat edin.

Dosyalar üzerinde yaptığımız işlemleri tamamladıktan sonra ``close()`` metodu
ile bunları kapatmayı unutmuyoruz::
    
    d1.close()
    d2.close()

Karakter Dizisindeki Karakterleri Sayma
=========================================

Yukarıdaki örneklerde içerik karşılaştırmaya ilişkin birkaç örnek verdik. Şimdi
yine bilgilerimizi pekiştirmek için başka bir konuya ilişkin örnekler verelim. 

Mesela elimizde şöyle bir metin olduğunu varsayalım::
    
    Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
    tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
    isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
    yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
    dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
    The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
    Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
    gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
    figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır.

Yapmamız gereken bir istatistik çalışması gereğince bu metinde her harfin kaç
kez geçtiğini hesaplamanız gerekiyor. 

Bunun için şöyle bir program yazabiliriz::
    
    metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
    tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
    isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
    yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
    adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
    Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
    gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
    da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
    edilmesi neredeyse bir gelenek halini almıştır."""
    
    harf = input("Sorgulamak istediğiniz harf: ")
    
    sayı = ''
    
    for s in metin:
        if harf == s:
            sayı += harf
    
    print(len(sayı))
   
Burada öncelikle metnimizi bir değişken olarak tanımladık. Ardından da
kullanıcıya hangi harfi sorgulamak istediğini sorduk. 

Bu kodlarda tanımladığımız `sayı` adlı değişken, sorgulanan harfi, metinde
geçtiği sayıda içinde barındıracaktır. Yani mesela metin `5` tane `a` harfi
varsa `sayı` değişkeninin değeri `aaaaa` olacaktır.

Sonraki satırlarda ``for`` döngümüzü tanımlıyoruz::
    
    for s in metin:         # metin içinde 's' adını verdiğimiz herbir öğe için
        if harf == s:       # eğer kullanıcıdan gelen harf 's' ile aynıysa
            sayı += harf    # kullanıcıdan gelen bu harfi sayı değişkenine yolla
            
Dediğimiz gibi, `sayı` değişkeni, sorgulanan harfi, metinde geçtiği sayıda
barındırıyor. Dolayısıyla bir harfin metinde kaç kez geçtiğini bulmak için
`sayı` değişkeninin uzunluğunu yazdırmamız yeterli olacaktır::
    
    print(len(sayı))
    
Dilerseniz yukarıdaki programı yazmak için daha farklı bir mantık da
kullanabilirsiniz. Dikkatlice bakın::

    metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
    tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
    isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
    yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
    adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
    Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
    gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
    da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
    edilmesi neredeyse bir gelenek halini almıştır."""
    
    harf = input("Sorgulamak istediğiniz harf: ")
    
    sayı = 0
    
    for s in metin:
        if harf == s:
            sayı += 1
    
    print(sayı)
    
Burada `sayı` değişkeninin ilk değeri `0` olarak belirledik. Döngü içinde de,
sorgulanan harfin metin içinde her geçişinde `sayı` değişkeninin değerini `1`
sayı artırdık. Dolayısıyla sorgulanan harfin metinde kaç kez geçtiğini bulmak
için `sayı` değişkeninin son değerini yazdırmamız yeterli oldu.

Dosya içindeki Karakterleri Sayma
==================================

Dilerseniz bir önceki örnekte kullandığımız metnin program içinde bir değişken
değil de, mesela bir dosyadan okunan bir metin olduğunu varsayalım şimdi::
   
    hakkında = open("hakkında.txt", encoding="utf-8")
    
    harf = input("Sorgulamak istediğiniz harf: ")
    
    sayı = 0
    
    for karakter_dizisi in hakkında:
        for karakter in karakter_dizisi:
            if harf == karakter:
                sayı += 1
    print(sayı)
    
    hakkında.close()
    
Burada yaptığımız ilk iş elbette dosyamızı açmak oldu::
    
    hakkında = open("hakkında.txt", encoding="utf-8")

Bu komutla, `hakkında.txt` adlı dosyayı `UTF-8` kodlaması ile açtık. Daha sonra
kullanıcıya, sorgulamak istediği harfi soruyoruz::
    
    harf = input("Sorgulamak istediğiniz harf: ")

Ardından da sorgulanan harfin dosyada kaç kez geçtiği bilgisini tutacak olan
`sayı` adlı bir değişken tanımlıyoruz::

    sayı = 0

Sıra geldi ``for`` döngümüzü tanımlamaya::  

    for karakter_dizisi in hakkında:
        for karakter in karakter_dizisi:
            if harf == karakter:
                sayı += 1

Bu döngüyü anlamakta bir miktar zorlanmış olabilirsiniz. Her zaman söylediğimiz
gibi, Python'da bir kod parçasını anlamanın en iyi yöntemi, gerekli yerlere
``print()`` fonksiyonları yerleştirerek, programın verdiği çıktıları
incelemektir::
    
    for karakter_dizisi in hakkında:
        print(karakter_dizisi)
        #for karakter in karakter_dizisi:
        #    if harf == karakter:
        #        sayı += 1

Gördüğünüz gibi, ilk ``for`` döngüsünün hemen sonrasına bir ``print()`` fonksiyonu
yerleştirerek bu döngünün verdiği çıktıları inceliyoruz. Bu arada, amacımıza
hizmet etmeyen satırları da yorum içine alarak etkisizleştirdiğimize dikkat
edin.

Çıktıya baktığımız zaman, şöyle bir durumla karşılaşıyoruz::
    
    Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
    
    tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
    
    isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
    
    yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
    
    adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
    
    Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
    
    gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
    
    da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
    
    edilmesi neredeyse bir gelenek halini almıştır.
    
Burada herbir satır ayrı bir karakter dizisidir. Eğer herbir satırın ayrı bir
karakter dizisi olduğunu daha net bir şekilde görmek istiyorsanız ``repr()``
adlı özel bir fonksiyondan yararlanabilirsiniz::
    
    for karakter_dizisi in hakkında:
        print(repr(karakter_dizisi))
        #for karakter in karakter_dizisi:
        #    if harf == karakter:
        #        sayı += 1
   
Bu kodlar bu kez şöyle bir çıktı verir::
  
    'Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı\n'
    'tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,\n'
    'isminin Python olmasına aldanarak, bu programlama dilinin, adını piton\n'
    'yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin\n'
    'adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty\n'
    'Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı\n'
    'gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa\n'
    'da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil\n'
    'edilmesi neredeyse bir gelenek halini almıştır.'
    
Bu çıktıya çok dikkatlice bakın. ``repr()`` fonksiyonu sayesinde Python'ın
alttan alta neler çevirdiğini bariz bir biçimde görüyoruz. Karakter dizisinin
başlangıç ve bitişini gösteren tırnak işaretleri ve `\\n` kaçış dizilerinin
görünür vaziyette olması sayesinde herbir satırın ayrı bir karakter dizisi
olduğunu daha net bir şekilde görebiliyoruz.

Biz yazdığımız kodlarda, kullanıcıdan bir harf girmesini istiyoruz.
Kullandığımız algoritma gereğince bu harfi metindeki karakter dizileri içinde
geçen herbir karakterle tek tek karşılaştırmamız gerekiyor. ``input()`` metodu
aracılığıyla kullanıcıdan tek bir karakter alıyoruz. Kullandığımız ``for`` döngüsü
ise bize bir karakter yerine her satırda bir karakter dizisi veriyor.
Dolayısıyla mesela kullanıcı 'a' harfini sorgulamışsa, ilk ``for`` döngüsü bu
harfin karşısına `'Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı\n'` adlı karakter dizisini çıkaracaktır. Dolayısıyla bizim bir seviye
daha alta inerek, ilk ``for`` döngüsünden elde edilen değişken üzerinde başka bir
``for`` döngüsü daha kurmamız gerekiyor. Bu yüzden şöyle bir kod yazıyoruz::
	
    for karakter_dizisi in hakkında:
        for karakter in karakter_dizisi:
        	...
        	
Böylece iç içe iki ``for`` döngüsü oluşturmuş oluyoruz. İsterseniz bu anlattığımız
şeyleri daha net görmek için yine ``print()`` fonksiyonundan
yararlanabilirsiniz::
	
	hakkında = open("hakkında.txt", encoding="utf-8")
	
	harf = input("Sorgulamak istediğiniz harf: ")
	
	sayı = 0
	
	for karakter_dizisi in hakkında:
	    for karakter in karakter_dizisi:
		print(karakter)
	#        if harf == karakter:
	#            sayı += 1
	#print(sayı)

`karakter` değişkenin değerini ekrana yazdırarak Python'ın alttan alta neler
çevirdiğini daha net görebiliyoruz.

Kodların geri kalanında ise, kullanıcının sorguladığı harfin, ``for`` döngüsü
ile üzerinden geçtiğimiz `karakter_dizisi` adlı değişken içindeki karakterlerle
eşleşip eşleşmediğini denetliyoruz. Eğer eşleşiyorsa, her eşleşmede `sayı`
değişkeninin değerini `1` sayı artırıyoruz. Böylece en elimizde sorgulanan
harfin metin içinde kaç kez geçtiği bilgisi olmuş oluyor.

Son olarak da, ilk başta açtığımız dosyayı kapatıyoruz::
    
    hakkında.close()

Nihayet bir konunun daha sonuna ulaştık. Döngüler ve döngülerle ilişkili
araçları da epey ayrıntılı bir şekilde incelediğimize göre gönül rahatlığıyla
bir sonraki konuya geçebiliriz.

            

    

