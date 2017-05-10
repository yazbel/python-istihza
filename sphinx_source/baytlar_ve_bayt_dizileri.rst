.. meta::
   :description: Python 3.x'te baytlar adlı veri tipi
   :keywords: python, bayt, baytlar, bytes, karakter, karakter dizisi, encode

.. highlight:: py3

*********************************************
Baytlar (Bytes) ve Bayt Dizileri (Bytearrays)
*********************************************

Bu bölüme gelinceye kadar veri tipi olarak karakter dizilerinden, listelerden ve
dosyalardan söz etmiştik. Bu bölümde ise Python programlama dilindeki iki veri
tipinden daha söz edeceğiz. Birbirleriyle doğrudan bağlantılı oldukları için
bu bölümde birlikte ele alacağımız bu veri tiplerinin adı 'baytlar'(*bytes*) ve
'bayt dizileri' (*bytearrays*).

Bu bölümde yalnızca 'baytlar' ve 'bayt dizileri' adlı veri tiplerinden söz
etmeyeceğiz. Bu iki yeni veri tipini bilgi dağarcığımıza eklemenin yanısıra,
önceki bölümlerde öğrendiğimiz konuları zihnimizde pekiştirmeye ve
sağlamlaştırmaya da devam edeceğiz.

Giriş
******

Bilgisayar teknolojisi ve bilimi açısından 'karakter' tamamen soyut bir
kavramdır. Son birkaç bölümdür üstüne basa basa tekrar ettiğimiz gibi, karakter
dediğimiz şey, bilgisayarların anlayabildiği tek kavram olan sayılara biz
insanların atadığı birtakım işaretlerden ibarettir. Dolayısıyla bilgisayarlar
açısından karakterler değil, ikili sayma düzenindeki birtakım sayılar, yani
bitler ve baytlar vardır. 

Teknik olarak 1 bit, ikili sayma sistemindeki her bir basamağa verilen isimdir.
Zaten 'bit' kelimesinin de İngilizcede 'ikili basamak' anlamına gelen '*binary
digit* ifadesinin kısaltması olduğunu geçen bölümde öğrenmiştiniz. 

Örneğin ikili sayma sistemindeki `0`, bir bitlik bir sayı iken, `100` üç bitlik
bir sayıdır. Bu bit'lerin `8` tanesi bir araya gelince 'bayt' denen birimi
oluşturur. Yani bayt, 8 adet bit'ten oluşan bir birimdir. Nasıl bir düzinede 10,
bir destede de 12 öğe olmasını biz insanlar tercih etmiş ve belirlemişsek, bir
bayt'ta da 8 bit olmasını yine biz insanlar tercih etmiş ve belirlemişizdir.

Önceki derslerimizde de öğrendiğimiz gibi, 8 adet bit, yani 1 bayt,
Genişletilmiş ASCII sisteminde bir adet karakteri temsil etmek için
kullanılabilecek en büyük birim olarak tasarlanmıştır. Yani Genişletilmiş ASCII
tablolarının en sonundaki 255 numaralı karakteri temsil edebilmek için 8 adet
bit, yani toplam 1 bayt kullanmamız gerekir. Standart ASCII sistemi ise 7 bitlik
bir sistem olduğu için, bir adet karakteri temsil etmek için kullanılabilecek en
büyük birimin 7 bit olduğunu biliyorsunuz. Dolayısıyla ASCII sistemindeki son
karaktere karşılık gelen 127. sayıyı temsil edebilmek için toplam 7 bit
yeterlidir.

