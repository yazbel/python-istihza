.. meta::
   :description: Bu bölümde paketler konusunu inceleyeceğiz. 
   :keywords: python, paket, import, __init__.py, init, Android, iOS, kivy,
    django, üçüncü şahıs paketleri, standart paketler, bağıl içe aktarma,
    relative import

.. highlight:: py3

***************
Paketler
***************

.. warning:: Bu makale yoğun bir şekilde geliştirilmekte, içeriği sık sık
 güncellenmektedir.

Birkaç bölüm önce, Python'ın belkemiği olduğunu söylediğimiz modüller konusundan
söz etmiştik. Bu bölümde de yine modüllerle bağlantılı bir konuyu ele alacağız.
Konumuz Python'da paketler. 

Paket Nedir?
**************

Öncelikle paketin ne demek olduğunu anlamaya çalışarak başlayalım. Python'da bir
dizin yapısı içinde bir araya getirilen, birbiriyle bağlantılı modüllere paket
adı verilir. Dolayısıyla paketler modüllerden oluşur. 

Python programlama dilinde paketler hem geniş bir yer tutar, hem de büyük bir
önem taşır. Hatta Python'ı bilmenin paketleri bilmek demek olduğunu söylersek
çok da abartmış olmayız. Mesela Python'la web programları yazmak için kullanılan
en gözde araçlardan biri olan `django` web çatısı, aslında birtakım üçüncü şahıs
modüllerinin bir paket yapısı içinde bir araya getirilmiş halinden başka bir şey
değildir. Aynı şekilde Python'la Android ve iOS üzerinde çalışabilecek
programlar yazmak isterseniz `kivy` adlı bir başka Python paketini öğrenmeniz
gerekir. Python programlama dilini kullanarak grafik arayüzlü yazılımlar
geliştirmemizi sağlayan `tkinter` ise standart kütüphanede bulunan pek çok
paketten yalnızca bir tanesidir.

