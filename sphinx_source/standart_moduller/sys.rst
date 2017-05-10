.. meta::
   :description: Bu bölümde sys modülünü inceleyeceğiz. 
   :keywords: python, modül, import, sys

.. highlight:: py3

sys Modülü
***************

Tıpkı ``os`` modülü gibi, ``sys`` de Python programlama dilindeki önemli
standart kütüphane modüllerinden biridir. Bu modül, kullandığınız Python sürümü
ile ilgili bilgi edinmenizi ve kullandığınız Python sürümü ile çeşitli işlemler
yapabilmenizi sağlar. 

Bütün modüllerde olduğu gibi, bu modülü de şu komutla içe aktarıyoruz::
    
    >>> import sys
    
Bu modülün içinde hangi nitelik ve fonksiyonların olduğunu görmek için şu
komutu kullanabileceğinizi biliyorsunuz::
    
    >>> dir(sys)

Gördüğünüz gibi bu modül içinde de epeyce fonksiyon ve nitelik var. Biz bu
bölümde, ``sys`` modülünün en yaygın kullanılan, en önemli fonksiyon ve
niteliklerini ele alacağız.

İlk olarak `exit()` fonksiyonu ile başlayalım...

sys.exit()
===========

``sys`` modülünün ``exit()`` fonksiyonunu kullanarak, programınızın işleyişini
durdurabilir, programınızı kapanmaya zorlayabilirsiniz. Basit bir örnek
verelim::
    
    import sys
    
    sayı = input('Bir sayı girin: ')
    
    if int(sayı) < 0:
        print('çıkılıyor...')
        sys.exit()
    
    else:
        print(sayı)
        
Eğer kullanıcı 0'dan küçük bir sayı girerse programımız ``sys.exit()`` komutunun
etkisiyle çalışmayı durdurup kapanacaktır.

sys.argv
==========

``sys`` modülünün `argv` niteliği, yazdığımız program çalıştırılırken
kullanılan parametreleri bir liste halinde tutar. 

Gelin isterseniz bunun ne demek olduğunu bir örnek üzerinde gösterelim.

Şimdi mesela masaüstünde `deneme.py` adlı bir dosya oluşturun ve içine şunları
yazın::
    
    import sys
    print(sys.argv)
    
Bu programı şu komutla çalıştırın::
    
    python deneme.py
    
Programı çalıştırdığınızda şuna benzer bir çıktı alacaksınız::
    
    ['deneme.py']
    
Gördüğünüz gibi, ``sys.argv`` komutu bize bir liste veriyor. Bu listenin ilk
öğesi, yazdığımız programın adı. Yani `deneme.py`.

Şimdi aynı programı bir de şu şekilde çalıştıralım::
    
    python deneme.py parametre
    
Bu defa programımız bize şu çıktıyı verecek::
    
    ['deneme.py', 'parametre']
    
Gördüğünüz gibi, ``sys.argv`` komutu, programın ismi ile birlikte, bu programa
parametre olarak verilen değerleri de bir liste halinde saklıyor. Bu oldukça
önemli ve kullanışlı bir özelliktir. Bu özellikten pek çok farklı şekillerde
yararlanabilirsiniz. 

Mesela::
    
    import sys
    
    def çık():
        print('Çıkılıyor...')
        sys.exit()
    
    if len(sys.argv) < 2:
        print('Gerekli parametreleri girmediniz!')
        çık()
        
    elif len(sys.argv) > 2:
        print('Çok fazla parametre girdiniz!')
        çık()
    
    elif sys.argv[1] in ['-v', '-V']:
        print('Program sürümü: 0.8')
        
    else:
        mesaj = 'Girdiğiniz parametre ({}) anlaşılamadı!'
        print(mesaj.format(sys.argv[1]))
        çık()
        
Burada öncelikle modülümüzü içe aktardık::
    
    import sys
    
Bunu yapmadan, o modülü kullanamayacağımızı biliyorsunuz.

Ardından ``çık()`` adlı bir fonksiyon tanımladık::
    
    def çık():
        print('Çıkılıyor...')
        sys.exit()
        
Programı sonlandırmak istediğimizde bu fonksiyonu kullanacağız.

Daha sonra şöyle bir ``if`` bloğu oluşturduk::
    
    if len(sys.argv) < 2:
        print('Gerekli parametreleri girmediniz!')
        çık()
        
