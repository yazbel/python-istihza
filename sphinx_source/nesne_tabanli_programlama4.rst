.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

*******************************************
Nesne Tabanlı Programlama (Devamı)
*******************************************

Geçen bölümlerde, nesne tabanlı programlamaya ilişkin hem temel, hem orta, hem
de ileri düzey sayılabilecek pek çok konuya değindik. Şimdiye kadar
öğrendiklerimiz, nesne tabanlı programlama yaklaşımı çerçevesinde yazılım
üretirken yönümüzü bulabilmemiz açısından büyük ölçüde yeterlidir. Ancak daha
önce de söylediğimiz gibi, nesne tabanlı programlama çok geniş kapsamlı bir
konudur ve içinde şimdiye kadar adını bile anmadığımız daha pek çok kavram
barındırır. İşte bu bölümde, geçen derslerimizde incelemeye fırsat
bulamadığımız, ancak nesne tabanlı programlamayı daha derinlemesine tanımak
bakımından bilmemizin iyi olacağı birtakım ileri düzey kavramlardan söz
edeceğiz.

Bu bölümde inceleyeceğimiz ilk konu 'sınıf üyeleri'.
 
Sınıf Üyeleri
*************

Python'da bir sınıf içinde bulunan nitelikler, değişkenler, metotlar,
fonksiyonlar ve buna benzer başka veri tipleri, o sınıfın üyelerini meydana
getirir. Bir sınıfın üyelerini genel olarak üçe ayırarak inceleyebiliriz: 

+ Aleni üyeler (*public members*) 
+ Gizli üyeler (*private members*)
+ Yarı-gizli üyeler (*semi-private members*). 

Bu bölümde bu üç üye türünü ve bunların birbirinden farkını ele alacağız.
Öncelikle aleni üyelerden başlayalım.

Aleni Üyeler
==============

Eğer bir sınıf üyesi dışarıya açıksa, yani bu üyeye sınıf dışından *normal
yöntemlerle* erişilebiliyorsa bu tür üyelere 'aleni üyeler' adı verilir.
Programlama maceranız boyunca karşınıza çıkacak veri üyelerinin tamamına yakını
alenidir. Biz de bu kitapta şimdiye kadar yalnızca aleni üyeleri gördük.

Eğer bildiğiniz tek programlama dili Python ise, şu anda tam olarak neden
bahsediyor olduğumuza anlam verememiş olabilirsiniz. Dilerseniz durumu
zihninizde biraz olsun netleştirebilmek için basit bir örnek verelim.

Diyelim ki elimizde şöyle bir sınıf var::
    
    class Sınıf():
        sınıf_niteliği = 'sınıf niteliği'
        
        def örnek_metodu(self):
            print('örnek metodu')
        
        @classmethod
        def sınıf_metodu(cls):
            print('sınıf metodu')
        
        @staticmethod
        def statik_metot():
            print('statik metot')
            
Bu kodların `sinif.py` adlı bir dosya içinde yer aldığını varsayarsak şöyle bir
şeyler yazabiliriz::
    
    >>> import sinif
    >>> s = sinif.Sınıf()
    >>> dir(s)
            
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
     '__hash__', '__init__', '__le__', '__lt__', '__module__', 
     '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
     '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
     'statik_metot', 'sınıf_metodu', 'sınıf_niteliği', 'örnek_metodu']

Burada öncelikle kodlarımızı barındıran modülü içe aktardık. Daha sonra, içe
aktardığımız modülün içindeki ``Sınıf()`` adlı sınıfımızı `s` örneğine atadık ve
ardından ``dir()`` komutunu kullanarak, içe aktardığımız bu sınıfın içeriğini
sorguladık.

Gördüğünüz gibi, içe aktardığımız sınıfın bütün öğeleri listede var. Yani biz bu
sınıf içindeki bütün öğelere normal yollardan erişme imkanına sahibiz::
    
    >>> s.statik_metot()
    
    'statik metot'
    
    >>> s.örnek_metodu()
    
    'örnek metodu'
    
    >>> s.sınıf_metodu()
    
    'sınıf metodu'
    
    >>> s.sınıf_niteliği
    
    'sınıf niteliği'
    
İşte ``dir()`` komutunun çıktısında görünen ve normal yollardan erişebildiğimiz
bütün bu öğeler birer aleni üyedir. 

Yukarıda da ifade ettiğimiz gibi, program yazarken çoğu zaman yalnızca aleni
üyelerle muhatap olacaksınız. Ancak bazı durumlarda, yazdığınız bir sınıftaki
bütün sınıf üyelerinin dışarıya açık olmasını istemeyebilirsiniz. Eğer
kodlarınızda, sınıfın yalnızca iç işleyişini ilgilendiren, bu yüzden de
dışarıdan erişilmesine gerek olmadığını veya erişilirse problem çıkacağını
düşündüğünüz birtakım öğeler varsa bunları dışarıya kapatarak bir 'gizli üye'
haline getirmek isteyebilirsiniz. Peki ama nasıl?

Gizli Üyeler
=============

Python'da şimdiye kadar gördüğümüz ve yukarıda andığımız aleni üyelerin dışında,
bir de gizli üyeler bulunur. Aleni üyelerin aksine gizli üyeler dışarıya açık
değildir. Gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemeyiz.

Konuyu açıklığa kavuşturmak için, aleni üyeleri anlatırken verdiğimiz sınıf
örneğinde şu değişikliği yapalım::
    
    class Sınıf():
        __gizli = 'gizli'
        
        def örnek_metodu(self):
            print(self.__gizli)
            print('örnek metodu')
        
        @classmethod
        def sınıf_metodu(cls):
            print('sınıf metodu')
        
        @staticmethod
        def statik_metot():
            print('statik metot')
            
