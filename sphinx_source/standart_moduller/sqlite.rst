.. meta::
   :description: Python 2.x ve Veritabanı Programlama (Database Programming)
   :keywords: python, veritabanı, database, sqlite, SQL, SQL injection, sızma, güvenlik

*********************************
Sqlite ile Veritabanı Programlama
*********************************

Giriş
*************

Bu bölümde, Python'daki ileri düzey konulardan biri olan veritabanı
programlamayı (*database programming*) inceleyeceğiz. Dilerseniz öncelikle
'veritabanı' denen şeyin ne olduğunu anlamaya çalışarak işe başlayalım.

Esasında veritabanı, hiçbirimizin yabancısı olduğu bir kavram değil. Biz bu
kelimeyi, teknik anlamının dışında, günlük hayatta da sıkça kullanıyoruz.
Veritabanı, herkesin bildiği ve kullandığı anlamıyla, içinde veri barındıran bir
'şey'dir. Günlük kullanımda, hakikaten, içinde veri barındıran her şeye
veritabanı dendiğini duyarsınız.

Veritabanı kelimesinin günlük kullanımdaki anlamı dışında bir de teknik anlamı
vardır. Bizi esas ilgilendiren de zaten terimin teknik anlamıdır. Mesela
Vikipedi'de veritabanı şöyle tanımlanıyor:

    *Bilgisayar terminolojisinde, sistematik erişim imkânı olan, yönetilebilir,
    güncellenebilir, taşınabilir, birbirleri arasında tanımlı ilişkiler
    bulunabilen bilgiler kümesidir. Bir başka tanımı da, bir bilgisayarda
    sistematik şekilde saklanmış, programlarca işlenebilecek veri yığınıdır.*
    
Yukarıdaki tanım, veritabanının ne demek olduğunu gayet iyi ifade ediyor. Ama
esasında bizim veritabanı tanımı üzerinde fazlaca durmamıza gerek yok. Biz her
zaman olduğu gibi işin teknik boyutuyla değil, taktik boyutuyla ilgilenmeyi
tercih edeceğiz. O halde yavaş yavaş işe koyulmaya başlayalım.

Python'la veritabanı programlama işlemleri için pek çok alternatifimiz var.
Python'la hangi veritabanı sistemlerini kullanabileceğinizi görmek için
http://wiki.python.org/moin/DatabaseInterfaces adresindeki listeyi
inceleyebilirsiniz. Biz bunlar içinde, sadeliği, basitliği ve kullanım kolaylığı
nedeniyle **Sqlite** adlı veritabanı yönetim sistemini ele alacağız.

Neden Sqlite?
**************

Dediğimiz gibi, Python'da veritabanı işlemleri için kullanabileceğiniz pek çok
alternatif bulunur. Ama biz bütün bu alternatifler içinde Sqlite'ı tercih
edeceğiz. Peki neden Sqlite?

Sqlite'ın öteki sistemlere göre pek çok avantajı bulunur. Gelin isterseniz
Sqlite'ın bazı avantajlarına şöyle bir göz gezdirelim:

- Her şeyden önce Sqlite Python'un 2.5 sürümlerinden bu yana bu dilin bir
  parçasıdır. Dolayısıyla eğer kullandığınız Python sürümü 2.5 veya üstü ise
  Sqlite'ı Python'daki herhangi bir modül gibi içe aktarabilir ve kullanmaya
  başlayabilirsiniz.

- Sqlite herhangi bir yazılım veya sunucu kurulumu gerektirmez. Bu sayede, bu
  modülü kullanabilmek için öncelikle bir sunucu yapılandırmanıza da gerek
  yoktur. Bazı veritabanlarını kullanabilmek için arka planda bir veritabanı
  sunucusu çalıştırıyor olmanız gerekir. Sqlite'ta ise böyle bir şey
  yapmazsınız.

- Sqlite, öteki pek çok veritabanı alternatifine göre basittir. Bu yüzden
  Sqlite'ı çok kısa bir sürede kavrayıp kullanmaya başlayabilirsiniz.

- Sqlite özgür bir yazılımdır. Bu yazılımın baştan aşağı bütün kodları kamuya
  açıktır. Dolayısıyla Sqlite kodlarının her zerresini istediğiniz gibi
  kullanabilir, değişikliğe uğratabilir, satabilir ve ticari olan/olmayan bütün
  uygulamalarınızda gönül rahatlığıyla kullanabilirsiniz.

- Sqlite'ın sade ve basit olması sizi yanıltmasın. Bu özelliklerine bakarak,
  Sqlite'ın yeteneksiz bir veritabanı sistemi olduğunu düşünmeyin. Bugün
  Sqlite'ı aktif olarak kullanan pek çok büyük ve tanınmış şirket bulunur.
  Mesela, Adobe, Apple, Mozilla/Firefox, Google, Symbian ve Sun bu şirketlerden
  bazılarıdır. Hatta GNOME masaüstü ortamının sevilen müzik ve video
  çalarlarından Banshee'de de veritabanı olarak Sqlite kullanıldığını
  söyleyelim.

Yukarıdaki sebeplerden ötürü, veritabanı konusunu Sqlite üzerinden anlatacağız.
O halde hemen yola koyulalım.

Sqlite'ın Yapısı
******************

Bu bölümün en başında verdiğimiz veritabanı tanımından da anlaşılacağı gibi,
veritabanları, verileri sonradan kullanılmak üzere içinde tutan bir sistemdir.
Bütün `ilişkisel veritabanları
<http://tr.wikipedia.org/wiki/%C4%B0li%C5%9Fkisel_veri_taban%C4%B1_y%C3%B6netim_sistemi>`_\nda
olduğu gibi, Sqlite da bu verileri tablo benzeri bir yapı içinde tutar. Yani
aslında bir Sqlite veritabanı içindeki veriler şöyle bir yapıya sahiptir:

    +-----------+-----------+-----------+-----------+-----------+
    | Sütun 1   | Sütun 2   | Sütun 3   | Sütun 4   | Sütun 5   |
    +===========+===========+===========+===========+===========+
    | Değer 1/1 | Değer 2/1 | Değer 3/1 | Değer 4/1 | Değer 5/1 |
    +-----------+-----------+-----------+-----------+-----------+
    | Değer 1/2 | Değer 2/2 | Değer 3/2 | Değer 4/2 | Değer 5/2 |
    +-----------+-----------+-----------+-----------+-----------+
    | Değer 1/3 | Değer 2/3 | Değer 3/3 | Değer 4/3 | Değer 5/3 |
    +-----------+-----------+-----------+-----------+-----------+
    | Değer 1/4 | Değer 2/4 | Değer 3/4 | Değer 4/4 | Değer 5/4 |
    +-----------+-----------+-----------+-----------+-----------+

Sqlite içinde oluşturulan yukarıdakine benzer her tablonun bir de ismi vardır.
Daha doğrusu, Sqlite ile bir tablo oluştururken, bu tabloya bir de ad vermemiz
gerekir. Mesela yukarıdaki tabloya 'değerler' adını verdiğimizi
varsayabilirsiniz.

Sqlite ile çalışırken veriler üzerinde yapacağımız işlemleri, yukarıdaki
tablonun adını ve bu tablodaki sütunları kullanarak gerçekleştireceğiz. Bu
yüzden Sqlite'ın yapısını anlamak büyük önem taşır. Gördüğünüz gibi, bu
veritabanı sisteminin yapısını anlamak da öyle zor bir iş değildir.

Yardımcı Araçlar
********************

Veritabanları üzerinde yapacağımız çalışmalar sırasında, işlerimizi
kolaylaştırmak için bazı harici araçlara da ihtiyaç duyacağız. Gelin şimdi bu
araçları tanıyalım.

Sqlitebrowser
====================

Sqlitebrowser, Sqlite veritabanlarının içeriğini grafik bir arayüz aracılığıyla
görüntüleyebilmemizi sağlayan bir program. Bu program sayesinde, veritabanı
üzerinde yaptığınız çalışmanın doğru sonuç verip vermediğini teyit edebilir,
elinizdeki veritabanının içeriğinde hangi verilerin olduğunu açık seçik
görebilirsiniz. 

Bu programı indirmek için ziyaret etmemiz gereken adres
http://sqlitebrowser.org/.

Eğer siz bir Windows kullanıcısı iseniz, sitedeki `.exe` dosyasını indirip,
programı herhangi bir Windows programı gibi kurabilirsiniz.

GNU/Linux kullanıcılarının önünde ise her zaman olduğu gibi birkaç farklı
seçenek var. Öncelikle, bu program çoğu GNU/Linux dağıtımının paket deposunda
zaten bulunur. Dolayısıyla bu programı dağıtımınızın paket deposu aracılığıyla
rahatlıkla kurabilirsiniz. Mesela Ubuntu kullananlar şu komutla programı
kurabilir::
    
    sudo apt-get install sqlitebrowser
    
GNU/Linux kullanıcıları, eğer arzu ederlerse, programın kaynak kodlarını
sitesinden indirip programı kendileri derlemeyi de tercih edebilir. Bunun için
öncelikle http://sqlitebrowser.org/ adresine gidip `.tar.gz` uzantılı dosyayı
indirin.

Bu programı derlemeye geçmeden önce şu bağımlılıkları kurmamız gerekiyor:

    #. cmake 
    #. libqt4-dev 
    #. libsqlite3-dev
    
Ubuntu'da ayrıca `build-essential` paketine de ihtiyacınız olacak. Ubuntu
kullanıcıları şu komutu vererek Sqlitebrowser programının bütün bağımlılıklarını
sistemlerine kurabilir::
    
    sudo apt-get install build-essential cmake libqt4-dev libsqlite3-dev
    
