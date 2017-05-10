.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

*******************************************
Nesne Tabanlı Programlama (Devamı)
*******************************************

Bu bölümde de, temellerini geçen derslerimizde attığımız nesne tabanlı
programlama konusunu incelemeye devam edeceğiz. Bu bölümde uygulamaya yönelik
bazı örnekler yapmanın yanısıra, nesne tabanlı programlamaya ilişkin bazı teorik
bilgiler de vereceğiz.

Nesneler
**********

Geçen bölümlerden birinde sınıfları tanımlarken, bunların, nesne üretmemizi
sağlayan bir veri tipi olduğuna dair muğlak bir laf etmiştik. İşte bu başlık
altında, o tanım içinde geçen ve nesne tabanlı programlamanın temelini oluşturan
'nesne' kavramı üzerine eğileceğiz.

Nesne Nedir?
***************

Programlamaya ilişkin kavramlar içinde, özellikle programlamaya yeni
başlayanların kafasını en fazla karıştıran kavram nedir diye sorsak, herhalde
alacağımız cevap 'nesne' olur. Hakikaten, sağda solda sürekli duyduğumuz bu
'nesne' denen şey, öteden beri yazılım geliştirici adaylarının zihnini
karıştırır durur.

Aslında 'nesne' (*object*) dedikleri, ilk bakışta uyandırdığı izlenimin aksine,
anlaması zor, gizemli bir kavram değildir. Dolayısıyla, nesne kavramına ilişkin
olarak öğrenmemiz gereken ilk şey, bunun abartılacak veya korkulacak bir şey
olmadığıdır. Peki ama tam olarak nedir bu nesne dedikleri?

Kabaca, Python'da belli birtakım metotlara ve/veya niteliklere sahip olan
öğelere nesne adı verilir. Yani 'nesne' kelimesi, içinde birtakım metot ve/veya
nitelikler barındıran öğeleri tanımlamak için kullanılan bir tabirden, basit bir
isimlendirmeden ibarettir.

Peki bir nesne oluşturmak için acaba ne yapmamız gerekiyor?

Hatırlarsanız, geçen bölümde, sınıfların nesne üretmemizi sağlayan veri tipleri
olduğunu söylemiştik. O halde gelin minik bir nesne üretelim::
    
    class Sınıf():
        pass
        
    sınıf = Sınıf()
    
İşte bu kodlardaki ``sınıf = Sınıf()`` komutu ile bir nesne üretmiş olduk.
Nesnemizin adı da 'sınıf'. Teknik olarak ifade edersek, `sınıf` örneği,
``Sınıf()`` adlı sınıfın bütün nitelik ve metotlarını bünyesinde barındıran bir
nesnedir. Mesela yukarıdaki kodların `sınıf.py` adlı bir dosyada bulunduğunu
varsayarak şöyle bir deneme yapalım::
    
    >>> import sınıf
    >>> snf = sınıf.Sınıf()
    
Bu şekilde, kodları içeren modülü içe aktarmış ve modül içindeki ``Sınıf()``
adlı sınıfı `snf` adı ile örneklemiş olduk. Yani yukarıdaki kodlar yardımıyla
`snf` adlı bir nesne oluşturduk. Bakalım bu nesne hangi nitelik ve/veya
metotlara sahipmiş::
    
    >>> dir(snf)
    
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
     '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
     '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
     
Gördüğünüz gibi, biz boş bir sınıf tanımlamış olsak da, `snf` nesnesi öntanımlı
olarak yine de bazı nitelik ve metotlara sahip. İşte Python'da, yukarıdaki gibi
birtakım nitelik ve metotlara sahip olan bu tür öğelere 'nesne' adı veriyoruz. 

Bir de isterseniz yukarıdaki gibi boş bir sınıf tanımlamak yerine, sınıfımız
içinde kendimiz birtakım nitelik ve metotlar tanımlamayı da deneyelim::
    
    class Sınıf():
        sınıf_niteliği = 'sınıf niteliği'
        
        def __init__(self):
            self.örnek_niteliği = 'örnek niteliği'
        
        def örnek_metodu(self):
            print('örnek metodu')
            
        @classmethod
        def sınıf_metodu(cls):
            print('sınıf metodu')
            
        @staticmethod
        def statik_metot():
            print('statik metot')
            
Şimdi nesne içeriğini tekrar kontrol edelim::
    
    >>> import sınıf
    >>> snf = sınıf.Sınıf()
    >>> dir(snf)
    
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
     '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
     '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
     'statik_metot', 'sınıf_metodu', 'sınıf_niteliği', 
     'örnek_metodu', 'örnek_niteliği']
     
Gördüğünüz gibi, kendi tanımladığımız nitelik ve metotlar da `snf` adlı nesne
içine eklenmiş...

İşte `snf` adlı sınıf örneğinin, yukarıda gösterilen birtakım durum ve
davranışlara sahip olmasından yola çıkarak, `snf` örneğinin bir nesne olduğunu
söylüyoruz.