Farklı bir sistem olan UTF-8 ise birden fazla bayt kullanarak çok sayıda
karakteri temsil etmeye imkan tanır. UTF-8 ile, duruma göre 1, 2, 3 veya 4 bayt
kullanarak, UNICODE sistemi içinde tanımlanmış bütün karakterleri temsil
edebilirsiniz. UTF-8, değişken boyutlu bir kodlama sistemi olması sayesinde, bir
karakteri temsil edebilmek için kaç bayt gerekiyorsa, o karakteri temsil etmek
için o kadar bayt kullanır. Ama mesela UTF-32 adlı kod çözücü hangi karakter
olursa olsun hepsini 4 bayt (32 bit) ile temsil eder. Bu durumda aslında tek
baytla temsil edilebilecek 'a', 'b', 'c' gibi karakterler de boşu boşuna 4 bayt
yer kaplamış olur. Zaten UTF-8'in bu kadar yaygın ve gözde olmasının nedeni de
hem çok sayıda karakteri kodlayabilmesi, hem de bu işi yaparken tasarruflu
olmayı başarabilmesidir.

Python programlama dilinde karakter dizileri UNICODE kod konumları şeklinde
temsil edilir. Dolayısıyla `str` adı verilen veri tipi esasında karakter
dizilerini birtakım UNICODE kod konumları şeklinde gösteren soyut bir yapıdır.
Yani biz Python'da karakter dizileri üzerinde işlem yaparken aslında baytlarla
değil, UNICODE kod konumları ile muhatap oluyoruz. Ancak UNICODE kod konumları
da tamamen soyut kavramlardır. Bunları bilgisayarın belleğinde bu şekilde temsil
edemezsiniz ya da bu kod konumlarını herhangi bir ağ üzerinden başka
bilgisayarlara iletemezsiniz. Bu kod konumlarını anlamlı bir şekilde
kullanabilmek için öncelikle bunları bilgisayarların anlayabileceği bir biçim
olan baytlara çevirmeniz gerekir. Çünkü dediğimiz gibi bilgisayarlar yalnızca
bitler ve baytlardan anlar. İşte kod çözücülerin görevi de zaten bu kod
konumlarını baytlara çevirmektir.

Esasında programcılık maceranız boyunca genellikle metin ihtiyaçlarınızı UNICODE
kod konumları üzerinden halledeceksiniz. Python sistemdeki öntanımlı kod
çözücüyü kullanarak bu kod konumlarını alttan alta bayta çevirip bellekte
saklayacaktır. Ama eğer yazdığınız programlarda herhangi bir şekilde doğrudan
baytlarla muhatap olmanız gerekirse `str` veri tipini değil, `bytes` adlı başka
bir veri tipini kullanacaksınız. Örneğin ikili (*binary*) dosyalar üzerinde
çeşitli çalışmalar yapacaksanız ve bu ikili dosyalara birtakım veriler
girecekseniz, gireceğiniz bu veriler `bytes` tipinde olacaktır.

Bütün bu sebeplerden ötürü, `str` ve `bytes` veri tipleri arasındaki farkı
anlamak, yazdığınız programların kararlılığı ve sağlamlığı açısından büyük önem
taşır. O anda elinizde olan verinin hangi tipte olduğunu bilmezseniz, bu
verinin, programınızın çalışması esnasında size ne tür tuzaklar kurabileceğini
de kestiremezsiniz. Örneğin bütün karakterlerin 1 bayt olduğunu ve bunların da
yalnızca 0 ile 127 arası sayılarla temsil edilebileceğini zanneden
yazılımcıların tasarladığı programlara Türkçe karakterler girdiğinizde nasıl bu
programlar patır patır dökülüyorsa, eğer siz de baytlar ve karakterler
arasındaki farkı anlamazsanız sizin yazdığınız programlar da hiç beklemediğiniz
bir anda tökezleyebilir.

Örneğin yazdığınız bir programın bir aşamasında programa yalnızca tek
karakterlik verilerin girilmesi temeli üzerinden bir işlem yaptığınızı düşünün.
Yani programınız içinde yapacağınız bir işlem, birden fazla karakter girişinin
engellenmesini gerektiriyor olsun. 

Bunun için şöyle bir şey yazmış olun::
    
    a = "k"
    
    if len(a) > 1:
        print("Lütfen yalnızca tek bir karakter giriniz!")
    else:
        print("Teşekkürler!")
        
