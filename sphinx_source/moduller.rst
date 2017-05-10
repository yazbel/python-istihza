.. meta::
   :description: Bu bölümde modüller konusunu inceleyeceğiz. 
   :keywords: python, modül, import

.. highlight:: py3

***************
Modüller
***************

Bu bölümde, geçen derste ayrıntılı olarak incelediğimiz 'Fonksiyonlar' kadar
önemli bir konuyu ele alacağız. Bu önemli konunun adı 'modüller'.

Biz şimdiye kadar modül konusunu hiç ayrıntılı olarak ele almamış olsak da
esasında siz modül kavramına büsbütün yabancı sayılmazsınız. Zira biz önceki
derslerimizde zaman zaman modüllerden söz etmiş, hatta yeri geldiğinde bunları
kodlarımız içinde kullanmaktan da çekinmemiştik.

Bu konuya gelene kadar, çeşitli bölümlerde şu modüllerden bahsettiğimizi
hatırlıyorsunuzdur:

    - sys
    - os
    - keyword
    - random
    - unicodedata
    - locale

İşte şimdi, daha önce farklı bölümlerde şöyle bir temas edip geçtiğimiz modüller
konusunu bu bölümde derinlemesine incelemeye çalışacağız.

Modül Nedir?
*************

Dediğimiz gibi, bu bölümde Python'daki en önemli konulardan biri olan
modüllerden söz edeceğiz. Ancak modülleri kullanabilmek için elbette öncelikle
'modül' denen şeyin ne olduğunu iyice bir anlamamız gerekiyor. Peki, nedir bu
modül denen şey?

Bu soruyu, şimdiye kadar gördüğümüz modüllere bakarak cevaplayacak olursak,
modüllerin, bazı işlevleri kolaylıkla yerine getirmemizi sağlayan birtakım
fonksiyonları ve nitelikleri içinde barındıran araçlar olduğunu söyleyebiliriz.

Mesela 'Kümeler ve Dondurulmuş Kümeler' adlı bölümde ``random`` adlı bir modüle
değindiğimizi hatırlıyor olmalısınız. Orada bu modülle ilgili şöyle bir örnek
vermiştik::
    
    liste = [random.randint(0, 10000) for i in range(1000)]
    
Bu örnekte, ``random`` adlı modülün içindeki ``randint()`` adlı faydalı bir
fonksiyondan yararlanarak 0 ile 10.000 sayıları arasında 1000 adet rastgele sayı
içeren bir liste oluşturmuştuk. Dolayısıyla, yukarıdaki tanımda da belirttiğimiz
gibi, bir modül olan ``random``, örnekte bahsettiğimiz işlevi kolaylıkla yerine
getirmemizi sağlayan bir fonksiyon barındırıyor. Biz de bu fonksiyonu kullanarak
amacımızı rahatlıkla yerine getirebiliyoruz. 

``random`` modülünün dışında, önceki derslerimizde şöyle bir değinip geçtiğimiz,
``sys``, ``os`` ve ``locale`` gibi modüllerin de çeşitli görevleri kolayca
yerine getirmemizi sağlayan birtakım araçlar barındırdığını görmüştük.

İşin doğrusu, modül denen şey Python programlama dilinin bel kemiğidir. Eğer
modüller olmasaydı, Python programlama dili hem çok kullanışsız bir dil olurdu,
hem de modüller sayesinde çok kolay bir şekilde üstesinden gelebildiğimiz
zorluklar için her defasında kendimiz yeniden bir çözüm icat etmek zorunda
kalırdık.

Belki bu iddialı laf size şu anda pek anlamlı gelmemiş olabilir. Şu ana kadar
modüllerle ilgili öğrendikleriniz, henüz zihninizde bu lafın iddiasını teyit
etmiyor olabilir. Ama modüllerin neden bu kadar önemli olduğunu birazdan çok
daha net bir şekilde anlayacaksınız. Şimdilik okumaya devam edin.

Hatırlarsanız bir önceki bölümde Python'daki fonksiyonlardan bahsetmiştik. Yine
hatırlarsanız o bölümde pek çok örnek fonksiyon da tanımlamıştık. Mesela
``kayıt_oluştur()`` adlı şöyle bir fonksiyon tanımladığımızı hatırlıyor
olmalısınız::
    
    def kayıt_oluştur(isim, soyisim, işsis, şehir):
        print("-"*30)
        
        print("isim           : ", isim)
        print("soyisim        : ", soyisim)
        print("işletim sistemi: ", işsis)
        print("şehir          : ", şehir)
        
        print("-"*30)
    
Bu fonksiyonu bir kez tanımladıktan sonra, bu fonksiyonu aynı program içinde
istediğimiz kadar kullanabiliyoruz. Yani ``kayıt_oluştur`` adlı bir fonksiyon
tanımlamış olmamız sayesinde, bu fonksiyonun gövdesinde belirttiğimiz işlemleri
her defasında tekrar tekrar yapmak zorunda kalmıyoruz; bütün bu işlemleri tek
bir 'kayıt_oluştur' ismine atamış olduğumuz için, bu fonksiyonun bize sunduğu
işleve ihtiyaç duyduğumuz her yerde bu fonksiyonu kullanabiliyoruz. Örneğin::
    
    kayıt_oluştur('Fırat', 'Özgül', 'Debian', 'Arsuz')
    
Ya da::

    kayıt_oluştur('Zerrin', 'Söz', 'Ubuntu', 'Bolvadin')  
    
Eğer yukarıdaki işlevselliği bir fonksiyon olarak tanımlamış olmasaydık,
``kayıt_oluştur('Fırat', 'Özgül', 'Debian', 'Arsuz')`` kodunun verdiği çıktıyı
elde etmek için şu kodları yazmak zorunda kalacaktık::
    
        print("-"*30)
        
        print("isim           : ", "Fırat")
        print("soyisim        : ", "Özgül")
        print("işletim sistemi: ", "Debian")
        print("şehir          : ", "Arsuz")
        
        print("-"*30)
        
Burada isim, soyisim, işletim sistemi ve şehir bilgileri değiştiğinde de her
defasında aynı şeyleri uzun uzadıya tekrar tekrar yazmamız gerekecekti::
    
        print("-"*30)
        
        print("isim           : ", "Zerrin")
        print("soyisim        : ", "Söz")
        print("işletim sistemi: ", "Ubuntu")
        print("şehir          : ", "Bolvadin")
        
        print("-"*30)    
    
İşte modüller de buna benzer bir vazife görür. Yani Python'ın fonksiyon sistemi
nasıl bize bir işlevselliği **aynı dosya içinde** tekrar tekrar kullanma imkanı
veriyorsa, modül sistemi de bir fonksiyonu **farklı dosyalar ve programlar
içinde** tekrar tekrar kullanma imkanı verir.

Dolayısıyla, eğer modül sistemi olmasaydı, biz bir kez yazdığımız (veya başka
bir Python programcısı tarafından yazılmış) ``kayıt_oluştur()`` fonksiyonunu
başka bir programda da kullanmak istediğimizde, bu fonksiyonu alıp her defasında
yeni programa elle kopyalamak zorunda kalırdık. Ama modül sistemi sayesinde, bir
program içinde bulunan fonksiyonları (ve diğer nitelikleri) başka Python
programları içine 'aktarabiliyoruz'. Böylece bir Python programındaki (veya
modülündeki) işlevsellikten, başka bir Python programında da yararlanabiliyoruz.
Dolayısıyla modüller sayesinde, bir kez yazdığımız kodları pek çok farklı
program içinde kullanma imkanı elde ediyoruz. Bu da bizim;
    
    * Daha az kod yazmamızı,
    * Bir kez yazdığımız kodları tekrar tekrar kullanabilmemizi,
    * Daha düzenli, daha derli toplu bir şekilde çalışabilmemizi 

sağlıyor.

İşte bu bölümde, modüllerin bütün bu işlevleri nasıl yerine getirdiğini, modül
denen şeyden nasıl faydalanabileceğimizi ve modüllerin neden bu kadar önemli
olduğunu öğreneceğiz. Dilerseniz lafı daha fazla dolandırmadan modüller konusuna
hızlı bir giriş yapalım.

Hazır Modüller
****************

Hatırlarsanız, Python'da iki farklı fonksiyon türü olduğundan söz etmiştik:

    #. Kendi tanımladığımız fonksiyonlar
    #. Gömülü ('built-in') fonksiyonlar
    
Aynı şekilde modüller de iki farklı başlık altında incelenebilir:

    #. Kendi tanımladığımız modüller
    #. Hazır modüller
    
Biz burada öncelikle hazır modülleri ele alacağız. Bu şekilde modül kavramını
iyice anladıktan sonra da kendi modüllerimizi nasıl yazacağımızı öğreneceğiz.

Hazır modüller, Python geliştiricilerinin veya bizim dışımızdaki Python
programcılarının yazıp hizmetimize sunduğu modüllerdir.

Hazır modüller de kendi içinde ikiye ayrılabilir:

    #. Standart Kütüphane Modülleri
    #. Üçüncü Şahıs Modülleri
    
Standart Kütüphane Modülleri, doğrudan Python geliştiricileri tarafından yazılıp
dile kaynaştırılmış modüllerdir. Bu yönüyle bu modüller daha önce öğrendiğimiz
gömülü fonksiyonlara çok benzer. Tıpkı gömülü fonksiyonlarda olduğu gibi,
Standart Kütüphane Modülleri de her an emrimize amadedir. Biz bunları
istediğimiz her an, herhangi bir ek yazılım kurmak zorunda kalmadan, kendi
programlarımız içinde kullanabiliriz.

.. seealso:: Python'ın Standart Kütüphanesi içinde hangi modüllerin olduğunu
    https://docs.python.org/3/library/ adresinden inceleyebilirsiniz.
    
Standart Kütüphane içinde, Python ile programlama yaparken işlerinizi bir hayli
kolaylaştıracak pek çok modül bulacaksınız.

Başta da söylediğimiz gibi, biz bu bölüme gelinceye kadar üstünkörü de olsa
modüllerden söz etmiştik. Örneğin önceki derslerimizde andığımız ``sys``,
``os``, ``random`` ve benzeri modüller hep birer Standart Kütüphane modülüdür.
Dolayısıyla bu modüllerin sunduğu işlevsellikten kendi programlarımızda
istediğimiz her an yararlanabiliriz.

Modüllerin İçe Aktarılması
***************************

Python'da herhangi bir modülü kullanabilmek için öncelikle onu 'içe aktarmamız'
gerekir. İçe aktarmak, bir modül içindeki fonksiyon ve nitelikleri başka bir
program (veya ortam) içinden kullanılabilir hale getirmek demektir. İsterseniz
bu soyut tanımlamayı bir örnek ile somutlaştıralım. Mesela, bir Standart
Kütüphane modülü olduğunu öğrendiğimiz ve önceki derslerimizde de değindiğimiz
``os`` adlı modülü içe aktaralım. Bunun için öncelikle etkileşimli kabuğu
çalıştıralım ve şu komutu verelim::
    
    >>> import os
    
Böylece ``os`` adlı modülü içe aktarmış, yani bu modül içindeki fonksiyon ve
nitelikleri kullanılabilir hale getirmiş olduk. 

Hatırlarsanız 'modül' kavramını tanımlarken, bunların bize birtakım yararlı
fonksiyonlar ve nitelikler sunan araçlar olduğunu söylemiştik. İşte, mesela bu
``os`` modülünün bize hangi yararlı fonksiyonları ve nitelikleri sunduğunu
öğrenmek için ``dir()`` fonksiyonunu kullanabiliriz::
    
    >>> dir(os)
    
