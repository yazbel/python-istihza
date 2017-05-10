.. meta:: :description: Bu bölümde Python'daki kaçış dizilerinden (escape sequences) 
           söz edeceğiz. 
          :keywords: python, kaçış dizileri, escape sequences, satır başı, tab, 
           sekme 
           
.. highlight:: py3

**************** 
Kaçış Dizileri 
****************

Python'da karakter dizilerini tanımlayabilmek için tek, çift veya üç tırnak
işaretlerinden faydalandığımızı geçen bölümde öğrenmiştik. Python bir verinin
karakter dizisi olup olmadığına bu tırnak işaretlerine bakarak karar verdiği
için, tek, çift ve üç tırnak işaretleri Python açısından özel bir önem taşıyor.
Zira Python'ın gözünde bir başlangıç tırnağı ile bitiş tırnağı arasında yer alan
her şey bir karakter dizisidir. 

Örneğin ilk olarak bir `"` işareti koyup ardından `"elma` şeklinde devam
ettiğinizde, Python ilk tırnağı gördükten sonra karakter dizisini
tanımlayabilmek için ikinci bir tırnak işareti aramaya başlar. Siz `"elma"`
şeklinde kodunuzu tamamladığınızda ise Python bellekte `"elma"` adlı bir
karakter dizisi oluşturur.

Bu noktada size şöyle bir soru sormama izin verin: Acaba tırnak işaretleri
herhangi bir metin içinde kaç farklı amaçla kullanılabilir? 

İsterseniz bu sorunun cevabını örnekler üzerinde vermeye çalışalım:

    Ahmet, "Bugün sinemaya gidiyorum," dedi.

Burada tırnak işaretlerini, bir başkasının sözlerini aktarmak için kullandık.

    'book' kelimesi Türkçede 'kitap' anlamına gelir.

Burada ise tırnak işaretlerini bazı kelimeleri vurgulamak için kullandık. 

Bir de şuna bakalım:

    Yarın Adana'ya gidiyorum. 
    
Burada da tırnak işaretini, çekim eki olan '-(y)a' ile özel isim olan 'Adana'
kelimesini birbirinden ayırmak için kesme işareti görevinde kullandık.

Şimdi yukarıda verdiğimiz ilk cümleyi bir karakter dizisi olarak tanımlamaya
çalışalım::

    >>> 'Ahmet, "Bugün sinemaya gidiyorum," dedi.'

Burada karakter dizisini tanımlamaya tek tırnak işareti ile başladık. Böylece
Python bu karakter dizisini tanımlama işlemini bitirebilmek için ikinci bir tek
tırnak işareti daha aramaya koyuldu ve aradığı tek tırnak işaretini cümlenin
sonunda bularak, karakter dizisini düzgün bir şekilde oluşturabildi.

Dediğimiz gibi, Python'ın gözünde tırnak işaretleri bir karakter dizisini başka
veri tiplerinden ayırt etmeye yarayan bir ölçüttür. Ama biz insanlar, yukarıda
verdiğimiz örnek cümlelerden de göreceğiniz gibi, programlama dillerinden farklı
olarak, tırnak işaretlerini bir metin içinde daha farklı amaçlar için de
kullanabiliyoruz.

Şimdi yukarıdaki karakter dizisini şöyle tanımlamaya çalıştığımızı düşünün::

    >>> "Ahmet, "Bugün sinemaya gidiyorum," dedi."

İşte burada Python'ın çıkarları ile bizim çıkarlarımız birbiriyle çatıştı.
Python karakter dizisini başlatan ilk çift tırnak işaretini gördükten sonra,
karakter dizisini tanımlama işlemini bitirebilmek için ikinci bir tırnak işareti
daha aramaya koyuldu. Bu arayış sırasında da 'Bugün' kelimesinin başındaki çift
tırnak işaretini gördü ve karakter dizisinin şu olduğunu zannetti::

    >>> "Ahmet, "

Buraya kadar bir sorun yok. Bu karakter dizisi Python'ın sözdizimi kurallarına
uygun.

Karakter dizisi bu şekilde tanımlandıktan sonra Python cümlenin geri kalanını
okumaya devam ediyor ve herhangi bir tırnak işareti ile başlamayan ve
kendisinden önce gelen öğeden herhangi bir virgül işareti ile ayrılmamış 'Bugün'
kelimesini görüyor. Eğer bir kelime tırnak işareti ile başlamıyorsa bu kelime ya
bir değişkendir ya da sayıdır. Ama 'Bugün' kelimesi ne bir değişken, ne de bir
sayı olduğu, üstelik önceki öğeden de virgülle ayrılmadığı için Python'ın hata
vermekten başka çaresi kalmıyor. Çünkü biz burada 'Bugün' kelimesinin baş
tarafındaki çift tırnak işaretini karakter dizisi tanımlamak için değil,
başkasının sözlerini aktarmak amacıyla kullandık. Ancak elbette bir programlama
dili bizim amacımızın ne olduğunu kestiremez ve hata mesajını suratımıza
yapıştırır::

      File "<stdin>", line 1
        "Ahmet, "Bugün sinemaya gidiyorum," dedi."
                      ^
    SyntaxError: invalid syntax

Peki biz böyle bir durumda ne yapmalıyız?

Bu hatayı engellemek için karakter dizisini tanımlamaya çift tırnak yerine tek
tırnakla ya da üç tırnakla başlayabiliriz::

    >>> 'Ahmet, "Bugün sinemaya gidiyorum," dedi.'

... veya:: 

    >>> """Ahmet, "Bugün sinemaya gidiyorum," dedi.""" 

Böylece karakter dizisini başlatan işaret 'Bugün sinemaya gidiyorum,' cümlesinin
başındaki ve sonundaki işaretlerden farklı olduğu için, Python okuma esnasında
bu cümleye takılmaz ve doğru bir şekilde, karakter dizisini kapatan tırnak
işaretini bulabilir.

Bu yöntem tamamen geçerli ve mantıklıdır. Ama eğer istersek, aynı karakter
dizisini çift tırnakla tanımlayıp, yine de hata almayı engelleyebiliriz. Peki
ama nasıl?

İşte burada 'kaçış dizileri' adı verilen birtakım araçlardan faydalanacağız.

Peki nedir bu 'kaçış dizisi' denen şey?

Kaçış dizileri, Python'da özel anlam taşıyan işaret veya karakterleri, sahip
oldukları bu özel anlam dışında bir amaçla kullanmamızı sağlayan birtakım
araçlardır. Mesela yukarıda da örneklerini verdiğimiz gibi, tırnak işaretleri
Python açısından özel anlam taşıyan işaretlerdir. Normalde Python bu işaretleri
karakter dizilerini tanımlamak için kullanır. Ama eğer siz mesela bir metin
içinde bu tırnak işaretlerini farklı bir amaçla kullanacaksanız Python'ı bu
durumdan haberdar etmeniz gerekiyor. İşte kaçış dizileri, Python'ı böyle bir
durumdan haberdar etmemize yarayan araçlardır.

Python'da pek çok kaçış dizisi bulunur. Biz burada bu kaçış dizilerini tek tek
inceleyeceğiz. O halde hemen işe koyulalım.

Ters Taksim (\\) 
*****************

Yukarıda verdiğimiz örneklerde, çift tırnakla gösterdiğimiz karakter dizilerinin
içinde de çift tırnak işareti kullanabilmek için birkaç farklı yöntemden
yararlanabildiğimizi öğrenmiştik. Buna göre, eğer bir karakter dizisi içinde
çift tırnak işareti geçiyorsa, o karakter dizisini tek tırnakla; eğer tek tırnak
geçiyorsa da o karakter dizisini çift tırnakla tanımlayarak bu sorunun
üstesinden gelebiliyorduk. Ama daha önce de söylediğimiz gibi, 'kaçış dizileri'
adı verilen birtakım araçları kullanarak, mesela içinde çift tırnak geçen
karakter dizilerini yine çift tırnakla tanımlayabiliriz.