Ben burada temsili olarak `a` adlı bir değişken oluşturdum ve örnek olması
açısından da bunun değerini 'k' olarak belirledim. Bu değerlerle programımız
düzgün bir şekilde çalışır. Çünkü `a` değişkeninin değeri tek bir karakter olan
'k' harfi. Ama eğer `a` değişkeninin değeri mesela 'kz' gibi bir şey olsaydı
programımız 'Lütfen yalnızca tek bir karakter giriniz!' uyarısı verecekti...

Şimdi bu `a` değişkeninin sizin tarafınızdan belirlenmediğini, bu değerin başka
bir kaynaktan geldiğini düşünün. Eğer size bu değeri gönderen kaynak, bu değeri
UNICODE kod konumu olarak gönderiyorsa programınız düzgün çalışır. Ama peki ya
gelen bu veri bayt olarak geliyorsa ne olacak? 

Yukarıda verdiğimiz örneğin neden önemli olduğunu, daha doğrusu bu örnekle ne
demek istediğimiz ve nereye varmaya çalıştığımızı anlamamış olabilirsiniz. Ama
endişe etmenize hiç gerek yok. Zira bu bölümde yukarıda sorduğumuz sorunun
cevabını derinlemesine ele alacağız. Bu bölümün sonuna vardığımızda neler olup
bittiğini ve baytların neden bu kadar önemli olduğunu gayet iyi anlıyor
olacaksınız. 

Eskisi ve Yenisi
****************

Gelin isterseniz tam olarak ne ile karşı karşıya olduğumuzu daha iyi
anlayabilmek için Python3 öncesi durumun nasıl olduğuna bakalım. Eğer geçmişte
Python programlama dilinin karakter dizileri ve baytları nasıl ele aldığını
bilirsek bugünkü durumu ve dolayısıyla genel olarak karakter dizisi ve bayt
kavramını çok daha net bir şekilde kavrayabiliriz. 

Python'ın 2.x sürümlerinde, bir karakter dizisi tanımladığınızda Python bu
karakter dizisini bir bayt dizisi olarak temsil ediyordu. Örneğin::
    
    >>> kardiz = "e"
    
Burada `kardiz` adlı değişkenin değeri, bir baytlık bir karakter dizisidir. Bunu
``len()`` fonksiyonu ile teyit edelim::
    
    >>> len(kardiz)
    
    1
    
Bir de şuna bakalım::

    >>> kardiz = "ş"

Burada ise `kardiz` adlı değişkenin değerinin kaç baytlık bir karakter dizisi
olduğu, yani bir bakıma ``len()`` fonksiyonunun ne çıktı vereceği işletim
sisteminden işletim sistemine farklılık gösterir. Eğer kullandığınız işletim
sistemi Windows ise muhtelemen ``len(kardiz)`` komutu `1` çıktısı verecektir.
Ama eğer bu komutu GNU/Linux dağıtımlarından birinde veriyorsanız alacağınız
çıktı büyük ihtimalle `2` olacaktır. 

Dediğimiz gibi, Python2'de `str` veri tipi bize bir dizi bayt verir. Dolayısıyla
bu veri tipinin içinde tuttuğu karakter dizisinin kaç bayt ile gösterileceği,
sistemdeki öntanımlı kod çözücünün hangisi olduğuna bağlıdır. Kullandığınız
işletim sisteminde öntanımlı kod çözücünün hangisi olduğunu şu komutla
bulabilirsiniz::
    
    >>> import locale
    >>> locale.getpreferredencoding()
    
Eğer Windows kullanıyorsanız buradan alacağınız çıktı muhtemelen cp1254
olacaktır. cp1254, Microsoft'un Türkçe için özel olarak kullandığı bir kod
sayfası olduğu için, 128 ile 256 sayıları arasında Türkçe karakterleri içerir. O
yüzden bu kodlama sisteminde Türkçe karakterler 1 bayt ile gösterilebilir. Bu
kod sayfasının içeriğinde hangi karakterlerin hangi sayılara karşılık geldiğini
görmek için `en.wikipedia.org/wiki/Windows-1254
<http://en.wikipedia.org/wiki/Windows-1254>`_ adresindeki tabloyu
inceleyebilirsiniz.