Gördüğünüz gibi bu modül pek çok fonksiyon ve nitelik barındırıyor. 

Bu modüle adını veren ``os`` kelimesi *operating system* (işletim sistemi)
ifadesinin kısaltmasıdır. Bu modül, kullandığımız işletim sistemine ilişkin
işlemler yapabilmemiz için bize çeşitli fonksiyonlar ve nitelikler sunar. Hemen
bir örnek verelim.

Diyelim ki bir program yazdınız. Ancak yazdığınız bu programın yalnızca Windows
işletim sisteminde çalışmasını istiyorsunuz. Buna göre, eğer programınız Windows
işletim sistemi kurulu bir bilgisayarda çalıştırılırsa programınızın normal bir
şekilde başlamasını, ama eğer Windows dışı bir işletim sisteminde çalıştırılırsa
da kullanıcıya bir uyarı mesajı verilmesini istiyorsunuz.

İşte bunun için ``os`` modülünden yararlanabilirsiniz. Şimdi ``dir(os)``
komutuyla elde ettiğimiz listeye bakalım. Orada `name` adlı bir nitelik olduğunu
göreceksiniz. Bu nitelik, bize kodlarımızın hangi işletim sisteminde çalıştığını
gösterir. Dolayısıyla da yukarıda tarif ettiğimiz iş için gayet uygun bir
araçtır. 

Önceden ``import os`` komutuyla ``os`` modülünü içe aktarmış olduğumuzu
varsayarsak, modülün bu niteliğini şöyle kullanıyoruz::
    
    >>> os.name
    
    'posix'
    
``os`` adlı modülün içindeki `name` niteliğine nasıl eriştiğimize çok dikkat
edin. Önce modülümüzün adı olan 'os'u yazıyoruz. Ardından bir nokta işareti
koyup, ihtiyacımız olan niteliğin adını belirtiyoruz. Yani şöyle bir formül
takip ediyoruz::

    modül_adı.fonksiyon_veya_nitelik
    
``os.name`` komutu, kullandığınız işletim sistemine bağlı olarak farklı çıktılar
verir. Eğer bu komutu bir GNU/Linux dağıtımında veya bir Mac bilgisayarda
verirsek yukarıdaki gibi 'posix' çıktısı alırız. Ama eğer aynı komutu Windows'ta
verirsek 'nt' çıktısı alırız. Dolayısıyla ``os`` modülünün `name` niteliğini
kullanarak, yazdığımız bir programın hangi işletim sisteminde çalıştığını
denetleyebiliriz::
    
    >>> if os.name != 'nt':
    ...     print('Kusura bakmayın! Bu programı yalnızca', 
    ...     'Windows\'ta kullanabilirsiniz!')
    ... else:
    ...     print('Hoşgeldin Windows kullanıcısı!')

Etkileşimli kabukta yazdığımız bu programı gelin bir de bir metin dosyasına
kaydedelim. Zira biz henüz modülleri öğrenme aşamasında olduğumuz için şimdilik
bunları etkileşimli kabukta test ediyor olsak da, gerçek hayatta programlarımızı
etkileşimli kabuğa değil, program dosyaları içine yazacağız.

Yukarıdaki kodları bir dosyaya kaydettiğimizde programımız şöyle görünür::
    
    import os
    
    if os.name != 'nt':
        print('Kusura bakmayın! Bu programı yalnızca',
              'Windows\'ta kullanabilirsiniz!')
    else:
        print('Hoşgeldin Windows kullanıcısı!')
        
Gördüğünüz gibi, programımızı kaydederken, programımızın en başına ``import os``
komutunu yazarak öncelikle ilgili modülü içe aktarıyoruz. Python'da modüller
genellikle programın en başında içe aktarılır. Ama bu bir zorunluluk değildir.
Modülleri programın istediğiniz her yerinde içe aktarabilirsiniz (bununla ilgili
bir istisnadan biraz sonra söz edeceğiz).

Modül içe aktarmaya ilişkin en önemli kural, modüle ait bir nitelik veya
fonksiyonun kullanılmasından önce modülün içe aktarılmış olması gerekliliğidir.
Yani mesela yukarıdaki programda ``os`` modülü içindeki `name` niteliğini
kullanmadan önce ``os`` modülünü içe aktarmış olmamız gerekir. Eğer Python, ``if
os.name != 'nt':`` satırından önce herhangi bir yerde ``import os`` gibi bir
komutla ``os`` modülünün içe aktarıldığını göremezse hata verecektir.

Bu programı yukarıdaki gibi bir dosyaya kaydettikten sonra bunu herhangi bir
Python programı gibi çalıştırabilirsiniz. 
    
Eğer bu programı Windows dışındaki bir işletim sisteminde çalıştırırsanız şu
çıktıyı alırsınız::
    
    Kusura bakmayın! Bu programı yalnızca 
    Windows'ta kullanabilirsiniz!
    
Ama eğer bu program Windows işletim sisteminde çalıştırılırsa şu çıktıyı verir::
    
    Hoşgeldin Windows kullanıcısı!
    
Böylece modül içindeki bir niteliğe erişmiş olduk. Yalnız burada asla
unutmamamız gereken şey, öncelikle kullanacağımız modülü ``import modül_adı``
komutuyla içe aktarmak olacaktır. Modülü içe aktarmazsak tabii ki o modüldeki
fonksiyon veya niteliklere de erişemeyiz. (Sık yapılan bir hata olduğu için,
bunu tekrar tekrar vurguluyoruz...)

Bu arada bir modülü, her etkileşimli kabuk oturumunda yalnızca bir kez içe
aktarmak yeterlidir. Yani siz etkileşimli kabuğu çalıştırdıktan sonra bir kez
``import os`` komutuyla modülü içe aktardıktan sonra, o etkileşimli kabuk
oturumunu kapatana kadar, aynı modülü tekrar içe aktarmak zorunda kalmadan bu
modülün içeriğini kullanabilirsiniz.

Aynı şekilde, eğer bu kodları etkileşimli kabuğa değil de bir program dosyasına
yazıyorsanız, ``import os`` komutunu dosyanın başına bir kez yazdıktan sonra
aynı modülü programın ilerleyen kısımlarında tekrar içe aktarmak zorunda
kalmadan, o modülünün içeriğinden yararlanabilirsiniz.
    
Gördüğünüz gibi, bir Standart Kütüphane Modülü olan ``os`` bize `name` adlı çok
kullanışlı bir nitelik sunuyor. Eğer ``os`` modülü olmasaydı, `name` adlı
niteliğin sunduğu işlevi kendimiz icat etmek zorunda kalırdık. 

Başka bir örnek daha verelim...

Diyelim ki yine bir program yazdınız. Programınızın çalışması için, programınızı
kullanan kişinin bilgisayarında birtakım dizinler oluşturmanız gerekiyor. İşte
bu iş için de ``os`` modülünden yararlanabilirsiniz.
    
Bu modül içindeki ``makedirs()`` fonksiyonunu kullanarak, o anda içinde
bulunduğunuz dizinde yeni bir dizin oluşturabilirsiniz::
    
    >>> os.makedirs('DATA')
    
Bu komutu verdikten sonra, o anda altında bulunduğunuz dizinde `DATA` adlı bir
dizin oluşacaktır. Eğer o anda hangi dizin altında bulunduğunuzu öğrenmek
isterseniz de yine ``os`` modülünden faydalanabilirsiniz::
    
    >>> os.getcwd()
    
``os`` modülünün ``getcwd()`` fonksiyonu bize o anda hangi dizin altında
bulunduğumuzu gösterir. Bu komutun çıktısında hangi dizin adını görüyorsanız,
biraz önce ``makedirs()`` fonksiyonu ile oluşturduğunuz `DATA` dizini de o dizin
altında oluşmuştur...

Gördüğünüz gibi, bir çırpıda ``os`` modülünün birkaç özelliğinden birden
yararlandık. Daha önce de söylediğimiz gibi, eğer ``os`` modülü olmasaydı
yukarıda gerçekleştirdiğimiz bütün işlevleri kendiniz icat etmek zorunda
kalırdınız.

Böylece Python'daki modüllerin neye benzediğini ve nasıl kullanıldığını anlamış
olduk. Modüllerin faydalı araçlar olduğu konusunda sizleri ikna edebilmiş
olduğumuzu varsayarak bir sonraki bölüme geçelim.

Farklı İçe Aktarma Yöntemleri
=================================

Biz şimdiye kadar, modülleri ``import modül_adı`` şeklinde içe aktardık.
Esasında standart içe aktarma yöntemi de budur. Bir modülü bu şekilde içe
aktardığımız zaman, modül adını kullanarak, o modülün içeriğine erişebiliriz::
    
    >>> import sys
    >>> sys.version #Python'ın sürümünü verir
    
veya::
    
    >>> import os
    >>> os.name #İşletim sistemimizin adını verir
    
gibi...

Ancak Python'da bir modülü içe aktarmanın tek yöntemi bu değildir. Eğer istersek
modülleri daha farklı şekillerde de içe aktarabiliriz. 

Gelin şimdi bu alternatif modül aktarma biçimlerinin neler olduğunu görelim.

import modül_adı as farklı_isim
---------------------------------

Bazı koşullar, bir modülü kendi adıyla değil de başka bir isimle içe aktarmanızı
gerektirebilir. Ya da siz bir modülü kendi adı dışında bir adla içe aktarmanın
daha iyi bir fikir olduğunu düşünebilirsiniz. 

Peki ama ne tür koşullar bir modülü farklı bir adla içe aktarmamızı
gerektirebilir veya biz hangi sebeple bir modülü farklı adla içe aktarmayı
isteyebiliriz?

Bu soruların cevabını verebilmek için, gelin isterseniz ``subprocess`` adlı bir
Standart Kütüphane modülünden yararlanalım. Hem bu vesileyle yeni bir modül de
öğrenmiş oluruz...

.. note:: ``subprocess`` modülü, harici komutları Python içinden
 çalıştırabilmemizi sağlayan oldukça faydalı bir araçtır. Bu modülü kullanarak
 Python programlarımız içinden, başka programları çalıştırabiliriz.
    
Bir modülün içindeki fonksiyon ve nitelikleri her kullanmak isteyişimizde, o
fonksiyon veya niteliğin başına modül adını da eklememiz gerektiğini artık gayet
iyi biliyorsunuz. Örneğin ``subprocess`` adlı modülü

::
    
    >>> import subprocess
    
komutuyla içe aktardıktan sonra, bu modül içindeki herhangi bir fonksiyon veya
niteliği kullanabilmenin birinci şartı, modül adını ilgili fonksiyon veya
niteliğin önüne getirmektir. Mesela biz ``subprocess`` modülünün ``call()`` adlı
fonksiyonunu kullanmak istersek, şöyle bir kod yazmamız gerekir::
    
    >>> subprocess.call('notepad.exe')
    
Bu şekilde 'Notepad' programını Python içinden çalıştırmış olduk. 

Ancak gördüğünüz gibi, 'subprocess' biraz uzun bir kelime. Bu modülü her
kullanmak isteyişinizde nitelik veya fonksiyon adının önüne bu uzun kelimeyi
getirmek bir süre sonra sıkıcı bir hal alabilir. Bu yüzden eğer isterseniz
modülü ``import subprocess`` şeklinde kendi adıyla değil de daha kısa bir adla
içe aktarmayı tercih edebilirsiniz::
    
    >>> import subprocess as sp
    
