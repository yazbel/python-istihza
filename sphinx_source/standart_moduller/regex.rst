.. meta::
   :description: Python'da düzenli ifadeler (regular expressions) 
   :keywords: Python, python3, regex, düzenli ifadeler, regular expressions

*****************
Düzenli İfadeler
*****************

Düzenli ifadeler Python programlama dilinin en çetrefilli konularından biridir.
Öyle ki, düzenli ifadelerin Python içinde ayrı bir dil olarak düşünülmesi
gerektiğini söyleyenler dahi vardır. Ama bütün zorluklarına rağmen programlama
deneyimimizin bir noktasında mutlaka karşımıza çıkacak olan bu yapıyı
öğrenmemizde büyük fayda var. Düzenli ifadeleri öğrendikten sonra, elle
yapılması saatler sürecek bir işlemi saliseler içinde yapabildiğinizi
gördüğünüzde eminim düzenli ifadelerin ne büyük bir nimet olduğunu siz de
anlayacaksınız. Tabii her güzel şey gibi, düzenli ifadelerin nimetlerinden
yararlanabilecek düzeye gelmek de bir miktar kan, ter ve gözyaşı istiyor.

Peki, düzenli ifadeleri kullanarak neler yapabiliriz? Çok genel bir ifadeyle, bu
yapıyı kullanarak metinleri veya karakter dizilerini parmağımızda oynatabiliriz.
Örneğin bir web sitesinde dağınık halde duran verileri bir çırpıda
ayıklayabiliriz. Bu veriler, mesela, toplu halde görmek istediğimiz web
adreslerinin bir listesi olabilir. Bunun dışında, örneğin, çok sayıda belge
üzerinde tek adımda istediğimiz değişiklikleri yapabiliriz.

Ancak genel bir kural olarak, düzenli ifadelerden kaçabildiğimiz müddetçe
kaçmamız gerekir. Eğer Python'daki karakter dizisi metotları, o anda yapmak
istediğimiz şey için yeterli geliyorsa mutlaka o metotları kullanmalıyız. Çünkü
karakter dizisi metotları, düzenli ifadelere kıyasla hem daha basit, hem de çok
daha hızlıdır. Ama bir noktadan sonra karakter dizilerini kullanarak yazdığınız
kodlar iyice karmaşıklaşmaya başlamışsa, kodların her tarafı `if` deyimleriyle
dolmuşsa, hatta basit bir işlemi gerçekleştirmek için yazdığınız kod sayfa
sınırlarını zorlamaya başlamışsa, işte o noktada artık düzenli ifadelerin
dünyasına adım atmanız gerekiyor olabilir. Ama bu durumda Jamie Zawinski'nin şu
sözünü de aklınızdan çıkarmayın: *"Bazıları, bir sorunla karşı karşıya
kaldıklarında şunu der: 'Evet, burada düzenli ifadeleri kullanmam gerekiyor.'
İşte onların bir sorunu daha vardır artık..."*

Başta da söylediğim gibi, düzenli ifadeler bize zorlukları unutturacak kadar
büyük kolaylıklar sunar. Emin olun yüzlerce dosya üzerinde tek tek elle
değişiklik yapmaktan daha zor değildir düzenli ifadeleri öğrenip kullanmak...
Hem zaten biz de bu sayfalarda bu "sevimsiz" konuyu olabildiğince sevimli hale
getirmek için elimizden gelen çabayı göstereceğiz. Sizin de çaba göstermeniz,
bol bol alıştırma yapmanız durumunda düzenli ifadeleri kavramak o kadar da
zorlayıcı olmayacaktır. Unutmayın, düzenli ifadeler ne kadar uğraştırıcı olsa da
programcının en önemli silahlarından biridir. Hatta düzenli ifadeleri
öğrendikten sonra onsuz geçen yıllarınıza acıyacaksınız.

Şimdi lafı daha fazla uzatmadan işimize koyulalım.

Düzenli İfadelerin Metotları
******************************

Python'daki düzenli ifadelere ilişkin her şey bir modül içinde tutulur. Bu
modülün adı `re`. Tıpkı `os` modülünde, `sys` modülünde, `tkinter` modülünde ve
öteki bütün modüllerde olduğu gibi, düzenli ifadeleri kullanabilmemiz için de
öncelikle bu `re` modülünü içe aktarmamız gerekecek. Bu işlemi nasıl
yapacağımızı çok iyi biliyorsunuz::

    >>> import re

Başta da söylediğimiz gibi, düzenli ifadeler bir programcının en önemli
silahlarından biridir. Şu halde silahımızın özelliklerine bakalım. Yani bu
yapının bize sunduğu araçları şöyle bir listeleyelim. Etkileşimli kabukta şu
kodu yazıyoruz::

    >>> dir(re)

Tabii yukarıdaki ``dir(re)`` komutunu yazmadan önce ``import re`` şeklinde
modülümüzü içe aktarmış olmamız gerekiyor. 

Gördüğünüz gibi, `re` modülü içinde epey metot/fonksiyon var. Biz bu sayfada ve
ilerleyen sayfalarda, yukarıdaki metotların/fonksiyonların en sık
kullanılanlarını size olabildiğince yalın bir şekilde anlatmaya çalışacağız.
Eğer isterseniz, şu komutu kullanarak yukarıdaki metotlar/fonksiyonlar hakkında
yardım da alabilirsiniz::

    >>> help(metot_veya_fonksiyon_adı)

Bir örnek vermek gerekirse::

    >>> help(re.match)

    Help on function match in module re:
    match(pattern, string, flags=0)
     Try to apply the pattern at the start of the string,
    returning a match object, or None if no match was found.

Ne yazık ki, Python'ın yardım dosyaları hep İngilizce. Dolayısıyla eğer
İngilizce bilmiyorsanız, bu yardım dosyaları pek işinize yaramayacaktır. Bu
arada yukarıdaki yardım bölümünden çıkmak için klavyedeki `q` düğmesine basmanız
gerekir.

match() Metodu
=================

Bir önceki bölümde metotlar hakkında yardım almaktan bahsederken ilk örneğimizi
``match()`` metoduyla vermiştik, o halde ``match()`` metodu ile devam edelim.

``match()`` metodunu tarif etmek yerine, isterseniz bir örnek yardımıyla bu
metodun ne işe yaradığını anlamaya çalışalım. Diyelim ki elimizde şöyle bir
karakter dizisi var::

    >>> a = "python güçlü bir programlama dilidir."

Varsayalım ki biz bu karakter dizisi içinde 'python' kelimesi geçip geçmediğini
öğrenmek istiyoruz. Ve bunu da düzenli ifadeleri kullanarak yapmak istiyoruz.
Düzenli ifadeleri bu örneğe uygulayabilmek için yapmamız gereken şey, öncelikle
bir düzenli ifade kalıbı oluşturup, daha sonra bu kalıbı yukarıdaki karakter
dizisi ile karşılaştırmak. Biz bütün bu işlemleri ``match()`` metodunu
kullanarak yapabiliriz::

    >>> re.match("python", a)

Burada, `'python'` şeklinde bir düzenli ifade kalıbı oluşturduk. Düzenli ifade
kalıpları ``match()`` metodunun ilk argümanıdır (yani parantez içindeki ilk
değer). İkinci argümanımız ise (yani parantez içindeki ikinci değer),
hazırladığımız kalıbı kendisiyle eşleştireceğimiz karakter dizisi olacaktır.

Klavyede ENTER tuşuna bastıktan sonra karşımıza şöyle bir çıktı gelecek::

    <_sre.SRE_Match object; span=(0, 6), match='python'>

Bu çıktı, düzenli ifade kalıbının karakter dizisi ile eşleştiği anlamına
geliyor. Yani aradığımız şey, karakter dizisi içinde bulunmuş.

Yukarıdaki çıktıda gördüğümüz ifadeye Python'cada eşleşme nesnesi (*match
object*) adı veriliyor. Çünkü ``match()`` metodu yardımıyla yaptığımız şey
aslında bir eşleştirme işlemidir (*match* kelimesi İngilizcede 'eşleşmek'
anlamına gelir). Biz burada `'python'` düzenli ifadesinin `a` değişkeniyle
eşleşip eşleşmediğine bakıyoruz. Yani ``re.match("python", a)`` ifadesi
aracılığıyla 'python' ifadesi ile `a` değişkeninin tuttuğu karakter dizisinin
eşleşip eşleşmediğini sorguluyoruz. Bizim örneğimizde 'python' `a` değişkeninin
tuttuğu karakter dizisi ile eşleştiği için bize bir eşleşme nesnesi
döndürülüyor.

Bu çıktı, düzenli ifade kalıbının karakter dizisi ile eşleştiğini bildirmenin
yanısıra, bize başka birtakım bilgiler daha veriyor. Mesela bu çıktıdaki `span`
parametresi, aradığımız 'python' karakter dizisinin, `a` değişkeninin 0. ila 6.
karakterleri arasında yer aldığını söylüyor bize. Yani::
    
    >>> a[0:6]
    
    'python'
    
Ayrıca yukarıdaki çıktıda gördüğümüz `match` parametresi de bize eşleşen
ifadenin 'python' olduğu bilgisini veriyor.

Bir de şu örneğe bakalım::

    >>> re.match("Java", a)

Burada ENTER tuşuna bastığımızda hiç bir çıktı almıyoruz. Aslında biz görmesek
de Python burada "None" çıktısı veriyor. Eğer yukarıdaki komutu şöyle yazarsak
"None" çıktısını biz de görebiliriz::

    >>> print(re.match("Java", a))
    
    None

Gördüğünüz gibi, ENTER tuşuna bastıktan sonra "None" çıktısı geldi. Demek ki
"Java" ifadesi, "a" değişkeninin tuttuğu karakter dizisi ile eşleşmiyormuş.
Buradan çıkardığımız sonuca göre, Python ``match()`` metodu yardımıyla
aradığımız şeyi eşleştirdiği zaman bir eşleşme nesnesi (*match object*)
döndürüyor. Eğer eşleşme yoksa, o zaman da "None" değerini döndürüyor.

Biraz kafa karıştırmak için şöyle bir örnek verelim::

    >>> a = "Python güçlü bir dildir"
    >>> re.match("güçlü", a)

Burada "a" değişkeninde "güçlü" ifadesi geçtiği halde ``match()`` metodu bize
bir eşleşme nesnesi döndürmedi. Peki ama neden?

Aslında bu gayet normal. Çünkü ``match()`` metodu bir karakter dizisinin sadece
en başına bakar. Yani "Python güçlü bir dildir" ifadesini tutan `a` değişkenine
re.match("güçlü", a) gibi bir fonksiyon uyguladığımızda, ``match()`` metodu `a`
değişkeninin yalnızca en başına bakacağı ve `a` değişkeninin en başında "güçlü"
yerine "python" olduğu için, ``match()`` metodu bize olumsuz yanıt veriyor.

Aslında ``match()`` metodunun yaptığı bu işi, karakter dizilerinin ``split()``
metodu yardımıyla da yapabiliriz::

    >>> a.split()[0] == "python"
    
    True

Demek ki `a` değişkeninin en başında "python" ifadesi varmış. Bir de şuna
bakalım::

    >>> a.split()[0] == "güçlü"
    
    False

Veya aynı işi sadece ``startswith()`` metodunu kullanarak dahi yapabiliriz::

    >>> a.startswith("python")

Eğer düzenli ifadelerden tek beklentiniz bir karakter dizisinin en başındaki
veriyle eşleştirme işlemi yapmaksa, ``split()`` veya ``startswith()``
metotlarını kullanmak daha mantıklıdır. Çünkü ``split()`` ve ``startswith()``
metotları ``match()`` metodundan çok daha hızlı çalışacaktır.

``match()`` metodunu kullanarak bir kaç örnek daha yapalım::

    >>> sorgu = "1234567890"
    >>> re.match("1", sorgu)
    
    <_sre.SRE_Match object; span=(0, 1), match='1'>   
    
    >>> re.match("1234", sorgu)
    
    <_sre.SRE_Match object; span=(0, 4), match='1234'>
    
    >>> re.match("124", sorgu)
    
İsterseniz şimdiye kadar öğrendiğimiz şeyleri şöyle bir gözden geçirelim:

#. Düzenli ifadeler Python'ın çok güçlü araçlarından biridir.

#. Python'daki düzenli ifadelere ilişkin bütün fonksiyonlar `re` adlı
   bir modül içinde yer alır.

#. Dolayısıyla düzenli ifadeleri kullanabilmek için öncelikle bu `re`
   modülünü ``import re`` diyerek içe aktarmamız gerekir.

#. `re` modülünün içeriğini ``dir(re)`` komutu yardımıyla listeleyebiliriz.

#. ``match()`` metodu `re` modülü içindeki fonksiyonlardan biridir.

#. ``match()`` metodu bir karakter dizisinin yalnızca en başına bakar.