Yukarıdaki açıklamaların, 'nesne' kavramı hakkında en azından bir fikir sahibi
olmanızı sağladığını zannediyorum. Gördüğünüz gibi, nesne denen şey aslında
basit bir isimlendirmeden ibarettir: Python'da belli bir
durumu/niteliği/metodu/davranışı olan elemanlara/öğelere nesne (*object*) adı
veriyoruz. Peki o zaman, nesne denen şey basit bir adlandırmadan ibaretse nesne
tabanlı programlamanın etrafında koparılan bunca yaygaranın sebebi nedir?

Nesne tabanlı programlamayı bu kadar özel ve önemli kılan şeyin ne olduğunu
anlamak için gelin nesnelere biraz daha yakından bakalım.

Basit Bir Oyun
****************

Gelin isterseniz nesne denen kavramı daha iyi anlayabilmek, bir nesneyi nesne
yapan metot ve nitelikler arasındaki ilişkiyi daha net bir şekilde kavrayabilmek
için, komut satırı üzerinde çalışan çok basit bir oyun tasarlayalım. Bu şekilde
hem eski bilgilerimizi tekrar etmiş oluruz, hem teorik bilgilerimizi uygulama
sahasına dökmüş oluruz, hem de yeni şeyler öğrenmiş oluruz. 

Oyunumuzun kodları şöyle::
    
    import time
    import random
    import sys
    
    class Oyuncu():
        def __init__(self, isim, can=5, enerji=100):
            self.isim = isim
            self.darbe = 0
            self.can = can
            self.enerji = enerji
            
        def mevcut_durumu_görüntüle(self):
            print('darbe: ', self.darbe)
            print('can: ', self.can)
            print('enerji: ', self.enerji)
                    
        def saldır(self, rakip):
            print('Bir saldırı gerçekleştirdiniz.')
            print('Saldırı sürüyor. Bekleyiniz.')
    
            for i in range(10):
                time.sleep(.3)
                print('.', end='', flush=True)
                
            sonuç = self.saldırı_sonucunu_hesapla()
            
            if sonuç == 0:
                print('\nSONUÇ: kazanan taraf yok')
                
            if sonuç == 1:
                print('\nSONUÇ: rakibinizi darbelediniz')
                self.darbele(rakip)
                    
            if sonuç == 2:
                print('\nSONUÇ: rakibinizden darbe aldınız')
                self.darbele(self)
         
        def saldırı_sonucunu_hesapla(self):
             return random.randint(0, 2)
             
        def kaç(self):
            print('Kaçılıyor...')
            for i in range(10):
                time.sleep(.3)
                print('\n', flush=True)
                
            print('Rakibiniz sizi yakaladı')
             
        def darbele(self, darbelenen):
            darbelenen.darbe += 1
            darbelenen.enerji -= 1
            if (darbelenen.darbe % 5) == 0:
                darbelenen.can -= 1
            if darbelenen.can < 1:
                darbelenen.enerji = 0
                print('Oyunu {} kazandı!'.format(self.isim))
                self.oyundan_çık()
            
        def oyundan_çık(self):
            print('Çıkılıyor...')
            sys.exit()
            
    ##################################
            
    # Oyuncular 
    siz = Oyuncu('Ahmet')
    rakip = Oyuncu('Mehmet')
    
    # Oyun başlangıcı
    while True:
        print('Şu anda rakibinizle karşı karşıyasınız.',
              'Yapmak istediğiniz hamle: ',
              'Saldır:  s',
              'Kaç:     k',
              'Çık:     q', sep='\n')
        
        hamle = input('\n> ')
        if hamle == 's':
            siz.saldır(rakip)
    
            print('Rakibinizin durumu')
            rakip.mevcut_durumu_görüntüle()
            
            print('Sizin durumunuz')
            siz.mevcut_durumu_görüntüle()
            
        if hamle == 'k':
            siz.kaç()
            
        if hamle == 'q':
            siz.oyundan_çık()

Komut satırı üzerinde çalışan basit bir oyundur bu. Dilerseniz bu kodları
incelemeye başlamadan önce, bir dosyaya kaydedip çalıştırın. Karşınıza şöyle bir
ekran gelecek::
    
    Şu anda rakibinizle karşı karşıyasınız.
    Yapmak istediğiniz hamle:
    Saldır:  s
    Kaç:     k
    Çık:     q
    
    >
    
Programımız bize burada üç farklı seçenek sunuyor. Eğer rakibimize saldırmak
istiyorsak klavyedeki 's' tuşuna; rakibimizden kaçmak istiyorsak klavyedeki 'k'
tuşuna; yok eğer oyundan çıkmak istiyorsak da klavyedeki 'q' tuşuna basacağız.
Tercihinizi belirleyip neler olduğunu inceleyin ve oyunu iyice tanımaya çalışın.

Oyunu iyice anlayıp tanıdıktan sonra oyun kodlarını incelemeye geçebiliriz.

Yukarıda ilk olarak `Oyuncu` adlı bir sınıf tanımladık::
    
    class Oyuncu():
        def __init__(self, isim, can=5, enerji=100):
            self.isim = isim
            self.darbe = 0
            self.can = can
            self.enerji = enerji
            