Burada şöyle bir formül uyguladığımıza dikkat edin::
    
    >>> import modül_adı as farklı_bir_isim
    
Böylece artık bu modülü yalnızca ``sp`` önekiyle kullanabilirsiniz::
    
    >>> sp.call('notepad.exe')
        
Örnek olması açısından başka bir modülü daha ele alalım. Modülümüzün adı
``webbrowser``.

.. note:: ``webbrowser`` modülü, bilgisayarımızda kurulu internet tarayıcısını
    kullanarak internet sitelerini açabilmemizi sağlar.
    
Tıpkı 'subprocess' gibi, 'webbrowser' kelimesi de, her defasında tekrar etmesi
sıkıcı olabilecek bir kelime. Dolayısıyla dilerseniz bu modülü ``import
webbrowser`` yerine farklı bir isimle içe aktarabilirsiniz. Örneğin::
    
    >>> import webbrowser as br
    
veya::
    
    >>> import webbrowser as web
    
Modülü hangi adla içe aktaracağınız tamamen size kalmış. Diyelim ki bu modülü
'web' adıyla içe aktardık. Artık bu modülün içindeki araçları ``web`` önekiyle
kullanabiliriz::
    
    >>> web.open('www.istihza.com')
    
.. warning:: Bazı GNU/Linux dağıtımlarında websitesi adresini 'http' önekiyle
    birlikte belirtmeniz gerekebilir. Örn. ``web.open('http://www.istihza.com')``.
    
Bu kod, bilgisayarımızdaki öntanımlı web tarayıcısı hangisiyse onu çalıştıracak
ve bizi, parantez içinde gösterilen web sayfasına götürecektir.

Eğer biz ``webbrowser`` modülünü doğrudan kendi adıyla içe aktarsaydık::
    
    >>> import webbrowser
    
Bu durumda yukarıdaki komutu şu şekilde vermek zorunda kalacaktık::
    
    >>> webbrowser.open('www.istihza.com')
    
Ama bu modülü daha kısa bir adla içe aktarmış olmamız sayesinde, bu modülü gayet
pratik bir şekilde kullanma imkanına kavuşuyoruz.

from modül_adı import isim1, isim2
--------------------------------------

Şimdiye kadar verdiğimiz örneklerden de gördüğünüz gibi, Standart Kütüphane
Modülleri'nin içinde çok sayıda fonksiyon ve nitelik bulunuyor. Mesela
``os`` modülünü ele alalım::
    
    >>> import os
    >>> dir(os)

Listede epey isim var...

Biz ``import os`` komutunu verdiğimizde, listedeki bütün o isimleri 'os' ismi
altında içe aktarmış oluyoruz. Bunun bir sakıncası yok, ancak yazdığımız
programlarda bu fonksiyon ve niteliklerin hepsine ihtiyaç duymayız. O yüzden,
eğer arzu ederseniz, ``import os`` gibi bir komutla bütün o isimleri içe
aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarmayı tercih de
edebilirsiniz. Mesela ``os`` modülünün yalnızca `name` niteliğini
kullanacaksanız, modülü şu şekilde içe aktarabilirsiniz::
    
    >>> from os import name
    
Bu şekilde ``os`` modülünden yalnızca `name` ismi içe aktarılmış olur ve
yalnızca bu ismi kullanabiliriz::
    
    >>> name
    
    'posix'
    
Bu durumda ``os.name`` komutu hata verecektir::
    
    >>> os.name
    
    NameError: name 'os' is not defined
    
Çünkü biz ``from os import name`` komutunu verdiğimizde, ``os`` modülünü değil,
bu modül içindeki bir nitelik olan `name`'i içe aktarmış oluyoruz. Dolayısıyla
``os`` ismini kullanamıyoruz.
    
Bu şekilde, aynı modül içinden birkaç farklı nitelik ve fonksiyonu da içe
aktarabilirsiniz::
    
    >>> from os import name, listdir, getcwd
    
Bu komutla ``os`` modülü içinden yalnızca ``name`` niteliğini, ``listdir()``
fonksiyonunu ve ``getcwd()`` fonksiyonunu aktarmış olduk::
    
    >>> listdir()
    
Bu fonksiyon, o anda içinde bulunduğumuz dizindeki dosyaları listeler.

`name` ve ``getcwd()`` isimlerinin görevini ise daha önce öğrenmiştik::

    >>> name
    
    'nt'
    
    >>> getcwd()

    'C:\\Documents and Settings\\fozgul\\'
    
Gelelim bir başka modül aktarma biçimine...

from modül_adı import isim as farklı_isim
-------------------------------------------

Bir modülü, kendi adından farklı bir adla nasıl içe aktarabileceğinizi
biliyorsunuz::
    
    import subprocess as sp
    
Bu şekilde ``subprocess`` modülünü ``sp`` adıyla içe aktarmış oluyoruz. 

Aynı şekilde, bir modül içinden belli nitelik ve fonksiyonları da nasıl içe
aktaracağınızı biliyorsunuz::
    
    from os import path, listdir
    
Bu şekilde ``os`` modülünden `path` niteliğini ve ``listdir()`` fonksiyonunu içe
aktarmış oluyoruz. 

Peki ya bir modül içinden belli nitelik ve fonksiyonları farklı bir adla içe
aktarmak isterseniz ne yapacaksınız? 

İşte Python size bunun için de bir yol sunar. Dikkatlice bakın::
    
    from os import path as p
    
veya::
    
    from os import listdir as ld
    
gibi...

Bu örneklerde, ``os`` modülü içinden `path` adlı niteliği `p` adıyla;
``listdir()`` fonksiyonunu ise `ld` adıyla içe aktardık. Böylece `path`
niteliğini `p` adıyla; ``listdir()`` fonksiyonunu da `ld` adıyla kullanabiliriz.

Yalnız bu yöntem çok sık kullanılmaz. Bunu da not edip, içe aktarma
yöntemlerinin sonuncusuna geçelim.
    
from modül_adı import *
-------------------------

Python'daki modülleri ``from modül_adı import *`` formülüne göre içe aktarmak da
mümkündür (bu yönteme 'yıldızlı içe aktarma' diyebilirsiniz). Bu şekilde bir
modül içindeki bütün fonksiyon ve nitelikleri içe aktarmış oluruz (ismi `_` ile
başlayanlar hariç)::
    
    >>> from sys import *
    
Böylece ``sys`` modülü içindeki bütün fonksiyon ve nitelikleri, başlarına modül
adını eklemeye gerek olmadan kullanabiliriz::
    
    >>> version
    
Ancak bu yöntem pek tavsiye edilmez. Çünkü bu şekilde, modül içindeki bütün
isimleri kontrolsüz bir şekilde mevcut ortama 'boşaltmış' oluyoruz. Mesela eğer
modül bu şekilde içe aktarılmadan önce `version` diye başka bir değişken
tanımlamışsanız, modül içe aktarıldıktan sonra, önceden tanımladığınız bu
`version` değişkeninin değeri kaybolacaktır::
    
    >>> version = '1.0'
    >>> print(version)
    
    1.0
    
Bu ortama ``from sys import *`` komutuyla ``sys`` modülünün bütün içeriğini
aktaralım::
    
    >>> from sys import *
    
Şimdi de `version` değişkeninin değerini yazdıralım::
    
    >>> print(version)
    
Burada alacağımız çıktı şu olur:

.. parsed-literal::

    |version3-string|
    
Gördüğünüz gibi, ``sys`` modülünün içindeki `version` niteliği bizim önceden
tanımladığımız `version` değişkeniyle çakıştı ve herhangi bir uyarı vermeden,
bizim tanımladığımız `version` değerini silip kendi `version` değerini
bizimkinin yerine geçirdi... 

``from modül_adı import *`` komutunun yaptığı şeyi, sıkıştırılmış bir klasörün
bütün içeriğini olduğu gibi masaüstüne açmaya benzetebilirsiniz. Böyle bir
durumda, eğer masaüstünde sıkıştırılmış klasördekilerle aynı adlı dosyalar
varsa, sıkıştırılmış klasör içindeki dosya adları, masaüstünde halihazırda
varolan dosya adlarıyla çakışacaktır.

Bir sonraki konuya geçmeden önce, yıldızlı içe aktarma ile ilgili önemli bir
noktaya değinelim.

Hatırlarsanız, bu konunun başında, modülleri programımızın her yerinden içe
aktarabileceğimizi söylemiştik. Mesela bir modülü, program dosyamızın en başında
içe aktarabiliriz::
    
    from os import *
    
Ama bunun bir istisnası var. Bir modülü yıldızlı olarak içe aktaracaksak, bu
işlemi lokal etki alanları içinden gerçekleştiremeyiz. Yani mesela bir
fonksiyonun lokal isim alanı içinde şöyle bir kod yazabiliriz::
    
    def fonksiyon():
        import os
        
Veya::
    
    def fonksiyon():
        import subprocess as sp
        
Ama şöyle bir kod yazamayız::
    
    def fonksiyon():
        from os import *
        
Bu kodları bir dosyaya kaydedip çalıştırdığımızda şuna benzer bir hata alırız::
    
      File "falanca.py", line 1
        def fonksiyon():
    SyntaxError: import * only allowed at module level    

Bunun anlamı şu: Yıldızlı içe aktarma işlemleri ancak modül seviyesinde, yani
global isim alanında gerçekleştirilebilir. Dolayısıyla yukarıdaki içe aktarma
işlemini ancak fonksiyonun dışında gerçekleştirebiliriz::
    
    from os import *
    
    def fonksiyon():
        pass

Veya::
    
    def fonksiyon():
        pass
        
    from os import *
    
Bu istisnai duruma dikkat ediyoruz. Elbette modül içe aktarma işlemlerini
gerçekleştirmenin en sağlıklı yolu bütün modülleri program dosyasının en başında
içe aktarmaktır. 

Kendi Tanımladığımız Modüller
******************************

Buraya gelene kadar sadece Python'daki hazır modüllerden söz ettik. Hazır
modüllerin, 'Standart Kütüphane Modülleri' ve 'Üçüncü Şahıs Modülleri' olarak
ikiye ayrıldığını öğrenmiştiniz. Yukarıda bu hazır modüllerin 'Standart
Kütüphane Modülleri' adını verdiğimiz alt başlığını halihazırda ele aldık.
Dolayısıyla artık standart modüllerin neler olduğunu ve genel olarak bunların
nasıl kullanıldığını biliyoruz.

Hazır modül başlığı altında bir de 'üçüncü şahıs modülleri'nin bulunduğunu da
söylemiştik. Birazdan üçüncü şahıs modüllerinden de söz edeceğiz. Ama isterseniz
ondan önce hazır modüllere bir ara verelim ve biraz da kendi modüllerimizi nasıl
yazabileceğimize bakalım. Kendi modüllerimizi yazmak, modül konusunu biraz daha
net bir şekilde anlamamızı sağlayacaktır.

Modüllerin Tanımlanması
========================

Hatırlarsanız bu bölümün başında, 'modül nedir?' sorusuna şu cevabı vermiştik:
    
    *Bazı işlevleri kolaylıkla yerine getirmemizi sağlayan birtakım
    fonksiyonları ve nitelikleri içinde barındıran araçlar...*
    
Esasında Python'daki modülleri şöyle de tanımlayabiliriz:

    *Diyelim ki bir program yazıyorsunuz. Yazdığınız bu programın içinde
    karakter dizileri, sayılar, değişkenler, listeler, demetler, sözlükler ve
    fonksiyonlar var. Programınız da .py uzantılı bir metin dosyası içinde yer
    alıyor. İşte bütün bu öğeleri ve veri tiplerini içeren .py uzantılı dosyaya
    'modül' adı verilir. Yani şimdiye kadar yazdığınız ve yazacağınız bütün
    Python programları aynı zamanda birer modül adayıdır.*
    
