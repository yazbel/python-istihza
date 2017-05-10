.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

*******************************************
Nesne Tabanlı Programlama (Devamı)
*******************************************

.. warning:: Bu makale yoğun bir şekilde geliştirilmekte, içeriği sık sık
 güncellenmektedir.
 
Geçen bölümde verdiğimiz bilgiler sayesinde miras alma konusunun temelini
oluşturan taban sınıf, alt sınıf ve türeme gibi kavramlarla birlikte ``super()``
ve `object` gibi araçların ne olduğunu ve ne işe yaradığını da öğrendik.
Dolayısıyla artık miras alma mekanizmasına dair daha renkli, daha teşvik edici
örnekler verebiliriz. Böylece, belki de gözünüze ilk bakışta pek de matah bir
şey değilmiş gibi görünen bu 'miras alma' denen mekanizmanın aslında ne kadar
önemli bir konu olduğuna sizleri ikna edebiliriz.

Bu bölümde ayrıca geçen bölümlerde incelemeye fırsat bulamasak da nesne tabanlı
programlama kapsamında incelememiz gereken başka konuları da ele alacağız.

Nesne tabanlı programlamadan ilk bahsettiğimiz derste, nesne tabanlı programlama
yaklaşımının grafik arayüz tasarımı için biçilmiş kaftan olduğundan söz etmiştik
hatırlarsanız. Bu bölümde inceleyeceğimiz konuların bazılarını grafik arayüz
tasarımı eşliğinde anlatacağız. Grafik arayüz programlamanın bize sunduğu
düğmeli-menülü görsel programların, nesne tabanlı programlamaya ilişkin soyut
kavramları somut bir düzleme taşımamıza imkan tanıması sayesinde, nesne tabanlı
programlamaya ilişkin çetrefilli konuları daha rahat anlama fırsatı
bulacağız.

Tkinter Hakkında
*******************

Hatırlarsanız, önceki derslerimizde birkaç kez Tkinter adlı bir modülden söz
etmiştik. Tkinter, Python kurulumu ile birlikte gelen ve pencereli-menülü modern
programlar yazmamızı sağlayan grafik arayüz geliştirme takımlarından biridir.

