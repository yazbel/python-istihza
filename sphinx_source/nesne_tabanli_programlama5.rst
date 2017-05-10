.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

*******************************************
Nesne Tabanlı Programlama (Devamı)
*******************************************
 
Nesne tabanlı programlamaya giriş yaparken, bu programlama yaklaşımının oldukça
geniş kapsamlı bir konu olduğunu söylemiştik. Bu bölümde de bu geniş kapsamlı
konunun ileri düzey yönlerini ele almaya devam edeceğiz.

Ayrıca bu bölümü bitirdikten sonra, nesne tabanlı programlamanın yoğun bir
şekilde kullanıldığı 'grafik arayüz tasarlama' konusundan da söz edebileceğiz.
Böylece, bu zamana kadar gördüğümüz komut satırı uygulamalarından sonra, bu
bölümle birlikte ilk kez düğmeli-menülü modern arayüzleri tanımaya da
başlayacağız. Üstelik grafik arayüzlü programlar üzerinde çalışmak, nesne
tabanlı programlamanın özellikle karmaşık yönlerini çok daha kolay ve net bir
şekilde anlamamızı da sağlayacak.

Miras Alma
*************

Bu bölümde, yine nesne tabanlı programlamaya ait bir kavram olan 'miras alma'dan
söz edeceğiz. Bütün ayrıntılarıyla ele alacağımız miras alma, nesne tabanlı
programlamanın en önemli konularından birisidir. Hatta nesne tabanlı
programlamayı faydalı bir programlama yaklaşımı haline getiren özelliklerin
başında miras alma gelir dersek çok da abartmış olmayız. Ayrıca miras alma
konusu, komut satırında çalışan programların yanısıra grafik arayüzlü programlar
da yazabilmemizin önündeki son engel olacak. Bu bölümü tamamladıktan sonra,
grafik arayüzlü programlar yazmamızı sağlayacak özel modüllerin belgelerinden
yararlanabilmeye ve grafik arayüzlü programların kodlarını okuyup anlamaya
başlayabileceğiz.

Daha önce de söylediğimiz gibi, Python programlama dilinin temel felsefesi, bir
kez yazılan kodları en verimli şekilde tekrar tekrar kullanabilmeye dayanır.
Genel olarak baktığımızda dilin hemen hemen bütün öğeleri bu amaca hizmet edecek
şekilde tasarlanmıştır. İşte bu başlık altında ele alacağımız 'miras alma'
kavramı da kodların tekrar tekrar kullanılabilmesi felsefesine katkı sunan bir
özelliktir.

İsterseniz miras alma konusunu anlatmaya basit bir örnekle başlayalım.

Diyelim ki bir oyun yazıyorsunuz. Bu oyun içinde askerler, işçiler, yöneticiler,
krallar, kraliçeler ve bunun gibi oyuncu türleri olacak. Bu oyuncuları ve 
kabiliyetlerini mesela şöyle tanımlayabilirsiniz::

    class Asker():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 100
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class İşçi():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 70
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Yönetici():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 20
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')

Burada asker, işçi ve yöneticinin her biri için ayrı bir sınıf tanımladık. Her
sınıfın bir ismi, rütbesi ve gücü var. Ayrıca her sınıf; hareket etme, puan
kazanma ve puan kaybetme gibi kabiliyetlere sahip.

Bu kodların `oyuncular.py` adlı bir dosyada bulunduğunu varsayarsak, mesela bir
asker oluşturmak için yukarıdaki kodları şöyle kullanabiliriz::
    
    >>> import oyuncular
    >>> asker1 = oyuncular.Asker('Mehmet', 'er')
    
``Asker()`` sınıfının `isim` ve `rütbe` parametrelerini belirtmek suretiyle bir
asker nesnesi oluşturduk. Tıpkı Python'da gördüğümüz başka nesneler gibi, bu
nesne de çeşitli nitelik ve metotlardan oluşuyor::
    
    >>> dir(asker1)
        
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
     '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
     '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'güç', 
     'hareket_et', 'isim', 'puan_kaybet', 'puan_kazan', 'rütbe']
     
Bu nitelik ve metotları asker nesnesi üzerine nasıl uygulayacağımızı
biliyorsunuz::
    
    >>> asker1.isim
    
    'Mehmet'
    
    >>> asker1.rütbe
    
    'er'
    
    >>> asker1.güç
    
    100
    
    >>> asker1.hareket_et()
    
    'hareket ediliyor...'
    
    >>> asker1.puan_kazan()
    
    'puan kazanıldı'
    
    >>> asker1.puan_kaybet()
    
    'puan kaybedildi'
    