#. Eğer aradığımız şey karakter dizisinin en başında yer alıyorsa,
   ``match()`` metodu bir eşleştirme nesnesi döndürür.

#. Eğer aradığımız şey karakter dizisinin en başında yer almıyorsa,
   ``match()`` metodu "None" değeri döndürür.

Daha önce söylediğimiz gibi, ``match()`` metodu ile bir eşleştirme işlemi
yaptığımızda, eğer eşleşme varsa Python bize bir eşleşme nesnesi döndürecektir.
Döndürülen bu eşleşme nesnesi bize `span` ve `match` parametreleri aracılığıyla,
eşleşen karakter dizisinin sorgu dizisi içindeki yerini ve eşleşen dizinin ne
olduğu söylüyor. `span` paramtresinin değerine ``span()`` adlı bir metot
yardımıyla erişebiliyoruz. Örneğin::
    
    >>> import re
    >>> sorgu = 'Bin kunduz'
    >>> eşleşme = re.match('Bin', sorgu)
    >>> eşleşme
    
    <_sre.SRE_Match object; span=(0, 3), match='Bin'>
    
    >>> eşleşme.span()
    (0, 3)
    
Ancak, ``match()`` metodu ile bulunan şeyin ne olduğunu eşleşme nesnesinin
`match` parametresine bakarak görebilsek de, bu değeri bir kod yardımıyla
alamıyoruz. Çünkü eşleşme nesnelerinin ``span()`` metoduna benzeyen bir
``match()`` metodu bulunmaz.

Ama istersek tabii ki bulunan şeyi de programatik olarak alma imkânımız var.
Bunun için ``group()`` adlı bir başka metottan yararlanacağız::
    
    >>> kardiz = "perl, python ve ruby yüksek seviyeli dillerdir."
    >>> eşleşme = re.match("perl", kardiz)
    >>> eşleşme.group()
    
    'perl'

Burada, ``re.match("perl", kardiz)`` komutunu bir değişkene atadık.
Hatırlarsanız, bu fonksiyonu komut satırına yazdığımızda bir eşleşme nesnesi
elde ediyorduk. İşte burada değişkene atadığımız şey aslında bu eşleşme
nesnesinin kendisi oluyor. Bu durumu şu şekilde teyit edebilirsiniz::

    >>> type(eşleşme)
    
    <class '_sre.SRE_Match'>

Gördüğünüz gibi, `eşleşme` değişkeninin tipi bir eşleşme nesnesi (*match
object*). İsterseniz bu nesnenin metotlarına bir göz gezdirebiliriz::

    >>> dir(eşleşme)

Dikkat ederseniz yukarıda kullandığımız ``group()`` metodu listede görünüyor. Bu
metot, doğrudan doğruya düzenli ifadelerin değil, eşleşme nesnelerinin bir
metodudur. Listedeki öbür metotları da sırası geldiğinde inceleyeceğiz. Şimdi
isterseniz bir örnek daha yapıp bu konuyu kapatalım::

    >>> iddia = "Adana memleketlerin en güzelidir!"
    >>> nesne = re.match("Adana", iddia)
    >>> nesne.group()
    
    'Adana'

Peki, eşleştirmek istediğimiz düzenli ifade kalıbı bulunamazsa ne olur? Öyle bir
durumda yukarıdaki kodlar hata verecektir. Hemen bakalım::

    >>> nesne = re.match("İstanbul", iddia)
    >>> nesne.group()

Hata mesajımız::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'NoneType' object has no attribute 'group'

Böyle bir hata, yazdığınız bir programın çökmesine neden olabilir. O yüzden
kodlarımızı şuna benzer bir şekilde yazmamız daha mantıklı olacaktır::

    >>> nesne = re.match("İstanbul", iddia)
    >>> if nesne:
    ...     print("eşleşen ifade:", nesne.group())
    ... else:
    ...     print("eşleşme başarısız!")

Şimdi isterseniz bu ``match()`` metoduna bir ara verip başka bir metodu
inceleyelim.

search() Metodu
================

Bir önceki bölümde incelediğimiz ``match()`` metodu, karakter dizilerinin sadece
en başına bakıyordu. Ama istediğimiz şey tabii ki her zaman bununla sınırlı
olmayacaktır. ``match()`` metodunun, karakter dizilerinin sadece başına
bakmasını engellemenin yolları olmakla birlikte, bizim işimizi görecek çok daha
kullanışlı bir metodu vardır düzenli ifadelerin. Önceki bölümde ``dir(re)``
şeklinde gösterdiğimiz listeye tekrar bakarsanız, orada `re` modülünün
``search()`` adlı bir metodu olduğunu göreceksiniz. İşte bu yazımızda
inceleyeceğimiz metot bu ``search()`` metodu olacaktır.

``search()`` metodu ile ``match()`` metodu arasında çok önemli bir fark vardır.
``match()`` metodu bir karakter dizisinin en başına bakıp bir eşleştirme işlemi
yaparken, ``search()`` metodu karakter dizisinin genelinde bir arama işlemi
yapar. Yani biri eşleştirir, öbürü arar.

Hatırlarsanız, ``match()`` metodunu anlatırken şöyle bir örnek vermiştik::

    >>> a = "Python güçlü bir dildir"
    >>> re.match("güçlü", a)

Yukarıdaki kod, karakter dizisinin başında bir eşleşme bulamadığı için bize
`None` değeri döndürüyordu. Ama eğer aynı işlemi şöyle yaparsak, daha farklı bir
sonuç elde ederiz::
    
    >>> a = "Python güçlü bir dildir"
    >>> re.search("güçlü", a)
    
 <_sre.SRE_Match object; span=(7, 12), match='güçlü'>
 
Gördüğünüz gibi, ``search()`` metodu "güçlü" kelimesini buldu. Çünkü
``search()`` metodu, ``match()`` metodunun aksine, bir karakter dizisinin sadece
baş tarafına bakmakla yetinmiyor, karakter dizisinin geneli üzerinde bir arama
işlemi gerçekleştiriyor.

Tıpkı ``match()`` metodunda olduğu gibi, ``search()`` metodunda da ``span()`` ve
``group()`` metotlarından faydalanarak bulunan şeyin hangi aralıkta olduğunu ve
bu şeyin ne olduğunu görüntüleyebiliriz::

    >>> kardiz = "Python güçlü bir dildir"
    >>> nesne = re.search("güçlü", kardiz)
    >>> nesne.span()
    
    (7, 12)
    
    >>> nesne.group()
    
    'güçlü'   

Şimdiye kadar hep karakter dizileri üzerinde çalıştık. İsterseniz biraz da
listeler üzerinde örnekler verelim.

Şöyle bir listemiz olsun::

    >>> liste = ["elma", "armut", "kebap"]
    >>> re.search("kebap", liste)

