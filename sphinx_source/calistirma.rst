.. meta:: :description: Bu bölümde Python programlama dilinin farklı işletim
           sistemlerinde nasıl çalıştırılacağını öğreneceğiz.
          :keywords: python, python2, python3, nasıl çalıştırılır, kaynaktan
           kurulum, yol, path, yola ekleme, gnu linux, windows, py 

.. highlight:: none

**************************
Python Nasıl Çalıştırılır? 
**************************

Bir önceki bölümde, Python'ı farklı platformlara nasıl kuracağımızı bütün
ayrıntılarıyla anlattık. Bu bölümde ise kurduğumuz bu Python programını hem
GNU/Linux'ta hem de Windows'ta nasıl çalıştıracağımızı göreceğiz. Öncelikle
GNU/Linux kullanıcılarının Python'ı nasıl çalıştıracağına bakalım.

GNU/Linux Kullanıcıları 
*************************

Geçen bölümlerde gördüğünüz gibi, Python3'ü GNU/Linux sistemleri üzerine farklı
şekillerde kurabiliyoruz. Bu bölümde, her bir kurulum türü için Python3'ün nasıl
çalıştırılacağını ayrı ayrı inceleyeceğiz.

Kurulu Python3'ü Kullananlar 
==============================

Eğer sisteminizde zaten Python3 kurulu ise komut satırında yalnızca şu komutu
vererek Python3'ü başlatabilirsiniz::
    
    python

Ancak daha önce de dediğimiz gibi, |today| tarihi itibariyle pek çok GNU/Linux
dağıtımında öntanımlı olarak Python2 kuruludur. Dolayısıyla ``python`` komutunu
verdiğinizde çalışan sürüm muhtemelen Python2 olacaktır. Bu yüzden sistemimizde
öntanımlı olarak hangi sürümün kurulu olduğuna ve ``python`` komutunun hangi
sürümü başlattığına çok dikkat etmelisiniz.

Yine daha önce de söylediğimiz gibi, sisteminizde hem Python2 hem de Python3
zaten kurulu durumda olabilir. O yüzden yukarıdaki komutu bir de ``python3``
şeklinde vermeyi deneyebilirsiniz.

Örneğin Ubuntu GNU/Linux dağıtımının **12.10** sürümünden itibaren ``python``
komutu Python2'yi; ``python3`` komutu ise Python3'ü çalıştırıyor.

Python3'ü Depodan Kuranlar 
============================

Dediğimiz gibi, |today| tarihi itibariyle GNU/Linux dağıtımlarında öntanımlı
Python sürümü ağırlıklı olarak Python2'dir. Dolayısıyla ``python`` komutu
Python'ın 2.x sürümlerini çalıştırır. Bu durumdan ötürü, herhangi bir çakışmayı
önlemek için GNU/Linux dağıtımları Python3 paketini farklı bir şekilde
adlandırma yoluna gider. Şu anda piyasada bulunan dağıtımların ezici çoğunluğu
Python3 paketini 'python3' şeklinde adlandırıyor. O yüzden GNU/Linux
kullanıcıları, eğer paket yöneticilerini kullanarak Python kurulumu
gerçekleştirmiş iseler, komut satırında şu komutu vererek Python3'ü
başlatabilirler::

	python3

Bu komutun ardından şuna benzer bir ekranla karşılaşmış olmalısınız:

.. container:: screenshot

    |screenshotlin|

Eğer yukarıdaki ekranı gördüyseniz Python'la programlama yapmaya hazırsınız
demektir. Değilse, geriye dönüp işlerin nerede ters gittiğini bulmaya
çalışabilirsiniz.