Bağımlılıkları kurduktan sonra, indirdiğiniz `.tar.gz` dosyasını aşağıdaki
komut yardımıyla açın::
    
    tar zxvf sqlitebrowser-3.7.0.tar.gz
    
Ben burada indirdiğiniz program sürümünün 3.7.0 olduğunu varsaydım. Sizin
indirdiğiniz sürüm farklıysa yukarıdaki komutu o sürüme göre vereceksiniz. 
    
Daha sonra şu komutu vererek, açtığınız klasörün içine girin::
    
    cd sqlitebrowser-3.7.0
    
Yine, burada da klasör adı ve sürüm numarası sizde farklıysa komutu düzeltin. 
    
Ardından sırasıyla şu komutları verin (``cmake`` komutunun yanındaki nokta
işaretine dikkat!!)::
    
    cmake .
    
::
    
    make
    
:: 

    sudo make install
    
Böylece Sqlitebrowser programını sisteminize kurmuş oldunuz. Programın
kurulduğunu teyit etmek için şu komutu çalıştırın::
    
    sqlitebrowser
    
Eğer program penceresi açıldıysa her şey yolunda demektir. Eğer programı
çalıştıramadıysanız veya yukarıdaki komutları anlamakta ve işletmekte zorluk
çekiyorsanız paket deponuzdaki Sqlitebrowser sürümü ile yola devam etmenizi
tavsiye ederim. Ya da eğer arzu ederseniz, http://www.istihza.com/forum adresine
uğrayıp yardım talebinde bulunabilirsiniz.

Örnek Veritabanı
==================

Sqlite'ı öğrenirken, içinde örnek veriler barındıran bir veritabanının elimizin
altında bulunması alıştırma yapabilmek açısından faydalı olacaktır. Bunun için
http://www.istihza.com/denemeler/kitaplar.sqlite adresindeki örnek veritabanını
bilgisayarınıza indirin. Veritabanı sorgu çalışmalarımızı bu örnek veritabanı
üzerinde gerçekleştireceğiz.

Şimdi mesela biraz önce indirip kurduğunuz Sqlitebrowser programını çalıştırın
ve *File* > *Open Database* yolunu takip ederek bu `kitaplar.sqlite` adlı
veritabanı dosyasını açın. Eğer Sqlitebrowser programını Sqlite veritabanı
dosyaları ile ilişkilendirdiyseniz, `kitaplar.sqlite` dosyası üzerine çift
tıkladığınızda da bu veritabanı dosyası otomatik olarak Sqlitebrowser programı
ile açılacaktır. Ayrıca elbette veritabanı dosyası üzerine sağ tıklayıp,
'Birlikte aç...' seçeneğini kullanarak da Sqlitebrowser programını çalıştırmayı
deneyebilirsiniz.

Sqlitebrowser programını çalıştırıp, `kitaplar.sqlite` dosyasını da açtıktan
sonra, program penceresi üzerindeki 'Browse Data' sekmesine tıklayarak
veritabanının içinde ne tür verilerin olduğunu inceleyin. Gördüğünüz gibi,
Sqlitebrowser programı, veritabanı içindeki verileri görselleştirmek açısından
epey kolaylık sağlıyor. Birazdan bu verilere Python aracılığıyla nasıl
erişebileceğimizi de öğreneceğiz.

Yeni Bir Veritabanı Oluşturmak
*******************************

Bu bölümde `sqlite` adlı bir modül aracılığıyla yeni bir veritabanını nasıl
oluşturacağımızı öğreneceğiz. 

Yukarıda `sqlite` adlı bir modülden söz ettik. Dolayısıyla, tahmin
edebileceğiniz gibi, bu modülü kullanabilmek için öncelikle modülü içe
aktarmamız gerekiyor. Bu bölümün başında da söylediğimiz gibi, Sqlite, Python'ın
2.5 sürümünden bu yana dilin bir parçasıdır::
    
    >>> import sqlite3

Python'da Sqlite veritabanı sistemine ait modül 'sqlite3' adını taşır. Bu
yüzden, bu modülü içe aktarmak için ``import sqlite3`` ifadesini kullanmamız
gerekiyor. Eğer bu isim size çok uzun geliyorsa veya modül adında sayıların ve
harflerin birlikte bulunması nedeniyle hem sayı hem de harf girmeyi bir angarya
olarak görüyorsanız elbette `sqlite3` modülünü farklı bir adla da içe
aktarabileceğinizi biliyorsunuz. Mesela::
    
    >>> import sqlite3 as sql
    
Veya::

    >>> import sqlite3 as lite

Böylece `sqlite3` modülünü 'sql' veya 'lite' adıyla içe aktarmış olduk. Ancak
ben konuyu anlatırken, okur açısından kafa karışıklığına sebep olmamak için,
modülü ``import sqlite3`` şeklinde içe aktarmışız gibi davranacağım.

Gelelim bu modül yardımıyla nasıl veritabanı oluşturulacağına... Bunun için
`sqlite3` modülünün ``connect()`` adlı metodundan yararlanacağız. Bu metodu şu
şekilde kullanıyoruz::
    
    >>> vt = sqlite3.connect('veritabanı_adı')

``connect()`` metoduna verdiğimiz `varitabanı_adı` adlı argüman, kullanacağımız
veritabanının adıdır. Eğer belirtilen isimde bir veritabanı sistemde
bulunmuyorsa o adla yeni bir veritabanı oluşturulacaktır. Mesela::
    
    >>> vt = sqlite3.connect('deneme.sqlite')
    
Eğer bu komutu verdiğiniz dizin içinde `deneme.sqlite` adlı bir veritabanı
yoksa, bu ada sahip bir veritabanı oluşturulacaktır.

Bu arada, biz veritabanı dosyasının uzantısı olarak `.sqlite`'ı seçtik. Ama eğer
siz isterseniz kendinize uygun başka bir uzantı da belirleyebilirsiniz.
Veritabanı dosyasının uzantısının ne olması gerektiği konusunda kesin kurallar
bulunmaz. `.sqlite` uzantısının yerine, `.sqlite3`, `.db` veya `.db3` gibi
uzantıları tercih edenler de vardır. Hatta eğer siz isterseniz veritabanınızın
uzantısını `.osman` olarak dahi belirleyebilirsiniz. Bu konuda herhangi bir
kısıtlama bulunmaz.

Yukarıdaki örnekte `deneme.sqlite` adını verdiğimiz bir veritabanı dosyasına,
``connect()`` metodu yardımıyla bağlandık. Elbette isteseydik ``connect()``
metoduna argüman olarak tam dosya yolu da verebilirdik::

    >>> import sqlite3
    >>> vt = sqlite3.connect('/home/istihza/test.sqlite') #GNU/Linux
    >>> vt = sqlite3.connect('c:/users/fozgul/desktop/test.sqlite') #Windows

Bu komut yardımıyla sabit disk üzerinde bir Sqlite veritabanı dosyası oluşturmuş
oluyoruz. Ancak isterseniz ``sqlite3`` ile geçici bir veritabanı da
oluşturabilirsiniz::
    
    >>> vt = sqlite3.connect(':memory:')

Oluşturduğunuz bu geçici veritabanı sabit disk üzerinde değil RAM (bellek)
üzerinde çalışır. Veritabanını kapattığınız anda da bu geçici veritabanı
silinir. Eğer arzu ederseniz, RAM üzerinde değil, disk üzerinde de geçici
veritabanları oluşturabilirsiniz. Bunun için de şöyle bir komut kullanıyoruz::
    
    >>> vt = sqlite3.connect('')
    
Gördüğünüz gibi, disk üzerinde geçici bir veritabanı oluşturmak için boş bir
karakter dizisi kullandık. Tıpkı ``:memory:`` kullanımında olduğu gibi, boş
karakter dizisiyle oluşturulan geçici veritabanları da veritabanı bağlantısının
kesilmesiyle birlikte ortadan kalkacaktır.

Geçici veritabanı oluşturmak, özellikle çeşitli testler veya denemeler
yaptığınız durumlarda işinize yarar. Sonradan nasıl olsa sileceğiniz, sırf test
amaçlı tuttuğunuz bir veritabanını disk üzerinde oluşturmak yerine RAM üzerinde
oluşturmayı tercih edebilirsiniz. Ayrıca, geçici veritabanları sayesinde,
yazdığınız bir kodu test ederken bir hatayla karşılaşırsanız sorunun veritabanı
içinde varolan verilerden değil, yazdığınız koddan kaynaklandığından da emin
olabilirsiniz. Çünkü, dediğimiz gibi, programın her yeniden çalışışında
veritabanı baştan oluşturulacaktır.

Dikkatinizi çekmek istediğim bir nokta da şudur: Gördüğünüz gibi Sqlite,
veritabanını o anda içinde bulunduğunuz dizin içinde oluşturuyor. Mesela MySQL
kullanıyor olsaydınız, oluşturulan veritabanlarının önceden tanımlanmış bir
dizin içine atıldığını görecektiniz. Örneğin GNU/Linux sistemlerinde, MySQL
veritabanları `/var/lib/mysql` gibi bir dizinin içinde tutulur.
    
Varolan Bir Veritabanıyla Bağlantı Kurmak
******************************************

Biraz önce, `deneme.sqlite` adlı yeni bir Sqlite veritabanı oluşturmak için
şöyle bir komut kullanmıştık::
    
    >>> vt = sqlite3.connect('deneme.sqlite')

