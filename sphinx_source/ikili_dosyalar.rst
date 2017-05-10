.. meta::
   :description: Bu bölümde ikili dosyaları (binary files) ele alacağız.
   :keywords: python, python3, dosyalar

.. highlight:: py3

*************************
İkili (*Binary*) Dosyalar
*************************

Dosyalar çoğunlukla iki farklı sınıfa ayrılır: Metin dosyaları ve ikili
dosyalar. Metin dosyaları derken neyi kastettiğimiz az çok anlaşılıyor. Eğer bir
dosyayı bir metin düzenleyici ile açtığınızda herhangi bir dilde yazılmış
'okunabilir' bir metin görüyorsanız, o dosya bir metin dosyasıdır. Mesela
Notepad, Gedit, Kwrite veya benzeri metin düzenleyicileri kullanarak
oluşturduğunuz dosyalar birer metin dosyasıdır. Şimdiye kadar verdiğimiz bütün
örnekler metin dosyalarını içeriyordu. Peki 'ikili' (*binary*) dosya ne demek?

İkili dosyalar ise, metin dosyalarının aksine, metin düzenleyicilerle
açılamayan, açılmaya çalışıldığında ise çoğunlukla anlamsız karakterler içeren
bir dosya türüdür. Resim dosyaları, müzik dosyaları, video dosyaları, MS Office
dosyaları, LibreOffice dosyaları, OpenOffice dosyaları, vb. ikili dosyalara
örnektir. 

Önceki bölümlerde de ifade ettiğimiz gibi, bilgisayarlar yalnızca sayılarla
işlem yapabilir. Bilgisayarların üzerinde işlem yapabildiği bu sayıların `0` ve
`1` adlı iki sayı olduğunu biliyoruz.

Peki bu iki farklı sayıyı kullanarak neler yapabiliriz? Aslında, bu iki farklı
sayıyı kullanarak her türlü işlemi yapabiliriz: Basit veya karmaşık aritmetik
hesaplamalar, metin düzenleme, resim veya video düzenleme, web siteleri
hazırlama, uzaya mekik gönderme... Bütün bu işlemleri sadece iki farklı sayı
kullanarak yapabiliriz. Daha doğrusu bilgisayarlar yapabilir.

Durum böyle olmasına rağmen, ilk bilgisayarlar yalnızca hesaplama işlemleri için
kullanılıyordu. Yani metin içeren işlemleri yapmak bilgisayarların değil, mesela
daktiloların görevi olarak görülüyordu. Bu durumu telefon teknolojisi ile
kıyaslayabilirsiniz. Bildiğiniz gibi, ilk telefonlar yalnızca iki kişi
arasındaki sesli iletişimi sağlamak için kullanılıyordu. Ama yeni nesil
telefonlar artık ikiden fazla kişi arasındaki sesli ve görüntülü iletişimi
sağlayabilmenin yanısıra, önceleri birbirinden farklı cihazlarla
gerçekleştirilen işlemleri artık tek başına yerine getirebiliyor.

İlk bilgisayarlarda ise metinlerin, daha doğrusu karakterlerin görevi bir hayli
sınırlıydı.