Etrafta `django`, `kivy` ve `tkinter` gibi pek çok kullanışlı paket
bulabilirsiniz. Mesela standart kütüphanede bulunan `sqlite3`, Sqlite
veritabanları üzerinde çalışmamıza imkan tanıyan çeşitli modülleri içinde
barındıran bir Python paketidir. Yine standart kütüphanede bulunan `urllib`
paketi yardımıyla internet adresleri (URL'ler) üzerinde çeşitli işlemler
yapabilirsiniz. Python kurulum dizini içindeki `Lib` klasörü altında pek çok
standart Python paketi görebilirsiniz.

Peki modüllerle paketleri birbirinden ayıran şey nedir?

Öncelikle, paketler modüllere kıyasla çok daha kapsamlı bir yapıdır. Zira bir
paket içinde (genellikle) birden fazla modül bulunur. Örneğin standart
kütüphanede bulunan ve tek bir `os.py` dosyasından oluşan `os` bir modülken,
içinde pek çok farklı modülü barındıran `collections` bir pakettir. Tek bir
dosyadan oluştuğu ve bir dizin yapısı içinde yer almadığı için bir modülden içe
aktarma işlemi gerçekleştirmek son derece kolaydır. Paketlerden içe aktarma
yaparken uymamız gereken kurallar ise haliyle biraz daha karmaşıktır.

İkincisi, bütün paketler aynı zamanda birer modüldür, ancak bütün modüller birer
paket değildir. Örneğin `venv` paketinden bahsederken '`venv` modülü' demek
yanlış olmaz. Ancak `os` modülünden bahsederken '`os` paketi' demek biraz abes
kaçacaktır.

Üçüncüsü, paketlerin `__path__` adlı özel bir niteliği bulunur. Modüllerde ise
bu nitelik bulunmaz. Örneğin::
    
    >>> import os
    >>> os.__path__

    AttributeError: 'module' object has no attribute '__path__'

`os` bir modül olduğu için, ``__path__`` niteliğine sahip değildir. Bir de
`json` paketine bakalım::
    
    >>> import json
    >>> json.__path__
    
`json` ise bir paket olduğu için, ``__path__`` niteliğine sahiptir. Birazdan
bu niteliğin ne işe yaradığını anlatacağız. Ama ondan önce öğrenmeniz gereken
başka şeyler var.

Paket Türleri
**************

Tıpkı fonksiyonlarda ve modüllerde olduğu gibi, paketlerin de türleri vardır.
Paketleri, kaynaklarına göre ikiye ayırabiliriz:

    * Standart Paketler
    * Üçüncü Şahıs Paketleri
    
Bu türlerin ne anlama geldiğini isimlerine bakarak rahatlıkla anlayabiliyoruz.
Ama gelin isterseniz bunları kısaca gözden geçirelim.

Öncelikle standart paketlerden başlayalım.

Standart Paketler
==================

Standart paketler, Python'ın standart kütüphanesinde bulunan paketlerdir. Tıpkı
gömülü fonksiyonlar ve standart modüller gibi, standart paketler de dilin bir
parçası olduklarından, bunlara erişebilmek için herhangi bir ek yazılım indirip
kurmamıza gerek kalmaz; bu paketler her an emrimize amadedir. Standart paketlere
Python kurulum dizini içindeki `Lib` klasöründen erişebilirsiniz. Bir standart
paketin tam olarak hangi konumda bulunduğunu öğrenmek için ise ilgili paketin
``__path__`` niteliğini sorgulayabilirsiniz::
    
    >>> import urllib
    >>> urllib.__path__
    
Eğer sorguladığınız şeyin bir ``__path__`` niteliği yoksa, paket sandığınız o
şey, aslında bir paket değildir. Örneğin::
    
    >>> import subprocess
    >>> subprocess.__path__
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute '__path__'    
    
Çünkü, bildiğiniz gibi, paketlerin aksine, modüllerin ``__path__`` adlı bir
niteliği bulunmaz. `subprocess` de bir paket değil, modül olduğu için
`__path__` sorgusu hata verecektir.

Bir paketin ``__path__`` niteliğini sorguladığınızda çıktıda hangi dizini
görüyorsanız, o paketin bilgisayardaki konumu odur. Mesela yukarıda adını
andığımız `urllib` paketinin ``__path__`` niteliğini sorgulayıp, karşımıza çıkan
klasöre gidelim. Paket dizininin içini açtığımızda karşımıza şu dosyalar
çıkacak::
    
    error.py
    parse.py
    request.py
    response.py
    robotparser.py
    __init__.py
    
Daha önce de dediğimiz gibi, paketler modüllerden oluşur. İşte `urllib` paketi
de yukarıda ismini gördüğümüz modüllerin birleşiminden oluşuyor. Python kurulum
dizini içindeki `Lib` klasörü altında yer alan paketleri inceleyerek, hangi
paketin hangi modüllerden oluştuğunu kendiniz de görebilirsiniz.
    
Üçüncü Şahıs Paketleri
=======================

Python'da standart paketlerin dışında bir de üçüncü şahıs paketleri vardır.
Bunlar Python geliştiricileri haricindeki kişilerce yazılıp kullanımımıza
sunulmuş araçlardır. Bu paketler, standart paketlerin aksine dilin bir parçası
olmadığından, bu paketleri kullanabilmek için öncelikle bunları bilgisayarımıza
kurmamız gerekir. Mesela `django`, `kivy` ve ilk derslerimizden birinde
bahsettiğimiz `cx_freeze` birer üçüncü şahıs paketidir.

Peki bu üçüncü şahıs paketlerini nereden bulabiliriz?

Hatırlarsanız Modüller konusunu işlerken 'Üçüncü Şahıs Modüllerinden' de söz
etmiştik. Üçüncü şahıs modüllerini bulabileceğimiz başlıca kaynağın
https://pypi.python.org/pypi adresi olduğunu ve buradan 60.000'in üzerinde
üçüncü şahıs Python modülüne ulaşabileceğimizi de ifade etmiştik. İşte orada
bahsettiğimiz üçüncü şahıs modülleri, aslında birer pakettir. Zira üçüncü şahıs
modülleri çoğunlukla birer paket biçiminde sunulur. Dolayısıyla üçüncü şahıs
modüllerine nereden ve nasıl ulaşıyorsak, üçüncü şahıs paketlerine de aynı
yerden ve aynı şekilde ulaşabiliriz. Ayrıca bir üçüncü şahıs paketini kurmadan
önce, ilgili paketin yardım dosyalarını veya websitesini incelemekte de fayda
var. Çünkü bazı üçüncü şahıs modüllerini kurabilmek için birtakım özel
gereksinimleri yerine getirmeniz gerekiyor olabilir. Bu tür bilgilere de ancak
ilgili paketi geliştiren kişi veya ekibin websitesinden ulaşabilirsiniz.

Bir üçüncü şahıs paketinin https://pypi.python.org/pypi adresindeki adını
öğrendikten sonra, bu paketi şu komutla kurabilirsiniz::
    
    pip3 install paket_adı
    
Mesela `restructuredText` biçimli metin dosyalarından şık ve kullanışlı
belgeler üretmemizi sağlayan `sphinx` paketi PyPI sitesinde bulunuyor.
Dolayısıyla bu paketi kurmak için şu komutu verebiliriz::
    
    pip3 install sphinx
    
Elbette, eğer bir GNU/Linux dağıtımı kullanıyorsanız, bu komutu root haklarıyla
çalıştırmanız gerektiğini söylememe herhalde gerek yok::
    
    sudo pip3 install sphinx

`pip3` adlı yazılım, `sphinx` paketinin bütün dosyalarını PyPI sitesinden çekip
otomatik olarak bilgisayarımıza kuracaktır. 

Bir üçüncü şahıs paketini ``pip3`` komutuyla kurmak yerine elle kurmayı da
tercih edebilirsiniz. Örnek olarak bu defa `django` paketini alalım. Bu paketin
en son sürümünü https://github.com/django/django/archive/master.tar.gz
adresinden indirebilirsiniz. Ayrıca arzu ederseniz https://www.djangoproject.com
adresine uğrayarak bu modülün resmi websitesine de gözatabilirsiniz.

İndirdiğiniz `tar.gz` uzantılı sıkıştırılmış dosyayı açtığınızda karşısınıza pek
çok dizin ve bu dizinlerin içinde de pek çok Python dosyası çıkacak. Django,
geniş kapsamlı üçüncü şahıs paketlerine güzel bir örnektir. 

Django paketini açıp `django-master` adlı dizinin içine girdiğinizde, orada
`setup.py` adlı bir dosya göreceksiniz. İşte ``pip3`` komutu yerine, bu dosyayı
kullanarak da bu paketi bilgisayarımıza kurabiliriz. 

Dikkatlice bakın::
    
    python3 setup.py install

Bu komutta iki önemli unsur var. Birincisi, komutu çalıştırdığımız Python
sürümü. Unutmayın, bir Python paketini hangi Python sürümü ile kurarsanız, o
paketi o sürüm ile kullanabilirsiniz. Ben yukarıdaki komutta, sizin Python
sürümünüzü başlatan komutun ``python3`` olduğunu varsaydım. Eğer siz Python'ı
başlatmak için veya başka Python programlarını çalıştırmak için farklı bir komut
kullanıyorsanız, `setup.py` dosyasını da o komutla çalıştıracaksınız. Neticede
`setup.py` de sıradan bir Python programıdır. Bu programı `install` parametresi
ile birlikte çalıştırarak Django paketini sisteminize kurmuş oluyorsunuz.
Kurulum tamamlandıktan sonra, kurulumun başarılı olup olmadığını test etmek için
Python komut satırında şu komutu verin::
    
    >>> import django
    
Eğer herhangi bir çıktı verilmeden alt satıra geçildiyse, bir üçüncü şahıs
paketi olan `django`'yu bilgisayarınıza başarıyla kurmuşsunuz demektir. Bu
üçüncü şahıs modülünü nasıl kullanacağınızı öğrenmek için internet üzerindeki
sayısız makaleden ve kitaptan yararlanabilirsiniz.

Paketlerin İçe Aktarılması
****************************

Modüllerle paketler arasındaki önemli bir fark, paketlerin modüllere kıyasla
daha karmaşık bir yapıda olmasıdır. Yalnızca tek bir dosyadan oluşan modüllerin
bu basit yapısından ötürü, bir modülden nitelik veya metot içe aktarmak çok
kolaydır. Mesela bir modül olan `os`'u şu şekilde içe aktarabiliriz::
    
    >>> import os
    
Eğer `os` modülünden `name` niteliğini almak istersek şu komutu kullanabiliriz::
    
    >>> from os import name
    
`os` modülü içindeki bütün nitelik ve metotları içe aktarmak istediğimizde
yıldızlı içe aktarma yönteminden yararlanabiliriz::
    
    >>> from os import *
    
Veya bu modül içindeki bir niteliği veya metodu başka bir isim altında da içe
aktarabiliriz::
    
    >>> from os import execv as exe
    
Gelelim paketlere...

import paket
==============

Mesela `urllib` paketini ele alalım. Tıpkı `os` modülünde yaptığımız gibi,
`urllib` modülünü de şu şekilde içe aktarabiliriz::
    
    >>> import urllib
    
Ancak `os` modülünün aksine, `urllib` paketini içe aktardığımızda mevcut isim
alanına herhangi bir nitelik veya metot otomatik olarak aktarılmaz. Örneğin `os`
modülünü içe aktardığımızda bu modülün içeriğinin, `os` öneki altında mevcut
isim alanına döküldüğünü biliyoruz::
    
    >>> dir(os)
    
Gördüğünüz gibi, modül içeriği kullanılabilir durumda. Listedeki nitelik ve
metotlara `os` öneki ile erişebiliriz::
    
    >>> os.name
    >>> os.listdir(os.getcwd())
  
gibi...

Ancak ``import os`` komutunun aksine, ``import urllib`` komutu, paket içeriğini
otomatik olarak mevcut isim alanına aktarmaz::
    
    >>> import urllib
    >>> dir(urllib)

    ['__builtins__', '__cached__', '__doc__', '__file__', 
     '__loader__', '__name__', '__package__', '__path__', 
     '__spec__']
     
Gördüğünüz gibi listede yalnızca standart metot ve nitelikler var. Bu listede
mesela paket içeriğinde olduğunu bildiğimiz `error.py`, `parse.py`,
`request.py`, `response.py` ve `robotparser.py` gibi modülleri göremiyoruz. Eğer
paket içinde bulunan belirli bir modülü içe aktarmak istiyorsak bunu açık açık
belirtmeliyiz. Nasıl mı? Görelim...

import paket.modül
======================

Mesela `urllib` paketinden `request` modülünü içe aktarmak
istersek şu komutu yazacağız::
    
    >>> import urllib.request
    
Bu modülü yukarıdaki şekilde içe aktardığımızda, modül içindeki nitelik ve
metotlara `urllib.request` önekiyle erişebiliriz::
    
    >>> urllib.request.urlopen('http://www.istihza.com')
        
from paket import modül
========================
    
Yukarıda olduğu gibi, `urllib` paketi içindeki `request` modülünü ``import
paket.modül`` gibi bir komutla içe aktardığımızda ilgili modülün bütün nitelik
ve metotları `urllib.request` ismi altında içe aktarıldığından, `urllib` paketi
içindeki `request` modülünün nitelik ve metotlarına ulaşabilmek için her
defasında `urllib.request` önekini kullanmamız gerekir. Eğer her defasında uzun
uzun `urllib.request` yazmak istemiyorsanız paket içindeki modülü şu şekilde içe
aktarabilirsiniz::
    
    >>> from urllib import request
    
Böylece `request` modülünün nitelik ve metotlarına yalnızca `request` önekiyle
erişebilirsiniz::
    
    >>> request.urlopen('http://www.istihza.com')
        
from paket.modül import nitelik_veya_metot
=============================================

Peki bir paket içinde yer alan herhangi bir modül içindeki nitelik ve metotlara
öneksiz olarak erişmek istersek ne yapacağız? Python bize bu isteğimizi yerine
getirmemizi sağlayacak bir yol da sunar. 

Dikkatlice bakın::
    
    from urllib.request import urlopen
    
Bu şekilde `urllib` paketi içindeki `request` modülünden `urlopen` adlı metodu
doğrudan içe aktarmış olduk. Dolayısıyla bu metodu dümdüz kullanabiliriz::
    
    >>> urlopen('http://www.istihza.com')
    
Ancak, modüller konusunu işlerken öneksiz aktarmaya ilişkin söylediklerimizin
paketler için de geçerli olduğunu aklımızdan çıkarmıyoruz.

from paket.modül import *
==========================

Eğer bir paket içindeki bir modülün bütün nitelik ve metotlarını mevcut isim
alanına olduğu gibi aktarmak isterseniz şu içe aktarma yöntemini
kullanabilirsiniz::
    
    >>> from paket.modül import *
    
Bu bilgiyi `urllib` modülüne uygulayalım::
    
    >>> from urllib.request import *
    
Bu şekilde `urllib` paketi içindeki `request` modülünün bütün nitelik ve
metotlarını doğrudan mevcut isim alanına aktarmış olduk. Bu yöntemin büyük bir
rahatlık sunmakla birlikte önemli dezavantajlara da sahip olduğunu gayet iyi
bildiğinizden eminim.

Kendi Oluşturduğumuz Paketler
*******************************

Buraya kadar hep başkalarının yazdığı, hazır paketlerden söz ettik. Bu sayede
bir Python paketinin yapı olarak neye benzediğini ve nasıl kullanılacağını
kabataslak da olsa anlamış olduk. Elbette biz sadece başkalarının yazdığı
paketleri kullanmayacağız. Bir de bizim kendi yazdığımız Python paketleri
olacak.

Kendi oluşturduğumuz paketler, adı üzerinde, kendi kendimize yazıp meydana
getirdiğimiz paketlerdir. Bu paketleri iyice geliştirdikten ve başkaları için de
yararlı olabilecek hale getirdikten sonra, istersek https://pypi.python.org/pypi
adresindeki üçüncü şahıs paket deposuna yükleyebiliriz. Böylece kendi
geliştirdiğimiz paketler de, üçüncü şahıs Python paketleri arasına girmiş
olur...

İşte bu bölümde, bu tür paketleri nasıl yazacağımızı ele alacağız.

Paket Oluşturmak
=================

Bir Python programı yazdığınızı düşünün. Programınızı ilk yazmaya başlarken
doğal olarak programınız tek bir dosyadan oluşacaktır. Ancak elbette programınız
büyüdükçe, bütün kodları tek bir dosyaya sıkıştırmak yerine, farklı işlevleri
farklı dosyalar içinde tanımlamanın daha mantıklı olduğunu farkedeceksiniz.
Mesela programın grafik arayüz kısmını bir dosyada tanımlarken, düğmelere,
menülere bağlayacağınız işlevleri bir başka dosyada tanımlamak isteyebilirsiniz.
Programınızın gerçekleştirdiği işlemleri küçük, mantıklı birimlere bölüp bunları
farklı modüllere taşımanız, programınızı çok daha rahat bir şekilde idare
etmenizi sağlayacaktır. Yani, yazdığınız programı birkaç modüle bölüp, bunları
bir paket yapısı içinde sunmanız hem kendiniz açısından, hem de kodlarınızı
okuyan başkaları açısından işleri epey kolaylaştıracaktır.

Python'da bir paket oluşturmak son derece kolaydır. Program kodlarını içeren
`.py` dosyasını bir klasör içine koyduğunuz anda, o klasörün adını taşıyan bir
paket meydana getirmiş olursunuz. 

Mesela bir sipariş takip programı yazdığımızı düşünelim. Ana klasörümüzün adını
`siparistakip` koyalım. Bu klasör içinde de `komut.py`, `veritabani.py` ve
`siparis.py` adlı modüller olsun. Yani şöyle bir dosya-dizin yapısı
oluşturalım::
    
    + siparistakip
    |__ siparis.py
    |__ komut.py
    |__ veritabani.py
    
İşte bu şekilde basit bir dosya-dizin yapısı oluşturduğumuzda, `siparistakip`
adlı bir Python paketi meydana getirmiş oluyoruz\ [#]_.

Gelin isterseniz, `siparistakip` dizininin gerçekten bir paket olduğunu teyit
edelim.

Öncelikle paketimizi içe aktaralım. Bunun için `siparistakip` dizininin
bulunduğu klasörde şu komutu verelim::
    
    >>> import siparistakip
    
Şimdi paket içeriğini kontrol edelim::
    
    >>> dir(siparistakip)
    
    ['__doc__', '__loader__', '__name__', 
     '__package__', '__path__', '__spec__']
     
Gördüğünüz gibi, listede `__path__` adlı bir nitelik var. Bu niteliğin yalnızca
paketlerde bulunduğunu biliyorsunuz. Demek ki `siparistakip` gerçekten de bir
Python paketiymiş. Bunun dışında, listede gördüğünüz `__package__` niteliğini
kullanarak da bir modülün paket olup olmadığını kontrol edebilirsiniz::
    
    >>> siparistakip.__package__
    
    'siparistakip'
    
Eğer test ettiğimiz modül bir paketse, `__package__` niteliği bize bir paket adı
verecektir. Yok eğer test ettiğimiz modül bir paket değil de alelade bir
modülse, `__package__` niteliği boş bir karakter dizisi döndürecektir. Mesela
`os` modülünün bir paket olmadığını biliyoruz::
    
    >>> import os
    >>> os.__package__
    
    ''
    
Gördüğünüz gibi, bu modülün `__package__` niteliği boş bir karakter dizisi.
Ayrıca bu modül bir paket olmadığı için, `__path__` adlı bir nitelik de
barındırmıyor::
    
    >>> os.__path__
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute '__path__'
    
Dolayısıyla bütün işaretler, gerçekten de `siparistakip` adlı bir paket
oluşturduğumuzu gösteriyor...

İçe Aktarma İşlemleri
=====================

Standart paketleri anlatırken, bu paketlerin her konumdan içe aktarılabileceğini
söylemiştik. Aynı şey üçüncü şahıs paketleri için de geçerlidir. Çünkü gerek
Python geliştiricileri, gerekse üçüncü şahıs paketleri geliştirenler, bu
paketleri bize sunarken bunları Python'ın `sys.path` çıktısına eklemişlerdir. O
yüzden standart ve üçüncü şahıs paketlerini içe aktarırken sorun yaşamayız. 

Ancak tabii ki kendi yazdığımız paketler `sys.path` listesine ekli olmadığı
için, bunları içe aktarırken bazı noktalara dikkat etmeniz gerekir. 

Mesela masaüstünde şu yapıya sahip bir paket oluşturalım::

    + paket
    |__ modul1.py
    |__ modul2.py
    |__ modul3.py
        + altdizin
        |__altmodul1.py
        |__altmodul2.py
        
Bu dizinde dosya içerikleri şöyle olsun:

`modul1.py`::
    
    isim1 = 'modul1'
    print(isim1)

`modul2.py`::
    
    isim2 = 'modul2'
    print(isim2)
    
`modul3.py`::
    
    isim3 = 'modul3'
    print(isim3)
    
`altmodul1.py`::
    
    altisim1 = 'altmodul1'
    print(altisim1)
    
`altmodul2.py`::
        
    altisim2 = 'altmodul2'
    print(altisim2)
    
Şimdi `paket` adlı dizinin bulunduğu klasörde bir etkileşimli kabuk oturumu
açalım. Yalnız bu oturumu `paket` dizinin içinde değil, bir üst dizinde
açacaksınız. Yani o anda bulunduğunuz dizinde `dir` veya `ls` komutu
verdiğinizde `paket` adlı dizini görüyor olmanız lazım... Eğer `dir` veya `ls`
komutunun çıktısında `altdizin` adlı dizini görüyorsanız yanlış yerdesiniz
demektir. Hemen bir üst dizine gidin.

Bulunduğumuz konumda şu komutu verelim::
    
    >>> import paket
    
Eğer hiçbir çıktı almadan bir alt satıra geçtiyseniz her şey yolunda demektir.
Eğer bir hata mesajı görüyorsanız, etkileşimli kabuk oturumunu yanlış konumda
açmışsınızdır. Oturumu doğru konumda açıp tekrar gelin...

Standart paketlerde ve üçüncü şahıs paketlerinde gördüğümüz gibi, bir paketi
yukarıdaki şekilde içe aktardığımızda, o pakete ait herhangi bir modül veya
nitelik otomatik olarak içe aktarılmıyor. ``dir(paket)`` komutu verdiğinizde
yalnızca standart niteliklerin içe aktarıldığını göreceksiniz::
    
    >>> dir(paket)
    
    ['__doc__', '__loader__', '__name__', 
     '__package__', '__path__', '__spec__']
    
Gördüğünüz gibi, oluşturduğumuz paket, bir Python paketinin sahip olması gereken
bütün niteliklere sahip.

Şimdi bu paket içindeki `modul1` adlı modülü içe aktaralım::
    
    >>> from paket import modul1
    
    modul1
    
Böylece `modul1` adlı modülün içindeki değişkenin değerini almış olduk. Paket
içindeki öteki modülleri de aynı şekilde içe aktarabilirsiniz::
    
    >>> from paket import modul2
    
    modul2
    
    >>> from paket import modul3
    
    modul3
    
Peki ya mesela `modul1` içindeki `isim1` değişkenini almak istersek ne
yapacağız?

Dikkatlice bakın::
    
    >>> from paket.modul1 import isim1
    
    modul1
    
Gördüğünüz gibi, `paket` içindeki `modul1` modülünün `isim1` niteliğini
başarıyla aldık. Örnek olması açısından ötekileri de alalım::
    
    >>> from paket.modul2 import isim2
    
    modul2
    
    >>> from paket.modul3 import isim3
    
    modul3
    
Buradaki temel mantığı kavradığınızı zannediyorum. Standart modülleri incelerken
bahsettiğimiz içe aktarma yöntemlerini tek tek yukarıdaki yapıya uygulayarak,
buraya kadar anlattıklarımızı anlayıp anlamadığınızı test edebilirsiniz.
Dilerseniz pratik yapmak açısından bir de `altdizin` içindeki modüllere
uzanalım.

Öncelikle `altdizin`'i içe aktaralım::
        
    >>> import paket.altdizin
    
Bu şekilde `paket` adlı paketin `altdizin` adlı alt dizinini içe aktarmış olduk.
Artık bu alt dizin içindeki modüllere ve onların niteliklerine erişebiliriz.
Mesela `paket` adlı paketin `altdizin` adlı alt dizini içindeki `altmodul1` adlı
modülün `altisim1` niteliğini alalım::
    
    >>> paket.altdizin.altmodul1.altisim1
    
    'altmodul1'
    
Gördüğünüz gibi, `altisim1` niteliğine erişmek için uzun bir yol gitmemiz
gerekiyor. Bu yolu kısaltmak isterseniz modülü şu şekilde içe aktarabilirsiniz::

    >>> from paket.altdizin import altmodul1
    
Artık `altmodul1`'in niteliklerine yalnızca `altmodul1` önekiyle
ulaşabilirsiniz:: 

    >>> altmodul1.altisim1
    
    'altmodul1'   

Hatta doğrudan `altisim1` niteliğinin kendisini de alabilirsiniz::
    
    >>> from paket.altdizin.altmodul1 import altisim1
    >>> altisim1
    
    'altmodul1'
    
Gördüğünüz gibi, Python'ın içe aktarma mantığı gayet basit. Bulunduğunuz
konumdan itibaren, alt dizin ve modül adlarını sırasıyla kullanarak ve bunları
birbiriyle nokta işareti ile birleştirerek her bir modüle ve modül içindeki
niteliğe erişebiliyoruz.

İçe Aktarma Mantığı
=======================

Yukarıdaki örneklerden gördüğünüz gibi, Python'ın içe aktarma mekanizması gayet
basit bir şekilde işliyor. Ancak yine de bu durum sizin rehavete kapılmanıza yol
açmasın. Zira kimi zaman bu mekanizma hiç beklemediğiniz durumların ortaya
çıkmasına da yol açabilir. 

Python'da paketler üzerinde çalışırken, Python programlama dilinin paketleri içe
aktarma mekanizmasını çok iyi anlamış olmalısınız. Eğer bu mekanizmayı hakkıyla
anlamadan paket yapmaya kalkışırsanız, Python'ın içe aktarma sırasında
verebileceği sürpriz hatalar size saç baş yoldurabilir. İşte bu bölümde
Python'ın paket içe aktarma mantığı üzerine eğilerek, engebeli yüzeyleri nasıl
aşabileceğimizi anlamaya çalışacağız.

İçe Aktarma İşleminin Konumu
-------------------------------

Python'da herhangi bir içe aktarma işlemi yapacağımız zaman, unutmamamız gereken
en önemli konu, Python'ın bütün içe aktarma işlemlerini tek bir konumdan
gerçekleştirdiği gerçeğidir. Bunun ne demek olduğunu anlamak için çok basit bir
örnek verelim. 

Yukarıda şöyle bir paket yapısı oluşturmuştuk::

    + paket
    |__ modul1.py
    |__ modul2.py
    |__ modul3.py
        + altdizin
        |__altmodul1.py
        |__altmodul2.py
        
Burada `altmodul2.py` dosyasının içine şunu yazalım::
    
    import altmodul1
    
Yani bu dosya ile aynı dizinde bulunan `altmodul1.py` dosyasını, `altmodul2.py`
dosyası içinden bir modül olarak içe aktaralım.

Şimdi, daha önce yaptığımız gibi, `paket` adlı dizinin bulunduğu klasörde bir
etkileşimli kabuk oturumu açalım ve şu komutu yazalım::
    
    >>> from paket.altdizin import altmodul2
    
Bu komut bize şöyle bir hata mesajı verecek::
    
    ImportError: No module named 'altmodul1'
    
Bu hatanın sebebi, Python'ın `altmodul1` adlı modülü bulamıyor olmasıdır.
Halbuki bu modül, `altmodul2` ile aynı dizinde bulunuyor. O halde acaba Python
bu modülü neden bulamıyor?

Bunu anlamak için şöyle bir deneme yapalım:

Şimdi `altmodul1.py` ve `altmodul2.py` dosyalarının bulunduğu konumda bir
etkileşimli kabuk oturumu başlatın ve şu komutu verin::
    
    >>> import altmodul2
    
Gördüğünüz gibi, bu defa Python herhangi bir hata mesajı vermeden, ``impport
altmodul1`` komutuyla `altmodul2.py` dosyası içinden çağırdığımız `altmodul1`
modülünün içeriğini alabildi. Peki ama neden?

Başta da söylediğimiz gibi, Python bütün aktarma işlemlerini tek bir konumdan
yapar. Yani eğer siz bir modülü üst dizinden içe aktardıysanız, o üst dizinin
adı paket içindeki bütün aktarmalara önek olarak eklenecektir. Dolayısıyla
`paket` adlı dizinin bulunduğu konumdan `altdizin` içindeki `altmodul2.py`
dosyasını çağırdığınızda, `altmodul2.py` içindeki ``import altmodul1`` komutu,
`altmodul1.py` dosyasını bulamayacaktır. Ama siz `altmodul2.py` dosyasını kendi
dizini içinden çağırdığınızda, ``import altmodul1`` komutu, aynı dizin içindeki
`altmodul1.py` dosyasını bulabilecektir.

Bu okuduklarınız ilk bakışta size çok karmaşıkmış gibi gelebilir, ama aslında
biraz dikkat ederseniz bu sistemin hiç de öyle karmaşık olmadığını, aksine son
derece mantıklı olduğunu göreceksiniz.

Durumu daha da netleştirmek için şöyle bir şey yapalım:

`altmodul2.py` dosyasını açıp, ``import altmodul1`` komutunu şöyle yazalım::
    
    from paket.altdizin import altmodul1
    
Bu değişikliği kaydettikten sonra tekrar `paket` dizininin bulunduğu konumda bir
oturum açıp şu komutu verelim::
    
    >>> from paket.altdizin import altmodul2

İşte bu kez komutumuz başarıyla çalıştı ve `altmodul1` modülünü bulabildi...    

Şimdi de `altmodul1.py` ve `altmodul2.py` dosyalarının bulunduğu konuma tekrar
dönüp burada yine bir etkileşimli kabuk oturumu başlatalım ve daha önce
verdiğimiz şu komutu tekrar verelim::
    
    >>> import altmodul2
    
O da ne! Geçen sefer hatasız çalışan kod bu defa hata verdi::
    
    ImportError: No module named 'paket'
    
Gördüğünüz gibi, modülü içe aktardığımız konumdan ötürü Python bu kez de
`paket` adlı paketi bulamıyor.

Birazdan bütün bu sorunların kesin çözümünü vereceğiz. Ama ondan önce başka bir
konudan söz edelim.
    
Bağıl İçe Aktarma
------------------

Dediğimiz gibi, bir içe aktarma işleminin başarılı olabilmesi, o içe aktarma
işleminin yapıldığı konumun neresi olduğuna ve paket içinde bulunan öteki
modüllerdeki içe aktarmaların nasıl yazıldığına bağlıdır. Yani mesela normalde
aynı konumda bulunan iki modül birbirini yalnızca ``import modül_adı`` gibi bir
komutla içe aktarabilecekken, eğer bu modüller üst dizinin bulunduğu konumdan
çağrılıyorsa, içe aktarma başarısız olabilir. Bunun bir örneğini yukarıda
görmüştük. `altdizin` içinde bulunan `altmodul1.py` dosyasını, aynı dizindeki
`altmodul2.py` dosyasından içe aktarmak için `altmodul2.py` dosyasına ``import
altmodul1`` yazdığımızda, ana `paket` dizininin bulunduğu konumdan `altdizin`
içindeki `altmodul2.py` dosyasını ``from paket.altdizin import altmodul2`` gibi
bir komut ile içe aktarma girişimimiz başarısızlığa uğruyordu. Python'ın ilgili
modülü bulabilmesini sağlamak için, `altmodul2.py` dosyasına ``import
altmodul1`` yazmak yerine ``from paket.altdizin import altmodul1`` yazmıştık.
İşte aynı şeyi 'bağıl içe aktarma' (*relative import*) denen bir mekanizma
yardımıyla da gerçekleştirebiliriz.

Bu mekanizmada içe aktarma işlemi, içe aktaran modülün bulunduğu konuma göre
gerçekleşir. Bir örnek verelim...

`altmodul2.py` dosyasına ``import altmodul1`` veya ``from paket.altdizin import
altmodul1`` yerine şunu yazalım::
    
    from . import altmodul1
    
Burada `from` kelimesinden sonra gelen nokta (`.`), içe aktaran modülle aynı
dizine atıfta bulunuyor. Yani bu şekilde `altmodul2.py`'nin bulunduğu dizine
atıfta bulunmuş, böylece bu dizinde bulunan `altmodul1` adlı modülü içe
aktarabilmiş olduk. `paket` dizininden, hatta `altdizin` dizininden yapılacak
içe aktarma işlemleri bu komut sayesinde başarılı olacaktır.

Dediğimiz gibi, orada `.` işareti, içe aktaran modülle aynı dizini temsil
ediyor. Eğer oraya yan yana iki nokta (`..`) koyacak olursanız, bir üst dizine
atıfta bulunabilirsiniz. Mesela bir üst dizinde bulunan `modul3.py` dosyasını
`altmodul2.py` veya `altmodul1.py` dosyasından içe aktarmak isterseniz, bu
dosyaların herhangi birine şu kodu yazabilirsiniz::
    
    from .. import modul3
    
Üç nokta yan yana koyduğunuzda ise (`...`) iki üst dizine atıfta bulunmuş
olursunuz. Ancak bu şekilde paketin dışına çıkamayacağınızı da unutmayın. Yani
mesela `paket` dizininin bulunduğu konuma göre bir üst dizinde bulunan, yani
paket dışındaki `falanca.py` adlı bir modülü şu şekilde içe aktaramazsınız::
    
    from ... import falanca
    
Ama tabii eğer paketinizin dizin yapısı iki üst dizine çıkılmasına müsaade
ediyorsa yukarıdaki komut çalışacaktır. Yani elinizdeki, aşağıdakine benzer
yapıda bir pakette::

    + paket
    |__ modul1.py
    |__ modul2.py
    |__ modul3.py
        + altdizin
        |__altmodul1.py
        |__altmodul2.py
            + altaltdizin
            |__altaltmodul1.py
            |__altaltmodul2.py
            
`altaltmodul1.py` dosyasının bulunduğu konumdan itibaren iki üst dizine çıkarak
`modul2.py` dosyasını içe aktarabilirsiniz::
    
    from ... import modul2
    
Yukarıda gösterdiğimiz bağıl içe aktarma mekanizması, paket adı belirtmeden içe
aktarma işlemi gerçekleştirmenizi sağlar. Yani bu mekanizma sayesinde ``from
paketadi.modul import altmodul`` yerine ``from . import modul`` gibi bir kod
yazarak, aynı dizin içinde veya üst dizinlerde bulunan modüllere atıfta
bulunabilirsiniz.

Paketlerin Yola Eklenmesi
=============================

Daha önce de birkaç kez vurguladığımız gibi, içe aktarma işlemlerinde Python
aradığımız modülü veya paketi bulabilmek için `sys.path` adlı listede görünen
dizinlerin içine bakar. Eğer içe aktarmak istediğiniz paket dizini bu listede
değilse, o paketi içe aktarabilmek için, komut satırını o dizinin bulunduğu
klasörde açmanız gerekir. Yani standart paketler ve üçüncü şahıs paketlerin
aksine, `sys.path`'e eklenmemiş bir paketi her yerden içe aktaramazsınız. 

Peki bir paketi `sys.path` listesine nasıl ekleyeceğiz?

Aslında bu sorunun cevabı çok basit. Bildiğiniz gibi, `sys.path` aslında basit
bir listeden ibarettir. Dolayısıyla listeler üzerinde nasıl değişiklik
yapıyorsanız, `sys.path` üzerinde de o şekilde değişiklik yapacaksınız.

Gelin isterseniz, yukarıda oluşturduğumuz `paket` adlı paket üzerinden bir
uygulama yapalım.

Python'da bir paketi `sys.path` listesine eklerken dikkat etmemiz gereken çok
önemli bir konu var: Bir paketi `sys.path` listesine eklerken, paket adına
karşılık gelen dizini değil, paketi içeren dizini bu listeye eklemeliyiz. Yani
mesela `paket` adlı dizin masaüstündeyse, bizim listeye masaüstünün olduğu
dizini eklememiz gerekiyor, paketin olduğu dizini değil... 

Dikkatlice bakın::
    
    >>> import os, sys
    >>> kullanıcı = os.environ['HOME'] #Windows'ta os.environ['HOMEPATH']
    >>> masaüstü = os.path.join(kullanıcı, 'Desktop')
    >>> sys.path.append(masaüstü)
    
Böylece masaüstünün bulunduğu dizini `sys.path`'e eklemiş olduk. Burada
uyguladığımız adımlara şöyle bir bakalım.

Öncelikle gerekli modülleri içe aktardık::
    
    >>> import os, sys
    
Amacımız masaüstünün yolunu `sys.path`'e eklemek. Dolayısıyla öncelikle
kullanıcı dizininin nerede olduğunu tespit etmemiz lazım. Bildiğiniz gibi,
kullanıcı dizinleri, bilgisayarı kuran kişinin ismine göre belirlendiği için,
bütün bilgisayarlarda bu değer farklı olur. Bu değerin ne olduğu tespit
edebilmek için `os` modülünün `environ` niteliğinden yararlanabiliriz. Bu
nitelik, işletim sistemine özgü çevre değişkenlerini tutar.

GNU/Linux'ta kullanıcı dizinini tutan çevre değişkeni 'HOME' anahtarı ile
gösterilir::
    
    >>> kullanıcı = os.environ['HOME']
    
Windows'ta ise 'HOMEPATH' anahtarını kullanıyoruz::
    
    >>> kullanıcı = os.environ['HOMEPATH']
    
Kullanıcı dizinini elde ettikten sonra, masaüstüne giden yolu bulabilmek için şu
komutu kullanıyoruz::
    
    >>> masaüstü = os.path.join(kullanıcı, 'Desktop')
    
Sıra geldi elde ettiğimiz tam dizin yolunu `sys.path`'e eklemeye::
    
    >>> sys.path.append(masaüstü)
    
Gördüğünüz gibi, listelerin ``append()`` metodu yardımıyla masaüstünün yolunu
`sys.path` adlı listeye ekledik.

Artık masaüstünde bulunan paketleri rahatlıkla her yerden içe aktarabiliriz.
    
.. note:: `os` modülü hakkında daha geniş bilgi için :doc:`standart_moduller/os`
 başlıklı konuyu inceleyebilirsiniz. `sys` modülü hakkında bilgi için ise
 :doc:`standart_moduller/sys` başlığını ziyaret edebilirsiniz.



Paketlerde İsim Çakışmaları
============================

__init__.py Dosyası
---------------------

.. rubric:: Dipnotları:
 
.. [#] Daha önce Python'ın 2.x sürümlerini kullanmış olanlar, bu yapının
 bir paket oluşturmak için yeterli olmadığını düşünebilir. Çünkü Python'ın 2.x
 sürümlerinde bir paket oluşturabilmek için, `siparistakip` dizininin içinde
 `__init__.py` adlı bir dosya daha oluşturmamız gerekiyordu. Ancak Python3'te
 bu zorunluluk ortadan kaldırıldı. Eğer bu söylediğimiz şeyin ne anlama
 geldiğini bilmiyorsanız, bu uyarıyı görmezden gelip yolunuza devam
 edebilirsiniz.