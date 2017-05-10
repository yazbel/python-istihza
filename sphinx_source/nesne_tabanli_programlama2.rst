.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

***********************************
Nesne Tabanlı Programlama (Devamı)
***********************************

Geçen bölümde Python'da nesne tabanlı programlama konusunun temellerinden söz
etmiştik. Bu bölümde ise nesne tabanlı programlamanın ayrıntılarına inmeye
başlayacağız.

Sınıf Metotları
*****************

Nesne tabanlı programlamaya giriş yaptığımız geçen bölümde şunlara değindik:

#. Sınıflar (*classes*)
#. Örnekler (*instances*)
#. Sınıf nitelikleri (*class attributes*)
#. Örnek nitelikleri (*instance attributes*)
#. Örnek metotları (*instance methods*)

Bunlar nesne tabanlı programlamanın en temel kavramlarıdır. Bunları iyice
öğrendiyseniz, etrafta gördüğünüz kodların büyük bölümünü anlayabilecek kıvama
gelmişsiniz demektir. 

Ama elbette nesne tabanlı programlama yalnızca bu temel kavramlardan ibaret
değil. Nesne tabanlı programlamanın derinlerine indikçe, bunların dışında başka
pek çok kavramla daha karşılaşacağız. Mesela sınıf metotları (*class methods*)
bu kavramlardan biridir. İşte bu bölümde, nesne tabanlı programlamanın ileri
düzey kavramlarının ilki olan bu sınıf metotlarından (*class methods*) söz
edeceğiz.

Dilerseniz ne ile karşı karşıya olduğumuzu anlayabilmek için basit bir örnek
üzerinden ilerleyelim. 

Hatırlarsanız bir önceki bölümde şöyle bir kod parçası vermiştik::
    
    class Çalışan():
        personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
            
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
            
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Bu kodlarda, bir personel listesi oluşturmamızı, personele ekleme yapmamızı,
personeli görüntülememizi, personele yeni kabiliyet eklememizi ve eklediğimiz
kabiliyetleri görüntüleyebilmemizi sağlayan örnek metotları var. Gelin bu
kodlara bir de personel sayısını görüntülememizi sağlayacak bir başka örnek
metodu daha ekleyelim::
    
    class Çalışan():
        personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
        
        def personel_sayısını_görüntüle(self):
            print(len(self.personel))
            
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
            
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)

Burada yeni olarak ``personel_sayısını_görüntüle()`` adlı bir örnek metodu
tanımladık. Bu metot, bir sınıf niteliği olan `personel`'e erişerek bunun
uzunluğunu ekrana basıyor. Böylece personelin kaç kişiden oluştuğunu öğrenmiş
oluyoruz.

Bu yeni örnek metodunu aşağıdaki şekilde kullanabiliriz.

Öncelikle kodlarımızı barındıran modülü içe aktaralım::
        
    >>> import çalışan 
    
Daha sonra personel listesine birkaç çalışan ekleyelim::

    >>> ahmet = çalışan.Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi
    
    >>> mehmet = çalışan.Çalışan('Mehmet')
    
    Mehmet adlı kişi personele eklendi
    
    >>> ayşe = çalışan.Çalışan('Ayşe')
    
    Ayşe adlı kişi personele eklendi
    
Artık herhangi bir örnek değişkeni üzerinden personel sayısına erişebiliriz::
    
    >>> ayşe.personel_sayısını_görüntüle()
    
    3
    
Ancak kodların çalışma mantığı açısından burada bir tutarsızlıktan söz
edebiliriz. Genel olarak bütün personele dair bilgi veren bir fonksiyona
`ahmet`, `mehmet`, `ayşe` gibi bireysel örnek değişkenleri üzerinden erişmek
kulağa sizce de biraz tuhaf gelmiyor mu? Neticede bu fonksiyon, aslında sınıfın
herhangi bir örneği ile özellikle veya doğrudan ilişkili değil. Yani bu
fonksiyon tek tek sınıf örneklerini değil, genel olarak sınıfın bütününü
ilgilendiriyor. Bu bakımdan, ``personel_sayısını_görüntüle()`` fonksiyonunun
örnek değişkenlerinden bağımsız bir biçimde kullanılabilmesi çok daha mantıklı
olacaktır. 

Ayrıca, bir örnek metodu olan ``personel_sayısını_görüntüle()`` fonksiyonunu
örneklerden bağımsız olarak kullanamadığımız için, bu metot yardımıyla personel
sayısının 0 olduğu bir durumu görüntülememiz de mümkün olmuyor. Çünkü bu
fonksiyona erişebilmek için öncelikle sınıfı en az bir kez örneklemiş, yani
sınıfın en az bir adet örneğini çıkarmış olmamız gerekiyor. Bu durum da
kodlarımızın mantığı açısından son derece ciddi bir kısıtlamadır.

Yukarıda sıralanan gerekçeler doğrultusunda kodları hem daha tutarlı bir hale
getirmek hem de personel sayısının 0 olduğu durumu göstermemizi engelleyen
kısıtlamayı aşabilmek için şöyle bir şey deneyebilirsiniz::
    
    def personel_sayısını_görüntüle():
        print(len(Çalışan.personel))
    
    class Çalışan():
        personel = []
    
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
    
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
    
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
    
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
    
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Burada personel sayısını görüntüleyen fonksiyonu sınıftan ayırdık. Böylece şu
şekilde bir kullanım mümkün olabildi::
    
    >>> import çalışan
    >>> çalışan.personel_sayısını_görüntüle()
    
    0
    