Eğer ``sys.argv`` listesinin uzunluğu 2'den düşükse, programımız herhangi bir
parametre olmadan, yalnızca ismiyle çalıştırılmış demektir. Bu durumda
kullanıcıya 'Gerekli parametreleri girmediniz!' mesajını gösterip programı
sonlandırıyoruz.

Sonraki kod bloğumuz şöyle::
    
    elif len(sys.argv) > 2:
        print('Çok fazla parametre girdiniz!')
        çık()

Eğer ``sys.argv`` listesi 2'den büyükse, programımız birden fazla parametre ile
çalıştırılmış demektir. Bu durumda kullanıcıya 'Çok fazla parametre girdiniz!'
mesajını gösterip yine programı sonlandırıyoruz.

Bir sonraki kodlarımız şöyle::
    
    elif sys.argv[1] in ['-v', '-V']:
        print('Program sürümü: 0.8')
        
Eğer ``sys.argv`` listesinin ikinci öğesi `-v` veya `-V` ise programımızın
sürüm bilgisini veriyoruz.

Son olarak da şu bloğu yazıyoruz::
    
    else:
        mesaj = 'Girdiğiniz parametre ({}) anlaşılamadı!'
        print(mesaj.format(sys.argv[1]))
        çık()
        
Kullanıcının `-v` veya `-V` dışında bir parametre girmesi durumunda ise, girilen
parametrenin anlaşılamadığı konusunda kullanıcıyı bilgilendirip programdan
çıkıyoruz.

Aşağıda, programımızın hangi komutlara hangi karşılıkları verdiğini
görüyorsunuz::
    
    C:\Users\fozgul\Belgelerim> python deneme.py
    Gerekli parametreleri girmediniz!
    Çıkılıyor...
    
    C:\Users\fozgul\Belgelerim> python deneme.py -a
    Girdiğiniz parametre (-a) anlaşılamadı!
    Çıkılıyor...
    
    C:\Users\fozgul\Belgelerim> python deneme.py -a -b
    Çok fazla parametre girdiniz!
    Çıkılıyor...
    
    C:\Users\fozgul\Belgelerim> python deneme.py -v
    Program sürümü: 0.8
    
    C:\Users\fozgul\Belgelerim> python deneme.py -V
    Program sürümü: 0.8
    
sys.executable
===============

Eğer, yazdığınız bir programda, programınızın çalıştığı sistemdeki Python'ın
çalıştırılabilir dosyasının adını ve yolunu öğrenmeniz gerekirse bu niteliği
kullanabilirsiniz:

.. parsed-literal::
    
    >>> sys.executable   
    
    C:\\Python\ |ext-noformat|\ python.exe

sys.getwindowsversion()
==========================

Bu fonksiyon, kullanılan Windows sürümüne ilişkin bilgi verir::
    
    >>> sys.getwindowsversion()

    sys.getwindowsversion(major=5, minor=1, build=2600, 
    platform=2, service_pack='Service Pack 3')
    
.. warning:: Bu fonksiyon yalnızca Windows'ta çalışır. GNU/Linux'ta bu fonksiyon
    tanımlı değildir.
    
Bu fonksiyon kendi içinde de bazı nitelikler barındırır. Bunları görmek için şu
komutu kullanabilirsiniz::
    
    >>> ver = sys.getwindowsversion()
    >>> dir(ver)
    
    ['__add__', '__class__', '__contains__', '__delattr__', 
     '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
     '__getattribute__', '__getitem__', '__getnewargs__', 
     '__gt__', '__hash__', '__init__', '__iter__', '__le__', 
     '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
     '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
     '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
     'build', 'count', 'index', 'major', 'minor', 'n_fields', 
     'n_sequence_fields', 'n_unnamed_fields', 'platform', 
     'product_type', 'service_pack', 'service_pack_major', 
     'service_pack_minor', 'suite_mask']
     
Bu niteliklere erişmek için şu söz dizimini kullanabilirsiniz::
    
    >>> ver.service_pack()

sys.path
===========

:doc:`../moduller` konusunu işlerken ``sys`` modülünün `path` niteliğinden söz
etmiştik. O yüzden orada söylediklerimizi tekrarlamayacağız. 

sys.platform
==============