Burada `__gizli` adlı bir gizli sınıf niteliği tanımladık. Bu değişkenin
yalnızca baş tarafında iki adet alt çizgi olduğuna, ancak uç tarafında alt
çizgi bulunmadığına dikkat edin. İşte Python'da baş tarafında yukarıdaki gibi
iki adet alt çizgi olan, ancak uç tarafında alt çizgi bulunmayan (veya yalnızca
tek bir alt çizgi bulunan) bütün öğeler birer gizli üyedir. Dışarıya kapalı olan
bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.

İsterseniz deneyelim::
    
    >>> import sinif
    >>> s = sinif.Sınıf()
    >>> s.__gizli
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Sınıf' object has no attribute '__gizli'
    
Gördüğünüz gibi, örnek adı üzerinden `__gizli` niteliğine erişemiyoruz. Bir de
sınıf adı üzerinden erişmeyi deneyelim::
    
    >>> sinif.Sınıf.__gizli
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: type object 'Sınıf' has no attribute '__gizli'
    
Bu şekilde de erişemedik. Çünkü dediğimiz gibi, başında çift alt çizgi olan,
ancak ucunda herhangi bir çizgi bulunmayan (veya tek bir alt çizgi bulunan) bu
gizli öğelere **normal yollardan** erişemeyiz.

Dilerseniz gizli üye oluşturma kurallarını şöyle bir netleştirelim:

Bir üyenin gizli olabilmesi için başında **en az** iki adet, ucunda da **en
fazla** bir adet alt çizgi bulunmalıdır. Yani şunlar birer gizli üyedir::
    
    >>> __gizli = 'gizli'
    >>> __gizli_ = 'gizli'
    >>> __gizli_üye = 'gizli'
    >>> __gizli_üye_ = 'gizli'

Burada önemli bir noktaya dikkatinizi çekmek istiyorum: Gizli üyeler yalnızca
**sınıf dışına** kapalıdır. Bu üyelere **sınıf içinden** rahatlıkla
erişebiliriz. Mesela yukarıdaki örnekte bu durumu görüyorsunuz. `__gizli` adlı
değişkene ``örnek_metodu()`` içinden normal bir şekilde erişebiliyoruz::

    def örnek_metodu(self):
        print(self.__gizli)
        print('örnek metodu')
        
Bu durumda sınıf dışından bu ``örnek_metodu()``'na eriştiğimizde gizli üye olan
`__gizli`'ye de erişmiş oluyoruz::
    
    >>> import sinif
    >>> s = sinif.Sınıf()
    >>> s.örnek_metodu()
    
    'gizli'
    'örnek metodu'
    
Burada ``örnek_metodu()``, `__gizli` adlı gizli üyeye erişmemiz için bize
aracılık etmiş oluyor. 

Peki ama bir insan neden bu şekilde birtakım gizli üyeler tanımlamak istiyor
olabilir?

Hatırlarsanız geçen bölümde şöyle bir örnek vermiştik::
    
    class Çalışan():
        personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
        
        @classmethod
        def personel_sayısını_görüntüle(cls):
            print(len(cls.personel))
            
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
        
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Burada `personel` adlı bir sınıf niteliğimiz var. Bu niteliğe sınıf içinde hem
``personele_ekle()`` adlı örnek metodundan hem de
``personel_sayısını_görüntüle()`` ve ``personeli_görüntüle()`` adlı sınıf
metotlarından erişmek suretiyle bu nitelik üzerinde çeşitli işlemler yapıyoruz.

Esasında şöyle bir düşününce, `personel` adlı niteliğin yalnızca sınıfın iç
işleyişi açısından önem taşıdığını rahatlıkla söyleyebiliriz. Bu niteliğe sınıf
dışından doğrudan erişilerek personel üzerinde işlem yapılmaya çalışılması çok
mantıksız. Yani sınıfımızı kullanacak kişilerin şu tür bir kod yazması biraz
abes kaçacaktır::
    
    >>> from calisan import Çalışan
    >>> Çalışan.personel.append('Ahmet')
    
Zira biz, kodlarımızın yapısı gereği, personel üzerindeki işlemlerin yalnızca
çeşitli fonksiyonlar/metotlar aracılığıyla yapılmasını istiyoruz.
    
Personele eleman ekleyecek kişilerin doğrudan `personel` listesine erişmesi,
kodlarımızın kullanım kurallarının bir bakıma ihlal edilmesi anlamına geliyor.
Çünkü biz personele eleman ekleme işlemleri için halihazırda ayrı bir metot
tanımlamış durumdayız. Eğer personele adam eklenecekse, bu işlem doğrudan
`personel` listesi üzerinden değil, ``personele_ekle()`` adlı örnek metodu
üzerinden gerçekleştirilmeli. Yukarıdaki kodlarda bu ``personele_ekle()`` metodu
doğrudan sınıfın kendi ``__init__()`` metodu tarafından kullanılıyor.
Dolayısıyla yukarıdaki sınıfı kullanmanın doğru yolu, ilgili sınıfı
örneklemektir::
    
    >>> from calisan import Çalışan
    >>> ahmet = Çalışan('Ahmet')
    
Aynı şekilde personel listesini görüntülemek için de doğrudan `personel`
listesine erişmeye çalışmayacağız. Yani şöyle bir şey yazmayacağız::
    
    >>> Çalışan.personel
    
Bunun yerine, bu iş için özel olarak tasarladığımız ``personeli_görüntüle()``
fonksiyonunu kullanacağız::
    
    >>> Çalışan.personeli_görüntüle()
    