`class` kelimesinin sınıf tanımlamamızı sağlayan bir araç, `Oyuncu` kelimesinin
ise tanımladığımız sınıfın adı olduğunu biliyoruz. Bu satırın hemen ardından
gelen ``__init__()`` fonksiyonu, sınıfımız örneklendiğinde neler olacağını
tanımladığımız yerdir. Bu sınıfın, örnekleme sırasında hangi parametreleri
alacağını da ``__init__()`` fonksiyonu içinde belirliyoruz. Parametre listesinde
gördüğümüz ilk öğe, yani `self`, sınıfın o anki örneğini temsil ediyor.
Python'ın sözdizimi kuralları gereğince bu kelimeyi oraya yazmamız gerektiğini
biliyoruz.

Yukarıdaki fonksiyon, `self` dışında toplam üç parametre alıyor: `isim`, `can`
ve `enerji`. Bunlardan ilki, yani `isim` parametresinin öntanımlı bir değeri
yok. Dolayısıyla sınıfı çağırırken (yani örneklerken) bu parametrenin değerini
belirtmemiz gerekecek. Öteki iki parametre olan `can` ve `enerji` ise birtakım
öntanımlı değerlere sahip. Dolayısıyla sınıfı örneklendirirken bu parametrelere
farklı bir değer atamadığımız sürece, bu parametreler, listede belirtilen
değerleri taşıyacak.

Parametre olarak belirlediğimiz değerleri sınıf içinde kullanabilmek için,
bunları ``__init__()`` fonksiyonunun gövdesinde birer örnek niteliğine
dönüştürüyoruz::
    
    self.isim = isim
    self.darbe = 0
    self.can = can
    self.enerji = enerji    
    
Burada ilave olarak bir de değeri 0 olan `self.darbe` adlı bir değişken
tanımladık. Bu da sınıfımızın örnek niteliklerinden biri olup, ilgili oyuncu
(yani sınıfın o anki örneği) darbe aldıkça bunun değeri yükselecektir.

Gelin isterseniz bu aşamada sınıfımızı örnekleyerek neler olup bittiğini daha
net anlamaya çalışalım::
    
    class Oyuncu():
        def __init__(self, isim, can=5, enerji=100):
            self.isim = isim
            self.darbe = 0
            self.can = can
            self.enerji = enerji
    
    #Sınıfımızı örnekliyoruz
    oyuncu = Oyuncu('Ahmet')

Burada ``oyuncu = Oyuncu('Ahmet')`` komutunu verdiğimiz anda ``__init__()``
fonksiyonu çalışmaya başlıyor ve `oyuncu` adlı nesne için sırasıyla şu
değişkenleri oluşturuyor::
    
    isim = 'Ahmet'
    darbe = 0
    can = 5
    enerji = 100
    
Bu örnek niteliklerine nasıl ulaşabileceğinizi biliyorsunuz::

    print('İsim: ', oyuncu.isim)
    print('Darbe: ', oyuncu.darbe)
    print('Can: ', oyuncu.can)
    print('Enerji: ', oyuncu.enerji)    
    
Başta da söylediğimiz gibi, ``Oyuncu()`` sınıfını örnekleyerek meydana
getireceğiniz bütün sınıf örnekleri, yani nesneler, ``__init__()`` fonksiyonu
içinde tanımladığınız örnek niteliklerini taşıyacaktır::
    
    
    class Oyuncu():
        def __init__(self, isim, can=5, enerji=100):
            self.isim = isim
            self.darbe = 0
            self.can = can
            self.enerji = enerji
            
    oyuncu1 = Oyuncu('Ahmet')
    oyuncu2 = Oyuncu('Mehmet')
    oyuncu3 = Oyuncu('Veli')
    oyuncu4 = Oyuncu('Ayşe')
    
Burada `oyuncu1`, `oyuncu2`, `oyuncu3` ve `oyuncu4` olmak üzere dört farklı
nesne oluşturduk. Bu nesnelerin hangi niteliklere sahip olacağını ise
``Oyuncu()`` sınıfının tanımı içinde belirttik. Yani sınıfımız tıpkı bir fabrika
gibi çalışarak, bizim için, aynı nitelikleri taşıyan dört farklı nesne üretti.

İşte nesne tabanlı programlamanın özünü oluşturan 'nesne' budur. Bir nesnenin
hangi niteliklere sahip olacağını belirleyen veri tipine sınıf (*class*) derken,
o sınıfın ortaya çıkardığı ürüne ise nesne (*object*) adı veriyoruz. Bunu şuna
benzetebilirsiniz: Eğer 'İnsan' bir sınıfsa, 'Mahmut' bu sınıfın bir örneğidir.
Dolayısıyla Mahmut, İnsan sınıfından türemiş bir nesnedir. Aynı şekilde eğer
'Köpek' bir sınıfsa, 'Karabaş' da bu sınıfın bir örneğidir. Yani Karabaş,
Köpek sınıfından türemiş bir nesnedir. Mahmut'un hangi özelliklere sahip
olacağını İnsan sınıfının nasıl tanımlandığı, Karabaş'ın hangi özelliklere
sahip olacağını ise Köpek sınıfının nasıl tanımlandığı belirler. İşte aynı
bunun gibi, ``Oyuncu()`` sınıfından türeyen nesnelerin hangi özelliklere sahip
olacağını da ``Oyuncu()`` sınıfının nasıl tanımlandığı belirler.