Başta da söylediğimiz gibi, çoğunlukla dosyalar iki farklı sınıfa ayrılır: Metin
dosyaları ve ikili dosyalar. Ama işin aslı sadece tek bir dosya türü vardır:
İkili dosyalar (*binary files*). Yani bilgisayarlar açısından bütün dosyalar,
içlerinde ne olursa olsun, birer ikili dosyadır ve içlerinde sadece 0'ları ve
1'leri barındırır. İşte bu 0 ve 1'lerin ne anlama geleceğini, işletim sistemleri
ve bu sistemler üzerine kurulu yazılımlar belirler. Eğer bir dosya metin
dosyasıysa bu dosyadaki 0 ve 1'ler birer karakter/harf olarak yorumlanır. Ama
eğer dosya bir ikili dosyaysa dosya içindeki 0 ve 1'ler özel birtakım veriler
olarak ele alınır ve bu verileri okuyan yazılıma göre değer kazanır. Örneğin
eğer ilgili dosya bir resim dosyasıyla, bu dosya herhangi bir resim
görüntüleyici yazılım ile açıldığında karşımıza bir resim çıkar. Eğer ilgili
dosya bir video dosyasıyla, bu dosya bir video görüntüleyici yazılım ile
açıldığında karşımıza bir video çıkar. Bu olgudan bir sonraki bölümde daha
ayrıntılı olarak söz edeceğiz. Biz şimdilik işin sadece pratiğine yoğunlaşalım
ve temel olarak iki farklı dosya çeşidi olduğunu varsayalım: Metin dosyaları ve
ikili dosyalar.

Buraya gelene kadar hep metin dosyalarından söz etmiştik. Şimdi ise ikili
dosyalardan söz edeceğiz. 

Hatırlarsanız metin dosyalarını açmak için temel olarak şöyle bir komut
kullanıyorduk::
    
    f = open(dosya_adı, 'r')
    
Bu şekilde bir metin dosyasını okuma kipinde açmış oluyoruz. Bir metin dosyasını
değil de, ikili bir dosyayı açmak için ise şu komutu kullanacağız::
    
    f = open(dosya_adı, 'rb')
    
Dosyaya erişme kiplerini gösterdiğimiz tabloda ikili erişim türlerini de
verdiğimizi hatırlıyorsunuz. 

Peki neden metin dosyaları ve ikili dosyalar için farklı erişim kipleri
kullanıyoruz?

İşletim sistemleri satır sonları için birbirinden farklı karakterler
kullanırlar. Örneğin GNU/Linux dağıtımlarında satır sonları `\\n` karakteri ile
gösterilir. Windows işletim sistemi ise satır sonlarını `\\r\\n` karakterleriyle
gösterir. İşte Python herhangi bir dosyayı açarken, eğer o dosya bir metin
dosyası ise, satır sonlarını gösteren karakterleri, dosyanın açıldığı işletim
sistemine göre ayarlar. Yani satır sonlarını standart bir hale getirerek `\\n`
karakterine dönüştürür.

Metin dosyaları ile ikili dosyalar arasında önemli bir fark bulunur: Bir metin
dosyasındaki ufak değişiklikler dosyanın okunamaz hale gelmesine yol açmaz.
Olabilecek en kötü şey, değiştirilen karakterin okunamaz hale gelmesidir. Ancak
ikili dosyalarda ufak değişiklikler dosyanın tümden bozulmasına yol açabilir.
Dolayısıyla Python'ın yukarıda bahsedilen satır sonu değişiklikleri ikili
dosyaların bozulmasına yol açabilir. Yani eğer siz ikili bir dosyayı `'rb'`
yerine sadece `'r'` gibi bir kiple açarsanız dosyanın bozulmasına yol
açabilirsiniz. İkili bir dosyayı `'rb'` (veya `'wb'`, `'ab'`, `'xb'`, vb.) gibi
bir kipte açtığınızda Python satır sonlarına herhangi bir değiştirme-dönüştürme
işlemi uygulamaz. Böylece dosya bozulma riskiyle karşı karşıya kalmaz. O yüzden,
metin dosyalarını ve ikili dosyaları açarken farklı kipler kullanmamız
gerektiğine dikkat ediyoruz.

İkili Dosyalarla Örnekler
**************************

Gelin isterseniz bu noktada birkaç örnek verelim. 

PDF Dosyalarından Bilgi Alma
===============================

Tıpkı resim, müzik ve video dosyaları gibi, `PDF` dosyaları da birer ikili
dosyadır. O halde hemen önümüze bir `PDF` dosyası alalım ve bu dosyayı okuma
kipinde açalım::
    
    >>> f = open("falanca.pdf", "rb")
    
