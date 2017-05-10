.. meta::
   :description: Bu bölümde fonksiyonlar konusunu inceleyeceğiz. 
   :keywords: python, fonksiyon

.. highlight:: py3

************************
Fonksiyonlar
************************

İlk derslerimizden bu yana bir şey özellikle dikkatinizi çekmiş olmalı: İlk
andan itibaren hep 'fonksiyon' diye bir kavramdan söz ettik; üstelik yazdığımız
kodlarda da bu fonksiyon denen şeyi bolca kullandık. Evet, belki bu kavramı
şimdiye dek enine boyuna inceleme fırsatımız hiç olmadı, ama yine de adının
fonksiyon olduğunu söylediğimiz pek çok araç tanıdık bu noktaya gelinceye kadar.

Herhalde, 'Fonksiyon denince aklınıza ilk ne geliyor?' diye bir soru sorsam,
vereceğiniz cevap ``print()`` fonksiyonu olacaktır. Gerçekten de bu fonksiyonu
ilk derslerimizden bu yana o kadar sık kullandık ki, fonksiyon denince aklınıza
ilk bu fonksiyonun gelmesi gayet doğal.

Elbette öğrendiğimiz tek fonksiyon ``print()`` değildi. Bunun dışında ``type()``
diye bir fonksiyondan da söz etmiştik. ``print()`` kadar olmasa da, ``type()``
fonksiyonunu da yazdığımız kodlarda epey kullandık. ``print()`` ve ``type()``
dışında, fonksiyon olarak ``str()``, ``int()`` ve benzeri araçlarla da tanıştık.
Bunların dışında pek çok başka fonksiyon da Python'la birlikte hayatımıza girdi.

İşte bu bölümde, en baştan bu yana sıklıkla sözünü ettiğimiz, ama hiçbir zaman
tam anlamıyla ele almadığımız bu kavramı daha iyi anlayabilmek için, fonksiyon
konusunu ayrıntılı olarak ele alacağız. Bu bölümde amacımız fonksiyonları enine
boyuna inceleyerek, okurun bilgi dağarcığında fonksiyonlara ilişkin sağlam bir
altyapı oluşturmaktır. Okur, bu bölümü bitirdikten sonra fonksiyonlara ilişkin
olarak bilmesi gereken her şeyi öğrenmiş olacak.

Fonksiyon Nedir ve Ne İşe Yarar?
*********************************

Biz şimdiye dek karşılaştığımız ``print()``, ``len()``, ``type()`` ve ``open()``
gibi örnekler sayesinde 'fonksiyon' denen şeyi az çok tanıdığımızı
söyleyebiliriz. Dolayısıyla fonksiyonun ne demek olduğunu şeklen de olsa
biliyoruz ve hatta fonksiyonları kodlarımız içinde etkili bir şekilde
kullanabiliyoruz.

İlk derslerimizden bu yana öğrendiğimiz fonksiyonlara şöyle bir bakacak olursak,
fonksiyonların görünüşüne ve yapısına dair herhalde şu tespitleri yapabiliriz:

    #. Her fonksiyonun bir adı bulunur ve fonksiyonlar sahip oldukları bu
       adlarla anılır. (``print`` fonksiyonu, ``open`` fonksiyonu, ``type``
       fonksiyonu, ``input`` fonksiyonu, ``len`` fonksiyonu vb.)  
    
    #. Şekil olarak, her fonksiyonun isminin yanında birer parantez işareti
       bulunur. (``open()``, ``print()``, ``input()``, ``len()`` vb.)
    
    #. Bu parantez işaretlerinin içine, fonksiyonlara işlevsellik kazandıran
       bazı parametreler yazılır. (``open(dosya_adı)``, ``print("Merhaba Zalim
       Dünya!")``, ``len("kahramanmaraş")`` vb.)    
       
    #. Fonksiyonlar farklı sayıda parametre alabilir. Örneğin ``print()``
       fonksiyonu toplam `256` adet parametre alabilirken, ``input()`` fonksiyonu
       yalnızca tek bir parametre alır.    
    
    #. Fonksiyonların isimli ve isimsiz parametreleri vardır. ``print()``
       fonksiyonundaki `sep`, `end` ve `file` parametreleri isimli parametrelere
       örnekken, mesela ``print("Merhaba Dünya!")`` kodunda `Merhaba Dünya!`
       parametresi isimsiz bir parametredir. Aynı şekilde ``input("Adınız: ")``
       gibi bir kodda `Adınız:` parametresi isimsiz bir parametredir.
    
    #. Fonksiyonların, isimli ve isimsiz parametreleri dışında, bir de
       varsayılan değerli parametreleri vardır. Örneğin ``print()`` fonksiyonunun
       `sep`, `end` ve `file` parametreleri varsayılan değerli parametrelere birer
       örnektir. Eğer bir parametrenin varsayılan bir değeri varsa, o parametreye
       herhangi bir değer vermeden de fonksiyonu kullanabiliriz. Python bu
       parametrelere, belirli değerleri öntanımlı olarak kendisi atayacaktır. Tabii
       eğer istersek, varsayılan değerli parametrelere kendimiz de başka birtakım
       değerler verebiliriz.
    
Fonksiyon kavramının tam olarak ne olduğunu henüz bilmiyor da olsak, şimdiye
kadar öğrendiğimiz fonksiyonlara bakarak fonksiyonlar hakkında yukarıdaki
çıkarımları yapabiliyoruz. Demek ki aslında fonksiyonlar hakkında alttan alta
pek çok şey öğrenmişiz. O halde, fonksiyonlar hakkında şimdiden bildiklerimize
güvenerek, fonksiyon kavramının ne olduğundan ziyade ne işe yaradığı konusuna
rahatlıkla eğilebiliriz. Zaten fonksiyonların ne işe yaradığını öğrendikten
sonra, fonksiyonların ne olduğunu da hemencecik anlayacaksınız.

Fonksiyonların ne işe yaradığını en genel ve en kaba haliyle tarif etmek
istersek şöyle bir tanımlama yapabiliriz:

    **Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu
    işlemleri tek adımda yapmamızı sağlamaktır. Fonksiyonlar çoğu zaman, yapmak
    istediğimiz işlemler için bir şablon vazifesi görür. Fonksiyonları
    kullanarak, bir veya birkaç adımdan oluşan işlemleri tek bir isim altında
    toplayabiliriz. Python'daki 'fonksiyon' kavramı başka programlama dillerinde
    'rutin' veya 'prosedür' olarak adlandırılır. Gerçekten de fonksiyonlar
    rutin olarak tekrar edilen görevleri veya prosedürleri tek bir ad/çatı
    altında toplayan araçlardır.** 
    
Dilerseniz yukarıdaki soyut ifadeleri basit bir örnek üzerinde somutlaştırmaya
çalışalım. Örneğin ``print()`` fonksiyonunu ele alalım.

Bu fonksiyonun görevini biliyorsunuz: ``print()`` fonksiyonunun görevi,
kullanıcının girdiği parametreleri ekrana çıktı olarak vermektir. Her ne kadar
``print()`` fonksiyonunun görevini, ekrana çıktı vermek olarak tanımlasak da,
aslında bu fonksiyon, ekrana çıktı vermenin yanısıra, başka bir takım ilave
işlemler de yapar. Yani bu fonksiyon, aslında aldığı parametreleri sadece ekrana
çıktı olarak vermekle yetinmez. Örneğin şu komutu inceleyelim::
    
    >>> print("Fırat", "Özgül", "1980", "Adana")

Burada ``print()`` fonksiyonu toplam dört adet parametre alıyor. Fonksiyonumuz,
görevi gereği, bu parametreleri ekrana çıktı olarak verecek. Bu komutu
çalıştırdığımızda şöyle bir çıktı alıyoruz::
    
    Fırat Özgül 1980 Adana

Dikkat ederseniz, burada salt bir 'ekrana çıktı verme' işleminden fazlası var.
Zira ``print()`` fonksiyonu aldığı parametreleri şu şekilde de ekrana
verebilirdi::
    
    FıratÖzgül1980Adana
    
Veya şu şekilde::

    F
    ı
    r
    a
    t
    Ö
    z
    g
    ü
    l
    1
    9
    8
    0
    A
    d
    a
    n
    a

Neticede bunlar da birer çıktı verme işlemidir. Ama dediğimiz gibi, ``print()``
fonksiyonu aldığı parametreleri sadece ekrana çıktı olarak vermekle yetinmiyor.
Gelin isterseniz ne demek istediğimizi biraz daha açıklayalım:

``print()`` fonksiyonunun yukarıdaki komutu nasıl algıladığını önceki
derslerimizde öğrenmiştik. Yukarıdaki komut Python tarafından şu şekilde
algılanıyor::
    
    >>> print("Fırat", "Özgül", "1980", "Adana", sep=" ", end="\n", 
    ... file=sys.stdout, flush=False)
    
Yani ``print()`` fonksiyonu; 

#. Kendisine verilen `"Fırat"`, `"Özgül"`, `"1980"` ve `"Adana"`
   parametrelerini ekrana basıyor,

#. `sep=" "` parametresinin etkisiyle, bu parametreler arasına birer boşluk
   ekliyor,

#. `end="\\n"` parametresinin etkisiyle, sonuncu parametreyi de ekrana
   bastıktan sonra bir alt satıra geçiyor,

#. `file=sys.stdout` parametresinin etkisiyle, çıktı konumu olarak komut
   ekranını kullanıyor. Yani çıktıları ekrana veriyor.  

#. `flush=False` parametresinin etkisiyle, çıktılar ekrana gönderilmeden önce
   tamponda bekletiliyor.
    
Eğer ``print()`` gibi bir fonksiyon olmasaydı, yukarıda listediğimiz bütün bu
işlemleri kendimiz yapmak zorunda kalacaktık. Yani ekranda göstermek istediğimiz
ifadeleri ekrana çıktı olarak vermenin yanısıra, bunların ekranda nasıl
görüneceğini de tek tek kendimiz elle ayarlamak zorunda kalacaktır. Ekrana çıktı
verme ile ilgili pek çok işlem tek bir ``print()`` fonksiyonu altında
birleştirildiği için, her ihtiyaç duyduğumuzda o işlemleri tek tek bizim
yapmamıza gerek kalmıyor.

Aynı şey mesela ``input()`` fonksiyonu için de geçerlidir. Bu fonksiyonu
kullanarak, programımızı kullanan kişilerle etkileşim içine girebiliyoruz. Tıpkı
``print()`` fonksiyonunda olduğu gibi, ``input()`` fonksiyonu da aslında alttan
alta epey karmaşık işlemler gerçekleştirir. Ama o karmaşık işlemlerin tek bir
``input()`` fonksiyonu içinde bir araya getirilmiş olması sayesinde, sadece
``input()`` gibi basit bir komut vererek kullanıcılarımızla iletişime
geçebiliyoruz.

Bu açıdan bakıldığında fonksiyonlar değişkenlere benzer. Bildiğiniz gibi, her
defasında bir değeri tekrar tekrar yazmak yerine bir değişkene atayarak o değere
kolayca erişebiliyoruz. Örneğin::
    
    >>> kurum = "Sosyal Sigortalar Kurumu"

Burada tanımladığımız `kurum` adlı değişken sayesinde, 'Sosyal Sigortalar
Kurumu' ifadesini kullanmamız gereken her yerde sadece değişken adını
kullanarak, değişkenin tuttuğu değere ulaşabiliyoruz. İşte fonksiyonlar da buna
benzer bir işlev görür: Örneğin ekrana bir çıktı vermemiz gereken her yerde,
yukarıda verdiğimiz karmaşık adımları tek tek gerçekleştirmeye çalışmak yerine,
bu karmaşık ve rutin adımları bir araya getiren ``print()`` gibi bir
fonksiyondan yararlanarak işlerimizi çok daha kolay bir şekilde halledebiliriz.

Bu anlattıklarımız fonksiyonların ne işe yaradığı konusunda size bir fikir
vermiş olabilir. Dilerseniz bu anlattıklarımızı bir örnek aracılığıyla biraz
daha somutlaştırmaya çalışalım:

Hatırlarsanız 'Kullanıcıyla Veri Alışverişi' başlıklı bölümde şöyle bir örnek
vermiştik::
    
    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu"
    şehir   = "İstanbul"

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

Bu programı çalıştırdığımızda şöyle bir çıktı alıyoruz::

    isim           :  Fırat
    soyisim        :  Özgül
    işletim sistemi:  Ubuntu
    şehir          :  İstanbul

Bu program, belli değerleri kullanarak bir kayıt oluşturma işlemi
gerçekleştiriyor. Mesela yukarıdaki örnekte, 'Fırat Özgül' adlı şahsa ait isim,
soyisim, işletim sistemi ve şehir bilgilerini alarak, bu kişi için bir kayıt
oluşturuyoruz.

Peki 'Fırat Özgül' adlı kişinin yanısıra, 'Mehmet Öztaban' adlı başka bir kişi
için de kayıt oluşturmak istersek ne yapacağız?

Aklınıza şöyle bir şey yazmak gelmiş olabilir::

    isim1    = "Fırat"
    soyisim1 = "Özgül"
    işsis1   = "Ubuntu"
    şehir1   = "İstanbul"

    print("isim           : ", isim1)
    print("soyisim        : ", soyisim1)
    print("işletim sistemi: ", işsis1)
    print("şehir          : ", şehir1)

    print("-"*30)

    isim2    = "Mehmet"
    soyisim2 = "Öztaban"
    işsis2   = "Debian"
    şehir2   = "Ankara"

    print("isim           : ", isim2)
    print("soyisim        : ", soyisim2)
    print("işletim sistemi: ", işsis2)
    print("şehir          : ", şehir2)

    print("-"*30)

Programa her yeni kayıt eklenişinde, her yeni kişi için benzer satırları tekrar
tekrar yazabilirsiniz. Peki ama bu yöntem sizce de çok sıkıcı değil mi? Üstelik
bir o kadar da hataya açık bir yöntem. Muhtemelen ilk kaydı ekledikten sonra,
ikinci kaydı eklerken birinci kayıttaki bilgileri kopyalayıp, bu kopya üzerinden
ikinci kaydı oluşturuyorsunuz. Hatta muhtemelen kopyalayıp yapıştırdıktan sonra
yeni kaydı düzenlerken bazı hatalar da yapıyor ve düzgün çalışan bir program
elde edebilmek için o hataları düzeltmekle de uğraşıyorsunuz.

Bütün bu işleri kolaylaştıracak bir çözüm olsa ve bizi aynı şeyleri tekrar
tekrar yazmaktan kurtarsa sizce de çok güzel olmaz mıydı? Mesela tıpkı
``print()`` fonksiyonu gibi, ``kayıt_oluştur()`` adlı bir fonksiyon olsa, biz
sadece gerekli bilgileri bu fonksiyonun parantezleri içine parametre olarak
yazsak ve bu fonksiyon bize istediğimiz bilgileri içeren bir kayıt oluştursa ne
hoş olurdu, değil mi? Yani örneğin bahsettiğimiz bu hayali ``kayıt_oluştur()``
fonksiyonunu şu şekilde kullanabilseydik...

::

    kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")

... ve bu komut bize şu çıktıyı verebilseydi...

::
    
    ------------------------------
    isim           :  Mehmet
    soyisim        :  Öztaban
    işletim sistemi:  Debian
    şehir          :  Ankara
    ------------------------------

... ne kadar güzel olurdu, değil mi?

İşte böyle bir şey Python'da mümkündür. Nasıl Python geliştiricileri
``print()``, ``input()`` ve benzeri fonksiyonları tanımlayıp, karmaşık işlemleri
tek adımda yapabilmemiz için bize sunmuş ve böylece bizi her defasında tekerleği
yeniden icat etme külfetinden kurtarmışsa, biz de kendi fonksiyonlarımızı
tanımlayarak, kendimizi aynı işlemleri tekrar tekrar yapma zahmetinden
kurtarabiliriz.

Gelin şimdi bu işi nasıl yapabileceğimizi tartışalım.

Fonksiyon Tanımlamak ve Çağırmak
*********************************

Bir önceki bölümde, ``kayıt_oluştur()`` adlı hayali bir fonksiyondan söz
etmiştik. Tasarımıza göre bu fonksiyon şu şekilde kullanılacak::
    
    kayıt_oluştur("Ahmet", "Gür", "Pardus", "İzmir")

Bu komutu verdiğimizde ise şöyle bir çıktı almayı planlıyoruz::

    ------------------------------
    isim           :  Ahmet
    soyisim        :  Gür
    işletim sistemi:  Pardus
    şehir          :  İzmir
    ------------------------------

Dediğimiz gibi, böyle bir şey yapmak Python'la mümkündür. Ancak tabii ki
``kayıt_oluştur()`` adlı böyle bir fonksiyonu kullanabilmenin belli ön koşulları
var. Nasıl `sayı` adlı bir değişkeni kullanabilmek için öncelikle bu ada sahip
bir değişken tanımlamış olmamız gerekiyorsa, aynı şekilde ``kayıt_oluştur()``
adlı bir fonksiyonu kullanabilmek için de öncelikle bu ada sahip bir fonksiyonu
tanımlamış olmamız gerekiyor. Zira mesela ``input()`` ve ``print()`` gibi
fonksiyonları kullanabiliyor olmamız, Python geliştiricilerinin bu fonksiyonları
tanımlayıp dilin içine gömmüş olmaları sayesindedir.

İşte biz de ``kayıt_oluştur()`` adlı fonksiyonu kullanabilmek için bu ada sahip
fonksiyonu aşağıdaki şekilde tanımlamalıyız::

    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)

İlk bakışta bu kodlar size hiçbir şey ifade etmemiş olabilir. Ama hiç endişe
etmeyin. Biz birazdan bu satırların ne anlama geldiğini bütün ayrıntılarıyla
anlatacağız. Siz şimdilik anlamadığınız kısımları görmezden gelip okumaya devam
edin.

Yukarıdaki kodlar yardımıyla fonksiyonumuzu tanımlamış olduk. Artık elimizde,
tıpkı ``print()`` veya ``input()`` gibi, ``kayıt_oluştur()`` adlı 'ev yapımı'
bir fonksiyon var. Dolayısıyla bu yeni fonksiyonumuzu, daha önce öğrendiğimiz
fonksiyonları nasıl kullanıyorsak aynı şekilde kullanabiliriz. Yani aşağıdaki
gibi komutlar yazabiliriz::
    
    kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
    kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")

Yalnız fonksiyonumuzu tanımlayıp bitirdikten sonra, bu fonksiyonu kullanırken,
kodlarımızın hizalamasına dikkat ediyoruz. Fonksiyonu kullanmak için yazdığımız
kodları `def` ifadesinin hizasına getiriyoruz. Yani::
    
    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)

    kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
    kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")