Kodlarımızı incelemeye devam edelim...

::
               
    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)

Burada ``mevcut_durumu_görüntüle()`` adlı bir örnek metodu tanımladık. Örnek
metotlarının ilk parametresinin her zaman `self` olması gerektiğini biliyoruz.

Tanımladığımız örnek metodunun görevi, ``Oyuncu()`` sınıfından oluşturduğumuz
nesnelerin (yani örneklerin) o anki `darbe`, `can` ve `enerji` durumlarını
görüntülemek. Birer örnek niteliği olan `darbe`, `can` ve `enerji`
değişkenlerine `self` aracılığıyla eriştiğimize özellikle dikkat ediyoruz.

Gelelim sınıfımızın önemli örnek metotlarından biri olan ``saldır()``
fonksiyonunu incelemeye::

    def saldır(self, rakip):
        print('Bir saldırı gerçekleştirdiniz.')
        print('Saldırı sürüyor. Bekleyiniz.')

        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
            
        sonuç = self.saldırı_sonucunu_hesapla()
        
        if sonuç == 0:
            print('\nSONUÇ: kazanan taraf yok')
            
        if sonuç == 1:
            print('\nSONUÇ: rakibinizi darbelediniz')
            self.darbele(rakip)
                
        if sonuç == 2:
            print('\nSONUÇ: rakibinizden darbe aldınız')
            self.darbele(self)
            
Bu fonksiyon, `self` dışında tek bir parametre alıyor. Fonksiyonu çalıştırırken
kullanacağımız `rakip` parametresi, saldırının kime karşı (yani sınıf
örneklerinden hangisine karşı) düzenleneceğini belirleyecek.

Fonksiyon gövdesinde ilk olarak şöyle bir kısım görüyoruz::
    
    print('Bir saldırı gerçekleştirdiniz.')
    print('Saldırı sürüyor. Bekleyiniz.')
    
    for i in range(10):
        time.sleep(.3)
        print('.', end='', flush=True)            

Burada saldırının gerçekleştiğine dair kullanıcıyı bilgilendirdikten sonra şöyle 
bir kod parçası yazdık::
    
    for i in range(10):
        time.sleep(.3)
        print('.', end='', flush=True)   
    
Bu kodlarda `time` adlı bir standart kütüphane modülünün ``sleep()`` adlı bir
metodundan yararlandığımızı görüyorsunuz. Elbette bu modülü kullanabilmek için
öncelikle bu modülü içe aktarmış olmamız gerekiyor. Bu işlemi dosyanın en
başında ``import time`` satırı yardımıyla gerçekleştirdiğimizi görebilirsiniz.

Yukarıdaki satırlar, 300'er milisaniye aralıklarla, yan yana nokta işaretleri
yerleştirecektir. Dilerseniz etkileşimli kabukta bu kodları şu şekilde test
edebilirsiniz::
    
    >>> import time
    >>> for i in range(10):
    ...     time.sleep(.3)
    ...     print('.', end='', flush=True)
    
``print()`` fonksiyonu içinde kullandığımız `end` ve `flush` parametrelerinin ne
olduğunu ve ne işe yaradığını ilk derslerimizden hatırlıyor olmalısınız. Eğer
hatırlamıyorsanız, bu parametreleri tek tek kodlardan çıkarıp, bu kodları bir de
öyle çalıştırın. Sonucun ne olduğunu takip ederek, `end` ve `flush`
parametrelerinin görevini daha iyi anlayabilirsiniz.
    
Bu kodların ardından şöyle bir satır yazdık::
    
    sonuç = self.saldırı_sonucunu_hesapla()
    
Burada, ``saldırı_sonucunu_hesapla()`` adlı bir örnek metodunu çağırdığımızı
görüyorsunuz::
    
    def saldırı_sonucunu_hesapla(self):
         return random.randint(0, 2)  
         
Biraz önce `time` adlı bir standart kütüphane modülünü kullanmıştık. Şimdi ise
`random` adlı başka bir standart kütüphane modülünü kullanıyoruz. Elbette bu
modülü de kullanabilmek için öncelikle bu modülü ``import random`` komutuyla içe
aktarmış olmamız gerekiyor. Bu zorunluluğu da, tıpkı `time` modülünde olduğu
gibi, dosyanın en başında yerine getirmiştik.

Yukarıda `random` modülünü, 0 ile 2 arası rastgele sayılar üretmek için
kullandık. ``random.randint(0, 2)`` komutu her çalışışında 0, 1 ve 2
sayılarından birini rastgele üretecektir. Buradan elde ettiğimiz sonucu `sonuç`
adlı bir değişkene atayarak ``saldır()`` fonksiyonu içinde şu şekilde
kullanıyoruz::
    
    sonuç = self.saldırı_sonucunu_hesapla()
    
    if sonuç == 0:
        print('\nSONUÇ: kazanan taraf yok')
        
    if sonuç == 1:
        print('\nSONUÇ: rakibinizi darbelediniz')
        self.darbele(rakip)
            
    if sonuç == 2:
        print('\nSONUÇ: rakibinizden darbe aldınız')
        self.darbele(self)
    