Ama eğer yukarıdaki komutların çıktısı UTF-8 veya başka bir kod çözücü ise,
Türkçe karakterler 1 bayt ile gösterilemeyeceği için ``len(kardiz)`` komutu `1`
değil, `2` çıktısı verecektir.

Bir de şuna bakalım::
    
    >>> len("€")
    
Bu komutu hangi işletim sisteminde verdiğinize bağlı olarak yukarıdaki komuttan
alacağınız çıktı farklı olacaktır. `str` tipi Python2'de karakter dizilerini
bayt olarak temsil eder. Bu temsilin de hangi kurallara göre yapılacağı
kullanılan kod çözücüye bağlıdır. Eğer karakter dizileri baytlara çevrilirken
cp1254 adlı kod çözücü kullanılırsa, bu kod çözücü '€' simgesini tek bayt
ile gösterilebildiği için yukarıdaki komut `1` çıktısı verir. Ama UTF-8 adlı kod
çözücü '€' simgesini `3` baytla gösterebildiği için yukarıdaki komutun çıktısı
da buna paralel olarak `3` olacaktır.

`str` veri tipi ile gösterilen bu karakter dizilerinin içindeki baytlara ulaşmak
için şu yöntemi kullanabilirsiniz::
    
    >>> "ş"[0]
    
    '\xc5'
    
    >>> "ş"[1]
    
    '\x9f'
    
Gördüğünüz gibi, `str` veri tipi gerçekten de bize bir dizi bayt veriyor. Eğer
karakter dizilerini baytlarına göre değil de sahip oldukları karakter sayısına
göre saymak isterseniz bunları UNICODE olarak tanımlanız gerekiyor::
    
    >>> len(u'ş')
    
    1
    
Python3 ile birlikte yukarıda bahsettiğimiz durumda bazı değişiklikler oldu.
Artık `str` veri tipi UNICODE kod konumlarını döndürüyor. Dolayısıyla artık her
karakter dizisi, sahip oldukları karakter sayısına göre sayılabiliyor::
    
    >>> len("ş")
    
    1
    
    >>> len("€")
    
    1
    
İşte eğer Python2'deki `str` veri tipini elde etmek istiyorsanız, Python3'te
`bytes` adlı yeni veri tipini kullanmanız gerekiyor.
    
Bayt Tanımlamak
****************

Bildiğiniz gibi Python programlama dilinde her veri tipinin kendine özgü bir
tanımlanma biçimi var. Örneğin bir liste tanımlamak için şöyle bir şey
yazıyoruz::
    
    >>> liste = []
    
Böylece boş bir liste tanımlamış olduk. Aynı şekilde karakter dizilerini de
şöyle tanımlıyorduk::
    
    >>> kardiz = ''
    
Bu şekilde de boş bir karakter dizisi tanımlamış olduk. İşte boş bir bayt
tanımlamak için de şu yapıyı kullanıyoruz::
    
    >>> bayt = b''
    
Gelin tanımladığımız bu veri tipinin bayt olduğunu teyit edelim::
    
    >>> type(bayt)
    
    <class 'bytes'
    
Gördüğünüz gibi, gerçekten de bayt tipinde bir veri tanımlamışız. Nasıl karakter
dizileri 'str', listeler 'list' ifadesiyle gösteriliyorsa, baytlar da 'bytes'
ifadesi ile gösterilir. 

Peki bu şekilde bir bayt veri tipi tanımlamak ne işimize yarar? 