Bu aşamada işlerin nerede ters gitmiş olabileceğine dair birkaç ipucu verelim:

    #. Python3 kurulurken paket yöneticinizin herhangi bir hata vermediğinden,
       programın sisteminize başarıyla kurulduğundan emin olun. Bunun için
       Python3'ün kurulu paketler listesinde görünüp görünmediğini
       denetleyebilirsiniz. 
    
    #. ``python3`` komutunu doğru verdiğinize emin olun. Python programlama
       diline özellikle yeni başlayanların en sık yaptığı hatalardan biri *python*
       kelimesini yanlış yazmaktır. *Python* yerine yanlışlıkla *pyhton*, *pyton*
       veya *phyton* yazmış olabilirsiniz. Ayrıca ``python3`` komutunun tamamen
       küçük harflerden oluştuğuna dikkat edin. *Python* ve *python* bilgisayar
       açısından aynı şeyler değildir. 
    
    #. Kullandığınız dağıtımın Python3 paketini adlandırma politikası yukarıda
       anlattığımızdan farklı olabilir. Yani sizin kullandığınız dağıtım, belki de
       Python3 paketini farklı bir şekilde adlandırmıştır. Eğer durum böyleyse,
       dağıtımınızın yardım kaynaklarını (wiki, forum, irc, yardım belgeleri, kullanıcı
       listeleri, vb.) kullanarak ya da `istihza.com/forum
       <http://www.istihza.com/forum>`_ adresinde sorarak Python3'ün nasıl
       çalıştırılacağını öğrenmeyi deneyebilirsiniz. 
       
Gelelim Python3'ü kaynaktan derlemiş olanların durumuna...

Python3'ü root Olarak Derleyenler 
====================================

Eğer Python3'ü önceki bölümlerde anlattığımız şekilde kaynaktan `root` hakları
ile derlediyseniz ``python3`` komutu çalışmayacaktır. Bunun yerine şu komutu
kullanmanız gerekecek:

.. parsed-literal::

    python\ |major-noformat|

.. note:: Kurduğunuz Python3 sürümünün |major| olduğunu varsayıyorum. Eğer
          farklı bir Python3 sürümü kurduysanız, elbette başlatıcı komut olarak o sürümün
          adını kullanmanız gerekecektir. Mesela: ``python3.0`` veya ``python3.1``. Bu
          arada |pycommand| komutunda |ext-noformat| sayısının rakamları arasında bir adet
          nokta işareti olduğunu gözden kaçırmıyoruz...

Tıpkı paket deposundan kurulumda olduğu gibi, eğer yukarıdaki komut Python'ı
çalıştırmanızı sağlamıyorsa, kurulum esnasında bazı şeyler ters gitmiş olabilir.
Örneğin kaynaktan kurulumun herhangi bir aşamasında bir hata almış olabilirsiniz
ve bu da Python'ın kurulumunu engellemiş olabilir.

Gördüğünüz gibi, Python'ı kaynaktan derleyenler Python programlama dilini
çalıştırabilmek için Python'ın tam sürüm adını belirtiyor. Dilerseniz bu şekilde
çalışmaya devam edebilirsiniz. Bunun hiçbir sakıncası yok. Ancak ben size
kolaylık açısından, `/usr/bin/` dizini altına `py3` adında bir sembolik bağ
yerleştirmenizi tavsiye ederim. Böylece sadece ``py3`` komutunu vererek
Python3'ü başlatabilirsiniz.

Peki bunu nasıl yapacağız?

Python kaynaktan derlendiğinde çalıştırılabilir dosya `/usr/local/bin/` dizini
içine `Python`\ |major| (veya kurduğunuz Python3 sürümüne bağlı olarak
`Python3.0` ya da `Python3.1`) adıyla kopyalanır. Bu nedenle Python3'ü
çalıştırabilmek için |pycommand| komutunu kullanmamız gerekir. Python3'ü
çalıştırabilmek için mesela sadece ``py3`` gibi bir komut kullanmak istiyorsak
yapacağımız tek şey `/usr/local/bin/` dizini içindeki `python`\ |major| adlı
dosyaya `/usr/bin` dizini altından, `py3` adlı bir sembolik bağ oluşturmak
olacaktır. Bunun için ``ln`` komutunu kullanacağız:

.. parsed-literal::

    ln -s /usr/local/bin/python\ |major-noformat| /usr/bin/py3

Tabii bu komutu yetkili kullanıcı olarak vermeniz gerektiğini söylememe herhalde
gerek yoktur. Bu komutu verdikten sonra artık sadece ``py3`` komutu ile
Python programlama dilini başlatabilirsiniz.

Çok Önemli Bir Uyarı
---------------------