``personel_sayısını_görüntüle()`` adlı fonksiyonu sınıftan ayırıp *modül
düzeyinde çalışan bir fonksiyon* (veya bir başka deyişle *global düzeyde çalışan
bir fonksiyon*) haline getirdiğimiz için, artık bu fonksiyon ``Çalışan()``
sınıfının herhangi bir örneğine bağımlı değil. Dolayısıyla bu fonksiyonu,
``Çalışan()`` sınıfı için bir örnek çıkarmak zorunda kalmadan da
kullanabiliyoruz. Bu da bize personel sayısının 0 olduğu durumu gösterebilme
imkanı tanıyor.

Bu fonksiyonu bir de birkaç örnek çıkardıktan sonra çalıştıralım...

Önce sınıfımızın birkaç örneğini çıkaralım::

    >>> ahmet = çalışan.Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi
    
    >>> ayşe = çalışan.Çalışan('Ayşe')
    
    Ayşe adlı kişi personele eklendi
    
    >>> mehmet = çalışan.Çalışan('Mehmet')
    
    Mehmet adlı kişi personele eklendi
    
Şimdi de personelin şu anda kaç kişiden oluştuğunu sorgulayalım::
    
    >>> çalışan.personel_sayısını_görüntüle()
    
    3

Gördüğünüz gibi, bu şekilde kodlarımız biraz daha tutarlı bir görünüme kavuştu.
Ancak bu şekilde, bariz bir biçimde ``Çalışan()`` sınıfı ile ilişkili olan
``personel_sayısını_görüntüle()`` fonksiyonunu sınıftan ayırmış ve kod
bütünlüğünü bozmuş olduk. Çünkü, her ne kadar ``personel_sayısını_görüntüle()``
fonksiyonu ``Çalışan()`` sınıfının herhangi bir örneği ile ilişkili olmasa da,
anlam açısından bu fonksiyonun ``Çalışan()`` sınıfına ait olduğu besbelli.
Ayrıca, yukarıdaki kodları barındıran modülün tamamını değil de, ``from çalışan
import Çalışan`` gibi bir komutla yalnızca ``Çalışan()`` sınıfını içe
aktarırsak, ``personel_sayısını_görüntüle()`` fonksiyonu dışarıda kalacaktır::
    
    >>> from çalışan import Çalışan
    >>> dir()
    
Gördüğünüz gibi, ``personel_sayısını_görüntüle()`` fonksiyonu listede yok.
Dolayısıyla, sınıfla sıkı sıkıya ilişkili olan bu fonksiyonu sınıftan
kopardığımız için, seçmeli içe aktarmalarda bu fonksiyon geride kalıyor ve
böylece bu fonksiyonu kullanamaz hale geliyoruz.

Seçmeli içe aktarmalarda bu fonksiyon aktarım işlemiyle birlikte gelmediği için,
ilgili fonksiyonu özel olarak içe aktarmamız gerekir::
    
    >>> from çalışan import personel_sayısını_görüntüle
    
Bu şekilde `çalışan` modülü içinden ``personel_sayısını_görüntüle()`` adlı
fonksiyonu özel olarak elle içe aktarmış olduk. Artık bu fonksiyonu şöyle
kullanabiliriz::
    
    >>> personel_sayısını_görüntüle()
    
Ancak bu da, her zaman tercih etmeyeceğiniz bir kısıtlama olabilir. O halde bu
kısıtlamayı aşmak için gelin, ilgili fonksiyonu tekrar sınıf içine alalım::
    
    class Çalışan():
        personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
        
        def personel_sayısını_görüntüle(self):
            print(len(self.personel))
            
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
            
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)

Yukarıdaki kodlarda ilgili fonksiyona bir örnek adıyla değil de, sınıf adıyla
erişmek için ilk etapta şu kodu denemek aklınıza gelmiş olabilir::
    
    >>> from çalışan import Çalışan   
    >>> Çalışan.personel_sayısını_görüntüle()
    
Ancak bu kod size şöyle bir hata mesajı verir::   
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: personel_sayısını_görüntüle() missing 
    1 required positional argument: 'self'
    
Çünkü burada siz ``Çalışan.personel_sayısını_görüntüle()`` komutunu vererek
aslında sınıfın bir metoduna (*class method*) erişmeye çalışıyorsunuz. Ancak
kodlarımızın içinde bir *sınıf metodu* yok. Zira, yukarıda sınıf adıyla erişmeye
çalıştığımız ``personel_sayısını_görüntüle()`` fonksiyonu bir sınıf metodu
değil, bir örnek metodudur. Örnek metotlarına da sınıf adlarıyla erişmemizin
mümkün olmadığını, bu tür metotlara erişebilmek için sınıfı en az bir kez
örneklemiş olmamız gerektiğini biliyorsunuz.

Burada, ``__init__()`` ve ``personel_sayısını_görüntüle()`` dışında şu *örnek
metotları* var: ``personel_sayısını_görüntüle()``, ``personele_ekle()``,
``personeli_görüntüle()``, ``kabiliyet_ekle()``,
``kabiliyetlerleri_görüntüle()``. Bunları birer örnek metodu yapan şeyin, `self`
kelimesi olduğunu biliyoruz...

Daha önce de söylediğimiz gibi, her ne kadar Python'da sınıf niteliklerine hem
örnekler hem de doğrudan sınıf adları üzerinden erişebilsek de örnek
niteliklerine ve örnek metotlarına yalnızca örnekler üzerinden erişebiliriz. Bir
metoda, sınıf adı ile erişebilmek için, ilgili metodu bir sınıf metodu olarak
tanımlamış olmamız gerekir. Peki ama nasıl?       

@classmethod Bezeyicisi ve cls
***********************************

Bildiğiniz gibi, örnek metotlarını oluşturmak için `self` adlı bir kelimeden
yararlanıyorduk. Tanımladığımız örnek metotlarının parametre listesinde ilk
sıraya yerleştirdiğimiz bu kelimeyi kullanarak, sınıf içinde örnek metotlarına
erişebiliyoruz. İşte sınıf metotları için de benzer bir işlem yapacağız. 