Aynı şekilde öteki ``İşçi()`` ve ``Yönetici()`` sınıflarını da örnekleyip
kullanabiliriz. Bu konuda bir problem yok. Ancak yukarıdaki kodları
incelediğinizde, aynı kodların sürekli tekrarlandığını göreceksiniz. Gördüğünüz
gibi, aynı nitelik ve metotları her sınıf için yeniden tanımlıyoruz. Bu durumun
Python'ın mantalitesine aykırı olduğunu tahmin etmek hiç zor değil. Peki acaba
yukarıdaki kodları nasıl daha 'Pythonvari' hale getirebiliriz?

Bu noktada ilk olarak taban sınıflardan söz etmemiz gerekiyor.

Taban Sınıflar
*****************

Taban sınıflar (*base classes*) miras alma konusunun önemli kavramlarından
biridir. Dilerseniz taban sınıfın ne olduğu anlayabilmek için, yukarıda
verdiğimiz örneği temel alarak çok basit bir uygulama yapalım.

Öncelikle yukarıda verdiğimiz örneği tekrar önümüze alalım::
    
    class Asker():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 100
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class İşçi():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 70
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Yönetici():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 20
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')

Bu örnekte, ``Asker()``, ``İşçi()`` ve ``Yönetici()`` adlı sınıfların içeriğine
baktığımızda pek çok metot ve niteliğin aslında birbiriyle aynı olduğunu
görüyoruz. Gelin isterseniz bütün sınıflarda ortak olan bu nitelik ve metotları
tek bir sınıf altında toplayalım. 

``Asker()``, ``İşçi()`` ve ``Yönetici()`` sınıflarının, yazdığımız programdaki
oyuncuları temsil ettiğini düşünürsek, ortak nitelik ve metotları barındıran
sınıfımızı da ``Oyuncu()`` olarak adlandırmamız mantıksız olmayacaktır::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
        
İşte burada ``Oyuncu()`` adlı sınıf, bir 'taban sınıf' olarak adlandırılır.
Taban sınıf denen şey, birkaç farklı sınıfta ortak olan nitelik ve metotları
barındıran bir sınıf türüdür. İngilizcede *base class* olarak adlandırılan taban
sınıflar, ayrıca üst sınıf (*super class*) veya ebeveyn sınıf (*parent class*)
olarak da adlandırılır. Biz bu makalede taban sınıf ismini tercih edeceğiz.

Yukarıdaki ``Oyuncu()`` adlı taban sınıf da, ``İşçi()``, ``Asker()``,
``Yönetici()`` gibi sınıfların hepsinde ortak olarak bulunacak nitelik ve
metotları barındıracak. Öteki bütün sınıflar, ortak nitelik ve metotlarını her
defasında tek tek yeniden tanımlamak yerine, ``Oyuncu()`` adlı bu taban sınıftan
devralacak. Peki ama nasıl? İşte bunu anlamak için de 'alt sınıf' adlı bir
kavrama değinmemiz gerekiyor.

Alt Sınıflar
***************

Bir taban sınıftan türeyen bütün sınıflar, o taban sınıfın alt sınıflarıdır.
(*subclass*). Alt sınıflar, kendilerinden türedikleri taban sınıfların metot ve
niteliklerini miras yoluyla devralır. 

Anlattığımız bu soyut şeyleri anlamanın en kolay yolu somut bir örnek üzerinden
ilerlemektir. Mesela, biraz önce tanımladığımız ``Oyuncu()`` adlı taban sınıftan
bir alt sınıf türetelim::
    
    class Asker(Oyuncu):
        pass
        
Kodlarımız tam olarak şöyle görünüyor::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Asker(Oyuncu):
        pass
     
Burada ``Asker()`` sınıfını tanımlarken, bu sınıfın parantezleri içine
``Oyuncu()`` sınıfının adını yazdığımıza dikkat edin. İşte bu şekilde bir
sınıfın parantezleri içinde başka bir sınıfın adını belirtirsek, o sınıf,
parantez içinde belirttiğimiz sınıfın bir alt sınıfı olmuş olur. Yani mesela
yukarıdaki gibi ``Asker()`` sınıfının parantezleri arasına ``Oyuncu()``
sınıfının adını yazdığımızda, ``Asker()`` adlı sınıf; 

    #. ``Oyuncu()`` adlı sınıfı miras almış, 
    #. ``Oyuncu()`` adlı sınıfın bütün metot ve niteliklerini devralmış,
    #. ``Oyuncu()`` adlı sınıftan türemiş oluyor.