Bir önceki adımda anlattığımız gibi Python3'ü resmi sitesinden indirip kendiniz
derlediniz. Gayet güzel. Ancak bu noktada çok önemli bir konuya dikkatinizi
çekmek isterim. En baştan beri söylediğimiz gibi, Python programlama dili
GNU/Linux işletim sistemlerinde çok önemli bir yere sahiptir. Öyle ki bu
programlama dili, kullandığınız dağıtımın belkemiği durumunda olabilir.

Örneğin Ubuntu GNU/Linux dağıtımında pek çok sistem aracı Python ile
yazılmıştır. Bu yüzden, sistemdeki öntanımlı Python sürümünün ne olduğu ve
dolayısıyla ``python`` komutunun hangi Python sürümünü çalıştırdığı çok
önemlidir. Çünkü sisteminizdeki hayati bazı araçlar, ``python`` komutunun
çalıştırdığı Python sürümüne bel bağlamış durumdadır. Dolayısıyla sizin bu
``python`` komutunun çalıştırdığı Python sürümüne dokunmamanız gerekir. 

Mesela eğer kullandığınız işletim sisteminde ``python`` komutu Python'ın 2.x
sürümlerinden birini çalıştırıyorsa sembolik bağlar veya başka araçlar
vasıtasıyla ``python`` komutunu Python'ın başka bir sürümüne bağlamayın. Bu
şekilde bütün sistemi kullanılmaz hale getirirsiniz. Elbette eğer kurulum
aşamasında tarif ettiğimiz gibi, Python3'ü ``make install`` yerine ``make
altinstall`` komutu ile kurmaya özen gösterdiyseniz, sonradan oluşturduğunuz bağ
dosyasını silip ``python`` komutunu yine sistemdeki öntanımlı sürüme
bağlayabilirsiniz. Bu şekilde her şey yine eski haline döner. Ama eğer Python'ı
``make install`` komutuyla kurmanızdan ötürü sistemdeki öntanımlı Python
sürümüne ait dosyaları kaybettiyseniz sizin için yapılacak fazla bir şey yok...
Sistemi tekrar eski kararlı haline getirmek için kan, ter ve gözyaşı
dökeceksiniz...

Aynı şekilde, kullandığınız dağıtımda ``python3`` komutunun öntanımlı olarak
belirli bir Python sürümünü başlatıp başlatmadığı da önemlidir. Yukarıda
``python`` komutu ile ilgili söylediklerimiz ``python3`` ve buna benzer başka
komutlar için de aynen geçerli. 

Örneğin, Ubuntu GNU/Linux dağıtımında ``python`` komutu sistemde kurulu olan
Python 2.x sürümünü; ``python3`` komutu ise sistemde kurulu olan Python 3.x
sürümünü çalıştırdığından, biz kendi kurduğumuz Python sürümleri için,
sistemdeki sürümlerle çakışmayacak isimler seçtik. Mesela kendi kurduğumuz
Python3 sürümünü çalıştırmak için ``py3`` gibi bir komut tercih ettik.

İyi bir test olarak, Python programlama dilini kendiniz kaynaktan derlemeden
önce şu komutun çıktısını iyice inceleyebilirsiniz::

    ls -g {,/usr{,/local}}/bin | grep python
    
Bu komut iki farklı Python sürümünün kurulu olduğu sistemlerde şuna benzer bir
çıktı verir (çıktı kırpılmıştır):

.. parsed-literal::
    
    dh_python2
    dh_python3
    pdb2.7 -> ../lib/python2.7/pdb.py
    pdb3.2 -> ../lib/python3.2/pdb.py
    py3versions -> ../share/python3/py3versions.py
    *python -> python2.7*
    *python2 -> python2.7*
    python2.7
    *python3 -> python3.2*
    python3.2 -> python3.2mu
    python3.2mu
    python3mu -> python3.2mu
    pyversions -> ../share/python/pyversions.py

Yatık harflerle gösterdiğimiz kısımlara dikkat edin. Gördüğünüz gibi ``python``
ve ``python2`` komutları bu sistemde Python'ın 2.7 sürümünü çalıştırıyor.
``python3`` komutu ise Python'ın 3.2 sürümünü... Dolayısıyla yukarıdaki çıktıyı
aldığımız bir sistemde kendi kurduğumuz Python sürümlerine 'python', 'python2'
veya 'python3' gibi isimler vermekten kaçınmalıyız.