İşte yukarıdaki kodlarda yer alan `personel` listesinin usulsüz bir şekilde
kullanılmasını önlemek amacıyla bu listeyi bir gizli üye haline
getirebilirsiniz::
        
    class Çalışan():
        __personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
        
        @classmethod
        def personel_sayısını_görüntüle(cls):
            print(len(cls.__personel))
            
        def personele_ekle(self):
            self.__personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
            
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.__personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
    
Burada `personel` listesinin baş tarafına iki alt çizgi ekleyerek bunu sınıf
dışından, normal yollarla erişilmez hale getirdik::
    
    >>> Çalışan.__personel
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: type object 'Çalışan' has no attribute '__personel'    
    
Gördüğünüz gibi, aslında sınıfımız içinde `__personel` adlı bir nitelik olmasına
rağmen, Python bu niteliğe sınıf dışından erişilmesine izin vermiyor. Eğer
amacımız personel üzerinde çeşitli işlemler yapmaksa, bu iş için sınıfın bize
sunduğu metotları kullanmamız gerekiyor::
    
    >>> Çalışan.personel_sayısını_görüntüle()
    
Bu tip durumlarda gizli üyeler epey işinize yarayabilir...

Bir örnek daha verelim.
    
Yukarıdaki kodlarda, tıpkı `personel` listesi gibi, aslında ``personele_ekle()``
fonksiyonu da dışarıdan erişilmesine gerek olmayan, hatta dışarıdan erişilirse
kafa karıştırıcı olabilecek bir sınıf üyesidir. 

``personele_ekle()`` adlı örnek metodu, sınıfımız içinde ``__init__()``
fonksiyonu tarafından kullanılıyor. Dolayısıyla sınıfımız örneklendiğinde
``personele_ekle()`` metodu devreye girerek yeni elemanı personel listesine
ekliyor::
    
    >>> ayşe = Çalışan('Ayşe')
    
    'Ayşe adlı kişi personele eklendi'
    
Öte yandan, bu fonksiyon aleni bir üye olduğu için, buna dışarıdan erişmemizin
önünde herhangi bir engel yok::
    
    >>> ayşe.personele_ekle()
    
    'Ayşe adlı kişi personele eklendi'
 
Bu fonksiyon sınıf dışından çağrıldığında, kendisini çağıran örnek adını
personel listesine tekrar ekleyecektir:: 

    >>> Çalışan.personeli_görüntüle()
    
    Ayşe
    Ayşe

Yani yukarıdaki komut Ayşe adlı kişiyi personel listesine tekrar ekler.
Dolayısıyla bu fonksiyona sınıf dışından erişilmesi son derece mantıksız, son
derece yanlış ve hatta son derece kafa karıştırıcıdır. O yüzden, herhangi bir
sıkıntı yaşanmasını engellemek amacıyla bu fonksiyonu da bir gizli üye olarak
tanımlayabiliriz::
    
    class Çalışan():
        __personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.__personele_ekle()
        
        @classmethod
        def personel_sayısını_görüntüle(cls):
            print(len(cls.__personel))
            
        def __personele_ekle(self):
            self.__personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
        
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.__personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Bu şekilde ``personele_ekle()`` fonksiyonunu da dışarıya kapatmış olduk. Artık
bu fonksiyon da, olması gerektiği gibi, yalnızca sınıf içinde kullanılabilecek.

Yukarıdaki örnekler, bazı durumlarda veri gizlemenin epey işimize
yarayabileceğini bariz bir biçimde gösteriyor. Ama elbette, yukarıdaki
işlemlerin hiçbiri zorunlu değildir. Yani siz, yazdığınız kodlarda hiçbir sınıf
üyesini gizlemek mecburiyetinde değilsiniz. Yukarıda gösterdiğimiz kullanımlar
tamamen tercih meselesidir. Zaten birkaç nadir durum dışında, Python'da
verilerinizi gizlemek zorunda da kalmazsınız. Ama tabii kendiniz Python'ın bu
özelliğinden yararlanmasanız da, sırf bu özellikten yararlanan başka
programcıların yazdığı kodları anlayabilmek için bile olsa bu özellikten
haberdar olmalısınız.

İsim Bulandırma
=================

Gelin isterseniz gizli üyelere ilişkin ilginç bir özellikten söz edelim. 

Python'da 'gizli' olarak adlandırdığımız öğeler aslında o kadar da gizli
değildir... Çünkü Python'da gerçek anlamda gizli ve dışarıya tamamen kapalı
üyeler bulunmaz. Peki bu ne anlama geliyor?

Bu şu anlama geliyor: Her ne kadar yukarıdaki örneklerde üyeleri dışarıya
kapatmak için kullandığımız alt çizgi işaretleri ilgili değişkeni gizlese de,
bunu tamamen erişilmez hale getirmez. Dediğimiz gibi, Python'da gerçek anlamda
dışa kapalı sınıf üyeleri bulunmadığı için biz bu üyelere **bir şekilde** erişme
imkanına sahibiz. Peki ama nasıl?

Python, kodlar içinde gizli bir üye ile karşılaştığında özel bir 'isim
bulandırma' (*name mangling*) işlemi gerçekleştirir ve ilgili gizli üyenin
görünüşünü değiştirir. Eğer Python'ın arkaplanda neler çevirdiğini bilirseniz,
gizli üyeye de erişebilirsiniz.

Örnek sınıfımız şöyleydi::
    
    class Sınıf():
        __gizli = 'gizli'
        
        def örnek_metodu(self):
            print(self.__gizli)
            print('örnek metodu')
        
        @classmethod
        def sınıf_metodu(cls):
            print('sınıf metodu')
        
        @staticmethod
        def statik_metot():
            print('statik metot')
            