Yukarıdaki yapıyı kullanarak, istediğiniz sayıda kayıt oluşturabilirsiniz. Mesela::

    kayıt_oluştur("İlkay", "Kaya", "Mint", "Adana")
    kayıt_oluştur("Seda", "Kara", "SuSe", "Erzurum")

Gördüğünüz gibi, yukarıdaki yöntem sayesinde kodlarımızdaki tekrar eden kısımlar
ortadan kalktı. Yukarıdaki fonksiyonun bize nasıl bir kolaylık sağladığını daha
net görebilmek için, fonksiyon kullanarak sadece şu `11` satırla elde ettiğimiz
çıktıyı, fonksiyon kullanmadan elde etmeyi deneyebilirsiniz::
    
    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)

    kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
    kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")
    kayıt_oluştur("İlkay", "Kaya", "Mint", "Adana")
    kayıt_oluştur("Seda", "Kara", "SuSe", "Erzurum")

Bu anlattıklarımız size çok karmaşık gelmiş olabilir. Ama endişe etmenize hiç
gerek yok. Biraz sonra, yukarıda yazdığımız kodların hepsini didik didik
edeceğiz. Ama öncelikle yukarıdaki kod parçasını yapısal olarak bir incelemenizi
istiyorum. Fonksiyonu tanımladığımız aşağıdaki kod parçasına şöyle bir
baktığınızda neler görüyorsunuz?

::

   def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)
    
   kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")

Bu kodları incelediğinizde şu noktalar dikkatinizi çekiyor olmalı: 

#. Kodlar `def` adlı bir ifade ile başlamış. 

#. Bunun ardından 'kayıt_oluştur' ifadesini görüyoruz. 

#. Bu ifadeyi, içinde birtakım kelimeler barındıran bir parantez çifti izliyor. 

#. Parantezin içinde, `isim`, `soyisim`, `işsis` ve `şehir` adlı değerler var. 

#. `def` ile başlayan bu satır iki nokta üst üste işareti ile son buluyor.

#. İlk satırın ardından gelen kısım ilk satıra göre girintili bir şekilde yazılmış.

#. ``kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")`` satırı önceki
   satırlara göre girintisiz yazılmış.
    
Eğer bu kodlara dikkatlice bakacak olursanız, aslında bu kodların topu topu iki
parçadan oluştuğunu göreceksiniz. İsterseniz yukarıdaki yapıyı biraz
sadeleştirelim::
    
    def kayıt_oluştur(parametre1, parametre2, parametre3, parametre4):
        (...)
    
    kayıt_oluştur(parametre1, parametre2, parametre3, parametre4)

Bu yapının ilk parçası şudur::

    def kayıt_oluştur(parametre1, parametre2, parametre3, parametre4):
        (...)
    
İkinci parçası ise şu::

    kayıt_oluştur(parametre1, parametre2, parametre3, parametre4)

Teknik olarak söylemek gerekirse, ilk parçaya 'fonksiyon tanımı' (*function
definition*), ikinci parçaya ise 'fonksiyon çağrısı' (*function call*) adı
verilir. Dolayısıyla bir fonksiyonun yaşam döngüsü iki aşamadan oluşur. Buna
göre bir fonksiyon önce tanımlanır;

::

    def kayıt_oluştur(parametre1, parametre2, parametre3, parametre4):
        (...)

...sonra da çağrılır;

::

    kayıt_oluştur(parametre1, parametre2, parametre3, parametre4)

Aslında biz şimdiye kadar gördüğümüz ``print()``, ``type()``, ``open()`` vb.
fonksiyonlarda bu 'fonksiyon çağrısı' kısmıyla zaten tanışmıştık. Zira şu komut
tam anlamıyla bir fonksiyon çağrısıdır (yani bir fonksiyon çağırma işlemidir)::
    
    print("Fırat", "Özgül", "Adana", 32)

Gördüğünüz gibi, yukarıdaki komutun yapı olarak şu komuttan hiçbir farkı yok::

    kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
    
Bu iki fonksiyon arasındaki tek fark, ``print()`` fonksiyonunu Python
geliştiricilerinin; ``kayıt_oluştur()`` fonksiyonunu ise sizin tanımlamış
olmanızdır.

Elbette bu iki fonksiyon yapı olarak birbirinin aynı olsa da, işlev olarak
birbirinden farklıdır. ``print()`` fonksiyonunun görevi kendisine parametre
olarak verilen değerleri ekrana çıktı vermek iken, ``kayıt_oluştur()``
fonksiyonunun görevi kendisine parametre olarak verilen değerleri kullanarak bir
kayıt oluşturmaktır.

Bu derse gelinceye kadar öğrendiğimiz ``print()``, ``type()`` ve ``open()`` gibi
fonksiyonlara teknik olarak 'gömülü fonksiyonlar' (*builtin functions*) adı
verilir. Bu fonksiyonlara bu adın verilmiş olmasının sebebi, bu fonksiyonların
gerçekten de Python programlama dili içine gömülü bir vaziyette olmalarıdır.
Dikkat ederseniz kendi yazdığımız fonksiyonları kullanabilmek için öncelikle
fonksiyonu tanımlamamız gerekiyor. Gömülü fonksiyonlar ise Python
geliştiricileri tarafından halihazırda tanımlanmış olduğu için bunları biz
herhangi bir tanımlama işlemi yapmaya gerek kalmadan doğrudan çağırabiliyoruz.

Böylece bir fonksiyonun yapı olarak neye benzediğini üstünkörü de olsa incelemiş
olduk. Buraya kadar anlatılan kısımda bazı noktaları anlamakta zorlanmış
olabilirsiniz. Eğer öyleyse hiç endişelenmeyin. Bu gayet doğal.

Gelin isterseniz şimdi yukarıda anlattıklarımızın içini doldurmaya çalışalım.

Fonksiyonların Yapısı
***********************

İsterseniz biraz da fonksiyonların yapısından söz edelim. Böylelikle ne ile
karşı karşıya olduğumuzu anlamak zihninizde biraz daha kolaylaşır.

Dedik ki, bir fonksiyonun ilk parçasına 'fonksiyon tanımı' (*function
definition*) adı verilir. Bir fonksiyonu tanımlamak için `def` adlı bir
parçacıktan yararlanıyoruz. Örneğin::
    
    def bir_fonksiyon():
        (...)

Burada `def` parçacığı, tanımladığımız şeyin bir fonksiyon olduğunu gösteriyor.
`bir_fonksiyon` ifadesi ise tanımladığımız bu fonksiyonun adıdır. Fonksiyonu
tanımladıktan sonra, çağırırken bu adı kullanacağız.