Sözün özü, bir GNU/Linux kullanıcısı olarak sistemdeki öntanımlı hiçbir Python
sürümünü silmemeli, öntanımlı sürüme ulaşan komutları değiştirmemelisiniz. Eğer
mesela sisteminizde ``python3`` komutu halihazırda bir Python sürümünü
çalıştırıyorsa, siz yeni kurduğunuz Python sürümüne ulaşmak için öntanımlı adla
çakışmayacak başka bir komut adı kullanın. Yani örneğin sisteminizde ``python3``
komutu Python'ın `3.2` sürümünü çalıştırıyorsa, siz yeni kurduğunuz sürümü
çalıştırmak için ``py3`` gibi bir sembolik bağ oluşturun. Bırakın öntanımlı
komut (``python``, ``python3`` vb.) öntanımlı Python sürümünü çalıştırmaya devam
etsin.

Asla unutmayın. Siz bir programcı adayı olarak, program yazacağınız işletim
sistemini enine boyuna tanımakla yükümlüsünüz. Dolayısıyla işletim sisteminizi
kararsız hale getirecek davranışları bilmeli, bu davranışlardan kaçınmalı,
yanlış bir işlem yaptığınızda da nasıl geri döneceğinizi bilmelisiniz. Hele ki
bir programı kaynaktan derlemeye karar vermişseniz...

Bu ciddi uyarıyı da yaptığımıza göre gönül rahatlığıyla yolumuza devam
edebiliriz.

Python3'ü Ev Dizinine Kuranlar 
================================

Eğer Python3'ü kısıtlı kullanıcı hakları ile derleyip ev dizininize kurduysanız
yukarıdaki komutlar Python'ı çalıştırmanızı sağlamayacaktır. Python3'ü ev
dizinine kurmuş olan kullanıcılar Python3'ü çalıştırabilmek için, öncelikle
komut satırı aracılığıyla Python3'ü kurdukları dizine, oradan da o dizin
altındaki `bin/` klasörüne ulaşacak ve orada şu komutu verecek:

.. parsed-literal::

    ./python\ |major-noformat|

Diyelim ki Python3'ü `$HOME/python` adlı dizine kurdunuz. Önce şu komutla
`$HOME/python/bin` adlı dizine ulaşıyoruz::

    cd $HOME/python/bin

Ardından da şu komutu veriyoruz:

.. parsed-literal::

    ./python\ |major-noformat|

.. note:: Komutun başındaki `./` işaretinin ne işe yaradığını artık adınız gibi
          biliyorsunuz...

.. note:: Elbette ben burada kurduğunuz Python sürümünün |major-noformat|
          olduğunu varsaydım. Eğer farklı bir sürüm kurduysanız yukarıdaki komutu ona göre
          yazmanız gerekiyor.

Eğer isterseniz bu şekilde çalışmaya devam edebilirsiniz. Ancak her defasında
Python'ın kurulu olduğu dizin altına gelip orada ./python\ |major-noformat|
komutunu çalıştırmak bir süre sonra eziyete dönüşecektir. İşlerinizi
kolaylaştırmak için şu işlemleri takip etmelisiniz:

\1. ev dizininizin altında bulunan `.profile` (veya kullandığınız dağıtıma göre
`.bash_profile` ya da `.bashrc`) adlı dosyayı açın.

\2. Bu dosyanın en sonuna şuna benzer bir satır yerleştirerek Python'ı
çalıştırmamızı sağlayan dosyanın bulunduğu dizini yola ekleyin:

    .. parsed-literal::

        export PATH=$PATH:$HOME/python/bin/

\3. `$HOME/python/bin/` satırı Python3'ün çalıştırılabilir dosyasının hangi
dizin altında olduğunu gösteriyor. Ben burada Python3'ün çalıştırılabilir
dosyasının `$HOME/python/bin` dizini içinde olduğunu varsaydım. O yüzden de
`$HOME/python/bin/` gibi bir satır yazdım. Ama eğer Python3'ün çalıştırılabilir
dosyası sizde farklı bir dizindeyse bu satırı ona göre yazmalısınız.