Çok basit bir örnek verelim::
    
    class Sınıf():
        sınıf_niteliği = 0
    
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
            self.örnek_niteliği = 0
    
        def örnek_metodu(self):
            self.örnek_niteliği += 1
            return self.örnek_niteliği
    
        def sınıf_metodu(cls):
            cls.sınıf_niteliği += 1
            return cls.sınıf_niteliği
            
Burada ``örnek_metodu()`` ile ``sınıf_metodu()`` arasındaki fark, ilkinde
`self`, ikincisinde ise `cls` kullanmamız. Ancak hatırlarsanız, `self`
kelimesinin Python açısından bir zorunluluk olmadığını söylemiştik. Tıpkı `self`
gibi, aslında `cls` kelimesi de Python açısından bir zorunluluk değildir. Yani
`cls` yerine de istediğimiz kelimeyi kullanabilirdik. Bu metotlarda önemli olan,
parametre listesinin ilk sırasını işgal eden kelimenin ne olduğudur. Dolayısıyla
yukarıdaki örnekte Python açısından ``örnek_metodu()`` ile ``sınıf_metodu()``
arasında hiçbir fark bulunmaz. Python her iki metodu da birer örnek metodu
olarak değerlendirir. Bu iki örnek metodu arasındaki fark, ilkinde sınıf
örneklerini temsil edecek kelimenin `self`, ikincisinde ise `cls` olarak
belirlenmiş olmasıdır. Python `self` veya `cls` kelimelerine özel bir önem
atfetmez. Ama Python topluluğu içinde, örnek metotları için `self`, sınıf
metotları için ise `cls` kullanmak çok güçlü bir gelenektir.

Sözün özü, ``sınıf_metodu()`` fonksiyonunun ilk parametresini `cls` yapmış
olmamız bu metodun bir sınıf metodu olabilmesi için gereklidir, ama yeterli
değildir. Python'da bir sınıf metodu oluşturabilmek için bir parçaya daha
ihtiyacımız var::
    
    class Sınıf():
        sınıf_niteliği = 0
    
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
            self.örnek_niteliği = 0
    
        def örnek_metodu(self):
            self.örnek_niteliği += 1
            return self.örnek_niteliği
    
        @classmethod
        def sınıf_metodu(cls):
            cls.sınıf_niteliği += 1
            return cls.sınıf_niteliği
            
İşte Python'da bir sınıf metodunu örnek metodundan ayıran asıl öğe, yukarıdaki
örnekte gördüğümüz `@classmethod` ifadesidir. Python'da isminin önünde `@`
işareti olan bu tür öğelere 'bezeyici' (*decorator*) adı verilir. Gördüğünüz
gibi, `@classmethod` bezeyicisi, yukarıdaki örnekte bir fonksiyonu sınıf
metoduna dönüştürme işlevi görüyor. İlerleyen derslerimizde bezeyicilerin başka
özelliklerinden de söz edeceğiz. Gelin isterseniz şimdi yukarıda öğrendiğimiz
özelliği ``Çalışan()`` adlı sınıfa uygulayalım::
    
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
                
Yukarıda ``personel_sayısını_görüntüle()`` adlı fonksiyonun yanısıra,
``personeli_görüntüle()`` adlı fonksiyonu da bir sınıf metodu haline getirdik.
Çünkü tıpkı ``personel_sayısını_görüntüle()`` fonksiyonu gibi,
``personeli_görüntüle()`` fonksiyonu da aslında tek tek örneklerden ziyade
sınıfın genelini ilgilendiriyor. Dolayısıyla bu fonksiyona da sınıf adı
üzerinden erişebilmek gayet makul ve mantıklı bir iştir.

Sınıf metotlarımızı başarıyla tanımladığımıza göre artık yukarıdaki sınıfı şu
şekilde kullanabiliriz::
    
    >>> from çalışan import Çalışan
    >>> Çalışan.personel_sayısını_görüntüle()
    
    0
    
Bir sınıf metodu olarak tanımladığımız ``personel_sayısını_görüntüle()``
fonksiyonu artık ilgili sınıfın herhangi bir örneğine bağımlı olmadığı için,
sınıfı örneklemek zorunda kalmadan, yalnızca sınıf adını kullanarak
``personel_sayısını_görüntüle()`` fonksiyonuna erişebiliyoruz. Bu da bize
personel sayısının 0 olduğu durumu görüntüleyebilme imkanı veriyor...

Ayrıca, ``personel_sayısını_görüntüle()`` adlı sınıf metodumuz, fiziksel olarak
da sınıfın içinde yer aldığı için, seçmeli içe aktarmalarda sınıfın öteki
öğeleriyle birlikte bu metot da aktarılacaktır::
    
    >>> from çalışan import Çalışan
    >>> dir(Çalışan)
    
Listede sınıf metodumuzun da olduğunu görüyorsunuz.

Personele üye ekledikten sonra bu metodu nasıl kullanacağımızı biliyorsunuz::
        
    >>> ahmet = Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi
    
    >>> mehmet = Çalışan('Mehmet')
    
    Mehmet adlı kişi personele eklendi
    
    >>> ayşe = Çalışan('Ayşe')
    
    Ayşe adlı kişi personele eklendi
       
    >>> Çalışan.personel_sayısını_görüntüle()
    
    3
    