Eğer ``randint()`` metodu 0 sayısını üretirse, rakibimize karşı
gerçekleştirdiğimiz saldırının sonuçsuz kaldığına hükmediyoruz::
    
    if sonuç == 0:
        print('\nSONUÇ: kazanan taraf yok')
            
Eğer ``randint()`` metodu 1 sayısını üretirse, rakibimizi başarıyla
darbelediğimize, 2 sayısını üretirse de rakibimiz tarafından darbelendiğimize
hükmediyoruz::

    if sonuç == 1:
        print('\nSONUÇ: rakibinizi darbelediniz')
        self.darbele(rakip)
            
    if sonuç == 2:
        print('\nSONUÇ: rakibinizden darbe aldınız')
        self.darbele(self)
        
Saldırı sonucunda rakibimizi darbelediğimizde ve rakibimizden darbe yediğimizde
``darbele()`` adlı bir başka örnek metodunu çağırdığımızı da gözden
kaçırmayın. 

Bu arada, örnek metotlarına da `self` öneki ile eriştiğimize dikkatinizi çekmek
isterim. Ayrıca her ne kadar örnek metotlarını tanımlarken parantez listesi
içinde `self` kelimesini belirtsek de, bu metotları çağırırken bunları argüman
olarak kullanmadığımıza da özellikle dikkat etmelisiniz. Yani biz bu metotları
şöyle tanımlıyoruz::
    
    def saldırı_sonucunu_hesapla(self):
         return random.randint(0, 2) 
                             
Burada parametre listesinde `self`'i görüyoruz. Ama bu fonksiyonları çağırırken
parantez içinde bu `self`'i kullanmıyoruz::
    
    self.saldırı_sonucunu_hesapla()
    
`self`'i parantez içinde bir argüman olarak kullanmak yerine, bu kelimeyi
fonksiyon adının başına bir önek olarak takıyoruz.

Ne diyorduk? Evet, ``saldır()`` fonksiyonu içinde ``darbele()`` adlı bir
fonksiyona atıfta bulunduk. Yani saldırı sonucunda rakibimizi darbelediğimizde
ve rakibimizden darbe yediğimizde ``darbele()`` adlı bir başka örnek
metodunu çağırdık::
             
    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
            
Bu fonksiyon içinde, herhangi bir darbe alma durumunda oyuncunun `darbe`, `can`
ve `enerji` miktarlarında meydana gelecek değişiklikleri tanımlıyoruz. 

Buna göre herhangi bir darbe alma durumunda aşağıdaki işlemler
gerçekleştirilecek:

Darbelenen oyuncunun `darbe` değeri 1 birim artacak::
    
    darbelenen.darbe += 1
    
`enerji` değeri 1 birim azalacak::
    
    darbelenen.enerji -= 1
    
Darbelenen oyuncu her 5 darbede 1 `can` kaybedecek::
            
    if (darbelenen.darbe % 5) == 0:
        darbelenen.can -= 1
        
Burada her 5 darbede 1 `can` kaybetme kriterini nasıl belirlediğimize dikkat
edin. Bildiğiniz gibi, oyuncu darbe yedikçe `darbe` değişkeninin değeri artıyor.
Bu değer 5 sayısına ulaştığında, ``5 % 5`` işleminin sonucu 0 olacaktır. Yani bu
sayı 5'e bölündüğünde bölme işleminden kalan değer 0 olacaktır. 5'in tüm katları
için (5, 10, 15, 20 gibi...) bu durum geçerlidir. Eğer `darbe` değişkenin
ulaştığı değer 5'in katı değilse, bu sayı 5'e tam bölünmediği için, bölmeden
kalan değer 0 dışında bir sayı olur. Dolayısıyla `darbe` değerinin ulaştığı
sayının 5'e bölünmesinden kalan değerin 0 olup olmadığını kontrol ederek
oyuncunun 5 darbede 1 `can` kaybetmesini sağlayabiliyoruz.
        
Oyuncunun `can` değeri 1'in altına düştüğünde ise `enerji` değeri 0'a inecek ve
oyunu kimin kazandığı ilan edildikten sonra oyun kapatılacak::
    
    if darbelenen.can < 1:
        darbelenen.enerji = 0
        print('Oyunu {} kazandı!'.format(self.isim))
        self.oyundan_çık()
        
Burada ``oyundan_çık()`` adlı bir örnek metoduna daha atıfta bulunduk::
    
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()
        
Gayet basit bir fonksiyon. Herhangi bir şekilde oyundan çıkmak gerektiğinde
`sys` modülünün ``exit()`` fonksiyonunu kullanarak oyunu terk ediyoruz.