``def bir_fonksiyon():`` ifadesinin sonundaki iki nokta işaretinden de tahmin
edebileceğiniz gibi, sonraki satıra yazacağımız kodlar girintili olacak. Yani
mesela::
    
    def selamla():
        print("Elveda Zalim Dünya!")
        
Yukarıda ``selamla()`` adlı bir fonksiyon tanımlamış olduk. Bu fonksiyonun
görevi ekrana `Elveda Zalim Dünya!` çıktısı vermektir.
        
Bu noktada şöyle bir soru akla geliyor: Acaba fonksiyon gövdesindeki kısım için
ne kadarlık bir girinti oluşturacağız?

Girintilemeye ilişkin olarak önceki derslerde bahsettiğimiz bütün kurallar
burada da geçerlidir. Fonksiyon gövdesine, `def` ifadesinden itibaren `4` (dört)
boşlukluk bir girinti veriyoruz. `def` ifadesinden itibaren girintili olarak
yazdığımız kısmın tamamı o fonksiyonun gövdesini oluşturur ve bütünüyle o
fonksiyona aittir. 

Bu kodlarla yaptığımız şey bir fonksiyon tanımlama işlemidir. Eğer bu kodları
bir dosyaya kaydedip çalıştırırsak herhangi bir çıktı almayız. Çünkü henüz
fonksiyonumuzu çağırmadık. Bu durumu ``print()``, ``input()`` ve benzeri gömülü
fonksiyonlara benzetebilirsiniz. Tıpkı yukarıda bizim yaptığımız gibi, gömülü
fonksiyonlar da Python geliştiricileri tarafından bir yerlerde tanımlanmış
vaziyette dururlar, ama biz bu fonksiyonları yazdığımız programlarda çağırana
kadar bu fonksiyonlar çalışmaz.

Daha önce de dediğimiz gibi, bir fonksiyonun yaşam döngüsü iki aşamadan oluşur:
Fonksiyon tanımı ve fonksiyon çağrısı. Yukarıda bu döngünün sadece fonksiyon
tanımı aşaması mevcut. Unutmayın, bir fonksiyon çağrılmadan asla çalışmaz. Bir
fonksiyonun çalışabilmesi için o fonksiyonun tanımlandıktan sonra çağrılması
gerekir. Örneğin ``input()`` fonksiyonu Python'ın derinliklerinde bir yerlerde
tanımlanmış vaziyette durur. Bu fonksiyon, biz onu çağırana kadar, bulunduğu
yerde sessizce bekler. Aynı şekilde ``selamla()`` adlı fonksiyon da programımız
içinde tanımlanmış vaziyette, bizim onu çağıracağımız anı bekliyor. Bu
söylediklerimizi destekleyecek açıklayıcı bilgileri biraz sonra vereceğiz. Biz
şimdilik fonksiyon tanımı kısmını incelemeye devam edelim.

Bu arada yukarıdaki fonksiyon tanımının yapısına çok dikkat edin. İki nokta üst
üste işaretinden sonraki satırda girintili olarak yazılan bütün kodlar (yani
fonksiyonun gövde kısmı) fonksiyonun bir parçasıdır. Girintinin dışına çıkıldığı
anda fonksiyon tanımlama işlemi de sona erer.

Örneğin::

    def selamla():
        print("Elveda Zalim Dünya!")

    selamla()

İşte burada fonksiyonumuzu çağırmış olduk. Dikkat edin! Dediğim gibi, iki nokta
üst üste işaretinden sonraki satırda girintili olarak yazılan bütün kodlar
fonksiyona aittir. ``selamla()`` satırı ise fonksiyon tanımının dışında yer
alır. Bu satırla birlikte girintinin dışına çıkıldığı için artık fonksiyon
tanımlama safhası sona ermiş oldu.

Biz yukarıdaki örnekte, ``selamla()`` adlı fonksiyonu tanımlar tanımlamaz
çağırmayı tercih ettik. Ama elbette siz bir fonksiyonu tanımlar tanımlamaz
çağırmak zorunda değilsiniz. Yazdığınız bir program içinde fonksiyonlarınızı
tanımladıktan sonra, ihtiyacınıza bağlı olarak, programın herhangi başka bir
yerinde fonksiyonlarınızı çağırabilirsiniz.

Fonksiyonlarla ilgili söylediklerimizi toparlayacak olursak şöyle bir bilgi
listesi ortaya çıkarabiliriz:

#. Python'da kabaca iki tip fonksiyon bulunur. Bunlardan biri gömülü
   fonksiyonlar (*builtin functions*), öteki ise özel fonksiyonlardır (*custom
   functions*). Burada 'özel' ifadesi, 'kullanıcının ihtiyaçlarına göre
   kullanıcı tarafından özel olarak üretilmiş' anlamına gelir.

#. Gömülü fonksiyonlar; Python geliştiricileri tarafından tanımlanıp dilin
   içine gömülmüş olan ``print()``, ``open()``, ``type()``, ``str()``,
   ``int()`` vb. fonksiyonlardır. Bu fonksiyonlar halihazırda tanımlanıp
   hizmetimize sunulduğu için bunları biz herhangi bir tanımlama işlemi
   yapmadan doğrudan kullanabiliriz.

#. Özel fonksiyonlar ise, gömülü fonksiyonların aksine, Python
   geliştiricileri tarafından değil, bizim tarafımızdan tanımlanmıştır. Bu
   fonksiyonlar dilin bir parçası olmadığından, bu fonksiyonları kullanabilmek
   için bunları öncelikle tanımlamamız gerekir.

#. Python'da bir fonksiyonun yaşam döngüsü iki aşamadan oluşur: Tanımlanma
   ve çağrılma.

#. Bir fonksiyonun çağrılabilmesi (yani kullanılabilmesi) için mutlaka
   birisi tarafından tanımlanmış olması gerekir.

#. Fonksiyonu tanımlayan kişi Python geliştiricileri olabileceği gibi, siz
   de olabilirsiniz. Ama neticede ortada bir fonksiyon varsa, bir yerlerde o
   fonksiyonun tanımı da vardır.

#. Fonksiyon tanımlamak için `def` adlı bir ifadeden yararlanıyoruz. Bu
   ifadeden sonra, tanımlayacağımız fonksiyonun adını belirleyip iki nokta üst
   üste işareti koyuyoruz. İki nokta üst üste işaretinden sonra gelen satırlar
   girintili olarak yazılıyor. Daha önce öğrendiğimiz bütün girintileme
   kuralları burada da geçerlidir.

#. Fonksiyonun adını belirleyip iki nokta üst üste koyduktan sonra, alt
   satırda girintili olarak yazdığımız bütün kodlar fonksiyonun gövdesini
   oluşturur. Doğal olarak, bir fonksiyonun gövdesindeki bütün kodlar o
   fonksiyona aittir. Girintinin dışına çıkıldığı anda fonksiyon tanımı da sona
   erer.
    
Fonksiyonlarla ilgili öğrendiklerimizi toparladığımıza göre, gelin isterseniz
fonksiyonlarla ilgili bir örnek yaparak, bu yapıyı daha iyi anlamaya çalışalım::
    
    def sistem_bilgisi_göster():
        import sys
        print("\nSistemde kurulu Python'ın;")
        print("\tana sürüm numarası:", sys.version_info.major)
        print("\talt sürüm numarası:", sys.version_info.minor)
        print("\tminik sürüm numarası:", sys.version_info.micro)
        
        print("\nKullanılan işletim sisteminin;")
        print("\tadı:", sys.platform)

Burada ``sistem_bilgisi_göster()`` adlı bir fonksiyon tanımladık. Bu fonksiyonun
görevi, kullanıcının sistemindeki Python sürümü ve işletim sistemine dair
birtakım bilgiler vermektir.

Bu arada, bu kodlarda, daha önceki derslerimizde öğrendiğimiz `sys` modülünden
ve bu modül içindeki değişkenlerden yararlandığımızı görüyorsunuz. Bu kodlarda
`sys` modülünün içindeki şu araçları kullandık:

#. `version_info.major`: Python'ın ana sürüm numarası (Örn. 3)
#. `version_info.minor`: Python'ın alt sürüm numarası (Örn. 4)
#. `version_info.micro`: Python'ın minik sürüm numarası (Örn. 0)
#. `platform`: Kullanılan işletim sisteminin adı (Örn. 'win32' veya 'linux2')

Yukarıda tanımladığımız fonksiyonu nasıl çağıracağımızı biliyorsunuz::
    
    sistem_bilgisi_göster()
    
Bu fonksiyon tanımı ve çağrısını eksiksiz bir program içinde gösterelim::
    
    def sistem_bilgisi_göster():
        import sys
        print("\nSistemde kurulu Python'ın;")
        print("\tana sürüm numarası:", sys.version_info.major)
        print("\talt sürüm numarası:", sys.version_info.minor)
        print("\tminik sürüm numarası:", sys.version_info.micro)
        
        print("\nKullanılan işletim sisteminin;")
        print("\tadı:", sys.platform)  
        
    sistem_bilgisi_göster()
    
Bu kodları bir dosyaya kaydedip çalıştırdığımızda şuna benzer bir çıktı
alacağız::
    
    Sistemde kurulu Python'ın;
            ana sürüm numarası: 3
            alt sürüm numarası: 3
            minik sürüm numarası: 0
    
    Kullanılan işletim sisteminin;
            adı: linux
            
Demek ki bu kodların çalıştırıldığı sistem Python'ın 3.3.0 sürümünün kurulu
olduğu bir GNU/Linux işletim sistemi imiş...

Fonksiyonlar Ne İşe Yarar?
****************************

Şimdiye kadar söylediklerimizden ve verdiğimiz örneklerden fonksiyonların ne işe
yaradığını anlamış olmalısınız. Ama biz yine de fonksiyonların faydası üzerine
birkaç söz daha söyleyelim. Böylece fonksiyonların ne işe yaradığı konusunda
aklımızda hiçbir şüphe kalmaz...

İsterseniz bir örnek üzerinden ilerleyelim.

Diyelim ki, bir sayının karesini bulan bir program yazmak istiyoruz. Şimdiye
kadarki bilgilerimizi kullanarak şöyle bir şey yazabiliriz::

    sayı = 12
    çıktı = "{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı, sayı**2))

Yukarıdaki programı çalıştırdığımızda şöyle bir çıktı elde edeceğiz::
    
    12 sayısının karesi 144 sayısıdır

Gayet güzel. Şimdi şöyle bir durum hayal edin: Diyelim ki büyük bir program
içinde, farklı farklı yerlerde yukarıdaki işlemi tekrar tekrar yapmak
istiyorsunuz. Böyle bir durumda şöyle bir şey yazmanız gerekebilir::
    
    sayı = 12
    çıktı = "{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı, sayı**2))
    
    ####programla ilgili başka kodlar###
    
    sayı = 15
    print(çıktı.format(sayı, sayı**2))
    
    ###programla ilgili başka kodlar###
    
    sayı = 29
    print(çıktı.format(sayı, sayı**2))

Buradaki sorun, aynı şeyleri tekrar tekrar yazmak zorunda kalmamızdır. Bu küçük
örnekte pek belli olmuyor olabilir, ama özellikle büyük programlarda aynı
kodların program içinde sürekli olarak tekrarlanması pek çok probleme yol açar.
Örneğin kodlarda bir değişiklik yapmak istediğinizde, tekrarlanan kısımları
bulup hepsinin üzerinde tek tek değişiklik yapmanız gerekir. Mesela `çıktı` adlı
değişkenin içeriğini değiştirmek isterseniz, yaptığınız değişiklik programınızın
pek çok kısmını etkileyebilir. Örneğin, `çıktı` değişkenini şu şekle
getirdiğinizi düşünün::
    
    çıktı = "{} sayısının karesi {}, karekökü {} sayısıdır"

Böyle bir durumda, program içinde geçen bütün ``print(çıktı.format(sayı,
sayı**2))`` satırlarını bulup, üçüncü `{}` işaretine ait işlemi parantez içine
eklemeniz gerekir. Tahmin edebileceğiniz gibi, son derece sıkıcı, yorucu ve
üstelik hata yapmaya açık bir işlemdir bu. İşte bu tür problemlere karşı
fonksiyonlar çok iyi bir çözümdür.

Yukarıda bahsettiğimiz kare bulma işlemi için şu şekilde basit bir fonksiyon
tanımlayabiliriz::
    
    def kare_bul():
        sayı = 12
        çıktı = "{} sayısının karesi {} sayısıdır"
        print(çıktı.format(sayı, sayı**2))

Bu fonksiyonu tanımladık. Şimdi de fonksiyonumuzu çağıralım::

    kare_bul()