``os`` modülünü incelerken öğrendiğimiz `name` niteliği gibi, ``sys`` modülünün
`platform` adlı niteliği de, kodlarımızın çalıştığı işletim sistemi hakkında
bize bilgi verir::
    
    >>> sys.platform
    
Eğer bu komutu GNU/Linux'ta verirsek `linux` çıktısı, Windows'ta verirsek
`win32` çıktısı, Mac OS X'te verirsek `darvin` çıktısı alırız. 

sys.prefix
===========

``sys`` modülünün `prefix` niteliği Python'ın hangi dizine kurulduğunu
gösterir::
    
    >>> sys.prefix
    
    '/home/local/python'

Veya::
    
    >>> sys.prefix

    'C:\\Python'

sys.ps1
========

``sys`` modülünün `ps1` niteliği, etkileşimli kabuktaki '>>>' işaretini tutar::
    
    >>> sys.ps1
    
    '>>> '
    
Eğer isterseniz bu işareti değiştirebilirsiniz::
    
    >>> sys.ps1 = '+++ '
 
Bu komutu verdikten sonra '>>>' işaretinin '+++' olarak değiştiğini
göreceksiniz. 

sys.ps2
========

Etkileşimli kabukta Python bizden girdiğimiz kodların devamını beklediğini
göstermek için '...' işaretini kullanır::
    
    >>> a = 5
    >>> if a == 5:
    ...
    
``sys`` modülünün `ps2` niteliği, işte etkileşimli kabuktaki devam satırlarında
gördüğümüz bu '...' işaretini tutar::
    
    >>> sys.ps2
    
    '... '
    
Eğer isterseniz bu işareti değiştirebilirsiniz::
    
    >>> sys.ps1 = '--- '
 
Bu komutu verdikten sonra '...' işaretinin '---' olarak değiştiğini
göreceksiniz.

sys.version
=============

``sys`` modülünün `version` niteliği kullandığınız Python sürümüne ilişkin
ayrıntılı bilgi verir:

.. parsed-literal::

    >>> sys.version

    |version3-string|

sys.version_info
===================

``sys`` modülünün `version_info` niteliği de kullandığınız Python sürümüne
ilişkin bilgi verir:

.. parsed-literal::

    >>> sys.version_info

    |version-info3|
    
Bu nitelik kendi içinde birtakım başka nitelikler de barındırır::
    
    >>> dir(sys.version_info)
    
    ['count', 'index', 'major', 'micro', 'minor', 
     'n_fields', 'n_sequence_fields', 'n_unnamed_fields', 
     'releaselevel', 'serial']
     
Bu niteliklere nasıl ulaşacağınızı biliyorsunuz::
    
    >>> sys.version_info.major #büyük sürüm numarası
    >>> sys.version_info.minor #küçük sürüm numarası
    >>> sys.version_info.micro #minik sürüm numarası
       
sys.winver
============

``sys`` modülünün `winver` niteliği Python'ın büyük sürüm numarasıyla küçük
sürüm numarasını verir:

.. parsed-literal::

    >>> sys.winver

    |major-noformat|
    
.. warning:: Bu nitelik yalnızca Windows'ta çalışır; GNU/Linux'ta tanımlı
    değildir. 

sys.stdout
==========

Önceki derslerimizden de bildiğiniz gibi `stdout`, 'standart çıktı konumu', yani
programlarımızın çıktılarını standart olarak verdikleri konum anlamına geliyor.

Python'da yazdığımız programlar çıktılarını standart olarak komut satırına
verir. Yani mesela::
    
    >>> print('merhaba zalim dünya')
    
komutunu verdiğimizde, bu komutun çıktısı komut ekranında görünecektir.

Python'da standart çıktı konumununun neresi olacağı bilgisi ``sys`` modülünün
`stdout` adlı niteliği içinde tutulur::
    
    >>> import sys
    >>> sys.stdout
    
    <_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1254'>
    
Standart çıktı konumuna yazmanın en yaygın yolunun ``print()`` komutunu
kullanmak olduğunu biliyoruz. Bu komut, standart çıktı konumu neresi ise oraya
yazacaktır. 

Standart çıktı konumuma yazmanın başka bir yolu da doğrudan ``sys.stdout``
niteliğinin ``write()`` metodunu kullanmaktır. 

Dikkatlice bakın::
    
    >>> sys.stdout.write('merhaba zalim dünya')
    