Gelin isterseniz yukarıdaki bu tanımın doğruluğunu test edelim. 

Şimdi Python'ın etkileşimli kabuğunu çalıştırın ve kütüphane modüllerinden biri
olan ``os`` modülünü içe aktarın::
    
    >>> import os
    
``dir(os)`` komutunu kullanarak modülün içeriğini kontrol ettiğinizde, o listede
`__file__` adlı bir niteliğin olduğunu göreceksiniz. Bu nitelik Python ile
yazılmış tüm modüllerde bulunur. Bu niteliği şu şekilde kullanıyoruz:

.. parsed-literal::
    
    >>> os.__file__
    
    'C:\\Python\ |ext-noformat|\ \\lib\\os.py'
    
İşte buradan aldığımız çıktı bize ``os`` modülünün kaynak dosyasının nerede
olduğunu gösteriyor. Hemen çıktıda görünen konuma gidelim ve `os.py` dosyasını
açalım. 

Dosyayı açtığınızda, gerçekten de bu modülün aslında sıradan bir Python programı
olduğunu göreceksiniz. Dosyanın içeriğini incelediğinizde, ``dir(os)`` komutuyla
elde ettiğimiz nitelik ve fonksiyonların dosya içinde nasıl tanımlandığını
görebilirsiniz. Mesela yeni dizinler oluşturmak için ``os.makedirs()`` şeklinde
kullandığımız ``makedirs`` fonksiyonunun `os.py` içinde tanımlanmış alelade bir
fonksiyon olduğunu görebilirsiniz.

Aynı şekilde, önceki sayfalarda örneklerini verdiğimiz ``webbrowser`` modülü de,
bilgisayarımızdaki sıradan bir Python programından ibarettir. Bu modülün nerede
olduğunu da şu komutla görebilirsiniz::
    
    >>> import webbrowser
    >>> webbrowser.__file__
     
Gördüğünüz gibi, ``webbrowser`` modülü de, tıpkı ``os`` modülü gibi,
bilgisayarımızdaki `.py` uzantılı bir dosyadan başka bir şey değil. İsterseniz
bu dosyanın da içini açıp inceleyebilirsiniz.

Yalnız şu gerçeği de unutmamalıyız: Python'daki bütün modüller Python
programlama dili ile yazılmamıştır. Bazı modüller C ile yazılmıştır. Dolayısıyla
C ile yazılmış bir modülün `.py` uzantılı bir Python dosyası bulunmaz. Mesela
``sys`` böyle bir modüldür. Bu modül C programlama dili ile yazıldığı için,
kayıtlı bir `.py` dosyasına sahip değildir. Dolayısıyla bu modülün bir
`__file__` niteliği de bulunmaz::
    
    >>> import sys
    >>> sys.__file__

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute '__file__'

Ama tabii ki, Python'daki standart kütüphane modüllerinin çok büyük bölümü
Python ile yazılmıştır ve bu modüllerin kaynak dosyalarını ``os`` ve
``webbrowser`` modüllerini bulduğunuz dizinde görebilirsiniz. Örneğin önceki
derslerimizde bahsi geçen ``locale`` ve ``random`` gibi modüllerin kaynak
dosyalarını da burada bulabilirsiniz. 

Gelelim asıl konumuz olan 'modül tanımlama'ya...

Hatırlarsanız, Python'da bir fonksiyon tanımlamak için şu söz dizimini
kullanıyorduk::
    
    def fonksiyon_adı(parametreler):
        fonksiyon_gövdesi
        
Ancak yukarıdaki örneklerden de rahatlıkla görebileceğiniz gibi, modüller için
böyle özel bir söz dizimi yoktur. Yazdığınız her Python programı aynı zamanda
potansiyel bir modüldür. 

O halde şimdi gelin bir tane de kendimiz modül yazalım.

Mesela bir program dosyası oluşturalım ve adını da `sözlük.py` koyalım. İşte bu
program, aynı zamanda bir Python modülüdür. Bu modülün adı da 'sözlük'tür.
Dediğimiz gibi, Python'da modüller genellikle `.py` uzantısına sahiptir. Ancak
bir modülün adı söylenirken bu `.py` uzantısı dikkate alınmaz. Bu yüzden
elinizdeki 'sözlük.py' adlı programın modül adı 'sözlük' olacaktır.

Gördüğünüz gibi, modül tanımlamakta herhangi bir özel zorluk yok. Yazdığımız her
program, otomatik olarak, aynı zamanda bir modül oluyor.

`sözlük.py` adlı programımızın içeriği şöyle olsun::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        return sözlük.get(sözcük, hata.format(sözcük))
        
İşte böylece ilk modülümüzü tanımlamış olduk. Şimdi de, yazdığımız bu modülü
nasıl kullanacağımızı öğrenelim.

Esasında kütüphane modülleriyle kendi yazdığımız modüller arasında kullanım
açısından pek bir fark yoktur. Bu bölümün başında gördüğümüz kütüphane
modüllerini nasıl kullanıyorsak, kendi modüllerimizi de öyle kullanıyoruz.

Kütüphane modüllerini anlatırken gördüğümüz gibi, modül sistemi sayesinde, bir
program içinde bulunan fonksiyon (ve nitelikleri) başka Python programları
içine aktarabiliyoruz. Böylece bir Python programındaki (veya modülündeki)
işlevsellikten, başka bir Python programında da yararlanabiliyoruz.

Şimdi, eğer bu `sözlük.py` dosyasını, mesela masaüstüne kaydettiyseniz,
masaüstünün bulunduğu konumda bir komut satırı açın ve Python'ın etkileşimli
kabuğunu başlatın. Tıpkı kütüphane modüllerinde olduğu gibi, etkileşimli kabukta
şu komutu vererek ``sözlük`` adlı modülü içe aktarın::

    >>> import sözlük

Eğer hiçbir şey olmadan bir alt satıra geçildiyse modülünüzü başarıyla içe
aktardınız demektir. Eğer ``No module named sözlük`` gibi bir hata mesajıyla
karşılaşıyorsanız, muhtemelen Python'ı `sözlük.py` dosyasının olduğu dizinde
başlatamamışsınızdır.

``import sözlük`` komutunun başarılı olduğunu varsayarak yolumuza devam
edelim...

Modüllerin Yolu
==================

Python geliştiricilerinin yazıp dile kaynaştırdığı kütüphane modülleri ile
kendi yazdığınız modüller arasında pek bir fark bulunmadığını ifade etmiştik.
Her iki modül türü de, içinde Python komutlarını ve veri tiplerini barındıran
alelade Python programlarından ibarettir.

Ancak şimdiye kadar yaptığımız örneklerde bir şey dikkatinizi çekmiş olmalı.
Kütüphane modüllerini her yerden içe aktarabiliyoruz. Yani, komut satırını
çalıştırdığımız her konumda veya program dosyamızın bulunduğu her dizin altında
bu modülleri rahatlıkla kullanabiliyoruz. Python'ın bu modülleri bulamaması
gibi bir şey söz konusu değil. 

Ama kendi yazdığımız modülleri içe aktarabilmemiz için, bu modüllerin o anda
içinde bulunduğumuz dizin altında yer alması gerekiyor. Yani mesela yukarıda
örneğini verdiğimiz ``sözlük`` modülünü, `sözlük.py` dosyasını
bilgisayarımızdaki hangi konuma kaydetmişsek o konumdan içe aktarabiliyoruz.

Diyelim ki `sözlük.py` dosyasını masaüstüne kaydetmiştik. İşte bu modülü komut
satırında içe aktarabilmemiz için, komut satırını da masaüstünün bulunduğu
konumda çalıştırmış olmamız gerekiyor. 

Aynı şekilde eğer biz bu ``sözlük`` modülünü, `deneme.py` adlı başka bir program
içinde kullanacaksak, bu `deneme.py` dosyasının da `sözlük.py` adlı dosya ile
aynı dizinde yer alması gerekiyor. 

Aksi halde, ``import sözlük`` komutu hata verecektir.

Peki neden kütüphane modüllerini her yerden içe aktarabilirken, kendi yazdığımız
modülleri yalnızca bulundukları dizin altında içe aktarabiliyoruz? 

Aslında bunun cevabı çok basit: Biz bir program dosyasında veya komut satırında
``import modül_adı`` gibi bir komut verdiğimizde Python 'modül_adı' olarak
belirttiğimiz modülü bulmak için bir arama işlemi gerçekleştirir. Elbette Python
bu modülü sabit diskin tamamında aramaz. Python, içe aktarmak istediğimiz modülü
bulmak için belli birtakım dizinlerin içini kontrol eder. Peki Python modül
dosyasını bulmak için hangi dizinlerin içine bakar? Bu sorunun cevabını bize
``sys`` modülünün `path` adlı bir niteliği verecek. Hemen bakalım::
    
    >>> import sys
    >>> sys.path
    
İşte Python bir modül dosyasını ararken, ``import`` komutunun verildiği dizin
ile birlikte, ``sys.path`` çıktısında görünen dizinlerin içine de bakar. Eğer
modül dosyasını bu dizinlerin içinde bulursa modülü başarıyla içe aktarır, ama
eğer bulamazsa ``ImportError`` cinsinden bir hata verir.

Peki eğer biz kendi modüllerimizi de her yerden içe aktarabilmek istersek ne
yapmamız gerekiyor?

Bunun için iki seçeneğimiz var: Birincisi, modülün yolunu ``sys.path`` listesine
ekleyebiliriz. İkincisi, modülümüzü ``sys.path`` içinde görünen dizinlerden
birine kopyalayabilir veya taşıyabiliriz. 

Öncelikle birinci seçeneği ele alalım.

Gördüğünüz gibi, ``sys.path`` komutunun çıktısı aslında basit bir listeden başka
bir şey değildir. Dolayısıyla Python'da liste adlı veri tipi üzerinde ne tür
işlemler yapabiliyorsanız, ``sys.path`` üzerinde de aynı şeyleri yapabilirsiniz.

Mesela, modül dosyasının `/home/istihza/programlar` adlı dizin içinde
bulunduğunu varsayarsak, modül dosyasının yolunu ``sys.path`` listesinin en
sonuna şu şekilde ekleyebiliriz::
    
    sys.path.append(r'/home/istihza/programlar')
    
Burada listelerin ``append()`` metodunu kullandığımıza dikkat edin. Dediğimiz
gibi, ``sys.path`` aslında basit bir listeden ibarettir. Dolayısıyla bir listeye
nasıl öğe ekliyorsak, ``sys.path``'e de aynı şekilde öğe ekliyoruz. 

Modül dosyasının bulunduğu `/home/istihza/programlar` yolunu ``sys.path``
listesine eklediğimize göre, artık modülümüzü her yerden içe aktarabiliriz. 

Kendi yazdığımız bir modülü her yerden içe aktarabilmenin ikinci yönteminin,
ilgili modül dosyasını ``sys.path`` çıktısında görünen dizinlerden herhangi
birine kopyalamak olduğunu söylemiştik. Dolayısıyla, ``sys.path`` çıktısına
bakıp, modül dosyanızı orada görünen dizinlerden herhangi biri içine
kopyalayabilirsiniz. Yaygın olarak tercih edilen konum, Python kurulum dizini
içindeki `site-packages` adlı dizindir. Bu dizinin yerini şu şekilde tespit
edebilirsiniz::
    
    >>> from distutils import sysconfig
    >>> sysconfig.get_python_lib()

