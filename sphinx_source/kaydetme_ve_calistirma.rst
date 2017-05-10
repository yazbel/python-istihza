.. meta:: :description: Bu bölümde, Python programlarını temel olarak nasıl
           kaydedeceğimizi ve bu programları nasıl çalıştıracağımızı öğreneceğiz.
          :keywords: Python, path, yol, Windows, GNU/Linux, Python programlarını
           çalıştırmak, kaydetmek

.. highlight:: py3

************************************
Programları Kaydetme ve Çalıştırma 
************************************

Bu noktaya kadar bütün işlerimizi Python'ın etkileşimli kabuğu üzerinden
hallettik. Her ne kadar etkileşimli kabuk son derece kullanışlı bir ortam da
olsa, bizim asıl çalışma alanımız değildir. Daha önce de dediğimiz gibi,
etkileşimli kabuğu genellikle ufak tefek Python kodlarını test etmek için
kullanacağız. Ama asıl programlarımızı tabii ki etkileşimli kabuğa değil,
program dosyasına yazacağız.

Ne dedik? Özellikle küçük kod parçaları yazıp bunları denemek için etkileşimli
kabuk mükemmel bir ortamdır. Ancak kodlar çoğalıp büyümeye başlayınca bu ortam
yetersiz gelmeye başlayacaktır. Üstelik tabii ki yazdığınız kodları bir yere
kaydedip saklamak isteyeceksiniz. İşte burada metin düzenleyiciler devreye
girecek.

Python kodlarını yazmak için istediğiniz herhangi bir metin düzenleyiciyi
kullanabilirsiniz. Hatta Notepad bile olur. Ancak Python kodlarını ayırt edip
renklendirebilen bir metin düzenleyici ile yola çıkmak her bakımdan hayatınızı
kolaylaştıracaktır.

.. note:: Python kodlarınızı yazmak için Microsoft Word veya OpenOffice.Org
 OOWriter gibi, belgeleri ikili (*binary*) düzende kaydeden programlar uygun
 değildir. Kullanacağınız metin düzenleyici, belgelerinizi düz metin (*plain
 text*) biçiminde kaydedebilmeli.

Biz bu bölümde farklı işletim sistemlerinde, metin düzenleyici kullanılarak
Python programlarının nasıl yazılacağını ve bunların nasıl çalıştırılacağını tek
tek inceleyeceğiz.

Daha önce de söylediğimiz gibi, hangi işletim sistemini kullanıyor olursanız
olun, hem Windows hem de GNU/Linux başlığı altında yazılanları okumalısınız.

Dilerseniz önce GNU/Linux ile başlayalım:

GNU/Linux 
*********

Eğer kullandığınız sistem GNU/Linux'ta Unity veya GNOME masaüstü ortamı ise
başlangıç düzeyi için Gedit adlı metin düzenleyici yeterli olacaktır.

Eğer kullandığınız sistem GNU/Linux'ta KDE masaüstü ortamı ise Kwrite veya Kate
adlı metin düzenleyicilerden herhangi birini kullanabilirsiniz. Şu aşamada
kullanım kolaylığı ve sadeliği nedeniyle Kwrite önerilebilir.

İşe yeni bir Gedit belgesi açarak başlayalım. Yeni bir Gedit belgesi açmanın en
kolay yolu `Alt+F2` tuşlarına bastıktan sonra çıkan ekranda::

    gedit 
    
yazıp `Enter` düğmesine basmaktır.

Eğer Gedit yerine mesela Kwrite kullanıyorsanız, yeni bir Kwrite belgesi
oluşturmak için `Alt+F2` tuşlarına bastıktan sonra::

    kwrite 
    
komutunu vermelisiniz. Elbette kullanacağınız metin düzenleyiciye, komut vermek
yerine, dağıtımınızın menüleri aracılığıyla da ulaşabilirsiniz.

Python kodlarımızı, karşımıza çıkan bu boş metin dosyasına yazıp kaydedeceğiz.

Aslında kodları metin dosyasına yazmakla etkileşimli kabuğa yazmak arasında çok
fazla fark yoktur. Dilerseniz hemen bir örnek vererek ne demek istediğimizi
anlatmaya çalışalım:

\1. Boş bir Gedit ya da Kwrite belgesi açıyoruz ve bu belgeye şu kodları
eksiksiz bir şekilde yazıyoruz:

::

    tarih = "02.01.2012" 
    gün = "Pazartesi" 
    vakit = "öğleden sonra"

    print(tarih, gün, vakit, "buluşalım", end=".\n")

\2. Bu kodları yazıp bitirdikten sonra dosyayı masaüstüne `randevu.py` adıyla
kaydedelim.

\3. Sonra işletim sistemimize uygun bir şekilde komut satırına ulaşalım.