İlerlemeden önce, ``darbele()`` fonksiyonunu kullandığımız kısma tekrar
bakalım::
    
    sonuç = self.saldırı_sonucunu_hesapla()
    
    if sonuç == 0:
        print('\nSONUÇ: kazanan taraf yok')
        
    if sonuç == 1:
        print('\nSONUÇ: rakibinizi darbelediniz')
        self.darbele(rakip)
            
    if sonuç == 2:
        print('\nSONUÇ: rakibinizden darbe aldınız')
        self.darbele(self)

Bildiğiniz gibi, ``darbele()`` fonksiyonu, `self` dışında 1 adet parametre daha
alıyor. Bu parametre, darbeyi hangi oyuncunun alacağını gösteriyor. Yani darbeyi
alan oyuncu biz miyiz yoksa rakibimiz mi? İşte bunu tespit etmek için
`darbelenen` adlı bir parametre belirledik. Gördüğünüz gibi, ``darbele()``
fonksiyonu ``saldır()`` adlı başka bir fonksiyonun içinden çağrılıyor.
``saldır()`` fonksiyonu da `rakip` adlı bir parametre alıyor. İşte darbe alan
oyuncunun can ve enerji değerlerini yenilemek istediğimizde bu parametreyi,
``darbele()`` fonksiyonuna gönderiyoruz::
    
    self.darbele(rakip)
    
Burada darbelenen oyuncu karşı taraf. Yani rakibimiz darbe yemiş. Eğer
darbelenen kişi kendimizsek, kendimize atıfta bulunmak için de `self`
parametresini kullanıyoruz::
    
    self.darbele(self)
    
Pek çok kez söylediğimiz gibi, `self` kelimesi mevcut sınıf örneğini temsil
eder. Dolayısıyla kendimize atıfta bulunmak istediğimiz durumlarda, yukarıda
olduğu gibi `self`'i kullanabiliriz.

Eğer arzu ederseniz, ``darbele()`` fonksiyonunu şöyle de yazabilirsiniz::
    
    def darbele(self):
        self.darbe += 1
        self.enerji -= 1
        if (self.darbe % 5) == 0:
            self.can -= 1
        if self.can < 1:
            self.enerji = 0
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
            
Burada `darbelenen` parametresini iptal ettik. Kimin durumunun yenileceğini
`self`'in kim olduğu belirleyecek::
    
    if sonuç == 1:
        print('\nSONUÇ: rakibinizi darbelediniz')
        rakip.darbele()

    if sonuç == 2:
        print('\nSONUÇ: rakibinizden darbe aldınız')
        self.darbele()
        
Gördüğünüz gibi, eğer rakibi darbeleyip onun can ve enerji durumunu yenilemek
istiyorsak, ilgili fonksiyonu ``rakip.darbele()`` şeklinde çağırıyoruz.
Kendimizin durumunu yenilemek istediğimizde ise ``self.darbele()`` komutunu
kullanıyoruz.

Sınıfımızı tanımladığımıza göre artık bu sınıfı nasıl kullanacağımızı incelemeye
geçebiliriz::
    
    siz = Oyuncu('Ahmet')
    rakip = Oyuncu('Mehmet')
            
Burada öncelikle ``Oyuncu()`` sınıfı için iki farklı nesne/örnek oluşturuyoruz::
    
    siz = Oyuncu('Ahmet')
    rakip = Oyuncu('Mehmet')
    
Bu iki nesne, ``Oyuncu()`` sınıfının bütün niteliklerini taşıyor. Nesneleri
oluştururken, zorunlu argüman olan `isim` değerini mutlaka belirtmemiz
gerektiğini unutmuyoruz.

Daha sonra bir ``while`` döngüsü içinde, oyunumuzun kullanıcı tarafından
görüntülenecek kısmını kodluyoruz::
    
    while True:
        print('Şu anda rakibinizle karşı karşıyasınız.',
              'Yapmak istediğiniz hamle: ',
              'Saldır:  s',
              'Kaç:     k',
              'Çık:     q', sep='\n')
        
        hamle = input('\n> ')
        if hamle == 's':
            siz.saldır(rakip)
    
            print('Rakibinizin durumu')
            rakip.mevcut_durumu_görüntüle()
            
            print('Sizin durumunuz')
            siz.mevcut_durumu_görüntüle()
            
        if hamle == 'k':
            siz.kaç()
            
        if hamle == 'q':
            siz.oyundan_çık()
            
Oyunun nasıl oynanacağı konusunda kullanıcılarımızı bilgilendiriyoruz::
    
    print('Şu anda rakibinizle karşı karşıyasınız.',
          'Yapmak istediğiniz hamle: ',
          'Saldır:  s',
          'Kaç:     k',
          'Çık:     q', sep='\n')
          
Kullanıcılarımızın klavyede hangi tuşa bastığını şu şekilde alıyoruz::
    
    hamle = input('\n> ')
    
Eğer kullanıcı 's' tuşuna basarsa rakibimize saldırıyoruz::
    
    if hamle == 's':
        siz.saldır(rakip)
        