Şimdi de bu dosyadan `10` baytlık bir veri okuyalım::
    
    >>> f.read(10)
    
    b'%PDF-1.3\n4'
    
Bu çıktıda gördüğünüz `'b'` işaretine şimdilik takılmayın. Birazdan bunun ne
olduğunu bütün ayrıntılarıyla anlatacağız. Biz bu harfin, elimizdeki verinin
bayt türünde bir veri olduğunu gösteren bir işaret olduğunu bilelim yeter. 

Gördüğünüz gibi, bir `PDF` dosyasının ilk birkaç baytını okuyarak hem dosyanın
bir `PDF` belgesi olduğunu teyit edebiliyoruz, hem de bu `PDF` belgesinin, hangi
`PDF` sürümü ile oluşturulduğunu anlayabiliyoruz. Buna göre bu belge PDF
talimatnamesinin 1.3 numaralı sürümü ile oluşturulmuş. 

Eğer biz bu belgeyi bir ikili dosya olarak değil de bir metin dosyası olarak
açmaya çalışsaydık şöyle bir hata alacaktık::

    >>> f = open("falanca.pdf")
    >>> okunan = f.read()
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\Python33\lib\encodings\cp1254.py", line 23, in decode
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 527: char
    acter maps to <undefined>
    
Python'ın bu dosyanın bir ikili dosya olduğu konusunda bilgilendirerek, dosyanın
düzgün bir şekilde açılıp okunabilmesini sağlıyoruz. 

Gelin bu `PDF` belgesi üzerinde biraz daha çalışalım.

`PDF` belgelerinde, o belge hakkında bazı önemli bilgiler veren birtakım özel
etiketler bulunur. Bu etiketler şunlardır:

    ==================  ===============================================
        Etiket                  Anlamı
    ------------------  -----------------------------------------------    
     /Creator             Belgeyi oluşturan yazılım
     /Producer            Belgeyi PDF'e çeviren yazılım
     /Title               Belgenin başlığı
     /Author              Belgenin yazarı
     /Subject             Belgenin konusu
     /Keywords            Belgenin anahtar kelimeleri
     /CreationDate        Belgenin oluşturulma zamanı
     /ModDate             Belgenin değiştirilme zamanı
    ==================  ===============================================
    
Bu etiketlerin tamamı bütün `PDF` dosyalarında tanımlı değildir. Ama özellikle
`/Producer` etiketi her `PDF` dosyasında bulunur. 

Şimdi örnek olması bakımından elimize bir `PDF` dosyası alalım ve bunu güzelce
okuyalım::
    
    >>> f = open("falanca.pdf", "rb")
    >>> okunan = f.read()
    
Şimdi de `/Producer` ifadesinin dosya içinde geçtiği noktanın sıra numarasını
bulalım. Bildiğiniz gibi, dosyaların ``read()`` metodu bize bir karakter dizisi
verir. Yine bildiğiniz gibi, karakter dizilerinin ``index()`` metodu yardımıyla
bir öğenin karakter dizisi içinde geçtiği noktayı bulabiliyoruz. Yani::
    
    >>> producer_index = okunan.index(b"/Producer")
    
Burada `/Producer` ifadesinin başına `'b'` harfini yerleştirmeyi unutmuyoruz.
Çünkü şu anda yaptığımız işlem ikili bir dosya içinde geçen birtakım baytları
arama işlemidir. 

`producer_index` değişkeni, '/Producer' ifadesinin ilk baytının dosya içindeki
konumunu tutuyor. Kontrol edelim::
    
    >>> producer_index
    
    4077883
    
Bu değerin gerçekten de '/Producer' ifadesinin ilk baytını depoladığını teyit
edelim::
    
    >>> okunan[producer_index]
    
    47
    
Daha önce de dediğimiz gibi, bilgisayarlar yalnızca sayıları görür. Bu sayının
hangi karaktere karşılık geldiğini bulmak için ``chr()`` fonksiyonundan
yararlanabilirsiniz::
    
    >>> chr(okunan[producer_index])
    
    '/'
    