\4. Ardından komut satırı üzerinden masaüstüne gelelim. (Bunun nasıl
yapılacağını hatırlıyorsunuz, değil mi?)

\5. Son olarak şu komutla programımızı çalıştıralım:

::

    python3 randevu.py

Şöyle bir çıktı almış olmalıyız::

    02.01.2012 Pazartesi öğleden sonra buluşalım.

Eğer bu çıktı yerine bir hata mesajı alıyorsanız bunun birkaç farklı sebebi
olabilir:

#. Kodlarda yazım hatası yapmış olabilirsiniz. Bu ihtimali bertaraf etmek için
   yukarıdaki kodlarla kendi yazdığınız kodları dikkatlice karşılaştırın.

#. Kodlarınızı kaydettiğiniz `randevu.py` adlı dosyanın adını yanlış yazmış
   olabilirsiniz. Dolayısıyla ``python3 randevu.py`` komutu, var olmayan bir dosyaya
   atıfta bulunuyor olabilir.

#. ``python3 randevu.py`` komutunu verdiğiniz dizin konumu ile `randevu.py`
   dosyasının bulunduğu dizin konumu birbirinden farklı olabilir. Yani siz
   `randevu.py` dosyasını masaüstüne kaydetmişsinizdir, ama ``python3 randevu.py``
   komutunu yanlışlıkla başka bir dizin altında veriyor olabilirsiniz. Bu ihtimali
   ortadan kaldırmak için, önceki derslerde öğrendiğimiz yöntemleri kullanarak
   hangi dizin altında bulunduğunuzu kontrol edin. O anda içinde bulunduğunuz
   dizinin içeriğini listeleyerek, `randevu.py` dosyasının orada görünüp
   görünmediğini kontrol edebilirsiniz. Eğer program dosyanız bu listede
   görünmüyorsa, elbette ``python3 randevu.py`` komutu çalışmayacaktır.

#. Geçen derslerde anlattığımız şekilde Python3'ü kaynaktan `root` haklarıyla
   derlemenize rağmen, derleme sonrasında `/usr/bin/` dizini altına `python3` adlı
   bir sembolik bağ oluşturmadığınız için ``python3`` komutu çalışmıyor olabilir.

#. Eğer Python3'ü yetkisiz kullanıcı olarak derlediyseniz, `$HOME/python/bin/`
   dizini altında hem ``python3`` adlı bir sembolik bağ oluşturmuş, hem de
   `$HOME/python/bin/` dizinini YOL'a (*PATH*) eklemiş olmanız gerekirken bunları
   yapmamış olabilirsiniz.

#. Asla unutmayın, Python'ın etkileşimli kabuğunu başlatmak için hangi komutu
   kullanıyorsanız, `randevu.py` dosyasını çalıştırmak için de aynı komutu
   kullanacaksınız. Yani eğer Python'ın etkileşimli kabuğunu |pycommand| gibi bir
   komutla çalıştırıyorsanız, programınızı da |pycommand| ``randevu.py`` şeklinde
   çalıştırmanız gerekir. Aynı şekilde, eğer etkileşimli kabuğu mesela ``python``
   (veya ``py3``) gibi bir komutla çalıştırıyorsanız, programınızı da ``python
   randevu.py`` (veya ``py3 randevu.py``) şeklinde çalıştırmalısınız. Neticede
   etkileşimli kabuğu çalıştırırken de, bir program dosyası çalıştırırken de
   aslında temel olarak Python programlama dilini çalıştırmış oluyorsunuz. Python
   programını çalıştırırken bir dosya adı belirtmezseniz, yani Python'ı başlatan
   komutu tek başına kullanırsanız etkileşimli kabuk çalışmaya başlar. Ama eğer
   Python'ı başlatan komutla birlikte bir program dosyası ismi de belirtirseniz, o
   belirttiğiniz program dosyası çalışmaya başlar.

Kodlarınızı düzgün bir şekilde çalıştırabildiğinizi varsayarak yolumuza devam
edelim...

Gördüğünüz gibi, kod dosyamızı çalıştırmak için ``python3`` komutundan
yararlanıyoruz. Bu arada tekrar etmekte fayda var: Python'ın etkileşimli
kabuğunu çalıştırmak için hangi komutu kullanıyorsanız, dosyaya kaydettiğiniz
programlarınızı çalıştırmak için de aynı komutu kullanacaksınız. 

Gelelim Windows kullanıcılarına...

Windows  
********

Daha önce de söylediğimiz gibi, Python kodlarımızı yazmak için istediğimiz bir
metin düzenleyiciyi kullanabiliriz. Hatta Notepad'i bile kullansak olur. Ancak
Notepad'den biraz daha gelişmiş bir metin düzenleyici ile başlamak işinizi
kolaylaştıracaktır.