Şimdi, bu sınıf içindeki gizli üyeye erişeceğiz. 

Dikkatlice bakın::
    
    >>> import sinif
    >>> s = sinif.Sınıf()
    >>> s._Sınıf__gizli
    
    'gizli'
    
Ne kadar da tuhaf, değil mi?   

İşte Python, siz bir sınıf üyesini `__gizli` şeklinde tanımladığınızda, bu
öğe üzerinde şu işlemleri gerçekleştirir:

Öncelikle değişkenin baş tarafına bir alt çizgi ekler::
    
    _
    
Daha sonra, bu alt çizginin sağ tarafına bu gizli üyeyi barındıran sınıfın adını
iliştirir::
    
    _Sınıf

Son olarak da gizli üyeyi sınıf adının sağ tarafına yapıştırır::
    
    _Sınıf__gizli
    
Dolayısıyla ``_Sınıf__gizli`` kodunu kullanarak, `__gizli` adlı üyeye sınıf
dışından erişebilirsiniz.

Pratik olması bakımından bir örnek daha verelim. Mesela şu örneği ele alalım::
    
    class Çalışan():
        __personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.__personele_ekle()
        
        @classmethod
        def personel_sayısını_görüntüle(cls):
            print(len(cls.__personel))
            
        def __personele_ekle(self):
            self.__personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
        
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.__personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Burada ``__personele_ekle()`` adlı fonksiyon bir gizli üyedir. Dolayısıyla buna
dışarıdan normal yöntemlerle erişemeyiz.

Bunu test etmek için önce gerekli verileri oluşturalım::
    
    >>> from calisan import Çalışan
    >>> ahmet = Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi.
    
Şimdi `ahmet` örneği üzerinden bu gizli üyeye erişmeye çalışalım::
    
    >>> ahmet.__personele_ekle()
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Çalışan' object has no attribute '__personele_ekle'
    
Gördüğünüz gibi, Python bu üyeye normal yollardan erişmemize izin vermiyor. Ama
biz biliyoruz ki, Python bu üyeyi gizlerken özel bir isim bulandırma işlemi
gerçekleştiriyor. Bu bulandırma işleminin nasıl gerçekleştirildiğini bildiğimize
göre gizli üyeye erişebiliriz.

Öncelikle örneğimizin adını yazalım. Zira gizli üyeye bu ad üzerinden
erişeceğiz::
    
    >>> ahmet.
    
Şimdi bulandırma işlemini uygulamaya geçebiliriz.

Öncelikle bir alt çizgi ekleyelim::
    
    >>> ahmet._
    
Daha sonra sınıf adını iliştirelim::
    
    >>> ahmet._Çalışan
    
Son olarak da gizli üyenin kendisini yazalım::
    
    >>> ahmet._Çalışan__personele_ekle()
    
    Ahmet adlı kişi personele eklendi.
    
Gayet başarılı...

Yalnız buraya şöyle bir not düşelim: Her ne kadar Python bize gizli üyelere
erişme imkanı sunsa da, başkasının yazdığı kodları kullanırken, o kodlardaki
gizli üyelere erişmeye çalışmamak çoğu zaman iyi bir fikirdir. Nihayetinde eğer
bir programcı, bir sınıf üyesini gizlemişse bunun bir nedeni vardır. Eğer
erişmenizin istenmediği bir üyeye erişirseniz ve bunun sonucunda birtakım
sorunlarla karşılaşırsanız bu durum o programı yazan programcının değil, tamamen
sizin kabahatinizdir. Python programcılarının da sık sık söylediği gibi:
'Neticede hepimiz, doğruyu yanlışı bilen, yetişkin insanlarız.'

Yarı-gizli Üyeler
====================

Buraya kadar Python’a dair anlattığımız şeylerden, yerleşmiş adetlerin ve
geleneklerin Python açısından ne kadar önemli olduğunu anlamış olmalısınız. Daha
önce verdiğimiz örnekler, bu dildeki pek çok meselenin uzlaşma esası üzerinden
çözüme kavuşturulduğunu bize açık ve seçik olarak gösterdi. Mesela geçen
bölümlerde ele aldığımız `self` ve `cls` kelimeleri tamamen uzlaşmaya dayalı
kavramlardır. Python topluluğu içinde, `self` kelimesinin örnek metotları için,
`cls` kelimesinin ise sınıf metotları için kullanılması tamamen bir alışkanlık,
adet, gelenek ve uzlaşı meselesidir. Python’ın kendisi bize bu kelimeleri
dayatmaz. Ancak topluluk içinde süregelen kuvvetli gelenekler bizi başka
kelimeleri değil de yukarıdaki kelimeleri kullanmaya teşvik eder. Aynı şekilde
kod yazarken girinti sayısının dört boşluk olarak belirlenmiş olması da bir
gelenekten ibarettir. Yazdığınız kodlarda, aynı program içinde hep aynı sayıda
olmak şartıyla, istediğiniz sayıda boşluktan oluşan girintiler
kullanabilirsiniz. Ama Python'ın topluluk içi gelenekleri bizi dört boşlukluk
bir girintileme sistemi kullanmaya yöneltir.

İşte tıpkı yukarıdakiler gibi, Python'daki sınıf üyelerinin dışa açık veya dışa
kapalı olup olmaması da hep belli birtakım gelenekler üzerinden belirlenen bir
durumdur. 