Bu sayede ``Oyuncu()`` sınıfında tanımlanan bütün nitelik ve metotlara
``Asker()`` sınıfından da erişebiliyoruz::
    
    >>> import oyuncular
    >>> asker1 = oyuncular.Asker('Ahmet', 'Er')
    >>> asker1.isim
    
    'Ahmet'
    
    >>> asker1.rütbe
    
    'Er'
    
    >>> asker1.güç
    
    0
    
    >>> asker1.puan_kazan()
    
    'puan kazanıldı'
    
Örnek olması açısından, ``Oyuncu()`` sınıfından türeyen (miras alan) birkaç alt
sınıf daha tanımlayalım::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Asker(Oyuncu):
        pass
        
    class İşçi(Oyuncu):
        pass
        
    class Yönetici(Oyuncu):
        pass
        
Tanımladığımız bu ``İşçi()`` ve ``Yönetici()`` sınıfları da tıpkı ``Asker()``
sınıfı gibi ``Oyuncu()`` adlı sınıftan miras aldığı için, ``Oyuncu()`` sınıfının
sahip olduğu tüm nitelik ve metotlara sahiptirler.

Buraya kadar anlattıklarımızı özetleyecek olursak, şu sınıf bir taban sınıftır::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
Bu taban sınıf, kendisinden türeyecek alt sınıfların ortak nitelik ve
metotlarını tanımlar.

Şu sınıflar ise, yukarıdaki taban sınıftan türeyen birer alt sınıftır::
    
    class Asker(Oyuncu):
        pass
        
    class İşçi(Oyuncu):
        pass
        
    class Yönetici(Oyuncu):
        pass
        
Bu alt sınıflar, ``Oyuncu()`` adlı taban sınıfın bütün nitelik ve metotlarını
miras yoluyla devralır. Yani ``Oyuncu()`` adlı taban/ebeveyn/üst sınıfın nitelik
ve metotlarına, ``Asker()``, ``İşçi()`` ve ``Yönetici()`` adlı alt sınıflardan
erişebiliriz::
    
    >>> asker1 = Asker('Ahmet', 'İstihkamcı')
    >>> işçi1 = İşçi('Mehmet', 'Usta')
    >>> yönetici1 = Yönetici('Selim', 'Müdür')
    >>> asker1.hareket_et()
    
    'hareket ediliyor...'
    
    >>> işçi1.puan_kaybet()
    
    'puan kaybedildi'
    
    >>> yönetici1.puan_kazan()
    
    'puan kazanıldı'

İşte bu mekanizmaya miras alma (*inheritance*) adı verilir. Miras alma
mekanizması, bir kez yazılan kodların farklı yerlerde kullanılabilmesini
sağlayan, bu bakımdan da programcıyı kod tekrarına düşmekten kurtaran oldukça
faydalı bir araçtır. İlerleyen sayfalarda miras alma mekanizmasının başka
faydalarını da göreceğiz.

Miras Alma Türleri
********************

Tahmin edebileceğiniz gibi, miras alma yalnızca bir sınıfın parantezleri arasına
başka bir sınıfı yazarak ilgili sınıfın bütün nitelik ve metotlarını kayıtsız
şartsız devralmaktan ibaret değildir. Bir sınıf, muhtemelen, miras aldığı
nitelik ve metotlar üzerinde birtakım değişiklikler de yapmak isteyecektir.
Esasında miras alma mekanizmasının işleyişi bakımından kabaca üç ihtimalden söz
edebiliriz:

#. Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa olduğu gibi
   devredilir.

#. Miras alınan sınıfın bazı nitelik ve metotları alt sınıfta yeniden
   tanımlanır.

#. Miras alınan sınıfın bazı nitelik ve metotları alt sınıfta değişikliğe
   uğratılır.

Bu ihtimallerden ilkini zaten görmüştük. Bir sınıfın parantezleri arasına başka
bir sınıfın adını yazdıktan sonra eğer alt sınıfta herhangi bir değişiklik
yapmazsak, taban sınıftaki nitelik ve metotlar olduğu gibi alt sınıflara
aktarılacaktır.

Mesela::
    
    class Asker(Oyuncu):
        pass

Burada ``Asker()`` sınıfı, miras aldığı ``Oyuncu()`` sınıfının sanki bir kopyası
gibidir. Dolayısıyla ``Oyuncu()`` sınıfının bütün nitelik ve metotlarına
``Asker()`` sınıfı altından da aynen erişebiliriz.