Gördüğünüz gibi, gerçekten de `producer_index` değişkeni '/Producer' ifadesinin
ilk baytının dosya içindeki konumunu gösteriyor. Biz bu konumu ve bu konumun 50-60
bayt ötesini sorgularsak, `PDF` belgesini üreten yazılımın adına ulaşabiliriz.
Dikkatlice bakın::
    
    >>> okunan[producer_index:producer_index+50]

    b'/Producer (Acrobat Distiller 2.0 for Macintosh)\r/T'
    
Hatta eğer bu çıktı üzerine ``split()`` metodunu uygularsak, çıktıyı daha
kullanışlı bir hale getirebiliriz::
    
    >>> producer = okunan[producer_index:producer_index+50].split()
    >>> producer
    
    [b'/Producer', b'(Acrobat', b'Distiller', b'2.0', b'for', b'Macintosh)', b'/T']
    
Bu şekilde, ihtiyacımız olan bilginin istediğimiz parçasına kolayca
ulaşabiliriz::
    
    >>> producer[0]
    
    b'/Producer'
    
    >>> producer[1]
    
    b'(Acrobat'
    
    >>> producer[1:3]
    
    [b'(Acrobat', b'Distiller']
    
Elbette bu yöntem, bir `PDF` dosyasından gerekli etiketleri almanın en iyi
yöntemi değildir. Ama henüz Python bilgimiz bu kadarını yapmamıza müsaade
ediyor. Ancak yine de, yukarıda örnek, bir ikili dosyadan nasıl veri alınacağı
konusunda size iyi bir fikir verecektir. 

Resim Dosyalarının Türünü Tespit Etme
======================================

Dediğimiz gibi, resim dosyaları, müzik dosyaları, video dosyaları ve benzeri
dosyalar birer ikili dosyadır. Mesela resim dosyalarını ele alalım. Diyelim ki,
resimlerin hangi türde olduğunu tespit eden bir program yazmak istiyorsunuz.
Yani yazdığınız bu programla bir resim dosyasının `PNG` mi, `JPEG` mi, `TIFF`
mi, yoksa `BMP` mi olduğunu anlamak istiyorsunuz.

Peki bir resim dosyasının hangi türde olduğunu bulmak için uzantısına baksanız
olmaz mı? Asla unutmayın dosya uzantıları ile dosya biçimleri arasında doğrudan
bir bağlantı yoktur. O yüzden dosya uzantıları, dosya biçimini anlamak açısından
güvenilir bir yöntem değildir. Bir resim dosyasının sonuna hangi uzantıyı
getirirseniz getirin, o dosya bir resim dosyasıdır. Yani mesela bir resim
dosyasının uzantısı yanlışlıkla veya bilerek `.doc` olarak değiştirilmişse, o
dosya bir WORD dosyası haline gelmez. İşte yazacağınız program, bir resim
dosyasının uzantısı ne olursa olsun, hatta dosyanın bir uzantısı olmasa bile, o
dosyanın hangi türde olduğunu söyleyebilecek.

Bir resim dosyasının hangi türde olduğunu anlayabilmek için ilgili dosyanın ilk
birkaç baytını okumanız yeterlidir. Bu birkaç bayt içinde o resim dosyasının
türüne dair bilgileri bulabilirsiniz. 

Resim dosyalarının türlerini birbirinden ayırt etmenizi sağlayacak verilerin ne
olduğunu, ilgili resim türünün teknik şartnamesine bakarak öğrenebilirsiniz.
Ancak teknik şartnameler genellikle okuması zor metinlerdir. Bu yüzden, doğrudan
şartnameyi okumak yerine, Internet üzerinde kısa bir araştırma yaparak konuyu
daha kolay anlamanızı sağlayacak yardımcı belgelerden de yardım alabilirsiniz.