Bunun bir örneğini, yukarıda gizli üyeleri anlatırken vermiştik. Bir sınıf
içindeki herhangi bir niteliğin başında çift alt çizgi gördüğümüzde, o sınıfı
yazan kişinin, bu niteliğe sınıf dışından erişilmesini istemediğini anlıyoruz.
Python her ne kadar nitelikleri gizlememiz için bize özel bir mekanizma sunmuş
olsa da bu niteliğe erişmemizi tamamen engellemiyor, ancak ilgili sınıfı yazan
kişinin niyetine saygı göstereceğimizi varsayıyor.

Python'da sınıf üyelerinin gizliliği, yukarıda da gördüğümüz gibi, hem özel bir
mekanizma ile hem de topluluk içi gelenekler tarafından korunur. 

Python'da bir de yalnızca topluluk içi gelenekler tarafından korunan
'yarı-gizli' üyeler (*semi-private members*) vardır. İşte bu bölümde, bir gizli
üye türü olan yarı-gizli üyelerden söz edeceğiz.

Yarı-gizli üyeler, herhangi bir özel mekanizma aracılığıyla değil de yalnızca
topluluk içi gelenekler tarafından korunan niteliklerdir. Herhangi bir üyeyi
yarı-gizli olarak işaretlemek için yapmamız gereken tek şey başına bir adet alt
çizgi yerleştirmektir. Örneğin::
    
    class Falanca():
        _yarıgizli = 'yarıgizli'
        
Buradaki `_yarıgizli` adlı niteliğe sınıf içinden veya dışından erişmemizi
engelleyen veya zorlaştıran hiçbir mekanizma bulunmaz. Ama biz bir sınıf içinde
tek alt çizgi ile başlayan bir öğe gördüğümüzde, bunun sınıfın iç işleyişine
ilişkin bir ayrıntı olduğunu, sınıf dışından bu öğeyi değiştirmeye kalkışmamamız
gerektiğini anlarız. 

@property Bezeyicisi
**********************

Yukarıda aleni, gizli ve yarı-gizli sınıf üyelerinden söz ettik. İsterseniz
özellikle yarı-gizli öğelerin kullanıldığı bir kod örneği vererek yukarıda
anlattıklarımızı somut bir örnek üzerinden netleştirmeye çalışalım.

Diyelim ki şöyle bir kod yazdık::
    
    class Çalışan():
        personel = []
      
        def __init__(self, isim):
            self.isim = isim
            self.personele_ekle()
    
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
    
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.personel:
                print(kişi)

Burada personel veritabanına kişi eklememizi ve veritabanındaki kişileri
görüntülememizi sağlayan birtakım metotlar var. 

Bu metotları şöyle kullanıyoruz::
    
    >>> from calisan import Çalışan
    >>> ç1 = Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi
    
    >>> ç2 = Çalışan('Mehmet')
    
    Mehmet adlı kişi personele eklendi
    
    >>> Çalışan.personeli_görüntüle()
    
    Personel listesi:
    Ahmet    
    Mehmet
    
Peki eğer kodlarımızı kullananlar personel listesindeki bir kişinin ismini
sonradan değiştirmek isterse ne yapacak?

Kodlarımız içinde, isim değişikliği yapılmasını sağlayan özel bir metot yok.
Dolayısıyla kodlarımızı kullananlar, doğrudan `isim` adlı örnek değişkenine
erişerek isim değişikliğini şu şekilde yapabilir::
    
    >>> ç1.isim = 'Selim'
    
Bu şekilde 'Ahmet' adlı kişinin ismini değiştirdik. Bunu teyit edelim::
    
    >>> print(ç1.isim)
    
    Selim
    
Ancak burada şöyle bir sorun var. Bu isim değişikliği personel listesine
yansımadı. Kontrol edelim::
    
    >>> Çalışan.personeli_görüntüle()
    
    Personel listesi:
    Ahmet
    Mehmet
    
Gördüğünüz gibi, 'Ahmet' ismi hâlâ orada duruyor. Bu sorunu gidermek için,
personel listesine de müdahale edilmesi gerekir::
    
    >>> kişi = Çalışan.personel.index('Ahmet')
    >>> Çalışan.personel[kişi] = 'Selim'

Burada öncelikle listelerin ``index()`` metodunu kullanarak, değiştirmek
istediğimiz kişinin `personel` listesindeki sırasını bulduk. Daha sonra da bu
bilgiyi kullanarak listede gerekli değişikliği yaptık.

Personel listesini tekrar kontrol ettiğimizde her şeyin yolunda olduğunu
görebiliriz::
    
    >>> Çalışan.personeli_görüntüle()
    
    Personel listesi:
    Selim
    Mehmet
    
Ancak bunun hiç kullanışlı bir yöntem olmadığı çok açık. Basit bir isim
değişikliği için, kullanıcılarımız bir sürü kod yazmak zorunda kalıyor.
Kullanıcılarımızın hayatını kolaylaştırmak için onlara pratik bir metot
sunabiliriz::
    
    class Çalışan():
        personel = []
      
        def __init__(self, isim):
            self.isim = isim
            self.personele_ekle()
    
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
    
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.personel:
                print(kişi)
                
        def isim_değiştir(self, yeni_isim):
            kişi = self.personel.index(self.isim)
            self.personel[kişi] = yeni_isim
            print('yeni isim:', yeni_isim)    
            
Burada ``isim_değiştir()`` adlı yeni bir fonksiyon tanımladık. Artık
kodlarımızdan istifade edenler yalnızca bu yeni fonksiyonu kullanarak, personele
önceden ekledikleri kişilerin ismini kolayca değiştirebilir::
    
    >>> from calisan import Çalışan
    >>> ç1 = Çalışan('Ahmet')
    >>> ç2 = Çalışan('Mehmet')
    >>> ç3 = Çalışan('Selim')
    >>> Çalışan.personeli_görüntüle()
    
    Personel listesi:
    Ahmet
    Mehmet
    Selim
    
    >>> ç1.isim_değiştir('Emre')
    
    yeni isim: Emre
    
    >>> Çalışan.personeli_görüntüle()
    
    Personel listesi:
    
    Emre
    Mehmet
    Selim
    