Hatırlarsanız bayt veri tipini ikili (*binary*) dosyaları anlatırken de
görmüştük. Orada da söylediğimiz gibi, ikili dosyaları okuduğunuzda elde
edeceğiniz şey karakter dizisi değil bayttır. Aynı şekilde, ikili dosyalara da
ancak baytları yazabilirsiniz. Dolayısıyla eğer ikili dosyalarla birtakım
işlemler yapacaksanız bu bayt veri tipini yoğun olarak kullanacağınızdan hiç
şüpheniz olmasın. Yani bayt veri tipi kolayca görmezden gelebileceğiniz
gereksiz bir veri tipi değildir. 

bytes() Fonksiyonu
*******************

Bayt veri tipi temel olarak ASCII karakterleri kabul eder. Dolayısıyla ASCII
tablosu dışında kalan karakterleri doğrudan bayt olarak temsil edemezsiniz::
    
    >>> b'ş'

      File "<stdin>", line 1
    SyntaxError: bytes can only contain ASCII literal characters.
    
Ama ASCII dışında kalan karakterleri de bayt'a dönüştürmenin bir yolu var. Bunun
için ``bytes()`` adlı bir fonksiyondan yararlanacağız::
    
    >>> b = bytes("ş", "utf-8")
    
Gördüğünüz gibi, ilgili karakterin hangi kod çözücü ile kodlanacağını
belirterek, bayt tipinde bir veri oluşturabiliyoruz.

Tahmin edebileceğiniz gibi, ``bytes()`` fonksiyonu, belirttiğimiz kod çözücü ile
kodlanamayan karakterlerle karşılaşılması durumunda ne yapılacağını
belirlememizi sağlayan `errors` adlı bir parametreye de sahiptir::
    
    >>> b = bytes("Fırat", "ascii", errors="xmlcharrefreplace")
    >>> b
    
    b'F&#305;rat'
    
Önceki derslerimizde `errors` parametresinin hangi değerleri alabileceğini
tartışmıştık. Orada anlattığımız şeyler burada da geçerlidir.

Baytların Metotları
********************

Bütün veri tiplerinde olduğu gibi, `bytes` adlı veri tipinin de birtakım
metotları bulunur. Bu metotların listesini almak için şu komutu
kullanabileceğinizi biliyorsunuz::
    
    >>> dir(bytes)
    
Listeye baktığınızda bu metotları karakter dizilerinin metotları ile hemen hemen
aynı olduğunu göreceksiniz. Baytların metotları arasında olup da karakter
dizilerinin metotları arasında olmayan metotları şu şekilde elde edebilirsiniz::

    >>> for i in dir(bytes):
    ...     if i not in dir(str):
    ...         print(i)
    
    decode
    fromhex

Gördüğünüz gibi, ``decode()`` ve ``fromhex()`` adlı metotlar baytlarda var, ama
karakter dizilerinde yok. O yüzden biz de bu bölümde yalnızca bu iki metodu
incelemekle yetineceğiz. Çünkü öteki metotları zaten karakter dizilerinden
tanıyorsunuz.
    
decode
=========

Hatırlarsanız karakter dizilerinin ``encode()`` adlı bir metodu vardı. Bu metot
yardımıyla karakter dizilerini belli bir kodlama biçimine göre kodlayabiliyor,
yani bunları baytlara çevirebiliyorduk. Mesela 'İ' harfini UTF-8 ile
kodlayalım::
    
    >>> "İ".encode("utf-8")
    
    b'\xc4\xb0'
    
Aynı harfi cp1254 ile kodlarsak şu çıktıyı elde ederiz::

    >>> "İ".encode("cp1254")

    b'\xdd'    
    
Tahmin edebileceğiniz gibi, bu harfi ASCII ile kodlayamayız::
    
    >>> "İ".encode("ascii")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode character '\u0130' in position 0:
     ordinal not in range(128)
     
İşte bu kodlama işlemini tersine çevirebilmek, yani baytları belli bir kodlama
biçimine göre karakter dizilerine dönüştürebilmek için ``decode()`` metodundan
yararlanacağız::

    >>> b"\xc4\xb0".decode("utf-8")
    
    'İ'
    