Gördüğünüz gibi, sınıf metodumuza doğrudan sınıf adını kullanarak
erişebiliyoruz. Elbette bu durum, sınıf metoduna örnek adları üzerinden de
erişmemize engel değil. Eğer arzu edersek ``personel_sayısını_görüntüle()`` adlı
sınıf metodunu şu şekilde de çağırabiliriz::
    
    >>> ayşe.personel_sayısını_görüntüle()
    
    3
    
    >>> ahmet.personel_sayısını_görüntüle()
    
    3
    
    >>> mehmet.personel_sayısını_görüntüle()
    
    3
    
Ancak örnek metotlarına ve örnek niteliklerine atıfta bulunmak için örnek
adlarını kullanmak, sınıf metotları ve sınıf niteliklerine atıfta bulunmak için
ise sınıf adlarını tercih etmek daha akıllıca olabilir.

``personel_sayısını_görüntüle()`` fonksiyonu için söylediğimiz bu sözler,
``personeli_görüntüle()`` fonksiyonu için de aynen geçerlidir.
    
Sözün özü, sınıfın herhangi bir örneğine bağlı olmayan bir işlem yapan, ama
anlamsal olarak da sınıfla ilişkili olduğu için sınıf dışında bırakmak
istemediğiniz fonksiyonları birer sınıf metodu olarak tanımlayabilirsiniz. 

Alternatif İnşacılar
***********************

Sınıf metotlarının, işimize yarayabilecek bir başka özelliği ise, bunların bir
'alternatif inşacı' (*alternative constructor*) olarak kullanılabilecek
olmasıdır. "Alternatif neyci?" diye sorduğunuzu rahatlıkla duyabiliyorum...

Gelin isterseniz 'alternatif inşacı' kavramını bir dizi örnek üzerinde
kabataslak da olsa açıklamaya çalışalım.

Şimdi elinizde şöyle bir kitap listesi olduğunu düşünün::

    liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
             ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
             ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]  
  
Bu liste, her bir kitap için, sırasıyla o kitabın ISBN numarasını, yazarını,
ismini ve yayınevini gösteren birer demetten oluşuyor. Amacımız, bu listeden
çeşitli ölçütlere göre sorgulama yapabilen bir program yazmak. Yazdığımız
program; isbn, isim, eser ve yayınevi ölçütlerine göre bu listeden veri
alabilmemizi sağlayacak.

İlk denememizi yapalım::
    
    liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
             ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
             ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
    
    def sorgula(ölçüt=None, değer=None):
        for li in liste:
            if not ölçüt and not değer:
                print(*li, sep=', ')
                
            elif ölçüt == 'isbn':
                if değer == li[0]:
                    print(*li, sep=', ')
                    
            elif ölçüt == 'yazar':
                if değer == li[1]:
                    print(*li, sep=', ')
                    
            elif ölçüt == 'eser':
                if değer == li[2]:
                    print(*li, sep=', ')
                   
            elif ölçüt == 'yayınevi':
                if değer == li[3]:
                    print(*li, sep=', ')
    
Burada öncelikle kitap listemizi tanımladık. Daha sonra da sorgulama işlemini
gerçekleştirecek ``sorgula()`` adlı bir fonksiyon yazdık.

Bu fonksiyon toplam iki parametre alıyor: `ölçüt` ve `değer`. Bu parametrelerin
öntanımlı değerlerini `None` olarak belirledik. Böylece bu fonksiyonu herhangi
bir argüman vermeden de çalıştırabileceğiz.

Fonksiyon gövdesinde ilk yaptığımız iş, fonksiyon argümansız çalıştırıldığında,
yani `ölçüt` ve `değer` için herhangi bir değer belirlenmediğinde ne olacağını
ayarlamak::
    
    for li in liste:
        if not ölçüt and not değer:
            print(*li, sep=', ')    

Eğer `ölçüt` ve `değer` parametreleri için herhangi bir değer belirtilmemişse,
yani bunlar `None` olarak bırakılmışsa, kitap listesinin tamamını, her bir öğe
arasına birer virgül yerleştirerek ekrana basıyoruz.

Eğer ``sorgula()`` fonksiyonu çağrılırken `ölçüt` parametresine `'isbn'`
argümanı, `değer` parametresine ise bir ISBN değeri verilmişse şu işlemi
yapıyoruz::
    
    elif ölçüt == 'isbn':
        if değer == li[0]:
            print(*li, sep=', ')   
            
Burada yaptığımız şey şu: Eğer `ölçüt` 'isbn' ise, fonksiyona verilen `değer`
argümanını, kitap listesi içindeki her bir demetin ilk sırasında arıyoruz. Çünkü
ISBN bilgileri demetlerin ilk sırasında yer alıyor. Eğer bu koşul sağlanırsa
listenin ilgili kısmını ekrana basıyoruz::
    
    if değer == li[0]:
        print(*li, sep=', ')    
        
Bu mantığı kullanarak öteki ölçütler için de birer sorgu kodu yazıyoruz::

    elif ölçüt == 'yazar':
        if değer == li[1]:
            print(*li, sep=', ')
            
    elif ölçüt == 'eser':
        if değer == li[2]:
            print(*li, sep=', ')
           
    elif ölçüt == 'yayınevi':
        if değer == li[3]:
            print(*li, sep=', ')
            
Her bir `değer`'i, listenin ilgili sırasında aradığımıza dikkat edin. Yazar
bilgisi demetlerin ikinci sırasında yer aldığı için `li[1]`'i, aynı gerekçeyle
eser için `li[2]`'yi, yayınevi için ise `li[3]`'ü sorguluyoruz.

Gelelim bu fonksiyonu nasıl kullanacağımıza...

Her zaman söylediğimiz gibi, Python'ın etkileşimli kabuğu mükemmel bir test
ortamıdır. O halde şimdi bu kodları `klist.py` adlı bir dosyaya kaydedelim ve
dosyanın bulunduğu dizinde bir etkileşimli kabuk oturumu başlatarak modülümüzü
içe aktaralım::
    
    >>> import klist
    