Modül dosyanızı, bu komutlardan aldığınız çıktının gösterdiği dizin içine
kopyaladıktan sonra, modülünüzü her yerden içe aktarabilirsiniz.

Bu konuyu kapatmadan önce ``sys.path`` ile ilgili önemli bir bilgi daha verelim.
Python, içe aktarmak istediğimiz bir modülü bulabilmek için dizinleri ararken
``sys.path`` listesindeki dizin adlarını soldan sağa doğru okur. Modül dosyasını
bulduğu anda da arama işlemini sona erdirir ve modülü içe aktarır. Diyelim ki
``sys.path`` çıktımız şöyle::
    
    ['A', 'B', 'C']
    
Eğer hem `A`, hem de `B` dizininde `sözlük.py` adlı bir dosya varsa, Python `A`
dizinindeki ``sözlük`` modülünü içe aktarır. Çünkü ``sys.path`` çıktısında `A`
dizini `B` dizininden önce geliyor. Eğer siz içe aktarma sırasında bir dizine
öncelik vermek isterseniz o dizini ``append()`` metoduyla ``sys.path``
listesinin sonuna eklemek yerine, ``insert()`` metoduyla listenin en başına
ekleyebilirsiniz::
    
    >>> sys.path.insert(0, r'dizin/adı')
    
Böylece Python, modülünüzü en başa eklediğiniz dizinden içe aktaracaktır.
    
Tekrar tekrar söylediğimiz gibi, ``sys.path`` sıradan bir listedir. Dolayısıyla
listelerin üzerine hangi metotları uygulayabiliyorsanız ``sys.path`` üzerine de
o metotları uygulayabilirsiniz.

Modüllerde Değişiklik Yapmak
=============================

Python'da bir modül başka bir ortama aktarıldığında, o modülün içinde yer alan
nitelik ve fonksiyonların o ortam içinden kullanılabilir hale geldiğini
biliyorsunuz. Yukarıdaki örnekte biz ``import sözlük`` komutuyla, ``sözlük``
adlı modülün bütün içeriğini etkileşimli kabuk ortamına (veya program dosyasına)
aktarmış olduk. Dolayısıyla da artık bu modülün bütün içeriğine erişebiliriz.
Peki acaba bu modül içinde bizim erişebileceğimiz hangi nitelik ve fonksiyonlar
bulunuyor?

Tıpkı kütüphane modüllerini işlerken yaptığımız gibi, ``dir()`` fonksiyonundan
yararlanarak, içe aktardığımız bu modül içindeki kullanılabilir fonksiyon ve
nitelikleri görebilirsiniz::

    >>> dir(sözlük)

Bu komut bize şöyle bir çıktı verir::

    ['__builtins__', '__cached__', '__doc__', 
    '__file__', '__loader__', '__name__',
    '__package__', '__spec__', 'ara', 'sözlük']

Gördüğünüz gibi, nasıl ``os`` modülünün içinde `name`, ``listdir()`` ve
``getcwd()`` gibi nitelik ve fonksiyonlar varsa, kendi yazdığımız ``sözlük``
modülü içinde de ``ara()`` adlı bir fonksiyon ve `sözlük` adlı bir nitelik var.

İşte biz bu fonksiyon ve niteliği kullanma imkanına sahibiz. Gelin birkaç deneme
çalışması yapalım::
    
    >>> sözlük.sözlük
    
Bu komutun, bir kütüphane modülündeki niteliklere erişmekten hiçbir farkı
olmadığına dikkatinizi çekmek isterim. Mesela ``sys`` modülünün `version`
niteliğine nasıl erişiyorsak, ``sözlük`` modülünün `sözlük` niteliğine de aynı
şekilde erişiyoruz.
    
``sözlük.sözlük`` komutu bize ``sözlük`` modülü içindeki `sözlük` adlı
değişkenin içeriğini verecektir.
      
Şimdi de aynı modül içindeki ``ara()`` fonksiyonuna erişelim::
    
    >>> sözlük.ara('kitap')
    
Bu da bize ``ara()`` fonksiyonunu `kitap` argümanıyla birlikte çağırma imkanı
veriyor.

Yukarıda verdiğimiz örnekte ``sözlük`` modülünü etkileşimli kabuk üzerinde
kullandık. Elbette program yazarken modülleri etkileşimli kabukta değil, program
dosyaları içinde kullanacağız. Ancak özellikle bir modülün geliştirilme
aşamasında o modülü test etmek için etkileşimli kabuk üzerinde çalışmak oldukça
pratik ve faydalı bir yoldur. Mesela yazmakta olduğunuz bir programın (diğer bir
deyişle modülün) nitelik ve fonksiyonlarını test etmek için, o programı
etkileşimli kabukta bir modül olarak içe aktarıp çeşitli deneme çalışmaları
yapabilirsiniz.

Dilerseniz yine yukarıdaki örnek üzerinden gidelim::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        return sözlük.get(sözcük, hata.format(sözcük))    
        
Bu modülü içe aktaralım::
    
    >>> import sözlük
    
Modülün içeriğini kontrol edelim::
    
    >>> dir(sözlük)
    
Bu komutun çıktısında `sözlük` niteliğini ve ``ara()`` fonksiyonunu görüyoruz.
Gelin şimdi programımıza bir ekleme yapalım::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        return sözlük.get(sözcük, hata.format(sözcük))  
        
    def ekle(sözcük, anlam):
        mesaj = "{} kelimesi sözlüğe eklendi!"
        sözlük[sözcük] = anlam
        print(mesaj.format(sözcük))
        
Burada ``sözlük`` modülüne ``ekle()`` adlı bir fonksiyon ilave ettik. Bu
fonksiyon, sözlüğe yeni kelimeler eklememizi sağlayacak. Şimdi tekrar
modülümüzün içeriğini kontrol edelim::
    
    >>> dir(sözlük)
    
Ancak gördüğünüz gibi, modüle yeni eklediğimiz ``ekle()`` fonksiyonu bu çıktıda
görünmüyor. Bunun nedeni, etkileşimli kabukta modül bir kez içe aktarıldıktan
sonra, o modülde yapılan değişikliklerin otomatik olarak etkinleşmiyor oluşudur.
Yani değişikliklerin etkileşimli kabukta etkinleşebilmesi için o modülü yeniden
yüklememiz lazım. Bunu iki şekilde yapabiliriz:

Birincisi, etkileşimli kabuğu kapatıp yeniden açtıktan sonra ``import sözlük``
komutuyla ``sözlük`` modülünü tekrar içe aktarabiliriz. 

İkincisi, ``importlib`` adlı bir kütüphane modülünden yararlanarak kendi
modülümüzün tekrar yüklenmesini sağlayabiliriz. Bu modülü şöyle kullanıyoruz::
    
    >>> import importlib
    >>> importlib.reload(sözlük)
    
Bu iki komutu verdikten sonra, ``sözlük`` üzerinde tekrar ``dir()`` fonksiyonunu
uygularsak, yeni eklediğimiz ``ekle()`` fonksiyonunun çıktıya yansıdığını
görürüz::
    
    >>> dir(sözlük)

    ['__builtins__', '__cached__', '__doc__', '__file__', 
    '__loader__', '__name__', '__package__', '__spec__', 
    'ara', 'ekle', 'sözlük']
    
Tıpkı önceki derslerimizde gördüğümüz ``sys``, ``os`` ve ``keyword`` modülleri
gibi, ``importlib`` de bir kütüphane modülüdür. Bu modülün bizim yukarıda
yazdığımız ``sözlük`` adlı modülden farkı, Python geliştiricileri tarafından
yazılıp dile entegre edilmiş bir 'hazır modül' olmasıdır. Yani ``sözlük``
modülünü biz kendimiz yazdık, ``importlib`` modülünü ise Python geliştiricileri
yazdı. İkisi arasındaki tek fark bu. 

Ne diyorduk? Evet, ``sözlük`` adlı modüle ``ekle()`` adlı yeni bir fonksiyon
ilave ettik. Bu fonksiyona da, tıpkı `sözlük` niteliğinde ve ``ara()``
fonksiyonunda olduğu gibi, modül adını kullanarak erişebiliriz::
    
    >>> sözlük.ekle('araba', 'car')
    
    araba kelimesi sözlüğe eklendi!

Sözlüğümüze, 'araba' adlı yeni bir kelimeyi, 'car' karşılığı ile birlikte
ekledik. Hemen bunu sorgulayalım::
    
    >>> sözlük.ara('araba')
    
    'car'
    
Gayet güzel! Şimdi sözlüğümüze bir ekleme daha yapalım::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        return sözlük.get(sözcük, hata.format(sözcük))  
        
    def ekle(sözcük, anlam):
        mesaj = "{} kelimesi sözlüğe eklendi!"
        sözlük[sözcük] = anlam
        print(mesaj.format(sözcük))
    
    def sil(sözcük):
        try:
            sözlük.pop(sözcük)    
        except KeyError as err:
            print(err, "kelimesi bulunamadı!")
        else:
            print("{} kelimesi sözlükten silindi!".format(sözcük))

Bu defa da modülümüze ``sil()`` adlı başka bir fonksiyon ekledik. Bu fonksiyon,
sözlükten öğe silmemizi sağlayacak::
    
    >>> sözlük.sil('kitap')
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'sil'
    
Gördüğünüz gibi, bu kez bir hata mesajı aldık. Peki sizce neden? Elbette
değişiklik yaptıktan sonra modülü yeniden yüklemediğimizden... O halde önce
modülümüzü yeniden yükleyelim::
    
    >>> importlib.reload(sözlük)
    
Şimdi bu fonksiyonu kullanabiliriz::
    
    >>> sözlük.sil('kitap')

    kitap kelimesi sözlükten silindi!

Bu noktada, ``importlib`` modülünün ``reload()`` fonksiyonunun çalışma sistemine
ilişkin birkaç önemli bilgi verelim.

``importlib`` modülünün ``reload()`` fonksiyonu, bir modüle yeni eklenen öğeleri
yeniden yükleyerek, bunların etkileşimli kabukta kullanılabilir hale gelmesini
sağlar. Bunun ne demek olduğunu biliyoruz. Yukarıda bunun örneklerini vermiştik.
    
Eğer bir modüldeki bazı nitelik veya fonksiyonları silerseniz, ``importlib`` 
modülünün ``reload()`` fonksiyonu ile bu modülü yeniden yükledikten sonra bile
bu nitelik ve fonksiyonlar önbellekte tutulmaya devam eder. Örneğin, yukarıdaki
``sözlük`` modülünü önce içe aktaralım::
    
    >>> import sözlük
    
Şimdi modülün içeriğini kontrol edelim::
    
    >>> dir(sözlük)
    
    ['__builtins__', '__cached__', '__doc__', '__file__', 
    '__loader__', '__name__', '__package__', '__spec__', 
    'ara', 'ekle', 'sil', 'sözlük']    
    
Modül dosyasından ``sil()`` adlı fonksiyonu çıkaralım. Yani modülümüzün son hali
şöyle olsun::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        return sözlük.get(sözcük, hata.format(sözcük))  
        
    def ekle(sözcük, anlam):
        mesaj = "{} kelimesi sözlüğe eklendi!"
        sözlük[sözcük] = anlam
        print(mesaj.format(sözcük))   

Tekrar etkileşimli kabuğa dönüp, ``importlib`` modülünün ``reload()`` fonksiyonu
aracılığıyla modülümüzü yeniden yükleyelim::
    
    >>> import importlib
    >>> importlib.reload(sözlük)
    
