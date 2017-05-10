.. meta::
   :description: Bu bölümde os modülünü inceleyeceğiz. 
   :keywords: python, modül, import, os

.. highlight:: py3

os Modülü
***************

Bildiğiniz gibi, işletim sistemlerinin çalışma mantığı birbirinden farklıdır.
Örneğin Windows ve GNU/Linux işletim sistemleri aynı işi birbirlerinden farklı
şekillerde yaparlar. Mesela Windows'ta bir dizin içinde hangi klasör ve
dosyaların olduğunu öğrenmek için ``dir`` komutunu kullanırız. GNU/Linux'ta ise
aynı işlev için ``ls`` adlı bir komut vardır.

Aynı şekilde, iki işletim sistemi arasında dizin ayraçları konusunda da
farklılık bulunur. Windows'ta dizinleri birbirinden ayırmak için ters taksim
(**\\**) işareti kullanılırken, GNU/Linux'ta aynı iş için düz taksim (**/**)
işareti kullanılır.

.. note:: Düz taksim işaretini Windows da kabul eder, ancak Windows'un doğal
    dizin ayracı ters taksimdir. 

İşte biz hem Windows'ta, hem de GNU/Linux'ta çalışacak bir program yazmak
istediğimizde bu farklılıkları göz önünde bulundurmamız ve farklı durumların
herbiri için ayrı kodlar yazmamız gerekirken, ``os`` modülü bizi bu zahmetten
kurtarır ve bize ortak bir arayüz üzerinden farklı işletim sistemleri ile
tutarlı bir şekilde iletişim kurabilmemizi sağlayacak pek çok fonksiyon ve
nitelik sunar.

Bu nitelik ve fonksiyonların neler olduğunu ``dir(os)`` komutuyla
görebileceğinizi biliyorsunuz.

Bu bölümde, ``os`` modülünün sunduğu bu fonksiyon ve niteliklerin en
önemlilerini ve en yaygın kullanılanlarını olabildiğince ayrıntılı bir şekilde
ele almaya çalışacağız.

.. note:: Burada ``os`` modülünü ``import os`` komutuyla içe aktarmış olduğunuz
    varsayılmaktadır.

os.name
========

``os`` modülünün, önceki derslerde şöyle bir değinip geçtiğimiz `name` niteliği,
kullanıcılarımızın, yazdığımız kodları hangi işletim sisteminde çalıştırdığı
konusunda bize bilgi verir.

Bu niteliği şöyle kullanıyoruz::
    
    >>> os.name

Eğer kodlarımız Windows işletim sistemi üzerinde çalıştırılmışsa buradan şu
çıktıyı alırız::
    
    'nt'
    
MacOS ve GNU/Linux işletim sistemleri ise bu komuta şu cevabı verir::
    
    'posix'
    
Dolayısıyla ``os.name`` niteliğini kullanarak farklı işletim sistemlerinde
farklı çalışan programlar yazabiliriz.

os.sep
========

``os`` modülünün `sep` niteliği, kodlarımızın çalıştığı işletim sisteminin dizin
ayracının ne olduğunu bize gösterir.
    
Eğer bu niteliği Windows işletim sistemi üzerinde kullanırsak şu çıktıyı
alırız::
    
    >>> os.sep
    
    '\\'
    
MacOS ve GNU/Linux işletim sistemleri ise bu komuta şu cevabı verir::
    
    >>> os.sep
    
    '/'
    
Peki bu nitelik ne işe yarar?

Bu niteliği kullanarak, farklı işletim sistemlerine özgü dizin yolları
oluşturabilirsiniz. Mesela::
    
    >>> liste = ['aylar', 'mayıs', 'test']
    >>> os.sep.join(liste)
    
Burada karakter dizilerinin ``join()`` metodunu ``os.sep`` ile birlikte
kullandığımıza dikkat edin. 
    
Bu komutu Windows'ta verdiğinizde şu çıktıyı alırsınız::
    
    'aylar\\mayıs\\test'
    
Aynı komutu GNU/Linux'ta verdiğinizde ise şu çıktıyı::

    'aylar/mayıs/test'
    
Yani yukarıdaki komutu Windows'ta verdiğinizde Python şu komutu almış gibi
davranır::
    
    >>> liste = ['aylar', 'mayıs', 'test']
    >>> '\\'.join(liste)
    
GNU/Linux'ta ise şu komutu::
    
    >>> liste = ['aylar', 'mayıs', 'test']
    >>> '/'.join(liste)
    
Böylece yazdığınız programlarda hangi işletim sisteminin hangi dizin ayracını
kullandığını düşünmenize gerek kalmaz; bunu sizin yerinize Python düşünür...

os.getcwd()
============

``os`` modülünün ``getcwd()`` fonksiyonu bize o anda içinde bulunduğumuz dizinin
adını verir::
    
    >>> os.getcwd()
    
    '/home/istihza/Desktop' #GNU/Linux
    
veya::
    
    >>> os.getcwd()
    
    'C:\\Documents and Settings\\fozgul' #Windows
    
os.chdir()
============

``os`` modülünün ``chdir()`` fonksiyonu bize bir dizinden başka bir dizine geçme
imkanı verir.

Mesela GNU/Linux'ta, o anda bulunduğumuz dizinden `/usr/bin` adlı dizine geçmek
için şu komutu kullanabiliriz::
    
    >>> os.chdir('/usr/bin/')
    
veya Windows'ta `C:\\Documents and Settings\\fozgul\\Desktop` adlı dizine geçmek
için şunu::
    
    >>> os.chdir('C:\\Documents and Settings\\fozgul\\Desktop')
    
Gördüğünüz gibi, gitmek istediğimiz dizin adını ``os.chdir()`` fonksiyonuna
parametre olarak vermemiz yeterli oluyor. 

os.listdir()
==============

