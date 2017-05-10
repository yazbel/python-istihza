.. meta:: :description: Bu bölümde Python programlama dilinin farklı işletim
           sistemlerine nasıl kurulacağını anlatacağız. 
          :keywords: python, python2, python3, kurulum, kaynaktan, Windows, GNU, 
           Linux, root, configure, prefix, home, ev, path, yol

.. highlight:: none 

********************** 
Python Nasıl Kurulur?
**********************

Python ile program yazabilmemiz için bu programlama dilinin bilgisayarımızda
kurulu olması gerekiyor. Bu programlama dilini kurmanızın gerekip gerekmediği,
kullandığınız işletim sistemine bağlıdır. Biz burada hem GNU/Linux hem de
Windows kullanıcılarının durumunu sırasıyla ve ayrı ayrı inceleyeceğiz.
Dilerseniz öncelikle GNU/Linux kullanıcılarının durumuna bakalım:

.. note:: Bu kitap boyunca bazı konuların GNU/Linux ve Windows kullanıcıları
 için ayrı ayrı anlatıldığını göreceksiniz. Ancak konular bu şekilde ayrılmış da
 olsa, ben size her ikisini de okumanızı tavsiye ederim. Çünkü bu bölümlerde her
 iki kullanıcı grubunun da ilgisini çekebilecek bilgilere rastlayacaksınız.
 Ayrıca bu bölümler farklı kullanıcı gruplarına hitap ediyor olsa da, aslında bu
 bölümlerin birbirini tamamlayıcı nitelikte olduğunu göreceksiniz.

GNU/Linux Kullanıcıları 
***********************

GNU/Linux dağıtımlarına Python programlama dilini kurarken bazı noktaları göz
önünde bulundurmamız gerekiyor. İşte bu bölümde bu önemli noktaların neler
olduğunu inceleyeceğiz.

Kurulu Python Sürümü 
====================

Hemen hemen bütün GNU/Linux dağıtımlarında Python programlama dili kurulu olarak
gelir. Örneğin Ubuntu'da Python zaten kuruludur.

Ancak burada şöyle bir durum var:

Daha önce de belirttiğimiz gibi, şu anda piyasada iki farklı Python serisi
bulunuyor. Bunlardan birinin Python'ın 2.x serisi, ötekinin ise 3.x serisi
olduğunu biliyorsunuz. 

Sisteminizde kurulu olan Python sürümünü denetlemek için komut satırında
öncelikle şu komutu vermeyi deneyin (büyük 'V' ile)::
    
    python -V 

Eğer bu komuttan `Python 2.x.y` şeklinde bir çıktı alıyorsanız, yani x ve y'den
önceki kısım 2 ile başlıyorsa sisteminizde Python2 kuruludur.

Ancak ``python -V`` komutundan `Python 2.x.y` şeklinde bir çıktı almanız
sisteminizde **sadece** Python2'nin kurulu olduğunu göstermez. Sisteminizde
Python2 ile birlikte Python3 de halihazırda kurulu olabilir. Örneğin Ubuntu
GNU/Linux'un **12.10** sürümünden itibaren hem Python2, hem de Python3 sistemde
kurulu vaziyettedir.

Kullandığınız GNU/Linux dağıtımında durumun ne olduğunu denetlemek için
yukarıdaki komutu bir de ``python3 -V`` şeklinde çalıştırmayı deneyebilirsiniz.
Eğer bu komut size bir hata mesajı yerine bir sürüm numarası veriyorsa
sisteminizde Python3 de kuruludur. 

Sisteminizdeki Python sürümlerine ilişkin daha kesin bir rapor için ise şu
komutu kullanabilirsiniz::
    
    ls -g {,/usr{,/local}}/bin | grep python 