JPEG
-------

`JPEG` biçimi ile ilgili bilgileri http://www.jpeg.org adresinde bulabilirsiniz.
`JPEG` dosya biçimini daha iyi anlamanızı sağlayacak yardımcı kaynak ise
şudur:

    #. http://www.faqs.org/faqs/jpeg-faq/part1/section-15.html

Yukarıda verdiğimiz adreslerdeki bilgilere göre bir `JPEG` dosyasının en başında
şu veriler bulunur::

    FF	D8	FF	E0	?   ?	4A	46	49	46	00
    
Ancak eğer ilgili `JPEG` dosyası bir CANON fotograf makinesi ile oluşturulmuşsa
bu veri dizisi şöyle de olabilir::
    
    FF	D8	FF	E0	?   ?	45  78  69  66	00
    
Burada soru işareti ile gösterdiğimiz kısım, yani dosyanın `5.` ve `6.` baytları
farklı `JPEG` dosyalarında birbirinden farklı olabilir. Dolayısıyla bir `JPEG`
dosyasını başka resim dosyalarından ayırabilmek için dosyanın ilk dört baytına
bakmamız, sonraki iki baytı atlamamız ve bunlardan sonra gelen beş baytı kontrol
etmemiz yeterli olacaktır.
    
Yukarıda gördükleriniz birer on altılı (*hex*) sayıdır. Bunlar onlu düzende
sırasıyla şu sayılara karşılık gelir::

    255 216 255 224 ? ? 74 70 73 70 0
    255 216 255 224 ? ? 45 78 69 66 0 #canon        
    
Bu diziler içinde özellikle şu dört sayı bizi yakından ilgilendiriyor::
    
    74 70 73 70
    45 78 69 66 #canon
 
Bu sayılar sırasıyla 'J', 'F', 'I', 'F' ve 'E', 'x', 'i', 'f' harflerine
karşılık gelir. Yani bir `JPEG` dosyasını ayırt edebilmek için ilgili dosyanın
7-10 arası baytlarının ne olduğuna bakmamız yeterli olacaktır. Eğer bu aralıkta
'JFIF' veya 'Exif' ifadeleri varsa, o dosya bir `JPEG` dosyasıdır. Buna göre
şöyle bir kod yazabiliriz::
    
    f = open(dosya_adı, 'rb')
    data = f.read(10)
    if data[6:11] in [b"JFIF", b"Exif"]:
        print("Bu dosya JPEG!")
    else:
        print("Bu dosya JPEG değil!")
        
Burada herhangi bir resim dosyasının ilk on baytını okuduk öncelikle::
    
    data = f.read(10)
    
Çünkü aradığımız bilgiler ilk on bayt içinde yer alıyor. 

Daha sonra okuduğumuz kısmın 7 ila 10. baytları arasında kalan verinin ne
olduğuna bakıyoruz::

    if data[6:11] in [b"JFIF", b"Exif"]:
        ...
        
Eğer ilgili aralıkta 'JFIF' veya 'Exif' baytları yer alıyorsa bu dosyanın bir
`JPEG` dosyası olduğuna karar veriyoruz. 

Yukarıdaki kodları elinizdeki bir `JPEG` dosyasına uygulayarak kendi kendinize
pratik yapabilirsiniz.  

Mesela benim elimde `d1.jpg`, `d2.jpg` ve `d3.jpeg` adlı üç farklı `JPEG`
dosyası var::
    
    dosyalar = ["d1.jpg", "d2.jpg", "d3.jpeg"]
    
Bu dosyaların ilk onar baytını okuyorum::

    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        print(okunan)
        
Buradan şu çıktıyı alıyorum::
    
     d1.jpg         b'\xff\xd8\xff\xe0\x00\x10JFIF'
     d2.jpg         b'\xff\xd8\xff\xe1T\xaaExif'
     d3.jpeg        b'\xff\xd8\xff\xe0\x00\x10JFIF'
     