``os`` modülünün ``listdir()`` fonksiyonu, bize bir dizin içindeki dosya ve
klasörleri listeleme imkanı verir. ``listdir()``, ``os`` modülünün en kullanışlı
fonksiyonlarından biridir. 

Mesela o anda içinde bulunduğumuz dizindeki dosya ve klasörleri listelemek
istersek bu fonksiyonu şöyle kullanabiliriz::
    
    >>> mevcut_dizin = os.getcwd()
    >>> os.listdir(mevcut_dizin)
    
Eğer farklı bir dizinin içeriğini listelemek istersek, parametre olarak o
dizinin adını yazmamız yeterli olacaktır::
    
    >>> os.listdir('/var/www')
    
Gördüğünüz gibi, ``os.listdir()`` komutunun çıktısı liste türünde bir veri
tipidir. Dolayısıyla listelerle yapabildiğiniz her şeyi bununla da
yababilirsiniz. Mesela bu liste üzerinde bir döngü kurabilirsiniz::
    
    >>> for i in os.listdir(os.getcwd()):
    ...     print(i)
    
Ya da bir dizin içindeki, belli bir uzantıya sahip dosyaları süzebilirsiniz::
    
    >>> for i in os.listdir(os.getcwd()):
    ...     if i.endswith('.doc'):
    ...         print(i)
    
Bu kodlar bize, adı `.doc` ile biten bütün dosyaları listeleyecektir. 

Bu arada karakter dizilerinin ``endswith()`` adlı metodunu hatırlıyorsunuz,
değil mi?

os.curdir
==========

Çoğu işletim sisteminde mevcut dizini göstermek için '.' adlı karakter dizisi
kullanılır. Örneğin::
    
    >>> os.listdir(os.getcwd())
    
gibi bir komut yerine şu komutu da kullanabilirsiniz::
    
    >>> os.listdir('.')
    
``listdir()`` fonksiyonuna parametre olarak verdiğimiz '.' karakter dizisi o
anda içinde bulunduğumuz dizini temsil eder. 

Eğer bu karakter dizisini elle yazmak istemiyorsanız ``os`` modülü içindeki
`curdir` adlı nitelikten de yararlanabilirsiniz::
    
    >>> os.listdir(os.curdir)
    
Bu arada ``os.getcwd()`` ile `os.curdir`'i birbirine karıştırmamalısınız. Bu
ikisi aynı şey değildir. ``os.getcwd()`` çıktı olarak o anda içinde bulunduğumuz
dizinin adını verir. `os.curdir` ise, bir işletim sisteminde, o anda içinde
bulunulan dizini temsil eden karakter dizisi ne ise onun değerini barındırır. Bu
değer çoğu işletim sisteminde '.' adlı karakter dizisidir.

os.pardir
===========

Tıpkı '.' karakter dizisi gibi, çoğu işletim sisteminde bir üst dizini göstermek
için '..' adlı karakter dizisi kullanılır. Örneğin::
    
    >>> os.listdir('..')
    
komutu, o anda içinde bulunduğunuz dizindeki değil, bir üst dizindeki dosya ve
dizin adlarını listeleyecektir. Yine tıpkı `os.curdir` niteliğinde olduğu gibi,
eğer bu karakter dizisini kendiniz elle yazmak istemezseniz, bu karakter
dizisini içinde barındıran `os.pardir` adlı bir nitelikten yararlanabilirsiniz::
    
    >>> os.listdir(os.pardir)
    
Bu komut, ``os.listdir('..')`` ile aynı çıktıyı verir.

os.startfile()
===============

.. warning:: Bu fonksiyon yalnızca Windows'ta çalışır. GNU/Linux işletim
    sistemlerinde bu fonksiyon tanımlı değildir.
    
``os`` modülü içindeki ``startfile()`` adlı fonksiyonun görevi bilgisayarımızda
bulunan herhangi bir dosyayı, ilişkilendirilmiş olduğu programla açmaktır.

Hemen bir örnek verelim.

O anda içinde bulunduğumuz dizinde `deneme.txt` adlı bir dosya olduğunu
varsayalım. Şimdi de şu komutu verelim::
    
    >>> os.startfile('deneme.txt')
    
İşletim sisteminiz `.txt` uzantılı dosyaları hangi programla ilişkilendirmişse,
``startfile()`` fonksiyonu `deneme.txt` adlı dosyayı o programla açacaktır.
Windows'ta `.txt` dosyaları genellikle Notepad programıyla ilişkilendirildiği
için yukarıdaki komutu verdiğinizde muhtemelen `deneme.txt` dosyasının içeriği
Notepad programı aracılığıyla görüntülenecektir. 

Aynı şekilde, o anda bulunduğuz dizin içinde `deneme.docx` adlı bir dosyanın
olduğunu varsayalım ve şu komutu verelim::
    
    >>> os.startfile('deneme.docx')
    
Bu komut da `deneme.docx` dosyasının Microsoft Word adlı yazılımla açılmasını
sağlayacaktır. 

Eğer ``startfile()`` fonksiyonuna parametre olarak bir dosya değil de dizin adı
verecek olursanız, o dizin Windows Explorer ile açılır. Mesela içinde
bulunduğumuz dizini Windows Explorer ile açalım::
    
    >>> os.startfile(os.curdir)
    
Bunun yerine şu komutu kullanabileceğinizi de biliyorsunuz::
    
    >>> os.startfile('.')
    
veya::
    
    >>> os.startfile(os.getcwd())
    
Bu üç komut da aynı işlevi yerine getirir.

Peki bir üst dizini açmak istersek ne yapacağız?

Dikkatlice bakın::
    
    >>> os.startfile(os.pardir)
    
veya::
    
    >>> os.startfile('..')
    
Her iki komut da Windows Explorer yardımıyla bir üst dizinin görüntülenmesini
sağlayacaktır.