Bu baytları bir de başka kodlama sistemleri ile kodlamayı deneyelim::
    
    >>> b"\xc4\xb0".decode("cp1254")
    
    'Ä°'
    
Gördüğünüz gibi, cp1254 adlı kod çözücü bu baytı çözebiliyor, ama yanlış
çözüyor! Çünkü bu baytın gösterdiği sayı cp1254 adlı kod sayfasında 'İ'ye değil,
başka bir karaktere karşılık geliyor. Aslında başka iki karaktere, yani C4 ve B0
ile gösterilen `Ä` ve `°` karakterlerine karşılık geliyor... Bu durumu
http://en.wikipedia.org/wiki/Windows-1254 adresine gidip kendiniz de
görebilirsiniz.

Bu baytları bir de ASCII ile çözmeye çalışalım::

    >>> b"\xc4\xb0".decode("ascii")
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0: ordinal
    not in range(128)

Elbette, bu karakter 128'den büyük bir sayıya karşılık geldiği için ASCII
tarafından çözülemeyecektir.    

fromhex
========

Bu metot, onaltılı sayma sistemindeki bir sayıdan oluşan bir karakter dizisini
alıp, bayta dönüştürür. Bu metodu şöyle kullanıyoruz::
    
    >>> bytes.fromhex("c4b0")
    
    b'\xc4\xb0'

Gördüğünüz gibi, bu metot bir onaltılı sayı olan `c4b0`'ı alıp, bize bir bayt
nesnesi veriyor.

Bayt Dizileri
**************

`bytes` adlı veri tipi ile elde ettiğimiz veri tıpkı karakter dizileri gibi,
üzerinde değişiklik yapılamayan bir veridir. Dolayısıyla bir `bytes` nesnesi
üzerinde değişiklik yapabilmek için o nesneyi tekrar tanımlamamız gerekir::
    
    >>> b = b'PDF'
    >>> v = b'-1.7'
    >>> b = b + v
    >>> b
    
    b'PDF-1.7'
    
Ama Python programlama dilinde `bytes` veri tipi dışında, baytlara ilişkin ikinci
veri tipi daha bulunur. `bytearray` adlı bu veri tipi, `bytes` veri tipinin
aksine, üzerinde değişiklik yapılabilen bir veri tipidir. 

Python'da `bytearray` veri tipini şu şekilde tanımlıyoruz::
    
    >>> pdf = bytearray(b'PDF-1.7')
    
Gördüğünüz gibi, bir bayt dizisi tanımlayabilmek için ``bytearray()`` adlı bir
fonksiyondan faydalanıyoruz.

Bayt Dizilerinin Metotları
**************************

Bayt dizileri bir bakıma listelerle baytların karışımı gibidir. ``dir(bytearray)``
gibi bir komutla bu veri tipinin metotlarını inceleyecek olursanız, bu veri
tipinin hem baytlardan hem de listelerden birtakım metotlar aldığını görürsünüz.

Bu veri tipi listelerin şu metotlarına sahiptir:

    #. append
    #. clear
    #. copy
    #. count
    #. extend
    #. index
    #. insert
    #. pop
    #. remove
    #. reverse

Bu veri tipi baytların ise şu metotlarına sahiptir:

    #. capitalize
    #. center
    #. count
    #. decode
    #. endswith
    #. expandtabs
    #. find
    #. fromhex
    #. index
    #. isalnum
    #. isalpha
    #. isdigit
    #. islower
    #. isspace
    #. istitle
    #. isupper
    #. join
    #. ljust
    #. lower
    #. lstrip
    #. maketrans
    #. partition
    #. replace
    #. rfind
    #. rindex
    #. rjust
    #. rpartition
    #. rsplit
    #. rstrip
    #. split
    #. splitlines
    #. startswith
    #. strip
    #. swapcase
    #. title
    #. translate
    #. upper
    #. zfill
    