Gördüğünüz gibi, kodlarımız gayet güzel çalışıyor. Bu noktadan sonra, **eğer
arzu ederseniz**, kullanıcılarınızın `personel` ve `self.isim` adlı değişkenlere
doğrudan erişmesini engellemek için bunları tek alt çizgi veya çift alt çizgi
kullanarak gizleyebilirsiniz.

Çift alt çizgi ile::
        
    class Çalışan():
        __personel = []
      
        def __init__(self, isim):
            self.__isim = isim
            self.personele_ekle()
    
        def personele_ekle(self):
            self.__personel.append(self.__isim)
            print('{} adlı kişi personele eklendi'.format(self.__isim))
    
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls.__personel:
                print(kişi)
                
        def isim_değiştir(self, yeni_isim):
            kişi = self.__personel.index(self.__isim)
            self.__personel[kişi] = yeni_isim
            print('yeni isim: ', yeni_isim) 
 
Tek alt çizgi ile::            

    class Çalışan():
        _personel = []
      
        def __init__(self, isim):
            self._isim = isim
            self.personele_ekle()
    
        def personele_ekle(self):
            self._personel.append(self._isim)
            print('{} adlı kişi personele eklendi'.format(self._isim))
    
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls._personel:
                print(kişi)
                
        def isim_değiştir(self, yeni_isim):
            kişi = self._personel.index(self._isim)
            self._personel[kişi] = yeni_isim
            print('yeni isim: ', yeni_isim) 
            
`personel` ve `self.isim` adlı nitelikleri çift alt çizgi ile gizlediğimizde
Python'ın isim bulandırma mekanizmasını işleteceğini, tek alt çizgi ile
gizlediğimizde ise bu mekanizmanın işletilmeyeceğini biliyorsunuz.

Peki size şöyle bir soru sorayım: 

Acaba, personel listesindeki bir ismi, mesela yalnızca şöyle bir komut vererek
değiştiremez miyiz?

::
    
    >>> ç1.isim = 'Emre'
    
Elbette değiştirebiliriz. Ancak bunun için özel bir araçtan yararlanmamız
gerekir. Bu iş için `@property` adlı özel bir bezeyiciyi kullanacağız.

Dikkatlice bakın::    

    class Çalışan():
        _personel = []
      
        def __init__(self, isim):
            self._isim = isim
            self.personele_ekle()
    
        def personele_ekle(self):
            self._personel.append(self._isim)
            print('{} adlı kişi personele eklendi'.format(self._isim))
    
        @classmethod
        def personeli_görüntüle(cls):
            print('Personel listesi:')
            for kişi in cls._personel:
                print(kişi)
        
        @property
        def isim(self):
            return self._isim
        
        @isim.setter
        def isim(self, yeni_isim):        
            kişi = self._personel.index(self.isim)
            self._personel[kişi] = yeni_isim
            print('yeni isim: ', yeni_isim) 
            
Bu kodları çalıştırdığınızda, tıpkı yukarıda bahsettiğimiz gibi, herhangi bir
çalışanın ismini yalnızca şu şekilde değiştirebildiğinizi göreceksiniz::
    
    >>> ç1.isim = 'Emre'
    
Üstelik bu kod, isim değişikliğinin personel listesine de yansımasını sağlıyor::
    
    >>> Çalışan.personeli_görüntüle()
    
    Emre
    
Birazdan bu kodları derinlemesine inceleyeceğiz. Ama isterseniz öncelikle şu
`@property` bezeyicisinden biraz söz edelim. Böylelikle yukarıdaki kodları
anlamamız kolaylaşır.

Metottan Niteliğe
===================
            
Şimdiye kadar verdiğimiz örneklerden anlamış olabileceğiniz gibi, bir sınıf
içinde salt verileri tutan değişkenlere 'nitelik' adı veriyoruz. Mesela::
    
    class Falanca():
        nitelik = 'nitelik'
        
        def __init__(self):
            self.nitelik = 'nitelik'
            
Burada `nitelik` bir sınıf niteliği, `self.nitelik` ise bir örnek niteliğidir. 

Buna karşılık, bir sınıf içinde fonksiyon biçiminde yer alan ve bir işlemi veya
prosedürü yerine getiren öğelere ise metot adı veriyoruz. Mesela::
    
    class Falanca():
        def __init__(self):
            pass
            
        def örnek_fonk(self):
            pass
        
        @classmethod
        def sınıf_fonk(cls):
            pass
            
        @staticmethod
        def statik_fonk():
            pass
            
Burada ``örnek_fonk()`` adlı fonksiyon bir örnek metodu, ``sınıf_fonk()`` adlı
fonksiyon bir sınıf metodu, ``statik_fonk()`` adlı fonksiyon ise bir statik
metottur. Metotlar ile niteliklerin gerçekleştirebilecekleri işlemlerin
karmaşıklığının birbirinden farklı olmasının yanısıra, bunlar arasında kullanım
açısından da farklılık vardır. Mesela ``Falanca()`` sınıfı içindeki `nitelik`
adlı sınıf niteliğini şu şekilde kullanıyoruz::
    
    >>> Falanca.nitelik
    >>> Falanca.nitelik = 'yeni değer'
    
Aynı sınıf içindeki ``sınıf_fonk()`` adlı sınıf metoduna ise şöyle erişiyoruz::
    
    >>> Falanca.sınıf_fonk()
    