Önce `klist` modülü içindeki ``sorgula()`` fonksiyonunu argümansız olarak
çağıralım::
    
    >>> klist.sorgula()
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem    
    
Tam da beklediğimiz gibi, fonksiyon argümansız çağrıldığında bütün kitap
listesini, her bir öğe arasında bir virgül olacak şekilde ekrana basıyor.

Şimdi de mesela ISBN numarasına göre birkaç sorgu işlemi gerçekleştirelim::

    >>> klist.sorgula('isbn', '9789754060409')
    
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt , Cem
    
    >>> klist.sorgula('isbn', '975872519X')
    
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    
    >>> klist.sorgula('isbn', '9789753424080')
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
 
Burada, ``sorgula()`` fonksiyonunun ilk parametresine argüman olarak 'isbn'
değerini verdik. Böylece programımız ISBN numarasına göre sorgu yapmak
istediğimizi anladı. Daha sonra da ikinci argüman olarak istediğimiz bir ISBN
numarasını yazdık ve sorgu işlemini tamamladık.    

Bir de yayınevine göre sorgulama yapalım::
    
    >>> klist.sorgula('yayınevi', 'Metis')
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    
    >>> klist.sorgula('yayınevi', 'İthaki')
    
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    
    >>> klist.sorgula('yayınevi', 'Cem')
    
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem
    
Gördüğünüz gibi, fonksiyonumuz gayet güzel çalışıyor...

Yukarıda verdiğimiz kodlar, bahsettiğimiz amaç için yazılabilecek tek alternatif
değildir elbette. Mesela yukarıdaki ``if-else`` yapısını bir sözlük içine
yerleştirerek çok daha sade bir program elde edebiliriz.

Dikkatlice inceleyin::
    
    liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
             ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
             ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
    
        
    def sorgula(ölçüt=None, değer=None):
        d = {'isbn'     : [li for li in liste if değer == li[0]],
             'yazar'    : [li for li in liste if değer == li[1]],
             'eser'     : [li for li in liste if değer == li[2]],
             'yayınevi' : [li for li in liste if değer == li[3]]}
             
        for öğe in d.get(ölçüt, liste):
            print(*öğe, sep = ', ')
            
Burada bütün ``if-else`` cümleciklerini birer liste üretecine dönüştürüp, `d`
adlı sözlüğün anahtarları olarak belirledik. Artık sorgulama işlemlerini bir
``if-else`` yapısı içinde değil de, bir sözlük içinden gerçekleştireceğiz. 

Hangi parametrenin hangi listeyi çağıracağını belirleyen sözlüğümüzü yazdıktan
sonra, sözlüklerin ``get()`` metodunu kullanarak, `ölçüt` argümanının değerine
göre sözlükten veri çekiyoruz. Eğer sözlükte bulunmayan bir `ölçüt` değeri
verilirse tüm listeyi ekrana basıyoruz.

Bu arada, eğer `d` sözlüğü içindeki liste üreteçlerinin birbirini tekrar eder
bir yapıda olması sizi rahatsız ediyorsa, bu kısmı bir yardımcı fonksiyon
aracılığıyla sadeleştirebilirsiniz::
    
    liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
             ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
             ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

    def bul(değer, sıra):
        return [li for li in liste if değer == li[sıra]]
        
    def sorgula(ölçüt=None, değer=None):
        d = {'isbn'     : bul(değer, 0),
             'yazar'    : bul(değer, 1),
             'eser'     : bul(değer, 2),
             'yayınevi' : bul(değer, 3)}
             
        for öğe in d.get(ölçüt, liste):
            print(*öğe, sep = ', ')

Burada bütün liste üreteçlerini tek bir ``bul()`` fonksiyonu içinde oluşturarak,
``sorgula()`` fonksiyonu içindeki `d` sözlüğüne gönderdik.

Bu kodları da aynı ilk program örneğinde olduğu gibi kullanıyoruz::
    
    >>> import klist
    >>> klist.sorgula()
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem
    
    >>> klist.sorgula('yazar', 'Nietzsche')
    
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem
    
    >>> klist.sorgula('eser', 'Sana Gül Bahçesi Vadetmedim')
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis 
    
Yukarıdaki kodları yazmanın daha başka alternatifleri de var. Mesela, eğer arzu
ederseniz, yukarıdaki kodları bir sınıf yapısı içinde de ifade edebilirsiniz::
    
    class Sorgu():
        def __init__(self):
            self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                          ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                          ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
                                            
        def bul(self, değer, sıra):
            return [li for li in self.liste if değer == li[sıra]]
    
        def sorgula(self, ölçüt=None, değer=None):
            d = {'isbn'     : self.bul(değer, 0),
                 'yazar'    : self.bul(değer, 1),
                 'eser'     : self.bul(değer, 2),
                 'yayınevi' : self.bul(değer, 3)}
                 
            for öğe in d.get(ölçüt, self.liste):
                print(*öğe, sep = ', ')

Burada kitap listesini bir örnek niteliği olarak tanımlamak suretiyle sınıfın
her yerinden kullanılabilir hale getirdik.

Ardından da ``bul()`` ve ``sorgula()`` adlı fonksiyonları, birer örnek metodu
biçiminde sınıf içine yerleştirdik.

Bu sınıfı da şu şekilde kullanabiliriz::

    >>> import klist
    >>> sorgu = klist.Sorgu()
    >>> sorgu.sorgula()
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem
    
    >>> sorgu.sorgula('yazar', 'Evren')
    
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki

Elbette, bu örnekte, ilk yazdığımız kodları bir sınıf yapısı içinde tarif
etmenin bize pek bir katkısı yok. Burada yaptığımız şey esasında bütün kodları
'Sorgu' adlı bir etki alanı içine taşımaktan fazlası değil. Ama böyle bir
imkanınızın da olduğunu bilmeniz her halükarda sizin için faydalı olacaktır.

Gelelim yukarıdaki kodları yazmanın son alternatifine::

    class Sorgu():
        def __init__(self, değer=None, sıra=None):
            self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                          ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                          ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
            
            if not değer and not sıra:
                l = self.liste
            else:
                l = [li for li in self.liste if değer == li[sıra]]
                
            for i in l:
                print(*i, sep=', ')
    
        @classmethod    
        def isbnden(cls, isbn):
            cls(isbn, 0)
    
        @classmethod    
        def yazardan(cls, yazar):
            cls(yazar, 1)
    
        @classmethod    
        def eserden(cls, eser):
            cls(eser, 2)
    
        @classmethod    
        def yayınevinden(cls, yayınevi):
            cls(yayınevi, 3)
            
Burada da, her bir ölçütü ayrı birer sınıf metodu olarak tanımladık. Böylece bu
ölçütleri yapısal olarak birbirinden ayırmış olduk. Yukarıdaki sınıfı şu şekilde
kullanabiliriz:

Önce modülümüzü içe aktaralım::
    
    >>> from klist import Sorgu
    
ISBN numarasına göre bir sorgu gerçekleştirelim::
    
    >>> Sorgu.isbnden("9789753424080")
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    
Gördüğünüz gibi, sınıf metodu yaklaşımı, gayet temiz bir sorgu kodu üretmemize
imkan tanıyor.

Bir de yazara ve esere göre sorgulayalım::
    
    >>> Sorgu.yazardan("Greenberg")
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    
    >>> Sorgu.eserden("Postmodern Bir Kız Sevdim")
    
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    
Bunlar da gayet güzel görünüyor. 

Şimdi bir de bütün listeyi alalım::
    
    >>> hepsi = Sorgu()
    
    9789753424080, Greenberg, Sana Gül Bahçesi Vadetmedim, Metis
    975872519X, Evren, Postmodern Bir Kız Sevdim, İthaki
    9789754060409, Nietzsche, Böyle Buyurdu Zerdüşt, Cem

Gördüğünüz gibi, sınıfı parametresiz olarak örneklediğimizde bütün listeyi elde
ediyoruz. 

