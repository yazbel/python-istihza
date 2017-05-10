.. meta::
   :description: Bu bölümde dosyaların metot ve niteliklerini inceleyeceğiz.
   :keywords: python, python3, dosyalar

.. highlight:: py3

********************************
Dosyaların Metot ve Nitelikleri
********************************

Dosyalara ilişkin olarak bir önceki bölümde anlattığımız şeylerin kafanıza
yatması açısından size şu bilgiyi de verelim: Dosyalar da, tıpkı karakter
dizileri ve listeler gibi, Python programlama dilindeki veri tiplerinden
biridir. Dolayısıyla tıpkı karakter dizileri ve listeler gibi, dosya (*file*)
adlı bu veri tipinin de bazı metotları ve nitelikleri vardır. Gelin isterseniz
bu metot ve niteliklerin neler olduğunu şöyle bir listeleyelim::
    
    dosya = open("falanca_dosya.txt", "w") 
    print(*[metot for metot in dir(dosya) if not metot.startswith("_")], sep="\n")

Bu kodlar, dosya adlı veri tipinin bizi ilgilendiren bütün metotlarını alt alta
ekrana basacaktır. Eğer yukarıdaki kodları anlamakta zorluk çektiyseniz, bunları
şöyle de yazabilirsiniz::
    
    dosya = open("falanca_dosya.txt", "w")
    
    for metot in dir(dosya):
        if not metot.startswith("_"):
            print(metot, sep="\n")

Bildiğiniz gibi bu kodlar bir öncekiyle tamamen aynı anlama geliyor. 

Bu kodları çalıştırdığınızda karşınıza pek çok metot çıkacak. Biz buraya gelene
kadar bu metotların en önemlilerini zaten inceledik. İncelemediğimiz yalnızca
birkaç önemli metot (ve nitelik) kaldı. Gelin isterseniz henüz incelemediğimiz
bu önemli metot ve nitelikleri gözden geçirelim.

closed Niteliği
****************

Bu nitelik, bir dosyanın kapalı olup olmadığını sorgulamamızı sağlar. Dosya
adının `f` olduğunu varsayarsak, bu niteliği şöyle kullanıyoruz::
    
    f.closed
    
Eğer `f` adlı bu dosya kapalıysa `True` çıktısı, açıksa `False` çıktısı
verilecektir.  

readable() Metodu
******************

Bu metot bir dosyanın okuma yetkisine sahip olup olmadığını sorgulamamızı
sağlar. Eğer bir dosya `"r"` gibi bir kiple açılmışsa, yani o dosya 'okunabilir'
özellikle ise bu metot bize `True` çıktısı verir. Ama eğer dosya yazma kipinde
açılmışsa bu metot bize `False` çıktısı verecektir. 

writable() Metodu
*****************

Bu metot bir dosyanın yazma yetkisine sahip olup olmadığını sorgulamamızı
sağlar. Eğer bir dosya `"w"` gibi bir kiple açılmışsa, yani o dosya
'yazılabilir' özellikle ise bu metot bize `True` çıktısı verir. Ama eğer dosya
okuma kipinde açılmışsa bu metot bize `False` çıktısı verecektir.

truncate() Metodu
*****************

Bu metot, henüz işlemediğimiz metotlar arasında en önemlilerinden biridir. Bu
metot yardımıyla dosyalarımızı istediğimiz boyuta getirebiliyoruz. 

İngilizcede *truncate* kelimesi 'budamak, kırpmak' gibi anlamlara gelir. Bu
metodun yaptığı iş de bu anlamıyla uyumludur. Bu metodu temel olarak şöyle
kullanıyoruz::
    
    >>> with open("falanca.txt", "r+") as f:
    ...     f.truncate()
    
Bu komutu bu şekilde kullandığımızda dosyanın bütün içeriği silinecektir. Yani
bu kodlar, sanki dosyayı `"w"` kipiyle açmışsınız gibi bir etki ortaya
çıkaracaktır. 

``truncate()`` metodu yukarıda gördüğünüz şekilde parametresiz olarak
kullanılabileceği gibi, parametreli olarak da kullanılabilir. Bu metodun
parantezleri arasına, dosyanın kaç baytlık bir boyuta sahip olmasını
istediğinizi yazabilirsiniz. Örneğin::
    
    >>> with open("falanca.txt", "r+") as f:
    ...     f.truncate(10)
    
Bu kodlar, `falanca.txt` adlı dosyanın ilk `10` baytı dışındaki bütün verileri
siler. Yani dosyayı yalnızca `10` baytlık bir boyuta sahip olacak şekilde
kırpar. 

Gelin isterseniz bu metotla ilgili bir örnek verelim. Elimizdeki dosyanın şu
içeriğe sahip olduğunu varsayalım::
    
    Ahmet Özbudak : 0533 123 23 34
    Mehmet Sülün  : 0532 212 22 22
    Sami Sam      : 0542 333 34 34
    
Amacımız dosyadaki şu iki satırı tamamen silmek::
    
    Mehmet Sülün  : 0532 212 22 22
    Sami Sam      : 0542 333 34 34
    