Elbette ``startfile()`` fonksiyonuna parametre olarak belirli bir dizinin adını
da verebilirsiniz::
    
    >>> os.startfile(r"C:\Documents and Settings\fozgul")
    
``os.startfile()`` oldukça faydalı bir fonksiyondur. Hatta bu fonksiyonu sadece
dosyaları açmak için değil, internet sayfalarını açmak için dahi
kullanabilirsiniz::
    
    >>> os.startfile('www.istihza.com')
    
Ancak bu komutun yalnızca Windows'ta çalışacağını unutmayın. O yüzden bunun
yerine, daha önce öğrendiğimiz ``webbrowser`` modülünü kullanmak daha doğru
olacaktır.

os.mkdir()
============

``os`` modülünün ``mkdir()`` fonksiyonu yeni dizinler oluşturabilmemizi sağlar. 

Örneğin::
    
    >>> os.mkdir('yenidizin')
    
Bu komut, o anda içinde bulunduğumuz dizin içinde 'yenidizin' adlı bir dizin
oluşturacaktır. 

Elbette eğer dizini o anda içinde bulunduğunuz dizin içinde değil de farklı bir
konumda oluşturmak isterseniz, o konumun açık adresini belirtebilirsiniz::
    
    >>> os.mkdir('/home/istihza/Desktop/yenidizin')
    
veya::
    
    >>> os.mkdir(r'C:\Documents and Settings\fozgul\yenidizin')
    
Eğer oluşturmaya çalıştığınız dizin zaten varsa ``os.mkdir()`` hata verecektir::
    
    >>> os.mkdir(r'C:\Documents and Settings\fozgul\yenidizin')

    FileExistsError: [WinError 183] Halen varolan bir 
    dosya oluşturulamaz: 'yenidizin'
    
os.makedirs()
=============

``os.makedirs()`` fonksiyonu biraz önce öğrendiğimiz ``os.mkdir()`` fonksiyonuna
çok benzese de aralarında önemli farklar bulunur. 

Biraz önce ``os.mkdir()`` fonksiyonunu anlatırken şöyle bir örnek vermiştik::
    
    >>> os.mkdir(r'C:\Documents and Settings\fozgul\yenidizin')
    