Ne oldu? Hata aldınız, değil mi? Bu normal. Çünkü düzenli ifadeler karakter
dizileri üzerinde işler. Bunlar doğrudan listeler üzerinde işlem yapamaz. O
yüzden bizim Python'a biraz yardımcı olmamız gerekiyor:

    >>> for i in liste::
    ...     nesne = re.search("kebap", i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    kebap

Hatta şimdiye kadar öğrendiklerimizle daha karmaşık bir şeyler de yapabiliriz::

    >>> import re
    >>> from urllib.request import urlopen
    >>> f = urlopen("http://www.istihza.com")
    >>> for i in f:
    ...     nesne = re.search(b'programlama', i)
    ...     if nesne:
    ...             print(nesne.group())
    ...
    b'programlama'
    b'programlama'

Gördüğünüz gibi, www.istihza.com sayfasında kaç adet "programlama"
kelimesi geçiyorsa hepsi ekrana dökülüyor.

Bu arada, websitesinde arama işlemi gerçekleştirirken `urllib` paketinin
içindeki `request` modülünün ``urlopen()`` adlı fonksiyonunu kullandığımıza
dikkat edin. Ayrıca ``search()`` metoduna parametre olarak bir karakter dizisi
değil, bayt dizisi verdiğimizi de gözden kaçırmayın::

    re.search(b'programlama', i)
    
Siz isterseniz bu kodları biraz daha geliştirebilirsiniz::

    import re
    from urllib.request import urlopen
    
    kelime = input("istihza.com'da aramak istediğiniz kelime: ")
    
    f = urlopen("http://www.istihza.com")
    data = str(f.read())
    
    nesne = re.search(kelime, data)
    
    if nesne:
        print("kelime bulundu:", nesne.group())
    else:
        print("kelime bulunamadı!:", kelime)
        
Burada, kullanıcıdan aldığımız kelimeyi ``search()`` metoduna göndermeden önce,
siteden okuduğumuz verileri ``str()`` metodu yardımıyla karakter dizisine
dönüştürdüğümüze dikkat edin. Böylece kullanıcıdan gelen karakter dizisini bayt
dizisine çevirmemize gerek kalmadı.

İlerde bilgimiz artınca daha yetkin kodlar yazabilecek duruma geleceğiz. Ama
şimdilik elimizde olanlar ancak yukarıdaki kodu yazmamıza müsaade ediyor.
Unutmayın, düzenli ifadeler sahasında ısınma turları atıyoruz daha...

findall() Metodu
================

Python komut satırında, yani etkileşimli kabukta, ``dir(re)`` yazdığımız zaman
aldığımız listeye tekrar bakarsak orada bir de ``findall()`` adlı bir metodun
olduğunu görürüz. İşte bu bölümde ``findall()`` adlı bu önemli metodu incelemeye
çalışacağız.

Önce şöyle bir metin alalım elimize::
    
    metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani
    aslında Python için nispeten yeni bir dil denebilir. Ancak Python'un çok uzun
    bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı olması,
    ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden
    ötürü çoğu kimsenin gözdesi haline gelmiştir. Ayrıca Google'ın da Python'a özel
    bir önem ve değer verdiğini, çok iyi derecede Python bilenlere iş olanağı
    sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın
    yaratıcısı Guido Van Rossum Google'de işe başladı..."""

Bu metin içinde geçen bütün "Python" kelimelerini bulmak istiyoruz::

    print(re.findall("Python", metin))
    
    ['Python', 'Python', 'Python', 'Python', 'Python', 'Python']

Gördüğünüz gibi, metinde geçen bütün "Python" kelimelerini bir çırpıda liste
olarak aldık. Aynı işlemi ``search()`` metodunu kullanarak yapmak istersek yolu
biraz uzatmamız gerekir::

    >>> liste = metin.split()
    >>> for i in liste:
    ...     nesne = re.search("Python", i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    Python
    Python
    Python
    Python
    Python
    Python

Gördüğünüz gibi, metinde geçen bütün "Python" kelimelerini ``search()`` metodunu
kullanarak bulmak için öncelikle "metin" adlı karakter dizisini, daha önce
karakter dizilerini işlerken gördüğümüz ``split()`` metodu yardımıyla bir liste
haline getiriyoruz. Ardından bu liste üzerinde bir `for` döngüsü kurarak
``search()`` ve ``group()`` metotlarını kullanarak bütün "Python" kelimelerini
ayıklıyoruz. Eğer karakter dizisini yukarıdaki şekilde listeye dönüştürmezsek
şöyle bir netice alırız::

    >>> nesne = re.search("Python", metin)
    >>> print(nesne.group())
    
    Python

Bu şekilde metinde geçen sadece ilk "Python" kelimesini alabiliyoruz. 

Metakarakterler
*****************

Şimdiye kadar düzenli ifadelerle ilgili olarak verdiğimiz örnekler sizi biraz
şaşırtmış olabilir. "Zor dediğin bunlar mıydı?" diye düşünmüş olabilirsiniz.
Haklısınız, zira "zor" dediğim, buraya kadar olan kısımda verdiğim örneklerden
ibaret değildir. Buraya kadar olan bölümde verdiğim örnekler işin en temel
kısmını gözler önüne sermek içindi. Şimdiye kadar olan bölümde, mesela, "python"
karakter dizisiyle eşleştirme yapmak için "python" kelimesini kullandık.
Esasında bu, düzenli ifadelerin en temel özelliğidir. Yani "python" karakter
dizisini bir düzenli ifade sayacak olursak (ki zaten öyledir), bu düzenli ifade
en başta kendisiyle eşleşecektir. Bu ne demek? Şöyle ki: Eğer aradığınız şey
"python" karakter dizisi ise, kullanmanız gereken düzenli ifade de "python"
olacaktır. 

Diyoruz ki: "Düzenli ifadeler en başta kendileriyle eşleşirler". Buradan şu
anlam çıkıyor: Demek ki bir de kendileriyle eşleşmeyen düzenli ifadeler var.
İşte bu durum, Python'daki düzenli ifadelere kişiliğini kazandıran şeydir. Biraz
sonra ne demek istediğimizi daha açık anlayacaksınız. Artık gerçek anlamıyla
düzenli ifadelere giriş yapıyoruz!

Öncelikle, elimizde aşağıdaki gibi bir liste olduğunu varsayalım::
    
    >>> liste = ["özcan", "mehmet", "süleyman", "selim",    
    ... "kemal", "özkan", "esra", "dündar", "esin",    
    ... "esma", "özhan", "özlem"]

Diyelim ki, biz bu liste içinden "özcan", "özkan" ve "özhan" öğelerini
ayıklamak/almak istiyoruz. Bunu yapabilmek için yeni bir bilgiye
ihtiyacımız var: Metakarakterler.

Metakarakterler; kabaca, programlama dilleri için özel anlam ifade eden
sembollerdir. Örneğin daha önce gördüğümüz `\\n` bir bakıma bir metakarakterdir.
Çünkü `\\n` sembolü Python için özel bir anlam taşır. Python bu sembolü gördüğü
yerde yeni bir satıra geçer. Yukarıda "kendisiyle eşleşmeyen karakterler"
ifadesiyle kastettiğimiz şey de işte bu metakarakterlerdir. Örneğin, "a" harfi
yalnızca kendisiyle eşleşir. Tıpkı "istihza" kelimesinin yalnızca kendisiyle
eşleşeceği gibi... Ama mesela `\\t` ifadesi kendisiyle eşleşmez. Python bu
işareti gördüğü yerde sekme (tab) düğmesine basılmış gibi tepki verecektir. İşte
düzenli ifadelerde de buna benzer metakarakterlerden yararlanacağız. Düzenli
ifadeler içinde de, özel anlam ifade eden pek çok sembol, yani metakarakter
vardır. Bu metakarakterlerden biri de "[ ]" sembolüdür. Şimdi yukarıda
verdiğimiz listeden "özcan", "özhan" ve "özkan" öğelerini bu sembolden
yararlanarak nasıl ayıklayacağımızı görelim::

    >>> re.search("öz[chk]an", liste)

Bu kodu böyle yazmamamız gerektiğini artık biliyoruz. Aksi halde hata
alırız. Çünkü daha önce de dediğimiz gibi, düzenli ifadeler karakter
dizileri üzerinde işlem yapabilir. Listeler üzerinde değil. Dolayısıyla
komutumuzu şu şekilde vermemiz gerekiyor::

    >>> for i in liste:
    ...     nesne = re.search("öz[chk]an", i)
    ...     if nesne:
    ...         print(nesne.group())

Aynı işlemi şu şekilde de yapabiliriz::

    >>> for i in liste:
    ...     if re.search("öz[chk]an",i):
    ...         print(i)

Ancak, bu örnekte pek belli olmasa da, son yazdığımız kod her zaman
istediğimiz sonucu vermez. Mesela listemiz şöyle olsaydı::

    >>> liste = ["özcan demir", "mehmet", "süleyman",
    ... "selim", "kemal", "özkan nuri", "esra", "dündar",
    ... "esin", "esma", "özhan kamil", "özlem"]

Yukarıdaki kod bu liste üzerine uygulandığında, sadece almak istediğimiz
kısım değil, ilgisiz kısımlar da gelecektir.

Gördüğünüz gibi, uygun kodları kullanarak, "özcan", "özkan" ve "özhan"
öğelerini listeden kolayca ayıkladık. Bize bu imkânı veren şey ise "[ ]"
adlı metakarakter oldu. Aslında "[ ]" metakarakterinin ne işe yaradığını
az çok anlamış olmalısınız. Ama biz yine de şöyle bir bakalım bu
metakaraktere:

"[ ]" adlı metakarakter, yukarıda verdiğimiz listedeki "öz" ile
başlayıp, "c", "h" veya "k" harflerinden herhangi biri ile devam eden ve
"an" ile biten bütün öğeleri ayıklıyor. Gelin bununla ilgili bir örnek
daha yapalım::

    >>> for i in liste:
    ...     nesne = re.search("es[mr]a",i)
    ...     if nesne:
    ...         print(nesne.group())

Gördüğünüz gibi, "es" ile başlayıp, "m" veya "r" harflerinden herhangi
biriyle devam eden ve sonunda da "a" harfi bulunan bütün öğeleri
ayıkladık. Bu da bize "esma" ve "esra" çıktılarını verdi...

Dediğimiz gibi, metakarakterler programlama dilleri için özel anlam
ifade eden sembollerdir. "Normal" karakterlerden farklı olarak,
metakarakterlerle karşılaşan bir bilgisayar normalden farklı bir tepki
verecektir. Yukarıda metakarakterlere örnek olarak "\\n" ve "\\t" kaçış
dizilerini vermiştik. Örneğin Python'da print("\\n") gibi bir komut
verdiğimizde, Python ekrana "\\n" yazdırmak yerine bir alt satıra
geçecektir. Çünkü "\\n" Python için özel bir anlam taşımaktadır. Düzenli
ifadelerde de birtakım metakarakterlerin kullanıldığını öğrendik. Bu
metakarakterler, düzenli ifadeleri düzenli ifade yapan şeydir. Bunlar
olmadan düzenli ifadelerle yararlı bir iş yapmak mümkün olmaz. Bu giriş
bölümünde düzenli ifadelerde kullanılan metakarakterlere örnek olarak "[
]" sembolünü verdik. Herhangi bir düzenli ifade içinde "[ ]" sembolünü
gören Python, doğrudan doğruya bu sembolle eşleşen bir karakter dizisi
aramak yerine, özel bir işlem gerçekleştirecektir. Yani "[ ]" sembolü
kendisiyle eşleşmeyecektir...

Python'da bulunan temel metakarakterleri topluca görelim::

    [ ] . \* + ? { } ^ $ | ( )

Doğrudur, yukarıdaki karakterler, çizgi romanlardaki küfürlere benziyor.
Endişelenmeyin, biz bu metakarakterleri olabildiğince sindirilebilir
hale getirmek için elimizden gelen çabayı göstereceğiz.

Bu bölümde düzenli ifadelerin zor kısmı olan metakarakterlere,
okurlarımızı ürkütmeden, yumuşak bir giriş yapmayı amaçladık. Şimdi
artık metakarakterlerin temelini attığımıza göre üste kat çıkmaya
başlayabiliriz.

[ ] (Köşeli Parantez)
======================

[ ] adlı metakaraktere önceki bölümde değinmiştik. Orada verdiğimiz
örnek şuydu::

    >>> for i in liste:
    ...     nesne = re.search("öz[chk]an", i)
    ...     if nesne:
    ...         print(nesne.group())

Yukarıdaki örnekte, bir liste içinde geçen "özcan", "özhan" ve "özkan"
öğelerini ayıklıyoruz. Burada bu üç öğedeki farklı karakterleri ("c",
"h" ve "k") köşeli parantez içinde nasıl belirttiğimize dikkat edin.
Python, köşeli parantez içinde gördüğü bütün karakterleri tek tek liste
öğelerine uyguluyor. Önce "öz" ile başlayan bütün öğeleri alıyor,
ardından "öz" hecesinden sonra "c" harfiyle devam eden ve "an" hecesi
ile biten öğeyi buluyor. Böylece "özcan" öğesini bulmuş oldu. Aynı
işlemi, "öz" hecesinden sonra "h" harfini barındıran ve "an" hecesiyle
biten öğeye uyguluyor. Bu şekilde ise "özhan" öğesini bulmuş oldu. En
son hedef ise "öz" ile başlayıp "k" harfi ile devam eden ve "an" ile
biten öğe. Yani listedeki "özkan" öğesi... En nihayetinde de elimizde
"özcan", "özhan" ve "özkan" öğeleri kalmış oluyor.

Bir önceki bölümde yine "[ ]" metakarakteriyle ilgili olarak şu örneği
de vermiştik::

    >>> for i in liste:
    ...     nesne = re.search("es[mr]a",i)
    ...     if nesne:
    ...         print(nesne.group())

Bu örneğin de "özcan, özkan, özhan" örneğinden bir farkı yok. Burada da
Python köşeli parantez içinde gördüğü bütün karakterleri tek tek liste
öğelerine uygulayıp, "esma" ve "esra" öğelerini bize veriyor.

Şimdi bununla ilgili yeni bir örnek verelim

Diyelim ki elimizde şöyle bir liste var::

    >>> a = ["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]

Mesela biz bu listedeki öğeler içinde, sayıyla başlayanları ayıklayalım.
Şimdi şu kodları dikkatlice inceleyin::

    >>> for i in a:
    ...     if re.match("[0-9]",i):
    ...         print(i)
    ...
    23BH56
    4Y7UZ
    34534

Burada parantez içinde kullandığımız ifadeye dikkat edin. "0" ile "9"
arasındaki bütün öğeleri içeren bir karakter dizisi tanımladık. Yani
kısaca, içinde herhangi bir sayı barındıran öğeleri kapsama alanımıza
aldık. Burada ayrıca search() yerine match() metodunu kullandığımıza da
dikkat edin. match() metodunu kullanmamızın nedeni, bu metodun bir
karakter dizisinin sadece en başına bakması... Amacımız sayı ile
başlayan bütün öğeleri ayıklamak olduğuna göre, yukarıda yazdığımız kod,
liste öğeleri içinde yer alan ve sayı ile başlayan bütün öğeleri
ayıklayacaktır. Biz burada Python'a şu emri vermiş oluyoruz:

"Bana sayı ile başlayan bütün öğeleri bul! Önemli olan bu öğelerin
sayıyla başlamasıdır! Sayıyla başlayan bu öğeler ister harfle devam
etsin, ister başka bir karakterle... Sen yeter ki bana sayı ile başlayan
öğeleri bul!"

Bu emri alan Python, hemen liste öğelerini gözden geçirecek ve bize
"23BH56", "4Y7UZ" ve "34534" öğelerini verecektir. Dikkat ederseniz,
Python bize listedeki "TY76Z" ve "TYUDZ" öğelerini vermedi. Çünkü
"TY76Z" içinde sayılar olsa da bunlar bizim ölçütümüze uyacak şekilde en
başta yer almıyor. "TYUDZ" öğesinde ise tek bir sayı bile yok...

Şimdi de isterseniz listedeki "TY76Z" öğesini nasıl alabileceğimize
bakalım::

    >>> for i in a:
    ...     if re.match("[A-Z][A-Z][0-9]",i):
    ...         print(i)

Burada dikkat ederseniz düzenli ifademizin başında "A-Z" diye bir şey
yazdık. Bu ifade "A" ile "Z" harfleri arasındaki bütün karakterleri
temsil ediyor. Biz burada yalnızca büyük harfleri sorguladık. Eğer küçük
harfleri sorgulamak isteseydik "A-Z" yerine "a-z" diyecektik. Düzenli
ifademiz içinde geçen birinci "A-Z" ifadesi aradığımız karakter dizisi
olan "TY76Z" içindeki "T" harfini, ikinci "A-Z" ifadesi "Y" harfini,
"0-9" ifadesi ise "7" sayısını temsil ediyor. Karakter dizisi içindeki
geri kalan harfler ve sayılar otomatik olarak eşleştirilecektir. O
yüzden onlar için ayrı bir şey yazmaya gerek yok. Yalnız bu söylediğimiz
son şey sizi aldatmasın. Bu "otomatik eşleştirme" işlemi bizim şu anda
karşı karşıya olduğumuz karakter dizisi için geçerlidir. Farklı
nitelikteki karakter dizilerinin söz konusu olduğu başka durumlarda
işler böyle yürümeyebilir. Düzenli ifadeleri başarılı bir şekilde
kullanabilmenin ilk şartı, üzerinde işlem yapılacak karakter dizisini
tanımaktır. Bizim örneğimizde yukarıdaki gibi bir düzenli ifade kalıbı
oluşturmak işimizi görüyor. Ama başka durumlarda, duruma uygun başka
kalıplar yazmak gerekebilir/gerekecektir. Dolayısıyla, tek bir düzenli
ifade kalıbıyla hayatın geçmeyeceğini unutmamalıyız.

Şimdi yukarıdaki kodu search() ve group() metotlarını kullanarak yazmayı
deneyin. Elde ettiğiniz sonuçları dikkatlice inceleyin. match() ve
search() metotlarının ne gibi farklılıklara sahip olduğunu kavramaya
çalışın... Sorunuz olursa bana nasıl ulaşacağınızı biliyorsunuz...

Bu arada, düzenli ifadelerle ilgili daha fazla şey öğrendiğimizde
yukarıdaki kodu çok daha sade bir biçimde yazabileceğiz.

. (Nokta)
==========

Bir önceki bölümde "[]" adlı metakarakteri incelemiştik. Bu bölümde ise
farklı bir metakarakteri inceleyeceğiz. İnceleyeceğimiz metakarakter:
"."

Bu metakarakter, yeni satır karakteri hariç bütün karakterleri temsil
etmek için kullanılır. Mesela::

    >>> for i in liste:
    ...     nesne = re.match("es.a",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    esma
    esra

Gördüğünüz gibi, daha önce "[]" metakarakterini kullanarak yazdığımız
bir düzenli ifadeyi bu kez farklı şekilde yazıyoruz. Unutmayın, bir
düzenli ifade birkaç farklı şekilde yazılabilir. Biz bunlar içinde en
basit ve en anlaşılır olanını seçmeliyiz. Ayrıca yukarıdaki kodu birkaç
farklı şekilde de yazabilirsiniz. Mesela şu yazım da bizim durumumuzda
geçerli bir seçenek olacaktır::

    >>> for i in liste:
    ...     if re.match("es.a",i):
    ...         print(i)

Tabii ki biz, o anda çözmek durumunda olduğumuz soruna en uygun olan
seçeneği tercih etmeliyiz...

Yalnız, unutmamamız gereken şey, bu "." adlı metakarakterin sadece tek
bir karakterin yerini tutuyor olmasıdır. Yani şöyle bir kullanım bize
istediğimiz sonucu vermez::

    >>> liste = ["ahmet","kemal", "kamil", "mehmet"]
    >>> for i in liste:
    ...     if re.match(".met",i):
    ...         print(i)

Burada "." sembolü "ah" ve "meh" hecelerinin yerini tutamaz. "."
sembolünün görevi sadece tek bir karakterin yerini tutmaktır (yeni satır
karakteri hariç). Ama biraz sonra öğreneceğimiz metakarakter yardımıyla
"ah" ve "meh" hecelerinin yerini de tutabileceğiz.

"." sembolünü kullanarak bir örnek daha yapalım. Bir önceki bölümde
verdiğimiz "a" listesini hatırlıyorsunuz::

    >>> a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534']

Önce bu listeye bir öğe daha ekleyelim::

    >>> a.append("1agAY54")

Artık elimizde şöyle bir liste var::

    >>> a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ',
    ... '34534', "1agAY54"]

Şimdi bu listeye şöyle bir düzenli ifade uygulayalım::

    >>> for i in a:
    ...     if re.match(".[0-9a-z]", i):
    ...         print(i)
    ...
    23BH56
    34534
    1agAY54

Burada yaptığımız şey çok basit. Şu özelliklere sahip bir karakter
dizisi arıyoruz:

#. Herhangi bir karakter ile başlayacak. Bu karakter sayı, harf veya
   başka bir karakter olabilir.

#. Ardından bir sayı veya alfabedeki küçük harflerden herhangi birisi
   gelecek.

#. Bu ölçütleri karşıladıktan sonra, aradığımız karakter dizisi
   herhangi bir karakter ile devam edebilir.

Yukarıdaki ölçütlere uyan karakter dizilerimiz: "23BH56", "34534",
"1agAY54"

Yine burada da kendinize göre birtakım değişiklikler yaparak, farklı
yazım şekilleri ve farklı metotlar kullanarak ne olup ne bittiğini daha
iyi kavrayabilirsiniz. Düzenli ifadeleri gereği gibi anlayabilmek için
bol bol uygulama yapmamız gerektiğini unutmamalıyız.

\* (Yıldız)
===========

Bu metakarakter, kendinden önce gelen bir düzenli ifade kalıbını sıfır
veya daha fazla sayıda eşleştirir. Tanımı biraz karışık olsa da örnek
yardımıyla bunu da anlayacağız::

    >>> yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
    >>> for i in yeniliste:
    ...     if re.match("sa*t",i):
    ...         print(i)

Burada "\*" sembolü kendinden önce gelen "a" karakterini sıfır veya daha
fazla sayıda eşleştiriyor. Yani mesela "st" içinde sıfır adet "a"
karakteri var. Dolayısıyla bu karakter yazdığımız düzenli ifadeyle
eşleşiyor. "sat" içinde bir adet "a" karakteri var. Dolayısıyla bu da
eşleşiyor. "saat" ve "saaat" karakter dizilerinde sırasıyla iki ve üç
adet "a" karakteri var. Tabii ki bunlar da yazdığımız düzenli ifadeyle
eşleşiyor. Listemizin en son öğesi olan "falanca"da da ilk hecede bir
adet "a" karakteri var. Ama bu öğedeki sorun, bunun "s" harfiyle
başlamaması. Çünkü biz yazdığımız düzenli ifadede, aradığımız şeyin "s"
harfi ile başlamasını, sıfır veya daha fazla sayıda "a" karakteri ile
devam etmesini ve ardından da "t" harfinin gelmesini istemiştik.
"falanca" öğesi bu koşulları karşılamadığı için süzgecimizin dışında
kaldı.

Burada dikkat edeceğimiz nokta, "\*" metakarakterinin kendinden önce
gelen yalnızca bir karakterle ilgileniyor olması... Yani bizim
örneğimizde "\*" sembolü sadece "a" harfinin sıfır veya daha fazla
sayıda bulunup bulunmamasıyla ilgileniyor. Bu ilgi, en baştaki "s"
harfini kapsamıyor. "s" harfinin de sıfır veya daha fazla sayıda
eşleşmesini istersek düzenli ifademizi "s\*a\*t" veya "[sa]\*t"
biçiminde yazmamız gerekir... Bu iki seçenek içinde "[sa]\*t" şeklindeki
yazımı tercih etmenizi tavsiye ederim. Burada, daha önce öğrendiğimiz "[
]" metakarakteri yardımıyla "sa" harflerini nasıl grupladığımıza dikkat
edin...

Şimdi "." metakarakterini anlatırken istediğimiz sonucu alamadığımız
listeye dönelim. Orada "ahmet" ve "mehmet" öğelerini listeden başarıyla
ayıklayamamıştık. O durumda bizim başarısız olmamıza neden olan kullanım
şöyleydi::

    >>> liste = ["ahmet", "kemal", "kamil", "mehmet"]
    >>> for i in liste:
    ...     if re.match(".met",i):
    ...         print(i)

Ama artık elimizde "\*" gibi bir araç olduğuna göre şimdi istediğimiz
şeyi yapabiliriz. Yapmamız gereken tek şey "." sembolünden sonra "\*"
sembolünü getirmek::

    >>> for i in liste:
    ...     if re.match(".*met", i):
    ...         print(i)

Gördüğünüz gibi "ahmet" ve "mehmet" öğelerini bu kez başarıyla
ayıkladık. Bunu yapmamızı sağlayan şey de "\*" adlı metakarakter oldu...
Burada Python'a şu emri verdik: "Bana kelime başında herhangi bir
karakteri ("." sembolü herhangi bir karakterin yerini tutuyor) sıfır
veya daha fazla sayıda içeren ve sonu da "met" ile biten bütün öğeleri
ver!"

Bir önceki örneğimizde "a" harfinin sıfır veya daha fazla sayıda bulunup
bulunmamasıyla ilgilenmiştik. Bu son örneğimizde ise herhangi bir
harfin/karakterin sıfır veya daha fazla sayıda bulunup bulunmamasıyla
ilgilendik. Dolayısıyla ".\*met" şeklinde yazdığımız düzenli ifade,
"ahmet", "mehmet", "muhammet", "ismet", "kısmet" ve hatta tek başına
"met" gibi bütün öğeleri kapsayacaktır. Kısaca ifade etmek gerekirse,
sonu "met" ile biten her şey ("met" ifadesinin kendisi de dâhil olmak
üzere) kapsama alanımıza girecektir. Bunu günlük hayatta nerede
kullanabileceğinizi hemen anlamış olmalısınız. Mesela bir dizin içindeki
bütün "mp3" dosyalarını bu düzenli ifade yardımıyla listeleyebiliriz::

    >>> import os
    >>> import re
    >>> dizin = os.listdir(os.getcwd())
    >>> for i in dizin:
    ...     if re.match(".*mp3",i):
    ...         print(i)

match() metodunu anlattığımız bölümde bu metodun bir karakter dizisinin
yalnızca başlangıcıyla ilgilendiğini söylemiştik. Mesela o bölümde
verdiğimiz şu örneği hatırlıyorsunuzdur::

    >>> a = "python güçlü bir dildir"
    >>> re.match("güçlü", a)

Bu örnekte Python bize çıktı olarak "None" değerini vermişti. Yani
herhangi bir eşleşme bulamamıştı. Çünkü dediğimiz gibi, match() metodu
bir karakter dizisinin yalnızca en başına bakar. Ama geldiğimiz şu
noktada artık bu kısıtlamayı nasıl kaldıracağınızı biliyorsunuz::

    >>> re.match(".*güçlü", a)

Ama match() metodunu bu şekilde zorlamak yerine performans açısından en
doğru yol bu tür işler için search() metodunu kullanmak olacaktır.

Bunu da geçtiğimize göre artık yeni bir metakarakteri incelemeye
başlayabiliriz.

\+ (Artı)
==========

Bu metakarakter, bir önceki metakarakterimiz olan "\*" ile benzerdir.
Hatırlarsanız, "\*" metakarakteri kendisinden önceki sıfır veya daha
fazla sayıda tekrar eden karakterleri ayıklıyordu. "+" metakarakteri ise
kendisinden önceki bir veya daha fazla sayıda tekrar eden karakterleri
ayıklar. Bildiğiniz gibi, önceki örneklerimizden birinde "ahmet" ve
"mehmet" öğelerini şu şekilde ayıklamıştık::

    >>> for i in liste:
    ...     if re.match(".*met",i):
    ...         print(i)

Burada "ahmet" ve "mehmet" dışında "met" şeklinde bir öğe de bu düzenli
ifadenin kapsamına girecektir. Mesela listemiz şöyle olsa idi::

    >>> liste = ["ahmet", "mehmet", "met", "kezban"]

Yukarıdaki düzenli ifade bu listedeki "met" öğesini de içine alacaktı.
Çünkü "\*" adlı metakarakter sıfır sayıda tekrar eden karakterleri de
ayıklıyor. Ama bizim istediğimiz her zaman bu olmayabilir. Bazen de,
ilgili karakterin en az bir kez tekrar etmesini isteriz. Bu durumda
yukarıdaki düzenli ifadeyi şu şekilde yazmamız gerekir::

    >>> for i in liste:
    ...     if re.match(".+met",i):
    ...         print(i)

Burada şu komutu vermiş olduk: " Bana sonu 'met' ile biten bütün öğeleri
ver! Ama bana 'met' öğesini yalnız başına verme!"

Aynı işlemi search() metodunu kullanarak da yapabileceğimizi
biliyorsunuz::

    >>> for i in liste:
    ...     nesne = re.search(".+met",i)
    ...     if nesne:
    ...         nesne.group()
    ...
    ahmet
    mehmet

Bir de daha önce verdiğimiz şu örneğe bakalım::

    >>> yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
    >>> for i in yeniliste:
    ...     if re.match("sa*t",i):
    ...         print(i)

Burada yazdığımız düzenli ifadenin özelliği nedeniyle "st" de kapsama
alanı içine giriyordu. Çünkü burada "\*" sembolü "a" karakterinin hiç
bulunmadığı durumları da içine alıyor. Ama eğer biz "a" karakteri en az
bir kez geçsin istiyorsak, düzenli ifademizi şu şekilde yazmalıyız::

    >>> for i in yeniliste:
    ...     if re.match("sa+t", i):
    ...         print(i)

Hatırlarsanız önceki derslerimizden birinde köşeli parantezi anlatırken
şöyle bir örnek vermiştik::

    >>> a = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34534"]
    >>> for i in a:
    ...     if re.match("[A-Z][A-Z][0-9]",i):
    ...         print(i)

Burada amacımız sadece "TY76Z" öğesini almaktı. Dikkat ederseniz, öğenin
başındaki "T" ve "Y" harflerini bulmak için iki kez "[A-Z]" yazdık. Ama
artık "+" metakarakterini öğrendiğimize göre aynı işi daha basit bir
şekilde yapabiliriz::

    >>> for i in a:
    ...     if re.match("[A-Z]+[0-9]",i):
    ...         print(i)
    ...
    TY76Z

Burada "[A-Z]" düzenli ifade kalıbını iki kez yazmak yerine bir kez
yazıp yanına da "+" sembolünü koyarak, bu ifade kalıbının bir veya daha
fazla sayıda tekrar etmesini istediğimizi belirttik...

"+" sembolünün ne iş yaptığını da anladığımıza göre, artık yeni bir
metakarakteri incelemeye başlayabiliriz.

? (Soru İşareti)
==================

Hatırlarsanız, "\*" karakteri sıfır ya da daha fazla sayıda eşleşmeleri;
"+" ise bir ya da daha fazla sayıda eşleşmeleri kapsıyordu. İşte şimdi
göreceğimiz "?" sembolü de eşleşme sayısının sıfır veya bir olduğu
durumları kapsıyor. Bunu daha iyi anlayabilmek için önceden verdiğimiz
şu örneğe bakalım::

    >>> yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
    >>> for i in yeniliste:
    ...     if re.match("sa*t",i):
    ...         print(i)
    ...
    st
    sat
    saat
    saaat
    
    >>> for i in yeniliste:
    ...     if re.match("sa+t",i):
    ...         print(i)
    ...
    sat
    saat
    saaat

"\*" ve "+" sembollerinin hangi karakter dizilerini ayıkladığını
görüyoruz. Şimdi de "?" sembolünün ne yaptığına bakalım::

    >>> for i in yeniliste:
    ...     if re.match("sa?t",i):
    ...         print(i)
    ...
    st
    sat

Gördüğünüz gibi, "?" adlı metakarakterimiz, kendisinden önce gelen
karakterin hiç bulunmadığı (yani sıfır sayıda olduğu) ve bir adet
bulunduğu durumları içine alıyor. Bu yüzden de çıktı olarak bize sadece
"st" ve "sat" öğelerini veriyor.

Şimdi bu metakarakteri kullanarak gerçek hayatta karşımıza çıkabilecek
bir örnek verelim. Bu metakarakterin tanımına tekrar bakarsak, "olsa da
olur olmasa da olur" diyebileceğimiz durumlar için bu metakarakterin
rahatlıkla kullanılabileceğini görürüz. Şöyle bir örnek verelim: Diyelim
ki bir metin üzerinde arama yapacaksınız. Aradığınız kelime
"uluslararası"::

    metin = """Uluslararası hukuk, uluslar arası ilişkiler altında bir
    disiplindir. Uluslararası ilişkilerin hukuksal boyutunu bilimsel bir
    disiplin içinde inceler. Devletlerarası hukuk da denir. Ancak uluslar
    arası ilişkilere yeni aktörlerin girişi bu dalı sadece devletlerarası
    olmaktan çıkarmıştır."""

.. note:: Bu metin http://tr.wikipedia.org/wiki/Uluslararas%C4%B1_hukuk
    adresinden alınıp üzerinde ufak değişiklikler yapılmıştır.

Şimdi yapmak istediğimiz şey "uluslararası" kelimesini bulmak. Ama
dikkat ederseniz metin içinde "uluslararası" kelimesi aynı zamanda
"uluslar arası" şeklinde de geçiyor. Bizim bu iki kullanımı da
kapsayacak bir düzenli ifade yazmamız gerekecek...

::

    >>> nesne = re.findall("[Uu]luslar ?arası", metin)
    >>> for i in nesne:
    ...     print(i)

Verdiğimiz düzenli ifade kalıbını dikkatlice inceleyin. Bildiğiniz gibi,
"?" metakarakteri, kendinden önce gelen karakterin (düzenli ifade
kalıbını) sıfır veya bir kez geçtiği durumları arıyor. Burada "?"
sembolünü " " karakterinden, yani "boşluk" karakterinden sonra
kullandık. Dolayısıyla, "boşluk karakterinin sıfır veya bir kez geçtiği
durumları" hedefledik. Bu şekilde hem "uluslar arası" hem de
"uluslararası" kelimesini ayıklamış olduk. Düzenli ifademizde ayrıca
şöyle bir şey daha yazdık: "[Uu]". Bu da gerekiyor. Çünkü metnimiz
içinde "uluslararası" kelimesinin büyük harfle başladığı yerler de
var... Bildiğiniz gibi, "uluslar" ve "Uluslar" kelimeleri asla aynı
değildir. Dolayısıyla hem "u" harfini hem de "U" harfini bulmak için,
daha önce öğrendiğimiz "[]" metakarakterini kullanıyoruz.

{ } (Küme Parantezi)
=====================

{ } adlı metakarakterimiz yardımıyla bir eşleşmeden kaç adet
istediğimizi belirtebiliyoruz. Yine aynı örnek üzerinden gidelim::

    >>> for i in yeniliste:
    ...     if re.match("sa{3}t",i):
    ...         print(i)
    ...
    saaat

Burada "a" karakterinin 3 kez tekrar etmesini istediğimizi belirttik.
Python da bu emrimizi hemen yerine getirdi.

Bu metakarakterin ilginç bir özelliği daha vardır. Küme içinde iki
farklı sayı yazarak, bir karakterin en az ve en çok kaç kez tekrar
etmesini istediğimizi belirtebiliriz. Örneğin::

    >>> for i in yeniliste:
    ...     if re.match("sa{0,3}t",i):
    ...         print(i)
    ...
    st
    sat
    saat
    saaat

sa{0,3}t ifadesiyle, "a" harfinin en az sıfır kez, en çok da üç kez
tekrar etmesini istediğimiz söyledik. Dolayısıyla, "a" harfinin sıfır,
bir, iki ve üç kez tekrar ettiği durumlar ayıklanmış oldu. Bu sayı
çiftlerini değiştirerek daha farklı sonuçlar elde edebilirsiniz. Ayrıca
hangi sayı çiftinin daha önce öğrendiğimiz "?" metakarakteriyle aynı işi
yaptığını bulmaya çalışın...

^ (Şapka)
===========

^ sembolünün iki işlevi var. Birinci işlevi, bir karakter dizisinin en
başındaki veriyi sorgulamaktır. Yani aslında match() metodunun
varsayılan olarak yerine getirdiği işlevi bu metakarakter yardımıyla
açıkça belirterek yerine getirebiliyoruz. Şu örneğe bakalım::

    >>> a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ',    
    ... '34534', '1agAY54']
    >>> for i in a:
    ...     if re.search("[A-Z]+[0-9]",i):
    ...         print(i)
    ...
    23BH56
    TY76Z
    4Y7UZ
    1agAY54