Yani yukarıdaki kod, ``Oyuncu()`` adlı sınıfın bütün nitelik ve metotlarının
``Asker()`` sınıfı tarafından miras alınmasını sağlar. Bu şekilde, ``Oyuncu()``
sınıfı içinde hangi metot veya nitelik nasıl tanımlanmışsa, ``Asker()`` sınıfına
da o şekilde devredilir.

Taban sınıfımızın şu şekilde tanımlandığını biliyoruz::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
        
Dolayısıyla bu taban sınıfta hangi nitelik ve metotlar hangi değerlere sahipse
aşağıdaki ``Asker()``, ``İşçi()`` ve ``Yönetici()`` sınıfları da o değerlere
sahip olacaktır::
    
    class Asker(Oyuncu):
        pass
        
    class İşçi(Oyuncu):
        pass
        
    class Yönetici(Oyuncu):
        pass

Ancak, dediğimiz gibi, miras almada tek seçenek bütün metot ve nitelikleri
olduğu gibi alt sınıflara aktarmak değildir. Zaten öyle olsaydı miras alma
mekanizmasının pek bir anlamı olmazdı. Biz miras aldığımız sınıflar üzerinde,
içinde bulunduğumuz durumun gerektirdiği birtakım değişiklikleri yapabilmeliyiz
ki bu mekanizmanın ilgi çekici bir yanı olsun.

Ayrıca eğer bir taban sınıfı alt sınıflara olduğu gibi aktaracaksanız, taban
sınıftan gelen metot ve nitelikler üzerinde herhangi bir değişiklik
yapmayacaksanız ve alt sınıflara da herhangi bir nitelik ilave etmeyecekseniz,
alt sınıflar tanımlamak yerine doğrudan taban sınıfın örneklerinden yararlanmak
daha akıllıca ve pratik bir tercih olabilir::
    
    >>> asker = Oyuncu('Ahmet', 'Er')
    >>> işçi = Oyuncu('Mehmet', 'Usta')
    >>> yönetici = Oyuncu('Selim', 'Müdür')
    
Burada asker, işçi ve yönetici için ayrı ayrı alt sınıflar tanımlamak yerine,
her biri için doğrudan ``Oyuncu()`` sınıfını farklı `isim` ve `rütbe`
değerleriyle örnekleyerek istediğimiz şeyi elde ettik.

İlerleyen derslerde miras alma alternatiflerinden daha ayrıntılı bir şekilde söz
edeceğiz, ama dilerseniz şimdi konuyu daha fazla dağıtmadan miras alınan metot
ve niteliklerin alt sınıflar içinde nasıl yeniden tanımlanacağını, nasıl
değişikliğe uğratılacağını ve alt sınıflara nasıl yeni nitelik ve metotlar
ekleneceğini incelemeye geçelim ve ilk örneklerimizi vermeye başlayalım.

Hatırlarsanız bir önceki başlıkta şöyle bir kod yazmıştık::
    
    class Asker(Oyuncu):
        pass
        
Burada ``Oyuncu()`` sınıfını bütünüyle alt sınıfa aktardık. Peki ya biz bir
taban sınıfı olduğu gibi miras almak yerine, bazı nitelikleri üzerinde
değişiklik yaparak miras almak istersek ne olacak? Mesela taban sınıf içinde
`self.güç` değeri 0. Biz bu değerin ``Asker()``, ``İşçi()`` ve ``Yönetici()``
örnekleri için birbirinden farklı olmasını isteyebiliriz. Veya taban sınıfı
olduğu gibi miras almakla birlikte, alt sınıflardan herhangi birine ilave
nitelik veya nitelikler eklemek de isteyebiliriz. Diyelim ki biz ``Asker()``
sınıfı için, öteki sınıflardan farklı olarak, bir de `memleket` niteliği
tanımlamak istiyoruz. Peki bu durumda ne yapacağız?

İşte bunun için ``Asker()`` sınıfını şu şekilde yazabiliriz::
    
    class Asker(Oyuncu):
        memleket = 'Arpaçbahşiş'
    
Burada ``Asker()`` sınıfına `memleket` adlı bir sınıf niteliği eklemiş olduk.
Dolayısıyla ``Asker()`` sınıfı, ``Oyuncu()`` adlı taban sınıftan miras alınan
bütün nitelik ve metotlarla birlikte bir de `memleket` niteliğine sahip olmuş
oldu::
    
    >>> asker = Asker('Ahmet', 'binbaşı')
    >>> asker.isim
    
    'Ahmet'
    
    >>> asker.memleket
    
    'Arpaçbahşiş'
    