\4. Kendi sisteminize uygun satırı dosyaya ekledikten sonra dosyayı kaydedip
çıkın. Dosyada yaptığımız değişikliğin etkin hale gelebilmesi için şu komutu
verin:

    .. parsed-literal::

        source .profile

Elbette eğer sizin sisteminizdeki dosyanın adı `.bash_profile` veya `.bashrc`
ise yukarıdaki komutu ona göre değiştirmelisiniz.

\5. Daha sonra `$HOME/python/bin/python`\ |major| adlı dosyaya
`$HOME/python/bin/` dizini altından mesela `py3` gibi bir sembolik bağ verin:

    .. parsed-literal:: 
    
        ln -s $HOME/python/bin/python\ |major-noformat| $HOME/python/bin/py3
        
\6. Bilgisayarınızı yeniden başlatın.

\7. Artık hangi konumda bulunursanız bulunun, şu komutu vererek Python3'ü
başlatabilirsiniz:

    .. parsed-literal::

        py3

Burada da eğer yukarıdaki komut Python3'ü çalıştırmanızı sağlamıyorsa, bazı
şeyleri eksik veya yanlış yapmış olabilirsiniz. Yardım almak için
`istihza.com/forum <http://www.istihza.com/forum>`_ adresine uğrayabilirsiniz.

Python3'ü başarıyla kurup çalıştırabildiğinizi varsayarak yolumuza devam edelim.

GNU/Linux'ta Farklı Sürümleri Birlikte Kullanmak 
==================================================

Daha önce de dediğimiz gibi, şu anda piyasada iki farklı Python serisi
bulunuyor: Python2 ve Python3. Çok uzun zamandan beri kullanımda olduğu için,
Python2 Python3'e kıyasla daha yaygın. Eğer hem Python2 ile yazılmış programları
çalıştırmak, hem de Python3 ile geliştirme yapmak istiyorsanız, sisteminizde hem
Python2'yi hem de Python3'ü aynı anda bulundurmayı tercih edebilirsiniz. Peki
bunu nasıl yapacaksınız?

En başta da söylediğimiz gibi, hemen hemen bütün GNU/Linux dağıtımlarında
Python2 kurulu olarak gelir. Dolayısıyla eğer sisteminize ek olarak Python3'ü de
kurduysanız (kaynaktan veya paket deposundan), başka herhangi bir şey yapmanıza
gerek yok. Yukarıda anlattığımız yönergeleri takip ettiyseniz, konsolda
``python`` komutu verdiğinizde Python2 çalışacak, ``python3`` (veya ``py3``)
komutunu verdiğinizde ise Python3 çalışacaktır.

Ama eğer sisteminizde Python2 bile kurulu değilse, ki bu çok çok düşük bir
ihtimaldir, Python2'yi paket yöneticiniz yardımıyla sisteminize kurabilirsiniz.
Şu anda piyasada olup da paket deposunda Python bulundurmayan GNU/Linux dağıtımı
pek azdır.

GNU/Linux'ta Python'ı nasıl çalıştıracağımızı ve farklı Python sürümlerini bir
arada nasıl kullanacağımızı öğrendiğimize göre, Windows kullanıcılarının
durumuna bakabiliriz.

Windows Kullanıcıları 
**********************

Windows kullanıcıları Python3'ü iki şekilde başlatabilir:

    1. *Başlat > Tüm Programlar > Python*\ |major-italic|\ *> Python (Command
       Line)* yolunu takip ederek. 
    
    2. Komut satırında ``python`` komutunu vererek.

Eğer birinci yolu tercih ederseniz, Python'ın size sunduğu komut satırına
doğrudan ulaşmış olursunuz. Ancak Python komut satırına bu şekilde ulaştığınızda
bazı kısıtlamalarla karşı karşıya kalırsınız. Doğrudan Python'ın komut satırına
ulaşmak yerine önce MS-DOS komut satırına ulaşıp, oradan Python komut satırına
ulaşmak özellikle ileride yapacağınız çalışmalar açısından çok daha mantıklı
olacaktır. O yüzden komut satırına bu şekilde ulaşmak yerine ikinci seçeneği
tercih etmenizi tavsiye ederim. Bunun için önceki bölümlerde gösterdiğimiz
şekilde komut satırına ulaşın ve orada şu komutu çalıştırın::

    python 
    