Eğer bu komutu verdiğiniz dizin içinde `deneme.sqlite` adlı bir veritabanı
yoksa, bu ada sahip bir veritabanı oluşturulur. Eğer zaten bu adla bir
veritabanı dosyanız varsa, ``sqlite3`` bu veritabanına bağlanacaktır.
Dolayısıyla Sqlite'ta hem yeni bir veritabanı oluşturmak hem de mevcut bir
veritabanına bağlanmak için birbiriyle tamamen aynı kodları kullanıyoruz.

Mesela biraz önce http://www.istihza.com/denemeler/kitaplar.sqlite adresinden
indirdiğimiz `kitaplar.sqlite` adlı veritabanına bağlanalım.

Bu dosyanın bulunduğu konumda bir Python etkileşimli kabuk oturumu açtığımızı
varsayarsak::
    
    >>> vt = sqlite3.connect('kitaplar.sqlite')
    
komutunu kullanarak `kitaplar.sqlite` adlı veritabanıyla bağlantı kurabiliriz.

İmleç Oluşturma
****************

Yukarıda ``connect()`` metodunu kullanarak hem Sqlite ile nasıl veritabanı
bağlantısı kuracağımızı hem de nasıl yeni bir veritabanı oluşturacağımızı
öğrendik. 

``connect()`` metodu, bir veritabanı üzerinde işlem yapabilmemizin ilk adımıdır.
Veritabanını oluşturduktan veya varolan bir veritabanı ile bağlantı kurduktan
sonra, veritabanı üzerinde işlem yapabilmek için sonraki adımda bir imleç
oluşturmamız gerekir.

İmleç oluşturmak için ``cursor()`` adlı bir metottan yararlanacağız::
    
    >>> im = vt.cursor()

İmleci oluşturduktan sonra artık önümüz iyice açılıyor. Böylece, yukarıda
oluşturduğumuz ``im`` nesnesinin ``execute()`` metodunu kullanarak SQL
komutlarını çalıştırabileceğiz. Nasıl mı? Hemen bakalım.

Tablo Oluşturma
*****************

Önceki bölümün sonunda söylediğimiz gibi, bir imleç nesnesi oluşturduktan sonra
bunun ``execute()`` metodunu kullanarak SQL komutlarını işletebiliyoruz.

Dilerseniz şimdi basit bir örnek yaparak neyin ne olduğunu anlamaya çalışalım. 

Öncelikle gerekli modülü içe aktaralım::
    
    >>> import sqlite3
    
Şimdi de yeni bir veritabanı dosyası oluşturalım (veya varolan bir veritabanı
dosyasına bağlanalım)::
    
    >>> vt = sqlite3.connect('veritabani.sqlite')
    
Bu veritabanı üzerinde işlem yapabilmek için öncelikle imlecimizi oluşturalım::
    
    >>> im = vt.cursor()
    
Şimdi de yukarıda oluşturduğumuz imlecin ``execute()`` adlı metodunu kullanarak
veritabanı içinde bir tablo oluşturalım::

    >>> im.execute("CREATE TABLE adres_defteri (isim, soyisim)")

Hatırlarsanız, Sqlite veritabanı sisteminin tablo benzeri bir yapıya sahip
olduğunu ve bu sistemdeki her tablonun da bir isminin bulunduğunu söylemiştik.
İşte burada yaptığımız şey, 'adres_defteri' adlı bir tablo oluşturup, bu tabloya
'isim' ve 'soyisim' adlı iki sütun eklemekten ibarettir. Yani aslında şöyle bir
şey oluşturmuş oluyoruz:

    +---------+---------+
    | isim    | soyisim |
    +=========+=========+
    |         |         |
    +---------+---------+

Ayrıca oluşturduğumuz bu tablonun adının da 'adres_defteri' olduğunu
unutmuyoruz...

Bu işlemleri nasıl yaptığımıza dikkat edin. Burada ``CREATE TABLE adres_defteri
(isim, soyisim)`` tek bir karakter dizisidir. Bu karakter dizisindeki ``CREATE
TABLE`` kısmı bir SQL komutu olup, bu komut bir tablo oluşturulmasını sağlar.

Burada ``CREATE TABLE`` ifadesini büyük harflerle yazdık. Ancak bu ifadeyi siz
isterseniz küçük harflerle de yazabilirsiniz. Benim burada büyük harf
kullanmaktaki amacım SQL komutlarının, 'adres_defteri', 'isim' ve 'soyisim' gibi
öğelerden görsel olarak ayırt edilebilmesini sağlamak. Yani ``CREATE TABLE``
ifadesinin mesela 'adres_defteri' öğesinden kolayca ayırt edilebilmesini
istediğim için burada ``CREATE TABLE`` ifadesini büyük harflerle yazdım.

Karakter dizisinin devamında ``(isim, soyisim)`` ifadesini görüyoruz. Tahmin
edebileceğiniz gibi, bunlar tablodaki sütun başlıklarının adını gösteriyor. Buna
göre, oluşturduğumuz tabloda 'isim' ve 'soyisim' adlı iki farklı sütun başlığı
olacak.

Bu arada, Sqlite tabloları oluştururken tablo adı ve sütun başlıklarında Türkçe
karakter kullanmaktan kaçınmak iyi bir fikirdir. Ayrıca eğer tablo adı ve sütun
başlıklarında birden fazla kelimeden oluşan etiketler kullanacaksanız bunları ya
birbirine bitiştirin ya da tırnak içine alın. Örneğin::
    
    import sqlite3
    
    vt = sqlite3.connect('perso.sqlite')
    im = vt.cursor()
    
    im.execute("""CREATE TABLE 'personel dosyasi'
    ('personel ismi', 'personel soyismi', memleket)""")
    
Ayrıca, ``execute()`` metoduna parametre olarak verilen SQL komutlarının alelade
birer karakter dizisi olduğuna da dikkatinizi çekmek isterim. Bunlar
Python'daki karakter dizilerinin bütün özelliklerini taşır. Mesela bu karakter
dizisini ``execute()`` metoduna göndermeden önce bir değişkene atayabilirsiniz::
    
    import sqlite3
    
    vt = sqlite3.connect('perso.sqlite')
    im = vt.cursor()
    
    sql = """CREATE TABLE 'personel dosyasi' 
    ('personel ismi', 'personel soyismi', memleket)"""
    
    im.execute(sql)
    
Bu kodları kullanarak oluşturduğunuz `perso.sqlite` adlı veritabanı dosyasının
içeriğini Sqlitebrowser programı yardımıyla görüntüleyip, gerçekten 'personel
ismi', 'personel soyismi' ve 'memleket' sütunlarının oluşup oluşmadığını kontrol
edin.

Bu arada, bu kodları ikinci kez çalıştırdığınızda şöyle bir hata mesajı
alacaksınız::
    
    sqlite3.OperationalError: table 'personel dosyasi' already exists
    
Bu hata mesajını almanız gayet normal. Bunun üstesinden nasıl geleceğinizi
öğrenmek için okumaya devam edin...  

Şartlı Tablo Oluşturma 
***********************

``CREATE TABLE`` komutunu kullanarak tablo oluştururken şöyle bir problemle
karşılaşmış olabilirsiniz. Diyelim ki şu kodları yazdınız::
    
    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    
    im = vt.cursor()
    im.execute("CREATE TABLE personel (isim, soyisim, memleket)")
    
Bu kodları ilk kez çalıştırdığınızda, mevcut dizin altında `vt.sqlite` adlı bir
veritabanı dosyası oluşturulacak ve bu veritabanı içinde 'isim', 'soyisim' ve
'memleket' başlıklı sütunlara sahip, 'personel' adlı bir tablo meydana
getirilecektir.

Ancak aynı kodları ikinci kez çalıştırdığınızda şöyle bir hata mesajı ile
karşılaşacaksınız::
    
    sqlite3.OperationalError: table personel already exists
    
Buradaki sorun, `vt.sqlite` dosyası içinde 'personel' adlı bir tablonun zaten
bulunuyor olmasıdır. Bir veritabanı üzerinde işlem yaparken, aynı ada sahip iki
tablo oluşturamayız. Bu hatayı önlemek için şartlı tablo oluşturma yönteminden
yararlanacağız. Bunun için kullanacağımız SQL komutu şudur: ``CREATE TABLE IF
NOT EXISTS``.

Örneğimizi bu yeni bilgiye göre tekrar yazalım::
    
    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    
    im = vt.cursor()
    
    sorgu = """CREATE TABLE IF NOT EXISTS personel 
    (isim, soyisim, memleket)"""
    
    im.execute(sorgu)
    
Bu kodları kaç kez çalıştırırsanız çalıştırın, programınız hata vermeden
işleyecek; eğer veritabanında 'personel' adlı bir tablo yoksa oluşturacak,
bu adla zaten bir tablo varsa da sessizce yoluna devam edecektir.

Tabloya Veri Girme 
********************

Buraya kadar, `sqlite3` modülünü kullanarak nasıl bir veritabanı
oluşturacağımızı ve çeşitli sütünlardan oluşan bir tabloyu bu veritabanına nasıl
yerleştireceğimizi öğrendik. Şimdi de oluşturduğumuz bu sütun başlıklarının
altını dolduracağız.

Dikkatlice bakın::
    
    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    im = vt.cursor()
    
    tablo_yap = """CREATE TABLE IF NOT EXISTS personel
    (isim, soyisim, memleket)"""
    
    değer_gir = """INSERT INTO personel VALUES ('Fırat', 'Özgül', 'Adana')"""
    
    im.execute(tablo_yap)
    im.execute(değer_gir)
    