Saldırının ardından hem kendi durumumuzu hem de rakibimizin durumunu
görüntülüyoruz::
    
    print('Rakibinizin durumu')
    rakip.mevcut_durumu_görüntüle()
    
    print('Sizin durumunuz')
    siz.mevcut_durumu_görüntüle()
        
Eğer kullanıcı 'k' tuşuna basarsa::
        
    if hamle == 'k':
        ...
    
...sınıf içinde tanımladığımız ``kaç()`` metodunu çalıştırıyoruz::
    
    def kaç(self):
        print('Kaçılıyor...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
            
        print('Rakibiniz sizi yakaladı')
        
Burada 300'er milisaniyelik aralıklarla `'\\n'` kaçış dizisini kullanarak bir
alt satıra geçiyoruz.

Kullanıcının 'q' tuşuna basması halinde ise oyundan derhal çıkıyoruz::
    
    if hamle == 'q':
        siz.oyundan_çık()
        
Bu örnek kodlar bize sınıflar ve nesneler hakkında epey bilgi verdi. Ayrıca bu
kodlar sayesinde önceki bilgilerimizi de pekiştirmiş olduk.

Her Şey Bir Nesnedir
**********************

Belki sağda solda şu sözü duymuşsunuzdur: Python'da her şey bir nesnedir.
Gerçekten de (`if`, `def`, `and`, `or` gibi deyim ve işleçler hariç) Python'da
her şey bir nesnedir. Peki her şeyin nesne olması tam olarak ne anlama geliyor?

Hatırlarsanız nesnenin ne olduğunu tanımlarken, belli bir durumda bulunan ve
belli birtakım davranışları olan öğelere nesne adı verildiğini söylemiştik. İşte
Python'daki her şey, bu tanım doğrultusunda bir nesnedir. 

Mesela, aşağıdaki komutu verdiğimiz anda bir nesne oluşturmuş oluyoruz::
    
    >>> 'istihza'
    
`'istihza'` karakter dizisi, `str` adlı sınıfın...

::
    
    >>> type('istihza')
    
    <class 'str'>
    
...bütün özelliklerini taşıyan bir nesnedir::
    
    >>> dir('istihza')
    
    ['__add__', '__class__', '__contains__', '__delattr__', 
     '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
     '__getattribute__', '__getitem__', '__getnewargs__', 
     '__gt__', '__hash__', '__init__', '__iter__', '__le__', 
     '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
     '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
     '__str__', '__subclasshook__', 'capitalize', 'casefold', 
     'center', 'count', 'encode', 'endswith', 'expandtabs', 
     'find', 'format', 'format_map', 'index', 'isalnum', 
     'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 
     'islower', 'isnumeric', 'isprintable', 'isspace', 
     'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
     'maketrans', 'partition', 'replace', 'rfind', 'rindex', 
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
     'splitlines', 'startswith', 'strip', 'swapcase', 
     'title', 'translate', 'upper', 'zfill']
     
Aynı şekilde, ``['elma', 'armut']`` listesi de, `list` adlı sınıfın...

::
    
    >>> type(['elma', 'armut'])
    
    <class 'list'>    
    
...bütün özelliklerini taşıyan bir nesnedir::
    
    >>> dir(['elma', 'armut'])
    
    ['__add__', '__class__', '__contains__', '__delattr__', 
     '__delitem__', '__dir__', '__doc__', '__eq__', 
     '__format__', '__ge__', '__getattribute__', '__getitem__', 
     '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
     '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
     '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
     '__repr__', '__reversed__', '__rmul__', '__setattr__', 
     '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
     'append', 'clear', 'copy', 'count', 'extend', 'index', 
     'insert', 'pop', 'remove', 'reverse', 'sort']    
     
Hatta mesela 1 gibi alelade bir sayı bile, dış dünyayla iletişim kurmasını ve
dış dünyanın kendisiyle iletişim kurabilmesini sağlayan pek çok nitelik ve
metoda sahip bir nesnedir::
    
    >>> dir(1)
    
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', 
     '__class__', '__delattr__', '__dir__', '__divmod__', 
     '__doc__', '__eq__', '__float__', '__floor__', 
     '__floordiv__', '__format__', '__ge__', '__getattribute__', 
     '__getnewargs__', '__gt__', '__hash__', '__index__', 
     '__init__', '__int__', '__invert__', '__le__', '__lshift__', 
     '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', 
     '__new__', '__or__', '__pos__', '__pow__', '__radd__', 
     '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
     '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
     '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
     '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', 
     '__setattr__', '__sizeof__', '__str__', '__sub__', 
     '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
     'bit_length', 'conjugate', 'denominator', 'from_bytes', 
     'imag', 'numerator', 'real', 'to_bytes']
     
İşte konuya bu noktadan baktığımızda, Python'da her şey bir nesnedir. Yani
Python'daki her şeyle, sahip oldukları metotlar ve nitelikler aracılığıyla
etkileşebilirsiniz.