Bu komutu verdiğinizde şuna benzer bir ekranla karşılaşacaksınız:

.. container:: screenshot

    |screenshotwin|

Eğer bu komut yukarıdakine benzer bir ekran yerine bir hata mesajı verdiyse
kurulum sırasında bazı adımları eksik veya yanlış yapmış olabilirsiniz.
Yukarıdaki komut çalışmıyorsa, muhtemelen kurulum sırasında *Add python*\
|major-italic| *to path* kutucuğunu işaretlemeyi unutmuşsunuzdur. Eğer öyleyse,
kurulum dosyasını tekrar çalıştırıp, ilgili adımı gerçekleştirmeniz veya
Python'ı kendiniz YOL'a eklemeniz gerekiyor.

``python`` komutunu başarıyla çalıştırabildiğinizi varsayarak yolumuza devam
edelim.

Windows'ta Farklı Sürümleri Birlikte Kullanmak 
==================================================

Daha önce de dediğimiz gibi, şu anda piyasada iki farklı Python serisi
bulunuyor: Python2 ve Python3. Çok uzun zamandan beri kullanımda olduğu için,
Python2 Python3'e kıyasla daha yaygın. Eğer hem Python2 ile yazılmış programları
çalıştırmak, hem de Python3 ile geliştirme yapmak istiyorsanız, sisteminizde hem
Python2'yi hem de Python3'ü aynı anda bulundurmayı tercih edebilirsiniz. Peki
bunu nasıl yapacaksınız?

Windows'ta bu işlemi yapmak çok kolaydır. `python.org/download
<http://www.python.org/download/>`_ adresine giderek farklı Python sürümlerini
bilgisayarınıza indirebilir ve bunları bilgisayarınıza normal bir şekilde
kurabilirsiniz. Bu şekilde sisteminize istediğiniz sayıda farklı Python sürümü
kurabilirsiniz. Peki bu farklı sürümlere nasıl ulaşacaksınız?

Python, bilgisayarımızdaki farklı Python sürümlerini çalıştırabilmemiz için bize
'py' adlı özel bir program sunar.

.. note:: Py programı yalnızca Windows'a özgüdür. GNU/Linux'ta böyle bir program
 bulunmaz.

Py programını çalıştırmak için, daha önce gösterdiğimiz şekilde sistem komut
satırına ulaşıyoruz ve orada şu komutu veriyoruz::

    py 

Bu komutu verdiğinizde (teorik olarak) sisteminize en son kurduğunuz Python
sürümü çalışmaya başlayacaktır. Ancak bu her zaman böyle olmayabilir. Ya da
aldığınız çıktı beklediğiniz gibi olmayabilir. O yüzden bu komutu verdiğinizde
hangi sürümün başladığına dikkat edin.
    
Eğer sisteminizde birden fazla Python sürümü kurulu ise, bu betik yardımıyla
istediğiniz sürümü başlatabilirsiniz. Mesela sisteminizde hem Python'ın 2.x
sürümlerinden biri, hem de Python'ın 3.x sürümlerinden biri kurulu ise, şu komut
yardımıyla Python 2.x'i başlatabilirsiniz::

    py -2

Python 3.x'i başlatmak için ise şu komutu veriyoruz::

    py -3 
    
Eğer sisteminizde birden fazla Python2 veya birden fazla Python3 sürümü kurulu
ise, ana ve alt sürüm numaralarını belirterek istediğiniz sürüme
ulaşabilirsiniz::

    py -2.6

::
    
    py -2.7
    
::

    py -3.4 

::

    py -3.5
    
Bu arada dikkat ettiyseniz, Python programlarını başlatabilmek için hem
``python`` hem de ``py`` komutunu kullanma imkanına sahibiz. Eğer sisteminizde
tek bir Python sürümü kurulu ise, Python'ı başlatmak için ``python`` komutunu
kullanmak isteyebilir, farklı sürümlerin bir arada bulunduğu durumlarda ise
``py`` ile bu farklı sürümlere tek tek erişmek isteyebilirsiniz.