Dilerseniz, kaçış dizisi kavramını açıklamaya geçmeden önce bununla ilgili
birkaç örnek verelim. Bu sayede ne ile karşı karşıya olduğumuz, zihnimizde biraz
daha belirginleşebilir::

    >>> print('Yarın Adana\'ya gidiyorum.') 
    
    Yarın Adana'ya gidiyorum.

Bir örnek daha verelim::

    >>> print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.")
    
    "book" kelimesi Türkçede "kitap" anlamına gelir.

Burada da cümle içinde çift tırnak işaretlerini kullandığımız halde, `\\`
işaretleri sayesinde karakter dizilerini yine çift tırnakla tanımlayabildik.

Bir de şu örneğe bakalım::

    >>> print("Python programlama dilinin adı \"piton\" yılanından gelmez")
    
Bütün bu örneklerde, karakter dizisini hem çift tırnakla tanımlayıp hem de
karakter dizisi içinde çift tırnak işaretlerini kullandığımız halde, herhangi
bir hata almadığımızı görüyorsunuz. Yukarıdaki kodlarda hata almamızı önleyen
şeyin `\\` işareti olduğu belli. Ama dilerseniz bu işaretin, hata almamızı nasıl
önlediğini anlatmadan önce son bir örnek daha verelim.

Hatırlarsanız önceki sayfalarda şöyle bir karakter dizisi ile karşılaşmıştık::

    >>> print('İstanbul'un 5 günlük hava durumu tahmini')

      File "<stdin>", line 1
        print('İstanbul'un 5 günlük hava durumu tahmini')
                          ^
    SyntaxError: invalid syntax
    
Burada da 'İstanbul'un' kelimesi içinde geçen tırnak işareti nedeniyle karakter
dizisini tek tırnak kullanarak tanımlayamıyorduk. Bu karakter dizisini hatasız
bir şekilde tanımlayabilmek için ya çift tırnak ya da üç tırnak kullanmamız
gerekiyordu::

    >>> print("İstanbul'un 5 günlük hava durumu tahmini")

    İstanbul'un 5 günlük hava durumu tahmini

... veya::

    >>> print("""İstanbul'un 5 günlük hava durumu tahmini""")

    İstanbul'un 5 günlük hava durumu tahmini 
    
Tıpkı önceki örneklerde olduğu gibi, yukarıdaki karakter dizisini de aslında tek
tırnakla tanımlayıp hata oluşmasını önleyebiliriz. Hemen görelim::

    >>> print('İstanbul\'un 5 günlük hava durumu tahmini')

    İstanbul'un 5 günlük hava durumu tahmini

Bütün örneklerde `\\` işaretini kullandığımızı görüyorsunuz. İşte bu tür
işaretlere Python'da kaçış dizisi (*escape sequence*) adı verilir. Bu işaretler
karakter dizilerini tanımlarken oluşabilecek hatalardan kaçmamızı sağlar. Peki
bu `\\` işareti nasıl oluyor da karakter dizisini tanımlarken hata almamızı
önlüyor? Gelin bu süreci adım adım tarif edelim:

Python bir karakter dizisi tanımladığımızda, karakter dizisini soldan sağa doğru
okumaya başlar. Mesela yukarıdaki örnekte ilk olarak karakter dizisini
tanımlamaya tek tırnakla başladığımızı görür.

Python karakter dizisini başlatan bu tek tırnak işaretini gördüğü zaman, soldan
sağa doğru ilerleyerek karakter dizisini bitirecek olan tek tırnak işaretini
aramaya başlar.

Soldan sağa doğru ilerlerken 'İstanbul'un' kelimesi içinde geçen kesme işaretini
görür ve karakter dizisinin burada sona erdiğini düşünür. Ancak karakter
dizisini sona erdiren işaret bu olmadığı için Python'ın hata vermekten başka
çaresi kalmaz.

İşte biz 'İstanbul'un' kelimesi içinde geçen bu kesme işaretinin sol tarafına
bir adet `\\` işareti yerleştirerek Python'a, 'Aradığın işaret bu değil. Sen
karakter dizisini okumaya devam et. Biraz sonra aradığın tırnağı bulacaksın!'
mesajı vermiş, yani orada tırnak işaretini farklı bir amaçla kullandığımız
konusunda Python'ı bilgilendirmiş oluruz.

Şurada da aynı durum sözkonusu::

    >>> print("Python programlama dilinin adı \"piton\" yılanından gelmez")

Tıpkı bir önceki örnekte olduğu gibi, burada da Python karakter dizisini soldan
sağa doğru okumaya başlıyor, karakter dizisini başlatan çift tırnak işaretini
görüyor ve bunun üzerine Python karakter dizisini bitirecek olan çift tırnak
işaretini aramaya koyuluyor.

Karakter dizisini soldan sağa doğru okuduğu sırada, karakter dizisi içinde geçen
'piton' kelimesini görüyor. Eğer burada bir önlem almazsak Python bu kelimenin
başındaki çift tırnak işaretini, karakter dizisini sona erdiren tırnak olarak
algılar ve durum aslında böyle olmadığı için de hata verir.

Bu hatayı önlemek için 'piton' kelimesinin başındaki çift tırnağın soluna bir
adet `\\` işareti yerleştirerek Python'a, 'Aradığın tırnak bu değil!' mesajı
veriyoruz. Yani bir bakıma, `\\` adlı kaçış dizisi kendisini tırnak işaretine
siper edip Python'ın bu tırnağı görmesine mani oluyor...

Bunun üzerine Python bu çift tırnak işaretini görmezden gelerek, soldan sağa
doğru okumaya devam eder ve yol üzerinde 'piton' kelimesinin sonundaki çift
tırnak işaretini görür. Eğer burada da bir önlem almazsak Python yine bir hata
verecektir.

Tıpkı biraz önce yaptığımız gibi, bu tırnak işaretinin de soluna bir adet `\\`
işareti yerleştirerek Python'a, 'Aradığın tırnak bu da değil. Sen yine okumaya
devam et!' mesajı veriyoruz.

Bu mesajı alan Python karakter dizisini soldan sağa doğru okumaya devam ediyor
ve sonunda karakter dizisini bitiren çift tırnak işaretini bularak bize hatasız
bir çıktı veriyor.

Böylece `\\` işareti üzerinden hem kaçış dizilerinin ne olduğunu öğrenmiş, hem
de bu kaçış dizisinin nasıl kullanılacağına dair örnekler vermiş olduk. Ancak
`\\` kaçış dizisinin yetenekleri yukarıdakilerle sınırlı değildir. Bu kaçış
dizisini, uzun karakter dizilerini bölmek için de kullanabiliriz. Şimdi şu
örneği dikkatlice inceleyin::

    >>> print("Python 1990 yılında Guido Van Rossum \ 
    ... tarafından geliştirilmeye başlanmış, oldukça \ 
    ... güçlü ve yetenekli bir programlama dilidir.") 
    
    Python 1990 yılında Guido Van Rossum tarafından geliştirilmeye
    başlanmış, oldukça güçlü ve yetenekli bir programlama dilidir.

Normal şartlar altında, bir karakter dizisini tanımlamaya tek veya çift tırnakla
başlamışsak, karakter dizisinin kapanış tırnağını koymadan `Enter` tuşuna
bastığımızda Python bize bir hata mesajı gösterir::

    >>> print("Python 1990 yılında Guido Van Rossum

      File "<stdin>", line 1
        print("Python 1990 yılında Guido Van Rossum
                                                    ^
    SyntaxError: EOL while scanning string literal

İşte `\\` kaçış dizisi bizim burada olası bir hatadan kaçmamızı sağlar. Eğer
`Enter` tuşuna basmadan önce bu işareti kullanırsak Python tıpkı üç tırnak
işaretlerinde şahit olduğumuz gibi, hata vermeden bir alt satıra geçecektir. Bu
sırada, yani `\\` kaçış dizisini koyup `Enter` tuşuna bastığımızda `>>>`
işaretinin `...` işaretine dönüştüğünü görüyorsunuz. Bu işaretin, Python'ın bize
verdiği bir 'Yazmaya devam et!' mesajı olduğunu biliyorsunuz.

Satır Başı (\\n) 
*****************

Python'daki en temel kaçış dizisi biraz önce örneklerini verdiğimiz `\\`
işaretidir. Bu kaçış dizisi başka karakterlerle birleşerek, farklı işlevlere
sahip yeni kaçış dizileri de oluşturabilir. Aslında bu olguya yabancı değiliz.
Önceki sayfalarda bu duruma bir örnek vermiştik. Hatırlarsanız ``print()``
fonksiyonunu anlatırken `end` parametresinin ön tanımlı değerinin `\\n`, yani
satır başı karakteri olduğunu söylemiştik.

.. note:: Satır başı karakterine 'yeni satır karakteri' dendiği de olur.

Satır başı karakterini ilk öğrendiğimizde bu karakteri anlatırken bazı örnekler
de vermiştik::
    
    >>> print("birinci satır\nikinci satır\nüçüncü satır") 
    
    birinci satır 
    ikinci satır 
    üçüncü satır

Gördüğünüz gibi, `\\n` adlı kaçış dizisi, bir alt satıra geçilmesini sağlıyor.
İşte aslında `\\n` kaçış dizisi de, `\\` ile 'n' harfinin birleşmesinden oluşmuş
bir kaçış dizisidir. Burada `\\` işaretinin görevi, 'n' harfinin özel bir anlam
kazanmasını sağlamaktır. `\\` işareti ile 'n' harfi birleştiğinde 'satır başı
karakteri' denen özel bir karakter dizisi ortaya çıkarıyor.

Gelin bu kaçış dizisi ile ilgili bir örnek verelim. Şimdi şu kodları dikkatlice
inceleyin::

    >>> başlık = "Türkiye'de Özgür Yazılımın Geçmişi" 
    >>> print(başlık, "\n", "-"*len(başlık), sep="") 
    
    Türkiye'de Özgür Yazılımın Geçmişi
    ----------------------------------

Burada, `başlık` adlı değişkenin tuttuğu `"Türkiye'de Özgür Yazılımın Geçmişi"`
adlı karakter dizisinin altını çizdik. Dikkat ederseniz, başlığın altına
koyduğumuz çizgiler başlığın uzunluğunu aşmıyor. Yazdığımız program, başlığın
uzunluğu kadar çizgiyi başlığın altına ekliyor. Bu programda başlık ne olursa
olsun, programımız çizgi uzunluğunu kendisi ayarlayacaktır. Örneğin::

    >>> başlık = "Python Programlama Dili" 
    >>> print(başlık, "\n", "-"*len(başlık), sep="")

    Python Programlama Dili 
    ----------------------- 
    
    >>> başlık = "Alışveriş Listesi" 
    >>> print(başlık, "\n", "-"*len(başlık), sep="")

    Alışveriş Listesi 
    -----------------

Gelin isterseniz bu kodlardaki ``print()`` satırını şöyle bir inceleyelim.
Kodumuz şu::

    >>> print(başlık, "\n", "-"*len(başlık), sep="")

Burada öncelikle `başlık` adlı değişkeni ``print()`` fonksiyonunun parantezleri
içine yazdık. Böylece `başlık` değişkeninin değeri ekrana yazdırılacak.

``print()`` fonksiyonunun ikinci parametresinin `\\n` adlı kaçış dizisi olduğunu
görüyoruz. Bu kaçış dizisini eklememiz sayesinde Python ilk parametreyi çıktı
olarak verdikten sonra bir alt satıra geçiyor. Bu parametrenin tam olarak ne işe
yaradığını anlamak için, yukarıdaki satırı bir de o parametre olmadan
çalıştırmayı deneyebilirsiniz::

    >>> print(başlık, "-"*len(başlık), sep="")

    Alışveriş Listesi-----------------

``print()`` fonksiyonunun üçüncü parametresinin ise şu olduğunu görüyoruz:
``"-"*len(başlık)``.

İşte `başlık` değişkeninin altına gerekli sayıda çizgiyi çizen kodlar bunlardır.
Burada ``len()`` fonksiyonunu nasıl kullandığımıza çok dikkat edin. Bu kod
sayesinde `başlık` değişkeninin uzunluğu (``len(başlık)``) sayısınca `-`
işaretini ekrana çıktı olarak verebiliyoruz.

Yukarıdaki kodlarda ``print()`` fonksiyonunun son parametresi ise `sep=''`. Peki
bu ne işe yarıyor? Her zaman olduğu gibi, bu kod parçasının ne işe yaradığını
anlamak için programı bir de o kodlar olmadan çalıştırmayı deneyebilirsiniz::

    >>> print(başlık, "\n", "-"*len(başlık)) 
    
    Alışveriş Listesi 
      -----------------
    
Gördüğünüz gibi, `başlık` değişkeninin tam altına gelmesi gereken çizgi
işaretleri sağa kaymış. Bunun nedeni `sep` parametresinin öntanımlı değerinin
bir adet boşluk karakteri olmasıdır. `sep` parametresinin öntanımlı değeri
nedeniyle çizgilerin baş tarafına bir adet boşluk karakteri ekleniyor çıktıda. O
yüzden bu çizgiler sağa kaymış görünüyor. İşte biz yukarıdaki kodlarda `sep`
parametresinin öntanımlı değerini değiştirip, boşluk karakteri yerine boş bir
karakter dizisi yerleştiriyoruz. Böylece çizgiler çıktıda sağa kaymıyor.

Satır başı karakteri, programlama maceramız sırasında en çok kullanacağımız
kaçış dizilerinden biri ve hatta belki de birincisidir. O yüzden bu kaçış
dizisini çok iyi öğrenmenizi tavsiye ederim. 

Ayrıca bu kaçış dizisini (ve tabii öteki kaçış dizilerini) tanıyıp öğrenmeniz,
yazacağınız programların selameti açısından da büyük önem taşır. Eğer bir
karakter dizisi içinde geçen kaçış dizilerini ayırt edemezseniz Python size hiç
beklemediğiniz çıktılar verebilir. Hatta yazdığınız programlar kaçış dizilerini
tanımıyor olmanızdan ötürü bir anda hata verip çökebilir. Peki ama nasıl? 

Şimdi şu örneğe dikkatlice bakın:

Diyelim ki bilgisayarınızın 'C:\\' dizinindeki 'nisan' adlı bir klasörün içinde
yer alan `masraflar.txt` adlı bir dosyayı yazdığınız bir program içinde
kullanmanız gerekiyor. Mesela bu dosyayı, tam adresiyle birlikte
kullanıcılarınıza göstermek istiyorsunuz.

İlk denememizi yapalım::
    
    >>> print("C:\nisan\masraflar.txt")
    
Buradan şöyle bir çıktı aldık::

    C:
    isan\masraflar.txt    
    
Gördüğünüz gibi, bu çıktıyı normal yollardan vermeye çalıştığımızda Python bize
hiç de beklemediğimiz bir çıktı veriyor. Peki ama neden?

Python'da karakter dizileri ile çalışırken asla aklımızdan çıkarmamamız gereken
bir şey var: Eğer yazdığımız herhangi bir karakter dizisinin herhangi bir
yerinde `\\` işaretini kullanmışsak, bu işaretten hemen sonra gelen karakterin
ne olduğuna çok dikkat etmemiz gerekir. Çünkü eğer dikkat etmezsek, farkında
olmadan Python için özel anlam taşıyan bir karakter dizisi oluşturmuş
olabiliriz. Bu da kodlarımızın beklediğimiz gibi çalışmasını engeller.

Yukarıdaki sorunun kaynağını anlamak için ``"C:\nisan\masraflar.txt"`` adlı
karakter dizisine çok dikkatlice bakın. Python bu karakter dizisinde bizim
'\\nisan' olarak belirttiğimiz kısmın başındaki `\\n` karakterlerini bir kaçış
dizisi olarak algıladı. Çünkü `\\n` adlı karakter dizisi, 'satır başı kaçış
dizisi' adını verdiğimiz, Python açısından özel anlam taşıyan bir karakter
dizisine işaret ediyor. Zaten yukarıdaki tuhaf görünen çıktıya baktığınızda da,
bu kaçış dizisinin olduğu noktadan itibaren karakter dizisinin bölünüp yeni bir
satıra geçildiğini göreceksiniz. İşte biz yukarıdaki örnekte alelade bir dizin
adı belirttiğimizi zannederken aslında hiç farkında olmadan bir kaçış dizisi
üretmiş oluyoruz. Bu nedenle, daha önce de söylediğimiz gibi, karakter dizileri
içinde farkında olarak veya olmayarak kullandığımız kaçış dizilerine karşı her
zaman uyanık olmalıyız. Aksi takdirde, yukarıda olduğu gibi hiç beklemediğimiz
çıktılarla karşılaşabiliriz.

Esasen yukarıdaki problem bir dereceye kadar (ve yerine göre) 'masum bir kusur'
olarak görülebilir. Çünkü bu hata programımızın çökmesine yol açmıyor. Ama bir
karakter dizisi içindeki gizli kaçış dizilerini gözden kaçırmak, bazı durumlarda
çok daha yıkıcı sonuçlara yol açabilir. Mesela yukarıdaki sorunlu dizin adını
ekrana yazdırmak yerine ``open()`` fonksiyonunu kullanarak, bu karakter dizisi
içinde belirttiğimiz `masraflar.txt` adlı dosyayı açmaya çalıştığımızı düşünün::
    
    >>> open("C:\nisan\masraflar.txt")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OSError: [Errno 22] Invalid argument: 'C:\nisan\\masraflar.txt'
    
Eğer sorunun gözden kaçan bir kaçış dizisinden kaynaklandığını farkedemezseniz,
bu sorunu çözebilmek için saatlerinizi ve hatta günlerinizi harcamak zorunda
kalabilirsiniz. Çünkü yukarıdaki hata mesajı sorunun nedenine dair hiçbir şey
söylemiyor. Ancak ve ancak yukarıdaki karakter dizisi içinde sinsice gizlenen
bir `\\n` kaçış dizisi olduğu gözünüze çarparsa bu sorunu çözme yolunda bir adım
atabilirsiniz.

Diyelim ki sorunun '\\nisan' ifadesinin başındaki `\\n` karakterlerinin Python
tarafından bir kaçış dizisi olarak algılanmasından kaynaklandığını farkettiniz.
Peki bu sorunu nasıl çözeceksiniz? 

Bu sorunun birkaç farklı çözüm yolu var. Biz şimdilik sadece ikisini göreceğiz.
Bu bölümün sonuna vardığınızda öteki çözüm yolunu da öğrenmiş olacaksınız. 

Yukarıdaki problemi, ilgili kaçış dizisi içindeki ters taksim işaretini
çiftleyerek çözebilirsiniz::
    
    >>> open("C:\\nisan\masraflar")
    
Tabii tutarlılık açısından karakter dizisi içindeki bütün ters taksim
işaretlerini çiftlemek mantıklı olacaktır::
    
    >>> open("C:\\nisan\\masraflar")
    
Bunun dışında, bu örnek için, dizin adlarını ters taksim yerine düz taksim
işaretiyle ayırmayı tercih edebilirsiniz::
    
    >>> open("C:/nisan/masraflar")
    
Dediğimiz gibi, üçüncü (ve aslında daha kullanışlı olan) yöntemi biraz sonra
inceleyeceğiz. Biz şimdilik kaçış dizilerini anlatmaya devam edelim.

Sekme (\\t) 
************

Python'da `\\` işareti sadece 'n' harfiyle değil, başka harflerle de
birleşebilir. Örneğin `\\` işaretini 't' harfiyle birleştirerek yine özel bir
anlam ifade eden bir kaçış dizisi elde edebiliriz::

    >>> print("abc\tdef") 
    
    abc def

Burada `\\t` adlı kaçış dizisi, `"abc"` ifadesinden sonra sanki `Tab` (sekme)
tuşuna basılmış gibi bir etki oluşturarak `"def"` ifadesini sağa doğru itiyor.
Bir de şu örneğe bakalım::

    >>> print("bir", "iki", "üç", sep="\t")

    bir     iki     üç

Bir örnek daha::

    >>> print(*"123456789", sep="\t")

    1   2   3   4   5   6   7   8   9

Gördüğünüz gibi, parametreler arasında belli aralıkta bir boşluk bırakmak
istediğimizde `\\t` adlı kaçış dizisinden yararlanabiliyoruz.

Tıpkı `\\n` kaçış dizisinde olduğu gibi, karakter dizilerinde `\\t` kaçış
dizisinin varlığına karşı da uyanık olmalıyız::
    
    >>> open("C:\nisan\masraflar\toplam_masraf.txt")

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OSError: [Errno 22] Invalid argument: 'C:\nisan\\masraflar\toplam_masraf.txt'
    
Burada da `\\n` ile yaşadığımız soruna benzer bir durum var. Biz
`toplam_masraf.txt` adlı bir dosyaya atıfta bulunmaya çalışıyoruz, ama Python bu
ifadenin başındaki 't' harfinin, kendisinden önce gelen `\\` işareti ile
birleşmesinden ötürü, bunu `\\t` kaçış dizisi olarak algılıyor ve ona göre
davranıyor.

Belki yukarıdaki kodları şöyle yazarsak durumu anlamak daha kolay olabilir::
    
    >>> print("C:\nisan\masraflar\toplam_masraf.txt")
    
    C:
    isan\masraflar	oplam_masraf.txt

Gördüğünüz gibi, Python `\\n` kaçış dizisini gördüğü noktada alt satırın başına
geçiyor ve `\\t` kaçış dizisini gördüğü noktada da önceki ve sonraki öğeler
arasında bir sekme boşluğu bırakıyor. Bu durumu engellemek için ne yapmanız
gerektiğini biliyorsunuz: Ya ters taksim işaretlerini çiftleyeceksiniz::
    
    >>> print("C:\\nisan\\masraflar\\toplam_masraf.txt")
    
Ya da dizin adı ayracı olarak düz taksim işaretini kullanacaksınız::

    >>> print("C:/nisan/masraflar/toplam_masraf.txt")    
    
Daha önce de söylediğimiz gibi, üçüncü ve daha pratik olan yolu biraz sonra
göreceğiz. Şimdilik sadece biraz sabır...

Zil Sesi (\\a) 
*****************

`\\` işaretinin birleştiğinde farklı bir anlam türettiği bir başka harf de 'a'
harfidir. `\\` işareti 'a' harfiyle birleşerek !bip! benzeri bir zil sesi
üretilmesini sağlayabilir::

    >>> print("\a") 
    
    !bip!

İsterseniz yukarıdaki komutu şu şekilde yazarak, kafa şişirme katsayısını
artırabilirsiniz::

    >>> print("\a" * 10)

Bu şekilde !bip! sesi `10` kez tekrar edilecektir. Ancak bu kaçış dizisi
çoğunlukla sadece Windows üzerinde çalışacaktır. Bu kaçış dizisinin GNU/Linux
üzerinde çalışma garantisi yoktur. Hatta bu kaçış dizisi bütün Windows
sistemlerinde dahi çalışmayabilir. Dolayısıyla bu kaçış dizisinin işlevine bel
bağlamak pek mantıklı bir iş değildir.

Tıpkı `\\n` ve `\\t` kaçış dizilerinde olduğu gibi bu kaçış dizisinin varlığına
karşı da uyanık olmalıyız. Burada da mesela 'C:\\aylar' gibi bir dizin adı
tanımlamaya çalışırken aslında `\\a` kaçış dizisini oluşturuyor olabilirsiniz
farkında olmadan.

Aynı Satır Başı (\\r) 
*************************

Bu kaçış dizisi, bir karakter dizisinde aynı satırın en başına dönülmesini
sağlar. Bu kaçış dizisinin işlevini tanımına bakarak anlamak biraz zor olabilir.
O yüzden dilerseniz bu kaçış dizisinin ne işe yaradığını bir örnek üzerinde
göstermeye çalışalım::

    >>> print("Merhaba\rZalim Dünya!") 
    
    Zalim Dünya!

Burada olan şey şu: Normal şartlar altında, ``print()`` fonksiyonu içine
yazdığımız bir karakter dizisindeki bütün karakterler soldan sağa doğru tek tek
ekrana yazdırılır::

    >>> print("Merhaba Zalim Dünya!") 
    
    Merhaba Zalim Dünya!

Ancak eğer karakter dizisinin herhangi bir yerine `\\r` adlı kaçış dizisini
yerleştirirsek, bu kaçış dizisinin bulunduğu konumdan itibaren **aynı** satırın
başına dönülecek ve `\\r` kaçış dizisinden sonra gelen bütün karakterler satır
başındaki karakterlerin üzerine yazacaktır. Şu örnek daha açıklayıcı olabilir::

    >>> print("Merhaba\rDünya") 
    
    Dünyaba

Burada, `"Merhaba"` karakter dizisi ekrana yazdırıldıktan sonra `\\r` kaçış
dizisinin etkisiyle satır başına dönülüyor ve bu kaçış dizisinden sonra gelen
`"Dünya"` karakter dizisi `"Merhaba"` karakter dizisinin üzerine yazıyor. Tabii
`"Dünya"` karakter dizisi içinde `5` karakter, `"Merhaba"` karakter dizisi
içinde ise `7` karakter olduğu için, `"Merhaba"` karakter dizisinin son iki
karakteri (`"ba"`) dışarda kalıyor. Böylece ortaya `"Dünyaba"` gibi bir şey
çıkıyor.

Önceki kaçış dizilerinde olduğu gibi, bu kaçış dizisini de farkında olmadan
karakter dizisi içinde kullanırsanız beklemediğiniz çıktılar alırsınız::
    
    >>> print("C:\ülke\türkiye\iller\rize\nüfus.txt")
    
    izeülke	ürkiye\iller
    üfus.txt
    
Burada farkında olmadan sadece bir değil, üç kaçış dizisi birden oluşturduk!    

Düşey Sekme (\\v) 
********************

Eğer `\\` işaretini 'v' harfiyle birlikte kullanırsak düşey sekme denen şeyi
elde ederiz. Hemen bir örnek verelim::

    >>> print("düşey\vsekme")

    düşey 
         sekme

Yalnız bu `\\v` adlı kaçış dizisi her işletim sisteminde çalışmayabilir.
Dolayısıyla, birden fazla platform üzerinde çalışmak üzere tasarladığınız
programlarınızda bu kaçış dizisini kullanmanızı önermem.

İmleç Kaydırma (\\b) 
*********************

`\\` kaçış dizisinin, biraraya geldiğinde özel bir anlam kazandığı bir başka
harf de b'dir. `\\b` kaçış dizisinin görevi, imleci o anki konumundan sola
kaydırmaktır. Bu tanım pek anlaşılır değil. O yüzden bir örnek verelim::
    
    >>> print("yahoo.com\b")
    
Bu kodu çalıştırdığınızda herhangi bir değişiklik görmeyeceksiniz. Ama aslında
en sonda gördüğümüz `\\b` kaçış dizisi, imleci bir karakter sola kaydırdı.
Dikkatlice bakın::
    
    >>> print("yahoo.com\b.uk")
    
Gördüğünüz gibi, `\\b` kaçış dizisinin etkisiyle imleç bir karakter sola kaydığı
için, 'com' kelimesinin son harfi silindi ve bunun yerine `\\b` kaçış dizisinden
sonra gelen `.uk` karakterleri yerleştirildi. Dolayısıyla biz de şu çıktıyı
aldık::
    
    yahoo.co.uk
    
Bir örnek daha verelim... 

Bildiğiniz gibi, ``print()`` fonksiyonu, kendisine verilen parametreler arasına
birer boşluk yerleştirir::
    
    >>> print('istihza', '.', 'com')
    
    istihza . com
    
Biz bu öğeleri birbirine bitiştirmek için şöyle bir yol izleyebileceğimizi
biliyoruz::
    
    >>> print('istihza', '.', 'com', sep='')
    
    istihza.com
    
İşte aynı etkiyi `\\b` kaçış dizisini kullanarak da elde edebiliriz::
    
    >>> print('istihza', '\b.', '\bcom')
    
    istihza.com
    
Gördüğünüz gibi, `\\b` kaçış dizisi, '.' ve 'com' parametrelerinden önce imleci
birer karakter sola kaydırdığı için, parametreler arasındaki boşluk karakterleri
ortadan kalktı.

Bu kaçış dizisini kullanarak şöyle gereksiz işler peşinde de koşabilirsiniz::
    
    >>> print('istihza\b\b\bsn')

    istisna
    
Burada `\\b` kaçış dizisini üst üste birkaç kez kullanarak imleci birkaç
karakter sola kaydırdık ve 'sn' harflerini 'hz' harflerinin üzerine bindirdik.
Böylece 'istihza' kelimesi 'istisna' kelimesine dönüşmüş oldu...

Daha fazla uzatmadan, bu kaçış dizisinin Python'da çok nadir kullanıldığı
bilgisini vererek yolumuza devam edelim...

Küçük Unicode (\\u)
********************

Tıpkı bundan önceki kaçış dizileri gibi, karakter dizileri içindeki varlığı
konusunda dikkatli olmamız gereken bir başka kaçış dizisi de `\\u` adlı kaçış
dizisidir. Eğer bu kaçış dizisini tanımaz ve dikkatli kullanmazsak, yazdığımız
programlar tespit etmesi çok güç hatalar üretebilir.

Örneğin şöyle bir çıktı vermek istediğinizi düşünün:

    Dosya konumu: C:\\users\\zeynep\\gizli\\dosya.txt
    
Bu çıktıyı normal yollardan vermeye çalışırsak Python bize bir hata mesajı
gösterecektir::
    
    >>> print("Dosya konumu: C:\users\zeynep\gizli\dosya.txt")
    
      File "<stdin>", line 1
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in
    position 16-18: truncated \uXXXX escape

Belki sağda solda 'UNICODE' diye bir şey duymuşsunuzdur. Eğer şimdiye kadar
böyle bir şey duymadıysanız veya duyduysanız bile ne olduğunu bilmiyorsanız hiç
ziyanı yok. Birkaç bölüm sonra bunun ne anlama geldiğini bütün ayrıntılarıyla
anlatacağız. Biz şimdilik sadece şunu bilelim: UNICODE, karakterlerin,
harflerin, sayıların ve bilgisayar ekranında gördüğümüz öteki bütün işaretlerin
her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir. Bu
sistemde, 'kod konumu' (*code point*) adı verilen bu numaralar özel bir şekilde
gösterilir. Örneğin 'ı' harfi UNICODE sisteminde şu şekilde temsil edilir::
    
    u+0131
    
Aynı şekilde 'a' harfi bu sistemde şu kod konumu ile gösterilir::
    
    u+0061
    
Python programlama dilinde ise, yukarıdaki kod konumu düzeni şöyle gösterilir::
    
    \\u0131
    
Gördüğünüz gibi, Python UNICODE sistemindeki her bir kod konumunu gösterebilmek
için, önce `\\u` şeklinde bir kaçış dizisi tanımlıyor, ardından UNICODE
sisteminde `+` işaretinden sonra gelen sayıyı bu kaçış dizisinin hemen
sağına ekliyor. Gelin kendi kendimize birkaç deneme çalışması yapalım::
    
    >>> '\u0130'
    
    'İ'
    
    >>> '\u0070'
    
    'p'
    
    >>> "\ufdsf"
    
      File "<stdin>", line 1
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in
    position 0-4: truncated \uXXXX escape

Gördüğünüz gibi, eğer `\\u` kaçış dizisinden sonra doğru bir kod konumu
belirtmezsek Python bize bir hata mesajı gösteriyor...

Bu hata mesajının, biraz önce ``print("Dosya konumu:
C:\users\zeynep\gizli\dosya.txt")`` kodunu yazdıktan sonra aldığımız hata ile
aynı olduğuna dikkat edin. Tıpkı `\\ufdsf` örneğinde olduğu gibi, `\\users`
ifadesi de varolan bir UNICODE kod konumuna karşılık gelmediği için, Python'ın
hata vermekten başka çaresi kalmıyor. 

Biz bu örnekte 'users' kelimesini kullanmaya çalışıyoruz, ama 'u' harfinden
hemen önce gelen `\\` kaçış dizisi nedeniyle, hiç farkında olmadan Python
açısından önemli bir karakter dizisi (`\\u`) meydana getirmiş oluyoruz. O
yüzden, böyle can sıkıcı hatalarla karşılaşmamak için olası kaçış dizilerine
karşı her zaman uyanık olmamız gerekiyor.

Pekı biz bu kaçış dizisi yüzünden, yazdığımız programlarda `Dosya konumu:
C:\\users\\zeynep\\gizli\\dosya.txt")` gibi bir çıktı veremeyecek miyiz? 

Verebileceğimizi, ama bunun bir yolu yordamı olduğunu biliyorsunuz. Biz yine de
tekrar edelim::
    
    >>> print("Dosya konumu: C:\\users\\zeynep\\gizli\\dosya.txt")
    
    Dosya konumu: C:\users\zeynep\gizli\dosya.txt
    
Gördüğünüz gibi, karakter dizisi içinde geçen bütün `\\` işaretlerini
çiftleyerek sorunumuzu çözdük. Buradaki gibi bir sorunla karşılaşmamak için,
dizin adlarını ayırırken ters taksim işareti yerine düz taksim işaretini
kullanmayı da tercih edebilirsiniz::
    
   >>> print("Dosya konumu: C:/users/zeynep/gizli/dosya.txt")
   
Biraz sonra bu sorunu halletmenin üçüncü ve daha kolay bir yönteminden daha söz
edeceğiz. Ama biz şimdilik bu kaçış dizisini bir kenara bırakıp başka bir kaçış
dizisini incelemeye geçelim.

Büyük Unicode (\\U)
*********************

Bu kaçış dizisi biraz önce gördüğümüz `\\u` adlı kaçış dizisiyle hemen hemen
aynı anlama gelir. Bu kaçış dizisi de, tıpkı `\\u` gibi, UNICODE kod konumlarını
temsil etmek için kullanılır. Ancak `\U` ile gösterilen kod konumları `\u` ile
gösterilenlere göre biraz daha uzundur. Örneğin, hatırlarsanız `\u` kaçış
dizisini kullanarak 'ı' harfinin UNICODE kod konumunu şöyle temsil ediyorduk::
    
    >>> '\u0131'
    
    'ı'
    
Eğer aynı kod konumunu `\U` adlı kaçış dizisi ile göstermek istersek şöyle bir
şey yazmamız gerekir::
    
    >>> '\U00000131'
    
Gördüğünüz gibi, burada `\\U` kaçış dizisinden sonra gelen kısım toplam 8
haneli bir sayıdan oluşuyor. `\u` kaçış dizisinde ise bu kısmı toplam 4 haneli
bir sayı olarak yazıyorduk. İşte `\\u` kaçış dizisi ile `\U` kaçış dizisi
arasındaki fark budur. `\u` kaçış dizisi hakkında söylediğimiz öteki her şey
`\U` kaçış dizisi için de geçerlidir.

Uzun Ad (\\N)
******************

UNICODE sistemi ile ilgili bir başka kaçış dizisi de `\\N` adlı kaçış dizisidir.

Dediğimiz gibi, UNICODE sistemine ilişkin ayrıntılardan ilerleyen derslerde söz
edeceğiz, ama bu sistemle ilgili ufak bir bilgi daha verelim.

UNICODE sisteminde her karakterin tek ve benzersiz bir kod konumu olduğu gibi,
tek ve benzersiz bir de uzun adı vardır. Örneğin 'a' harfinin UNICODE
sistemindeki uzun adı şudur::
    
    LATIN SMALL LETTER A
    
Bir karakterin UNICODE sistemindeki uzun adını öğrenmek için `unicodedata` adlı
bir modülden yararlanabilirsiniz::
    
    >>> import unicodedata
    >>> unicodedata.name('a')
    
    LATIN SMALL LETTER A
    
    >>> unicodedata.name('Ş')
    
    LATIN CAPITAL LETTER S WITH CEDILLA
    
Bu arada, daha önce de söylediğimiz gibi, bu 'modül' kavramına şimdilik
takılmayın. İlerde modülleri ayrıntılı olarak inceleyeceğiz. Şimdilik
`unicodedata` denen şeyin, (tıpkı daha önce örneklerini gördüğümüz `os`, `sys`
ve `keyword` gibi) bir modül olduğunu ve bu modül içindeki `name` adlı bir
fonksiyonu kullanarak, parantez içinde belirttiğimiz herhangi bir karakterin
UNICODE sistemindeki uzun adını elde edebileceğimizi bilelim yeter.

İşte `\\N` kaçış dizisi bu uzun isimleri, Python programlarımızda kullanma
imkanı verir bize. Bu kaçış dizisini, karakterlerin UNICODE sistemindeki uzun
adları ile birlikte kullanarak asıl karakterleri elde edebiliriz. Dikkatlice
bakın::
    
    >>> print("\N{LATIN SMALL LETTER A}")
    
    a
    
    >>> print("\N{LATIN CAPITAL LETTER S WITH CEDILLA}")
    
    ş
    
    >>> print("\Nisan")
    
      File "<stdin>", line 1
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in
    position 0-1: malformed \N character escape
    
Gördüğünüz gibi, herhangi bir karşılığı olmayan bir uzun ad belirttiğimizde
Python bize bir hata mesajı gösteriyor. Çünkü Python `\\N` kaçış dizisinin hemen
ardından `{` işaretinin getirilmesini ve sonra da UNICODE sistemi dahilinde
geçerli bir uzun ad belirtilmesini bekliyor. Yukarıdaki örnekte `\\N` kaçış
dizisinden sonra `{` işareti yok. Zaten `\\N` kaçış dizisinin hemen ardından
gelen 'isan' ifadesi de doğru bir uzun ada işaret etmiyor. Dolayısıyla da
Python'ın bize hata mesajı göstermekten başka çaresi kalmıyor...

`\\u`, `\\U` ve `\\N` kaçış dizileri, UNICODE sistemi ile ilgili çalışmalar
yapmak isteyen programcılar için Python programlama dilinin sunduğu faydalı
araçlardan yalnızca birkaçıdır. Ancak bu araçların sizin işinize yaramayacağını
asla düşünmeyin. Zira `\\u`, `\\U` ve `\\N` kaçış dizileri ile ilgili yukarıdaki
durum hiç beklemediğiniz bir anda sizi de vurabilir. Çünkü bu kaçış dizilerinin
oluşturduğu risk hiç de öyle nadir karşılaşılacak bir sorun değildir.

Bildiğiniz gibi Windows 7'de kullanıcının dosyalarını içeren dizin adı
`C:\\Users\\kullanıcı_adı` şeklinde gösteriliyor. Dolayısıyla Windows
kullananlar UNICODE kaçış dizilerinden kaynaklanan bu tuzağa her an düşebilir.
Ya da eğer adınız 'u' veya 'n' harfi ile başlıyorsa yine bu tuzağa düşme
ihtimaliniz epey yüksek olacak, `C:\\Users\\umut` veya `C:\\Users\\Nihat` gibi
bir dizin adı belirtirken çok dikkatli olmanız gerekecektir. Zira özellikle
dosyalar üzerinde işlem yaparken, bu tür dizin adlarını sık sık kullanmak
durumunda kalacaksınız. Bu yüzden, alelade bir kelime yazdığınızı zannederken
hiç farkında olmadan bir kaçış dizisi tanımlıyor olma ihtimalini her zaman göz
önünde bulundurmalı ve buna uygun önlemleri almış olmalısınız.

Onaltılı Karakter (\\x)
**************************

'x' harfi de `\\` işareti ile birleştiğinde özel anlam kazanarak bir kaçış
dizisi meydana getirir. 

`\\x` kaçış dizisini kullanarak, onaltılı
(*hexadecimal*) sayma sistemindeki bir sayının karakter karşılığını
gösterebilirsiniz. Dikkatlice bakın::
    
    >>> "\x41"
    
    'A'
    
Onaltılı sayma sistemindeki `41` sayısı 'A' harfine karşılık gelir. Eğer hangi
karakterlerin hangi sayılara karşılık geldiğini merak ediyorsanız
http://www.ascii.cl/ adresindeki tabloyu inceleyebilirsiniz. Bu tabloda 'hex'
sütunu altında gösterilen sayılar onaltılı sayılar olup, 'symbol' sütununda
gösterilen karakterlere karşılık gelirler. Örneğin 'hex' sütunundaki `4E` sayısı
'symbol' sütunundaki 'N' harfine karşılık gelir. Bu durumu Python'la da teyit
edebilirsiniz::
    
    >>>"\x4E"
    
    N
    
Eğer sayılarla karakterler arasındaki bağlantının tam olarak ne olduğunu
bilmiyorsanız hiç endişe etmeyin. Birkaç bölüm sonra sayılarla karakterler
arasında nasıl bir bağ olduğunu gayet ayrıntılı bir şekilde anlatacağız. Biz
şimdilik yalnızca `\\x` karakter dizisinin özel bir kaçış dizisine karşılık
geldiğini ve bu kaçış dizisini karakter dizileri içinde kullanırken dikkatli
olmamız gerektiğini bilelim yeter::
    
    >>> print("C:\Users\Ayşe\xp_dosyaları")

      File "<stdin>", line 1
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in 
    position 2-4: truncated \UXXXXXXXX escape
    
Gördüğünüz gibi, Python `\\x` ifadesinden sonra onaltılı bir sayı belirtmenizi
bekliyor. Halbuki biz burada `\\x` ifadesini 'xp_dosyaları' adlı dizini
gösterebilmek için kullanmıştık. Ama görünüşe göre yanlışlıkla Python için özel
bir anlam ifade eden bir karakter dizisi oluşturmuşuz...

Etkisizleştirme (r) 
*********************

Dediğimiz gibi, Python'daki en temel kaçış dizisi `\\` işaretidir. Bu işaret
bazı başka harflerle birleşerek yeni kaçış dizileri de oluşturabilir.

Python'da `\\` işaretinin dışında temel bir kaçış dizisi daha bulunur. Bu kaçış
dizisi 'r' harfidir. Şimdi bu kaçış dizisinin nasıl kullanılacağını ve ne işe
yaradığını inceleyelim:

Şöyle bir çıktı vermek istediğimizi düşünün::

    Kurulum dizini: C:\aylar\nisan\toplam masraf

Bildiğimiz yoldan bu çıktıyı vermeye çalışırsak neler olacağını adınız gibi
biliyorsunuz::

    >>> print("Kurulum dizini: C:\aylar\nisan\toplam masraf") 
    
    Kurulum dizini: C:ylar
    isan	oplam masraf

.. note:: Eğer Windows üzerinde çalışıyorsanız bu komutu verdikten sonra bir
          !bip! sesi de duymuş olabilirsiniz...

Python tabii ki, karakter dizisi içinde geçen '**\\a**\ ylar', '**\\n**\ isan', ve
'**\\t**\ oplam masraf' ifadelerinin ilk karakterlerini yanlış anladı!
`\\a`, `\\n` ve `\\t` gibi ifadeler Python'ın gözünde birer kaçış dizisi. Dolayısıyla Python
`\\a` karakterlerini görünce bir !bip! sesi çıkarıyor, `\\n` karakterlerini
görünce satır başına geçiyor ve `\\t` karakterlerini görünce de `Tab` tuşuna
basılmış gibi bir tepki veriyor. Sonuç olarak da yukarıdaki gibi bir çıktı
üretiyor. 

Daha önce bu durumu şöyle bir kod yazarak engellemiştik::

    >>> print("Kurulum dizini: C:\\aylar\\nisan\\toplam masraf") 
    
    Kurulum dizini: C:\aylar\nisan\toplam masraf

Burada, `\\` işaretlerinin her birini çiftleyerek sorunun üstesinden geldik.
Yukarıdaki yöntem doğru ve kabul görmüş bir çözümdür. Ama bu sorunun üstesinden
gelmenin çok daha basit ve pratik bir yolu var. Bakalım::

    >>> print(r"Kurulum dizini: C:\aylar\nisan\toplam masraf") 
    
    Kurulum dizini: C:\aylar\nisan\toplam masraf

Gördüğünüz gibi, karakter dizisinin baş kısmının dış tarafına bir adet `r` harfi
yerleştirerek sorunun üstesinden geliyoruz. Bu kaçış dizisinin, kullanım
açısından öteki kaçış dizilerinden farklı olduğuna dikkat edin. Öteki kaçış
dizileri karakter dizisinin içinde yer alırken, bu kaçış dizisi karakter
dizisinin dışına yerleştiriliyor.

Bu kaçış dizisinin tam olarak nasıl işlediğini görmek için dilerseniz bir örnek
daha verelim::

    >>> print("Kaçış dizileri: \, \n, \t, \a, \\, r") 

    Kaçış dizileri: \, 
    , 	, , \, r

Burada da Python bizim yapmak istediğimiz şeyi anlayamadı ve karakter dizisi
içinde geçen kaçış dizilerini doğrudan ekrana yazdırmak yerine bu kaçış
dizilerinin işlevlerini yerine getirmesine izin verdi. Tıpkı biraz önceki
örnekte olduğu gibi, istersek kaçış dizilerini çiftleyerek bu sorunu
aşabiliriz::

    >>> print("Kaçış dizileri: \\, \\n, \\t, \\a, \\\, r") 
    
    Kaçış dizileri: \, \n, \t, \a, \\, r

Ama tabii ki bunun çok daha kolay bir yöntemi olduğunu biliyorsunuz::

    >>> print(r"Kaçış dizileri: \, \n, \t, \a, \\, r") 
    
    Kaçış dizileri: \, \n, \t, \a, \\, r

Gördüğünüz gibi, karakter dizisinin başına getirdiğimiz `r` kaçış dizisi,
karakter dizisi içinde geçen kaçış dizilerinin işlevlerini yerine getirmesine
engel olarak, istediğimiz çıktıyı elde etmemizi sağlıyor.

Bu arada bu kaçış dizisini, daha önce öğrendiğimiz `\\r` adlı kaçış dizisi ile
karıştırmamaya dikkat ediyoruz.

Python'daki bütün kaçış dizilerinden söz ettiğimize göre, konuyu kapatmadan önce
önemli bir ayrıntıdan söz edelim.

Python'da karakter dizilerinin sonunda sadece çift sayıda `\\` işareti
bulunabilir. Tek sayıda `\\` işareti kullanıldığında karakter dizisini bitiren
tırnak işareti etkisizleşeceği için çakışma sorunu ortaya çıkar. Bu
etkisizleşmeyi, karakter dizisinin başına koyduğunuz 'r' kaçış dizisi de
engelleyemez. Yani::
    
    >>> print("Kaçış dizisi: \")

Bu şekilde bir tanımlama yaptığımızda Python bize bir hata mesajı gösterir.
Çünkü kapanış tırnağının hemen öncesine yerleştirdiğimiz `\\` kaçış dizisi,
Python'ın karakter dizisini kapatan tırnak işaretini görmezden gelmesine yol
açarak bu tırnağı etkisizleştiriyor. Böylece sanki karakter dizisini tanımlarken
kapanış tırnağını hiç yazmamışız gibi bir sonuç ortaya çıkıyor:: 

    >>> print("Kaçış dizisi: \")
      File "<stdin>", line 1
        print("Kaçış dizisi: \")
                                  ^
    SyntaxError: EOL while scanning string literal

Üstelik bu durumu, `r` adlı kaçış dizisi de engelleyemiyor::
    
    >>> print(r"Kaçış dizisi: \")
      File "<stdin>", line 1
        print(r"Kaçış dizisi: \")
                                   ^
    SyntaxError: EOL while scanning string literal
  
Çözüm olarak birkaç farklı yöntemden yararlanabilirsiniz. Mesela karakter
dizisini kapatmadan önce karakter dizisinin sonundaki `\\` işaretinin sağına bir
adet boşluk karakteri yerleştirmeyi deneyebilirsiniz::
    
    >>> print("Kaçış dizisi: \ ")

Veya kaçış dizisini çiftleyebilirsiniz::
    
    >>> print("Kaçış dizisi: \\")

Ya da karakter dizisi birleştirme yöntemlerinden herhangi birini
kullanabilirsiniz::
    
    >>> print("Kaçış dizisi: " + "\\")
    >>> print("Kaçış dizisi:", "\\")
    >>> print("Kaçış dizisi: " "\\")

Böyle bir durumla ilk kez karşılaştığınızda bunun Python programlama dilinden
kaynaklanan bir hata olduğunu düşünebilirsiniz, ancak bu durum Python'ın resmi
internet sitesinde 'Sıkça Sorulan Sorular' bölümüne alınacak kadar önemli bir
tasarım tercihidir: http://goo.gl/i3tkk

Sayfa Başı (\\f)
******************

`\\f` artık günümüzde pek kullanılmayan bir kaçış dizisidir. Bu kaçış dizisinin
görevi, özellikle eski yazıcılarda, bir sayfanın sona erip yeni bir sayfanın
başladığını göstermektir. Dolayısıyla eski model yazıcılar, bu karakteri
gördükleri noktada mevcut sayfayı sona erdirip yeni bir sayfaya geçer.

Bu kaçış dizisinin tam olarak ne işe yaradığını test etmek için şu kodları
çalıştırın::
    
    >>> f = open("deneme.txt", "w")
    >>> print("deneme\fdeneme", file=f)
    >>> f.close()
    
Şimdi bu kodlarla oluşturduğunuz `deneme.txt` adlı dosyayı LibreOffice veya
Microsoft Word gibi bir programla açın. 'deneme' satırlarının iki farklı sayfaya
yazdırıldığını göreceksiniz. Bu arada, eğer Microsoft Word dosyayı açarken bir
hata mesajı gösterirse, o hata mesajına birkaç kez 'tamam' diyerek hata
penceresini kapatın. Dosya normal bir şekilde açılacaktır.

Dediğimiz gibi, bu kaçış dizisi artık pek kullanılmıyor. Ama yine de bu kaçış
dizisine karşı da uyanık olmalısınız. Çünkü bu kaçış dizisi de beklemediğiniz
çıktılar almanıza yol açabilir. Mesela şu örneğe bir bakalım::

    >>> "\fırat"
    
    '\x0cırat'
    
Gördüğünüz gibi, siz aslında '\\fırat' yazmak isterken, Python bu kelimenin baş 
tarafındaki `\\f` karakter dizisini bir kaçış dizisi olarak değerlendirip ona 
göre bir çıktı verdi.

Bütün bu anlattıklarımızın ardından, kaçış dizilerinin, birleştirildikleri
karakterlerin farklı bir anlam yüklenmesini sağlayan birtakım işaretler olduğunu
anlıyoruz. Örneğin `\\` işareti `'` (tek tırnak) işareti ile bir araya gelerek,
tek tırnak işaretinin karakter dizisi tanımlama dışında başka bir anlam
yüklenmesini sağlıyor. Aynı şekilde yine `\\` işareti `"` (çift tırnak) işareti
ile birleşerek çift tırnak işaretinin de karakter dizisi tanımlama dışında bir
anlama kavuşmasını sağlıyor. Böylece tırnak işaretlerini karakter dizileri
içinde rahatlıkla kullanabiliyoruz.

Ya da yine `\\` işareti 'n' harfi ile bir araya gelip, bu harfin satır başına
geçilmesini sağlayan bir kaçış dizisi oluşturmasını mümkün kılıyor. Veya aynı
işaret 't' harfiyle birleşip, öğeler arasında sekme oluşturulmasını
sağlayabiliyor. Bu araçlar sayesinde ekrana yazdırdığımız bir metnin akışını
kontrol etme imkanına kavuşuyoruz.

Kaçış Dizilerine Toplu Bakış
******************************

Biraz sonra bu önemli konuyu kapatacağız. Ama dilerseniz kapatmadan önce, bu
bölümde öğrendiğimiz kaçış dizilerini şöyle bir topluca görelim:

+--------------+----------------------------------------------+
| Kaçış Dizisi | Anlamı                                       |
+==============+==============================================+
| `\\'`        | Karakter dizisi içinde tek tırnak işaretini  | 
|              | kullanabilmemizi sağlar.                     |
+--------------+----------------------------------------------+
| `\\"`        | Karakter dizisi içinde çift tırnak işaretini |
|              | kullanabilmemizi sağlar.                     |
+--------------+----------------------------------------------+
| `\\\\`       | Karakter dizisi içinde `\\` işaretini        |
|              | kullanabilmemizi sağlar.                     |
+--------------+----------------------------------------------+
| `\\n`        | Yeni bir satıra geçmemizi sağlar.            |
+--------------+----------------------------------------------+
| `\\t`        | Karakterler arasında sekme boşluğu           |
|              | bırakmamızı sağlar.                          |
+--------------+----------------------------------------------+
| `\\u`        | UNICODE kod konumlarını gösterebilmemizi     |
|              | sağlar.                                      |
+--------------+----------------------------------------------+
| `\\U`        | UNICODE kod konumlarını gösterebilmemizi     |
|              | sağlar.                                      |
+--------------+----------------------------------------------+
| `\\N`        | Karakterleri UNICODE adlarına göre           |
|              | kullanabilmemizi sağlar.                     |
+--------------+----------------------------------------------+
| `\\x`        | Onaltılı sistemdeki bir sayının karakter     |
|              | karşılığını gösterebilmemizi sağlar.         |
+--------------+----------------------------------------------+
| `\\a`        | Destekleyen sistemlerde, kasa hoparlöründen  |
|              | bir 'bip' sesi verilmesini sağlar.           |
+--------------+----------------------------------------------+
| `\\r`        | Aynı satırın başına dönülmesini sağlar.      |
+--------------+----------------------------------------------+
| `\\v`        | Destekleyen sistemlerde düşey sekme          |
|              | oluşturulmasını sağlar.                      |
+--------------+----------------------------------------------+
| `\\b`        | İmlecin sola doğru kaydırılmasını sağlar     |
+--------------+----------------------------------------------+
| `\\f`        | Yeni bir sayfaya geçilmesini sağlar.         |
+--------------+----------------------------------------------+
| `r`          | Karakter dizisi içinde kaçış dizilerini      |
|              | kullanabilmemizi sağlar.                     |
+--------------+----------------------------------------------+

Kaçış dizileriyle ilgili son olarak şunu söyleyebiliriz: Kaçış dizileri,
görmezden gelebileceğiniz, 'öğrenmesem de olur,' diyebileceğiniz önemsiz
birtakım işaretler değildir. Bu konu boyunca verdiğimiz örneklerden de
gördüğünüz gibi, kaçış dizileri, kullanıcıya göstereceğiniz metinlerin biçimini
doğrudan etkiliyor. Bütün bu örnekler, bu kaçış dizilerinin yersiz veya yanlış
kullanılmasının ya da bunların bir metin içinde gözden kaçmasının, yazdığınız
programların hata verip çökmesine, yani programınızın durmasına sebep
olabileceğini de gösteriyor bize.

Böylece bir bölümü daha bitirmiş olduk. Artık Python'la 'gerçek' programlar
yazmamızın önünde hiçbir engel kalmadı.