Niteliklerin aksine, metotlarda atama yoluyla değer değiştirme gibi bir şey söz
konusu değildir. Yani şuna benzer bir şey yazamayız::
    
    >>> Falanca.sınıf_fonk() = 'yeni değer'
    
Eğer metot bir parametre alıyorsa (yukarıdaki örneklerde metotlar parametre
almıyor), bu parametreyi kullanarak metotla iletişim kurabiliriz. Mesela::
    
    >>> Falanca.sınıf_fonk(yeni_değer)
    
*Property* kelimesi (*attribute* kelimesine benzer bir şekilde) İngilizcede
'özellik, nitelik' gibi anlamlara gelir. Kelime anlamına uygun olarak,
`@property` bezeyicisinin yaptığı en temel iş, bir metodu, nitelik gibi
kullanılabilecek hale getirmektir. Çok basit bir örnek verelim::
    
    class Program():
        def __init__(self):
            pass
        
        def versiyon(self):
            return '0.1'
            
Burada ``versiyon()`` adlı bir örnek metodu tanımladık. Bu programı şöyle
kullanıyoruz::
    
    >>> program = Program()
    >>> program.versiyon()
    
    '0.1'
    
Şimdi programımızda şu değişikliği yapalım::
    
    class Program():
        def __init__(self):
            pass
        
        @property
        def versiyon(self):
            return '0.1'   

Burada ``versiyon()`` adlı metodu `@property` bezeyicisi ile 'bezedik'. Böylece
bu metodu bir 'nitelik' haline getirmiş olduk. Artık bunu şöyle kullanabiliriz::
    
    >>> program = Program()
    >>> program.versiyon
    
    '0.1'

``versiyon()`` fonksiyonunu, `@property` bezeyicisi yardımıyla bir niteliğe
dönüştürdüğümüz için, artık bu fonksiyonu parantezsiz kullandığımıza dikkat
edin.

Gördüğünüz gibi, `@property` bezeyicisinin ilk görevi bir metodu niteliğe
dönüştürmek. Peki acaba neden bir metodu niteliğe dönüştürmek istiyor
olabiliriz?

Şöyle bir program yazdığınızı düşünün::
    
    class Program():
        def __init__(self):
            self.data = 0
            
Yazdığınız bu programı kullananlar, sınıf içindeki `data` niteliğine şu şekilde
erişiyor::
    
    >>> p = Program()
    >>> p.data
    
    0
    
Hatta duruma göre bu niteliği şu şekilde değişikliğe de uğratıyor::
    
    >>> p.data = 1
    
Günün birinde, 'data' kelimesi yerine 'veri' kelimesinin daha uygun olduğunu
düşünerek, 'data' kelimesini 'veri' olarak değiştirmek istediğinizi varsayalım.
Bunun için kodlarınızda şu değişikliği yapabilirsiniz::
    
    class Program():
        def __init__(self):
            self.veri = 0
            
Ancak bu şekilde, programınızı eskiden beri kullananların, sizin yazdığınız bu
programı temel alarak oluşturdukları programları bozmuş oldunuz... Çünkü eğer bu
programdan faydalanan birisi, yazdığı kodda eski `self.data` değişkenini
kullanmışsa, yukarıdaki isim değişikliği yüzünden programı kullanılamaz hale
gelecektir. İşte bunu önlemek için `@property` bezeyicisini kullanabilirsiniz.

Dikkatlice bakın::
    
    class Program():
        def __init__(self):
            self.veri = 0
            
        @property
        def data(self):
            return self.veri
            
Bu şekilde, `self.data` niteliğine yapılan bütün çağrılar ``data()`` adlı metot
vasıtasıyla `self.veri` niteliğine yönlendirilecek. Böylece başkalarının bu
programı kullanarak yazdığı eski kodları bozmadan, programımızda istediğimiz
değişikliği yapmış olduk. Yani programımızda geriye dönük uyumluluğu (*backwards
compatibility*) sağlamış olduk.

Yukarıdaki kodlarda `@property` bezeyicisini kullanarak ``data()`` metodunu bir
niteliğe dönüştürdüğümüz için artık şöyle bir kullanım mümkün::
    
    >>> p = Program()
    >>> p.data
    
    0
    
    >>> p.veri
    
    0
    
Bu yapıda, `self.veri` üzerindeki değişiklikler `self.data` niteliğine de
yansıyacaktır::
    
    >>> p.veri = 5   
    >>> p.data
    
    5 

Salt Okunur Nitelikler
========================

`@property` bezeyicisinin bir başka kabiliyeti de salt okunur nitelikler
oluşturabilmesidir. 

Mesela yukarıdaki programı temel alarak şöyle bir şey deneyelim::
    
    >>> p = Program()
    >>> p.data = 5
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
    
Gördüğünüz gibi, `data` niteliği üzerinde değişiklik yapamıyoruz. Dolayısıyla,
kodlarınızı kullananların değiştirmesini istemediğiniz, 'salt okunur' nitelikler
oluşturmak için `@property` bezeyicisinden yararlanabilirsiniz.

Veri Doğrulaması
==================

`@property` bezeyicisinin üç önemli işlevi bulunur:

+ Değer döndürmek
+ Değer atamak
+ Değer silmek

Yukarıdaki örneklerde bu bezeyicinin değer döndürme işlevini görmüştük. Şimdi
ise bu bezeyicinin değer atama işlevini anlamaya çalışalım.

Bildiğiniz gibi, `@property` bezeyicisinin 'değer döndürme' işlevini kullanarak,
bir niteliğe erişimi kısıtlayabiliyoruz. Örneğin, zamanında şöyle bir kod
yazdığımızı varsayalım::
    
    class Program():
        def __init__(self):
            self.sayı = 0
            