Kodlarımız tam olarak şöyle görünüyor::

    def kare_bul():
        sayı = 12
        çıktı = "{} sayısının karesi {} sayısıdır"
        print(çıktı.format(sayı, sayı**2))

    kare_bul()

Burada fonksiyonumuz ``def kare_bul():`` satırıyla başlıyor,
``print(çıktı.format(sayı, sayı**2))`` satırıyla bitiyor. Daha sonra gelen
``kare_bul()`` kodu, girintinin dışında yer aldığı için fonksiyon tanımına ait
değildir.

Bu kodları bir dosyaya kaydedip çalıştırdığımızda alacağımız çıktı şu
olacaktır::
    
    12 sayısının karesi 144 sayısıdır

``kare_bul()`` adlı fonksiyonu bir kez tanımladıktan sonra bu fonksiyonu
programınız içinde gereken her yerde çağırabilirsiniz::
    
    kare_bul()
    
    ####programla ilgili başka kodlar###
    
    kare_bul()
    
    ###programla ilgili başka kodlar###
    
    kare_bul()

Gördüğünüz gibi ``kare_bul()`` adlı bu fonksiyon bizi pek çok zahmetten
kurtarıyor. Ancak bu fonksiyonun bir sorunu var. Bu fonksiyon ekrana yalnızca
`12 sayısının karesi 144 sayısıdır` çıktısı verebiliyor. Buradaki problem,
fonksiyonun sadece `12` sayısı üzerinde işlem yapabilmesi. Şöyle bir düşününce,
bu çıktının ne kadar anlamsız olduğunu, aslında yukarıdaki fonksiyonun tamamen
gereksiz bir iş yaptığını rahatlıkla görebiliyoruz. Fonksiyonumuzun adı
``kare_bul``. Ama dediğimiz gibi, fonksiyonumuz sadece `12` sayısının karesini
söyleyebiliyor. Halbuki mantık olarak fonksiyonumuzun, bütün sayıların karesini
söyleyebilmesini beklerdik.

.. note:: Bu arada, gördüğünüz gibi, yukarıdaki fonksiyon parametresiz bir
    fonksiyondur. Dolayısıyla bu fonksiyonu çağırırken parantez içinde herhangi bir
    değer belirtmiyoruz.

Fonksiyonumuzun gerçek anlamda işlevli bir hale gelebilmesi için sadece tek bir
sayıyı değil, bütün sayıları inceleyebiliyor olması gerek. İşte fonksiyonumuza
bu yeteneği parametreler aracılığıyla kazandırabiliriz.

Dikkatlice bakın::

    def kare_bul(sayı):
        çıktı = "{} sayısının karesi {} sayısıdır"
        print(çıktı.format(sayı, sayı**2))
    
Fonksiyona parametre olarak nasıl bir isim verdiğinizin önemi yoktur. Parantez
içine parametre olarak istediğiniz kelimeyi yazabilirsiniz. Önemli olan,
parantez içinde fonksiyonun kaç parametre alacağını gösteren bir işaret
olmasıdır. Mesela yukarıdaki fonksiyonu şöyle de tanımlayabilirdik::
    
    def kare_bul(i):
        çıktı = "{} sayısının karesi {} sayısıdır"
        print(çıktı.format(i, i**2))

...veya şöyle::

    def kare_bul(osman):
        çıktı = "{} sayısının karesi {} sayısıdır"
        print(çıktı.format(osman, osman**2))

Elbette parametre adı olarak akılda kalıcı ve daha mantıklı bir seçim yapmak
işlerinizi kolaylaştıracaktır...

Şimdi de yukarıdaki fonksiyonu çağıralım::

    kare_bul(9)

Bu fonksiyonu çalıştırdığımızda şu çıktıyı alırız::

    9 sayısının karesi 81 sayısıdır

Bu fonksiyona parametre olarak hangi sayıyı verirseniz o sayının karesi
hesaplanacaktır. Örneğin::

    kare_bul(15)
    kare_bul(25555)

Yine bu fonksiyonu programınız içinde gereken her yerde çağırabilirsiniz::

    kare_bul(17)
    
    ####programla ilgili başka kodlar###
    
    kare_bul(21)
    
    ###programla ilgili başka kodlar###
    
    kare_bul(54354)

Fonksiyonu oluşturan kodlarda herhangi bir değişiklik yapmak istediğinizde
sadece fonksiyon tanımının gövdesini değiştirmeniz yeterli olacaktır. Örneğin::
    
    def kare_bul(sayı):
        çıktı = "{} sayısının karesi {}, karekökü ise {} sayısıdır"
        print(çıktı.format(sayı, sayı**2, sayı**0.5))

Bu sayede sadece fonksiyon gövdesinde değişiklik yaparak, programın başka
kısımlarını hiç etkilemeden yolumuza devam edebiliyoruz.

Buraya kadar anlattıklarımız, fonksiyonların ne işe yaradığı ve bir program
yazarken neden fonksiyonlara ihtiyaç duyacağımız konusunda size bir fikir vermiş
olmalı. Eğer hala aklınızda fonksiyonların faydası konusunda bir şüphe kaldıysa,
fonksiyonların faydasını anlamanızı sağlayabilmek için size şöyle bir soru
sormama izin verin: Acaba 'istihza' kelimesinin kaç karakterden oluştuğunu nasıl
buluruz?

'Elbette ``len()`` fonksiyonunu kullanarak!' dediğinizi duyar gibiyim. Gerçekten
de Python'da bir karakter dizisinin uzunluğunu bulmanın en iyi yolu ``len()``
fonksiyonunu kullanmaktır::
    
    >>> len("istihza")
    
    7

Peki ya Python'da ``len()`` diye bir fonksiyon olmasaydı ne yapacaktınız? Böyle
bir durumda, karakter dizilerinin uzunluğunu ölçmek için sizin bir yöntem icat
etmeniz gerekecekti. Mesela 'istihza' kelimesinin kaç karakterden oluştuğunu
bulmak için şöyle bir kod yazacaktınız::
    
    c = 0
    for s in "istihza":
        c += 1
    print(c)

Burada önce `c` adlı bir değişken tanımlayıp, bu değişkenin değerini `0` yaptık.
Bu değişken, uzunluğunu sorgulamak istediğimiz kelimenin kaç karakterden
oluştuğu bilgisini saklayacak.

Ardından bir ``for`` döngüsü tanımlıyoruz. Bu döngüde, 'istihza' kelimesindeki
her bir karakter için `c` değişkeninin değerini `1` sayı artırıyoruz. Böylece
döngü sonunda `c` değişkeni 'istihza' kelimesi içinde kaç karakter olduğu
bilgisini tutmuş oluyor.

Son olarak da `c` değişkeninin nihai değerini ekrana yazdırıyoruz.

Bu kodları çalıştırdığınızda `7` cevabı alacaksınız. Demek ki 'istihza'
kelimesinde `7` karakter varmış. Peki 'istihza' kelimesi yerine mesela
'Afyonkarahisar' kelimesi içinde kaç karakter olduğunu hesaplamak isterseniz ne
yapacaksınız? Elbette yukarıdaki kodları tekrar yazıp, 'istihza' kelimesini
'Afyonkarahisar' kelimesi ile değiştireceksiniz. Böylece bu kelimenin kaç
karakterden oluştuğunu bulmuş olacaksınız. Sorgulamak istediğiniz her kelime
için aynı şeyleri yapabilirsiniz...

Ne kadar verimsiz bir yöntem, değil mi?

Halbuki hiç bu tür şeylerle uğraşmaya gerek yok. Eğer Python bize ``len()``
fonksiyonu gibi bir fonksiyon vermemiş olsaydı, kendi ``len()`` fonksiyonumuzu
icat edebilirdik. Dikkatlice bakın::
    
    def uzunluk(öğe):
        c = 0
        for s in öğe:
            c += 1
        print(c)

Böylece adı `uzunluk` olan bir fonksiyon tanımlamış olduk. Artık bir öğenin
uzunluğunu hesaplamak istediğimizde, bütün o kodları her defasında tekrar tekrar
yazmak yerine sadece ``uzunluk()`` fonksiyonunu kullanabiliriz::
    
    uzunluk("istihza")
    uzunluk("Afyonkarahisar")
    uzunluk("Tarım ve Köyişleri Bakanlığı")
    
Üstelik bu fonksiyon yalnızca karakter dizilerinin değil öteki veri tiplerinin
de uzunluğunu hesaplayabilir::
    
    liste = ["ahmet", "mehmet", "veli"]
    uzunluk(liste)

Verdiğimiz bu örnek bize hem gömülü fonksiyonların faydasını, hem de genel
olarak fonksiyonların ne işe yaradığını açıkça gösteriyor. Buna göre, ``len()``
benzeri gömülü fonksiyonlar tekerleği yeniden icat etme derdinden kurtarıyor
bizi. Örneğin Python geliştiricilerinin ``len()`` gibi bir fonksiyon tanımlamış
olmaları sayesinde, bir karakter dizisinin uzunluğunu hesaplamak için kendi
kendimize yöntem icat etmek zorunda kalmıyoruz. Ama eğer kendi yöntemimizi icat
etmemiz gerekirse, istediğimiz işlevi yerine getiren bir fonksiyon tanımlamamız
da mümkün. 

Böylece temel olarak fonksiyonların ne işe yaradığını, neye benzediğini, nasıl
tanımlandığını ve nasıl çağrıldığını incelemiş olduk. Şimdi fonksiyonların biraz
daha derinine dalmaya başlayabiliriz.

Parametreler ve Argümanlar
**************************

Şimdiye kadar yaptığımız örnekler sayesinde aslında parametrelerin neye
benzediğini ve ne işe yaradığını öğrenmiştik. Bu bölümde ise sizi 'argüman' adlı
bir kavramla tanıştırıp, argüman ile parametre arasındaki benzerlik ve
farklılıkları inceleyeceğiz. Bunun yanısıra, parametre kavramını da bu bölümde
daha derinlikli bir şekilde ele alacağız.

O halde hemen yola koyulalım.

Parametrenin ne olduğunu biliyorsunuz. Bunlar fonksiyon tanımlarken parantez
içinde belirttiğimiz, fonksiyon gövdesinde yapılan işin değişken öğelerini
gösteren parçalardır. Mesela::
    
    def kopyala(kaynak_dosya, hedef_dizin):
        çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
        print(çıktı.format(kaynak_dosya, hedef_dizin))

Burada ``kopyala()`` adlı bir fonksiyon tanımladık. Bu fonksiyon toplam iki adet
parametre alıyor: `kaynak_dosya` ve `hedef_dizin`. Gördüğünüz gibi, bu iki
parametre gerçekten de fonksiyon gövdesinde yapılan işin değişken öğelerini
gösteriyor. Bu fonksiyonun üreteceği çıktı, fonksiyonu çağıran kişinin bu iki
parametreye vereceği değerlere bağlı olarak şekillenecek.

Bildiğiniz gibi, parametrelere ne ad verdiğinizin hiçbir önemi yok. Elbette
parametrenin görevine uygun bir isim vermeniz fonksiyonunuzun okunaklılığını
artıracaktır. Ama tabii ki bu fonksiyonu pekala şu parametrelerle de
tanımlayabilirdik::
    
    def kopyala(a, b):
        çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
        print(çıktı.format(a, b))

Burada önemli olan, parametre görevi görecek iki adet kelime bulmak. Bu
kelimelerin ne olduğunun önemi yok. Ama tabii ki `kaynak_dosya` ve `hedef_dizin`
adları, `a` ve `b` adlarına kıyasla, fonksiyondaki parametrelerin yaptığı işi
çok daha iyi tarif ediyor.

Parametre adı belirleme kuralları değişken adı belirleme kurallarıyla aynıdır.
Dolayısıyla bir değişken adı belirlerken neye dikkat ediyorsak, parametre adı
belirlerken de aynı şeye dikkat etmeliyiz.

Gelin şimdi isterseniz tanımladığınız bu fonksiyonu çağıralım::

    kopyala("deneme.txt", "/home/istihza/Desktop")

Kodlarımız dosya içinde tam olarak şöyle görünüyor::

    def kopyala(kaynak_dosya, hedef_dizin):
        çıktı = "{} adlı dosya {} adlı dizin içine kopyalandı!"
        print(çıktı.format(kaynak_dosya, hedef_dizin))

    kopyala("deneme.txt", "/home/istihza/Desktop")

Bu kodları bir dosyaya kaydedip çalıştırdığımızda şöyle bir çıktı alırız::

    deneme.txt adlı dosya /home/istihza/Desktop adlı dizin içine kopyalandı!