.. warning:: Bu kodları çalıştırdıktan sonra, eğer veritabanının içeriğini
 Sqlitebrowser ile kontrol ettiyseniz verilerin veritabanına işlenmediğini
 göreceksiniz. Endişe etmeyin; birazdan bunun neden böyle olduğunu açıklayacağız.
        
Burada ``INSERT INTO tablo_adı VALUES`` adlı yeni bir SQL komutu daha
öğreniyoruz. ``CREATE TABLE`` ifadesi Türkçe'de "TABLO OLUŞTUR" anlamına
geliyor. ``INSERT INTO`` ise "... İÇİNE YERLEŞTİR" anlamına gelir. Yukarıdaki
karakter dizisi içinde görünen ``VALUES`` ise "DEĞERLER" demektir. Yani aslında
yukarıdaki karakter dizisi şu anlama gelir: "*personel İÇİNE 'Fırat', 'Özgül' ve
'Adana' DEĞERLERİNİ YERLEŞTİR. Yani şöyle bir tablo oluştur*":

    +---------+---------+----------+
    | isim    | soyisim | memleket |
    +=========+=========+==========+
    | Fırat   | Özgül   | Adana    |
    +---------+---------+----------+

Buraya kadar gayet güzel gidiyoruz. İsterseniz şimdi derin bir nefes alıp, şu
ana kadar yaptığımız şeyleri bir gözden geçirelim:

* Öncelikle ``sqlite3`` modülünü içe aktardık. Bu modülün nimetlerinden
  yararlanabilmek için bunu yapmamız gerekiyordu. "sqlite3" kelimesini her
  defasında yazmak bize angarya gibi gelebileceği için bu modülü farklı bir adla
  içe aktarmayı tercih edebiliriz. Mesela ``import sqlite3 as sql`` veya ``import
  sqlite3 as lite`` gibi...

* ``sqlite3`` modülünü içe aktardıktan sonra bir veritabanına bağlanmamız veya
  elimizde bir veritabanı yoksa yeni bir veritabanı oluşturmamız gerekiyor. Bunun
  için ``connect()`` adlı bir fonksiyondan yararlanıyoruz. Bu fonksiyonu,
  ``sqlite3.connect('veritabanı_adı')`` şeklinde kullanıyoruz. Eğer içinde
  bulunduğumuz dizinde, "veritabanı_adı" adlı bir veritabanı varsa Sqlite bu
  veritabanına bağlanır. Eğer bu adda bir veritabanı yoksa, çalışma dizini altında
  bu ada sahip yeni bir veritabanı oluşturulur. Özellikle deneme amaçlı işlemler
  yapmamız gerektiğinde, sabit disk üzerinde bir veritabanı oluşturmak yerine RAM
  üstünde geçici bir veritabanı ile çalışmayı da tercih edebiliriz. Bunun için
  yukarıdaki komutu şöyle yazıyoruz: ``sqlite3.connect(':memory:')``. Bu komutla
  RAM üzerinde oluşturduğumuz veritabanı, bağlantı kesildiği anda ortadan
  kalkacaktır.

* Veritabanımızı oluşturduktan veya varolan bir veritabanına bağlandıktan sonra
  yapmamız gereken şey bir imleç oluşturmak olacaktır. Daha sonra bu imlece ait
  metotlardan yararlanarak önemli işler yapabileceğiz. Sqlite'ta bir imleç
  oluşturabilmek için ``db.cursor()`` gibi bir komut kullanıyoruz. Tabii ben
  burada oluşturduğunuz veritabanına "db" adını verdiğinizi varsayıyorum.

* İmlecimizi de oluşturduktan sonra önümüz iyice açılmış oldu. Şimdi ``dir(im)``
  gibi bir komut kullanarak imlecin metotlarının ne olduğunu inceleyebilirsiniz.
  Tabii ben burada imlece "im" adını verdiğinizi varsaydım. Gördüğünüz gibi,
  listede ``execute()`` adlı bir metot da var. Artık imlecin bu ``execute()``
  metodunu kullanarak SQL komutlarını işletebiliriz.

* Yukarıda üç adet SQL komutu öğrendik. Bunlardan ilki ``CREATE TABLE``. Bu komut
  veritabanı içinde bir tablo oluşturmamızı sağlıyor. İkinci komutumuz ``CREATE
  TABLE IF NOT EXISTS``. Bu komut da bir tabloyu eğer yoksa oluşturmamızı
  sağlıyor. Üçüncü komutumuz ise ``INSERT INTO ... VALUES ...``. Bu komut,
  oluşturduğumuz tabloya içerik eklememizi sağlıyor. Bunları şuna benzer bir
  şekilde kullandığımızı hatırlıyorsunuz:
  
::

    im.execute("CREATE TABLE personel (isim, soyisim, memleket)")
    im.execute("INSERT INTO personel VALUES ('Fırat', 'Özgül', 'Adana')")

Burada bir şey dikkatinizi çekmiş olmalı. SQL komutlarını yazmaya başlarken çift
tırnakla başladık. Dolayısıyla karakter dizisini yazarken iç taraftaki `Fırat`,
`Özgül` ve `Adana` değerlerini yazmak için tek tırnak kullanmamız gerekti.
Karakter dizileri içindeki manevra alanınızı genişletmek için, SQL komutlarını
üç tırnak içinde yazmayı da tercih edebilirsiniz. Böylece karakter dizisi
içindeki tek ve çift tırnakları daha rahat bir şekilde kullanabilirsiniz. Yani::
    
    im.execute("""CREATE TABLE personel (isim, soyisim, memleket)""")
    im.execute("""INSERT INTO personel VALUES ("Fırat", "Özgül", "Adana")""")

Ayrıca üç tırnak kullanmanız sayesinde, uzun satırları gerektiğinde bölerek çok
daha okunaklı kodlar da yazabileceğinizi biliyorsunuz.

Verilerin Veritabanına İşlenmesi
***********************************

Bir önceki bölümde bir Sqlite veritabanına nasıl veri gireceğimizi öğrendik. Ama
aslında iş sadece veri girmeyle bitmiyor. Verileri veritabanına "işleyebilmek"
için bir adım daha atmamız gerekiyor. Mesela şu örneğe bir bakalım::
    
    import sqlite3
    
    vt = sqlite3.connect("vt.sqlite")
    
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS 
        personel (isim, soyisim, sehir, eposta)""")
    
    im.execute("""INSERT INTO personel VALUES 
        ("Orçun", "Kunek", "Adana", "okunek@gmail.com")""")

Burada öncelikle `vt.sqlite` adlı bir veritabanı oluşturduk ve bu veritabanına
bağlandık. Ardından, ``vt.cursor()`` komutuyla imlecimizi de oluşturduktan
sonra, SQL komutlarımızı çalıştırıyoruz. Önce isim, soyisim, şehir ve eposta
adlı sütunlardan oluşan, "personel" adlı bir tablo oluşturduk. Daha sonra
"personel" tablosunun içine "Orçun", "Kunek", "Adana" ve "okunek@gmail.com"
değerlerini yerleştirdik.

Ancak her ne kadar veritabanına veri işlemiş gibi görünsek de aslında henüz
işlenmiş bir şey yoktur. İsterseniz bu durumu teyit etmek için Sqlitebrowser
programını kullanabilir, tabloya verilerin işlenmediğini kendi gözlerinizle
görebilirsiniz.

Biz henüz sadece verileri girdik. Ama verileri veritabanına işlemedik. Bu
girdiğimiz verileri veritabanına işleyebilmek için ``commit()`` adlı bir
metottan yararlanacağız::
    
    >>> vt.commit()

Gördüğünüz gibi, ``commit()`` imlecin değil, bağlantı nesnesinin (yani burada
``vt`` değişkeninin) bir metodudur. Şimdi bu satırı da betiğimize ekleyelim::
    
    import sqlite3
    
    vt = sqlite3.connect("vt.sqlite")
    
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS 
        personel (isim, soyisim, sehir, eposta)""")
    
    im.execute("""INSERT INTO personel VALUES 
        ("Orçun", "Kunek", "Adana", "okunek@gmail.com")""")
        
    vt.commit()

Bu son satırı da ekledikten sonra Sqlite veritabanı içinde şöyle bir tablo
oluşturmuş olduk:

    +------------------+------------------+------------------+------------------+
    | isim             | soyisim          | şehir            | eposta           |
    +==================+==================+==================+==================+
    | Orçun            | Kunek            | Adana            | okunek@gmail.com |
    +------------------+------------------+------------------+------------------+
    
Eğer ``vt.commit()`` satırını yazmazsak, veritabanı, tablo ve sütun başlıkları
oluşturulur, ama sütunların içeriği veritabanına işlenmez.

Veritabanının Kapatılması
**************************