Şimdi ``sözlük`` modülünün içeriğini tekrar kontrol edelim::
    
    >>> dir(sözlük)
    
    ['__builtins__', '__cached__', '__doc__', '__file__', 
    '__loader__', '__name__', '__package__', '__spec__', 
    'ara', 'ekle', 'sil', 'sözlük']    

Gördüğünüz gibi, biz ``sil()`` fonksiyonunu çıkarmış olduğumuz halde,
``dir(sözlük)`` çıktısında bu öğe görünmeye devam ediyor. Üstelik bu fonksiyon
halen kullanılabilir durumda!

::
    
    >>> sözlük.sil('programlama')
    
    programlama kelimesi sözlükten silindi!

Ancak bu durumu rahatlıkla görmezden gelebilirsiniz. Ama eğer o öğenin orada
olması sizi rahatsız ediyorsa, şu komutla o öğeyi silebilirsiniz::
    
    >>> del sözlük.sil
    
Dediğimiz gibi, modülden silinen öğeler, ``reload()`` ile yeniden yüklendikten
sonra dahi kullanılır durumda kalmaya devam eder. Ama eğer modül içinde varolan
bir öğe üzerinde değişiklik yaparsanız o değişiklik, ``reload()`` sonrası
modülün görünümüne yansıyacaktır. Yani mesela, modülde halihazırda varolan
``sil()`` fonksiyonu üzerinde bir değişiklik yaparsanız, bu değişiklik
``reload()`` ile yeniden yükleme sonrasında etkileşimli kabuğa yansıyacaktır.

Üçüncü Şahıs Modülleri
***********************

Buraya kadar Python'daki kütüphane modüllerinden ve kendi yazdığımız modüllerden
söz ettik. Artık modüllerin ne olduğunu ve ne işe yaradığını gayet iyi
biliyoruz. Bu bölümde ise, yine bir 'hazır modül' türü olan üçüncü şahıs
modüllerinden bahsedeceğiz. 

Üçüncü şahıs modülleri, başka Python programcıları tarafından yazılıp
hizmetimize sunulmuş programlardır. Bu yönüyle bunlar kütüphane modüllerine çok
benzer. Ama bu ikisi arasında önemli bir fark bulunur: Kütüphane modülleri
Python programlama dilinin bir parçasıdır. Dolayısıyla kütüphane modüllerini
kullanmak için herhangi bir ek yazılım indirmemiz gerekmez. Üçüncü şahıs
modülleri ise dilin bir parçası değildir. Bu modülleri kullanabilmek için,
öncelikle bunları modül geliştiricisinin koyduğu yerden bilgisayarımıza
indirmemiz gerekir.

Hatırlarsanız ilk derslerimizde Cx_Freeze adlı bir yazılımdan söz etmiştik. İşte
bu yazılım bir üçüncü şahıs modülüdür. Bu modülü kullanabilmek için öncelikle
ilgili yazılımı programımıza kurmamız gerekmişti. 

Python için yazılmış üçüncü şahıs modüllerine çeşitli kaynaklardan
ulaşabilirsiniz. Bu tür modülleri bulabileceğiniz en geniş kaynak
https://pypi.python.org/pypi adresidir. Burada 60.000'in üzerinde modüle
ulaşabilirsiniz. 

Peki bu modülleri nasıl kuracağız? 

Eğer bir modül https://pypi.python.org/pypi adresinde ise, bu modülü sistem
komut satırında şu şekilde kurabilirsiniz::
    
    pip3 install modül_adı
    
.. note:: Python'ın 2.7.9 ve 3.4.0 sürümlerinden itibaren, pip adlı yazılım
 öntanımlı olarak Python kurulumuyla birlikte geliyor. Dolayısıyla Python2'deki
 pip'i kullanmak isterseniz ``pip2`` komutunu, Python3'teki pip'i kullanmak
 isterseniz de ``pip3`` komutunu kullanabilirsiniz.
    
Örneğin amacınız Django adlı üçüncü şahıs modülünü kurmak ise bu modülü şu komut
ile kurabilirsiniz::
    
    pip3 install django
    
Eğer bir üçüncü şahıs modülünü https://pypi.python.org/pypi adresinden değil de
başka bir kaynaktan indiriyorsanız, kurulum için birkaç farklı seçenek olabilir.

Eğer indireceğiniz dosya Windows işletim sistemine uyumlu bir `.exe` dosyasıysa,
bunu herhangi bir Windows programı gibi kurabilirsiniz. 

Eğer indireceğiniz dosya `.tar.gz` veya `.zip` gibi sıkıştırılmış bir klasör
olarak iniyorsa öncelikle bu sıkıştırılmış klasörü açın. Eğer klasör içeriğinde
`setup.py` adlı bir dosya görürseniz bu dosyanın bulunduğu konumda bir komut
satırı açın ve şu komutu verin::
    
    python setup.py install
    
Tabii burada ``python`` komutunun ``python3`` mü, ``py -3`` mü yoksa başka bir
şey mi olacağı tamamen sizin Python kurulumunu nasıl yaptığınıza bağlıdır.
Neticede siz oraya, Python'ı hangi komutla başlatıyorsanız onu yazacaksınız.
Yani eğer Python'ı ``python3`` komutuyla başlatıyorsanız yukarıdaki komutu şöyle
vereceksiniz::
    
    python3 setup.py install
    
Aynı şekilde, GNU/Linux kullanıcılarının da bu komutu yetkili kullanıcı olarak
vermesi gerekecektir muhtemelen::
    
    sudo python3 setup.py install
    
Veya önce::
    
    su - 
    
Ardından::
    
    python3 setup.py install
    
İndirip kurduğunuz bir üçüncü şahıs modülünü nasıl kullanacağınızı, indirdiğiniz
modülün belgelerine bakarak öğrenebilirsiniz. 

.. note:: Paketler konusunu işlerken üçüncü şahıs modüllerinden daha ayrıntılı
 bir şekilde söz edeceğiz.

__all__ Listesi
******************

Önceki başlıklar altında da ifade ettiğimiz gibi, farklı içe aktarma
yöntemlerini kullanarak, bir modül içindeki öğeleri farklı şekillerde içe
aktarabiliyoruz. Gelin isterseniz Python'ın içe aktarma mekanizmasını
anlayabilmek için ufak bir test yapalım.

Şimdi masaüstünde, içeriği aşağıdaki gibi olan, `modül.py` adlı bir dosya
oluşturun::
    
    def fonk1():
        print('fonk1')
    
    def fonk2():
        print('fonk2')
    
    def fonk3():
        print('fonk3')
    
    def fonk4():
        print('fonk4')
    
    def fonk5():
        print('fonk5')
        
    def _fonk6():
        print('_fonk6')
        
    def __fonk7():
        print('__fonk7')
        
    def fonk8_():
        print('fonk8_')
 
Daha sonra, masaüstünün bulunduğu konumda bir komut penceresi açarak Python'ın
etkileşimli kabuğunu çalıştırın ve orada şu komutu verip bu `modül.py` adlı
dosyayı bir modül olarak içe aktarın::
    
    >>> import modül
    
Şimdi de şu komutu kullanarak modül içeriğini kontrol edin::
    
    >>> dir(modül)
    
Buradan şu çıktıyı alıyoruz::
    
    ['__builtins__', '__cached__', '__doc__', '__file__', '__fonk7', 
     '__loader__', '__name__', '__package__', '__spec__', '_fonk6', 
     'fonk1', 'fonk2', 'fonk3', 'fonk4', 'fonk5', 'fonk8_']    
   
Gördüğünüz gibi, modül içinde tanımladığımız bütün fonksiyonlar bu listede var.
Dolayısıyla bu fonksiyonlara şu şekilde erişebiliyoruz::
    
    >>> modül.fonk1()
    
    fonk1
    
    >>> modül.fonk2()
    
    fonk2
    
    >>> modül._fonk6()
    
    _fonk6
    
    >>> modül.__fonk7()
    
    __fonk7
    
    >>> modül.fonk8_()
    
    fonk8_
    
Bu şekilde, istisnasız bütün fonksiyonlara erişim yetkisi elde ettiğimize
dikkatinizi çekmek isterim.

Şimdi etkileşimli kabuğu kapatıp tekrar açalım ve bu kez modülümüzü şu şekilde
içe aktaralım::
    
    >>> from modül import *
    
Bu şekilde, ismi ``_`` ile başlayanlar hariç bütün fonksiyonları, modül öneki
olmadan mevcut etki alanına aktardığımızı biliyoruz.

Kontrol edelim::
    
    >>> dir()
    
Buradan şu çıktıyı alıyoruz::
    
    ['__builtins__', '__doc__', '__loader__', '__name__', 
     '__package__', '__spec__', 'fonk1', 'fonk2', 'fonk3', 
     'fonk4', 'fonk5', 'fonk8_']
     
Gördüğünüz gibi, gerçekten de ismi ``_`` ile başlayanlar hariç, bütün
fonksiyonlar, modül öneki olmadan kullanılmaya hazır bir şekilde mevcut etki
alanımız içinde görünüyor. Bunları şu şekilde kullanabileceğimizi biliyorsunuz::
    
    >>> fonk4()
    
    fonk4
    
    >>> fonk8_()
    
    fonk8_
    
Elbette, ismi ``_`` ile başlayan fonksiyonları, doğrudan isimlerini kullanarak
içe aktarma imkanına sahipsiniz::
    
    >>> from modül import __fonk7
    >>> from modül import _fonk6
    
Tabii, bu fonksiyonları içe aktarabilmek için bunların isimlerini biliyor
olmanız lazım...

Peki siz, yazdığınız bir programda yalnızca kendi belirlediğiniz isimlerin içe
aktarılmasını isterseniz ne yapacaksınız? İşte bunun için, başlıkta sözünü
ettiğimiz ``__all__`` adlı bir listeden yararlanabilirsiniz. 

Şimdi biraz önce oluşturduğunuz `modül.py` dosyasının en başına şu satırı
ekleyin::

    __all__ = ['fonk1', 'fonk2', 'fonk3']
    
Daha sonra etkileşimli kabukta modülünüzü şu şekilde içe aktarın::
    
    >>> from modül import *
    
Şimdi de içe aktarılan fonksiyonların neler olduğunu kontrol edin::
    
    >>> dir()
    
    ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', 
     '__spec__', 'fonk1', 'fonk2', 'fonk3']
     
Gördüğünüz gibi, yalnızca ``__all__`` listesi içinde belirttiğimiz fonksiyonlar
içe aktarıldı. Bu listeyi kullanarak, yıldızlı içe aktarmalarda nelerin içe
aktarılıp nelerin dışarıda bırakılacağını kontrol edebilirsiniz. Yalnız
unutmamanız gereken nokta, bu yöntemin öteki içe aktarma türlerinde hiçbir işe
yaramayacağıdır. Yani mesela ``modül`` adlı modülümüzü ``import modül`` şeklinde
içe aktarırsak ``__all__`` listesi dikkate alınmayacaktır.

Peki ya ``__all__`` listesini boş bırakırsak ne olur?

::
    
    __all__ = []
    
Tabii ki, bu şekilde yıldızlı aktarmalarda (modülün kendi varsayılan
fonksiyonları hariç) hiçbir fonksiyon içe aktarılmaz...

Modüllerin Özel Nitelikleri
****************************