Gördüğünüz gibi, `"deneme.txt"` ve `"/home/istihza/Desktop"` değerleri, `çıktı`
adlı karakter dizisinde uygun yerlere yerleştirildi ve ekrana çıktı olarak
verildi. İşte burada gördüğünüz bu `"deneme.txt"` ve `"/home/istihza/Desktop"`
değerlerine argüman adı verilir. Yani bir fonksiyonu **tanımlarken**
belirlediğimiz adlara parametre, aynı fonksiyonu **çağırırken** belirlediğimiz
adlara ise argüman deniyor. Dolayısıyla fonksiyon tanımında belirlediğimiz
`kaynak_dosya` ve `hedef_dizin` adlı değişkenler birer parametre, fonksiyon
çağrısında bu parametrelere karşılık gelen `"deneme.txt"` ve
`"/home/istihza/Desktop"` değerleri ise birer argüman oluyor.

Böylece parametre ve argüman arasındaki farkı öğrenmiş olduk. Ancak şunu
belirtmekte yarar var: Bu iki kavram genellikle birbirinin yerine kullanılır.
Yani bu iki kavram arasındaki, yukarıda açıkladığımız farka pek kimse dikkat
etmez. Dolayısıyla pek çok yerde hem parametre hem de argüman için aynı ifadenin
kullanıldığını görebilirsiniz. Özellikle Türkçede parametre kelimesi argüman
kelimesine kıyasla daha bilinir ve yaygın olduğu için, ayrım yapılmaksızın hem
fonksiyon çağrısındaki değerlere, hem de fonksiyon tanımındaki değerlere
parametre adı verilir.

Gelelim parametrelerin çeşitlerine...

Python'da parametreler işlevlerine göre farklı kategorilere ayrılır. Gelin şimdi
bu kategorileri tek tek inceleyelim.

Sıralı (veya İsimsiz) Parametreler
===================================

Python'da şöyle bir fonksiyon tanımlayabileceğimizi biliyoruz::

    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)

Yukarıda tanımladığımız bu fonksiyonu şu şekilde çağırabiliriz::

    kayıt_oluştur("Ahmet", "Öz", "Debian", "Ankara")

Bu fonksiyonda, yazdığımız parametrelerin sırası büyük önem taşır. Mesela
yukarıdaki fonksiyonu şöyle çağırdığımızı düşünün::
    
    kayıt_oluştur("Debian", "Ankara", "Öz", "Ahmet")

Eğer fonksiyon parametrelerini bu sırayla kullanırsak aldığımız çıktı hatalı
olacaktır::
    
    ------------------------------
    isim           :  Debian
    soyisim        :  Ankara
    işletim sistemi:  Öz
    şehir          :  Ahmet
    ------------------------------

Gördüğünüz gibi, isim, soyisim ve öteki bilgiler birbirine karışmış. İşte
Python'da, veriliş sırası önem taşıyan bu tür parametrelere 'sıralı
parametreler' (veya isimsiz parametreler) adı verilir.

İsimli Parametreler
===================

Bir önceki bölümde verdiğimiz şu örneği yeniden ele alalım::

    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)

Bu fonksiyonu çağırırken parametrelerin sırasını doğru vermenin, alacağımız
çıktının düzgün olması bakımından büyük önem taşıdığını biliyoruz. Ancak
özellikle parametre sayısının çok olduğu fonksiyonlarda parametre sırasını
akılda tutmak zor olabilir. Böyle durumlarda parametreleri isimleri ile birlikte
kullanmayı tercih edebiliriz::
    
    kayıt_oluştur(soyisim="Öz", isim="Ahmet", işsis="Debian", şehir= "Ankara")

Böylece fonksiyon parametrelerini istediğimiz sıra ile kullanabiliriz. Ancak
burada dikkat etmemiz gereken bazı noktalar var. Python'da isimli bir
parametrenin ardından sıralı bir parametre gelemez. Yani şu kullanım yanlıştır::
    
    kayıt_oluştur(soyisim="Öz", isim="Ahmet", "Debian", "Ankara")

Bu kodlar bize şu hatayı verir::

      File "<stdin>", line 1
    SyntaxError: non-keyword arg after keyword arg

Bu yüzden, eğer isimli parametreler kullanacaksak, isimli parametrelerden sonra
sıralı parametre kullanmamaya dikkat ediyoruz.

Varsayılan Değerli Parametreler
================================

Şimdiye kadar karşılaştığımız fonksiyonlarda bir şey dikkatinizi çekmiş olmalı.
Mesela ``print()`` fonksiyonunu ele alalım. Bildiğiniz gibi, bu fonksiyonu en
basit şekilde şöyle kullanıyoruz::
    
    print("Fırat", "Özgül")

Evet, ``print()`` fonksiyonunu bu şekilde kullanabiliyoruz, ancak bildiğiniz
gibi, aslında bu fonksiyonun bazı özel parametreleri de var. Daha önceki
derslerimizden hatırlayacağınız gibi, biz yukarıdaki komutu verdiğimizde aslında
Python bunu şu şekilde algılıyor::
    
    print("Fırat", "Özgül", sep=" ", end="\n", file=sys.stdout, flush=False)

Yani biz görmesek de aslında her ``print()`` çağrısı `sep`, `end`, `file` ve
`flush` parametrelerini de içeriyor. Biz bu özel parametreleri kullanmasak da,
yazdığımız kod düzgün bir şekilde çalışır. Bunun nedeni, `sep`, `end`, `file` ve
`flush` parametrelerinin öntanımlı olarak birtakım değerlere sahip olmasıdır.
Yani biz bu parametrelere kendimiz bir değer atamazsak Python bu parametrelere
kendi belirlediği bazı öntanımlı değerleri atayacaktır. Dolayısıyla, eğer biz
başka bir değer yazmazsak, `sep` parametresi `" "` değerine, `end` parametresi
`"\n"` değerine, `file` parametresi `sys.stdout` değerine, `flush` parametresi
ise `False` değerine sahip olacaktır. İşte bu tür parametrelere Python'da
'varsayılan değerli parametreler' adı verilir. Peki biz kendimiz varsayılan
değerli parametreler içeren fonksiyonları nasıl tanımlayabiliriz?

Şu örneğe dikkatlice bakın::

    def kur(kurulum_dizini="/usr/bin/"):
        print("Program {} dizinine kuruldu!".format(kurulum_dizini))
    
Burada ``kur()`` adlı bir fonksiyon tanımladık. Bu fonksiyonun görevi,
yazdığımız bir programı, kullanıcının bilgisayarındaki bir dizine kurmak ve
programın hangi dizine kurulduğu konusunda kullanıcıyı bilgilendirmek. Bu
fonksiyonu şu şekilde çağırabiliriz::

    kur()

Eğer ``kur()`` fonksiyonunu böyle çağırırsak bize şu çıktıyı verecektir::

    Program /usr/bin/ dizinine kuruldu!

Gördüğünüz gibi, ``kur()`` fonksiyonunun `kurulum_dizini` adlı bir parametresi
var. Biz fonksiyonu tanımlarken, bu parametreye bir varsayılan değer atadık
(`/usr/bin/`). Böylece ``kur()`` fonksiyonu parametresiz olarak çağrıldığında bu
varsayılan değer devreye girdi. Eğer biz bu değeri değiştirmek istersek, mesela
programımızın "C:\\Users\\firat" dizinine kurulmasını istersek, ``kur()``
fonksiyonunu şöyle çağırmalıyız::

    kur("C:\\Users\\firat")

``kur()`` fonksiyonunu yukarıdaki gibi çağırdığımızda Python bize şöyle bir
çıktı verir::
    
    Program C:\Users\firat dizinine kuruldu!

Bu örnek size, varsayılan değerli parametreler belirlemenin ne kadar faydalı
olabileceğini göstermiş olmalı. Mesela bir program yazdığınızı düşünün.
Programınızı indiren kullanıcılar, yukarıdaki gibi bir varsayılan değerli
parametre belirlemiş olmanız sayesinde programınızı nereye kuracaklarını
belirlemek zorunda kalmadan bir sonraki kurulum adımına geçebiliyorlar...

Elbette eğer isterseniz kullanıcılarınızı bir kurulum dizini belirlemeye
zorlamak da isteyebilirsiniz. Bunun için yine varsayılan değerli parametrelerden
yararlanabilirsiniz::
    
    def kur(kurulum_dizini=''):
        if not kurulum_dizini:
            print("Lütfen programı hangi dizine kurmak istediğinizi belirtin!")
        else:
            print("Program {} dizinine kuruldu!".format(kurulum_dizini))

Bu defa `kurulum_dizini` parametresinin varsayılan değerini boş bir karakter
dizisi olarak belirledik. Eğer bu parametrenin değeri boş bir karakter dizisi
olursa, kullanıcı herhangi bir kurulum dizini belirtmemiş demektir. Eğer
kullanıcı herhangi bir kurulum dizini belirtmezse `kurulum_dizini`
parametresinin bool değeri `False` olacaktır. Bu özelliği dikkate alarak
fonksiyon gövdesinde şu kodları kullanabiliyoruz::
    
    if not kurulum_dizini:
        print("Lütfen programı hangi dizine kurmak istediğinizi belirtin!")
    
Böylece, `kurulum_dizini` parametresinin bool değeri `False` olursa
kullanıcılarımıza şöyle bir uyarı gösteriyoruz::
    
    "Lütfen programı hangi dizine kurmak istediğinizi belirtin!"

Dolayısıyla kuruluma başlayabilmek için ``kur()`` fonksiyonunun şöyle
çalıştırılmasını zorunlu tutuyoruz::
    
    kur("C:\\Users\\istihza")

Buna benzer durumlarla pek çok kez karşılaşmış olmalısınız. Özellikle
programların kurulmasını sağlayan '*setup*' betiklerinde her aşama için bir
varsayılan değer belirlenip, kullanıcının sadece '*Next*' tuşlarına basarak
sağlıklı bir kurulum yapması sağlanabiliyor. Eğer kullanıcı varsayılan
değerlerin dışında birtakım değerler belirlemek isterse, yukarıda örneğini
verdiğimiz yapı kullanıcıya böyle bir özgürlük de sağlıyor.

Rastgele Sayıda İsimsiz Parametre Belirleme
===========================================
    
Şimdiye kadar öğrendiğimiz pek çok fonksiyonun toplam kaç parametre alabileceği
bellidir. Örneğin ``input()`` fonksiyonu yalnızca tek bir parametre alabilir.
Eğer bu fonksiyona birden fazla parametre verirsek Python bize bir hata mesajı
gösterecektir. Aynı şekilde mesela ``pow()`` fonksiyonunun da kaç parametre
alabileceği bellidir. Ama örneğin ``print()`` fonksiyonuna verebileceğimiz
parametre sayısı (teknik olarak 256 ile sınırlı olsa da) pratik olarak neredeyse
sınırsızdır.

Peki acaba biz kendimiz, sınırsız parametre alabilen fonksiyonlar üretebilir
miyiz? 

Bu sorunun cevabı 'evet' olacaktır. Şimdi şu örneğe dikkatlice bakın::
    
    def fonksiyon(*parametreler):
        print(parametreler)
        
    fonksiyon(1, 2, 3, 4, 5)
    
Bu kodları çalıştırdığımızda şu çıktıyı alacağız::

    (1, 2, 3, 4, 5)

Gördüğünüz gibi, fonksiyon tanımı içinde kullandığımız `*` işareti sayesinde
fonksiyonumuzun pratik olarak sınırsız sayıda parametre kabul etmesini
sağlayabiliyoruz. Bu arada, bu tür fonksiyonların alabileceği parametre sayısı,
dediğimiz gibi, pratikte sınırsızdır, ama teknik olarak bu sayı 256 adedi
geçemez.

Yukarıdaki kodların verdiği çıktının bir demet olduğuna dikkatinizi çekmek
isterim. Bu bilgiye sahip olduktan sonra, bu tür fonksiyonları demet işleme
kurallarına göre istediğiniz şekilde manipüle edebilirsiniz.

Peki böyle bir fonksiyon tanımlamak ne işimize yarar? 

Mesela bu yapıyı kullanarak şöyle bir fonksiyon yazabilirsiniz::
    
    def çarp(*sayılar):
        sonuç = 1
        for i in sayılar:
            sonuç *= i
        print(sonuç)
        
Bu fonksiyon kendisine verilen bütün parametreleri birbiriyle çarpar. Örneğin::
    
    çarp(1, 2, 3, 4)
    
Bu kodun çıktısı `24` olacaktır. Gördüğünüz gibi, fonksiyonumuza istediğimiz
sayıda parametre vererek bu sayıların birbiriyle çarpılmasını sağlayabiliyoruz. 

Aslında burada kullandığımız `*` işareti size hiç yabancı değil. Hatırlarsanız
``print()`` fonksiyonundan bahsederken şuna benzer bir kullanım örneği
vermiştik::
    
    >>> print(*'TBMM', sep='.')
    
    T.B.M.M
    