Böylece Python'la ilgili en temel bilgileri edinmiş olduk. Bu bölümde
öğrendiklerimiz sayesinde Python programlama dilini bilgisayarımıza kurabiliyor
ve bu programlama dilini başarıyla çalıştırabiliyoruz.

Hangi Komut Hangi Sürümü Çalıştırıyor?
***************************************

Artık Python programlama dilinin bilgisayarımıza nasıl kurulacağını ve bu
programlama dilinin nasıl çalıştırılacağını biliyoruz. Ancak konunun öneminden
ötürü, tekrar vurgulayıp, cevabını bilip bilmediğinizden emin olmak istediğimiz
bir soru var: Kullandığınız işletim sisteminde acaba hangi komut, hangi Python
sürümünü çalıştırıyor?

Bu kitapta anlattığımız farklı yöntemleri takip ederek, Python programlama
dilini bilgisayarınıza farklı şekillerde kurmuş olabilirsiniz. Örneğin Python
programlama dilini, kullandığınız GNU/Linux dağıtımının paket yöneticisi
aracılığıyla kurduysanız, Python'ı başlatmak için ``python3`` komutunu
kullanmanız gerekebilir. Aynı şekilde, eğer Python'ı Windows'a kurduysanız, bu
programlama dilini çalıştırmak için ``python`` komutunu kullanıyor
olabilirsiniz. Bütün bunlardan farklı olarak, eğer Python'ın kaynak kodlarını
sitesinden indirip derlediyseniz, Python'ı çalıştırmak için kendi belirlediğiniz
bambaşka bir adı da kullanıyor olabilirsiniz. Örneğin belki de Python'ı
çalıştırmak için ``py3`` gibi bir komut kullanıyorsunuzdur...

Python programlama dilini çalıştırmak için hangi komutu kullanıyor olursanız
olun, lütfen bir sonraki konuya geçmeden önce kendi kendinize şu soruları sorun:

#. Kullandığım işletim sisteminde Python programı halihazırda kurulu mu?
#. Kullandığım işletim sisteminde toplam kaç farklı Python sürümü var?
#. ``python`` komutu bu Python sürümlerinden hangisini çalıştırıyor?
#. ``python3`` komutu çalışıyor mu?
#. Eğer çalışıyorsa, bu komut Python sürümlerinden hangisini çalıştırıyor?
#. Kaynaktan derlediğim Python sürümünü çalıştırmak için hangi komutu
   kullanıyorum?

Biz bu kitapta şunları varsayacağız:

#. Kullandığınız işletim sisteminde Python'ın **2.x** sürümlerini ``python``
   komutuyla çalıştırıyorsunuz.
#. Kullandığınız işletim sisteminde Python'ın **3.x** sürümlerini ``python3``
   komutuyla çalıştırıyorsunuz.

Bu kitaptan yararlanırken, bu varsayımları göz önünde bulundurmalı, eğer
bunlardan farklı komutlar kullanıyorsanız, kodlarınızı ona göre ayarlamalısınız.

Sistem Komut Satırı ve Python Komut Satırı 
*********************************************

Buraya kadar Python programlama dilini nasıl çalıştıracağımız konusundaki bütün
bilgileri edindik. Ancak programlamaya yeni başlayanların çok sık yaptığı bir
hata var: Sistem komut satırı ile Python komut satırını birbirine karıştırmak.

Asla unutmayın, kullandığınız işletim sisteminin komut satırı ile Python'ın
komut satırı birbirinden farklı iki ortamdır. Yani Windows'ta ``cmd``, Ubuntu'da
ise `Ctrl+Alt+T` ile ulaştığınız ortam sistem komut satırı iken, bu ortamı açıp
``python3`` (veya ``python`` ya da ``py3``) komutu vererek ulaştığınız ortam
Python'ın komut satırıdır. Sistem komut satırında sistem komutları (mesela
``cd``, ``ls``, ``dir``, ``pwd``) verilirken, Python komut satırında, biraz
sonra öğrenmeye başlayacağımız Python komutları verilir. Dolayısıyla ``python3``
(veya ``python`` ya da ``py3``) komutunu verdikten sonra ulaştığınız ortamda
``cd Desktop`` ve ``ls`` gibi sistem komutlarını kullanmaya çalışmanız sizi
hüsrana uğratacaktır.