``print()`` komutundan farklı olarak ``sys.stdout.write()`` fonksiyonu şöyle bir
çıktı verir::
    
    merhaba zalim dünya19
    
Burada, çıktının sonundaki `19` sayısı 'merhaba zalim dünya' karakter dizisinin
uzunluğunu gösteriyor. ``sys.stdout.write()`` fonksiyonu etkileşimli kabukta
kullanıldığında böyle bir çıktı verir. Ama eğer bu kodları bir dosyaya yazıp
çalıştırırsanız sonraki `19` sayısı görünmez.

Bu arada, her ne kadar ``print()`` ve ``sys.stdout.write()`` birbirine benzese
de aralarında önemli farklar bulunur. Örneğin ``print()`` fonksiyonu parametre
olarak her türlü veri tipini alabilir. Ancak ``sys.stdout.write()`` fonksiyonu
parametre olarak yalnızca karakter dizisi alabilir::
    
    >>> sys.stdout.write(12)
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not int
    
Dolayısıyla ``sys.stdout.write()`` fonksiyonuna parametre olarak vereceğiniz
değeri öncelikle karakter dizisine çevirmeniz gerekir::
    
    >>> sys.stdout.write(str(12))
    
    122
    
.. note:: Sondaki `2` sayısının '12' karakter dizisinin uzunluğunu gösterdiğini
    söylemiştik. Bu kodları dosyaya yazıp çalıştırdığınızda yalnızca `12`
    çıktısı alırsınız.
    
``print()`` ile ``sys.stdout.write()`` arasındaki önemli bir fark da,
``print()`` fonksiyonu yazma işleminden sonra bir sonraki satıra geçerken,
``sys.stdout.write()`` fonksiyonunun geçmemesidir.

.. warning:: ``sys.stdout.write()`` fonksiyonu etkileşimli kabuktan
    çalıştırıldığında ve dosyadan çalıştırıldığında birbirinden farklı çıktılar
    verir. O yüzden aşağıdaki örnekleri dosyaya yazıp çalıştırmanızı tavsiye
    ederim.
    
Mesela şu örneğe bakalım::
    
    for i in 'istihza':
        print(i)
        
Bu komut şu çıktıyı verir::
    
    i
    s
    t
    i
    h
    z
    a
 
Gördüğünüz gibi, ``print()`` fonksiyonu, döngüye giren her öğeyi yeni satıra
basıyor.

Bir de ``sys.stdout.write()`` fonksiyonunun ne yaptığına bakalım::
    
    import sys
    
    for i in 'istihza':
        sys.stdout.write(i)
        
Bu komutlar ise şu çıktıyı verir::
    
    istihza
    
Gördüğünüz gibi, ``sys.stdout.write()`` fonksiyonu öğelerin hepsini aynı satıra
bastı. Eğer öğelerin ayrı satırlara basılmasını istiyorsanız bunu açıkça
belirtmelisiniz::
    
    import sys

    for i in 'istihza':
        sys.stdout.write(i+'\n')
        
``sys.stdout.write()`` fonksiyonunun otomatik olarak satır başı karakterini
basmıyor oluşunu kullanarak kronometre benzeri bir program yazabilirsiniz::
    
    import sys
    
    sayaç = 0
    
    while True:
        sys.stdout.write(str(sayaç)+'\r')
        sayaç += 1
        
Burada, önceki derslerimizde öğrendiğimiz kaçış dizilerinden `\\r`'yi
kullanarak, her öğenin ekrana basılmasının ardından satırın en başına
dönülmesini sağladık. Böylece öğeler yan yana değil de birbirlerinin üstüne
basılmış oldu.

Bu arada, eğer yukarıdaki kodlar herhangi bir çıktı vermeden bekliyorsa, kodları
şu şekilde yazın::
    
    import sys
    
    sayaç = 0
    
    while True:
        sys.stdout.write(str(sayaç)+'\r')
        sys.stdout.flush()
        sayaç += 1    

Burada eklediğimiz ``sys.stdout.flush()`` satırı, Python'ın tamponda beklettiği
verileri çıktıya göndermesini sağlar. Siz bu 'flush' kavramını ``print()``
fonksiyonundan hatırlıyor olmalısınız (``print()`` fonksiyonunun `flush`
parametresi).