Bir veritabanı üzerinde yapacağımız bütün işlemleri tamamladıktan sonra, prensip
olarak, o veritabanını kapatmamız gerekir. Mesela şu kodları ele alalım::
    
    import sqlite3
    
    vt = sqlite3.connect("vt.sqlite")
    
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS 
        personel (isim, soyisim, sehir, eposta)""")
    
    im.execute("""INSERT INTO personel VALUES 
        ("Orçun", "Kunek", "Adana", "okunek@gmail.com")""")
        
    vt.commit()
    vt.close()
    
    
Burada bütün işlemleri bitirdikten sonra veritabanını kapatmak için, ``close()``
adlı bir metottan yararlandık::
    
    vt.close()
    
Bu şekilde, veritabanının ilk açıldığı andan itibaren, işletim sisteminin
devreye soktuğu kaynakları serbest bırakmış oluyoruz. Esasında programımız
kapandığında, açık olan bütün Sqlite veritabanları da otomatik olarak kapanır.
Ama yine de bu işlemi elle yapmak her zaman iyi bir fikirdir. 

Eğer üzerinde işlem yaptığınız veritabanının her şey bittikten sonra otomatik
olarak kapanmasını garantilemek isterseniz, daha önce öğrendiğimiz `with`
sözcüğünü kullanabilirsiniz::
    
    import sqlite3
    
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
    
        im.execute("""CREATE TABLE IF NOT EXISTS personel 
            (isim, soyisim, memleket)""")
        im.execute("""INSERT INTO personel VALUES 
            ('Fırat', 'Özgül', 'Adana')""")
    
        vt.commit()   
        
Bu şekilde `with` sözcüğünü kullanarak bir veritabanı bağlantısı açtığımızda,
bütün işler bittikten sonra Python bizim için bağlantıyı otomatik olarak
sonlandıracaktır.

Parametreli Sorgular
*********************

Şu ana kadar verdiğimiz örneklerde, veritabanına girilecek verileri tek tek elle
yerine koyduk. Örneğin::

    im.execute("""INSERT INTO personel VALUES 
        ('Fırat', 'Özgül', 'Adana')""")
    
Ancak çoğu durumda veritabanına girilecek veriler harici kaynaklardan
gelecektir. Basit bir örnek verelim::
    
    import sqlite3

    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()
        
        veriler = [('Fırat', 'Özgül', 'Adana'),
                   ('Ahmet', 'Söz', 'Bolvadin'),
                   ('Veli', 'Göz', 'İskenderun'),
                   ('Mehmet', 'Öz', 'Kilis')]
    
        im.execute("""CREATE TABLE IF NOT EXISTS personel 
            (isim, soyisim, memleket)""")
        
        for veri in veriler:
            im.execute("""INSERT INTO personel VALUES 
                (?, ?, ?)""", veri)
    
        vt.commit()
        
Burada veritabanına işlenecek veriler, `veriler` adlı bir değişkenden geliyor.
Bu değişken içindeki verileri veritabanına nasıl yerleştirdiğimize dikkat edin::
    
    for veri in veriler:
        im.execute("""INSERT INTO personel VALUES 
            (?, ?, ?)""", veri)
        
Ayrıca her bir sütunun ('isim', 'soyisim', 'memleket') altına gelecek her bir
değer için (mesela sırasıyla 'Fırat', 'Özgül', 'Adana') bir adet '?' işareti
yerleştirdiğimizi de gözden kaçırmayın.

Tablodaki Verileri Seçmek  
***************************

Yukarıda, bir veritabanına nasıl veri gireceğimizi ve bu verileri veritabanına
nasıl işleyeceğimizi gördük. İşin asıl önemli kısmı, bu verileri daha sonra
veritabanından (yani tablodan) geri alabilmektir. Şimdi bu işlemi nasıl
yapacağımıza bakalım.

Veritabanından herhangi bir veri alabilmek için ilk olarak ``SELECT veri FROM
tablo_adı`` adlı bir SQL komutundan yararlanarak ilgili verileri seçmemiz
gerekiyor.

Dilerseniz önce bir tablo oluşturalım::

    import sqlite3

    vt = sqlite3.connect('vt.sqlite')

    im = vt.cursor()
    
    im.execute("""CREATE TABLE IF NOT EXISTS faturalar 
    (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
    
Şimdi bu tabloya bazı veriler ekleyelim::

    im.execute("""INSERT INTO faturalar VALUES 
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")

Verileri veritabanına işleyelim::

    vt.commit()

Yukarıdaki kodlar bize şöyle bir tablo verdi:

    +--------+--------+----------------+----------------+
    |fatura  | miktar |ilk_odeme_tarihi|son_odeme_tarihi|
    +========+========+================+================+
    |Elektrik| 45     |23 Ocak 2010    |30 Ocak 2010    |
    +--------+--------+----------------+----------------+

Buraya kadar olan kısmı zaten biliyoruz. Bilmediğimiz ise bu veritabanından
nasıl veri alacağımız. Onu da şöyle yapıyoruz::
    
    im.execute("""SELECT * FROM faturalar""")

Burada özel bir SQL komutu olan ``SELECT veri FROM tablo_adı`` komutundan
faydalandık. Burada joker karakterlerden biri olan "\*" işaretini kullandığımıza
dikkat edin. ``SELECT * FROM faturalar`` ifadesi şu anlama gelir: "*faturalar
adlı tablodaki bütün öğeleri seç!*"

Burada "*SELECT*" kelimesi "SEÇMEK" demektir. "*FROM*" ise "...DEN/...DAN"
anlamı verir. Yani "*SELECT FROM faturalar*" dediğimizde "faturalardan seç"
demiş oluyoruz. Burada kullandığımız "\*" işareti de "her şey" anlamına geldiği
için, "*SELECT \* FROM faturalar*" ifadesi "faturalardan her şeyi seç" gibi bir
anlama gelmiş oluyor.

Verileri seçtiğimize göre, artık seçtiğimiz bu verileri nasıl alacağımıza
bakabiliriz. Bunun için de ``fetchone()``, ``fetchall()`` veya ``fetchmany()``
adlı metotlardan ya da `for` döngüsünden yararlanacağız.

Seçilen Verileri Almak
************************

Bu bölümde, ``SELECT`` sorgusu ile veritabanından seçtiğimiz verileri farklı
yollarla nasıl çekebileceğimizi/alabileceğimizi inceleyeceğiz.

fetchall() Metodu
===================

Biraz önce şöyle bir program yazmıştık::
    
    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    
    im = vt.cursor()
    
    im.execute("""CREATE TABLE IF NOT EXISTS faturalar 
    (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
    
    im.execute("""INSERT INTO faturalar VALUES 
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
    
    vt.commit()
    
    im.execute("""SELECT * FROM faturalar""")
    
Burada `vt.sqlite` adlı bir veritabanında 'faturalar' adlı bir tablo oluşturduk
ve bu tabloya bazı veriler girdik. Daha sonra da ``SELECT`` adlı SQL komutu
yardımıyla bu verileri seçtik. Şimdi de seçtiğimiz bu verileri veritabanından
alacağız.

Yukarıdaki programa şu satırı ekliyoruz::

    veriler = im.fetchall()

Burada da ilk defa gördüğümüz bir metot var: ``fetchall()``. Gördüğünüz gibi,
``fetchall()`` imlecin bir metodudur. Yukarıda gördüğümüz ``SELECT * FROM
faturalar`` komutu 'faturalar' adlı tablodaki bütün verileri seçiyordu.
``fetchall()`` metodu ise seçilen bu verileri alma işlevi görüyor. Yukarıda biz
``fetchall()`` metoduyla aldığımız bütün verileri ``veriler`` adlı bir değişkene
atadık.

Artık bu verileri rahatlıkla yazdırabiliriz::

    print(veriler)

Dilerseniz betiğimizi topluca görelim::

    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    
    im = vt.cursor()
    
    im.execute("""CREATE TABLE IF NOT EXISTS faturalar 
    (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
    
    im.execute("""INSERT INTO faturalar VALUES 
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
    
    vt.commit()
    
    im.execute("""SELECT * FROM faturalar""")
    
    veriler = im.fetchall()
    
    print(veriler)
                
Bu betiği ilk kez çalıştırdığımızda şöyle bir çıktı alırız::
    
    [('Elektrik', 45, '23 Ocak 2010', '30 Ocak 2010')]

Gördüğünüz gibi, veriler bir liste içinde demet halinde yer alıyor. Ama tabii
siz bu verileri istediğiz gibi biçimlendirecek kadar Python bilgisine
sahipsiniz. Ayrıca programı her çalıştırdığınızda ``INSERT INTO`` sorgusu tekrar
işletileceği için verilerin tabloya tekrar tekrar yazılacağını, bu verileri
alırken de çıktı listesinin büyüyeceğini unutmayın. Peki eğer siz bir veritabanı
dosyasına verilerin yalnızca bir kez yazılmasını istiyorsanız ne yapacaksınız?
Yani mesela yukarıdaki kodlarda şu sorgu yalnızca tek bir kez işletilsin::
    
    im.execute("""INSERT INTO faturalar VALUES 
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
    
Böylece veritabanını her çalıştırdığınızda ``("Elektrik", 45, "23 Ocak 2010",
"30 Ocak 2010")`` satırı dosyaya tekrar tekrar yazdırılmasın. 

Bunu şu kodlarla halledebilirsiniz::
    
    import sqlite3, os
    
    dosya = 'vt.sqlite'
    dosya_mevcut = os.path.exists(dosya)
    
    vt = sqlite3.connect(dosya)
    im = vt.cursor()
    
    im.execute("""CREATE TABLE IF NOT EXISTS faturalar 
    (fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
    
    if not dosya_mevcut:
        im.execute("""INSERT INTO faturalar VALUES 
        ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
        vt.commit()
    
    im.execute("""SELECT * FROM faturalar""")
    
    veriler = im.fetchall()
    print(veriler)
    
Burada kodlarımızın en başında `vt.sqlite` adlı bir veritabanının mevcut olup
olmadığını kontrol ediyoruz (zira eğer ortada bir veritabanı dosyası yoksa, veri
de yok demektir)::
    
    dosya_mevcut = os.path.exists(dosya)
    
Eğer böyle bir dosya mevcut değilse (dolayısıyla veri mevcut değilse) ``INSERT
INTO`` sorgusu işletilerek gerekli veriler yerine yerleştirilecek::
    
    if not dosya_mevcut:
        im.execute("""INSERT INTO faturalar VALUES 
        ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
        vt.commit()
        
Eğer böyle bir dosya zaten mevcutsa bu sorgu işletilemeyecek, onun yerine
doğrudan ``SELECT`` sorgusuna geçilecek. Böylece değerler veritabanına bir kez
işlendikten sonra, programımız aynı verileri tekrar tekrar veritabanına
yerleştirmeye çalışmayacak.

Bu arada, daha önce de belirttiğimiz gibi, tablo oluştururken sütun adlarında
boşluk (ve Türkçe karakter) kullanmak iyi bir fikir değildir. Mesela ``ilk ödeme
tarihi`` yerine ``ilk_odeme_tarihi`` ifadesini tercih edin. Eğer kelimeler
arasında mutlaka boşluk bırakmak isterseniz bütün kelimeleri tırnak içine alın.
Mesela: ``"ilk odeme tarihi"`` veya ``"ilk ödeme tarihi"`` gibi.

Yukarıda gördüğünüz gibi, ``fetchall()`` metodu, bir veritabanından ``SELECT``
ile seçtiğimiz bütün verileri önümüze getiriyor. Eğer seçilen verilerden kaç
tanesini almak istediğinizi kendiniz belirlemek istiyorsanız ``fetchall()``
yerine ``fetchone()`` veya ``fetchmany()`` metotlarından o anki amacınıza uygun
olanını kullanmayı tercih edebilirsiniz. Birazdan ``fetchone()`` ve
``fetchmany()`` metotlarından da söz edeceğiz.

Gelin isterseniz şimdi ``fetchall()`` metodunu kullanarak veritabanlarından veri
çekme konusunda biraz alıştırma yapalım. Bu alıştırmalar için, daha önce söz
ettiğimiz ve bilgisayarımıza indirdiğimiz `kitaplar.sqlite` adlı örnek
veritabanını kullanacağız.

Öncelikle veritabanına bağlanalım ve bir imleç oluşturalım::
    
    >>> import sqlite3
    >>> vt = sqlite3.connect('kitaplar.sqlite')
    >>> im = vt.cursor()
    
Şimdi bu veritabanındaki tabloyu seçeceğiz. Peki ama seçeceğimiz tablonun adını
nereden bileceğiz? Hatırlarsanız, bir tablodaki bütün verileri seçebilmek için
şu SQL sorgusunu kullanıyorduk::
    
    "SELECT * FROM tablo_adı"
    
İşte bu sorguda 'tablo_adı' kısmına ne geleceğini bulabilmek için birkaç farklı
yöntemden yararlanabiliriz. 

Bir veritabanında hangi tabloların olduğunu öğrenmek için Sqlitebrowser
programını kullanabiliriz. Bir veritabanı dosyasını Sqlitebrowser ile açtıktan
sonra, 'Browse Data' sekmesine gidip, 'Table' ifadesinin karşısında ne yazdığına
bakabiliriz.

Veritabanındaki tabloların adını öğrenmenin ikinci yolu şu komutları
kullanmaktır::

    >>> import sqlite3
    >>> vt = sqlite3.connect('kitaplar.sqlite')
    >>> im = vt.cursor()
    >>> im.execute("SELECT name FROM sqlite_master")
    >>> im.fetchall()
    
Burada şu satıra dikkat edin::
    
    >>> im.execute("SELECT name FROM sqlite_master")

Bütün Sqlite veritabanlarında, ilgili veritabanının şemasını gösteren
'sqlite_master' adlı bir tablo bulunur. İşte bu tabloyu sorgulayarak veritabanı
hakkında bilgi edinebiliriz. Yukarıdaki örnekte, bu 'sqlite_master' tablosunun
'name' (isim) niteliğini sorguladık. Bu sorgu bize şu cevabı verdi::
    
    >>> im.fetchall()
    
    [('kitaplar',)]
    
Demek ki `kitaplar.sqlite` adlı veritabanında 'kitaplar' adlı tek bir tablo
varmış.

Gelin şimdi bu bu tablodaki bütün verileri alalım::
    
    >>> im.execute("SELECT * FROM kitaplar")
    >>> im.fetchall()
    
Bu şekilde tablo içinde ne kadar veri varsa hepsini ekrana yazdırdık. Ancak
tabii ki, bir veritabanının tamamını bir anda yazdırmak her zaman iyi bir fikir
olmayabilir. Eğer veritabanının içinde milyonlarca girdi varsa bütün verilerin
seçilip yazdırılması mantıklı olmayacaktır. Gelin o halde şimdi bizim seçilen
verilerin ne kadarını çekeceğimizi belirleyebilmemizi sağlayacak metotları
inceleyelim.

fetchone() Metodu
==================

``fetchone()`` metodu, bir veritabanından seçilen verilerin tek tek
alınabilmesine izin verir.

Bu metodun nasıl kullanılacağını 'kitaplar.sqlite' adlı örnek veritabanımız
üzerinden inceleyelim:

Önce veritabanına bağlanalım::

    >>> import sqlite3
    >>> vt = sqlite3.connect('kitaplar.sqlite')
    >>> im = vt.cursor()
    
Şimdi 'kitaplar' adlı tablodan bütün verileri seçelim::
    
    >>> im.execute("""SELECT * FROM kitaplar""")
    
    <sqlite3.Cursor object at 0x003C2D20>
    
Artık seçtiğimiz verileri tek tek almaya başlayabiliriz::
    
    >>> im.fetchone()
    
    ('UZMANLAR İÇİN PHP', 'Mehmet Şamlı', '33,00 TL')
    
Bir tane daha alalım::
    
    >>> im.fetchone()
    
    ('ADOBE AİR', 'Engin Yöğen', '28,00 TL')
    
İki tane daha...

::
    
    >>> im.fetchone()
    
    ('WEB TASARIM REHBERİ', 'Mustafa Aydemir', '38,50 TL')
    
    >>> im.fetchone()
    
    ('ORACLE 11g R2', 'Teoman Dinçel', '34,00 TL')
    
``fetchone()``'ın gayet faydalı bir metot olduğu her halinden belli...
    
fetchmany() Metodu
===================

Bu metot, bir veritabanından seçtiğiniz verilerin istediğiniz kadarını
alabilmenize imkan tanır. Dikkatlice bakın::
    
    >>> im.fetchmany(5)
    
    [('AS 3.0 İLE SUNUCU PROGRAMLAMA', 'Engin Yöğen', '24,00 TL'), 
     ('HACKING INTERFACE', 'Hamza Elbahadır', '25,00 TL'), 
     ('JAVA VE JAVA TEKNOLOJİLERİ', 'Tevfik Kızılören', '45,00 TL'), 
     ('XML VE İLERİ XML TEKNOLOJİLERİ', 'Musa Çiçek', '24,50 TL'), 
     ('GRAFİK&ANİMASYON', 'Anonim', '18,50 TL')]
     
Gördüğünüz gibi, beş öğeden oluşan bir liste elde ettik. 

Böylece bir veritabanından seçilen verileri almanın farklı yöntemlerini öğrenmiş
olduk. Bu metotların dışında, eğer arzu ederseniz `for` döngüsünden yararlanarak
da veri çekebilirsiniz. Bunun için herhangi bir metot kullanmanıza gerek yok::
    
    >>> for veri in im:
    ...     print(veri)
    
Gördüğünüz gibi, `for` döngüsünü doğrudan imleç üzerinde kuruyoruz. 

Eğer amacınız alınacak verilerin sayısını sınırlamaksa yine `for` döngüsünden ve
``fetchone()`` metodundan birlikte yararlanabilirsiniz::
    
    >>> for i in range(5):
    ...     print(im.fetchone())
    
Biraz sonra veri süzmeyi öğrendiğimizde, bir veritabanından veri seçip almanın
daha verimli yollarını göreceğiz.

Veri Süzme 
***********

Daha önce bir Sqlite veritabanında belli bir tablo içindeki bütün verileri
seçmek için şu SQL komutunu kullanmamız gerektiğini öğrenmiştik::
    
    SELECT * FROM tablo_adi
    
Ancak amacımız çoğu zaman bir tablo içindeki bütün verileri seçmek olmayacaktır.
Programcılık maceramız boyunca genellikle yalnızca belli ölçütlere uyan verileri
seçmek isteyeceğiz. Zira içinde milyonlarca veri barındırabilecek olan
veritabanlarındaki verilerin tamamını seçmek akıl kârı değildir. 

Verileri süzme işini ``WHERE`` adlı bir SQL komutu yardımıyla
gerçekleştireceğiz. Bu SQL komutunun sözdizimi şöyle::
  
    SELECT * FROM tablo_adı WHERE sütun_başlığı = aranan_veri
    
Gördüğünüz gibi, bu sorguyu gerçekleştirebilmek için tablodaki sütun
başlıklarını bilmemiz gerekiyor.

Önceki sayfalarda, `kitaplar.sqlite` adlı veritabanımızdaki tabloların adını
nasıl öğrenebileceğimizi anlatmıştık. Hatırlarsanız bu iş için şu komutu
kullanıyorduk::
    
    >>> im.execute("SELECT name FROM sqlite_master")
    
Bu şekilde, bütün Sqlite veritabanlarında bulunan 'sqlite_master' adlı özel bir
tablonun 'name' niteliğini sorgulayarak, elimizdeki veritabanında bulunan
tabloların adını elde edebiliyoruz. Adını öğrendiğimiz tablodaki sütun
başlıklarını elde etmek için yine buna benzer bir komuttan yararlanacağız.
Dikkatlice bakın::
    
    >>> im.execute("SELECT sql FROM sqlite_master").fetchone()
    
    ('CREATE TABLE "kitaplar" 
    (\n\t`KitapAdi`\tTEXT,\n\t`Yazar`\tTEXT,\n\t`Fiyati`\tTEXT\n)',)
    
'sqlite_master' adlı tablonun 'sql' niteliğini sorguladığımızda, ilgili tabloyu
oluşturmak için kullanılan SQL komutunu görüyoruz. Bu komuta dikkatli
bakarsanız, tablonun 'KitapAdi', 'Yazar' ve 'Fiyati' olmak üzere üç sütundan
oluştuğunu göreceksiniz. Elbette sütun adlarını öğrenmek için Sqlitebrowser 
programını da kullanabileceğinizi artık biliyorsunuz. 

Sütun adlarını öğrendiğimize göre gelin şimdi yazar adına göre veritabanında bir
sorgu yapalım::
    
    >>> im.execute("SELECT * FROM kitaplar WHERE Yazar = 'Fırat Özgül'")
    
Burada sorguyu nasıl kurduğumuza dikkat edin. Bu sorgunun ilk kısmı olan
``SELECT * FROM kitaplar`` ifadesini zaten daha önce öğrenmiştik. Yeni olan
kısım ``WHERE Yazar = 'Fırat Özgül'``. Burada da anlaşılmayacak bir şey yok. Bu
şekilde, veritabanındaki 'kitaplar' tablosunun 'Yazar' sütununda 'Fırat Özgül'
bulunan bütün kayıtları seçiyoruz.

Şimdi de seçtiğimiz bu verileri alalım::

    >>> im.fetchall()
    
    ('HERYÖNÜYLE PYTHON', 'Fırat Özgül', '34,00 TL')
    
Gayet başarılı... Bu arada, verileri almak için ``fetchall()`` yerine `for`
döngüsü kullanabileceğinizi de biliyorsunuz::
    
    >>> for s in im:
    ...     print(s)
    ...
    ('HERYÖNÜYLE PYTHON', 'Fırat Özgül', '34,00 TL')
    
İmleç üzerinde `for` döngüsü kurabildiğimize göre yıldızlı parametrelerden de
yararlanabileceğimizi tahmin etmişsinizdir::
    
    >>> print(*im)
    
    ('HERYÖNÜYLE PYTHON', 'Fırat Özgül', '34,00 TL')
    

Veritabanı Güvenliği 
*********************

Python'da veritabanları ve Sqlite konusunda daha fazla ilerlemeden önce çok
önemli bir konudan bahsetmemiz gerekiyor. Tahmin edebileceğiniz gibi, veritabanı
denen şey oldukça hassas bir konudur. Bilgiyi bir araya toplayan bu sistem,
içerdeki bilgilerin değerine ve önemine de bağlı olarak üçüncü şahısların
iştahını kabartabilir. Ancak depoladığınız verilerin ne kadar değerli ve önemli
olduğundan bağımsız olarak veritabanı güvenliğini sağlamak, siz programcıların
asli görevidir.

Peki veritabanı yönetim sistemleri acaba hangi tehditlerle karşı karşıya?

SQL komutlarını işleten bütün veritabanları için günümüzdeki en büyük
tehditlerden birisi hiç kuşkusuz kötü niyetli kişilerin veritabanınıza SQL
komutu sızdırma (*SQL injection*) girişimleridir.

Şimdi şöyle bir şey düşünün: Diyelim ki siz bir alışveriş karşılığı birine
100.000 TL'lik bir çek verdiniz. Ancak çeki verdiğiniz kişi bu çek üzerindeki
miktarı tahrif ederek artırdı ve banka da tahrif edilerek artırılan bu miktarı
çeki getiren kişiye (hamiline) ödedi. Böyle bir durumda epey başınız
ağrıyacaktır.

İşte böyle tatsız bir durumla karşılaşmamak için, çek veren kişi çekin
üzerindeki miktarı hem rakamla hem de yazıyla belirtmeye özen gösterir. Ayrıca
rakam ve yazılara ekleme yapılmasını da engellemek için rakam ve yazıların
sağına soluna "#" gibi işaretler de koyar. Böylece çeki alan kişinin, kendisine
izin verilenden daha fazla bir miktarı yazmasını engellemeye çalışır.

Yukarıdakine benzer bir şey veritabanı uygulamalarında da karşımıza çıkabilir.
Şimdi şu örneğe bakalım::
    
    import sqlite3
    
    #vt.sqlite adlı bir veritabanı dosyası oluşturup
    #bu veritabanına bağlanıyoruz.
    db = sqlite3.connect("vt.sqlite")
    
    #Veritabanı üzerinde istediğimiz işlemleri yapabilmek
    #için bir imleç oluşturmamız gerekiyor.
    im = db.cursor()
    
    #imlecin execute() metodunu kullanarak, veritabanı içinde 
    #"kullanicilar" adlı bir tablo oluşturuyoruz. Bu tabloda
    #kullanıcı_adi ve parola olmak üzere iki farklı sütun var.
    im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar 
        (kullanici_adi, parola)""")

    #Yukarıda oluşturduğumuz tabloya yerleştireceğimiz verileri
    #hazırlıyoruz. Verilerin liste içinde birer demet olarak
    #nasıl gösterildiğine özellikle dikkat ediyoruz.
    veriler = [
                ("ahmet123", "12345678"),
                ("mehmet321", "87654321"),
                ("selin456", "123123123")
              ]

    #veriler adlı liste içindeki bütün verileri kullanicilar adlı
    #tabloya yerleştiriyoruz. Burada tek öğeli bir demet
    #tanımladığımıza dikkat edin: (i,)
    for i in veriler:
        im.execute("""INSERT INTO kullanicilar VALUES %s""" %(i,))

    #Yaptığımız değişikliklerin tabloya işlenebilmesi için
    #commit() metodunu kullanıyoruz.
    db.commit()
    
    #Kullanıcıdan kullanıcı adı ve parola bilgilerini alıyoruz...
    kull = input("Kullanıcı adınız: ")
    paro = input("Parolanız: ")
    
    #Burada yine bir SQL komutu işletiyoruz. Bu komut, kullanicilar
    #adlı tabloda yer alan kullanici_adi ve parola adlı sütunlardaki
    #bilgileri seçiyor. 
    im.execute("""SELECT * FROM kullanicilar WHERE 
    kullanici_adi = '%s' AND parola = '%s'"""%(kull, paro))
    
    #Hatırlarsanız daha önce fetchall() adlı bir metottan
    #söz etmiştik. İşte bu fetchone() metodu da ona benzer.
    #fetchall() bütün verileri alıyordu, fetchone() ise
    #verileri tek tek alır.
    data = im.fetchone()

    #Eğer data adlı değişken False değilse, yani bu
    #değişkenin içinde bir değer varsa kullanıcı adı
    #ve parola doğru demektir. Kullanıcıyı içeri alıyoruz. 
    if data:
        print("Programa hoşgeldin {}!".format(data[0]))
    
    #Aksi halde kullanıcıya olumsuz bir mesaj veriyoruz.
    else:
        print("Parola veya kullanıcı adı yanlış!")

Bu örnekte henüz bilmediğimiz bazı kısımlar var. Ama siz şimdilik bunları
kafanıza takmayın. Nasıl olsa bu kodlarda görünen her şeyi biraz sonra tek tek
öğreneceğiz. Siz şimdilik sadece işin özüne odaklanın.

Yukarıdaki kodları çalıştırdığınızda, eğer kullanıcı adı ve parolayı doğru
girerseniz 'Programa hoşgeldin' çıktısını göreceksiniz. Eğer kullanıcı adınız
veya parolanız yanlışsa bununla ilgili bir uyarı alacaksınız.

Her şey iyi hoş, ama bu kodlarda çok ciddi bir problem var.

Dediğimiz gibi, bu kodlar çalışırken (teoride) eğer kullanıcı, veritabanında
varolan bir kullanıcı adı ve parola yazarsa sisteme kabul edilecektir. Eğer
doğru kullanıcı adı ve parola girilmezse sistem kullanıcıya giriş izni
vermeyecektir. Ama acaba gerçekten öyle mi?

Şimdi yukarıdaki programı tekrar çalıştırın. Kullanıcı adı ve parola
sorulduğunda da her ikisi için şunu yazın::
    
    x' OR '1' = '1

O da ne! Program sizi içeri aldı... Hem de kullanıcı adı ve parola doğru
olmadığı halde... Hatta şu kodu sadece kullanıcı adı kısmına girip parola
kısmını boş bırakmanız da sisteme giriş hakkı elde etmenize yetecektir.::
    
    x' OR '1' = '1' --

İşte yukarıda gösterdiğimiz bu işleme "SQL sızdırma" (SQL injection) adı verilir.
Kullanıcı, tıpkı en başta verdiğimiz tahrif edilmiş çek örneğinde olduğu gibi,
sistemin zaaflarından yararlanarak, elde etmeye hakkı olandan daha fazlasına
erişim hakkı elde ediyor.

Burada en basit şekliyle bool işleçlerinden biri olan ``or``'dan yararlanıyoruz.
``or``'un nasıl işlediğini gayet iyi biliyorsunuz, ama ben yine de birkaç
örnekle ``or``'un ne olduğunu ve ne yaptığını size hatırlatayım. Şu örneklere
bakın::
    
    >>> a = 21
    
    >>> a == 22
    
    False
    
    >>> b = 13
    
    >>> b == 13
    
    True

    >>> if a == 22 and b == 13:
    ...     print("Merhaba!")
    ...
    
    >>> if a == 22 or b == 13:
    ...     print("Merhaba!")
    ...
    Merhaba!

Örneklerden de gördüğünüz gibi, ``and`` işlecinin ``True`` sonucunu verebilmesi
için her iki önermenin de doğru olması gerekir. O yüzden ``a == 22 and b == 13``
gibi bir ifade ``False`` değeri veriyor. Ancak ``or`` işlecinin ``True`` sonucu
verebilmesi için iki önermeden sadece birinin doğru olması yeterlidir. Bu
yüzden, sadece ``b == 13`` kısmı ``True`` olduğu halde ``a == 22 or b == 13``
ifadesi ``True`` sonucu veriyor... İşte biz de yukarıdaki SQL sızdırma
girişiminde ``or``'un bu özelliğinden faydalanıyoruz.

Dilerseniz neler olup bittiğini daha iyi anlayabilmek için, sızdırılan kodu
doğrudan ilgili satıra uygulayalım::

    im.execute("""SELECT * FROM kullanicilar WHERE 
    kullanici_adi = 'x' OR '1' = '1' AND parola = 'x' OR '1' = '1'""")

Sanırım bu şekilde neler olup bittiği daha net görülüyor. Durumu biraz daha
netleştirmek için Python'ı yardıma çağırabiliriz::
    
    >>> kullanici_adi = 'ahmet123'
    
    >>> parola = '12345678'
    
    >>> kullanici_adi == 'x'
    
    False
    
    >>> '1' == '1'
    
    True
    
    >>> kullanici_adi == 'x' or '1' == '1' 
    
    True
    
    >>> parola == 'x'
    
    False

    >>> (kullanici_adi == 'x' or '1' == '1') and (parola == 'x' or '1' == '1')
    
    True

``'1' == '1'`` ifadesi her zaman ``True`` değeri verecektir. Dolayısıyla
kullanıcı adının ve parolanın doğru olup olmaması hiçbir önem taşımaz. Yani her
zaman ``True`` değerini vereceği kesin olan ifadeler yardımıyla yukarıdaki gibi
bir sızdırma girişiminde bulunabilirsiniz.

Yukarıda yaptığımız şey, '%s' ile gösterilen yerlere kötü niyetli bir SQL komutu
sızdırmaktan ibarettir. Burada zaten başlangıç ve bitiş tırnakları olduğu için
sızdırılan kodda başlangıç ve bitiş tırnaklarını yazmıyoruz. O yüzden sızdırılan
kod şöyle görünüyor::
    
    x' OR '1' = '1  

Gördüğünüz gibi, x'in başındaki ve 1'in sonundaki tırnak işaretleri koymuyoruz.

Peki yukarıda verdiğimiz şu kod nasıl çalışıyor::

    x' OR '1' = '1' --

Python'da yazdığımız kodlara yorum eklemek için "#" işaretinden yararlandığımızı
biliyorsunuz. İşte SQL kodlarına yorum eklemek için de "--" işaretlerinden
yararlanılır. Şimdi dilerseniz yukarıdaki kodu doğrudan ilgili satıra
uygulayalım ve ne olduğunu görelim::
    
    im.execute("""SELECT * FROM kullanicilar WHERE 
    kullanici_adi = 'x' OR '1'='1' --AND parola = '%s'""")

Burada yazdığımız "--" işareti ``AND parola = '%s'`` kısmının sistem tarafından
yorum olarak algılanmasını sağlıyor. Bu yüzden kodların bu kısmı işletilmiyor.
Dolayısıyla da sisteme giriş yapabilmek için sadece kullanıcı adını girmemiz
yeterli oluyor. Burada ayrıca kodlarımızın çalışması için 1'in sonuna bir adet
tırnak yerleştirerek kodu kapattığımıza dikkat edin. Çünkü normal bitiş tırnağı
yorum tarafında kaldı.

Dikkat ederseniz SQL sızdırdığımızda "ahmet123" adlı kullanıcının hesabını ele
geçirmiş olduk. Peki neden ötekiler değil de "ahmet123"? Bunun sebebi,
"ahmet123" hesabının tablonun en başında yer alması. Eğer tablonun başında
"admin" diye bir hesap olmuş olsaydı, veritabanına azami düzeyde zarar verme
imkanına kavuşacaktınız.

Peki SQL sızdırma girişimlerini nasıl önleyeceğiz? Bu girişime karşı
alabileceğiniz başlıca önlem "%s" işaretlerini kullanmaktan kaçınmak olacaktır.
Bu işaret yerine "?" işaretini kullanacaksınız. Yani yukarıdaki programı şöyle
yazacağız::
    
    import sqlite3
    
    db = sqlite3.connect("vt.sqlite")
    
    im = db.cursor()
    
    im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar 
        (kullanici_adi, parola)""")
    
    veriler = [
                ("ahmet123", "12345678"),
                ("mehmet321", "87654321"),
                ("selin456", "123123123")
              ]
    
    for i in veriler:
        im.execute("""INSERT INTO kullanicilar VALUES (?, ?)""", i)
    
    db.commit()
    
    kull = input("Kullanıcı adınız: ")
    paro = input("Parolanız: ")
    
    im.execute("""SELECT * FROM kullanicilar WHERE
    kullanici_adi = ? AND parola = ?""", (kull, paro))
    
    data = im.fetchone()
    
    if data:
        print("Programa hoşgeldin {}!".format(data[0]))
    else:
        print("Parola veya kullanıcı adı yanlış!")

Dediğimiz gibi, SQL sızdırma girişimlerine karşı alabileceğiniz başlıca önlem
"%s" işaretleri yerine "?" işaretini kullanmak olmalıdır. Bunun dışında, SQL
komutlarını işletmeden önce bazı süzgeçler uygulamak da güvenlik açısından
işinize yarayabilir. Örneğin kullanıcıdan alınacak verileri alfanümerik
karakterlerle [`http://www.istihza.com/blog/alfanumerik-ne-demek.html/
<http://www.istihza.com/blog/alfanumerik-ne-demek.html/>`_]
sınırlayabilirsiniz::
    
    if kull.isalnum() and paro.isalnum():
        im.execute("""SELECT * FROM kullanicilar WHERE
        kullanici_adi = '%s' AND parola = '%s'"""%(kull, paro))

Böylece kullanıcının bazı "tehlikeli" karakterleri girmesini engelleyebilir,
onları sadece harf ve sayı girmeye zorlayabilirsiniz.

Her halükarda unutmamamız gereken şey, güvenliğin çok boyutlu bir kavram
olduğudur. Birkaç önlemle pek çok güvenlik açığını engelleyebilirsiniz, ancak
bütün güvenlik açıklarını bir çırpıda yamamak pek mümkün değildir. Bir programcı
olarak sizin göreviniz, yazdığınız programları güvenlik açıklarına karşı sürekli
taramak ve herhangi bir açık ortaya çıktığında da bunu derhal kapatmaya
çalışmaktır.


Bölüm Soruları
*****************

#. Bir veritabanı dosyasının var olup olmadığını nasıl tespit edersiniz? 

#. Bir veritabanı içinde belli bir tablonun var olup olmadığını tespit edin.
   Eğer yoksa o tabloyu oluşturun, varsa herhangi bir işlem yapmayın.
   
#. Sqlite ile test amaçlı bir veritabanı oluşturun. Bu veritabanı dosyası,
   programınız kapanır kapanmaz ortadan kaybolmalı.

#. Aşağıdaki kodların istenen veritabanını, tabloyu, satır ve sütunları
   oluşturup oluşturmadığını teyit edin::

    import sqlite3
    
    vt = sqlite3.connect('vt.sqlite')
    
    im = vt.cursor()
    im.execute("CREATE TABLE kullanıcılar (ad, soyad, doğumtarihi, eposta)")
    
    vt.commit()
    vt.close()

   Eğer veritabanı içeriği beklediğiniz gibi değilse sebebini açıklayın.
   
#. Sqlite ile bir veritabanının oluşturulması ve bu veritabanına birtakım
   bilgiler girilebilmesi için sırasıyla hangi işlemlerin yapılması gerekir?
   
#. Aşağıdaki resimde yapılmaya çalışılan şey nedir?

    .. figure:: ../images/misc/sql.jpg
        :align: center
        
#. ``sqlite3.connect('kitaplar.sqlite')`` boş bir veritabanının mı
   oluşturulduğunu yoksa varolan `kitaplar.sqlite` adlı bir veritabanı dosyasına
   mı bağlandığınızı nasıl teyit edersiniz?
   
#. Sqlitebrowser programını ne şekilde kurdunuz? Eğer Ubuntu dışında bir
   GNU/Linux dağıtımına bu programı kurduysanız, programın kurulum aşamalarını
   anlatın. 
   
#. ``cmake`` komutu ile birlikte kullandığımız ``.`` (nokta) işaretinin anlamı
   nedir?
   
#. Yazdığınız bir programı kullanan kişilerin, programınızı ilk kez
   çalıştırdıklarında karşılarında görmeleri gereken verileri veritabanına
   yerleştirmek için nasıl bir yöntem takip edebilirsiniz? Kullanıcılarınız
   programınızı ikinci kez çalıştırdığında bu verileri görmemeli.
   
#. Bir önceki soruda uyguladığınız yöntemin herhangi bir kısıtlaması var mı? Bu
   yöntem hangi durumlarda işe yaramaz?
   
#. Bir veritabanındaki bütün tabloların adını nasıl listelersiniz?