Gördüğünüz gibi bu çıktılar yukarıda `JPEG` dosyalarına ilişkin olarak
verdiğimiz bayt dizilimi ile uyuşuyor. Mesela ilk dosyayı ele alalım::
    
    d1.jpg         b'\xff\xd8\xff\xe0\x00\x10JFIF'
    
Burada şu baytlar var::
    
    \xff \xd8 \xff \xe0 \x00 \x10 J F I F
    
Sayıların başındaki `\\x` işaretleri bunların birer on altılı sayı
olduğunu gösteren bir işarettir. Dolayısıyla yukarıdakileri daha net
inceleyebilmek için şöyle de yazabiliriz::
    
    ff d8 ff e0 00 10 J F I F
    
Şimdi de ikinci dosyanın çıktısını ele alalım::
    
    d2.jpg         b'\xff\xd8\xff\xe1T\xaaExif'
    
Burada da şu baytlar var::
    
    ff d8 ff e1T aa E x i f
    
İşte dosyaların türünü ayırt etmek için bu çıktılardaki son dört baytı kontrol
etmemiz yeterli olacaktır::
    
    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        if okunan[6:11] in [b'JFIF', b'Exif']:
            print("Evet {} adlı dosya bir JPEG!".format(f))
        else:
            print("{} JPEG değil!".format(f))
            
Bu kodları elinizde bulunan farklı türdeki dosyalara uygulayarak, aldığınız
çıktıları inceleyebilirsiniz. 
        
PNG
-------

`PNG` dosya biçiminin teknik şartnamesine http://www.libpng.org/pub/png/spec/
adresinden ulaşabilirsiniz. 

Ayrıca yardımcı kaynak olarak da http://www.fileformat.info/format/png/egff.htm
adresindeki belgeyi kullanabilirsiniz.

Şartnamade,
http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature
sayfasındaki bilgiye göre bir `PNG` dosyasının ilk `8` baytı mutlaka aşağıdaki
değerleri içeriyor:

    =======================    ========================================
       onlu değer                 137  80  78  71  13  10  26  10
       on altılı değer             89  50  4e  47  0d  0a  1a  0a
       karakter değeri          \\211   P   N   G  \\r  \\n \\032 \\n
    =======================    ========================================
    
Şimdi elimize herhangi bir `PNG` dosyası alarak bu durumu teyit edelim::
    
    >>> f = open("falanca.png", "rb")
  
    >>> okunan = f.read(8)
    
Şartnamede de söylendiği gibi, bir `PNG` dosyasını öteki türlerden ayırt
edebilmek için dosyanın ilk `8` baytına bakmamız yeterli olacaktır. O yüzden biz
de yukarıdaki kodlarda sadece ilk `8` baytı okumakla yetindik. 

Bakalım ilk `8` baytta neler varmış::
    
   >>> okunan

    b'\x89PNG\r\n\x1a\n'
    
Bu değerin, şartnamedeki karakter değeri ile aynı olup olmadığını sorgulayarak
herhangi bir dosyanın `PNG` olup olmadığına karar verebilirsiniz::
    
    >>> okunan == b"\211PNG\r\n\032\n"
    
    True
    
Dolayısıyla şuna benzer bir kod yazarak, farklı resim dosyalarının türünü tespit
edebilirsiniz::
    
    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        if okunan[6:11] in [b'JFIF', b'Exif']:
            print("{} adlı dosya bir JPEG!".format(f))
        elif okunan[:8] == b"\211PNG\r\n\032\n":
            print("{} adlı dosya bir PNG!".format(f))
        else:
            print("Türü bilinmeyen dosya: {}".format(f))
           
Bu kodlarda bir resim dosyasının ilk `10` baytını okuduk. 7-11 arası baytların
içinde 'JFIF' veya 'Exif' baytları varsa o dosyanın bir `JPEG` olduğuna; ilk
`8` bayt `b"\211PNG\r\n\032\n"` adlı bayt dizisine eşitse de o dosyanın bir
`PNG` olduğuna karar veriyoruz.    
    