Burada `*` işareti, eklendiği parametreyi öğelerine ayırıyor. `sep` parametresi
ise `*` işaretinin birbirinden ayırdığı öğelerin arasına birer '.' karakteri
ekliyor. 

Bu işaretin etkilerini şu örneklerde daha net görebilirsiniz::
    
    >>> liste = ["Ahmet", "Mehmet", "Veli"]
    >>> print(*liste)
    
    Ahmet Mehmet Veli

    >>> sözlük = {"a": 1, "b": 2}
    >>> print(*sözlük)
    
    a b
    
Gördüğünüz gibi, `*` işareti herhangi bir öğeyi alıp, bunu parçalarına ayırıyor.
İşte bu `*` işaretini fonksiyon tanımlarken kullandığımızda ise bu işlemin tam
tersi gerçekleşiyor. Yani fonksiyon tanımında parametrenin soluna `*`
getirdiğimizde, bu fonksiyon çağrılırken verilen argümanlar tek bir değişken
içinde bir demet olarak toplanıyor. Zaten bu konunun başında verdiğimiz şu
örnekte de bu durum açıkça görünüyor::
    
    def fonksiyon(*parametreler):
        print(parametreler)
        
    fonksiyon(1, 2, 3, 4, 5)
    
Bu fonksiyonu çağırdığımızda şu çıktı veriliyor::
    
    (1, 2, 3, 4, 5)
    
Aynen söylediğimiz gibi, ``fonksiyon()`` adlı fonksiyona argüman olarak
verdiğimiz her bir öğenin (`1`, `2`, `3`, `4`, `5`) tek bir demet içinde
toplandığını görüyorsunuz. 

Yıldızlı parametreler, tanımladığınız fonksiyonun parametre sayısını herhangi
bir şekilde sınırlamak istemediğiniz durumlarda çok işinize yarar. 

Elbette `*` işaretiyle birlikte kullanacağınız parametrenin adı olarak,
Python'ın değişken adlandırma kurallarına uygun bütün kelimeleri
belirleyebilirsiniz. Mesela biz yukarıda 'parametreler' adını tercih ettik. Ama
Python dünyasında `*` işaretiyle birlikte kullanılacak parametrenin adı
geleneksel olarak, 'argümanlar' anlamında 'args'tır. Yani Python programcıları
genellikle yukarıdaki gibi bir fonksiyonu şöyle tanımlar::
    
    def fonksiyon(*args):
        ...
        
`*` işareti ile birlikte kullanılacak parametrenin adını 'args' yapmak bir
zorunluluk olmamakla birlikte, başka Python programcılarının kodlarınızı daha
kolay anlayabilmesi açısından bu geleneği devam ettirmenizi tavsiye ederim.
Yazdığımız kodlarda Python programlama dilinin geleneklerine bağlı kalmak
çoğunlukla iyi bir alışkanlıktır.
       

Rastgele Sayıda İsimli Parametre Belirleme
==========================================

Bir önceki başlık altında, fonksiyon tanımlarken rastgele sayıda isimsiz
parametrelerin nasıl belirleneceğini tartıştık. Aynı bu şekilde, rastgele sayıda
**isimli** parametre belirlemek de mümkündür. 

Örneğin::
    
    def fonksiyon(**parametreler):
        print(parametreler)
    
    fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")
    
Bu kodları çalıştırdığımızda şöyle bir çıktı alıyoruz::
    
    {'şehir': 'Ankara', 'isim': 'Ahmet', 'soyisim': 'Öz', 'meslek': 'Mühendis'}
    
Gördüğünüz gibi, fonksiyonu tanımlarken parametremizin sol tarafına
yerleştirdiğimiz `**` işareti, bu fonksiyonu çağırırken yazdığımız isimli
parametrelerin bize bir sözlük olarak verilmesini sağlıyor. Bu yapının bize bir
sözlük verdiğini bildikten sonra, bunu sözlük veri tipinin kuralları
çerçevesinde istediğimiz şekilde evirip çevirebiliriz.

Peki bu araç ne işimize yarar?

Hatırlarsanız bu bölümün en başında ``kayıt_oluştur()`` adlı şöyle bir fonksiyon
tanımlamıştık::

    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)
        
Bu fonksiyon bize toplam dört adet parametre kullanarak, isim, soyisim, işletim
sistemi ve şehir bilgilerinden meydana gelen bir kayıt oluşturma imkanı
sağlıyor. Bu fonksiyonda kullanıcının girebileceği bilgiler sınırlı. Ama bir de
şöyle bir fonksiyon yazdığımızı düşünün::
    
    def kayıt_oluştur(**bilgiler):
        print("-"*30)
        
        for anahtar, değer in bilgiler.items():
            print("{:<10}: {}".format(anahtar, değer))
        
        print("-"*30)
        
    kayıt_oluştur(ad="Fırat", soyad="Özgül", şehir="İstanbul", tel="05333213232")

Bu fonksiyonu çalıştırdığımızda şu çıktıyı alacağız::
    
    tel       : 05333213232
    ad        : Fırat
    şehir     : İstanbul
    soyad     : Özgül
    
Gördüğünüz gibi, `**` işaretlerini kullanmamız sayesinde hem adlarını hem de
değerlerini kendimiz belirlediğimiz bir kişi veritabanı oluşturma imkanı elde
ediyoruz. Üstelik bu veritabanının, kişiye ait kaç farklı bilgi içereceğini de
tamamen kendimiz belirleyebiliyoruz. 

..
    def kayıt_oluştur(**bilgiler):
        print("-"*30)
        
        uzunluk = len(max(bilgiler.keys()))
        
        for anahtar, değer in bilgiler.items():
            print("{0:<{1}}: {2}".format(anahtar, uzunluk+2, değer))
        
        print("-"*30)
        
    kayıt_oluştur(ad="Fırat", soyad="Özgül", şehir="İstanbul", tel="05333213232")

Tıpkı `*` işaretlerinin betimlediği parametrenin geleneksel olarak 'args'
şeklinde adlandırılması gibi, `**` işaretlerinin betimlediği parametre de
geleneksel olarak 'kwargs' şeklinde adlandırılır. Dolayısıyla yukarıdaki gibi
bir fonksiyonu Python programcıları şöyle tanımlar::
    
    def kayıt_oluştur(**kwargs):
        ...

`**` işaretli parametreler pek çok farklı durumda işinize yarayabilir veya
işinizi kolaylaştırabilir. Mesela `*` ve `**` işaretlerini kullanarak şöyle bir
program yazabilirsiniz::
    
    def karşılık_bul(*args, **kwargs):
        for sözcük in args:
            if sözcük in kwargs:
                print("{} = {}".format(sözcük, kwargs[sözcük]))
            else:
                print("{} kelimesi sözlükte yok!".format(sözcük))
        
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
            
    karşılık_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)  
    
Burada tanımladığımız ``karşılık_bul()`` adlı fonksiyon, kendisine verilen
parametreleri (`*args`), bir sözlük içinde arayarak (`**sözlük`) karşılıklarını
bize çıktı olarak veriyor. Eğer verilen parametre sözlükte yoksa, ilgili
kelimenin sözlükte bulunmadığı konusunda da bizi bilgilendiriyor.

``karşılık_bul()`` adlı fonksiyonu nasıl tanımladığımıza çok dikkat edin.
Parametre listesi içinde belirttiğimiz `*args` ifadesi sayesinde, fonksiyonu
kullanacak kişiye, istediği sayıda isimsiz parametre girme imkanı tanıyoruz.
`**kwargs` parametresi ise kullanıcıya istediği sayıda isimli parametre girme
olanağı veriyor.

Esasında yukarıdaki kod `*args` ve `**kwargs` yapıları açısından ucuz bir
örnektir. Bu yapılar için daha nitelikli bir örnek verelim...

Bildiğiniz gibi ``print()`` fonksiyonu sınırsız sayıda isimsiz parametre ve buna
ek olarak birkaç tane de isimli parametre alıyor. Bu fonksiyonun alabildiği
isimli parametrelerin `sep`, `end`, `file` ve `flush` adlı parametreler olduğunu
biliyorsunuz. Yine bildiğiniz gibi, `sep` parametresi ``print()`` fonksiyonuna
verilen isimsiz parametrelerin her birinin arasına hangi karakterin geleceğini;
`end` parametresi ise bu parametrelerin en sonuna hangi karakterin geleceğini
belirliyor. Bizim amacımız bu fonksiyona bir de `start` adında isimli bir
parametre ekleyerek ``print()`` fonksiyonunun işlevini genişleten başka bir
fonksiyon yazmak. Bu yeni parametre, karakter dizilerinin **en başına** hangi
karakterin geleceğini belirleyecek.
        
Şimdi bu amacımızı gerçekleştirecek kodlarımızı yazalım::

    def bas(*args, start='', **kwargs):
        for öğe in args:
            print(start+öğe, **kwargs)
    
    bas('öğe1', 'öğe2', 'öğe3', start="#.")

``print()`` fonksiyonunun işlevini genişleten yeni fonksiyonumuzun adı
``bas()``. Bu fonksiyon her bakımdan ``print()`` fonksiyonu ile aynı işlevi
görecek. Ancak ``bas()`` fonksiyonu, ``print()`` fonksiyonuna ek olarak, sahip
olduğu `start` adlı bir isimli parametre sayesinde, kendisine verilen
parametrelerin **en başına** istediğimiz herhangi bir karakteri eklemek
olanağı da verecek bize. 

``bas()`` fonksiyonunun ilk parametresi olan `*args` sayesinde kullanıcıya
istediği kadar parametre verme imkanı tanıyoruz. Daha sonra da ilave `start`
parametresini tanımlıyoruz. Bu parametrenin öntanımlı değeri boş bir karakter
dizisi. Yani eğer kullanıcı bu parametrenin değerine herhangi bir şey yazmazsa,
`*args` kapsamında verilen parametreler üzerinde hiçbir değişiklik yapmıyoruz.
Bunun ardından gelen `**kwargs` parametresi ise ``print()`` fonksiyonunun
halihazırda sahip olduğu `sep`, `end`, `file` ve `flush` parametrelerinin
``bas()`` fonksiyonunda da aynı şekilde kullanılmasını sağlıyor. `**kwargs`
şeklinde bir tanımlama sayesinde, ``print()`` fonksiyonunun isimli
parametrelerini tek tek belirtip tanımlamak zorunda kalmıyoruz::
    
    def bas(*args, start='', **kwargs):
        for öğe in args:
            print(start+öğe, **kwargs)
    
    f = open("te.txt", "w")
    
    bas('öğe1', 'öğe2', 'öğe3', start="#.", end="", file=f)
    
Eğer elimizde `**kwargs` gibi bir imkan olmasaydı yukarıdaki fonksiyonu şu
şekilde tanımlamamız gerekirdi::
    
    import sys
    
    def bas(*args, start='', sep=' ', end='\n', file=sys.stdout, flush=False):
        for öğe in args:
            print(start+öğe, sep=sep, end=end, file=file, flush=flush)
            
Gördüğünüz gibi, ``print()`` fonksiyonunun bütün isimli parametrelerini ve
bunların öntanımlı değerlerini tanımlamak zorunda kaldık. Eğer günün birinde
Python geliştiricileri ``print()`` fonksiyonuna bir başka isimli parametre daha
eklerse, yukarıdaki fonksiyonu ilgili yeniliğe göre elden geçirmemiz gerekir.
Ama `**kwargs` yapısını kullandığımızda, ``print()`` fonksiyonuna Python
geliştiricilerince eklenecek bütün parametreler bizim fonksiyonumuza da otomatik
olarak yansıyacaktır...

return Deyimi
*************

Bu bölümde ``return`` adlı bir deyimden söz edeceğiz. Özellikle Python
programlama dilini öğrenmeye yeni başlayanlar bu deyimin ne işe yaradığını
anlamakta zorlanabiliyor. Biz burada bu deyimi anlaşılır hale getirebilmek için
elimizden geleni yapacağız. Öncelikle çok basit bir örnek verelim::
    
    def ismin_ne():
        isim = input("ismin ne? ")
        print(isim)

Bu çok basit bir fonksiyon. Bu fonksiyonu nasıl çağıracağımızı biliyoruz::
    
    ismin_ne()
    
Fonksiyonu bu şekilde çağırdıktan sonra, fonksiyon tanımında yer alan
``input()`` fonksiyonu sayesinde kullanıcıya ismi sorulacak ve verdiği cevap
ekrana basılacaktır. 