Elbette, bu niteliği öbür alt sınıflarda tanımlamadığımız için bu nitelik
yalnızca ``Asker()`` sınıfına özgüdür.

Aynı şekilde, bir taban sınıftan türeyen bir alt sınıfa yeni bir sınıf metodu,
örnek metodu veya statik metot da ekleyebiliriz::    
    
    class Asker(Oyuncu):
        memleket = 'Arpaçbahşiş'
        
        def örnek_metodu(self):
            pass
            
        @classmethod
        def sınıf_metodu(cls):
            pass
        
        @staticmethod
        def statik_metot():
            pass

**Kural şu**: Eğer alt sınıfa eklenen herhangi bir nitelik veya metot taban
sınıfta zaten varsa, alt sınıfa eklenen nitelik ve metotlar taban sınıftaki
metot ve niteliklerin yerine geçecektir. Yani diyelim ki taban sınıfımız şu::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
Bu sınıfın nitelik ve metotlarını miras yoluyla devralan ``Asker()`` sınıfımız
ise şu::
    
    class Asker(Oyuncu):
        pass
        
Şimdi bu sınıf içinde ``hareket_et()`` adlı bir örnek metodu tanımlayalım::
    
    class Asker(Oyuncu):       
        def hareket_et(self):
            print('yeni hareket_et() metodu')
           
Eğer taban sınıfta ``hareket_et()`` adlı bir sınıf olmasaydı, ``Asker()`` adlı
alt sınıf, taban sınıftan miras alınan öteki metot ve niteliklerle birlikte bir
de ``hareket_et()`` adlı yeni bir örnek metoduna sahip olmuş olacaktı. Ancak
taban sınıfta zaten ``hareket_et()`` adlı bir örnek metodu olduğu için, alt
sınıfta tanımladığımız aynı adlı örnek metodu, taban sınıftaki metodun yerine
geçip üzerine yazıyor.

Buraya kadar her şey tamam. Artık bir taban sınıfa ait metodu alt sınıfa miras
yoluyla aktarırken nasıl yeniden tanımlayacağımızı öğrendik. Ayrıca alt
sınıflara nasıl yeni metot ve nitelik ekleyeceğimizi de biliyoruz. Ama mesela,
`self.isim` ve `self.rütbe` değişkenlerini korurken, taban sınıf içinde 0 değeri
ile gösterilen `self.güç` değişkenini ``Asker()``, ``İşçi()`` ve ``Yönetici()``
sınıflarının her biri içinde nasıl farklı bir değerle göstereceğimizi
bilmiyoruz. Yani `self.güç` değerini ``Asker()`` sınıfı içinde 100, ``İşçi()``
sınıfı içinde 70, ``Yönetici()`` sınıfı içinde ise 50 ile göstermek istesek
nasıl bir yol takip etmemiz gerektiği konusunda bir fikrimiz yok. İsterseniz şu
ana kadar bildiğimiz yöntemleri kullanarak bu amacımızı gerçekleştirmeyi bir
deneyelim::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            self.güç = 100
            
    class İşçi(Oyuncu):
        def __init__(self, isim, rütbe):
            self.güç = 70
            
    class Yönetici(Oyuncu):
        def __init__(self, isim, rütbe):
            self.güç = 50
    
Burada taban sınıfın ``__init__()`` metodunu alt sınıflarda yeniden tanımladık.
Bu kodları bu şekilde yazıp çalıştırdığımızda `self.güç` değerinin herbir alt
sınıf için istediğimiz değere sahip olduğunu görürüz. Ancak burada şöyle bir
sorun var. Bu kodları bu şekilde yazarak `self.isim` ve `self.rütbe`
değişkenlerinin değerini maalesef kaybettik... 

``__init__()`` metodunun parametre listesine `isim` ve `rütbe` parametrelerini
yazdığımız halde bunları kodlarımız içinde herhangi bir şekilde kullanmadığımız
için, bu parametrelerin listede görünüyor olması bir şey ifade etmiyor. Yani alt
sınıflarda tanımladığımız ``__init__()`` metodu bizden `isim` ve `rütbe` adlı
iki parametre bekliyor olsa da, bu parametrelerin değerini kodlar içinde
kullanmadığımız için bu parametrelere değer atamamız herhangi bir amaca hizmet
etmiyor.

Gelin bu söylediklerimizi kanıtlayalım::
    
    >>> import oyuncular
    >>> asker = oyuncular.Asker('Ahmet', 'Er')
    >>> asker.rütbe
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Asker' object has no attribute 'rütbe'  
    
    >>> asker.isim
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Asker' object has no attribute 'isim'   
    