Python programlama dilini öğrenmeye yeni başlayan Windows kullanıcıları için en
uygun metin düzenleyici IDLE'dır. *Başlat > Tüm Programlar > Python*\
|major-noformat| *> IDLE (Python GUI)* yolunu takip ederek IDLE'a
ulaşabilirsiniz.

IDLE'ı açtığınızda şöyle bir ekranla karşılaşacaksınız:

    .. image:: ../images/idlegui/idle_main.png 
        :align: center 
        :width: 65%

Aslında bu ekran size bir yerlerden tanıdık geliyor olmalı. Dikkat ederseniz
beyaz ekranın en sonunda bordo renkli bir `>>>` işareti var. Evet, tahmin
ettiğiniz gibi, burası aslında Python'ın etkileşimli kabuğudur. Yani o siyah
etkileşimli kabuk ekranında ne yapabilirseniz burada da aynı şeyi
yapabilirsiniz. Dilerseniz kendi kendinize bazı denemeler yapın. Ama şu anda biz
IDLE'ın bu özelliğini değil, metin düzenleyici olma özelliğini kullanacağız. O
yüzden yolumuza devam ediyoruz.

.. note:: Dediğimiz gibi, yukarıda görünen ekran aslında Python'ın
          etkileşimli kabuğudur. Dolayısıyla biraz sonra göstereceğimiz kodları buraya
          yazmayacağız. Python programlama diline yeni başlayanların en sık yaptığı
          hatalardan biri de, kaydetmek istedikleri kodları yukarıda görünen ekrana
          yazmaya çalışmalarıdır. Unutmayın, Python'ın etkileşimli kabuğunda ne
          yapabiliyorsanız, IDLE'ı açtığınızda ilk karşınıza çıkan ekranda da onu
          yapabilirsiniz. Python'ın etkileşimli kabuğunda yazdığınız kodlar etkileşimli
          kabuğu kapattığınızda nasıl kayboluyorsa, yukarıdaki ekrana yazdığınız kodlar da
          IDLE'ı kapattığınızda kaybolur...

Bir önceki ekranda sol üst köşede *File* [Dosya] menüsü görüyorsunuz. Oraya
tıklayın ve menü içindeki *New Window* [Yeni Pencere] düğmesine basın. Şöyle bir
ekranla karşılaşacaksınız:

    .. image:: ../images/idlegui/idle_new.png 
        :align: center 
        :width: 65%

İşte Python kodlarımızı bu beyaz ekrana yazacağız. Şimdi bu ekrana şu satırları
yazalım::

    tarih = "02.01.2012" 
    gün = "Pazartesi" 
    vakit = "öğleden sonra"

    print(tarih, gün, vakit, "buluşalım", end=".\n")

Bu noktadan sonra yapmamız gereken şey dosyamızı kaydetmek olacak. Bunun için
*File > Save as* yolunu takip ederek programımızı masaüstüne `randevu.py` adıyla
kaydediyoruz.

Şu anda programımızı yazdık ve kaydettik. Artık programımızı çalıştırabiliriz.
Bunun için IDLE'da *Run > Run Module* yolunu takip etmeniz veya kısaca `F5`
tuşuna basmanız yeterli olacaktır. Bu iki yöntemden birini kullanarak
programınızı çalıştırdığınızda şöyle bir çıktı elde edeceksiniz::
    
    02.01.2012 Pazartesi öğleden sonra buluşalım. 

Tebrikler! İlk Python programınızı yazıp çalıştırdınız... Eğer
çalıştıramadıysanız veya yukarıdaki çıktı yerine bir hata mesajı aldıysanız
muhtemelen kodları yazarken yazım hatası yapmışsınızdır. Kendi yazdığınız
kodları buradaki kodlarla dikkatlice karşılaştırıp tekrar deneyin.

Şimdi gelin isterseniz yukarıda yazdığımız kodları şöyle bir kısaca inceleyelim.

Programımızda üç farklı değişken tanımladığımıza dikkat edin. Bu değişkenler
`tarih`, `gün` ve `vakit` adlı değişkenlerdir. Daha sonra bu değişkenleri
birbiriyle birleştiriyoruz. Bunun için ``print()`` fonksiyonundan nasıl
yararlandığımızı görüyorsunuz. Ayrıca ``print()`` fonksiyonunu kullanış
biçimimize de dikkat edin. Buradaki `end` parametresinin anlamını ve bunun ne
işe yaradığını artık gayet iyi biliyorsunuz. `end` parametresi yardımıyla
cümlenin en sonuna bir adet nokta yerleştirip, `\\n` adlı kaçış dizisi
yardımıyla da bir alt satıra geçiyoruz.

Böylece basit bir Python programının temel olarak nasıl yazılıp bir dosyaya
kaydedileceğini ve bu programın nasıl çalıştırılacağını öğrenmiş olduk.