Yani dosyanın yeni içeriğinin tam olarak şöyle olmasını istiyoruz::

    Ahmet Özbudak : 0533 123 23 34
    
Bunun için ``truncate()`` metodundan yararlanarak şu kodları yazabiliriz::
    
    with open("fihrist.txt", "r+") as f:
        f.readline()
        f.seek(f.tell())
        f.truncate()
        
Bu kodları bir dosyaya kaydedip çalıştırdığınızda, istediğiniz sonucu elde
ettiğinizi göreceksiniz. 

Burada sırasıyla şu işlemleri gerçekleştirdik:

#. Önce dosyamızı hem okuma hem de yazma kipinde açtık. Çünkü aynı dosya
   üzerinde hem okuma hem de yazma işlemleri gerçekleştireceğiz:
   
    .. parsed-literal::
    
        with open("fihrist.txt", "r+") as f:

#. Ardından dosyadan tek bir satır okuduk:

    .. parsed-literal::
        
        f.readline()
        
#. Daha sonra, ``truncate()`` metodunun imleç konumundan itibaren kırpma işlemi
   gerçekleştirebilmesi için imleci dosya içinde o anda bulunduğumuz konuma, yani
   ikinci satırın başına getirdik. Bildiğiniz gibi dosyaların ``tell()`` metodu, o
   anda dosya içinde hangi konumda bulunduğumuzu bildiriyor. Biz biraz önce
   yazdığımız ``readline()`` komutu yardımıyla dosyadan bir satır okuduğumuz için,
   o anda ikinci satırın başında bulunuyoruz. İşte ``seek()`` metodunu ve
   ``tell()`` metodundan elde ettiğimiz bu konum bilgisini kullanarak imleci
   istediğimiz konuma getirdik:
   
    .. parsed-literal::
    
        f.seek(f.tell())
       
#. İmleci istediğimiz konuma getirdiğimize göre artık kırpma işlemini
   gerçekleştirebiliriz:
    
    .. parsed-literal::
    
        f.truncate()
        
Artık elimizde tek satırlık bir dosya var...

``truncate()`` metodunun, yukarıda anlattığımızdan farklı bir özelliği daha
var. Her ne kadar *truncate* kelimesi 'kırpmak' anlamına gelse ve bu metotla
dosya boyutlarını küçültebilsek bile, bu metodu kullanarak aynı zamanda dosya
boyutlarını artırabiliriz de. Örneğin boyutu `1` kilobayt olan bir dosyayı `3`
kilobayta çıkarmak için bu metodu şöyle kullanabiliriz::
    
    >>> f = open("fihrist.txt", "r+")
    >>> f.truncate(1024*3)
    >>> f.close()
    
Dosyanın boyutunu kontrol edecek olursanız, dosyanın gerçekten de 3 kilobayt'a
çıktığını göreceksiniz. Peki bu metot bu işi nasıl yapıyor? Aslında bunun cevabı
çok basit: Dosyanın sonuna gereken miktarda `0` ekleyerek... Zaten eğer
`fihrist.txt` adlı bu dosyayı tekrar açıp okursanız bu durumu kendiniz de
görebilirsiniz::
    
    >>> f = open("fihrist.txt")
    >>> f.read()
    
Gördüğünüz gibi, dosya sıfırlarla dolu.

mode Niteliği
***************

Bu nitelik, bize bir dosyanın hangi kipte açıldığına dair bilgi verir::
    
    >>> f = open("falanca.txt")
    >>> f.mode
    
    'r'
    
Demek ki bu dosya `"r"` kipinde açılmış...  

name Niteliği
***************

Bu nitelik, bize bir dosyanın adını verir::
    
    >>> f.name
    
    'falanca.txt'

encoding Niteliği
******************

Bu nitelik, bize bir dosyanın hangi dil kodlaması ile kodlandığını söyler::
    
    >>> f.encoding
    
    'utf-8'
    
veya::
    
    >>> f.encoding
    
    'cp1254' #Windows
    
.. note:: Bu 'dil kodlaması' konusunu ilerleyen sayfalarda ayrıntılı olarak inceleyeceğiz.

Böylece dosyaların en önemli metot ve niteliklerini incelemiş olduk. Bu arada,
gerek bu derste, gerekse önceki derslerde verdiğimiz örneklerden, 'metot' ile
'nitelik' kavramları arasındaki farkı anladığınızı zannediyorum. Metotlar bir iş
yaparken, nitelikler bir değer gösterir. Nitelikler basit birer değişkenden
ibarettir. Metotlar ise bir işin nasıl yapılacağı ile ilgili süreci tanımlar.
Esasında bu ikisi arasındaki farkları çok fazla kafaya takmanıza gerek yok.
Zamanla (özellikle de başka programların kaynak kodlarını incelemeye
başladığınızda) bu ikisi arasındaki farkı bariz bir biçimde göreceksiniz. O
noktaya geldiğinizde, zaten kavramlar arasındaki farkları görmeniz konusunda biz
de size yardımcı olmaya çalışacağız.