Hatırlarsanız, 'flush' kavramının yanısıra, ``print()`` fonksiyonunu işlerken
öğrendiğimiz bir başka kavram da standart çıktı konumunun değiştirilmesi idi.
``print()`` fonksiyonuna verdiğimiz `file` parametresi yardımıyla
programlarımızın standart olarak çıktı verdiği konumu değiştirebiliyorduk::
    
    f = open('çıktılar.txt', 'w')
    print('merhaba zalim dünya', file=f)
    
Burada `çıktılar.txt` adlı bir dosya oluşturduk ve bunu ``print()``
fonksiyonunun `file` parametresine atayarak, çıktıları komut satırı yerine
`çıktılar.txt` adlı dosyaya gönderdik.

Aynı işlemi ``sys.stdout`` aracılığıyla da yapabileceğimizi biliyorsunuz::
    
    import sys
    
    f = open('çıktılar.txt', 'w'):
    sys.stdout = f
    sys.stdout.write('merhaba zalim dünya')
        
Gerçi bu sizin bilmediğiniz bir şey değil. Zira siz bunu :doc:`../print`
konusunu işlerken de görmüştünüz...

sys.stderr
==========

Önceki bölümde gördüğümüz şu kodları tekrar önümüze alalım::
    
    import sys
    
    f = open('çıktılar.txt', 'w')
    sys.stdout = f
    sys.stdout.write('merhaba zalim dünya')
        
Bu kodlar, bildiğiniz gibi, çıktı olarak verilmek istenen değerlerin
`çıktılar.txt` adlı bir dosyaya yönlendirilmesini sağlıyor. Ancak kodlarımızı bu
şekilde yazdığımızda sadece normal değerler yönlendirilecektir. Mesela çalışma
esnasında ortaya çıkan hatalar yine komut ekranına basılmaya devam edecektir::

    import sys
    
    f = open('çıktılar.txt', 'w')
    sys.stdout = f
    sys.stdout.write(1/0)
        
Bu kodları çalıştırdığınızda, standart çıktı konumu yönlendirilmiş olmasına
rağmen, hata mesajı komut satırına basılacaktır::
    
    Traceback (most recent call last):
      File "deneme.py", line 5, in <module>
        sys.stdout.write(1/0)
    ZeroDivisionError: division by zero
    
Çünkü Python'da hata mesajlarının öntanımlı olarak basıldığı yer komut
satırıdır. Nasıl çıktıların standart olarak basıldığı yeri teknik olarak
'standart çıktı konumu' (`Standard Output - stdout`) olarak adlandırıyorsak,
hataların standart olarak basıldığı yeri de teknik olarak 'standart hata
konumu' (`Standard Error - stderr`) olarak adlandırıyoruz. 

Tıpkı `stdout`'u manipüle edebildiğimiz gibi, `stderr`'i de manipüle
edebiliriz::
    
    import sys
    
    f =open('hatalar.txt', 'w')
    sys.stderr = f
    sys.stderr.write(1/0)
    
Bu durumda, programımızın işleyişi sırasında ortaya çıkan hatalar `hatalar.txt`
adlı bir dosyaya yönlendirilecektir. 

Bu bilgiyi kullanarak şöyle bir kod da yazabiliriz::
    
    import sys
    
    çıktılar = open('çıktılar.txt', 'w')
    hatalar = open('hatalar.txt', 'w')
    sys.stdout = çıktılar
    sys.stderr = hatalar
    
    print('normal çıktı')
    print('hata mesajı: ', 1/0)
    
Bu kodları çalıştırdığınızda, hata mesajı üretmeden başarıyla tamamlanan
çıktıların `çıktılar.txt` adlı dosyaya, hata mesajlarının ise `hatalar.txt` adlı
dosyaya yönlendirildiğini göreceksiniz. 
        
sys.stdin
==========

Python'da üç adet standart konum bulunur:

    #. Standart çıktı konumu - `stdout`
    #. Standart hata konumu - `stderr`
    #. Standart girdi konumu - `stdin`
    
İlk ikisini zaten görmüştük. Üçüncüsünü de şimdi ele alacağız. 

Bildiğiniz gibi Python'da kullanıcıdan veri almak için ``input()`` fonksiyonunu
kullanıyoruz::
    
    sayı = input('Lütfen bir sayı girin: ')
    