Bu sorunu çözmek için alt sınıflarımızı şu şekilde yazabiliriz::
    
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 100
            
    class İşçi(Oyuncu):
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 70
            
    class Yönetici(Oyuncu):
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 50

Burada `self.isim` ve `self.rütbe` değişkenlerini herbir alt sınıf için tekrar
tanımladık. Bu küçük örnekte pek sorun olmayabilir, ama taban sınıfın
``__init__()`` metodunun içinde çok daha karmaşık işlemlerin yapıldığı
durumlarda yukarıdaki yaklaşım hiç de pratik olmayacaktır. Ayrıca eğer miras
alma işlemini, içeriğini bilmediğiniz veya başka bir dosyada bulunan bir
sınıftan yapıyorsanız yukarıdaki yöntem tamamen kullanışsız olacaktır. Ayrıca
aynı şeyleri tekrar tekrar yazmak miras alma mekanizmasının ruhuna tamamen
aykırıdır. Çünkü biz miras alma işlemini zaten aynı şeyleri tekrar tekrar
yazmaktan kurtulmak için yapıyoruz.

Bu arada, yukarıda yapmak istediğimiz şeyi şununla karıştırmayın: Biz elbette
taban sınıftaki bir niteliği, örnekleme sırasında değiştirme imkanına her
koşulda sahibiz. Yani taban ve alt sınıfların şöyle tanımlanmış olduğunu
varsayarsak::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Asker(Oyuncu):
        pass
        
    class İşçi(Oyuncu):
        pass
        
    class Yönetici(Oyuncu):
        pass
        
Herbir alt sınıfın `güç` değişkenini şu şekilde değiştirebiliriz::
    
    >>> import oyuncular
    >>> asker = oyuncular.Asker('Ahmet', 'Er')
    >>> asker.güç
    
    0
    
Gördüğünüz gibi şu anda askerin gücü 0. Bunu 100 yapalım::
    
    >>> asker.güç = 100
    >>> asker.güç
    
    100
    
Aynı şeyi öteki ``İşçi()`` ve ``Yönetici()`` sınıflarının örnekleri üzerinde de
yapabiliriz. Ama bizim istediğimiz bu değil. Biz, ``Asker()`` sınıfını
örneklediğimiz anda gücü 100, ``İşçi()`` sınıfını örneklediğimiz anda gücü 70,
``Yönetici()`` sınıfını örneklediğimiz anda ise gücü 50 olsun istiyoruz.
      
İşte tam bu noktada imdadımıza yepyeni bir fonksiyon yetişecek. Bu yeni
fonksiyonun adı ``super()``.
            
super()
**********

Hatırlarsanız, taban sınıflardan ilk kez bahsederken, bunlara üst sınıf da
dendiğini söylemiştik. Üst sınıf kavramının İngilizcesi *super class*'tır. İşte
bu bölümde inceleyeceğimiz ``super()`` fonksiyonunun adı da buradaki 'super',
yani 'üst' kelimesinden gelir. Miras alınan üst sınıfa atıfta bulunan
``super()`` fonksiyonu, miras aldığımız bir **üst** sınıfın nitelik ve metotları
üzerinde değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi
sağlar.

Bir önceki başlıkta verdiğimiz örnek üzerinden ``super()`` fonksiyonunu
açıklamaya çalışalım::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
    
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
            
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            self.güç = 100
            
Bu kodlarda, ``Oyuncu()`` adlı taban sınıfı miras alan ``Asker()`` sınıfı,
``__init__()`` metodu içinde `self.güç` değerini yeniden tanımlıyor. Ancak bu
şekilde taban sınıfın ``__init__()`` metodu silindiği için, `self.isim` ve
`self.rütbe` değişkenlerini kaybediyoruz. İşte bu sorunu, üst sınıfa atıfta
bulunan ``super()`` fonksiyonu ile çözebiliriz.

Dikkatlice bakın::
              
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            super().__init__(isim, rütbe)
            self.güç = 100
            
Burada ``__init__()`` metodu içinde şöyle bir satır kullandığımızı
görüyorsunuz::
    
    super().__init__(isim, rütbe)
    