Python'da bütün modüllerin ortak olarak sahip olduğu bazı nitelikler vardır. Bu
niteliklerin hangileri olduğunu görmek için kesişim kümelerinden yararlanarak
şöyle bir kod yazabiliriz::
    
    import os, sys, random
    
    set_os = set(dir(os))
    set_sys = set(dir(sys))
    set_random = set(dir(random))
    
    print(set_os & set_sys & set_random)
    
Bu kodlar, `os`, `sys` ve `random` modüllerinin kesişim kümesini, yani her üç
modülde ortak olarak bulunan nitelikleri verecektir. Bu kodları
çalıştırdığımızda şu çıktıyı alıyoruz::
    
    {'__doc__', '__package__', '__loader__', '__name__', '__spec__'}
    
Demek ki hem `os` hem `sys` hem de `random` modülünde ortak olarak bulunan
nitelikler bunlarmış... Eğer bu üç modülün bütün modülleri temsil etmiyor
olabileceğinden endişe ediyorsanız, bildiğiniz başka modülleri de bu kodlara
ekleyerek testinizin kapsamını genişletebilirsiniz.
    
Mesela bu kodlara bir de `subprocess` modülünü ekleyelim::
    
    import os, sys, random, subprocess
    
    set_os = set(dir(os))
    set_sys = set(dir(sys))
    set_random = set(dir(random))
    set_subprocess = set(dir(subprocess))
    
    print(set_os & set_sys & set_random & set_subprocess)
    
Yalnız  burada şöyle bir şey dikkatinizi çekmiş olmalı: Kesişim kümesini bulmak
istediğimiz öğelere başka öğeler de eklemek istediğimizde her defasında birkaç
farklı işlem yapmak zorunda kalıyoruz. Bu da hem kodlarımızı hatalara açık hale
getiriyor, hem de aslında kolayca halledebileceğimiz bir işi gereksiz yere
uzatmamıza yol açıyor.
 
Gelin bu kodları biraz daha genel amaçlı bir hale getirelim. Zira 'kodların
yeniden kullanılabilir özellikte olması' (*code reusability*) programcılıkta
aranan bir niteliktir::
    
    modüller = ['os', 'sys', 'random']
    
    def kesişim_bul(modüller):
        kümeler = [set(dir(__import__(modül))) for modül in modüller]
        return set.intersection(*kümeler)
        
    print(kesişim_bul(modüller))

Eğer bu kodlara yeni bir modül eklemek istersek, yapmamız gereken tek şey en
baştaki `modüller` listesini güncellemek olacaktır. Mesela bu listeye bir de
`subprocess` modülünü ekleyelim::
    
    modüller = ['os', 'sys', 'random', 'subprocess']
    
    def kesişim_bul(modüller):
        kümeler = [set(dir(__import__(modül))) for modül in modüller]
        return set.intersection(*kümeler)
        
    print(kesişim_bul(modüller))
    
Gördüğünüz gibi, bu kodlar işimizi epey kolaylaştırdı. Sadece tek bir noktada
değişiklik yaparak istediğimiz sonucu elde ettik. 

Bu arada, ``__import__()`` fonksiyonu hariç, bu kodlardaki her şeyi daha önceki
derslerimizde öğrenmiştik. Ama gelin isterseniz biz yine de bu kodların
üzerinden şöyle bir geçelim.

Burada ilk yaptığımız iş, kullanmak istediğimiz modül adlarını tutması için bir
liste tanımlamak::
    
    modüller = ['os', 'sys', 'random', 'subprocess']
    
Bu listede modül adlarının birer karakter dizisi olarak gösterildiğine dikkat
edin. Zaten bu modülleri henüz içe aktarmadığımız için, bunları doğrudan
tırnaksız isimleriyle kullanamayız.

Daha sonra, asıl işi yapacak olan ``kesişim_bul()`` adlı fonksiyonumuzu
tanımlıyoruz::
    
    def kesişim_bul(modüller):
        kümeler = [set(dir(__import__(modül))) for modül in modüller]
        return set.intersection(*kümeler)
        
Bu fonksiyon, `modüller` adlı tek bir parametre alıyor.

Fonksiyonumuzun gövdesinde ilk olarak şöyle bir kod yazıyoruz::
    
    kümeler = [set(dir(__import__(modül))) for modül in modüller]
    
Burada `modüller` adlı listedeki her öğe üzerine sırasıyla ``__import()``
fonksiyonunu, ``dir()`` fonksiyonunu ve ``set()`` fonksiyonunu uyguluyoruz. Daha
sonra elde ettiğimiz sonucu bir liste üreteci yardımıyla liste haline getirip
`kümeler` değişkenine atıyoruz.

Gelelim ``__import__()`` fonksiyonunun ne olduğuna... 

Bir gömülü fonksiyon olan ``__import__()`` fonksiyonu, modül adlarını içeren
karakter dizilerini kullanarak, herhangi bir modülü içe aktarmamızı sağlayan bir
araçtır. Bu fonksiyonunu şöyle kullanıyoruz::
    
    >>> __import__('os')
    >>> __import__('sys')
    
Bu fonksiyonun parametre olarak bir karakter dizisi alıyor olmasının bize nasıl
bir esneklik sağladığına dikkatinizi çekmek isterim. Bu fonksiyon sayesinde
modül aktarma işlemini, kod parçaları içine programatik olarak yerleştirebilme
imkanı elde ediyoruz. Yani, modül aktarma işlemini mesela bir `for` döngüsü
içine alamıyorken::
    
    >>> modüller = ['os', 'sys', 'random']
    >>> for modül in modüller:
    ...     import modül
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    ImportError: No module named 'modül'    
    
``__import__()`` fonksiyonu bize böyle bir işlem yapabilme olanağı sunuyor::
    
    >>> modüller = ['os', 'sys', 'random']
    >>> for modül in modüller:
    ...     __import__(modül)
    
    <module 'os' from 'C:\\Python34\\lib\\os.py'>
    <module 'sys' (built-in)>
    <module 'random' from 'C:\\Python34\\lib\\random.py'>
    
Yalnız, ``__import__('os')`` gibi bir komut verdiğimizde, 'os' ismi doğrudan
kullanılabilir hale gelmiyor. Yani::
    
    >>> __import__('os')
    
...komutunu verdiğimizde, mesela `os` modülünün bir niteliği olan `name`'i
kullanamıyoruz::
    
    >>> os.name
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'os' is not defined
    
'os' ismini kullanabilmemiz için şöyle bir şey yazmış olmalıydık::
    
    >>> os = __import__('os')

Eğer ``__import__()`` fonksiyonu yardımıyla içe aktardığımız `os` modülünü bu
şekilde bir isme atamazsak, ``__import__('os')`` komutu ile içe aktarılan bütün
`os` fonksiyon ve nitelikleri, bu komut bir kez çalıştıktan sonra unutulacaktır.
Eğer ``__import__()`` fonksiyonunu bir isme atamadan, içe aktarılan modülün
niteliklerine erişmek isterseniz içe aktarma işlemi ile niteliğe erişme işlemini
aynı satırda gerçekleştirmeniz gerekir::
    
    >>> __import__('os').name
    
    'nt'
    
``__import__()`` fonksiyonu çok sık kullanacağınız bir araç değildir. Ancak
özellikle tek satırda hem bir modülü içe aktarmanız, hem de hemen ardından başka
işlemler yapmanız gereken durumlarda bu fonksiyon işinize yarayabilir::
    
    >>> open('den.txt', 'w').write('merhaba'); __import__('subprocess').call('notepad.exe den.txt')

Gerekli modülleri içe aktardıktan ve kümemimizi tanımladıktan sonra da fonksiyon
tanımını şu kodla bitiriyoruz::
    
    return set.intersection(*kümeler)
    
Burada kümelerin ``intersection()`` metodundan faydalandık. Bu metodu önceki
derslerimizde ele almıştık. Bu metot yardımıyla birden fazla kümenin kesişimini
bulabiliyoruz. 

Bu fonksiyonu normalde şöyle kullanıyorduk::
    
    >>> küme1.intersection(küme2)
    
Bu komut, `küme1` ile `küme2` adlı kümelerin kesişimini bulacaktır. Eğer bizim
kodlarımızda olduğu gibi küme ismi belirtmeksizin birden fazla kümenin
kesişimini bulmak isterseniz bu metodu doğrudan küme veri tipi (`set`) üzerine
uygulayabilirsiniz::
    
    >>> set.intersection(küme1, küme2)
    
Eğer ``intersection()`` metoduna parametreleri bir liste içinden atamak
isterseniz bu listeyi yıldız işleci yardımıyla çözmeniz gerekir::
    
    >>> liste = [küme1, küme2, küme3]
    >>> set.intersection(*liste)
    
İşte bizim yukarıda ``return set.intersection(*kümeler)`` komutuyla yaptığımız
şey de tam olarak budur. Burada ``intersection()`` metodunu doğrudan `set` veri
tipi üzerine uyguladık ve bu metodun parametrelerini `kümeler` adlı listeden
yıldız işleci yardımıyla çözdük. 

Son olarak da, tanımladığımız ``kesişim_bul()`` fonksiyonunu `modüller` adlı
parametre ile çağırdık::
    
    print(kesişim_bul(modüller))
    
Bütün bu kodları çalıştırdıktan sonra ise şöyle bir çıktı elde ettik::
    
    {'__doc__', '__name__', '__loader__', '__spec__', '__package__'}
    
İşte bu bölümün konusu, bütün modüllerde ortak olan bu beş özel nitelik. İlk
olarak ``__doc__`` niteliği ile başlayalım.

__doc__ Niteliği
=================

İsterseniz ``__doc__`` niteliğini tarif etmeye çalışmak yerine, bunu bir örnek
üzerinden anlatalım. Şimdi Python kurulum dizini içinde `os.py` dosyasının
bulunduğu konuma gidelim ve bu dosyayı açalım. Dosyayı açtığınızda, sayfanın en
başında şu karakter dizisini göreceksiniz::
        
    r"""OS routines for NT or Posix depending on what system we're on.
    
    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)
    
    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).
    """

Şimdi Python'ın etkileşimli kabuğunu açın ve şu komutları verin::
    
    >>> import os
    >>> print(os.__doc__)
    
Bu komutları verdiğinizde, yukarıdaki karakter dizisinin çıktı olarak
verildiğini göreceksiniz. Teknik dilde, üç tırnak içinde gösterilen karakter
dizilerine belge dizisi (*docstring*) veya belgelendirme dizisi (*documentation
string*) adı verilir. Modüllerin ``__doc__`` niteliğini kullanarak, bir modül
dosyasının en başında bulunan belgelendirme dizilerine erişebiliriz. 

Bir örnek daha verelim. Mesela `random` modülüne bakalım::
    
    >>> import random
    >>> print(random.__doc__)
    
`os.py` dosyası ile aynı konumda bulunan `random.py` dosyasını açtığınızda,
yukarıdaki komutlardan aldığınız çıktının `random.py` dosyasının en başındaki
uzun karakter dizisi olduğunu göreceksiniz.

Çeşitli yazılımlar, bu belge dizilerini kullanarak, ilgili modüle ilişkin kısa
kılavuzlar oluşturur. Mesela Python'ın ``help()`` fonksiyonu bu belge
dizilerinden yararlanır::
    
    >>> help(os)
    
Siz de kendi yazdığınız modüllerde bu belge dizilerinden yararlanabilirsiniz.
Ancak aklınızda bulundurmanız gereken önemli nokta, bu belge dizilerini üç
tırnak içinde belirtmeniz gerektiğidir. Alt alta çift veya tek tırnak ile
tanımladığınız karakter dizilerine ``__doc__`` niteliği aracılığıyla erişmeye
çalıştığınızda sadece ilk satırdaki karakter dizisine ulaşırsınız. Yani::
    
    "satır1"
    "satır2"
    "satır3"
    