Buradan aldığınız çıktıyı inceleyerek de sisteminizde birden fazla Python
sürümünün kurulu olup olmadığını görebilirsiniz. [Bununla ilgili bir
tartışma için bkz. http://goo.gl/RnRRc]

Ayrıca kullandığınız GNU/Linux dağıtımında ``whereis python`` gibi bir komut
vererek de sistemde kurulu Python sürümleri hakkında bilgi edinebilirsiniz. 

Eğer sisteminizde Python3 kuruluysa  ve siz de kurulu olan Python3 sürümünden
memnunsanız herhangi bir şey yapmanıza gerek yok. Farklı bir Python sürümü
kurmaya çalışmadan yolunuza devam edebilirsiniz.

Paket Deposundan Kurulum 
========================= 

Sistemlerinde öntanımlı olarak herhangi bir Python3 sürümü kurulu olmayan veya
sistemlerinde kurulu öntanımlı Python3 sürümünden memnun olmayan GNU/Linux
kullanıcılarının, Python3'ü elde etmek için tercih edebileceği iki yol var:
Birincisi ve benim size önereceğim yol, öncelikle kullandığınız dağıtımın paket
yöneticisini kontrol etmenizdir. Python3 sisteminizde kurulu olmasa bile,
dağıtımınızın depolarında bu sürüm paketlenmiş halde duruyor olabilir. O yüzden
sisteminize uygun bir şekilde paket yöneticinizi açıp orada 'python' kelimesini
kullanarak bir arama yapmanızı öneririm. Örneğin Ubuntu GNU/Linux dağıtımının
paket depolarında Python3 var. Dolayısıyla Ubuntu kullanıcıları, eğer
sistemlerinde zaten kurulu değilse (ki muhtemelen kuruludur), bu paketi Ubuntu
Yazılım Merkezi aracılığıyla veya doğrudan şu komutla kurabilir::

	sudo apt-get install python3

Bu komut, Python3'ü bütün bağımlılıkları ile beraber bilgisayarınıza kuracaktır.

Kaynaktan Kurulum 
=========================

Peki ya kullandığınız dağıtımın depolarında Python3 yoksa veya depodaki Python3
sürümü eskiyse ve siz daha yeni bir Python3 sürümü kullanmak istiyorsanız ne
yapacaksınız?

Eğer dağıtımınızın depolarında Python3 paketini bulamazsanız veya depodaki sürüm
sizi tatmin etmiyorsa, Python3'ü kaynaktan derlemeniz gerekecektir. Python3'ü
kaynaktan derlerken iki seçeneğiniz var: Python3'ü `root` hakları ile kurmak
veya Python3'ü yetkisiz kullanıcı olarak kurmak. Normal şartlar altında eğer
kullandığınız sistemde `root` haklarına sahipseniz Python3'ü yetkili kullanıcı
olarak kurmanızı tavsiye ederim.

root Hakları İle Kurulum 
----------------------------- 

Python'ı kurmadan önce sistemimizde bulunması gereken bazı programlar var.
Aslında bu programlar olmadan da Python kurulabilir, ancak eğer bu programları
kurmazsanız Python'ın bazı özelliklerinden yararlanamazsınız. Bu programlar
şunlardır:

    #. tcl-dev 
    #. tk-dev 
    #. zlib1g-dev 
    #. ncurses-dev 
    #. libreadline-dev
    #. libdb-dev 
    #. libgdbm-dev 
    #. libzip-dev 
    #. libssl-dev 
    #. libsqlite3-dev 
    #. libbz2-dev
    #. liblzma-dev

Bu programları, kullandığınız GNU/Linux dağıtımının paket yöneticisi
aracılığıyla kurabilirsiniz. Yalnız paket adlarının ve gerekli paket sayısının
dağıtımlar arasında farklılık gösterebileceğini unutmayın. Yukarıdaki liste
Ubuntu için geçerlidir. Mesela yukarıda `tcl-dev` olarak verdiğimiz paket adı
başka bir dağıtımda sadece `tcl` olarak geçiyor ya da yukarıdaki paketlerin
bazıları kullandığınız dağıtımda halihazırda kurulu olduğu için sizin daha az
bağımlılık kurmanız gerekiyor olabilir.

Ubuntu'da yukarıdaki paketlerin hepsini şu komutla kurabilirsiniz::

    sudo apt-get install tcl-dev tk-dev 
    zlib1g-dev ncurses-dev libreadline-dev 
    libdb-dev libgdbm-dev libzip-dev libssl-dev 
    libsqlite3-dev libbz2-dev liblzma-dev

.. note:: Farklı GNU/Linux dağıtımlarında, Python3'ü kaynaktan derleme
 işleminden önce halihazırda kurulu olması gereken paketlerin listesi için
 http://goo.gl/zfLpX adresindeki tabloyu inceleyebilirsiniz.

Yukarıdaki programları kurduktan sonra |download| adresine gidiyoruz. Bu
adreste, üzerinde 'Python-|py3|.tar.xz' yazan bağlantıya tıklayarak
sıkıştırılmış kurulum dosyasını bilgisayarımıza indiriyoruz.  

Daha sonra bu sıkıştırılmış dosyayı açıyoruz. Açılan klasörün içine girip, orada
ilk olarak şu komutu veriyoruz::
    
    ./configure

Bu komut, Python programlama dilinin sisteminize kurulabilmesi için gereken
hazırlık aşamalarını gerçekleştirir. Bu betiğin temel olarak yaptığı iş,
sisteminizin Python programlama dilinin kurulmasına uygun olup olmadığını,
derleme işlemi için gereken yazılımların sisteminizde kurulu olup olmadığını
denetlemektir. Bu betik ayrıca, bir sonraki adımda gerçekleştireceğimiz inşa
işleminin nasıl yürüyeceğini tarif eden *Makefile* adlı bir dosya da oluşturur.

Bu arada bu komutun başındaki `./` işareti, o anda içinde bulunduğunuz dizinde
yer alan `configure` adlı bir betiği çalıştırmanızı sağlıyor. Eğer yalnızca
``configure`` komutu verirseniz, işletim sistemi bu betiği PATH dizinleri içinde
arayacak ve bulamayacağı için de hata verecektir.

``./configure`` komutu hatasız olarak tamamlandıktan sonra ikinci olarak şu
komutu veriyoruz:: 

    make

Burada aslında ``./configure`` komutu ile oluşan *Makefile* adlı dosyayı `make`
adlı bir program aracılığıyla çalıştırmış oluyoruz. ``make`` bir sistem
komutudur. Bu komutu yukarıdaki gibi parametresiz olarak çalıştırdığımızda
``make`` komutu, o anda içinde bulunduğumuz dizinde bir *Makefile* dosyası arar
ve eğer böyle bir dosya varsa onu çalıştırır. Eğer bir önceki adımda
çalıştırdığımız ``./configure`` komutu başarısız olduysa, dizinde bir *Makefile*
dosyası oluşmayacağı için yukarıdaki ``make`` komutu da çalışmayacaktır. O
yüzden derleme işlemi sırasında verdiğimiz komutların çıktılarını takip edip,
bir sonraki aşamaya geçmeden önce komutun düzgün sonlanıp sonlanmadığından emin
olmamız gerekiyor.

``make`` komutunun yaptığı iş, Python programlama dilinin sisteminize kurulması
esnasında sistemin çeşitli yerlerine kopyalanacak olan dosyaları inşa edip
oluşturmaktır. Bu komutun tamamlanması, kullandığınız bilgisayarın kapasitesine
bağlı olarak biraz uzun sürebilir.

``make`` komutu tamamlandıktan sonra, komut çıktısının son satırlarına doğru
şöyle bir uyarı mesajı görebilirsiniz::

    Python build finished, but the necessary bits 
    to build these modules were not found: [burada 
    eksik olan modül veya modüllerin adları sıralanır]

Burada Python, sistemimizde bazı paketlerin eksik olduğu konusunda bizi
uyarıyor. Uyarı mesajında bir veya daha fazla paketin eksik olduğunu
görebilirsiniz. Eğer öyleyse, eksik olduğu bildirilen bütün paketleri kurmamız
gerekiyor.

Gerekli paketi ya da paketleri kurduktan sonra ``make`` komutunu tekrar
çalıştırıyoruz. Endişe etmeyin, ``make`` komutunu ikinci kez verdiğimizde
komutun tamamlanması birincisi kadar uzun sürmez. Eğer bu komutu ikinci kez
çalıştırdığınızda yukarıdaki uyarı mesajı kaybolduysa şu komutla yolunuza devam
edebilirsiniz::
    
    sudo make altinstall

Daha önce kaynaktan program derlemiş olan GNU/Linux kullanıcılarının eli,
``make`` komutundan sonra ``make install`` komutunu vermeye gitmiş olabilir. Ama
burada bizim ``make install`` yerine ``make altinstall`` komutunu kullandığımıza
dikkat edin. ``make altinstall`` komutu, Python kurulurken klasör ve dosyalara
sürüm numarasının da eklenmesini sağlar. Böylece yeni kurduğunuz Python,
sistemdeki eski Python3 sürümünü silip üzerine yazmamış olur ve iki farklı sürüm
yan yana varolabilir. Eğer ``make altinstall`` yerine ``make install`` komutunu
verirseniz sisteminizde zaten varolan eski bir Python3 sürümüne ait dosya ve
dizinlerin üzerine yazıp silerek o sürümü kullanılamaz hale getirebilirsiniz. Bu
da sistemde beklenmedik problemlerin ortaya çıkmasına yol açabilir. Bu önemli
ayrıntıyı kesinlikle gözden kaçırmamalısınız.

.. seealso:: Python3'ün kaynaktan kurulumu ile ilgili bir tartışma için bkz.
          http://www.istihza.com/forum/viewtopic.php?f=50&t=544

Derleme aşamalarının hiçbirinde herhangi bir hata mesajı almadıysanız kurulum
başarıyla gerçekleşmiş ve sisteminize Python programlama dilinin 3.x sürümü
kurulmuş demektir. 

Yetkisiz Kullanıcı Olarak Kurulum 
---------------------------------

Elbette ``sudo make altinstall`` komutunu verip Python'ı kurabilmek için `root`
haklarına sahip olmanız gerekiyor. Ama eğer kullandığınız sistemde bu haklara
sahip değilseniz Python'ı bu şekilde kuramazsınız. Kısıtlı haklara sahip
olduğunuz bir sistemde Python'ı ancak kendi ev dizininize (``$HOME``)
kurabilirsiniz.

Eğer Python'ı yetkisiz kullanıcı olarak kuracaksanız, öncelikle yukarıda
bahsettiğimiz Python bağımlılıklarının sisteminizde kurulu olup olmadığını
kontrol etmeniz lazım. Kullandığınız sistemde herhangi bir Python sürümü
halihazırda kuruluysa, bu bağımlılıklar da muhtemelen zaten kuruludur. Ama
değilse, bunları kurması için ya sistem yöneticisine ricada bulunacaksınız, ya
da bu bağımlılıkları da tek tek kendi ev dizininize kuracaksınız. Eğer sistem
yöneticisini bu bağımlılıkları kurmaya ikna edemezseniz, internet üzerinden
bulabileceğiniz bilgiler yardımıyla bu bağımlılıkları tek tek elle kendiniz
kurabilirsiniz. Ancak bu işlemin epey zaman alacağını ve süreç sırasında pek çok
başka bağımlılıkla da karşılacağınızı söyleyebilirim. O yüzden ne yapıp edip
sistem yöneticisini bağımlılıkları kurmaya ikna etmenizi tavsiye ederim... Tabii
sistem yöneticisini bu bağımlılıkları kurmaya ikna edebilirseniz, istediğiniz
Python sürümünü de kurmaya ikna edebileceğinizi düşünebiliriz! Ama biz burada
sizin Python'ı kendinizin kuracağını varsayarak yolumuza devam edelim.

Python'ı yetkisiz olarak kurmak, `root` haklarıyla kurmaya çok benzer.
Aralarında yalnızca bir-iki ufak fark vardır. Mesela Python'ı yetkisiz kullanıcı
olarak kurarken, ``./configure`` komutunu şu şekilde vermeniz gerekiyor::

    ./configure --prefix=$HOME/python

Python'ı `root` haklarıyla kurduğunuzda Python `/usr` dizini altına
kurulacaktır. Ancak siz yetkisiz kullanıcı olduğunuz için `/usr` dizinine
herhangi bir şey kuramazsınız. İşte bu yüzden, `configure` betiğine verdiğimiz
`--prefix` parametresi yardımıyla Python'ı, yazma yetkimiz olan bir dizine
kuruyoruz. Mesela yukarıdaki komut Python'ın `/usr` dizinine değil, ev dizininiz
içinde `python` adlı bir klasöre kurulmasını sağlayacaktır. Elbette siz `python`
yerine farklı bir dizin adı da belirleyebilirsiniz. Burada önemli olan nokta,
`--prefix` parametresine vereceğiniz dizin adının, sizin yazmaya yetkili
olduğunuz bir dizin olmasıdır.

Bu komutu çalıştırdıktan sonra ``make`` komutunu normal bir şekilde veriyoruz.
Bunun ardından da ``make install`` (veya duruma göre ``make altinstall``)
komutuyla Python'ı ev dizinimize kuruyoruz. Burada ``make install`` komutunu
``sudo``'suz kullandığımıza dikkat edin. Çünkü, dediğimiz gibi, siz yetkili
kullanıcı olmadığınız için ``sudo`` komutunu kullanamazsınız.

Python'ı bu şekilde ev dizininiz altında bir klasöre kurduğunuzda Python ile
ilgili bütün dosyaların bu klasör içinde yer aldığını göreceksiniz. Bu klasörü
dikkatlice inceleyip neyin nerede olduğuna aşinalık kazanmaya çalışın. Eğer
mümkünse `root` hakları ile kurulmuş bir Python sürümünü inceleyerek, dosyaların
iki farklı kurulum türünde nerelere kopyalandığını karşılaştırın. 

Böylece Python programlama dilini bilgisayarımıza nasıl kuracağımızı öğrenmiş
olduk. Ama bu noktada bir uyarı yapmadan geçmeyelim: Python özellikle bazı
GNU/Linux dağıtımlarında pek çok sistem aracıyla sıkı sıkıya bağlantılıdır. Yani
Python, kullandığınız dağıtımın belkemiği durumunda olabilir. Bu yüzden Python'ı
kaynaktan derlemek bazı riskler taşıyabilir. Eğer yukarıda anlatıldığı şekilde,
kaynaktan Python derleyecekseniz, karşı karşıya olduğunuz risklerin farkında
olmalısınız. Ayrıca GNU/Linux üzerinde kaynaktan program derlemek konusunda
tecrübeli değilseniz ve eğer yukarıdaki açıklamalar size kafa karıştırıcı
geliyorsa, mesela 'Ben bu komutları nereye yazacağım?' diye bir soru geçiyorsa
aklınızdan, kesinlikle dağıtımınızla birlikte gelen Python sürümünü
kullanmalısınız. Python sürümlerini başa baş takip ettiği için, ben size Ubuntu
GNU/Linux'u denemenizi önerebilirim. Ubuntu'nun depolarında Python'ın en yeni
sürümlerini rahatlıkla bulabilirsiniz. Ubuntu'nun resmi sitesine `ubuntu.com
<http://www.ubuntu.com>`_ adresinden, yerel Türkiye sitesine ise
`forum.ubuntu-tr.net <http://forum.ubuntu-tr.net/>`_ adresinden ulaşabilirsiniz.
Eğer şu anda kullandığınız GNU/Linux dağıtımından vazgeçmek istemiyorsanız,
sabit diskinizden küçük bir bölüm ayırıp bu bölüme sadece Python çalışmalarınız
için Ubuntu dağıtımını da kurmayı tercih edebilirsiniz.

Yalnız küçük bir uyarı daha yapalım. Kaynaktan kurulum ile ilgili bu
söylediklerimizden, Python'ın GNU/Linux'a kesinlikle kaynaktan derlenerek
kurulmaması gerektiği anlamı çıkmamalı. Yukarıdaki uyarıların amacı,
kullanıcının Python'ı kaynaktan derlerken sadece biraz daha dikkatli olması
gerektiğini hatırlatmaktır. Örneğin bu satırların yazarı, kullandığı Ubuntu
sisteminde Python3'ü kaynaktan derleyerek kullanmayı tercih ediyor ve herhangi
bir problem yaşamıyor.

Bu önemli uyarıları da yaptığımıza göre gönül rahatlığıyla yolumuza devam
edebiliriz.

Kurduğumuz yeni Python'ı nasıl çalıştıracağımızı biraz sonra göreceğiz. Ama önce
Windows kullanıcılarının Python3'ü nasıl kuracaklarına bakalım.

Windows Kullanıcıları 
**********************

Windows sürümlerinin hiçbirinde Python kurulu olarak gelmez. O yüzden Windows
kullanıcıları, Python'ı sitesinden indirip kuracak. 

Bunun için öncelikle http://www.python.org/downloads adresine gidiyoruz. 
        
Bu adrese gittiğinizde, üzerinde 'Download Python |py3|' ve 'Download |py2|’
yazan, yan yana iki düğme göreceksiniz. Daha önce de söylediğimiz gibi, eğer bir
Python sürüm numarası '2' ile başlıyorsa o sürüm 2.x serisine, yok eğer '3' ile
başlıyorsa 3.x serisine aittir. Dolayısıyla ilk düğme Python3 sürümünü, ikinci
düğme ise Python2 sürümünü içerir.

Biz bu kitapta Python’ın 3.x serisini anlatacağımız için (yeni Python sürümleri
çıktığında o düğmeler üzerinde yazan sürüm numaraları değişecek de olsa), '3'
ile başlayan sürüm numarasını içeren düğmeye tıklamaya özen gösteriyoruz. Bu
düğmeye tıkladığınızda bilgisayarınıza `.exe` uzantılı kurulum dosyası inecek.
Bu dosyaya çift tıklayarak kurulum programını başlatabilirsiniz.

.. note:: Eğer indireceğiniz Python sürümünün mimarisini ve sürümünü kendiniz
 seçmek isterseniz |download| adresinden kendinize uygun olan sürümü bulup
 indirebilirsiniz.

Kurulum dosyasına çift tıkladığınızda karşınıza ilk gelen ekranda, pencerenin
alt tarafında şu kutucukları göreceksiniz:

    #. Install launcher for all users (recommended)
    #. Add Python |major-noformat| to PATH

Burada ilk kutucuk zaten seçilidir. Bunu bu şekilde bırakabilirsiniz. İkinci
kutucuk ise Python’ı yola eklememizi, böylece yalnızca ``python`` komutu vererek
Python'ı başlatabilmemizi sağlayacak. O yüzden oradaki ikinci kutucuğu da
işaretliyoruz.

Aynı pencerenin üst tarafında ise şu seçenekleri göreceksiniz:

    #. -> Install Now
    #. -> Customize Installation

Burada 'Install Now' yazan kısma tıklayarak kurulumu başlatıyoruz.

Eğer Python’ın bilgisayarda nereye kurulacağını ve başka birtakım kurulum
özelliklerini değiştirmek istiyorsanız 'Customize Installation' yazılı kısma
tıklayabilirsiniz. Ben bu kitapta sizin 'Install Now' yazan kısma tıklayarak
kurulum yaptığınızı varsayacağım.

.. note:: Python'ın resmi sitesinde dolaşırken kurulum dosyaları arasında,
 'web-based installer' (web tabanlı kurulum betiği) adlı bir kurulum dosyası
 görebilirsiniz. Bu kurulum dosyası, Python'ın çalışması için gereken dosyaları
 kurulum esnasında internetten indirip kuran, 1MB'dan küçük bir kurulum programı
 içerir. Dolayısıyla eğer kurulumu bu dosyadan yapacaksanız, kesintisiz bir
 internet bağlantısına ihtiyacınız olacak.
 
.. warning:: Eğer Windows'ta Python'ı kurmaya çalışırken hata alıyorsanız,
 muhtemelen işletim sisteminiz güncel değildir. Örneğin Windows 7'de Python
 kurabilmeniz için, SP1 (Service Pack 1) kurulu olmalıdır. Windows
 güncellemelerini kurduktan sonra Python'ı kurmayı tekrar deneyin.
 
Python Kurulum ve Çalışma Dizini
*********************************

Python programlama dilini, kullandığımız işletim sistemine nasıl
kurabileceğimizi bilmek kadar önemli bir konu da Python'ı hangi dizine
kurduğumuzu bilmektir. Zira programcılık maceramız boyunca karşılaşacağımız bazı
sorunlar, Python'ın kurulu olduğu dizine gitmemizi gerektirecek, üstelik kendi
yazdığımız bazı programlarda da Python'ın kurulu olduğu dizinde çeşitli işlemler
yapmak ihtiyacı duyacağız. Ayrıca bazı durumlarda, o anda çalışan Python
sürümünün hangi konumdan çalıştığını tespit etmemiz de gerekebilir.

İşte bu sebeplerden, Python'ın hangi dizine kurulduğunu mutlaka biliyor olmamız
lazım.

Python'ın, işletim sisteminizde hangi dizine kurulduğu, Python'ı nasıl
kurduğunuza bağlı olarak farklılık gösterir.

GNU/Linux dağıtımlarında Python genellikle `/usr/lib/python`\ |major| dizininde
kurulur. Ama elbette, eğer siz Python'ı kaynaktan derlediyseniz, derleme
sırasında `configure` betiğine verdiğiniz `--prefix` parametresi yardımıyla
Python'ın kurulum dizinini kendiniz de belirlemiş olabilirsiniz.

Windows'ta Python programlama dilini aynen bu kitapta gösterdiğimiz şekilde
kurduysanız, Python ``%LOCALAPPDATA%\Programs\Python`` dizini içine
kurulacaktır. Ancak eğer kurulum penceresinde 'Customize Installation' düğmesine
basarak kurulumu özelleştirdiyseniz ve 'Install for all users' seçeneğini
işaretlediyseniz Python `%PROGRAMFILES%` veya `%PROGRAMFILES(x86)` adlı çevre
değişkenlerinin işaret ettiği dizin içine kurulacaktır.