Daha sonra herhangi bir sebepten ötürü buradaki `self.sayı` niteliğine erişimi
kısıtlayıp bu niteliği üzerinde değişiklik yapılamaz hale getirmek istersek
`@property` bezeyicisinden yararlanabiliriz::
    
    class Program():
        def __init__(self):
            self._sayı = 0
    
        @property
        def sayı(self):
            return self._sayı   
            
Gördüğünüz gibi, öncelikle `self.sayı` adlı niteliği, başına bir alt çizgi
getirerek normal erişime kapatmak istediğimizi belirttik. Bu kodları görenler,
`sayı` niteliğinin yarı-gizli bir üye olduğunu anlayıp ona göre davranacak.
Ayrıca biraz sonra tanımlayacağımız ``sayı()`` fonksiyonuyla bu değişkenin
adının birbirine karışmaması için de bir önlem almış olacağız. Python'da bir
değişkenin adını değiştirmeden o değişkene erişimi kontrol altına almak
istediğimizde tek alt çizgi kullanmak tercih edilen bir yöntemdir.

Daha sonra da ``sayı()`` fonksiyonumuzu tanımlıyoruz::
    
    @property
    def sayı(self):
        return self._sayı  
        
Bu ``sayı()`` fonksiyonunu `@property` ile bezediğimiz için, fonksiyon bir
niteliğe dönüştü ve `sayı` değişkenini salt okunur hale getirdi. Eğer amacınız
değişkeni salt okunur hale getirmek değilse `@property` ile bezediğimiz
fonksiyon için bir `setter` parametresi tanımlayabilirsiniz. Nasıl mı?
Dikkatlice inceleyin::
    
    class Program():
        def __init__(self):
            self._sayı = 0
    
        @property
        def sayı(self):
            return self._sayı
            
        @sayı.setter
        def sayı(self, yeni_değer):
            self._sayı = yeni_değer
            return self._sayı
        
`@property` ile bezeyerek bir nitelik haline getirdiğiniz fonksiyonu yazılabilir
hale getirmek ve bu yazma işleminin nasıl olacağını belirlemek için özel bir
`.setter` bezeyicisi ile bezenmiş yeni bir fonksiyon tanımlayabilirsiniz.

Biz yukarıda, yine `sayı` adını taşıyan, `.setter` ile bezenmiş bir fonksiyon
daha tanımladık::  

    @sayı.setter
    def sayı(self, yeni_değer):
        self._sayı = yeni_değer
        return self._sayı

Yukarıdaki kodları çalıştırdığımızda, `_sayı` değişkenine `sayı` adı ile normal
bir şekilde erişip istediğimiz değişikliği yapabiliyoruz::
    
    >>> p = Program()
    >>> p.sayı
    
    0
    
    >>> p.sayı = 5
    >>> p.sayı
    
    5
    
Gördüğünüz gibi, artık `sayı` değişkeni, kendisi için bir `.setter` bezeyicisi
tanımlamış olmamız sayesinde değişiklik kabul ediyor.

`.setter` bezeyicisini, bir niteliği yazılabilir hale getirmenin yanısıra,
doğrulama işlemleri için de kullanabilirsiniz.

Basit bir örnek verelim::
    
    class Program():
        def __init__(self):
            self._sayı = 0
    
        @property
        def sayı(self):
            return self._sayı
            
        @sayı.setter
        def sayı(self, yeni_değer):
            if yeni_değer % 2 == 0:
                self._sayı = yeni_değer
            else:
                print('çift değil!')
               
            return self.sayı    
            
Burada, `self.sayı` niteliğinin değerini çift sayılarla sınırlandırdık. Veri
doğrulama/kısıtlama işlemini `.setter` bezeyicisi içinden gerçekleştirdiğimize
dikkatinizi çekmek isterim. Buna göre, eğer `self.sayı` değişkenine girilen
değer bir çift sayı ise bu değişikliği kabul ediyoruz. Aksi halde 'çift değil!'
uyarısı gösteriyoruz::
    
    >>> p = Program()
    >>> p.sayı = 2
    >>> p.sayı = 5
    
    'çift değil!'
    
Bu arada, `.setter` dışında `.deleter` adlı özel bir `@property` bezeyicisi daha
bulunur. Bunu da bir değeri silmek için kullanıyoruz::
    
    class Program():
        def __init__(self):
            self._sayı = 0
    
        @property
        def sayı(self):
            return self._sayı
            
        @sayı.setter
        def sayı(self, yeni_değer):
            if yeni_değer % 2 == 0:
                self._sayı = yeni_değer
            else:
                print('çift değil!')
               
            return self.sayı
            
        @sayı.deleter
        def sayı(self):
            del self._sayı
            
Gördüğünüz gibi, `@property` bezeyicisini kullanırken üç ayrı metot
tanımlıyoruz:

+ İlgili niteliğe nasıl ulaşacağımızı gösteren bir metot: Bu metodu `@property`
  ile beziyoruz.
  
+ İlgili niteliği nasıl ayarlayacağımızı gösteren bir metot: Bu metodu
  `@metot_adı.setter` şeklinde beziyoruz.
  
+ İlgili niteliği nasıl sileceğimizi gösteren bir metot: Bu metodu
  `@metot_adı.deleter` şeklinde beziyoruz.
  
Bu bölümde nesne tabanlı programlamanın orta-ileri düzey sayılabilecek yönlerine
temas ettik. Artık nesne tabanlı programlamanın temellerinden biraz daha
fazlasını bildiğinizi rahatlıkla iddia edebilirsiniz.