Yukarıdaki fonksiyonun tek işlevi kullanıcıdan aldığı isim bilgisini ekrana
basmaktır. Aldığınız bu veriyi başka yerlerde kullanamazsınız. Bu fonksiyonu
çağırdığınız anda kullanıcıya ismi sorulacak ve alınan cevap ekrana
basılacaktır. Ancak siz, tanımladığınız fonksiyonların tek görevinin bir veriyi
ekrana basmak olmasını istemeyebilirsiniz.

Örneğin yukarıdaki fonksiyon yardımıyla kullanıcıdan ismini aldıktan sonra, bu
isim bilgisini başka bir karakter dizisi içinde kullanmak isteyebilirsiniz.
Diyelim ki amacınız ``ismin_ne()`` fonksiyonuyla aldığınız ismi şu karakter
dizisi içine aşağıdaki şekilde yerleştirmek::
    
    Merhaba Fırat. Nasılsın?
    
Bildiğimiz yöntemi kullanarak bu amacımızı gerçekleştirmeye çalışalım::
    
    print("Merhaba {}. Nasılsın?".format(ismin_ne()))
    
Buradan şöyle bir çıktı alıyoruz::
    
    ismin ne? Fırat
    Fırat
    Merhaba None. Nasılsın?
    
Gördüğünüz gibi, istediğimiz şeyi elde edemiyoruz. Çünkü dediğimiz gibi,
yukarıdaki fonksiyonun tek görevi kullanıcıdan aldığı çıktıyı ekrana basmaktır.
Bu fonksiyondan gelen çıktıyı başka yerde kullanamayız. Eğer kullanmaya
çalışırsak yukarıdaki gibi hiç beklemediğimiz bir sonuç alırız. 

Bu arada, çıktıda `None` diye bir şey gördüğünüze dikkat edin. Yukarıdaki
fonksiyonu şu şekilde çağırarak bunu daha net görebilirsiniz::
    
    print(ismin_ne())
    
Buradan şu çıktıyı alıyoruz::
    
    ismin ne? Fırat
    Fırat
    None
    
Bu çıktının ne anlama geldiğini birazdan açıklayacağız. Ama öncelikle başka bir
konudan söz edelim. 

Biraz önce söylediğimiz gibi, yukarıda tanımladığımız ``ismin_ne()`` adlı
fonksiyonun tek görevi kullanıcıdan aldığı isim bilgisini ekrana basmaktır.
Şimdi bu fonksiyonu bir de şöyle tanımlayalım::
    
    def ismin_ne():
        isim = input("ismin ne? ")
        return isim
        
Şimdi de bu fonksiyonu çağıralım::        
    
    ismin_ne()
    
Gördüğünüz gibi, fonksiyonu çağırdığımızda yalnızca fonksiyon gövdesindeki
``input()`` fonksiyonu çalıştı, ama bu fonksiyondan gelen veri ekrana çıktı
olarak verilmedi. Çünkü biz burada herhangi bir ekrana basma ('print') işlemi
yapmadık. Yaptığımız tek şey `isim` adlı değişkeni 'döndürmek'.

Peki bu ne anlama geliyor?

*return* kelimesi İngilizcede 'iade etmek, geri vermek, döndürmek' gibi anlamlar
taşır. İşte yukarıdaki örnekte de ``return`` deyiminin yaptığı iş budur. Yani bu
deyim bize fonksiyondan bir değer 'döndürür'. 

Eğer tanımladığımız bir fonksiyonda ``return`` deyimini kullanarak herhangi bir
değer döndürmezsek, Python fonksiyondan hususi bir değerin döndürülmediğini
göstermek için 'None' adlı bir değer döndürür... İşte yukarıda tanımladığımız
ilk ``ismin_ne()`` fonksiyonunu ``print(ismin_ne())`` şeklinde çağırdığımızda
ekranda `None` değerinin görünmesinin nedeni budur.

Peki bir fonksiyon içinde herhangi bir veriyi ekrana basmayıp ``return`` deyimi
yardımıyla döndürmemizin bize ne faydası var? 

Aslında bunun cevabı çok açık. Bir fonksiyon içinde bir değeri döndürmek yerine
ekrana bastığınızda o fonksiyonun işlevini alabildiğine kısıtlamış oluyorsunuz.
Fonksiyonunuzun tek işlevi bir değeri ekrana basmak oluyor. Şu örnekte de
gösterdiğimiz gibi, bu değeri daha sonra başka ortamlarda kullanamıyoruz::
    
    def ismin_ne():
        isim = input("ismin ne? ")
        print(isim)

    print("Merhaba {}. Nasılsın?".format(ismin_ne()))

Ama eğer, mesela yukarıdaki fonksiyonda `isim` değişkenini basmak yerine
döndürürsek işler değişir::
    
    def ismin_ne():
        isim = input("ismin ne? ")
        return isim
    
    print("Merhaba {}. Nasılsın?".format(ismin_ne()))

Bu kodları çalıştırdığımızda şu çıktıyı alıyoruz::
    
    ismin ne? Fırat
    Merhaba Fırat. Nasılsın?

Gördüğünüz gibi, istediğimiz çıktıyı rahatlıkla elde ettik. ``ismin_ne()`` adlı
fonksiyondan `isim` değerini döndürmüş olmamız sayesinde bu değerle istediğimiz
işlemi gerçekleştirebiliyoruz. Yani bu değeri sadece ekrana basmakla
sınırlamıyoruz kendimizi. Hatta fonksiyondan döndürdüğümüz değeri başka bir
değişkene atama imkanına dahi sahibiz bu şekilde::
    
    ad = ismin_ne()
    print(ad)
    
Eğer fonksiyondan değer döndürmek yerine bu değeri ekrana basmayı tercih
etseydik yukarıdaki işlemi yapamazdık.

``return`` deyimiyle ilgili son bir şey daha söyleyelim...

Bu deyim, içinde bulunduğu fonksiyonun çalışma sürecini kesintiye uğratır. Yani
``return`` deyimini kullandığınız satırdan sonra gelen hiçbir kod çalışmaz.
Basit bir örnek verelim::
    
    def fonk():
        print(3)
        return
        print(5)
        
    fonk()
    
Bu kodları çalıştırdığınızda yalnızca ``print(3)`` satırının çalıştığını,
``print(5)`` satırına ise hiç ulaşılmadığını göreceksiniz. İşte bu durumun
sebebi, Python'ın kodları ``return`` satırından itibaren okumayı bırakmasıdır.
Bu özellikten çeşitli şekillerde yararlanabilirsiniz. Örneğin::
    
    def fonk(n):
        if n < 0:
            return 'eksi değerli sayı olmaz!'
        else:
            return n
        
    f = fonk(-5)
    print(f)
    
Burada eğer fonksiyona parametre olarak eksi değerli bir sayı verilirse Python
bize bir uyarı verecek ve fonksiyonun çalışmasını durduracaktır.
            
Örnek bir Uygulama
*******************

Gelin isterseniz buraya kadar öğrendiklerimizi kullanarak örnek bir uygulama
yazalım. Bir yandan da yeni şeyler öğrenerek bilgimize bilgi katalım.

Amacımız belli miktarda ve belli aralıkta rastgele sayılar üreten bir program
yazmak. Örneğin programımız şu şekilde altı adet rastgele sayı üretebilecek::
    
    103, 298, 152, 24, 91, 285
    
Ancak programımız bu sayıları üretirken her sayıdan yalnızca bir adet üretecek.
Yani aynı seride bir sayıdan birden fazla bulunamayacak. 

Dilerseniz öncelikle kodlarımızı görelim::
        
    import random
    
    def sayı_üret(başlangıç=0, bitiş=500, adet=6):
        sayılar = set()
        
        while len(sayılar) < adet:
            sayılar.add(random.randrange(başlangıç, bitiş))
        
        return sayılar
        
Esasında bu kodların (neredeyse) tamamını anlayabilecek kadar Python bilgisine
sahipsiniz. Burada anlamamış olabileceğiniz tek şey `random` modülüdür. O yüzden
gelin isterseniz bu modülden biraz söz edelim. 

Biz henüz modül kavramını bilmiyoruz. Ama buraya gelene kadar birkaç konu
altında modüllerle ilgili bazı örnekler de yapmadık değil. Örneğin şimdiye kadar
yazdığımız programlardan öğrendiğimiz kadarıyla Python'da `os` ve `sys` adlı iki
modülün bulunduğunu, bu modüllerin içinde, program yazarken işimize yarayacak
pek çok değişken ve fonksiyon bulunduğunu ve bu fonksiyonları programlarımızda
kullanabilmek için ilkin bu modülleri içe aktarmamız gerektiğini biliyoruz. İşte
tıpkı `os` ve `sys` gibi, `random` da Python programlama dili bünyesinde bulunan
modüllerden biridir. Bu modülün içinde, rastgele sayılar üretmemizi sağlayacak
bazı fonksiyonlar bulunur. İşte ``randrange()`` de bu fonksiyonlardan biridir.
Dilerseniz bu fonksiyonun nasıl kullanıldığını anlamak için etkileşimli kabukta
birkaç deneme çalışması yapalım. 

`random` modülünün içindeki araçları kullanabilmek için öncelikle bu modülü içe
aktarmalıyız::
    
    >>> import random

Acaba bu modülün içinde neler varmış?

::
    
    >>> dir(random)

    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 
    'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', 
    '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', 
    '__cached__', '__doc__', '__file__', '__initializing__', 
    '__loader__', '__name__', '__package__', '_acos', '_ceil',
    '_cos', '_e', '_exp', '_inst', '_log', '_pi', '_random', '_sha512', 
    '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 
    'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 
    'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 
    'paretovariate', 'randint', 'random', 'randrange', 'sample', 
    'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 
    'vonmisesvariate', 'weibullvariate']
    
Gördüğünüz gibi bu modülün içinde epey araç var. Gelin isterseniz bu araçlardan
en sık kullanılanlarını tanıyalım.

Örneğin `random` modülü içinde bulunan ``sample()`` adlı fonksiyon herhangi bir
dizi içinden istediğimiz sayıda rastgele numune almamızı sağlar::
    
    >>> liste = ["ahmet", "mehmet", "sevgi", "sevim", "selin", "zeynep", "selim"]
    >>> random.sample(liste, 2)
    
    ['sevim', 'ahmet']
    
Gördüğünüz gibi, yedi kişilik bir isim listesinden `2` adet rastgele numune
aldık. Aynı işlemi tekrarlayalım::
    
    >>> random.sample(liste, 2)
    
    ['sevgi', 'zeynep']
    
    >>> random.sample(liste, 5)
    
    ['selin', 'zeynep', 'ahmet', 'selim', 'mehmet']
    
Numune alma işlemi tamamen rastgeledir. Ayrıca gördüğünüz gibi, listeden
istediğimiz sayıda numune alabiliyoruz.

`random` modülü içinde bulunan ``shuffle()`` adlı başka bir fonksiyon, bir dizi
içindeki öğelerin sırasını rastgele bir şekilde karıştırmamızı sağlar::
    
    >>> liste = ["ahmet", "mehmet", "sevgi", "sevim", 
    ... "selin", "zeynep", "selim"]
    >>> random.shuffle(liste)
    
``shuffle()`` fonksiyonu liste öğelerini yine aynı liste içinde değiştirdi.
Değişikliği görmek için listeyi ekrana basabilirsiniz::
    
    >>> liste
    
    ['selim', 'selin', 'ahmet', 'mehmet', 
    'sevim', 'sevgi', 'zeynep']

`random` modülü içinde bulunan bir başka fonksiyon ise ``randrange()``
fonksiyonudur. Bu fonksiyon, belli bir aralıkta rastgele sayılar üretmemizi
sağlar::
    
    >>> random.randrange(0, 500)
    
    156
    
Burada `0` ile `500` arasında rastgele bir sayı ürettik.

Gördüğünüz gibi `random` son derece faydalı olabilecek bir modüldür. Dilerseniz
şimdi `random` fonksiyonunu bir kenara bırakıp kodlarımıza geri dönelim::
    
    import random
    
    def sayı_üret(başlangıç=0, bitiş=500, adet=6):
        sayılar = set()
        
        while len(sayılar) < adet:
            sayılar.add(random.randrange(başlangıç, bitiş))
        
        return sayılar
        
Burada ilk satırın ne iş yaptığını öğrendik. Bu satır yardımıyla `random`
modülünü içe aktarıyoruz.

Sonraki satırda fonksiyonumuzu tanımlamaya başlıyoruz::
    
    def sayı_üret(başlangıç=0, bitiş=500, adet=6):
        ...
        
Fonksiyonumuzun adı `sayı_üret`. Bu fonksiyon toplam üç farklı parametre alıyor.
Bunlar `başlangıç`, `bitiş` ve `adet`. Dikkat ederseniz bu parametrelerin her
birinin bir varsayılan değeri var. Dolayısıyla ``sayı_üret()`` fonksiyonu
parametresiz olarak çağrıldığında bu üç parametre öntanımlı değerlerine sahip
olacaktır.