GIF
------

GIF şartnamesine http://www.w3.org/Graphics/GIF/spec-gif89a.txt adresinden
ulaşabilirsiniz. 

Bir dosyanın `GIF` olup olmadığına karar verebilmek için ilk `3` baytını
okumanız yeterli olacaktır. Standart bir `GIF` dosyasının ilk üç baytı 'G', 'I'
ve 'F' karakterlerinden oluşur. Dosyanın sonraki `3` baytı ise `GIF`'in sürüm
numarasını verir. |today| itibariyle `GIF` standardının şu sürümleri
bulunmaktadır:

    #. 87a - Mayıs 1987
    #. 89a - Temmuz 1989
    
Dolayısıyla standart bir `GIF` dosyasının ilk `6` baytı şöyledir:

    'GIF87a' veya 'GIF89a'
    
Eğer bir dosyanın `GIF` olup olmadığını anlamak isterseniz dosyanın ilk `3` veya
`6` baytını denetlemeniz yeterli olacaktır::
    
    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        if okunan[6:11] in [b'JFIF', b'Exif']:
            print("{} adlı dosya bir JPEG!".format(f))
        elif okunan[:8] == b"\211PNG\r\n\032\n":
            print("{} adlı dosya bir PNG!".format(f))
        elif okunan[:3] == b'GIF':
            print("{} adlı dosya bir GIF!".format(f))
        else:
            print("Türü bilinmeyen dosya: {}".format(f))
            
TIFF
------

`TIFF` şartnamesine http://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf
adresinden ulaşabilirsiniz. Bu şartnameye göre bir `TIFF` dosyası şunlardan
herhangi biri ile başlar:

    #. 'II'
    #. 'MM'
    
Dolayısıyla, bir `TIFF` dosyasını tespit edebilmek için dosyanın ilk `2` baytına
bakmanız yeterli olacaktır::
    
    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        if okunan[6:11] in [b'JFIF', b'Exif']:
            print("{} adlı dosya bir JPEG!".format(f))
        elif okunan[:8] == b"\211PNG\r\n\032\n":
            print("{} adlı dosya bir PNG!".format(f))
        elif okunan[:3] == b'GIF':
            print("{} adlı dosya bir GIF!".format(f))
        elif okunan[:2] in [b'II', b'MM']:
            print("{} adlı dosya bir TIFF!".format(f))
        else:
            print("Türü bilinmeyen dosya: {}".format(f))
            
BMP
------

`BMP` türündeki resim dosyalarına ilişkin bilgi için
http://www.digitalpreservation.gov/formats/fdd/fdd000189.shtml adresine
başvurabilirsiniz. 

Buna göre, `BMP` dosyaları 'BM' ile başlar. Yani::

    for f in dosyalar:
        okunan = open(f, 'rb').read(10)
        if okunan[6:11] in [b'JFIF', b'Exif']:
            print("{} adlı dosya bir JPEG!".format(f))
        elif okunan[:8] == b"\211PNG\r\n\032\n":
            print("{} adlı dosya bir PNG!".format(f))
        elif okunan[:3] == b'GIF':
            print("{} adlı dosya bir GIF!".format(f))
        elif okunan[:2] in [b'II', b'MM']:
            print("{} adlı dosya bir TIFF!".format(f))
        elif okunan[:2] in [b'BM']:
            print("{} adlı dosya bir BMP!".format(f))
        else:
            print("Türü bilinmeyen dosya: {}".format(f))

Gördüğünüz gibi ikili dosyalar, baytların özel bir şekilde dizildiği ve özel bir
şekilde yorumlandığı bir dosya türüdür. Dolayısıyla ikili dosyalarla
çalışabilmek için, ikili dosyanın bayt dizilimini yakından tanımak gerekiyor.