Bu komutun çalışabilmesi için, bilgisayarımızda halihazırda `C:\Documents and
Settings\fozgul\` yolunun varolması gerekir. Eğer bu yolu oluşturan dizinlerden
herhangi biri mevcut değilse, ``mkdir()`` fonksiyonu `yenidizin` adlı dizini
oluşturamaz. Bu fonksiyonun çalışabilmesi için, varolmayan bütün dizinleri tek
tek oluşturmanız gerekir. 

``os.makedirs()`` ise ``os.mkdir()`` fonksiyonunun aksine, varolmayan üst ve alt
dizinleri de oluşturma yeteneğine sahiptir. Örneğin::
    
    >>> os.makedirs('/home/istihza/Desktop/aylar/mayıs/ödeme/')
    
Bu komut sırasıyla `aylar`, `mayıs` ve `ödeme` adlı dizinleri iç içe
oluşturacaktır. Yani ``os.makedirs()`` komutunun `ödeme` adlı dizini oluşturması
için `aylar` ve `mayıs` adlı dizinlerin önceden varolması zorunlu değildir. Bu
dizinler varolsa da olmasa da ``os.makedirs()`` komutu `ödeme` dizinini
oluşturabilir. Ama ``os.mkdir()`` fonksiyonu böyle değildir. Eğer ``os.mkdir()``
fonksiyonuyla `ödeme` dizinini oluşturmak isterseniz, öncelikle `aylar` ve
`mayıs` adlı dizinleri oluşturmanız gerekir. 
    
os.rename()
===========

``os`` modülünün ``rename()`` adlı fonksiyonunu kullanarak dizinlerin adlarını
değiştirebiliriz. Bu fonksiyon iki parametre alır::
    
    >>> os.rename('dizinin_şimdiki_adı', 'dizinin_yeni_adı')
    
Mesela mevcut çalışma dizininde 'deneme' adlı bir dizin varsa, bu dizinin adını
'test' olarak değiştirmek için şu komutu verebiliriz::
    
    >>> os.rename('deneme', 'test')
    
Eğer zaten 'test' adlı bir dizin varsa (ve içi boşsa), yukarıdaki komut
GNU/Linux'ta 'test' adlı dizinin üzerine yazacak, Windows'ta ise hata
verecektir.  

os.replace()
==============

``os`` modülünün ``replace()`` fonksiyonu biraz önce öğrendiğimiz ``rename()``
fonksiyonu gibi çalışır:: 

    >>> os.replace('deneme', 'test')
    
Bu komut, tıpkı ``rename()`` fonksiyonunda olduğu gibi, `deneme` adlı dizinin
adını `test` olarak değiştirecektir.

Eğer `test` adlı bir dizin zaten varsa, ``replace()`` fonksiyonu, hem Windows'ta
hem de GNU/Linux'ta, varolan bu `test` dizininin üzerine yazmaya çalışır.
GNU/Linux'ta çoğu durumda bunu başarır, ancak Windows'ta yine de çeşitli izin
hataları ile karşılaşabilirsiniz.

os.remove()
============

``os`` modülünün ``remove()`` adlı fonksiyonu, bilgisayarımızdaki dosyaları
silmemizi sağlar::
    
    >>> os.remove('dosya_adı')
    
Yalnız bu komutu çok dikkatli kullanmalısınız. Çünkü bu komut, silme işleminden
önce herhangi bir soru sormadan, dosyayı doğrudan siler.

os.rmdir()
===========

``os`` modülünün ``rmdir()`` fonksiyonu, içi boş bir dizini silmek için
kullanılır:: 

    >>> os.rmdir('dizin_adı')

Eğer silmeye çalıştığınız dizin içinde herhangi bir başka dizin veya dosya varsa
bu fonksiyon hata verecektir.

Mesela şöyle bir dizin yapısı düşünelim::
    
    |___ anadizin
        |___ dizin1
            |___ dizin2
                |___ dizin3
                    |___ dizin4
                    
Bu arada, bu dizin yapısını kolayca oluşturmak için ne yapmanız gerektiğini
biliyorsunuz::
    
    >>> os.makedirs('anadizin/dizin1/dizin2/dizin3/dizin4')
 
Anadizin altındayken şu komutlar hata verecektir::
    
    >>> os.rmdir('anadizin')
    >>> os.rmdir(r'anadizin/dizin1')
    >>> os.rmdir(r'anadizin/dizin1/dizin2/dizin3')
    
Çünkü bu dizinlerinin hiçbirinin içi boş değil; her birinin içinde birer dizin
var. Ama şu komut başarılı olacaktır::
    
    >>> os.rmdir(r'anadizin/dizin1/dizin2/dizin3/dizin4')
    
Bu şekilde yukarı doğru ilerleyerek sırayla bütün dizinleri silebilirsiniz::
    
    >>> os.rmdir(r'anadizin/dizin1/dizin2/dizin3/')
    >>> os.rmdir(r'anadizin/dizin1/dizin2/')
    >>> os.rmdir(r'anadizin/dizin1')
    >>> os.rmdir(r'anadizin/')

os.removedirs()
===============

``os`` modülünün ``removedirs()`` fonksiyonu, içi boş dizin yollarını silmemizi
sağlar. Peki bu ne demek?

Diyelim ki elimizde şöyle bir dizin yapısı var::
    
    |___ anadizin
        |___ dizin1
            |___ dizin2
                |___ dizin3
                    |___ dizin4
                
Anadizin altından şu komutu verdiğimizde::
    
    >>> os.removedirs('anadizin/dizin1/dizin2/dizin3/dizin4')
    
Eğer bütün dizinlerin içi boşsa, `anadizin`'den `dizin4`'e kadar olan bütün
dizinler (`anadizin` ve `dizin4` dahil) silinecektir.

os.stat()
============

``os`` modülünün ``stat()`` fonksiyonu dosyalar hakkında bilgi almamızı sağlar.
Bu fonksiyonu kullanarak bir dosyanın boyutunu, oluşturulma tarihini,
değiştirilme tarihini ve erişilme tarihini sorgulayabiliriz.

``stat()`` fonksiyonunu şöyle kullanıyoruz::
    
    >>> dosya = os.stat('dosya_adı')
    >>> dosya
    
Buradan şuna benzer bir çıktı alırız::
    
    os.stat_result(st_mode=33279, st_ino=17732923532961356, 
    st_dev=1745874298, st_nlink=1, st_uid=0, st_gid=0, 
    st_size=495616, st_atime=1416488851, st_mtime=1415275662, 
    st_ctime=1415275658)
    
Bu, kendi içinde birtakım nitelikler barındıran özel bir veri tipidir. Bu veri
tipinin barındırdığı nitelikleri görmek için, her zaman olduğu gibi ``dir()``
fonksiyonundan yararlanabilirsiniz::
    
    dir(dosya)
    
Burada özellikle işimize yarayacak olan nitelikler şunlardır:

    :`st_atime`: dosyaya en son erişilme tarihi
    :`st_ctime`: dosyanın oluşturulma tarihi (Windows'ta)
    :`st_mtime`: dosyanın son değiştirilme tarihi
    :`st_size`: dosyanın boyutu
    
Mesela bir dosyanın boyutunu öğrenmek için `st_size` niteliğini şu şekilde
kullanabiliriz::
    
    >>> dosya = os.stat('dosya_adı')
    >>> dosya.st_size
    
Bu fonksiyon bize 'bayt' cinsinden bir çıktı verir. Bunu kilobayta çevirmek
için, bu değeri 1024'e bölebilirsiniz::
    
    >>> dosya.st_size / 1024
    
``os`` modülünün ``stat()`` fonksiyonunu kullanarak bir dosyanın oluşturulma,
erişilme ve değiştirilme tarihlerini de elde edebilirsiniz::
    
    >>> dosya = os.stat('dosya_adı')
    >>> dosya.st_ctime #oluşturulma tarihi
    >>> dosya.st_atime #erişilme tarihi
    >>> dosya.st_mtime #değiştirme tarihi
    
.. warning:: GNU/Linux'ta bir dosyanın ne zaman oluşturulduğunu öğrenmek mümkün
    değildir. Dolayısıyla ``dosya.st_ctime`` komutu yalnızca Windows'ta bir dosyanın
    oluşturulma tarihi verir. Bu komutu GNU/Linux'ta verdiğimizde elde edeceğimiz
    şey dosyanın son değiştirilme tarihidir.
    
Bu arada, yukarıdaki komutların çıktısı size anlamsız gelmiş olabilir. Birazdan,
``datetime`` adlı bir modülü öğrendiğimizde bu anlamsız görünen sayıları anlamlı
tarih bilgilerine nasıl dönüştüreceğimizi de anlatacağız.

os.system()
============

``os`` modülünün ``system()`` fonksiyonu Python içinden sistem komutlarını veya
başka programları çalıştırabilmemizi sağlar. Mesela::
    
    >>> os.system('notepad.exe')

os.urandom()
==============

``os`` modülünün ``urandom()`` fonksiyonu rastgele bayt dizileri elde etmek için
kullanılabilir::
    
    >>> os.urandom(12)
    
Bu komut, 12 bayttan oluşan rastgele bir dizi oluşturur. Buradan elde ettiğiniz
rastgele değeri kriptografik çalışmalarda veya rastgele parola üretme
işlemlerinde kullanabilirsiniz.

os.walk()
==========

Hatırlarsanız önceki sayfalarda ``os`` modülü içindeki ``listdir()`` adlı bir
fonksiyondan söz etmiştik. Bu fonksiyon, bir dizinin içeriğini listeleme imkanı
veriyordu bize. Mesela o anda içinde bulunduğumuz dizinde hangi dosya ve
alt dizinlerin olduğunu öğrenmek için şöyle bir komut kullanabiliyorduk::
    
    >>> os.listdir('.')

    ['build.py', 'gtk', 'kitap', 'make.bat', 'Makefile', 
     'meta_conf.py', 'py2', 'py3', 'theme', 'tk2', '__pycache__']

Gördüğünüz gibi bu fonksiyon yalnızca kendisine parametre olarak verilen dizinin
içeriğini listeliyor. Örneğin yukarıdaki çıktıda görünen `gtk`, `kitap`,
`py2`, `py3`, `theme`, `tk2` ve `\__pycache\__` birer dizin. Ama ``listdir()``
fonksiyonu bu dizinlerin de içine girip buradaki içeriği listelemeye çalışmıyor.
Eğer biz mesela `theme` dizininin içeriğini de listelemek istersek bunu açıkça
belirtmemiz gerekir::
    
    >>> os.listdir('theme')
    
    ['layout.html', 'localtoc.html', 'pydoctheme', 
     'sidebar.html', 'static']
    
Veya `theme` dizini içindeki `static` adlı dizine de erişmek istersek bunu da şu
şekilde açık açık ifade etmemiz gerekir:: 
   
    >>> os.listdir('theme/static')
    
    ['basic.css', 'copybutton.js', 'py.png', 'sidebar.js']

Peki ya biz o anda içinde bulunduğumuz dizinden itibaren içe doğru bütün
dizinleri otomatik olarak taramak istersek ne yapacağız? 

Bunun için ``listdir()`` fonksiyonunu kullanarak özyinelemeli (recursive) bir
fonksiyon yazabilirsiniz::
    
    import os
    
    def tara(dizin):
        başlangıç = os.getcwd()
        dosyalar = []
        os.chdir(dizin)
        
        for öğe in os.listdir(os.curdir):
            if not os.path.isdir(öğe):
                dosyalar.append(öğe)
            else:
                dosyalar.extend(tara(öğe))
        
        os.chdir(başlangıç)
        return dosyalar
    
.. note:: Bu kodlarda henüz öğrenmediğimiz tek şey ``os.path.isdir()``
    fonksiyonu. Bu fonksiyon, kendisine parametre olarak verilen bir değerin
    dizin olup olmadığını tespit etmemizi sağlıyor.

Yukarıdaki kodlarda öncelikle o anda içinde bulunduğumuz dizinin konumunu
`başlangıç` adlı bir değişkene atıyoruz. Çünkü daha sonra buraya dönmemiz
gerekecek::
    
    başlangıç = os.getcwd()

Ardından `dosyalar` adlı bir liste oluşturuyoruz:: 

    dosyalar = []

Bu liste, dizinler içindeki bütün dosyaları içinde barındıracak. 

Daha sonra, ``tara()`` fonksiyonuna parametre olarak verilen `dizin` adlı
dizinin içine giriyoruz::
    
    os.chdir(dizin)
    
Bu dizinin içine girdikten sonra, mevcut dizin içindeki bütün öğeleri
``listdir()`` fonksiyonu ile tek tek tarıyoruz::
    
    for öğe in os.listdir(os.curdir):
        ...

Eğer tarama sırasında karşılaştığımız öğe bir dizin değil ise::
    
    if not os.path.isdir(öğe):
        ...

Bu öğeyi, doğrudan en başta tanımladığımız `dosyalar` adlı listeye
gönderiyoruz::
    
    dosyalar.append(öğe)
    
Ama eğer tarama sırasında karşılaştığımız öğe bir dizin ise::
    
    else:
        ...

``tara()`` fonksiyonunun en başına dönüp, tanımladığımız bütün işlemleri bu
dizin üzerine özyinelemeli olarak uyguluyoruz ve elde ettiğimiz öğeleri
``dosyalar`` adlı listeye ``extend()`` metodu ile işliyoruz::
    
    dosyalar.extend(tara(öğe))
    
Burada neden ``append()`` değil de ``extend()`` kullandığımızı anlamak için,
yukarıdaki kodu bir de ``append()`` ile yazıp elde ettiğiniz çıktıyı
değerlendirebilirsiniz.

``for`` döngüsünden çıktıktan sonra da tekrar en baştaki konuma dönebilmek için
aşağıdaki komutu çalıştırıyoruz::
    
    os.chdir(başlangıç)
    
Eğer bu şekilde başa dönmezsek, dizin yapısı içindeki ilk alt dizine girildikten
sonra programımız o konumda takılı kalacağı için öteki üst dizinlerin içini
tarayamaz. Bunun ne demek olduğunu anlamak için kodları bir de
``os.chdir(başlangıç)`` kodu olmadan çalıştırmayı deneyebilirsiniz.

Yukarıdaki yöntem doğru olsa da, Python'da bir dizini en dibe kadar taramanın en
iyi yolu değildir. Python bize bu iş için özel bir fonksiyon sunar. İşte, bu
bölümde ele alacağımız bu fonksiyonun adı ``walk()``.

*Walk* kelimesi İngilizcede 'yürümek' anlamına gelir. ``walk()`` fonksiyonu da,
kelimenin bu anlamına uygun olarak, dizinler içinde 'yürünmesini' sağlar. Gelin
bunu biraz açıklayalım.

Şöyle bir durum düşünün: Sabit diskinizde, bir dizin içinde pek çok alt dizine
dağılmış bir sürü dosya var. Yani şunun gibi::
    
    +anadizin
        |dosya.txt
        |dosya.doc
        |dosya.xls
        |dosya.jpeg
        +resimler
            |resim1.jpeg
            |resim2.jpeg
            |resim3.jpeg
            |resim4.jpeg
            +başkadosyalar
                |dosya.pdf
                |dosya.zip
                |dosya.mp3
                |dosya.ogg
                |dosya.jpeg

Siz bu iç içe geçmiş dosya yığını içinden, sonu `.jpeg` ile bitenleri tek bir
yerde toplamak istiyorsunuz. Elbette, eğer isterseniz bu `.jpeg` dosyalarını tek
tek elle bulup istediğiniz yere taşıyabilirsiniz. Ama bu yöntem bir Python
programcısına yakışmaz, değil mi?

Python programcıları bu tür angaryaları kendi yapmak yerine Python'a yaptırmayı
tercih eder. O yüzden biz de bu işi yapmak için Python'dan yararlanacağız. 

``os`` modülünün ``walk()`` fonksiyonunu kullanarak bu görevi rahatlıkla yerine
getirebilirsiniz.

Peki ama nasıl?

Öncelikle şu kodlar yardımıyla, yukarıdaki sözünü ettiğimiz dosya-dizin yapısını
oluşturalım. Böylece daha somut bir yapı üzerinde çalışma imkanı elde etmiş
oluruz::
    
    import os
    
    uzantılar = ['txt', 'doc', 'xls', 
                 'jpeg', 'pdf', 'zip', 
                 'mp3', 'ogg', 'jpeg']
    
    şablon1 = ['{}.{}'.format('dosya', i) for i in uzantılar[:4]]
    şablon2 = ['resim{}.{}'.format(i, uzantılar[-1]) for i in range(1, 5)]
    şablon3 = ['{}.{}'.format('dosya', i) for i in uzantılar[4:]]
    
    dosyalar = [('anadizin',  şablon1),
                ('resimler', şablon2),
                ('başkadosyalar', şablon3)]
                                  
    os.makedirs(os.sep.join([dosya[0] for dosya in dosyalar]))
    
    for dizin, şablon in dosyalar:
        for s in şablon:
            open(os.sep.join([dizin, s]), 'w')
        os.chdir(dizin)
        
Bu kodlarda, şu ana kadar görmediğimiz, öğrenmediğimiz hiçbir şey yok. Bu
kodları rahatlıkla anlayabilecek kadar Python bilgisine sahipsiniz.

Dosya-dizin yapımızı oluşturduğumuza göre, ``os`` modülünün ``walk()``
fonksiyonunu bu yapı üzerinde nasıl kullanacağımıza geçebiliriz. 

Şimdi 'anadizin' adlı klasörün bulunduğu dizin içinde etkileşimli kabuğu
başlatalım ve şu komutları verelim::
    
    >>> for i in os.walk('anadizin'):
    ...     print(i)
    
Buradan şu çıktıyı alacağız::
    
    ('anadizin', ['resimler'], ['dosya.doc', 'dosya.jpeg', 
                  'dosya.txt', 'dosya.xls'])
    ('anadizin\\resimler', ['başkadosyalar'], ['resim1.jpeg', 
                  'resim2.jpeg', 'resim3.jpeg', 'resim4.jpeg'])
    ('anadizin\\resimler\\başkadosyalar', [], ['dosya.jpeg', 
                  'dosya.mp3', 'dosya.ogg', 'dosya.pdf', 'dosya.zip'])
    
İnceleme kolaylığı açısından bu çıktının ilk kısmını ele alalım::
    
    ('anadizin', ['resimler'], ['dosya.doc', 'dosya.jpeg', 
                                'dosya.txt', 'dosya.xls'])

Gördüğünüz gibi, burada üç öğeli bir demet var. Çıktının diğer kısımlarını da
incelerseniz aynı yapıyı göreceksiniz. Dolayısıyla ``os.walk()`` komutu bize şu
üç öğeden oluşan bir demet verir::
    
    (kökdizin, altdizinler, dosyalar)
    
Yukarıdaki çıktıyı incelediğinizde bu yapıyı rahatlıkla görebilirsiniz::
    
    kökdizin    => 'anadizin'
    altdizinler => ['resimler']
    dosyalar    => ['dosya.doc', 'dosya.jpeg', 
                    'dosya.txt', 'dosya.xls']
                    
    kökdizin    => 'anadizin\\resimler'
    altdizinler => ['başkadosyalar']
    dosyalar    => ['resim1.jpeg', 'resim2.jpeg', 
                    'resim3.jpeg', 'resim4.jpeg']
                    
    kökdizin    => 'anadizin\\resimler\\başkadosyalar'
    altdizinler => []
    dosyalar    => ['dosya.jpeg', 'dosya.mp3', 
                    'dosya.ogg', 'dosya.pdf', 
                    'dosya.zip']
    
    
Mesela bu üç öğeli demet içinden yalnızca dosyaları almak isterseniz şöyle bir
komut verebilirsiniz::
    
    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     print(dosyalar)

Burada, ``os.walk('anadizin')`` komutunun bize sunduğu üç öğeli demetin herbir
öğesini, şu satır yardımıyla tek tek `kökdizin`, `altdizinler` ve `dosyalar`
adlı değişkenlere atıyoruz::
    
    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     ...
    
Sonra da bu üçlü içinden, `dosyalar` adlı değişkeni ekrana yazdırıyoruz::
    
    >>> print(dosyalar)

Bu da bize şöyle bir çıktı veriyor::
    
    ['dosya.doc', 'dosya.jpeg', 'dosya.txt', 'dosya.xls']
    ['resim1.jpeg', 'resim2.jpeg', 'resim3.jpeg', 'resim4.jpeg']
    ['dosya.jpeg', 'dosya.mp3', 'dosya.ogg', 'dosya.pdf', 'dosya.zip']

Gördüğünüz gibi, bu çıktıda 'anadizin' ve bunun altındaki bütün dizinlerde yer
alan bütün dosyalar var. Bu konunun başında ``walk()`` fonksiyonunu tanımlarken
dediğimiz gibi, ``walk()`` fonksiyonu gerçekten de dizinler içinde 'yürünmesini'
sağlıyor.

Bu fonksiyonu daha iyi anlamak için birkaç deneme daha yapalım::
    
    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     print(altdizinler)
    ...
    ['resimler']
    ['başkadosyalar']
    
Bu da bize 'anadizin' içindeki alt dizinlerin isimlerini veriyor.
    
Bir de `kökdizin` değişkeninin ne olduğuna bakalım::

    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     print(yol)  
    ...
    anadizin
    anadizin\resimler
    anadizin\resimler\başkadosyalar
    
Burada da o üçlü değişkenler arasından `kökdizin`'i yazdırdık ve gördük ki bu
değişken bize bütün kök dizinlere ilişkin yol bilgilerini, yani dizinlerin
adresini veriyor. Dolayısıyla `kökdizin` değişkeni ile `dosyalar` değişkenini
birleştirerek bir dosyanın tam adresini elde edebiliriz.

Dikkatlice bakın::

    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     for dosya in dosyalar:
    ...             print(os.sep.join([yol, dosya]))
    ...
    anadizin\dosya.doc
    anadizin\dosya.jpeg
    anadizin\dosya.txt
    anadizin\dosya.xls
    anadizin\resimler\resim1.jpeg
    anadizin\resimler\resim2.jpeg
    anadizin\resimler\resim3.jpeg
    anadizin\resimler\resim4.jpeg
    anadizin\resimler\başkadosyalar\dosya.jpeg
    anadizin\resimler\başkadosyalar\dosya.mp3
    anadizin\resimler\başkadosyalar\dosya.ogg
    anadizin\resimler\başkadosyalar\dosya.pdf
    anadizin\resimler\başkadosyalar\dosya.zip
    
Bildiğiniz gibi, `dosya` değişkeninin bize verdiği veri tipi bir listedir. O
yüzden bu listenin öğelerini tek tek alabilmek için bu liste üzerinde de bir
``for`` döngüsü kurduğumuza dikkat edin.

Eğer yukarıdaki dizinler içinde yer alan bütün `.jpeg` dosyalarını listelemek
istersek de şöyle bir kod yazabiliriz::
    
    >>> for kökdizin, altdizinler, dosyalar in os.walk('anadizin'):
    ...     for dosya in dosyalar:
    ...             if dosya.endswith('.jpeg'):
    ...                     print(dosya)
    ...
    dosya.jpeg
    resim1.jpeg
    resim2.jpeg
    resim3.jpeg
    resim4.jpeg
    dosya.jpeg
    
Gördüğünüz gibi, ``os.walk()`` fonksiyonu gayet pratik ve kullanışlı bir araç.

os.environ
===========

``os`` modülünün `environ` adlı niteliği, kullandığımız işletim sistemindeki
çevre değişkenleri hakkında bilgi edinmemizi sağlar. 

Bu nitelik alelade bir sözlüktür. Dolayısıyla bu sözlüğün içinde neler olduğunu
şu kodlarla görebilirsiniz::
    
    >>> for k, v in os.environ.items():    
    ...     print(k.ljust(10), v)
    
Sözlük içindeki istediğiniz bir değere nasıl erişeceğinizi biliyorsunuz::
    
    >>> os.environ['HOMEPATH']

    '\\Documents and Settings\\fozgul'
    
    >>> os.environ['USERNAME']
    
    'FOZGUL'

Yalnız, Windows ve GNU/Linux işletim sistemlerinde çevre değişkenleri ve
bunların adları birbirinden farklı olduğu için, doğal olarak `environ` niteliği
de farklı işletim sistemlerinde farklı çıktılar verir. Birden fazla işletim
sistemi üzerinde çalışacak şekilde tasarladığımız programlarda bu duruma dikkat
etmeliyiz. Örneğin Windows'ta kullanıcı adını veren çevre değişkeni 'USERNAME'
iken, GNU/Linux'ta bu değişken 'USER' olarak adlandırılır.
    
os.path
========

``os`` modülü üzerinde ``dir()`` fonksiyonunu uyguladığınızda, orada `path` adlı
bir niteliğin olduğunu göreceksiniz. Bu nitelik, kendi içinde pek çok önemli
fonksiyon ve başka nitelik barındırır.

Şimdi bu bölümde ``os.path`` adlı bu niteliğin içeriğini inceleyeceğiz.

os.path.abspath()
------------------

``abspath()`` fonksiyonu, bir dosyanın tam yolunun ne olduğunu söyler::
    
    >>> os.path.abspath('falanca.txt')

os.path.dirname()
--------------------

``dirname()`` fonksiyonu, bir dosya yolunun dizin kısmını verir::
    
    >>> os.path.dirname('/home/istihza/Desktop/falanca.txt')
    
    '/home/istihza/Desktop'
    
Bu fonksiyonu ``abspath()`` fonksiyonu ile birlikte kullanabilirsiniz::
    
    >>> os.path.dirname(os.path.abspath('falanca.txt'))
    
    '/home/istihza/Desktop'

os.path.exists()
-------------------

``exists()`` fonksiyonu bir dosya veya dizinin varolup olmadığını kontrol eder::
    
    >>> os.path.exists('/home/istihza/Desktop/falanca.txt')
    
Eğer böyle bir dosya varsa yukarıdaki kod ``True`` çıktısı, yoksa ``False``
çıktısı verir.

os.path.expanduser()
------------------------

``expanduser()`` fonksiyonu bilgisayardaki kullanıcıya ait dizinin adresini
verir::

    >>> os.path.expanduser('~')
    
    'C:\\Documents and Settings\\fozgul'
    
veya::

    >>> os.path.expanduser('~')
    
    '/home/istihza'
    
Bu fonksiyonu kullanarak, Windows'ta belirli bir kullanıcı ismi ve dizini de
oluşturabilirsiniz::
    
    >>> os.path.expanduser('~denizege')

    'C:\\Documents and Settings\\denizege'
    
os.path.isdir()
-------------------

``isdir()`` fonksiyonu, kendisine parametre olarak verilen öğenin bir dizin olup
olmadığını sorgular::
    
    >>> os.path.isdir('/home/istihza')
    
Eğer parametre bir dizin ise ``True``, eğer bir dosya ise ``False`` çıktısı
alınır.

os.path.isfile()
--------------------

``isfile()`` fonksiyonu, kendisine parametre olarak verilen öğenin bir dosya
olup olmadığını sorgular::
    
    >>> os.path.isfile('/home/istihza/falance.txt')
    
Eğer parametre bir dosya ise ``True``, eğer bir dizin ise ``False`` çıktısı
alınır.

os.path.join()
-----------------

``join()`` fonksiyonu, kendisine verilen parametrelerden, ilgili işletim
sistemine uygun yol adresleri oluşturur::
    
    >>> os.path.join('dizin1', 'dizin2', 'dizin3') #Windows
    
    'dizin1\\dizin2\\dizin3'
    
    >>> os.path.join('dizin1', 'dizin2', 'dizin3')
    
    'dizin1/dizin2/dizin3'

os.path.split()
--------------------

``split()`` fonksiyonu, bir yol adresinin son kısmını baş kısmından ayırır::
    
    >>> os.path.split('/home/istihza/Desktop')
    
    ('/home/istihza', 'Desktop')
    
Bu fonksiyonu kullanarak dosya adlarını dizin adlarından ayırabilirsiniz::
    
    >>> dizin, dosya = os.path.split('/home/istihza/Desktop/falanca.txt')
    >>> dizin
    
    '/home/istihza/Desktop'
    
    >>> dosya
    
    'falanca.txt'

os.path.splitext()
-----------------------

``splitext()`` fonksiyonu dosya adı ile uzantısını birbirinden ayırmak için
kullanılır::

    >>> dosya, uzantı = os.path.splitext('falanca.txt')
    >>> dosya
    
    'falanca'
    
    >>> uzantı
    
    '.txt'

Gördüğünüz gibi, kendi içinde pek çok nitelik ve fonksiyon barındıran `os.path`,
kullandığımız işletim sistemine uygun şekilde dizin işlemleri yapabilmemizi
sağlayan son derece faydalı bir araçtır.

Gelin isterseniz şimdi biraz bu `os.path` niteliğinin bazı önemli
özelliklerinden söz edelim.

Hatırlarsanız önceki derslerimizde, modüllerin kaynak dosyalarını görmemizi
sağlayan ``__file__`` adlı bir araçtan söz etmiştik. Mesela bu aracı ``os``
modülü üzerinde uyguladığımızda şuna benzer bir çıktı alıyorduk::
    
    >>> os.__file__
    
    'C:\\Python\\lib\\os.py'
    
Demek ki ``os`` modülünün kaynak kodları bu dizin içinde yer alıyormuş...

Normalde ``__file__`` niteliğini yalnızca modül adlarına uygulayabilirsiniz.
Modüllerin nitelik ve fonksiyonları üzerinde ``__file__`` aracı kullanılamaz::
    
    >>> os.name.__file__
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'str' object has no attribute '__file__'
    
    >>> os.walk.__file__
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'function' object has no attribute '__file__'    
    
Ama ``os`` modülünün `path` niteliği için durum biraz farklıdır::
    
    >>> os.path.__file__
    
Eğer bu komutu Windows'ta verdiyseniz şu çıktıyı alırsınız:

.. parsed-literal::
    
    'C:\\Python\ |ext-noformat|\ \\lib\\ntpath.py'
    
Ama eğer bu komutu GNU/Linux'ta verdiyseniz şuna benzer bir çıktı alırsınız:

.. parsed-literal::
    
    '/home/python\ |ext-noformat|\ /lib/python\ |major-noformat|\ /posixpath.py'
    
Gördüğünüz gibi, ``__file__``, `os.path` üzerinde kullanılabiliyor. Yukarıdaki
çıktılardan anladığımıza göre `os.path` niteliği Windows'ta `ntpath`,
GNU/Linux'ta ise `posixpath` adlı bir modüle atıfta bulunuyor.
    
Dolayısıyla aslında biz `os.path` niteliğini kullanırken, eğer Windows'ta isek
``ntpath`` adlı bir modülü, ama eğer GNU/Linux'ta isek ``posixpath`` adlı bir
modülü içe aktarmış oluyoruz. 

Eğer `os.path` adlı ortak bir arayüz olmasaydı, yukarıda `os.path` başlığı
altında incelediğimiz araçları kullanabilmek için, kullandığımız işletim
sistemine göre ``posixpath`` veya ``ntpath`` modüllerinden uygun olanını
kendimiz elle içe aktarmak zorunda kalacaktık::
    
    if os.name == 'nt':
        import ntpath as path
        
    else:
        import posixpath as path
        
Ama Python programlama dilinin bize `os.path` adlı niteliği sunmuş olması
sayesinde Windows işletim sistemi için ``ntpath``, GNU/Linux işletim sistemi
için ise ``posixpath`` modülünü ayrı ayrı içe aktarmamıza gerek kalmıyor. Bütün
işi bizim yerimize Python hallediyor. Böylece farklı işletim sistemlerine
ilişkin birbirinden farklı işlemleri, `os.path` adlı tek bir arayüz üzerinden
gerçekleştirebiliyoruz.