Python'ın bu özelliğini bilmek, muhatap olduğunuz programlama dilini ve onun
kabiliyetlerini tanımak açısından önemlidir. Python'da her şeyin bir nesne
olduğunu anladığınız anda, ``{'a': 0, 'b': 1}`` gibi bir kodla yalnızca basit
bir sözlük tanımlamadığınızı, bunun arkaplanında, bu sözlükle etkileşim
kurmanızı sağlayacak koca bir mekanizma bulunduğunu bilirsiniz.

Birinci Sınıf Öğeler
*********************

Tıpkı 'her şey bir nesnedir' sözü gibi, yine sağda solda sıklıkla
duyabileceğiniz bir söz de Python'da nesnelerin 'birinci sınıf öğeler'
olduğudur. Peki burada 'birinci sınıf' (*first class*) ifadesiyle kastedilen şey
tam olarak nedir?

Programlama dillerinde herhangi bir öğenin birinci sınıf bir öğe olması, o
öğenin, dil içindeki herhangi bir değer ile aynı kabiliyetlere sahip olması
anlamına gelir. 'Bunun birinci sınıf olmakla ne alakası var?' diye sorduğunuzu
duyar gibiyim... 

Şöyle bir cümle kurduğunuzu düşünün: 'Gelişmiş bir toplumda kadınlar birinci
sınıf vatandaşlardır.' Bu cümleden, bir toplumun gelişmiş sayılabilmesi için
kadınların erkeklerle eşit haklara sahip olması gerektiğini anlıyoruz. Yani
kadınların birinci sınıf vatandaşlar olması, erkeklerle eşit haklara sahip
olması anlamına geliyor. İşte tıpkı bunun gibi, Python'daki sınıf yapılarının
'birinci sınıf' öğeler olması, bu yapıların, dil içindeki öteki değerlerle aynı
özelliklere ve kabiliyetlere sahip olması demektir. Yani Python'daki sınıflar şu
özelliklere sahiptir:

    #. Başka bir fonksiyona veya sınıfa parametre olarak atanabilirler
    #. Bir fonksiyondan döndürülebilirler
    #. Bir değişkene atanabilirler

Yani, bir öğenin 'birinci sınıf' olması demek, dil içindeki başka öğelerle
yapabildiğiniz her şeyi o öğeyle de yapabilmeniz demektir. 

Durumu biraz daha netleştirebilmek için, konu hakkında Guido Van Rossum'un ne
dediğine bir bakalım:
       
    *Python'a ilişkin hedeflerimden bir tanesi de, bu dili, bütün nesneler
    "birinci sınıf" olacak şekilde tasarlamaktı. Bununla kastettiğim, dil içinde
    kendisine bir isim verilebilen bütün nesnelerin (örn. tam sayılar, karakter
    dizileri, fonksiyonlar, sınıflar, modüller, metotlar, vb.) eşit statüye
    sahip olmasıdır. Yani, bütün nesnelerin değişkenlere atanabilmesi,
    listelerin içine yerleştirilebilmesi, sözlükler içinde depolanabilmesi,
    argüman olarak atanabilmesi ve saire...*
    
    kaynak: http://python-history.blogspot.com.tr/2009/02/first-class-everything.html

Gelin bütün bu tanımları somutlaştıran birkaç örnek verelim.

Mesela ``Deneme()`` adlı basit bir sınıf tanımlayalım::
    
    class Deneme():
        def __init__(self):
            self.değer = 0
        def metot(self):
            self.metot_değeri = 1

Yukarıdaki tanımlara göre, bu sınıfın birinci sınıf bir nesne olabilmesi için
başka bir fonksiyona veya sınıfa parametre olarak atanabilmesi gerekiyor.
Bakalım acaba gerçekten öyle mi?

::
    
    print(Deneme())
    
Gördüğünüz gibi, gerçekten de sınıfımızı ``print()`` fonksiyonuna parametre
olarak atayabildik. 

Yine yukarıdaki tanıma göre birinci sınıf nesnelerin bir fonksiyondan
döndürülebilmesi gerekiyor::
    
    def fonksiyon():
        return Deneme()
        
    print(fonksiyon())
    
Bu testi de başarıyla geçtik. 

Son olarak, bir nesnenin birinci sınıf olabilmesi için bir değişkene
atanabilmesi gerekiyor::
    
    değişken = Deneme()
    
Gördüğünüz gibi, Python için bu da oldukça basit bir görev.
    
İlk bakışta bu özellikten pek etkilenmemiş olabilirsiniz... Şöyle bir düşününce,
aslında çok da önemli bir özellik değilmiş gibi gelebilir bu size. Ancak başka
programlama dillerinin; 

    - Öğelerin kullanımına ilişkin çeşitli kısıtlamalar koyduğunu, 
    - Yani öğeler arasında ayrım yaptığını, 
    - Değişkenlerle fonksiyonların ve fonksiyonlarla sınıfların aynı haklara
      sahip olmadığını,    
    - Mesela bir değişkeni veya herhangi bir değeri kullanabildiğiniz her yerde
      fonksiyon veya sınıf kullanamadığınızı,    
    - Yani fonksiyonların ve/veya sınıfların birinci sınıf öğeler olmadığını 
    
gördüğünüzde Python'daki bu esneklik daha bir anlam kazanacaktır.
 



    