...şeklinde tanımladığınız karakter dizileri ``__doc__`` niteliği ile
çağrıldığında yalnızca "satır1" görüntülenecektir. Eğer bu üç satırın da
kapsama alanına girmesini istiyorsak yukarıdaki karakter dizilerini şöyle
tanımlamalıyız::
    
    '''
    satır1
    satır2
    satır3
    '''
    
__name__ Niteliği
===================

Şöyle bir program yazdığımızı varsayalım::

    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        print(sözlük.get(sözcük, hata.format(sözcük)))  
        
    def ekle(sözcük, anlam):
        mesaj = "{} kelimesi sözlüğe eklendi!"
        sözlük[sözcük] = anlam
        print(mesaj.format(sözcük))
    
    def sil(sözcük):
        try:
            sözlük.pop(sözcük)    
        except KeyError as err:
            print(err, "kelimesi bulunamadı!")
        else:
            print("{} kelimesi sözlükten silindi!".format(sözcük))
            
    no = input('Yapmak istediğiniz işlemin numarasını girin: ')
    print('1. Sözlükte kelime ara')
    print('2. Sözlüğe kelime ekle')
    print('3. Sözlükten kelime sil')
    
    if no == '1':
        sözcük = input('Aradığınız sözcük: ')
        ara(sözcük)
        
    elif no == '2':
        sözcük = input('Ekleyeceğiniz sözcük: ')
        anlam = input('Eklediğiniz sözcüğün anlamı: ')
        ekle(sözcük, anlam)
        
    elif no == '3':
        sözcük = input('Sileceğiniz sözcük: ')
        sil(sözcük)
        
    else:
        print('Yanlış işlem')

`sözlük.py` adını verdiğimiz bu programı normal bir şekilde komut satırında

::
    
    python sözlük.py
    
gibi bir komutla çalıştırdığımızda bize birtakım sorular sorulacak ve verdiğimiz
cevaplara göre sözlük üzerinde bazı işlemler yapılacaktır.  

Hatırlarsanız, modüller konusunu anlatmaya başlarken, yazdığımız bütün
programların aslında birer modül olduğunu, dolayısıyla bunların başka
programların içine aktarılarak, sahip oldukları işlevlerden başka programlarda
da yararlananılabileceğini söylemiştik.

Yukarıdaki kodları, komut satırı üzerinde bağımsız bir program gibi
çalıştırabiliyoruz. Peki acaba biz bu programı doğrudan çalıştırmak değil de
başka bir programın içine aktarıp sahip olduğu işlevlerden yararlanmak istersek
ne yapacağız?

İşte bunun için ``__name__`` adlı bir nitelikten yararlanacağız. 

Python'daki herhangi bir modülü içe aktardıktan sonra bu modül üzerine ``dir()``
fonksiyonunu uygularsanız, istisnasız her modülün ``__name__`` adlı bir niteliği
olduğunu görürsünüz.

``__name__`` niteliği iki farklı değer alabilir: İçinde bulunduğu modülün adı
veya ``"__main__"`` adlı özel bir değer.

Eğer bir Python programı başka bir program içinden modül olarak içe
aktarılıyorsa, ``__name__`` niteliğinin değeri o modülün adı olacaktır.

Eğer bir Python programı doğrudan bağımsız bir program olarak çalıştırılıyorsa,
``__name__`` niteliğinin değeri bu defa ``"__main__"`` olacaktır. 

Gelin isterseniz bu durumu bir örnek üzerinde somutlaştıralım. Mesela
masaüstünde `deneme.py` adlı bir dosya oluşturup içine sadece şunu yazalım::
    
    print(__name__)
    
Şimdi önce bu dosyayı bağımsız bir program olarak çalıştıralım::
    
    python deneme.py
    
Programımızı bu şekilde çalıştırdığımızda alacağımız çıktı şu olacaktır::
    
    __main__
  
Demek ki ``__name__`` niteliğinin değeri ``"__main__"`` imiş... 

Şimdi de `deneme.py` dosyasının bulunduğu konumda Python'ın etkileşimli kabuğunu
çalıştıralım ve şu komut yardımıyla bu dosyayı bir modül olarak içe aktaralım::
    
    >>> import deneme
    
Bu defa şu çıktıyı aldık::
    
    deneme
    
Gördüğünüz gibi, ``__name__`` niteliğinin değeri bu kez de modül dosyasının adı
oldu.

İşte bu özellikten yararlanarak, yazdığınız programların bağımsız
çalıştırılırken ayrı, modül olarak içe aktarılırken ayrı davranmasını
sağlayabilirsiniz.

Gelin bu bilgiyi yukarıdaki `sözlük.py` dosyasına uygulayalım.

Bu programı komut satırı üzerinde bağımsız bir program olarak çalıştırdığınızda
ne olacağını biliyorsunuz. Peki ya aynı programı bir modül olarak içe aktarırsak
ne olur?

Deneyelim::
    
    >>> import sözlük
    
    Yapmak istediğiniz işlemin numarasını girin:
    
Gördüğünüz gibi, programımız doğrudan çalışmaya başladı. Ama biz bunu
istemiyoruz. Biz istiyoruz ki, `sözlük.py` bir modül olarak aktarıldığında
çalışmaya başlamasın. Ama biz onun içindeki nitelikleri kullanabilelim. 

Bunun için `sözlük.py` dosyasında şu değişikliği yapacağız::
    
    sözlük = {"kitap"      : "book",
              "bilgisayar" : "computer",
              "programlama": "programming"}
    
    def ara(sözcük):
        hata = "{} kelimesi sözlükte yok!"
        print(sözlük.get(sözcük, hata.format(sözcük)))  
        
    def ekle(sözcük, anlam):
        mesaj = "{} kelimesi sözlüğe eklendi!"
        sözlük[sözcük] = anlam
        print(mesaj.format(sözcük))
    
    def sil(sözcük):
        try:
            sözlük.pop(sözcük)    
        except KeyError as err:
            print(err, "kelimesi bulunamadı!")
        else:
            print("{} kelimesi sözlükten silindi!".format(sözcük))
    
    #BURAYA DİKKAT!!!
    if __name__ == '__main__':
        no = input('Yapmak istediğiniz işlemin numarasını girin: ')
        print('1. Sözlükte kelime ara')
        print('2. Sözlüğe kelime ekle')
        print('3. Sözlükten kelime sil')
        
        if no == '1':
            sözcük = input('Aradığınız sözcük: ')
            ara(sözcük)
            
        elif no == '2':
            sözcük = input('Ekleyeceğiniz sözcük: ')
            anlam = input('Eklediğiniz sözcüğün anlamı: ')
            ekle(sözcük, anlam)
            
        elif no == '3':
            sözcük = input('Sileceğiniz sözcük: ')
            sil(sözcük)
            
        else:
            print('Yanlış işlem')    
            
Gördüğünüz gibi, çok basit bir `if` deyimi yardımıyla dosyamızın bağımsız bir
program olarak mı çalıştırıldığını yoksa bir modül olarak içe mi aktarıldığını
kontrol ettik. Eğer ``__name__`` niteliğinin değeri `'__main__'` ise, yani
programımız bağımsız olarak çalıştırılıyorsa `if` bloğu içindeki kodları
işletiyoruz. Eğer bu niteliğin değeri başka bir şey ise (yani modülün adı ise),
bu durumda programımız bir modül olarak içe aktarılıyor demektir. Bu durumda
`if` bloğu içindeki kodları çalıştırmıyoruz...

Her şeyin yolunda olup olmadığını kontrol etmek için `sözlük` modülünü içe
aktaralım::
    
    >>> import sözlük
    
Bu kez, tam da istediğimiz şekilde, programımız doğrudan çalışmaya başlamadan
bize içindeki fonksiyonları kullanma imkanı sundu::
    
    >>> dir(sözlük)

    ['__builtins__', '__cached__', '__doc__', '__file__', 
     '__loader__', '__name__', '__package__', '__spec__', 
     'ara', 'ekle', 'sil', 'sözlük']
     
__loader__ Niteliği
====================

Python'da içe aktarılan bütün modüllerin `__loader__` adlı bir niteliği
bulunur. Bu nitelik, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli
bilgiler veren birtakım araçlar sunar::
    
    >>> import os
    >>> yükleyici = os.__loader__
    
    >>> dir(yükleyici)
    
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
     '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
     '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
     '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
     '__str__', '__subclasshook__', '__weakref__', '_cache_bytecode', 
     'exec_module', 'get_code', 'get_data', 'get_filename', 'get_source', 
     'is_package', 'load_module', 'name', 'path', 'path_mtime', 'path_stats', 
     'set_data', 'source_to_code']
     
Mesela, içe aktardığınız bir modülün kaynak kodlarını görüntülemek için bu
modülden yararlanabilirsiniz::
    
    >>> import webbrowser
    >>> yükleyici = webbrowser.__loader__
    >>> kaynak = yükleyici.get_data(webbrowser.__file__)
    >>> kaynak
    
Burada, daha önce öğrendiğimiz `__file__` niteliğini kullandığımıza dikkat
edin. `__loader__` niteliğinin `get_data()` adlı metodu, parametre olarak,
sorgulayacağımız modülün dizin adresini ister. Bir modülün dizin adresini
`__file__` niteliği yardımıyla elde edebileceğimizi biliyoruz. Dolayısıyla da
`get_data()` metoduna parametre olarak ``webbrowser.__file__`` kodunu
veriyoruz. Elde ettiğimiz şey ise, sorguladığımız modülün kaynak kodlarını
içeren bir bayt (*bytes*) veri tipi oluyor.

`__loader__`, günlük olarak kullanacağımız bir araç değil. Eğer yazdığınız
kodlarda bu niteliğin sunduğu olanaklara ihtiyaç duyarsanız, doğrudan bu nitelik
yerine ``pkgutil`` adlı bir modülü kullanabilirsiniz.

__spec__ Niteliği
====================

`__spec__` niteliği de bize modüller hakkında çeşitli bilgiler sunan birtakım
araçları içinde barındırır. Mesela bir modülün ad ve konum bilgilerine ulaşmak
için bu niteliği kullanabiliriz::
    
    >>> import subprocess
    >>> adı = subprocess.__spec__.name
    >>> konumu = subprocess.__spec__.origin
    >>> adı
    
    'subprocess'
    
    >>> konumu
    
    'C:\\Pythonxy\\lib\\subprocess.py'
    
Tıpkı `__loader__` gibi, bu nitelik de günlük olarak kullanacağımız bir araç
değil. Bu niteliğin içindeki araçların sunduğu bilgileri başka yollardan da elde
edebileceğimizi biliyorsunuz.   
     
__package__ Niteliği
======================

Henüz bu niteliğin ne olduğunu anlayacak bilgiye sahip olmadığımız için, bu
niteliğin incelemesini 'Paketler' konusunu işlediğimiz bölüme bırakıyoruz.

Böylece modüller konusunu tamamlamış olduk. Bu bölümde modüllere ilişkin epey
bilgi verdik. Eğer modüller konusunda aklınıza yatmayan yerler varsa, hiç
ümitsizliğe kapılmadan okumaya devam edin. Birazdan 'sınıflar' konusunu
işlerken, modüllerden ve modüllerin çeşitli özelliklerinden de söz edeceğiz. O
zaman, burada anlamamış olabileceğiniz konuları çok daha net bir şekilde
anlayacaksınız.