Bu fonksiyonun görevi, standart girdi konumuna girilen verileri okumaktır.
Python'daki standart girdi konumu (genellikle) komut satırı olduğu için,
``input()`` fonksiyonu verileri komut satırından okur.

Python'da standart girdi konumunu tutan değişken `sys.stdin`'dir. Dolayısıyla
eğer isterseniz, verileri kullanıcıdan ``input()`` fonksiyonu yerine doğrudan
`sys.stdin` niteliği aracılığıyla da alabilirsiniz::
    
    >>> import sys
    >>> sys.stdin.read()
    
Bu komutları verdiğinizde, komut satırı sizden veri almaya hazır hale gelir. Bu
şekilde istediğiniz kadar veriyi komut satırına girebilirsiniz. Veri girişini
durdurmak istediğinizde ise Windows'ta `CTRL+C`, GNU/Linux'ta ise `CTRL+D`
tuşlarına basmanız gerekir. Bu şekilde komut satırını terkettiğinizde, girmiş
olduğunuz değerler bir karakter dizisi olarak ekrana basılacaktır.

`sys.stdin` niteliği, bize veri okumak için üç farklı fonksiyon sunar:

    #. ``sys.stdin.read()``
    #. ``sys.stdin.readline()``
    #. ``sys.stdin.readlines()``
    
``read()`` fonksiyonu birden fazla satır içeren verilerin girilmesine müsaade
eder ve çıktı olarak bir karakter dizisi verir::
     
    >>> sys.stdin.read()
    (Girdi)
    Fırat
    Özgül
    Adana
    (Çıktı)
    'Fırat\nÖzgül\nAdana\n'         
     
``readline()`` fonksiyonu tek bir satır içeren verilerin girilmesine müsaade
eder ve çıktı olarak bir karakter dizisi verir::

    >>> sys.stdin.readline()
    (Girdi)
    Fırat
    (Çıktı)
    'Fırat\n'
 
``readlines()`` fonksiyonu birden fazla satır içeren verilerin girilmesine
müsaade eder ve çıktı olarak bir liste verir::
    
    >>> sys.stdin.readlines()
    (Girdi)
    Fırat
    Özgül
    Adana
    (Çıktı)
    ['Fırat\n', 'Özgül\n', 'Adana\n']
    
Gelin isterseniz `sys.stdin` niteliğinin nasıl kullanılabileceğine ilişkin
birkaç örnek verelim::
    
    import sys
    
    with open('kayıtlar.txt', 'w') as kayıtlar:
        while True:
            satırlar = sys.stdin.readline()
            if satırlar.strip() == ':q':
                break
            else:
                kayıtlar.write(satırlar)
    
Burada `kayıtlar.txt` adlı bir dosya oluşturduk öncelikle. Daha sonra da
``readline()`` fonksiyonu aracılığıyla kullanıcıdan aldığımız bütün verileri bu
dosyaya yazdık. Kullanıcının programdan çıkabilmesini sağlamak için de ':q' tuş
kombinasyonunu ayarladık. Böylece komut satırından çalışan basit bir metin
düzenleyici yazmış olduk!

Tıpkı `sys.stdout` ve `sys.stderr` konumlarını değiştirdiğimiz gibi,
`sys.stdin` konumunu da değiştirebiliriz. Böylece verileri komut satırı
aracılığıyla değil, mesela bir dosya aracılığıyla alabiliriz.

Aşağıdaki örneği dikkatlice inceleyin::
            
    import sys
    
    f = open('oku.txt')
    
    sys.stdin = f
        
    while True:
        satırlar = sys.stdin.readline()
        if satırlar.strip() == ':q':
            break
        else:
            sys.stdout.write(satırlar)
            
Bu kodları yazdıktan sonra, bu kodların bulunduğu dizinde `oku.txt` adlı bir
dosya oluşturun. Ardından programınızı çalıştırın. Programınız şu anda sizden
veri girmenizi bekliyor. Verileri `oku.txt` adlı dosyaya gireceksiniz.

`oku.txt` adlı dosyayı açıp bir şeyler yazın. Veri girerken dosyayı her
kaydedişinizde dosya içindeki verilerin komut satırına düştüğünü göreceksiniz.
Veri girişini tamamladıktan sonra dosyanın en son satırına ':q' yazıp dosyayı
kaydettiğiniz anda da programınız kapanacaktır.
    