İşte bu satırda ``super()`` fonksiyonu, tam da adının anlamına uygun olarak,
miras alınan üst sınıfın ``__init__()`` metodu içindeki kodların, miras alan alt
sınıfın ``__init__()`` metodu içine aktarılmasını sağlıyor. Böylece hem taban
sınıfın ``__init__()`` metodu içindeki `self.isim` ve `self.rütbe` niteliklerini
korumuş, hem de `self.güç` adlı yeni bir nitelik ekleme imkanı elde etmiş
oluyoruz::
    
    >>> asker = oyuncular.Asker('Ahmet', 'Er')
    >>> asker.isim
    
    'Ahmet'
    
    >>> asker.rütbe
    
    'Er'
    
    >>> asker.güç
    
    100
    
Bu bilgiyi öteki alt sınıflara da uygulayalım::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
    
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            super().__init__(isim, rütbe)
            self.güç = 100
           
    class İşçi(Oyuncu):
        def __init__(self, isim, rütbe):
            super().__init__(isim, rütbe)
            self.güç = 70
            
    class Yönetici(Oyuncu):
        def __init__(self, isim, rütbe):
            super().__init__(isim, rütbe)
            self.güç = 20
            
Gördüğünüz gibi, ``super()`` fonksiyonu sayesinde taban sınıfın değiştirmek
istediğimiz niteliklerine yeni değerler atarken, değiştirmek istemediğimiz
nitelikleri ise aynı şekilde muhafaza ettik.
            
Bu arada eğer taban sınıfın ``__init__()`` metodundaki parametre listesini alt
sınıfta da tek tek tekrar etmek sizi rahatsız ediyorsa yukarıdaki kodları şöyle
de yazabilirsiniz::
    
    class Asker(Oyuncu):
        def __init__(self, *arglar):
            super().__init__(*arglar)
            self.güç = 100
           
    class İşçi(Oyuncu):
        def __init__(self, *arglar):
            super().__init__(*arglar)
            self.güç = 70
            
    class Yönetici(Oyuncu):
        def __init__(self, *arglar):
            super().__init__(*arglar)
            self.güç = 20
            
Yıldızlı parametreleri önceki derslerimizden hatırlıyor olmalısınız. Bildiğiniz
gibi, tek yıldızlı parametreler bir fonksiyonun bütün konumlu (*positional*)
argümanlarını, parametrelerin parantez içinde geçtiği sırayı dikkate alarak bir
demet içinde toplar. İşte yukarıda da bu özellikten faydalanıyoruz. Eğer taban
sınıfta isimli (*keyword*) argümanlar da olsaydı, o zaman da çift yıldızlı
argümanları kullanabilirdik.

Tek ve çift yıldızlı argümanlar genellikle şu şekilde gösterilir::
    
    class Asker(Oyuncu):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.güç = 100
            
Böylece konumlu argümanları bir demet içinde, isimli argümanları ise bir sözlük
içinde toplamış oluyoruz. Bu da bizi üst (ya da taban) sınıfın parametre
listesini alt sınıflarda tekrar etme derdinden kurtarıyor. 

Bu arada, miras alınan taban sınıfa atıfta bulunan ``super()`` fonksiyonu,
Python programlama diline sonradan eklenmiş bir özelliktir. Bu fonksiyon
gelmeden önce taban sınıfa atıfta bulunabilmek için doğrudan o sınıfın adını
kullanıyorduk::
    
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            Oyuncu.__init__(self, isim, rütbe)
            self.güç = 100
            
veya::
    
    class Asker(Oyuncu):
        def __init__(self, *args):
            Oyuncu.__init__(self, *args)
            self.güç = 100    
            
Gördüğünüz gibi, eski yöntemde taban sınıfın adını iki kez kullanmamız
gerekiyor. Ayrıca ``__init__()`` fonksiyonunun parametre listesinde ilk sıraya
yine `self` kelimesini de eklemek zorunda kalıyoruz. 

İsterseniz yukarıda gösterdiğimiz eski yöntemi kullanmaya devam edebilirsiniz
elbette. Ancak ``super()`` fonksiyonunu kullanmak eski yönteme göre biraz daha
pratiktir.

Yukarıdaki örneklerde ``super()`` fonksiyonunu ``__init__()`` metodu içinde
kullandık. Ancak elbette ``super()`` fonksiyonunu yalnızca ``__init__()``
fonksiyonu içinde kullanmak zorunda değiliz. Bu fonksiyonu başka fonksiyonlar
içinde de kullanabiliriz::
    
    class Oyuncu():
        def __init__(self, isim, rütbe):
            self.isim = isim
            self.rütbe = rütbe
            self.güç = 0
            
        def hareket_et(self):
            print('hareket ediliyor...')
            
        def puan_kazan(self):
            print('puan kazanıldı')
            
        def puan_kaybet(self):
            print('puan kaybedildi')
    
    class Asker(Oyuncu):
        def __init__(self, isim, rütbe):
            super().__init__(isim, rütbe)
            self.güç = 100
            
        def hareket_et(self):
            super().hareket_et()
            print('hedefe ulaşıldı.')
            