Gelelim fonksiyon gövdesine...

İlk olarak `sayılar` adlı bir küme tanımlıyoruz. 

Bildiğiniz gibi, kümeler içinde öğeler her zaman tektir. Yani bir küme içinde
aynı öğeden yalnızca bir adet bulunabilir. Kümelerin bu özelliği bizim
yazdığımız program için oldukça uygun. Çünkü biz de ürettiğimiz rastgele
sayıların benzersiz olmasını istiyoruz. Bu benzersizliği sağlayabilecek en uygun
veri tipi kümelerdir. 

Bir sonraki satırda bir ``while`` döngüsü görüyoruz::
    
    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))
        
Bu döngüye göre, `sayılar` değişkeninin uzunluğu `adet` parametresinin
değerinden az olduğu müddetçe, `sayılar` adlı değişkene `başlangıç` ve `bitiş`
parametrelerinin gösterdiği değerler arasından rastgele sayılar eklemeye devam
edeceğiz. Örneğin kullanıcı fonksiyonumuzu parametresiz olarak çağırdıysa,
yukarıdaki döngü şu şekilde işleyecektir::
    
    while len(sayılar) < 6:
        sayılar.add(random.randrange(0, 500))
        
Buna göre, `sayılar` değişkeninin uzunluğu `6`'dan az olduğu müddetçe bu
değişkene `0` ile `500` arasında rastgele sayılar eklemeye devam edeceğiz.
Böylelikle `sayılar` değişkeni içinde birbirinden farklı toplam `6` sayı olmuş
olacak. 

Fonksiyonun son satırında ise şu kodu görüyoruz::
    
    return sayılar
    
Bu kod yardımıyla, belirtilen miktardaki sayıları tutan `sayılar` adlı değişkeni
fonksiyondan döndürüyoruz. Yani fonksiyonumuz dış dünyaya `sayılar` adlı bir
değişken veriyor... Bu değişkeni bu şekilde döndürdükten sonra istediğimiz gibi
kullanabiliriz. Mesela::
    
    for i in range(100):
        print(sayı_üret())
        
  
Buradan şuna benzer bir çıktı alacaksınız::
    
    {34, 144, 211, 468, 58, 286}
    {41, 170, 395, 113, 178, 29}
    {161, 195, 452, 271, 212, 324}
    {1, 328, 461, 398, 464, 220}
    {356, 489, 12, 114, 329, 472}
    {320, 34, 238, 176, 243, 149}
    {364, 304, 434, 403, 217, 63}
    {452, 392, 175, 464, 81, 467}
    {36, 230, 21, 440, 287, 415}
    {292, 391, 145, 182, 440, 223}
    {386, 38, 309, 377, 59, 277}
    {0, 2, 42, 400, 404, 60}
    {48, 482, 393, 80, 116, 407}
    {483, 136, 431, 35, 344, 381}
    ...

Gördüğünüz gibi, ``sayı_üret()`` fonksiyonunu kullanarak, her biri `6` öğeden
oluşan `100` adet sayı listesi elde ettik. Biz yukarıda bu fonksiyonu
parametresiz olarak çalıştırdığımız için, Python `başlangıç`, `bitiş` ve `adet`
parametrelerinin öntanımlı değerlerini kullandı (sırasıyla `0`, `500` ve `6`).

İstersek biz fonksiyonumuzu farklı parametrelerle çağırabiliriz::
    
    print(sayı_üret(0, 100, 10))
    
Bu kodlar bize `0` ile `100` arasından `10` adet rastgele sayı seçer::
    
    {3, 4, 9, 11, 13, 47, 50, 53, 54, 61}

Eğer çıktının küme parantezleri arasında görünmesini istemiyorsanız elbette
çıktıyı keyfinize göre biçimlendirebilirsiniz::
    
    print(*sayı_üret(100, 1500, 20), sep='-')
    
Bu şekilde, `100` ile `1500` arası sayılardan rastgele `20` adet seçip her bir
sayının arasına bir tane `-` işareti yerleştirdik::
    
    352-1251-1366-1381-1350-330-203-842-269-285-816
    -658-643-308-1174-152-594-522-1214-959    

Fonksiyonların Kapsamı ve global Deyimi
****************************************

Elimizde şöyle bir kod olduğunu düşünelim::

    x = 0
    
    def fonk():
        x = 1
        return x
        
Bu kodlarda, fonksiyonun dışında `x` adlı bir değişken var. Fonksiyonun içinde
de yine `x` adını taşıyan başka bir değişken var. Fonksiyonumuzun görevi bu `x`
değişkenini döndürmek.

Bu noktada size şöyle bir soru sormama izin verin: Acaba fonksiyon içinde
tanımladığımız `x` değişkeni, fonksiyon dışındaki `x` değişkeninin değerini
değiştiriyor mu? Bu sorunun cevabını şu kodlarla verelim::
    
    x = 0
    
    def fonk():
        x = 1
        return x
    
    print('fonksiyon içindeki x: ', fonk())
    print('fonksiyon dışındaki x: ', x)

Bu kodları çalıştırdığımızda şu çıktıyı alacağız::
    
    fonksiyon içindeki x:  1
    fonksiyon dışındaki x:  0
    
Gördüğünüz gibi fonksiyon içindeki ve fonksiyon dışındaki aynı adlı değişkenler
birbirine karışmıyor. Bunun sebebi, Python'daki 'isim alanı' (*namespace*) adlı
bir kavramdır. 

Peki isim alanı ne demek? 

Python'da değişkenlerin, fonksiyonların ve daha sonra göreceğiniz gibi
sınıfların bir kapsamı vardır. Bu kapsama Python'da 'isim alanı' adı verilir.
Dolayısıyla Python'da her nesnenin, geçerli ve etkin olduğu bir isim alanı
bulunur. Örneğin yukarıdaki kodlarda fonksiyon dışındaki `x` değişkeni ana isim
alanında yer alan 'global' bir değişkendir. Fonksiyon içindeki `x` değişkeni ise
``fonk()`` değişkeninin isim alanı içinde yer alan 'lokal' bir değişkendir. Bu
iki değişken, adları aynı da olsa, birbirlerinden farklı iki nesnedir. 

Bir de şu örneklere bakalım::
        
    x = []
    print('x\'in ilk hali:', x)
    
    def değiştir():
        print('x\'i değiştiriyoruz...')
        x.append(1)
        return x
    
    değiştir()
    print('x\'in son hali: ', x)
    
Burada ise daha farklı bir durum söz konusu. Fonksiyon içinde ``append()``
metodunu kullanarak yaptığımız ekleme işlemi fonksiyon dışındaki listeyi de
etkiledi. Peki ama bu nasıl oluyor?

Python herhangi bir nesneye göndermede bulunduğumuzda, yani o nesnenin
değerini talep ettiğimizde aradığımız nesneyi ilk önce mevcut isim alanı içinde
arar. Eğer aranan nesneyi mevcut isim alanı içinde bulamazsa yukarıya doğru
bütün isim alanlarını tek tek kontrol eder. 

Birkaç örnek verelim::
        
    def fonk():
        print(x)
        
    fonk()
    
Tahmin edebileceğiniz gibi, bu kodlar şu hatayı verecektir::
    
    Traceback (most recent call last):
      File "deneme.py", line 4, in <module>
        fonk()
      File "deneme.py", line 2, in fonk
        print(x)
    NameError: global name 'x' is not defined 
    
Bu hatanın sebebi, `x` adlı bir değişkenin tanımlanmamış olmasıdır. Bu hatayı
gidermek için şöyle bir kod yazabiliriz::
    
    x = 0
    
    def fonk():
        print(x)
        
    fonk()    
    
Bu kod global alandaki `x` değişkeninin değerini verecektir. 

Yukarıdaki örnekte, biz ``print()`` ile `x`'in değerini sorguladığımızda Python
öncelikle ``fonk()`` adlı fonksiyonun isim alanına baktı. Orada `x`'i
bulamayınca bu kez global alana yönelip, orada bulduğu `x`'in değerini yazdırdı.

Bu durumu daha net anlayabilmek için şu kodları inceleyelim::
    
    x = 0
    
    def fonk():
        x = 10
        print(x)
        
    fonk()
    print(x)
    
Bu kodları çalıştırdığımızda `10` çıktısını alırız. Çünkü Python, dediğimiz
gibi, öncelikle mevcut isim alanını kontrol ediyor. `x` değişkenini mevcut isim
alanında bulduğu için de global alana bakmasına gerek kalmıyor.

Yalnız burada dikkat etmemiz gereken bazı şeyler var. 

Dediğimiz gibi, global isim alanındaki nesnelerin değerini lokal isim
alanlarından sorgulayabiliyoruz. Ancak istediğimiz şey global isim alanındaki
nesnelerin değerini değiştirmekse bazı kavramlar arasındaki farkları iyi
anlamamız gerekiyor.

Python'da bir nesnenin değerini değiştirmekle, o nesneyi yeniden tanımlamak
farklı kavramlardır. 

**Eğer bir nesne değiştirilebilir bir nesne ise**, o nesnenin değerini, lokal
isim alanlarından değiştirebilirsiniz::
    
    x = set()

    def fonk():
        x.add(10)
        return x
        
    print(fonk())

**Ama eğer bir nesne değiştirilemez bir nesne ise**, o nesnenin değerini zaten
normalde de değiştiremezsiniz. Değiştirmiş gibi yapmak için ise o nesneyi
yeniden tanımlamanız gerektiğini biliyorsunuz::
    
    >>> isim = 'Fırat'
    >>> isim += ' Özgül'
    >>> print(isim)
    
    Fırat Özgül
    
Burada yaptığımız şey, karakter dizisinin değerini değiştirmekten ziyade bu
karakter dizisini yeniden tanımlamaktır. Çünkü bildiğiniz gibi karakter dizileri
değiştirilemeyen veri tipleridir.

İşte karakter dizileri gibi değiştirilemeyen nesneleri, lokal isim alanlarında
değiştiremeyeceğiniz gibi, yeniden tanımlayamazsınız da...

::

    isim = 'Fırat'
    
    def fonk():
        isim += ' Özgül'
        return isim
        
    print(fonk())
    
Bu kodları çalıştırdığınızda Python size bir hata mesajı gösterecektir.

Aynı durum değiştirilebilir nesneler için de geçerlidir::
    
    isim_listesi = []
    
    def fonk():
        isim_listesi += ['Fırat Özgül', 'Orçun Kunek']
        return isim_listesi
        
    print(fonk())
    
Değiştirilebilen bir veri tipi olan listeleri, fonksiyon içinde yeniden
tanımlayamazsınız. Ancak tabii isterseniz listeleri değişikliğe
uğratabilirsiniz::
    
    isim_listesi = []
    
    def fonk():
        isim_listesi.extend(['Fırat Özgül', 'Orçun Kunek'])
        return isim_listesi
        
    print(fonk())

Bu kodlar düzgün bir şekilde çalışıp, fonksiyon dışındaki `isim_listesi` adlı
listeyi değişikliğe uğratacaktır. Ancak şu kodlar hata verecektir::
    
    isim_listesi = []
    
    def fonk():
        isim_listesi += ['Fırat Özgül', 'Orçun Kunek']
        return isim_listesi
        
    print(fonk())
    
İşte Python programlama dili bu tür durumlar için çözüm olacak bir araç sunar
bize. Bu aracın adı `global`.

Gelin isterseniz bu `global` adlı deyimin nasıl kullanılacağına bakalım önce...

Şu kodların hata vereceğini biliyorsunuz::
    
    isim = 'Fırat'
    
    def fonk():
        isim += ' Özgül'
        return isim
        
    print(fonk())
    
Ama bu kodlara şöyle bir ekleme yaparsanız işler değişir::
    
    isim = 'Fırat'
    
    def fonk():
        global isim
        isim += ' Özgül'
        return isim
        
    print(fonk())
    
Burada ``fonk()`` adlı fonksiyonun ilk satırında şöyle bir kod görüyoruz::
    
    global isim
    
İşte bu satır, `isim` adlı değişkenin global alana taşınmasını sağlıyor. Böylece
global alanda bulunan `isim` adlı değişkeni değişikliğe uğratabiliyoruz. 

`global` deyimi her ne kadar ilk bakışta çok faydalı bir araçmış gibi görünse de
aslında programlarımızda genellikle bu deyimi kullanmaktan kaçınmamız iyi bir
fikir olacaktır. Çünkü bu deyim aslında global alanı kirletmemize neden oluyor.
Global değişkenlerin lokal isim alanlarında değişikliğe uğratılması, eğer
dikkatsiz davranırsanız programlarınızın hatalı çalışmasına yol açabilir. 