Tkinter bir standart kütüphane paketi olduğu için, Python programlama dilini
kurduğunuzda Tkinter de otomatik olarak kurulur\ [#]_.

Elbette Python'da grafik arayüzlü programlar yazmamızı sağlayacak tek modül
Tkinter değildir. Bunun dışında PyQt, PyGI ve Kivy gibi alternatifler de
bulunur. Ancak Tkinter'in öteki alternatiflere karşı en büyük üstünlüğü hem
öbürlerine kıyasla çok daha kolay olması hem de Python'la birlikte gelmesidir.
PyQt, PyGI ve Kivy'yi kullanabilmek için öncelikle bunları bilgisayarınıza
kurmanız gerekir. Ayrıca Tkinter dışındaki alternatifleri kullanarak yazdığınız
programları dağıtırken, bu arayüz kütüphanelerini kullanıcılarınızın
bilgisayarına ya kendiniz kurmanız ya da kullanıcılarınızdan bu
kütüphaneleri kurmasını talep etmeniz gerekir.

Ben size, ilerde başka arayüz takımlarına geçiş yapacak da olsanız, Tkinter'i
mutlaka öğrenmenizi tavsiye ederim. Hem nesne tabanlı programlama hem de grafik
arayüz geliştirme kavramlarını öğrenmek açısından Tkinter son derece uygun bir
ortamdır.

Biz bu bölümde Tkinter modülünü kullanarak, prosedürel programlama, nesne
tabanlı programlama, sınıflar, miras alma ve nesne programlamaya ilişkin öteki
konular üzerine ufak tefek de olsa bazı çalışmalar yapacağız. Bu çalışmalar
sayesinde bir yandan öğrendiğimiz eski konulara ilişkin güzel bir pratik yapma
imkanı bulacağız, bir yandan Tkinter'in çalışmalarımızın sonucunu görsel bir
şekilde izleme imkanı sağlaması sayesinde nesne tabanlı programlamanın
çetrefilli kavramlarını anlamamız kolaylaşacak, bir yandan da ilk kez gördüğümüz
kodları anlama ve bunlar hakkında fikir yürütme kabiliyeti kazanacağız. Yani bir
taşla tamı tamına üç kuş vurmuş olacağız...

Prosedürel Bir Örnek
**********************

Başta da söylediğimiz gibi, nesne tabanlı programlama, grafik arayüzlü
programlar geliştirmek için son derece uygun bir programlama yaklaşımıdır. Zaten
kendi araştırmalarınız sırasında da, etraftaki grafik arayüzlü programların
büyük çoğunluğunun nesne tabanlı programlama yaklaşımıyla yazıldığını
göreceksiniz. Biz de bu derste vereceğimiz Tkinter örneklerinde sınıflı yapıları
kullanacağız. Ancak dilerseniz Tkinter'in nasıl bir şey olduğunu daha kolay
anlayabilmek için öncelikle nesne tabanlı yaklaşım yerine prosedürel yaklaşımı
kullanarak birkaç küçük çalışma yapalım. Zira özellikle basit kodlarda,
prosedürel yapıyı anlamak nesne tabanlı programlama yaklaşımı ile yazılmış
kodları anlamaktan daha kolaydır. Ancak tabii ki kodlar büyüyüp karmaşıklaştıkça
sınıflı yapıları kullanmak çok daha akıllıca olacaktır.

O halde gelin isterseniz Tkinter modülünü nasıl kullanacağımızı anlamak için,
bir metin dosyası açıp içine şu kodları yazalım::
    
    import tkinter
    
    pencere = tkinter.Tk()
    pencere.mainloop()
       
Bu kodları herhangi bir Python programı gibi kaydedip çalıştırdığınızda boş bir
pencerenin açıldığını göreceksiniz. İşte böylece siyah komut satırından renkli
grafik arayüze geçiş yapmış oldunuz. Hadi hayırlı olsun!

Gördüğünüz gibi, bu kodlarda sınıfları kullanmadık. Dediğimiz gibi, ilk etapta
Tkinter'i daha iyi anlayabilmek için sınıflı yapılar yerine prosedürel bir
yaklaşımı benimseyeceğiz.

Burada öncelikle Tkinter modülünü içe aktardığımıza dikkat edin::
    
    import tkinter
    
Modülü bu şekilde içe aktardığımız için, modül içindeki nitelik ve metotlara
erişmek istediğimizde modülün adını kullanmamız gerekecek. Mesela yukarıda
modülün adını kullanarak, `tkinter` modülü içindeki ``Tk()`` sınıfını
örnekledik::
    
    pencere = tkinter.Tk()
    
Dilerseniz içe aktarma işlemini şu şekilde yaparak işlerimizi biraz daha
kolaylaştırabiliriz::
    
    import tkinter as tk
    
Böylece `tkinter` modülünün nitelik ve metotlarına 'tkinter' yerine 'tk'
önekiyle erişebiliriz::
    
    pencere = tk.Tk()
    
Yukarıdaki kodları yazdığımızda, yani `tkinter` modülünün ``Tk()`` sınıfını
örneklediğimiz anda aslında penceremiz oluştu. Ancak bu pencere örnekleme ile
birlikte oluşmuş olsa da, Tkinter'in iç işleyişi gereği, 'ana döngü' adlı bir
mekanizma çalışmaya başlamadan görünür hale gelmez. İşte bu özel ana döngü
mekanizmasını çalıştırmak ve böylece oluşturduğumuz pencereyi görünür hale
getirmek için, ``Tk()`` sınıf örneklerinin ``mainloop()`` adlı bir metodunu
çalıştıracağız::
    
    pencere.mainloop()
   
Gördüğünüz gibi, ``Tk()`` sınıfını `pencere` adıyla örnekledikten sonra ``Tk()``
sınıfının ``mainloop()`` adlı metoduna `pencere` örneği üzerinden eriştik.
    
Bu ana döngü mekanizmasının benzerlerini Tkinter'in dışındaki öbür grafik arayüz
tasarım araçlarında da göreceksiniz.

Bu arada, yukarıdaki prosedürel örnekte bile, biz istemesek de sınıflarla
muhatap olduğumuza dikkatinizi çekmek isterim. Çünkü kullandığımız `tkinter`
modülünün kendisi halihazırda birtakım sınıflardan oluşuyor. Dolayısıyla bu
modülü içe aktardığımızda, kodlarımızın içine pek çok sınıfı ister istemez dahil
etmiş oluyoruz. Esasında sırf bu durum bile, grafik arayüzlü programlarda neden
nesne tabanlı programlamanın tercih edildiğini gayet güzel gösteriyor bize.
Neticede, kullandığımız harici kaynaklardan ötürü her şekilde sınıflarla ve
nesne tabanlı yapılarla içli dışlı olacağımız için, kendi yazdığımız kodlarda da
nesne tabanlı yapılardan kaçmamızın hiçbir gerekçesi yok.

Neyse... Biz konumuza dönelim...

Yukarıda Tkinter modülünü kullanarak boş bir pencere oluşturduk. Gelin
isterseniz bu boş pencere üzerinde birtakım değişiklikler yapalım.

Öncelikle `tkinter` modülümüzü içe aktaralım::
    
    import tkinter as tk
    
Şimdi bu modülün ``Tk()`` adlı sınıfını örnekleyelim::
    
    pencere = tk.Tk()
    
Böylece penceremizi oluşturmuş olduk. Tkinter'le verdiğimiz ilk örnekte de
gördüğünüz gibi, Tkinter'le oluşturulan boş bir pencere öntanımlı olarak 200
piksel genişliğe ve 200 piksel yüksekliğe sahip olacaktır. Ancak isterseniz,
``Tk()`` sınıfının ``geometry()`` adlı metodunu kullanarak, pencere boyutunu
ayarlayabilirsiniz (``Tk()`` sınıfının hangi metotlara sahip olduğunu görmek
için ``dir(pencere)`` komutunu verebileceğinizi biliyorsunuz)::
    
    import tkinter as tk
    
    pencere = tk.Tk()
    pencere.geometry('200x70')
    
    pencere.mainloop()
    
Kendi yazdığımız sınıflardaki nitelik ve metotlara nasıl erişiyorsak, ``Tk()``
sınıfının nitelik ve metotlarına da aynı şekilde eriştiğimize dikkat edin.
Neticede bizim yazdıklarımız da sınıftır, ``Tk()`` da sınıftır. ``Tk()``
sınıfının bizimkilerden tek farkı, ``Tk()`` sınıfının Python geliştiricilerince
yazılmış olmasıdır. Yazarları farklı olsa da bütün sınıflar aynı kurallara
tabidir. Dolayısıyla ilgili sınıfı kullanabilmek için önce sınıfımızı
örnekliyoruz, ardından da bu sınıf içinde tanımlı olan nitelik ve metotlara
noktalı gösterim tekniğini kullanarak ulaşıyoruz. Burada da ``Tk()`` sınıf
örneklerinin ``geometry()`` metodunu kullanarak 200x200 yerine 200x70
boyutlarında bir pencere oluşturduk::
    
    pencere.geometry('200x70')

Şimdi bu boş pencereye bir etiket bir de düğme ekleyelim::
    
    import tkinter as tk
    
    pencere = tk.Tk()
    pencere.geometry('200x70')
    
    etiket = tk.Label(text='Merhaba Zalim Dünya')
    etiket.pack()
    
    düğme = tk.Button(text='Tamam', command=pencere.destroy)
    düğme.pack()
    
    pencere.mainloop() 
    
Burada `tkinter` modülünün ``Tk()`` sınıfına ek olarak, aynı modülün ``Label()``
ve ``Button()`` adlı iki sınıfını daha kullandık. ``Label()`` sınıfı etiketler,
``Button()`` sınıfı ise düğmeler oluşturmamızı sağlıyor. Bu sınıfların örnekleri
üzerinde çalıştırdığımız ``pack()`` metodunu ise, etiket ve düğmeleri pencere
üzerine yerleştirmek için kullanıyoruz.

``Label()`` ve ``Button()`` sınıflarının `text` adlı bir parametre aldığını
görüyorsunuz. Bu parametrenin değeri, etiket veya düğmenin üzerinde ne
yazacağını gösteriyor. 

Bu kodları da tıpkı başka Python programlarını çalıştırdığınız gibi
çalıştırabilirsiniz.

Bu arada, Tkinter'de bir şeyi oluşturmanın ve görünür hale getirmenin iki farklı
işlem gerektirdiğine özellikle dikkat edin. Mesela üzerinde 'Merhaba Zalim
Dünya' yazan bir etiket oluşturmak için şu kodu kullanıyoruz::
    
    etiket = tk.Label(text='Merhaba Zalim Dünya')
    
Bu etiketi pencere üzerine yerleştirmek, yani görünür hale getirmek için ise şu
komutu kullanıyoruz::
    
    etiket.pack()
    
Aynı şekilde bir düğme oluşturmak için de şu komutu kullanıyoruz::
    
    düğme = tk.Button(text='Tamam', command=pencere.destroy)

Böylece üzerinde 'Tamam' yazan ve tıklandığında pencereyi kapatan bir düğme
oluşturmuş oluyoruz. Düğmenin üzerine tıklandığında ne olacağını ``Button()``
sınıfının `command` parametresi aracılığıyla belirledik. Bu parametreye,
`pencere` örneğinin ``destroy()`` metodunu verdiğimizde pencereye kapatma
sinyali gönderilecektir. Yalnız bu metodu yazarken parantez işaretlerini
kullanmadığımıza dikkat edin. Eğer metodu ``pencere.destroy()`` şeklinde
parantezli bir biçimde yazarsak, kapatma komutu daha düğmeye basmadan çalışacak
ve bu durumda düğmemiz düzgün işlemeyecektir.

Tıpkı etikette olduğu gibi, düğmemizi de pencere üzerine yerleştirmek, yani
görünür hale getirmek için ``pack()`` metodundan yararlanıyoruz::
    
    düğme.pack()
    
Bunun, ``Tk()`` sınıfı ile ``mainloop()`` metodu arasındaki ilişkiye benzediğine
dikkatinizi çekmek isterim: Tıpkı ``pack()`` metoduna benzer bir şekilde,
``Tk()`` sınıfı yardımıyla da bir pencere oluşturduktan sonra, bu pencerenin
görünür hale gelebilmesi için ``mainloop()`` metodunu çalıştırmamız gerektiğini
hatırlıyorsunuz.

Bu kodlarda Tkinter'e ilişkin ayrıntılardan ziyade, sınıflı yapıları kodlarımıza
nasıl dahil ettiğimize ve bunları nasıl kullandığımıza odaklanmanızı istiyorum.
Gördüğünüz gibi, `tkinter` modülünden içe aktardığımız ``Tk()``, ``Label()`` ve
``Button()`` gibi sınıfların metot ve niteliklerini, mesela tıpkı karakter
dizilerinin metot ve niteliklerini kullanır gibi kullanıyoruz.

Yukarıdaki örnekte, `tkinter` modülünün sınıflarını, kodlarımız içine prosedürel
olarak dahil ettik. Yani her sınıfı, belli bir sıraya göre kodlarımız içinde
belirtip, bunları adım adım çalıştırdık. Prosedürel programlamada kodların
yazılış sırası çok önemlidir. Bunu kanıtlamak için çok basit bir örnek verelim::
    
    import tkinter as tk
    
    pencere = tk.Tk()
    
    def çıkış():
        etiket['text'] = 'Elveda zalim dünya...'
        düğme['text'] = 'Bekleyin...'
        düğme['state'] = 'disabled'
        pencere.after(2000, pencere.destroy)
    
    etiket = tk.Label(text='Merhaba Zalim Dünya')
    etiket.pack()
    
    düğme = tk.Button(text='Çık', command=çıkış)
    düğme.pack()
    
    pencere.protocol('WM_DELETE_WINDOW', çıkış)
    
    pencere.mainloop()   
    
Burada herzamanki gibi öncelikle gerekli modülü içe aktardık::
    
    import tkinter as tk
    
Daha sonra ``Tk()`` sınıfı yardımıyla penceremizi oluşturduk::
    
    pencere = tk.Tk()
    
Ardından ``çıkış()`` adlı bir fonksiyon tanımladık::
    
    def çıkış():
        etiket['text'] = 'Elveda zalim dünya...'
        düğme['text'] = 'Bekleyin...'
        düğme['state'] = 'disabled'
        pencere.after(2000, pencere.destroy)    
        
Bu fonksiyon, pencere kapatılırken hangi işlemlerin yapılacağını belirliyor.
Buna göre, programdan çıkılırken sırasıyla şu işlemleri gerçekleştiriyoruz: 

#. Etiketin `text` parametresini 'Elveda zalim dünya...' olarak değiştiriyoruz.
#. Düğmenin `text` parametresini 'Bekleyin...' olarak değiştiriyoruz.
#. Düğmenin `state` parametresini 'disabled' olarak değiştirerek düğmeyi basılamaz
   hale getiriyoruz.
#. 2000 milisaniye (yani 2 saniye) sonra ise ``pencere.destroy()`` komutunu
   işleterek pencerenin kapanmasını sağlıyoruz.   
   
``çıkış()`` fonksiyonunu tanımladıktan sonra ``Label()`` ve ``Button()``
düğmeleri aracılığıyla etiket ve düğmelerimizi oluşturuyoruz::

    etiket = tk.Label(text='Merhaba Zalim Dünya')
    etiket.pack()
    
    düğme = tk.Button(text='Çık', command=çıkış)
    düğme.pack()
    
Buna göre, düğmeye basıldığında, `command` parametresinin değeri olan
``çıkış()`` fonksiyonu çalışmaya başlayacak ve fonksiyon gövdesinde
tanımladığımız işlemler gerçekleşecek.

Bildiğiniz gibi, bir program penceresinde, o programı kapatmayı sağlayacak
düğmelerin yanısıra, bir de en üst sağ (veya sol) köşede program penceresini
kapatan bir 'X' düğmesi bulunur. İşte bu 'X' düğmesine basıldığında da pencere
kapanmadan önce ``çıkış()`` fonksiyonunun çalışması için şu kodu yazıyoruz::
    
    pencere.protocol('WM_DELETE_WINDOW', çıkış)

``protocol()`` de tıpkı ``geometry()`` gibi, ``Tk()`` sınıfının metotlarından
biridir. Bu metodu `WM_DELETE_WINDOW` argümanıyla birlikte kullanarak, pencere
üzerindeki 'X' düğmesine basıldığında neler olacağını tanımlayabiliyoruz.

Son olarak da ana döngü mekanizmasını çalıştırıyoruz ve penceremizi görünür hale
getiriyoruz::
    
    pencere.mainloop()
    
Bu prosedürel kodları tekrar önümüze alalım::
    
    import tkinter as tk
    
    pencere = tk.Tk()
    
    def çıkış():
        etiket['text'] = 'Elveda zalim dünya...'
        düğme['text'] = 'Bekleyin...'
        düğme['state'] = 'disabled'
        pencere.after(2000, pencere.destroy)
    
    etiket = tk.Label(text='Merhaba Zalim Dünya')
    etiket.pack()
    
    düğme = tk.Button(text='Çık', command=çıkış)
    düğme.pack()
    
    pencere.protocol('WM_DELETE_WINDOW', çıkış)
    
    pencere.mainloop()
    
En başta da söylediğimiz gibi, bu kodlarda, satır sıraları çok önemlidir. Mesela
burada düğmeyi oluşturan kodlarla ``pencere.protocol()`` kodlarının çalışması
için bunların mutlaka ``çıkış()`` fonksiyonu tanımlandıktan sonra yazılması
gerekir. Eğer bu kodları şöyle yazarsanız::

    import tkinter as tk
    
    pencere = tk.Tk()
    pencere.protocol('WM_DELETE_WINDOW', çıkış)
        
    def çıkış():
        etiket['text'] = 'Elveda zalim dünya...'
        düğme['text'] = 'Bekleyin...'
        düğme['state'] = 'disabled'
        pencere.after(2000, pencere.destroy)
        
    etiket = tk.Label(text='Merhaba Zalim Dünya')
    etiket.pack()
    
    düğme = tk.Button(text='Çık', command=çıkış)
    düğme.pack()
    
    pencere.mainloop()   
    
... programınız çalışmayacaktır.

Bu durum, programcıyı, istediği kod düzenini oturtmak konusunda epey kısıtlar.
Ama eğer nesne tabanlı programlama yaklaşımını kullanırsak kod akışını
belirlerken daha özgür olabiliriz. Ayrıca prosedürel yaklaşımda kodlar büyüdükçe
programınızın çorbaya dönme ihtimali nesne tabanlı programlama yaklaşımına göre
daha fazladır. Ancak elbette nesne tabanlı programlama yaklaşımını kullanmak tek
başına düzgün ve düzenli kod yazmanın teminatı değildir. Nesne tabanlı
programlama yaklaşımını kullanarak da gayet sebze çorbası kıvamında kodlar
yazabilirsiniz. En başta da söylediğimiz gibi, nesne tabanlı programlama bir
seçenektir. Eğer istemezseniz, nesne tabanlı programlama yaklaşımını kullanmak
zorunda değilsiniz. Ama elinizde böyle bir imkanınız olduğunu ve başkalarının da
bu yaklaşımdan yoğun bir şekilde faydalandığını bilmek çok önemlidir.

Sınıflı Bir Örnek
**********************

Bir önceki başlıkta Tkinter'i kullanılarak prosedürel bir kod yazdık. Peki acaba
yukarıdaki kodları nesne tabanlı olarak nasıl yazabiliriz?

Dikkatlice bakın::
    
    import tkinter as tk
    
    class Pencere(tk.Tk):
        def __init__(self):
            super().__init__()
            self.protocol('WM_DELETE_WINDOW', self.çıkış)
            
            self.etiket = tk.Label(text='Merhaba Zalim Dünya')
            self.etiket.pack()
            
            self.düğme = tk.Button(text='Çık', command=self.çıkış)
            self.düğme.pack()
            
        def çıkış(self):
            self.etiket['text'] = 'Elveda zalim dünya...'
            self.düğme['text'] = 'Bekleyin...'
            self.düğme['state'] = 'disabled'
            self.after(2000, self.destroy)
            
    pencere = Pencere()
    pencere.mainloop()
    
Bu kodlarda gördüğünüz bütün satırları anlayacak kadar nesne tabanlı programlama
bilgisine sahipsiniz. Ama gelin biz yine de bu kodları sizin için tek tek ve
tane tane açıklayalım.

Öncelikle `tkinter` modülünü `tk` adıyla içe aktarıyoruz::
    
    import tkinter as tk
    
Daha sonra ``Pencere()`` adlı sınıfımızı tanımlamaya başlıyoruz::
    
    class Pencere(tk.Tk):
        ...
            
Burada öncelikle ``Tk()`` sınıfını miras aldığımıza dikkat edin. Bu sayede bu
sınıfın içindeki bütün nitelik ve metotları kendi uygulamamız içinden
çağırabileceğiz. 

Penceremiz oluşur oluşmaz pencere üzerinde bir etiket ile bir düğme olmasını
planlıyoruz. Pencere oluşur oluşmaz işletilecek kodları tanımlamak için bir
``__init__()`` metoduna ihtiyacımız olduğunu biliyorsunuz:: 

    class Pencere(tk.Tk):
        def __init__(self):
            ...

Ancak kendi ``__init__()`` metodumuzu tanımlarken, ``Tk()`` sınıfının kendi
``__init__()`` metodundaki işlemleri de gölgelemememiz lazım. Dolayısıyla
orijinal ``__init__()`` metodunu kendi ``__init__()`` metodumuza aktarmak için
``super()`` fonksiyonundan yararlanacağız::
    
    class Pencere(tk.Tk):
        def __init__(self):
            super().__init__()
    
Artık taban sınıfın ``__init__()`` metodunu kendi tanımladığımız alt sınıfın
``__init__()`` metodu içinden özelleştirmeye başlayabiliriz. Öncelikle şu satırı
yazıyoruz::
    
    self.protocol('WM_DELETE_WINDOW', self.çıkış)

``protocol()`` metodunun öntanımlı davranışı, pencerenin 'X' düğmesine
basıldığında programı sonlandırmaktır. İşte biz bu öntanımlı davranışı
değiştirmek için ``protocol()`` metodunu içeren kodu tekrar tanımlıyoruz ve
'X' düğmesine basıldığında ``çıkış()`` fonksiyonunun çalışmasını sağlıyoruz.

Daha sonra normal bir şekilde etiketimizi ve düğmemizi tanımlıyoruz::
    
    self.etiket = tk.Label(text='Merhaba Zalim Dünya')
    self.etiket.pack()
    
    self.düğme = tk.Button(text='Çık', command=self.çıkış)
    self.düğme.pack()

İki farklı yerde atıfta bulunduğumuz ``çıkış()`` fonksiyonumuz ise şöyle::
    
    def çıkış(self):
        self.etiket['text'] = 'Elveda zalim dünya...'
        self.düğme['text'] = 'Bekleyin...'
        self.düğme['state'] = 'disabled'
        self.after(2000, self.destroy)
        
Son olarak da şu kodları yazıp programımızı tamamlıyoruz::
    
    pencere = Pencere()
    pencere.mainloop()

Elbette zevkler ve renkler tartışılmaz, ancak ben yukarıdaki kodları, prosedürel
kodlara göre çok daha düzgün, düzenli, anlaşılır ve okunaklı bulduğumu, bu
kodlara baktığımda, programı oluşturan parçaların prosedürel kodlara kıyasla
daha yerli yerinde olduğunu düşündüğümü söylemeden de geçmeyeceğim...

Eğer siz aksini düşünüyorsanız sizi prosedürel yolu tercih etmekten alıkoyan
hiçbir şeyin olmadığını da bilin. Ancak tabii ki bu, nesne tabanlı
programlamadan kaçabileceğiniz anlamına da gelmiyor! Unutmayın, bu yaklaşımı siz
kullanmasanız da başkaları kullanıyor.

Çoklu Miras Alma
******************

Python'da bir sınıf, aynı anda birden fazla sınıfı da miras alabilir. Eğer
yazdığınız bir uygulamada birden fazla taban sınıftan nitelik ve metot miras
almanız gerekirse bunu şu şekilde gerçekleştirebilirsiniz::
    
    class Sınıf(taban_sınıf1, taban_sınıf2):
        pass
        
Bu şekilde hem `taban_sınıf1` hem de `taban_sınıf2`'de bulunan nitelik ve
metotlar aynı anda `Sınıf` adlı sınıfa dahil olacaktır.

Ufak bir örnek verelim. Diyelim ki elimizde şu sınıflar var::
    
    class c1:
        sn1 = 'sn1'
        
        def __init__(self):
            self.ön1 = 'ön1'
            print(self.ön1)
        
        def örn_metot1(self):
            self.öm1 = 'öm1'
            return self.öm1
            
    class c2:
        sn2 = 'sn2'
        
        def __init__(self):
            self.ön2 = 'ön2'
            print(self.ön2)
        
        def örn_metot2(self):
            self.öm2 = 'öm2'
            return self.öm2
            
    class c3:
        sn3 = 'sn3'
        
        def __init__(self):
            self.ön3 = 'ön3'
            print(self.ön3)
            
        def örn_metot3(self):
            self.öm3 = 'öm3'
            return self.öm3
        
Burada üç farklı sınıf ve herbir sınıfın içinde de birer sınıf niteliği, birer
``__init__()`` metodu, birer örnek niteliği ve birer örnek metodu görüyoruz.

Şimdi bu üç sınıfı birden taban sınıf olarak miras alan dördüncü bir sınıf
tanımlayalım::
    
    class c4(c1, c2, c3):
        pass
        
Burada, taban sınıf vazifesi görecek sınıfların adını ``c4`` sınıfının
parantezleri arasına tek tek yerleştirdiğimize dikkat edin. Bu şekilde ``c1``,
``c2`` ve ``c3`` adlı sınıfları aynı anda miras almış oluyoruz. İşte bu
mekanizmaya Python'da çoklu miras alma (*multiple inheritance*) adı veriliyor.

Tek bir sınıfı miras aldığınızda hangi kurallar geçerliyse, birden fazla sınıfı
miras aldığınızda da temel olarak aynı kurallar geçerlidir. Ancak çoklu miras
almada birden fazla sınıf söz konusu olduğu için, miras alınan sınıfların da
kendi aralarında veya başka sınıflarla nitelik ve/veya metot alışverişi yapması
halinde ortaya çıkabilecek beklenmedik durumlara karşı dikkatli olmalısınız.
Ayrıca çoklu miras alma işlemi sırasında, aynı adı taşıyan metotlardan yalnızca
birinin miras alınacağını da unutmayın.

Örneğin::
    
    class c1:
        sn1 = 'sn1'
        
        def __init__(self):
            self.ön1 = 'ön1'
            print(self.ön1)
        
        def örn_metot1(self):
            self.öm1 = 'öm1'
            return self.öm1
            
        def ortak_metot(self):
            self.om = 'ortak metot_c1'
            return self.om
            
    class c2:
        sn2 = 'sn2'
        
        def __init__(self):
            self.ön2 = 'ön2'
            print(self.ön2)
        
        def örn_metot2(self):
            self.öm2 = 'öm2'
            return self.öm2
        
        def ortak_metot(self):
            self.om = 'ortak metot_c2'
            return self.om
            
    class c3:
        sn3 = 'sn3'
        
        def __init__(self):
            self.ön3 = 'ön3'
            print(self.ön3)
            
        def örn_metot3(self):
            self.öm3 = 'öm3'
            return self.öm3
            
        def ortak_metot(self):
            self.om = 'ortak metot_c3'
            return self.om
            
    class c4(c1, c2, c3):
        def __init__(self):
            super().__init__()    
    
Burada, aynı adı taşıyan ``__init__()`` ve ``ortak_metot()`` adlı metotlardan
yalnızca biri miras alınacaktır. Bunlardan hangisinin miras alınacağını az çok
tahmin etmişsinizdir. Evet, doğru bildiniz. Miras alma listesinde hangi sınıf
önde geliyorsa onun metotları miras alınacaktır::
    
    s = c4()
    print(s.ortak_metot())
    
Gördüğünüz gibi, ``c4()`` sınıfı önce ``c1`` sınıfını miras aldığı için hep
``c1`` sınıfının metotları öncelik kazanıyor.

Eğer sınıfları ``class c4(c2, c3, c1):`` şeklinde miras alsaydık, bu kez de
``c2`` sınıfının metotları öncelik kazanacaktı.

Elbette, Python'ın sizin için belirlediği öncelik sırası yerine kendi
belirlediğiniz öncelik sırasını da dayatabilirsiniz::
        
    class c4(c1, c2, c3):
        def __init__(self):
            c2.__init__(self)
        
        def ortak_metot(self):
            return c3.ortak_metot(self)
            
Burada ``c2`` sınıfının ``__init__()`` metodu ile ``c3`` sınıfının
``ortak_metot``'una miras önceliği verdik.

Dahil Etme
***********

Bir sınıftaki nitelik ve metotları başka bir sınıf içinde kullanmanın tek yolu
ilgili sınıf veya sınıfları miras almak değildir. Hatta bazı durumlarda, miras
alma iyi bir yöntem dahi olmayabilir. Özellikle birden fazla sınıfa ait nitelik
ve metotlara ihtiyaç duyduğumuzda, çoklu miras alma yöntemini kullanmak yerine,
dahil etme (*composition*) denen yöntemi tercih edebiliriz.

Peki nedir bu dahil etme denen şey? Adından da anlaşılacağı gibi, dahil etme
yönteminde, taban sınıfın nitelik ve metotlarını miras almak yerine, alt sınıf
içine dahil ediyoruz. Esasında biz bunun örneğini görmüştük. Şu kodu
hatırlıyorsunuz::
    
    import tkinter as tk
    
    class Pencere(tk.Tk):
        def __init__(self):
            super().__init__()
            self.protocol('WM_DELETE_WINDOW', self.çıkış)
            
            self.etiket = tk.Label(text='Merhaba Zalim Dünya')
            self.etiket.pack()
            
            self.düğme = tk.Button(text='Çık', command=self.çıkış)
            self.düğme.pack()
            
        def çıkış(self):
            self.etiket['text'] = 'Elveda zalim dünya...'
            self.düğme['text'] = 'Bekleyin...'
            self.düğme['state'] = 'disabled'
            self.after(2000, self.destroy)
            
    pencere = Pencere()
    pencere.mainloop()
    
Burada aynı anda hem miras alma hem de dahil etme yönteminden yararlanıyoruz.
İlk önce ``Tk()`` sınıfını miras aldık. Böylece bu sınıfın nitelik ve
metotlarına doğrudan erişim elde ettik. Etiket ve düğme oluşturmamızı sağlayan
``Label()`` ve ``Button()`` sınıflarını ise ``Pencere()`` sınıfımız içine dahil
ettik. Böylece bu sınıfların nitelik ve metotlarına sırasıyla `self.etiket` ve
`self.düğme` adları altında erişim kazandık.

Miras alma ve dahil etme yöntemleri arasında tercih yaparken genel yaklaşımımız
şu olacak: Eğer yazdığımız uygulama, bir başka sınıfın türevi ise, o sınıfı
miras alacağız. Ama eğer bir sınıf, yazdığımız uygulamanın bir parçası ise o
sınıfı uygulamamıza dahil edeceğiz.

Yani mesela yukarıdaki örnekte temel olarak yaptığımız şey bir uygulama
penceresi tasarlamaktır. Dolayısıyla uygulama penceremiz, ``tk.Tk()`` sınıfının
doğrudan bir türevidir. O yüzden bu sınıfı miras almayı tercih ediyoruz. 

Pencere üzerine etiket ve düğme yerleştirmemizi sağlayan ``Label()`` ve
``Button()`` sınıfları ise, uygulama penceresinin birer parçasıdır. Dolayısıyla
bu sınıfları uygulamamız içine dahil ediyoruz.

Yukarıda anlattığımız iki farklı ilişki türü 'olma ilişkisi' (*is-a
relationship*) ve 'sahiplik ilişkisi' (*has-a relationship*) olarak
adlandırılabilir. Olma ilişkisinde, bir sınıf ötekinin türevidir. Sahip olma
ilişkisinde ise bir sınıf öteki sınıfın parçasıdır. Eğer iki sınıf arasında
'olma ilişkisi' varsa miras alma yöntemini kullanıyoruz. Ama eğer iki sınıf
arasında 'sahiplik ilişkisi' varsa dahil etme yöntemini kullanıyoruz.

.. rubric:: Dipnotları:

.. [#] GNU/Linux dağıtımlarında, dağıtımı geliştiren ekip genellikle
 Tkinter paketini Python paketinden ayırdığı için, Tkinter'i ayrıca kurmanız
 gerekebilir. Eğer Python'ın etkileşimli kabuğunda ``import tkinter`` komutunu
 verdiğinizde bir hata mesajı alıyorsanız http://www.istihza.com/forum
 adresinden yardım isteyin. Eğer Windows kullanıyorsanız, böyle bir probleminiz
 yok. Python'ı kurduğunuz anda Tkinter de emrinize amadedir.
 

 