Bu örneğin, ``super()`` fonksiyonunun nasıl işlediğini daha iyi anlamanızı
sağladığını zannediyorum. Gördüğünüz gibi, taban sınıfın ``hareket_et()`` adlı
metodunu alt sınıfta tanımladığımız aynı adlı fonksiyon içinde ``super()``
fonksiyonu yardımıyla genişlettik, yani taban sınıfın ``hareket_et()`` adlı
fonksiyonuna yeni bir işlev ekledik::
    
    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı.')    
        
Burada ``super().hareket_et()`` satırıyla taban sınıfın ``hareket_et()`` adlı
metodunu alt sınıfta tanımladığımız yeni ``hareket_et()`` metodu içinde
çalıştırarak, bu metodun kabiliyetlerini yeni ``hareket_et()`` metoduna
aktarıyoruz. 

object Sınıfı
**************

Biz buraya gelinceye kadar Python'da sınıfları iki farklı şekilde
tanımlayabileceğimizi öğrendik::
    
    class Deneme():
        pass
        
veya::
    
    class Deneme:
        pass
        
Sınıf tanımlarken parantez kullansak da olur kullanmasak da. Eğer miras
alacağınız bir sınıf yoksa parantezsiz yazımı tercih edebilir, parantezli yazım
tarzını ise başka bir sınıftan miras aldığınız durumlar için saklayabilirsiniz::
    
    class AltSınıf(TabanSınıf):
        pass
        
Ancak sağda solda incelediğiniz Python kodlarında bazen şöyle bir sınıf
tanımlama şekli de görürseniz şaşırmayın::
    
    class Sınıf(object):
        pass
        
Python'ın 3.x öncesi sürümlerinde sınıflar yeni ve eski tip olmak üzere ikiye
ayrılıyordu. Bu sürümlerde eski tip sınıflar şöyle tanımlanıyordu::
    
    class Sınıf:
        pass
        
veya::
    
    class Sınıf():
        pass
        
Yeni tip sınıflar ise şöyle::
    
    class Sınıf(object):
        pass
        
Yani eski tip sınıflar öntanımlı olarak herhangi bir taban sınıftan miras
almazken, yeni tip sınıfların `object` adlı bir sınıftan miras
alması gerekiyordu. Dolayısıyla, tanımladığınız bir sınıfta `object` sınıfını
miras almadığınızda, yeni tip sınıflarla birlikte gelen özelliklerden
yararlanamıyordunuz. Mesela önceki derslerde öğrendiğimiz `@property`
bezeyicisi yeni tip sınıflarla gelen bir özelliktir. Eğer Python 3 öncesi bir
sürüm için kod yazıyorsanız ve eğer `@property` bezeyicisini kullanmak
istiyorsanız tanımladığınız sınıflarda açık açık `object` sınıfını miras
almalısınız. 

Python 3'te ise bütün sınıflar yeni tip sınıftır. Dolayısıyla `object` sınıfını
miras alsanız da almasanız da, tanımladığınız bütün sınıflar öntanımlı olarak
`object` sınıfını miras alacaktır. Yani Python 3 açısından şu üç tanımlama
arasında bir fark bulunmaz::
    
    class Sınıf:
        pass
        
    class Sınıf():
        pass
        
    class Sınıf(object):
        pass
        
Bunların hepsi de Python 3 açısından birer yeni tip sınıftır. Daha doğrusu
Python 3'te bütün sınıflar bir yeni tip sınıf olduğu için, yukarıdaki sınıf
tanımlamaları hep aynı tipte sınıflara işaret eder. Python 2'de ise ilk iki
tanımlama eski tip sınıfları gösterirken, yalnızca üçüncü tanımlama yeni tip
sınıfları gösterir.

Geldik bir bölümün daha sonuna... Böylece miras almaya ilişkin temel konuları
incelemiş olduk. Bu bölümde öğrendiklerimiz sayesinde, etrafta gördüğümüz, miras
alma mekanizmasının kullanıldığı kodların çok büyük bir bölümünü anlayabilecek
duruma geldik. Bu mekanizmaya ilişkin olarak öğrenmemiz gerekenlerin geri
kalanını da bir sonraki bölümde, grafik arayüz tasarımı konusuyla birlikte ele
alacağız.