Bir de şuna bakalım::

    >>> for i in a:
    ...     nesne = re.search("[A-Z]+[0-9]",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    BH5
    TY7
    Y7
    AY5

Dikkat ederseniz, şu son verdiğimiz kod oldukça hassas bir çıktı verdi
bize. Çıktıdaki bütün değerler, aynen düzenli ifademizde belirttiğimiz
gibi, yan yana bir veya daha fazla harf içeriyor ve sonra da bir sayı
ile devam ediyor. Bu farklılığın nedeni, ilk kodlarda print(i) ifadesini
kullanmamız. Bu durumun çıktılarımızı nasıl değiştirdiğine dikkat edin.
Bir de şu örneğe bakalım::

    >>> for i in a:
    ...     if re.match("[A-Z]+[0-9]",i):
    ...         print(i)
    ...
    TY76Z

Burada sadece "TY76Z" çıktısını almamızın nedeni, match() metodunun
karakter dizilerinin en başına bakıyor olması. Aynı etkiyi search()
metoduyla da elde etmek için, başlıkta geçen "^" (şapka) sembolünden
yararlanacağız::

    >>> for i in a:
    ...     nesne = re.search("^[A-Z]+[0-9]",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    TY7

Gördüğünüz gibi, "^" (şapka) metakarakteri search() metodunun, karakter
dizilerinin sadece en başına bakmasını sağladı. O yüzden de bize sadece,
"TY7" çıktısını verdi. Hatırlarsanız aynı kodu, şapkasız olarak, şu
şekilde kullanmıştık yukarıda::

    >>> for i in a:
    ...     nesne = re.search("[A-Z]+[0-9]",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    BH5
    TY7
    Y7
    AY5

Gördüğünüz gibi, şapka sembolü olmadığında search() metodu karakter
dizisinin başına bakmakla yetinmiyor, aynı zamanda karakter dizisinin
tamamını tarıyor. Biz yukarıdaki koda bir "^" sembolü ekleyerek,
metodumuzun sadece karakter dizisinin en başına bakmasını istedik. O da
emrimize sadakatle uydu. Burada dikkatimizi çekmesi gereken başka bir
nokta da search() metodundaki çıktının kırpılmış olması. Dikkat
ettiyseniz, search() metodu bize öğenin tamamını vermedi. Öğelerin
yalnızca "[A-Z]+[0-9]" kalıbına uyan kısımlarını kesip attı önümüze.
Çünkü biz ona tersini söylemedik. Eğer öğelerin tamamını istiyorsak bunu
açık açık belirtmemiz gerekir::

    >>> for i in a:
    ...     nesne = re.search("[A-Z]+[0-9].*",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    BH56
    TY76Z
    Y7UZ
    AY54

Veya metodumuzun karakter dizisinin sadece en başına bakmasını istersek::

    >>> for i in a:
    ...     nesne = re.search("^[A-Z]+[0-9].*",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    TY76Z

Bu kodlarda düzenli ifade kalıbının sonuna ".\*" sembolünü eklediğimize
dikkat edin. Böylelikle metodumuzun sonu herhangi bir şekilde biten
öğeleri bize vermesini sağladık...

Başta da söylediğimiz gibi, "^" metakarakterinin, karakter dizilerinin
en başına demir atmak dışında başka bir görevi daha vardır: "Hariç"
anlamına gelmek... Bu görevini sadece "[]" metakarakterinin içinde
kullanıldığı zaman yerine getirir. Bunu bir örnekle görelim. Yukarıdaki
listemiz üzerinde öyle bir süzgeç uygulayalım ki, "1agAY54" öğesi
çıktılarımız arasında görünmesin... Bu öğeyi avlayabilmek için
kullanmamız gereken düzenli ifade şöyle olacaktır: [0-9A-Z][^a-z]+

::

    >>> for i in a:
    ...     nesne = re.match("[0-9A-Z][^a-z]+",i)
    ...     if nesne:
    ...         print(nesne.group())

Burada şu ölçütlere sahip bir öğe arıyoruz:

#. Aradığımız öğe bir sayı veya büyük harf ile başlamalı

#. En baştaki sayı veya büyük harften sonra küçük harf GELMEMELİ (Bu
   ölçütü "^" işareti sağlıyor)

#. Üstelik bu "küçük harf gelmeme durumu" bir veya daha fazla sayıda
   tekrar etmeli... Yani baştaki sayı veya büyük harften sonra kaç tane
   olursa olsun asla küçük harf gelmemeli (Bu ölçütü de "+" işareti
   sağlıyor")

Bu ölçütlere uymayan tek öğe "1agAY54" olacaktır. Dolayısıyla bu öğe
çıktıda görünmeyecek...

Burada, "^" işaretinin nasıl kullanıldığına ve küçük harfleri nasıl
dışarıda bıraktığına dikkat edin. Unutmayalım, bu "^" işaretinin "hariç"
anlamı sadece "[]" metakarakterinin içinde kullanıldığı zaman
geçerlidir.

$ (Dolar)
===========

Bir önceki bölümde "^" işaretinin, karakter dizilerinin en başına demir
attığını söylemiştik. Yani bu sembol arama/eşleştirme işleminin karakter
dizisinin en başından başlamasını sağlıyordu. Bu sembol bir bakıma
karakter dizilerinin nasıl başlayacağını belirliyordu. İşte şimdi
göreceğimiz "dolar işareti" de ($) karakter dizilerinin nasıl biteceğini
belirliyor. Bu soyut açıklamaları somut bir örnekle bağlayalım::

    >>> liste = ["at", "katkı", "fakat", "atkı", "rahat",
    ... "mat", "yat", "sat", "satılık", "katılım"]

Gördüğünüz gibi, elimizde on öğelik bir liste var. Diyelim ki biz bu
listeden, "at" hecesiyle biten kelimeleri ayıklamak istiyoruz::

    >>> for i in liste:
    ...     if re.search("at$",i):
    ...         print(i)
    ...
    at
    fakat
    rahat
    mat
    yat
    sat

Burada "$" metakarakteri sayesinde aradığımız karakter dizisinin nasıl
bitmesi gerektiğini belirleyebildik. Eğer biz "at" ile başlayan bütün
öğeleri ayıklamak isteseydik ne yapmamız gerektiğini biliyorsunuz::

    >>> for i in liste:
    ...     if re.search("^at",i):
    ...         print(i)
    ...
    at
    atkı

Gördüğünüz gibi, "^" işareti bir karakter dizisinin nasıl başlayacağını
belirlerken, "$" işareti aynı karakter dizisinin nasıl biteceğini
belirliyor. Hatta istersek bu metakarakterleri birlikte de
kullanabiliriz::
    
    >>> for i in liste:
    ...     if re.search("^at$",i):
    ...         print(i)
    ...
    at

Sonuç tam da beklediğimiz gibi oldu. Verdiğimiz düzenli ifade kalıbı ile
"at" ile başlayan ve aynı şekilde biten karakter dizilerini ayıkladık.
Bu da bize "at" çıktısını verdi.

\\ (Ters Bölü)
===============

Bu işaret bildiğimiz "kaçış dizisi"dir... Peki burada ne işi var?
Şimdiye kadar öğrendiğimiz konulardan gördüğünüz gibi, Python'daki
düzenli ifadeler açısından özel anlam taşıyan bir takım
semboller/metakarakterler var. Bunlar kendileriyle eşleşmiyorlar. Yani
bir karakter dizisi içinde bu sembolleri arıyorsak eğer, bunların
taşıdıkları özel anlam yüzünden bu sembolleri ayıklamak hemencecik
mümkün olmayacaktır. Yani mesela biz "$" sembolünü arıyor olsak, bunu
Python'a nasıl anlatacağız? Çünkü bu sembolü yazdığımız zaman Python
bunu farklı algılıyor. Lafı dolandırmadan hemen bir örnek verelim...

Diyelim ki elimizde şöyle bir liste var::

    >>> liste = ["10$", "25€", "20$", "10TL", "25£"]

Amacımız bu listedeki dolarlı değerleri ayıklamaksa ne yapacağız? Şunu
deneyelim önce::

    >>> for i in liste:
    ...     if re.match("[0-9]+$",i):
    ...         print(i)

Python "$" işaretinin özel anlamından dolayı, bizim sayıyla biten bir
karakter dizisi aradığımızı zannedecek, dolayısıyla da herhangi bir
çıktı vermeyecektir. Çünkü listemizde sayıyla biten bir karakter dizisi
yok... Peki biz ne yapacağız? İşte bu noktada "\\" metakarakteri devreye
girecek... Hemen bakalım::

    >>> for i in liste:
    ...     if re.match("[0-9]+\$",i):
    ...         print(i)
    ...
    10$
    20$

Gördüğünüz gibi, "\\" sembolünü kullanarak "$" işaretinin özel
anlamından kaçtık... Bu metakarakteri de kısaca anlattığımıza göre yeni
bir metakarakterle yolumuza devam edebiliriz...

\| (Dik Çizgi)
===============

Bu metakarakter, birden fazla düzenli ifade kalıbını birlikte
eşleştirmemizi sağlar. Bu ne demek? Hemen görelim::

    >>> liste = ["at", "katkı", "fakat", "atkı", "rahat",
    ... "mat", "yat", "sat", "satılık", "katılım"]
    >>> for i in liste:
    ...     if re.search("^at|at$",i):
    ...         print(i)
    ...
    at
    fakat
    atkı
    rahat
    mat
    yat
    sat

Gördüğünüz gibi "|" metakarakterini kullanarak başta ve sonda "at"
hecesini içeren kelimeleri ayıkladık. Aynı şekilde, mesela, renkleri
içeren bir listeden belli renkleri de ayıklayabiliriz bu metakarakter
yardımıyla...

::

    >>> for i in renkler:
    ...     if re.search("kırmızı|mavi|sarı", i):
    ...         print(i)

Sırada son metakarakterimiz olan "()" var...

( ) (Parantez)
================

Bu metakarakter yardımıyla düzenli ifade kalıplarını gruplayacağız. Bu
metakarakter bizim bir karakter dizisinin istediğimiz kısımlarını
ayıklamamızda çok büyük kolaylıklar sağlayacak.

Diyelim ki biz http://www.istihza.com/py2/icindekiler_python.html adresindeki
bütün başlıkları ve bu başlıklara ait html dosyalarını bir liste halinde
almak istiyoruz. Bunun için şöyle bir şey yazabiliriz::

    import re
    from urllib.request import urlopen
    
    url = "http://belgeler.istihza.com/py3/index.html"
    f = urlopen(url)
    
    regex = 'href=".+html">.+</a>'
    
    for i in f:
         nesne = re.search(regex, str(i, 'utf-8'))
         if nesne:
                 print(nesne.group())

Burada yaptığımız şey şu:

#. Öncelikle "http://belgeler.istihza.com/py3/index.html" sayfasını urllib
   modülü yardımıyla açtık. Amacımız bu sayfadaki başlıkları ve bu başlıklara ait
   html dosyalarını listelemek

#. Ardından, bütün sayfayı taramak için basit bir for döngüsü kurduk

#. Düzenli ifade kalıbımızı şöyle yazdık: ``'<href=".+html">.+</a>'``
   Çünkü bahsi geçen web sayfasındaki html uzantılı dosyalar bu şekilde
   gösteriliyor. Bu durumu, web tarayıcınızda
   http://belgeler.istihza.com/py3/index.html sayfasını açıp
   sayfa kaynağını görüntüleyerek teyit edebilirsiniz. (Firefox'ta
   CTRL+U'ya basarak sayfa kaynağını görebilirsiniz)

#. Yazdığımız düzenli ifade kalıbı içinde dikkatimizi çekmesi gereken
   bazı noktalar var: Kalıbın "(.+html)" kısmında geçen "+"
   metakarakteri kendisinden önce gelen düzenli ifadenin bir veya daha
   fazla sayıda tekrar eden eşleşmelerini buluyor. Burada "+"
   metakarakterinden önce gelen düzenli ifade, kendisi de bir
   metakarakter olan "." sembolü... Bu sembol bildiğiniz gibi, "herhangi
   bir karakter" anlamına geliyor. Dolayısıyla ".+" ifadesi şu demek
   oluyor: "Bana bir veya daha fazla sayıda tekrar eden bütün
   karakterleri bul!" Dolayısıyla burada "(.+html)" ifadesini birlikte
   düşünürsek, yazdığımız şey şu anlama geliyor: "Bana 'html' ile biten
   bütün karakter dizilerini bul!"

#. "http://belgeler.istihza.com/py3/index.html" adresinin
   kaynağına baktığımız zaman aradığımız bilgilerin hep şu şekilde
   olduğunu görüyoruz: href="kitap_hakkinda.html">Bu Kitap Hakk\xc4\xb1nda</a>
   Dolayısıyla aslında düzenli ifade kalıbımızı yazarken yaptığımız şey,
   düzenli ifademizi kaynakta görünen şablona uydurmak...
   
#. Ayrıca çıktıdaki Türkçe karakterlerin düzgün görünmesi için de bayt
   dizilerini karakter dizisine dönüştürürken 'utf-8' kodlamasını kullandık.

Yukarıda verdiğimiz kodları çalıştırdığımız zaman aldığımız çıktı şu
şekilde oluyor::

    b'href="kitap_hakkinda.html">Bu Kitap Hakk\xc4\xb1nda</a>'
    b'href="python_hakkinda.html">Python Hakk\xc4\xb1nda</a>'
    ...

Hemen hemen amacımıza ulaştık sayılır. Ama gördüğünüz gibi çıktımız
biraz karmaşık. Bunları istediğimiz gibi düzenleyebilsek iyi olurdu,
değil mi? Mesela bu çıktıları şu şekilde düzenleyebilmek hoş olurdu::

    Başlık: ANA SAYFA; Bağlantı: index.html

İşte bu bölümde göreceğimiz "( )" metakarakteri istediğimiz şeyi yapmada
bize yardımcı olacak.

Dilerseniz en başta verdiğimiz kodlara tekrar dönelim::

    import re
    from urllib.request import urlopen
    
    url = "http://belgeler.istihza.com/py3/index.html"
    f = urlopen(url)
    
    regex = 'href=".+html">.+</a>'
    
    for i in f:
         nesne = re.search(regex, str(i, 'utf-8'))
         if nesne:
                 print(nesne.group())

Şimdi bu kodlarda şu değişikliği yapıyoruz::
    
    import re
    from urllib.request import urlopen
    
    url = "http://belgeler.istihza.com/py3/index.html"
    f = urlopen(url)
    
    çıktı = "Başlık: {};\nBağlantı: {}\n"
    regex = 'href="(.+html)">(.+)</a>'
    
    for i in f:
         nesne = re.search(regex, str(i, 'utf-8'))
         if nesne:
                 print(çıktı.format(nesne.group(2), 
                                    nesne.group(1)))

Kodlarda yaptığımız değişikliklere dikkat edin ve anlamaya çalışın. Bazı
noktalar gözünüze karanlık göründüyse hiç endişe etmeyin, çünkü bir
sonraki bölümde bütün karanlık noktaları tek tek açıklayacağız. Burada
en azından, "( )" metakarakterini kullanarak düzenli ifadenin bazı
bölümlerini nasıl grupladığımıza dikkat edin.

Bu arada, elbette www.istihza.com sitesinde herhangi bir değişiklik
olursa yukarıdaki kodların istediğiniz çıktıyı vermeyeceğini
bilmelisiniz. Çünkü yazdığımız düzenli ifade istihza.com sitesinin sayfa
yapısıyla sıkı sıkıya bağlantılıdır.

Eşleşme Nesnelerinin Metotları
*******************************

group() metodu
================

Bu bölümde doğrudan düzenli ifadelerin değil, ama düzenli ifadeler kullanılarak
üretilen eşleşme nesnelerinin bir metodu olan ``group()`` metodundan
bahsedeceğiz. Esasında biz bu metodu önceki bölümlerde de kullanmıştık. Ama
burada bu metoda biraz daha ayrıntılı olarak bakacağız.

Daha önceki bölümlerden hatırlayacağınız gibi, bu metot düzenli ifadeleri
kullanarak eşleştirdiğimiz karakter dizilerini görme imkanı sağlıyordu. Bu
bölümde bu metodu "( )" metakarakteri yardımıyla daha verimli bir şekilde
kullanacağız. İsterseniz ilk olarak şöyle basit bir örnek verelim::

    >>> kardiz = "python bir programlama dilidir"
    >>> nesne = re.search("(python) (bir) (programlama) (dilidir)", kardiz)
    >>> print(nesne.group())
    
    python bir programlama dilidir

Burada düzenli ifade kalıbımızı nasıl grupladığımıza dikkat edin.
``print(nesne.group())`` komutunu verdiğimizde eşleşen karakter dizileri ekrana
döküldü. Şimdi bu grupladığımız bölümlere tek tek erişelim::
    
    >>> nesne.group(0)
    
    'python bir programlama dilidir'

Gördüğünüz gibi, "0" indeksi eşleşen karakter dizisinin tamamını veriyor. Bir de
şuna bakalım::

    >>> nesne.group(1)
    
    'python'

Burada 1 numaralı grubun öğesi olan "python"u aldık. Gerisinin nasıl olacağını
tahmin edebilirsiniz::

    >>> nesne.group(2)
   
    'bir'
    
    >>> nesne.group(3)
    
    'programlama'
    
    >>> nesne.group(4)
    
    'dilidir'

Bu metodun bize ilerde ne büyük kolaylıklar sağlayacağını az çok tahmin
ediyorsunuzdur. İsterseniz kullanabileceğimiz metotları tekrar listeleyelim::

    >>> dir(nesne)

Bu listede ``group()`` dışında bir de ``groups()`` adlı bir metodun olduğunu
görüyoruz. Şimdi bunun ne iş yaptığına bakalım.

groups() metodu
================

Bu metot, bize kullanabileceğimiz bütün grupları bir demet halinde sunar::

    >>> nesne.groups()
    
    ('python', 'bir', 'programlama', 'dilidir')

Şimdi isterseniz bir önceki bölümde yaptığımız örneğe geri dönelim::
        
    import re
    from urllib.request import urlopen
    
    url = "http://belgeler.istihza.com/py3/index.html"
    f = urlopen(url)
    
    çıktı = "Başlık: {};\nBağlantı: {}\n"
    regex = 'href="(.+html)">(.+)</a>'
    
    for i in f:
         nesne = re.search(regex, str(i, 'utf-8'))
         if nesne:
                 print(çıktı.format(nesne.group(2), 
                                    nesne.group(1)))

Bu kodlarda son satırı şöyle değiştirelim::
    
    import re
    from urllib.request import urlopen
    
    url = "http://belgeler.istihza.com/py3/index.html"
    f = urlopen(url)
    
    çıktı = "Başlık: {};\nBağlantı: {}\n"
    regex = 'href="(.+html)">(.+)</a>'
    
    for i in f:
         nesne = re.search(regex, str(i, 'utf-8'))
         if nesne:
                 print(nesne.groups())

Gördüğünüz gibi şuna benzer çıktılar elde ediyoruz::

    ('kitap_hakkinda.html', 'Bu Kitap Hakkında')
    ('python_hakkinda.html', 'Python Hakkında')
    ('temel_komut_satiri_bilgisi.html', 'Temel Komut Satırı Bilgisi')
    ('path.html', 'YOL (<em>PATH</em>) Kavramı')
    ('kurulum.html', 'Python Nasıl Kurulur?')
    ...
    ...
    ...

Demek ki (nesne.groups()) komutu bize "( )" metakarakteri ile daha önceden
gruplamış olduğumuz öğeleri bir demet olarak veriyor. Biz de bu demetin
öğelerine daha sonradan rahatlıkla erişebiliyoruz...

Böylece eşleştirme nesnelerinin en sık kullanılan iki metodunu görmüş olduk.
Bunları daha sonraki örneklerimizde de bol bol kullanacağız. O yüzden şimdilik
bu konuya ara verelim.

Özel Diziler
**************

Düzenli ifadeler içinde metakarakterler dışında, özel anlamlar taşıyan
bazı başka ifadeler de vardır. Bu bölümde bu özel dizileri
inceleyeceğiz: Boşluk karakterinin yerini tutan özel dizi: \\s

Bu sembol, bir karakter dizisi içinde geçen boşlukları yakalamak için
kullanılır. Örneğin::

    >>> a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
    >>> for i in a:
    ...     nesne = re.search("[0-9]\\s[A-Za-z]+",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    5 Ocak
    4 Ekim

Yukarıdaki örnekte, bir sayı ile başlayan, ardından bir adet boşluk karakteri
içeren, sonra da bir büyük veya küçük harfle devam eden karakter dizilerini
ayıkladık. Burada boşluk karakterini "\\s" simgesi ile gösterdiğimize dikkat
edin.

Ondalık Sayıların Yerini Tutan Özel Dizi: \\d
==============================================

Bu sembol, bir karakter dizisi içinde geçen ondalık sayıları eşleştirmek için
kullanılır. Buraya kadar olan örneklerde bu işlevi yerine getirmek için "[0-9]"
ifadesinden yararlanıyorduk. Şimdi artık aynı işlevi daha kısa yoldan, "\\d"
dizisi ile yerine getirebiliriz. İsterseniz yine yukarıdaki örnekten gidelim::

    >>> a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
    >>> for i in a:
    ...     nesne = re.search("\d\s[A-Za-z]+",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    5 Ocak
    4 Ekim

Burada, "[0-9]" yerine "\\d" yerleştirerek daha kısa yoldan sonuca vardık.

Alfanümerik Karakterlerin Yerini Tutan Özel Dizi: \\w
=========================================================

Bu sembol, bir karakter dizisi içinde geçen alfanümerik karakterleri ve buna ek
olarak "_" karakterini bulmak için kullanılır. Şu örneğe bakalım::

    >>> a = "abc123_$%+"
    >>> print(re.search("\w*", a).group())
    
    abc123_

"\\w" özel dizisinin hangi karakterleri eşlediğine dikkat edin. Bu özel dizi şu
ifadeyle aynı anlama gelir::

    [A-Za-z0-9_]

Düzenli ifadeler içindeki özel diziler genel olarak bunlardan ibarettir. Ama bir
de bunların büyük harfli versiyonları vardır ki, önemli oldukları için onları da
inceleyeceğiz.

Gördüğünüz gibi;

#. "\\s" özel dizisi boşluk karakterlerini avlıyor

#. "\\d" özel dizisi ondalık sayıları avlıyor

#. "\\w" özel dizisi alfanümerik karakterleri ve "_" karakterini
   avlıyor

Dedik ki, bir de bunların büyük harfli versiyonları vardır. İşte bu büyük harfli
versiyonlar da yukarıdaki dizilerin yaptığı işin tam tersini yapar. Yani:

#. "\\S" özel dizisi boşluk olmayan karakterleri avlar

#. "\\D" özel dizisi ondalık sayı olmayan karakterleri avlar. Yani
   "[^0-9]" ile eşdeğerdir.

#. "\\W" özel dizisi alfanümerik olmayan karakterleri ve "_" olmayan
   karakterleri avlar. Yani `[^A-Za-z0-9_]` ile eşdeğerdir.

"\\D" ve "\\W" dizilerinin yeterince anlaşılır olduğunu zannediyorum. Burada
sanırım sadece "S" dizisi bir örnekle somutlaştırılmayı hakediyor::

    >>> a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
    >>> for i in a:
    ...     nesne = re.search("\d+\S\w+",i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    27Mart

Burada "\\S" özel dizisinin listede belirtilen konumda boşluk içermeyen öğeyi
nasıl bulduğuna dikkat edin.

Şimdi bu özel diziler için genel bir örnek verip konuyu kapatalım...

Bilgisayarımızda şu bilgileri içeren "adres.txt" adlı bir dosya olduğunu
varsayıyoruz::

    esra : istinye 05331233445 esma : levent 05322134344 sevgi : dudullu
    05354445434 kemal : sanayi 05425455555 osman : tahtakale 02124334444
    metin : taksim 02124344332 kezban : caddebostan 02163222122

Amacımız bu dosyada yer alan isim ve telefon numaralarını "isim > telefon
numarası" şeklinde almak::
    
    import re
    dosya = open("adres.txt")
    for i in dosya.readlines():
        nesne = re.search("(\w+)\s+:\s(\w+)\s+(\d+)",i)
        if nesne:
            print("{} > {}".format(nesne.group(1), nesne.group(3)))

Burada formülümüz şu şekilde: "Bir veya daha fazla karakter" + "bir veya daha
fazla boşluk" + "':' işareti" + "bir adet boşluk" + "bir veya daha fazla sayı"

İsterseniz bu bölümü çok basit bir soruyla kapatalım. Sorumuz şu:

Elimizde şu adresteki yığın var:
`http://www.istihza.com/denemeler/yigin.txt <http://www.istihza.com/denemeler/yigin.txt>`_

Yapmanız gereken, bu yığın içindeki gizli mesajı düzenli ifadeleri
kullanarak bulmak... 

Düzenli İfadelerin Derlenmesi
*****************************

compile() metodu
=================

En başta da söylediğimiz gibi, düzenli ifadeler karakter dizilerine göre
biraz daha yavaş çalışırlar. Ancak düzenli ifadelerin işleyişini
hızlandırmanın da bazı yolları vardır. Bu yollardan biri de compile()
metodunu kullanmaktır. "compile" kelimesi İngilizcede "derlemek"
anlamına gelir. İşte biz de bu ``compile()`` metodu yardımıyla düzenli ifade
kalıplarımızı kullanmadan önce derleyerek daha hızlı çalışmalarını
sağlayacağız. Küçük boyutlu projelerde ``compile()`` metodu pek hissedilir
bir fark yaratmasa da özellikle büyük çaplı programlarda bu metodu
kullanmak oldukça faydalı olacaktır.

Basit bir örnekle başlayalım::

    >>> liste = ["Python2.7", "Python3.2", "Python3.3",    
    ... "Python3.4", "Java"]
    >>> derli = re.compile("[A-Za-z]+[0-9]\.[0-9]")
    >>> for i in liste:
    ...     nesne = derli.search(i)
    ...     if nesne:
    ...         print(nesne.group())
    ...
    Python2.7
    Python3.2
    Python3.3
    Python3.4

Burada öncelikle düzenli ifade kalıbımızı derledik. Derleme işlemini nasıl
yaptığımıza dikkat edin. Derlenecek düzenli ifade kalıbını ``compile()``
metodunda parantez içinde belirtiyoruz. Daha sonra ``search()`` metodunu
kullanırken ise, re.search() demek yerine, ``derli.search()`` şeklinde bir ifade
kullanıyoruz. Ayrıca dikkat ederseniz ``derli.search()`` kullanımında parantez
içinde sadece eşleşecek karakter dizisini kullandık (i). Eğer derleme işlemi
yapmamış olsaydık, hem bu karakter dizisini, hem de düzenli ifade kalıbını yan
yana kullanmamız gerekecektir. Ama düzenli ifade kalıbımızı yukarıda derleme
işlemi esnasında belirttiğimiz için, bu kalıbı ikinci kez yazmamıza gerek
kalmadı. Ayrıca burada kullandığımız düzenli ifade kalıbına da dikkat edin.
Nasıl bir şablon oturttuğumuzu anlamaya çalışın. Gördüğünüz gibi, liste
öğelerinde bulunan "." işaretini eşleştirmek için düzenli ifade kalıbı içinde
"\\." ifadesini kullandık. Çünkü bildiğiniz gibi, tek başına "." işaretinin
Python açısından özel bir anlamı var. Dolayısıyla bu özel anlamdan kaçmak için
"\\" işaretini de kullanmamız gerekiyor.

compile() ile Derleme Seçenekleri
==================================

Bir önceki bölümde ``compile(``) metodunun ne olduğunu, ne işe yaradığını ve
nasıl kullanıldığını görmüştük. Bu bölümde ise "compile" (derleme) işlemi
sırasında kullanılabilecek seçenekleri anlatacağız.

re.IGNORECASE veya re.I
-------------------------

Bildiğiniz gibi, Python'da büyük-küçük harfler önemlidir. Yani eğer "python"
kelimesini arıyorsanız, alacağınız çıktılar arasında "Python" olmayacaktır.
Çünkü "python" ve "Python" birbirlerinden farklı iki karakter dizisidir. İşte
`re.IGNORECASE` veya kısaca `re.I` adlı derleme seçenekleri bize büyük-küçük
harfe dikkat etmeden arama yapma imkanı sağlar. Hemen bir örnek verelim::
    
    import re
    
    metin = """Programlama dili, programcının bir bilgisayara ne yapmasını
    istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
    dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
    verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
    yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
    programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
    C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
    dilleridir."""
    
    derli = re.compile("programlama",re.IGNORECASE)
    print(derli.findall(metin))

Bu programı çalıştırdığımızda şu çıktıyı alıyoruz::

    ['Programlama', 'Programlama', 'programlama', 'programlama']

.. note:: Bu metin http://tr.wikipedia.org/wiki/Programlama_dili adresinden
    alınmıştır.

Gördüğünüz gibi, metinde geçen hem "programlama" kelimesini hem de "Programlama"
kelimesini ayıklayabildik. Bunu yapmamızı sağlayan şey de `re.IGNORECASE` adlı
derleme seçeneği oldu. Eğer bu seçeneği kullanmasaydık, çıktıda yalnızca
"programlama" kelimesini görürdük. Çünkü aradığımız şey aslında "programlama"
kelimesi idi. Biz istersek `re.IGNORECASE` yerine kısaca `re.I` ifadesini de
kullanabiliriz. Aynı anlama gelecektir...

re.DOTALL veya re.S
---------------------

Bildiğiniz gibi, metakarakterler arasında yer alan "." sembolü herhangi
bir karakterin yerini tutuyordu. Bu metakarakter bütün karakterlerin
yerini tutmak üzere kullanılabilir. Hatırlarsanız, "." metakarakterini
anlatırken, bu metakarakterin, yeni satır karakterinin yerini
tutmayacağını söylemiştik. Bunu bir örnek yardımıyla görelim. Diyelim ki
elimizde şöyle bir karakter dizisi var::

    >>> a = "Ben Python,\nMonty Python"

Bu karakter dizisi içinde "Python" kelimesini temel alarak bir arama
yapmak istiyorsak eğer, kullanacağımız şu kod istediğimiz şeyi yeterince
yerine getiremeyecektir::

    >>> print(re.search("Python.*", a).group())

Bu kod şu çıktıyı verecektir::

    Python,

Bunun sebebi, "." metakarakterinin `"\\n"` (yeni satır) kaçış dizisini dikkate
almamasıdır. Bu yüzden bu kaçış dizisinin ötesine geçip orada arama yapmıyor.
Ama şimdi biz ona bu yeteneği de kazandıracağız::
    
    >>> derle = re.compile("Python.*", re.DOTALL)
    >>> nesne = derle.search(a)
    >>> if nesne:
    ...     print(nesne.group())

`re.DOTALL` seçeneğini sadece re.S şeklinde de kısaltabilirsiniz...

Düzenli İfadelerle Metin/Karakter Dizisi Değiştirme İşlemleri
**************************************************************

sub() metodu
=================

Şimdiye kadar hep düzenli ifadeler yoluyla bir karakter dizisini nasıl
eşleştireceğimizi inceledik. Ama tabii ki düzenli ifadeler yalnızca bir karakter
dizisi "bulmak"la ilgili değildir. Bu araç aynı zamanda bir karakter dizisini
"değiştirmeyi" de kapsar. Bu iş için temel olarak iki metot kullanılır.
Bunlardan ilki ``sub()`` metodudur. Bu bölümde ``sub()`` metodunu inceleyeceğiz.

En basit şekliyle ``sub()`` metodunu şu şekilde kullanabiliriz::

    >>> a = "Kırmızı başlıklı kız, kırmızı elma dolu sepetiyle \
    ... anneannesinin evine gidiyormuş!"
    >>> derle = re.compile("kırmızı", re.IGNORECASE)
    >>> print(derle.sub("yeşil", a))

Burada karakter dizimiz içinde geçen bütün "kırmızı" kelimelerini "yeşil"
kelimesiyle değiştirdik. Bunu yaparken de re.IGNORECASE adlı derleme
seçeneğinden yararlandık.

Elbette ``sub()`` metoduyla daha karmaşık işlemler yapılabilir. Bu noktada şöyle
bir hatırlatma yapalım. Bu ``sub()`` metodu karakter dizilerinin ``replace()``
metoduna çok benzer. Ama tabii ki ``sub()`` metodu hem kendi başına
``replace()`` metodundan çok daha güçlüdür, hem de beraber kullanılabilecek
derleme seçenekleri sayesinde ``replace()`` metodundan çok daha esnektir. Ama
tabii ki, eğer yapmak istediğiniz iş ``replace()`` metoduyla halledilebiliyorsa
en doğru yol, ``replace()`` metodunu kullanmaktır...

Şimdi bu ``sub()`` metodunu kullanarak biraz daha karmaşık bir işlem yapacağız.
Aşağıdaki metne bakalım::

    metin = """Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
    gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı çileği ise ismini
    verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
    oradan da Ereğli'ye getirilen kralların meyvesi çilek, burada geçirdiği değişim
    sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
    bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı çileği
    unvanını hak eder. Bu nazik ve aromalı çilekten yapılan reçel de likör de bir
    başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Çileği Kültür
    Festivali'nde 36 üretici arasında yetiştirdiği çileklerle birinci olan Kocaali
    Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
    çileklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
    bahçemize giremez. Koca ayaklarıyla ezerler çileklerimizi" Çileği toplamanın zor
    olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana çilek bahçesinde
    çalışıyor. Her sabah 04.00'te kalkan Özhan, çileklerini özenle suluyor. Kasım
    başında ektiği çilek fideleri haziran başında meyve veriyor."""

.. note:: Bu metin http://www.radikal.com.tr/haber.php?haberno=40130
    adresinden alınmıştır.

Gelin bu metin içinde geçen "çilek" kelimelerini "erik" kelimesi ile
değiştirelim. Ama bunu yaparken, metin içinde "çilek" kelimesinin
"Çilek" şeklinde de geçtiğine dikkat edelim. Ayrıca Türkçe kuralları
gereği bu "çilek" kelimesinin bazı yerlerde ünsüz yumuşamasına uğrayarak
"çileğ-" şekline dönüştüğünü de unutmayalım.

Bu metin içinde geçen "çilek" kelimelerini "erik"le değiştirmek için
birkaç yol kullanabilirsiniz. Birinci yolda, her değişiklik için ayrı
bir düzenli ifade oluşturulabilir. Ancak bu yolun dezavantajı, metnin de
birkaç kez kopyalanmasını gerektirmesidir. Çünkü ilk düzenli ifade
oluşturulup buna göre metinde bir değişiklik yapıldıktan sonra, ilk
değişiklikleri içeren metnin, farklı bir metin olarak kopyalanması
gerekir (metin2 gibi...). Ardından ikinci değişiklik yapılacağı zaman,
bu değişikliğin metin2 üzerinden yapılması gerekir. Aynı şekilde bu
metin de, mesela, metin3 şeklinde tekrar kopyalanmalıdır. Bundan sonraki
yeni bir değişiklik de bu metin3 üzerinden yapılacaktır... Bu durum bu
şekilde uzar gider... Metni tekrar tekrar kopyalamak yerine, düzenli
ifadeleri kullanarak şöyle bir çözüm de üretebiliriz::
    
    import re
    
    derle = re.compile("çile[kğ]", re.IGNORECASE)
    
    def degistir(nesne):
        a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
        b = nesne.group().split()
        for i in b:
            return a[i]
    
    print(derle.sub(degistir, metin))

Gördüğünüz gibi, ``sub()`` metodu, argüman olarak bir fonksiyon da alabiliyor.
Yukarıdaki kodlar biraz karışık görünmüş olabilir. Tek tek açıklayalım...

Öncelikle şu satıra bakalım::

    derle = re.compile("çile[kğ]", re.IGNORECASE)

Burada amacımız, metin içinde geçen "çilek" ve "çileğ" kelimelerini
bulmak. Neden "çileğ"? Çünkü "çilek" kelimesi bir sesli harften önce
geldiğinde sonundaki "k" harfi "ğ"ye dönüşüyor. Bu seçenekli yapıyı,
daha önceki bölümlerde gördüğümüz "[ ]" adlı metakarakter yardımıyla
oluşturduk. Düzenli ifade kalıbımızın hem büyük harfleri hem de küçük
harfleri aynı anda bulması için re.IGNORECASE seçeneğinden yararlandık.

Şimdi de şu satırlara bakalım::

    def degistir(nesne):
        a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
        b = nesne.group().split()
        for i in b:
            return a[i]

Burada, daha sonra ``sub()`` metodu içinde kullanacağımız fonksiyonu yazıyoruz.
Fonksiyonu, ``def degistir(nesne)`` şeklinde tanımladık. Burada "nesne" adlı bir
argüman kullanmamızın nedeni, fonksiyon içinde ``group()`` metodunu kullanacak
olmamız. Bu metodu fonksiyon içinde "nesne" adlı argümana bağlayacağız. Bu
fonksiyon, daha sonra yazacağımız ``sub()`` metodu tarafından çağrıldığında,
yaptığımız arama işlemi sonucunda ortaya çıkan "eşleşme nesnesi" fonksiyona
atanacaktır (eşleşme nesnesinin ne demek olduğunu ilk bölümlerden
hatırlıyorsunuz). İşte "nesne" adlı bir argüman kullanmamızın nedeni de, eşleşme
nesnelerinin bir metodu olan ``group()`` metodunu fonksiyon içinde
kullanabilmek...

Bir sonraki satırda bir adet sözlük görüyoruz::

    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}

Bu sözlüğü oluşturmamızın nedeni, metin içinde geçen bütün "çilek" kelimelerini
tek bir "erik" kelimesiyle değiştiremeyecek olmamız... Çünkü "çilek" kelimesi
metin içinde pek çok farklı biçimde geçiyor. Başta da dediğimiz gibi, yukarıdaki
yol yerine metni birkaç kez kopyalayarak ve her defasında bir değişiklik yaparak
da sorunu çözebilirsiniz. (Mesela önce "çilek" kelimelerini bulup bunları "erik"
ile değiştirirsiniz. Daha sonra "çileğ" kelimelerini arayıp bunları "eriğ" ile
değiştirirsiniz, vb...) Ama metni tekrar tekrar oluşturmak pek performanslı bir
yöntem olmayacaktır. Bizim şimdi kullandığımız yöntem metin kopyalama
zorunluluğunu ortadan kaldırıyor. Bu sözlük içinde "çilek" kelimesinin alacağı
şekilleri sözlük içinde birer anahtar olarak, "erik" kelimesinin alacağı
şekilleri ise birer "değer" olarak belirliyoruz.

Sonraki satırda iki metot birden var::

    b = nesne.group().split()

Burada, fonksiyonumuzun argümanı olarak vazife gören eşleşme nesnesine ait
metotlardan biri olan ``group(``) metodunu kullanıyoruz. Böylece ``derle =
re.compile("çile[kğ]", re.IGNORECASE)`` satırı yardımıyla metin içinde
bulduğumuz bütün "çilek" ve çeşnilerini alıyoruz. Karakter dizilerinin
``split(``) metodunu kullanmamızın nedeni ise ``group()`` metodunun verdiği
çıktıyı liste haline getirip daha kolay manipüle etmek. Burada ``for i in b:
print(i)`` komutunu verirseniz ``group()`` metodu yardımıyla ne bulduğumuzu
görebilirsiniz::
    
    çileğ
    çilek
    çileğ
    çilek
    Çileğ
    çilek
    çilek
    çilek
    Çileğ
    çilek
    çilek
    çilek

Bu çıktıyı gördükten sonra, kodlarda yapmaya çalıştığımız şey daha anlamlı
görünmeye başlamış olmalı... Şimdi sonraki satıra geçiyoruz::

    for i in b:
        return a[i]

Burada, ``group()`` metodu yardımıyla bulduğumuz eşleşmeler üzerinde bir for
döngüsü oluşturduk. Ardından da ``return a[i]`` komutunu vererek "a" adlı sözlük
içinde yer alan öğeleri yazdırıyoruz. Bu arada, buradaki "i"nin yukarıda
verdiğimiz ``group()`` çıktılarını temsil ettiğine dikkat edin. ``a[i]`` gibi
bir komut verdiğimizde aslında sırasıyla şu komutları vermiş oluyoruz::

    a["çilek"]
    a["çileğ"]
    a["çilek"]
    a["Çileğ"]
    a["çilek"]
    a["çilek"]
    a["çilek"]
    a["Çileğ"]
    a["çilek"]
    a["çilek"]

Bu komutların çıktıları sırasıyla "erik", "eriğ", "erik", "Eriğ", "erik",
"erik", "erik", "Eriğ", "erik", "erik" olacaktır. İşte bu return satırı bir
sonraki kod olan ``print(derle.sub(degistir,metin))`` ifadesinde etkinlik
kazanacak. Bu son satırımız sözlük öğelerini tek tek metne uygulayacak ve mesela
``a["çilek"]`` komutu sayesinde metin içinde "çilek" gördüğü yerde "erik"
kelimesini yapıştıracak ve böylece bize istediğimiz şekilde değiştirilmiş bir
metin verecektir...

Bu kodların biraz karışık gibi göründüğünü biliyorum, ama aslında çok basit bir
mantığı var: ``group()`` metodu ile metin içinde aradığımız kelimeleri
ayıklıyor. Ardından da "a" sözlüğü içinde bunları anahtar olarak kullanarak
"çilek" ve çeşitleri yerine "erik" ve çeşitlerini koyuyor...

Yukarıda verdiğimiz düzenli ifadeyi böyle ufak bir metinde kullanmak çok
anlamlı olmayabilir. Ama çok büyük metinler üzerinde çok çeşitli ve
karmaşık değişiklikler yapmak istediğinizde bu kodların işinize
yarayabileceğini göreceksiniz.

subn() metodu
=================

Bu metodu çok kısa bir şekilde anlatıp geçeceğiz. Çünkü bu metot ``sub()``
metoduyla neredeyse tamamen aynıdır. Tek farkı, ``subn()`` metodunun bir metin
içinde yapılan değişiklik sayısını da göstermesidir. Yani bu metodu kullanarak,
kullanıcılarınıza "toplam şu kadar sayıda değişiklik yapılmıştır" şeklinde bir
bilgi verebilirsiniz. Bu metot çıktı olarak iki öğeli bir demet verir. Birinci
öğe değiştirilen metin, ikinci öğe ise yapılan değişiklik sayısıdır. Yani
kullanıcıya değişiklik sayısını göstermek için yapmanız gereken şey, bu demetin
ikinci öğesini almaktır. Mesela ``sub()`` metodunu anlatırken verdiğimiz
kodların son satırını şöyle değiştirebilirsiniz::

    ab = derle.subn(degistir, metin)
    print("Toplam {} değişiklik yapılmıştır.".format(ab[1]))
    
Yani::
    
    import re
    
    metin = """Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
    gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı çileği ise ismini
    verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
    oradan da Ereğli'ye getirilen kralların meyvesi çilek, burada geçirdiği değişim
    sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
    bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı çileği
    unvanını hak eder. Bu nazik ve aromalı çilekten yapılan reçel de likör de bir
    başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Çileği Kültür
    Festivali'nde 36 üretici arasında yetiştirdiği çileklerle birinci olan Kocaali
    Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
    çileklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
    bahçemize giremez. Koca ayaklarıyla ezerler çileklerimizi" Çileği toplamanın zor
    olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana çilek bahçesinde
    çalışıyor. Her sabah 04.00'te kalkan Özhan, çileklerini özenle suluyor. Kasım
    başında ektiği çilek fideleri haziran başında meyve veriyor."""
    
    derle = re.compile("çile[kğ]", re.IGNORECASE)
    
    def degistir(nesne):
        a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
        b = nesne.group().split()
        for i in b:
            return a[i]
    
    ab = derle.subn(degistir, metin)
    print("Toplam {} değişiklik yapılmıştır.".format(ab[1]))

Sonuç
*****

Böylelikle düzenli ifadeler konusunu bitirmiş olduk. Buradaki amacımız, size
düzenli ifadeler konusunda genel bir bakış sunabilmekti. Bu yazıları okuduktan
sonra kafanızda düzenli ifadelerle ilgili kabataslak da olsa bir resim oluştuysa
bu yazılar amacına ulaşmış demektir. Elbette düzenli ifadeler burada
anlattıklarımızdan ibaret değildir. Bu konunun üzerine eğildiğinizde aslında
düzenli ifadelerin dipsiz bir kuyu gibi olduğunu göreceksiniz. Esasında en başta
da dediğimiz gibi, düzenli ifadeler apayrı bir dil gibidir. Doğrusu şu ki,
düzenli ifadeler başlı başına bağımsız bir sistemdir. Hemen hemen bütün
programlama dilleri öyle ya da böyle düzenli ifadeleri destekler. Python’da
düzenli ifadeleri bünyesine adapte etmiş dillerden biridir. Bizim düzenli
ifadeler konusundaki yaklaşımımız, her zaman bunları "gerektiğinde" kullanmak
olmalıdır. Dediğimiz gibi, eğer yapmak istediğiniz bir işlemi karakter
dizilerinin metotları yardımıyla yapabiliyorsanız düzenli ifadelere girişmemek
en iyisidir. Çünkü karakter dizisi metotları hem daha hızlıdır hem de anlaması
daha kolaydır.