İşte 'alternatif inşa' denen işlem tam olarak budur. Yukarıdaki örnekte
``isbnden()``, ``yazardan()``, ``eserden()`` ve ``yayınevinden()`` adlı sınıf
metotları, ``Sorgu()`` adlı sınıfı alternatif şekillerde inşa etmemizi sağlıyor [#]_.

Normal şartlarda, bir sınıfı, ``__init__()`` fonksiyonuna verdiğimiz
parametreler aracılığıyla inşa ediyoruz (birkaç sayfa sonra 'inşa' kavramından
daha ayrıntılı olarak bahsedeceğiz).

Mesela::
    
    class Giriş():
        def __init__(self, mesaj='Müşteri numaranız: '):
            cevap = input(mesaj)
            print('Hoşgeldiniz!')
            
Burada tanımladığımız `Giriş()` sınıfı, bir müşteri numarası aracılığıyla
sisteme giriş imkanı sağlıyor::

    >>> from sistem import Giriş #kodlarımız sistem.py dosyası içinde
    >>> Giriş()

Eğer biz aynı zamanda bir parola ve TC Kimlik Numarası ile de giriş imkanı
sağlamak istersek, başka yöntemlerin yanısıra, sınıf metotlarından da
yararlanabiliriz::
    
    class Giriş():
        def __init__(self, mesaj='Müşteri numaranız: '):
            cevap = input(mesaj)
            print('Hoşgeldiniz!')
                
        @classmethod
        def paroladan(cls):
            mesaj = 'Lütfen parolanızı giriniz: '
            cls(mesaj) 
    
        @classmethod
        def tcknden(cls):
            mesaj = 'Lütfen TC kimlik numaranızı giriniz: '
            cls(mesaj)
            
Bu şekilde yukarıdaki sınıfı aşağıdaki gibi de inşa etme imkanına kavuşuyoruz::
    
    >>> Giriş.paroladan()
    
veya::
    
    >>> Giriş.tcknden()
    
Sınıf metotları içinde kullandığımız ``cls(mesaj)`` satırları, `Giriş()` adlı
sınıfı farklı bir parametre ile çağırmamızı sağlıyor. Gördüğünüz gibi, bu
sınıfın `mesaj` parametresinin öntanımlı değeri `'Müşteri numaranız: '`.
Sınıfımızı farklı bir şekilde çağırabilmek için, ``cls(mesaj)`` kodları
yardımıyla sınıfın `mesaj` parametresini `'Lütfen parolanızı giriniz: '` ve
`'Lütfen TC kimlik numaranızı giriniz: '` değerleri ile yeniden çalıştırıyoruz.

Daha önce de birkaç kez vurguladığımız gibi, `cls` kelimesi Python açısından bir
zorunluluk değildir. Yani yukarıdaki sınıfı mesela şöyle de yazabilirdik::
    
    class Giriş():
        def __init__(self, mesaj='Müşteri numaranız: '):
            cevap = input(mesaj)
            print('Hoşgeldiniz!')
                
        @classmethod
        def paroladan(snf):
            mesaj = 'Lütfen parolanızı giriniz: '
            snf(mesaj) 
    
        @classmethod
        def tcknden(snf):
            mesaj = 'Lütfen TC kimlik numaranızı giriniz: '
            snf(mesaj)

Ancak, tıpkı `self` kelimesinde olduğu gibi, `cls` de Python topluluğu içinde
son derece yerleşik bir gelenektir. Bu geleneği bozmak isteyeceğinizi
zannetmiyorum.

İlk bakışta sınıf metotları size pek gerekli değilmiş gibi gelebilir. Ama eğer
bu metotların gerçek dünyadaki kullanımına ilişkin bir örnek verirsek belki
fikriniz değişir.

Sınıf metotlarının kullanımına ilişkin güzel bir örneği `datetime` modülünde
görebilirsiniz. 

.. seealso:: Aşağıdaki örneği daha iyi anlayabilmek için
 :doc:`standart_moduller/datetime` ve :doc:`standart_moduller/time` belgelerine
 bakınız.

Bir standart kütüphane modülü olan `datetime`'ın kaynak dosyasını açarsanız
(kaynak dosyanın nerede olduğunu nasıl öğrenebilirim diye soran arkadaşlara
teessüflerimi iletiyorum...), orada `date` sınıfının şöyle yazıldığını
göreceksiniz::
    
    class date:
        __slots__ = '_year', '_month', '_day'
    
        def __new__(cls, year, month=None, day=None):
            if (isinstance(year, bytes) and len(year) == 4 and
                1 <= year[2] <= 12 and month is None):  # Month is sane
                # Pickle support
                self = object.__new__(cls)
                self.__setstate(year)
                return self
            _check_date_fields(year, month, day)
            self = object.__new__(cls)
            self._year = year
            self._month = month
            self._day = day
            return self
        
        @classmethod
        def fromtimestamp(cls, t):
            y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
            return cls(y, m, d)
    
        @classmethod
        def today(cls):
            t = _time.time()
            return cls.fromtimestamp(t)
    
        @classmethod
        def fromordinal(cls, n):
            y, m, d = _ord2ymd(n)
            return cls(y, m, d)

Gördüğünüz gibi, burada üç tane sınıf metodu var::
    
        @classmethod
        def fromtimestamp(cls, t):
            ...
    
        @classmethod
        def today(cls):
            ...
    
        @classmethod
        def fromordinal(cls, n):
            ...
            
Normal şartlarda `datetime` modülü içindeki `date` sınıfını şu şekilde
kullanıyoruz::
    
    >>> import datetime
    >>> bugün = datetime.date(2015, 6, 16)
    
Bu şekilde, `date` sınıfına sırasıyla yıl, ay ve gün bilgisi girerek `bugün`
adlı bir tarih nesnesi oluşturmuş oluyoruz. Bu şekilde herhangi bir tarihi elle
oluşturabilirsiniz.

Eğer amacınız bugünün tarihini oluşturmaksa, yıl, ay ve gün bilgilerini
yukarıdaki gibi `date` sınıfına elle girebileceğiniz gibi, ``today()`` adlı
sınıf metodunu da kullanabilirsiniz::
    
    >>> bugün = datetime.date.today()
    
İşte böylece, `date` sınıfının size sunduğu bir alternatif inşacı
(``today()``) vasıtasıyla bugünün tarihini otomatik olarak elde etmiş oldunuz. 

Aynı şekilde, eğer elinizde bir zaman damgası varsa ve siz bu zaman damgasından
bir tarih elde etmek istiyorsanız yine `date` sınıfının sunduğu bir başka
alternatif inşacıdan yararlanabilirsiniz:

    >>> import time
    >>> zaman_damgası = time.time()
    >>> bugün = datetime.date.fromtimestamp(zaman_damgası)
    
Eğer elinizde tam sayı biçimli bir Gregoryen tarih verisi varsa bu veriyi
kullanarak da bir tarih nesnesi elde edebilirsiniz::
    
    >>> gregoryen = 735765
    >>> bugün = datetime.date.fromordinal(gregoryen)
    
    datetime.date(2015, 6, 16)
    
Uzun lafın kısası, alternatif inşacılar, bir sınıftan nesne oluşturmak için bize
alternatif yollar sunan son derece faydalı araçlardır. Bu arada, eğer bu bölümde
değindiğimiz bazı kavramları anlamakta zorlandıysanız hiç canınızı sıkmayın. Bir
sonraki bölümü işledikten sonra, burada anlatılanlar kafanıza çok daha sağlam
bir şekilde yerleşmiş olacak.

Statik Metotlar
****************

Python'da örnek metotları ve sınıf metotları dışında bir de statik metotlar
bulunur. Bildiğiniz gibi, örnek nitelikleri üzerinde işlem yapacağımız zaman
örnek metotlarını kullanıyoruz. Aynı şekilde sınıf nitelikleri üzerinde işlem
yapacağımız zaman ise sınıf metotlarından faydalanıyoruz. Örnek metotları içinde
herhangi bir örnek niteliğine erişmek istediğimizde `self` kelimesini
kullanıyoruz. Sınıf metotları içinde bir sınıf niteliğine erişmek için ise
`cls` kelimesini kullanıyoruz. İşte eğer bir sınıf içindeki herhangi bir
fonksiyonda örnek veya sınıf niteliklerinin hiçbirine erişmeniz gerekmiyorsa,
statik metotları kullanabilirsiniz.

@staticmethod Bezeyicisi
************************

Buraya gelene kadar öğrendiğimiz örnek ve sınıf metotlarını nasıl
kullanacağımızı biliyorsunuz::
    
    class Sınıf():
        sınıf_niteliği = 0
        
        def __init__(self, veri):
            self.veri = veri
            
        def örnek_metodu(self):
            return self.veri
           
        @classmethod
        def sınıf_metodu(cls):
            return cls.sınıf_niteliği
            
Burada ``örnek_metodu()``, `self` yardımıyla örnek niteliklerine erişiyor.
``sınıf_metodu()`` ise `cls` yardımıyla sınıf niteliklerine erişiyor. Sınıf
metodu tanımlamak için ayrıca `@classmethod` bezeyicisini de kullanıyoruz. İşte
eğer sınıf içinde tanımlayacağınız fonksiyon herhangi bir örnek ya da sınıf
niteliği üzerinde herhangi bir işlem yapmayacaksa şöyle bir şey yazabilirsiniz::
    
    class Sınıf():
        sınıf_niteliği = 0
        
        def __init__(self, veri):
            self.veri = veri
            
        def örnek_metodu(self):
            return self.veri
           
        @classmethod
        def sınıf_metodu(cls):
            return cls.sınıf_niteliği
            
        @staticmethod
        def statik_metot():
            print('merhaba statik metot!')
            
Gördüğünüz gibi, statik metotları tanımlamak için `@staticmethod` bezeyicisini
kullanıyoruz. Statik metotlar, ilk parametre olarak `self` veya `cls` benzeri
kelimeler almaz. Çünkü bu tür sınıfların örnek veya sınıf nitelikleri ile
herhangi bir işi yoktur.

Peki statik metotlar ne işe yarar? 

Bu metotlar sınıf metotlarına çok benzer. Tıpkı sınıf metotlarında olduğu gibi,
anlamsal olarak sınıfla ilgili olan, ancak sınıf metotlarının aksine bu sınıfın
herhangi bir niteliğine erişmesine gerek olmayan fonksiyonları, sınıf dışına
atmak yerine, birer statik metot olarak sınıf içine yerleştirebiliriz.

Basit bir örnek verelim::

    class Mat():
        '''Matematik işlemleri yapmamızı sağlayan
        bir sınıf.'''
        
        @staticmethod
        def pi():
            return 22/7
        
        @staticmethod
        def karekök(sayı):
            return sayı ** 0.5
        
Burada ``Mat()`` adlı bir sınıf tanımladık. Bu sınıf içinde iki adet statik
metodumuz var: ``pi()`` ve ``karekök()``. Gördüğünüz gibi, bu iki fonksiyon,
örnek ve sınıf metotlarının aksine ilk parametre olarak `self` veya `cls`
almıyor. Çünkü bu iki sınıfın da sınıf veya örnek nitelikleriyle herhangi bir
işi yok. 

Statik metotları hem örnekler hem de sınıf adları üzerinden kullanabiliriz.

Yukarıdaki kodların `mat.py` adlı bir dosyada yer aldığını varsayarsak::
    
    >>> from mat import Mat
    >>> m = Mat()
    >>> m.pi() #örnek üzerinden
    
    3.142857142857143
    
    >>> m.karekök(144) #örnek üzerinden
    
    12.0
    
    >>> Mat.pi() #sınıf üzerinden
    3.142857142857143
    
    >>> Mat.karekök(144) #sınıf üzerinden
    
    12.0
    
Statik metotların özellikle sınıf adları üzerinden kullanılabilmesi, bu tür
metotları epey kullanışlı hale getirir. Böylece sınıfı örneklemek zorunda
kalmadan, sınıf içindeki statik metotlara ulaşabiliriz. 

Elbette eğer isteseydik biz bu fonksiyonları şöyle de tanımlayabilirdik::
    
    class Mat():  
        '''Matematik işlemleri yapmamızı sağlayan
        bir sınıf.'''
        
        def pi(self):
            return 22/7
        
        def karekök(self, sayı):
            return sayı ** 0.5
            
Burada bu iki fonksiyonu birer örnek metodu olarak tanımladık. Bu fonksiyonları
bu şekilde tanımladığımızda, bunlara örnekler üzerinden erişebiliriz::
       
    >>> from mat import Mat
    >>> m = Mat()
    >>> m.pi()
    
    3.142857142857143
    
    >>> m.karekök(144)
    
    12.0
    
Ancak bildiğiniz gibi, örnek metotlarına sınıf adları üzerinden erişemeyiz::
    
    >>> Mat.pi()
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: pi() missing 1 required positional argument: 'self'
    
Aynı şekilde bunları sınıf metodu olarak da tanımlayabilirdik::
    
    class Mat(): 
        '''Matematik işlemleri yapmamızı sağlayan
        bir sınıf.'''
        
        @classmethod
        def pi(cls):
            return 22/7
        
        @classmethod
        def karekök(cls, sayı):
            return sayı ** 0.5
            
Bu metotları böyle tanımladığımızda, bu metotlara hem örnekler üzerinden hem de
sınıf adı üzerinden erişebiliriz::
    
    >>> from mat import Mat
    >>> m = Mat()
    >>> m.pi() #örnek üzerinden
    
    3.142857142857143
    
    >>> m.karekök(144) #örnek üzerinden
    
    12.0
    
    >>> Mat.pi() #sınıf üzerinden
    3.142857142857143
    
    >>> Mat.karekök(144) #sınıf üzerinden
    
    12.0
    
Gördüğünüz gibi, kullanım açısından sınıf metotları ile statik metotlar aynı.
Ancak ``Mat()`` sınıfı içindeki fonksiyonları birer sınıf metodu olarak
tanımladığımızda gereksiz yere `cls` parametresi kullanmış oluyoruz. Fonksiyon
içinde herhangi bir yerde kullanılmadığı için, yukarıdaki örnekte `cls`
parametresinin hiçbir amaca hizmet etmediğine dikkat edin.

Statik metotların çok sık kullanılan araçlar olmadığını da belirterek yolumuza
devam edelim.

.. rubric:: Dipnotları:

.. [#] Aslında burada inşa edilen şey sınıftan ziyade nesnedir. Bu durumu ve
 'nesne' kavramını bir sonraki bölümde ayrıntılı olarak ele alacağız.