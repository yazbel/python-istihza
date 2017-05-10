.. meta::
   :description: Bu bölümde, bilgisayarların çalışma mantığını daha iyi anlayabilmek 
    için basit bir iletişim modeli oluşturacağız.
   :keywords: iletişim, Mors, alfabesi

.. highlight:: py3

**************************
Basit bir İletişim Modeli
**************************

Bu bölümde, bilgisayarların çalışma mantığını, verileri nasıl işlediğini,
sayılarla karakter dizilerini nasıl temsil ettiğini daha iyi ve daha net bir
şekilde anlayabilmek için basit bir iletişim modeli kuracağız.

Şimdi şöyle bir durum hayal edin: Diyelim ki, hatlar üzerinden iletilen elektrik
akımı yoluyla bir arkadaşınızla haberleşmenizi sağlayacak bir sistem
tasarlıyorsunuz. Bu sistem, verici tarafında elektrik akımının gönderilmesini
sağlayan bir anahtardan, alıcı tarafında ise, gelen akımın şiddetine göre loş
veya parlak ışık veren bir ampulden oluşuyor. Eğer vericiden gönderilen elektrik
akımı düşükse alıcı loş bir ışık, eğer gelen akım yüksekse alıcı parlak bir ışık
görecek. Elbette eğer isterseniz düşük akım-yüksek akım karşıtlığı yerine akım
varlığı-akım yokluğu karşıtlığını da kullanabilirsiniz. Böylece vericiden akım
gönderildiğinde ampul yanar, gönderilmediğinde ise söner. Bana düşük akım-yüksek
akım karşıtlığı daha kullanışlı geldiği için böyle tercih ettim. Siz tabii ki
öbür türlüsünü de tercih edebilirsiniz.

Yukarıda bahsedildiği gibi sistemimizi kurduk diyelim. Peki ama bu sistem verici
ile alıcı arasında basit de olsa bir iletişim kurmamızı nasıl olacak da
sağlayacak?

Aslında bunun cevabı ve mantığı çok basit. Gördüğünüz gibi, bu sistemde iki
farklı durum söz konusu: Loş ışık ve parlak ışık (veya yanan ampul ve sönmüş
ampul). 

Bu ikili yapıyı, tahmin edebileceğiniz gibi, ikili (*binary*) sayma sistemi
aracılığıyla rahatlıkla temsil edebiliriz. Mesela loş ışık durumuna `0`, parlak
ışık durumuna ise `1` diyebiliriz. Dolayısıyla verici, ampulün loş ışık
vermesini sağlayacak düşük bir akım gönderdiğinde bunun değerini `0`, ampulün
yüksek ışık vermesini sağlayacak yüksek bir akım gönderdiğinde ise bunun
değerini `1` olarak değerlendirebiliriz.

Burada yaptığımız dönüştürme işlemine teknik olarak 'kodlama' (*encoding*) adı
verilir. Bu kodlama sistemine göre biz, iki farklı elektrik akımı değerini, yani
loş ışık ve parlak ışık değerlerini sırasıyla ikili sistemdeki `0` ve `1`
sayıları ile eşleştirip, loş ışığa `0`, parlak ışığa ise `1` dedik.

Hemen anlayacağınız gibi, bahsettiğimiz bu hayali sistem, telgraf iletişimine
çok benziyor. İşte gerçekte de kullanılan telgraf sistemine çok benzeyen bu
basitleştirilmiş model bizim bilgisayarların çalışma mantığını da daha net bir
şekilde anlamamızı sağlayacak.

8 Bitlik bir Sistem
********************

Hatırlarsanız ikili sayma sisteminde `0`'lar ve `1`'lerin oluşturduğu her bir
basamağa 'bit' adını veriyorduk. 

.. note:: *Bit* kelimesi İngilizcede '**bi**\ nary' (ikili) ve 'digi\ **t**' (rakam)
          kelimelerinin birleştirilmesi ile üretilmiştir.

Bu bilgiye göre mesela `0` sayısı bir bitlik bir sayı iken, `1001` sayısı dört
bitlik bir sayıdır. İletişimimizi eksiksiz bir biçimde sağlayabilmemiz, yani
gereken bütün karakterleri temsil edebilmemiz için, sistemimizin 8 hanelik bir
sayı kapasitesine sahip olması, yani teknik bir dille ifade etmek gerekirse
sistemimizin 8 bitlik olması herhalde yeterli olacaktır.

8 bitlik bir iletişim sisteminde `10`'a kadar şu şekilde sayabiliriz::
        
    >>> for i in range(10):
    ...     print(bin(i)[2:].zfill(8))
    ...
    00000000
    00000001
    00000010
    00000011
    00000100
    00000101
    00000110
    00000111
    00001000
    00001001
    
Verici tarafındaki kişi elindeki anahtar yardımıyla farklı kuvvetlere sahip
sinyalleri art arda göndererek yukarıda gösterildiği gibi on farklı sayıyı
alıcıya iletebilir. Sistemimizin 8 bitlik olduğunu düşünürsek karşı tarafa `0`
sayısı ile birlikte toplam 2 ** 8 = 256 farklı sinyal gönderebiliriz::
    
    >>> for i in range(256):
    ...     print(bin(i)[2:].zfill(8))
    
    00000000
    00000001
    00000010
    00000011
    00000100
    ...
    ...
    ...
    11111001
    11111010
    11111011
    11111100
    11111101
    11111110
    11111111
    
Gördüğünüz gibi, bizim 8 bitlik bu sistemle gönderebileceğimiz son sinyal, yani
sayı `255`'tir. Bu sistemle bundan büyük bir sayıyı gönderemeyiz. Bu durumu
kendi gözlerinizle görmek için şu kodları çalıştırın::
    
    >>> for i in range(256):
    ...     print(bin(i)[2:], i.bit_length(), sep="\t")
    
Burada ilk sütun `256`'ya kadar olan sayıların ikili sistemdeki karşılıklarını,
ikinci sütun ise bu sayıların bit uzunluğunu gösteriyor. Bu çıktıyı
incelediğinizde de göreceğiniz gibi, 8 bit uzunluğa sahip son sayı `255`'tir.
`256` sayısı ise 9 bit uzunluğa sahiptir. Yani `256` sayısı mecburen bizim
sistemimizin dışındadır::
    
    >>> bin(255)[2:]
    
    '11111111'
    
    
    >>> (255).bit_length()
    
    8
    
    >>> bin(256)[2:]

    '100000000'
    
    >>> (256).bit_length()
    
    9
    
Dediğimiz gibi, bu sistemde elimizde toplam 8 bit var. Yani bu sistemi kullanarak
`0`'dan `256`'ya kadar sayıp, bu sayıları alıcıya iletebiliriz. 

Peki verici ile alıcı arasında birtakım sayıları gönderip alabilmek ne işimize
yarar? Yani bu iş neden bu kadar önemli? 

Bu soruların cevabını birazdan vereceğiz, ama ondan önce daha önemli bir konuya
değinelim.

Hata Kontrolü
***************

Buraya kadar her şey yolunda. Alıcı ve verici arasındaki iletişimi elektrik
akımı vasıtasıyla, 8 bitlik bir sistem üzerinden sağlayabiliyoruz. Ancak
sistemimizin çok önemli bir eksiği var. Biz bu sistemde hiçbir hata kontrolü
yapmıyoruz. Yani vericiden gelen mesajın doğruluğunu test eden hiçbir ölçütümüz
yok. Zira alıcı ile verici arasında gidip gelen veriler pek çok farklı şekilde
ve sebeple bozulmaya uğrayabilir. Örneğin, gönderilen veri alıcı tarafından
doğru anlaşılamayabilir veya elektrik sinyallerini ileten kablolardaki arızalar
sinyallerin doğru iletilmesini engelleyebilir.

İşte bütün bunları hesaba katarak, iletişimin doğru bir şekilde
gerçekleşebilmesini sağlamak amacıyla sistemimiz için basit bir hata kontrol
süreci tasarlayalım.

Dediğimiz gibi, elimizdeki sistem toplam `256`'ya kadar saymamıza olanak
tanıyor. Çünkü bizim sistemimiz 8 bitlik bir sistem. Bu sisteme bir hata kontrol
mekanizması ekleyebilmek için veri iletimini 8 bitten 7 bite çekeceğiz. Yani
iletişimimizi toplam 2 ** 7 = 127 sayı ile sınırlayacağız. Boşta kalan 8. biti
ise bahsettiğimiz bu hata kontrol mekanizmasına ayıracağız.

Peki hata kontrol mekanizmamız nasıl işleyecek? 

Çok basit: Vericiden alıcıya ulaşan verilerin tek mi yoksa çift mi olduğuna
bakacağız. 

Buna göre sistemimiz şöyle çalışacak:

Diyelim ki verici alıcıya sinyaller aracılığıyla şu sayıyı göndermek istiyor::
    
    0110111
    
Bu arada, bunun 7 bitlik bir sayı olduğuna dikkat edin. Dediğimiz gibi, biz
kontrol mekanizmamızı kurabilmek için elimizdeki 8 bitlik kapasitenin 7 bitini
kullanacağız. Boşta kalan 8. biti ise kontrol mekanizmasına tahsis edeceğiz. 

Ne diyorduk? Evet, biz karşı tarafa 7 bitlik bir sayı olan `0110111` sayısını
göndermek istiyoruz. Bu sayıyı göndermeden önce, içindeki `1`'lerin miktarına
bakarak bu sayının tek mi yoksa çift mi olduğuna karar verelim. Burada toplam
beş adet `1` sayısı var. Yani bu sayı bir tek sayıdır. Eğer göndermek
istediğimiz sayı bir tek sayı ise, karşı tarafa ulaştığında da bir tek sayı
olmalıdır. 

Biz bu sistem için şöyle bir protokol tasarlayabiliriz:

    Bu sistemde bütün sayılar karşı tarafa bir 'tek sayı' olarak iletilmelidir.
    Eğer iletilen sayılar arasında bir çift sayı varsa, o sayı hatalı iletilmiş
    veya iletim esnasında bozulmuş demektir. 
    
Peki biz iletilen bütün sayıların bir tek sayı olmasını nasıl sağlayacağız? İşte
bu işlemi, boşa ayırdığımız o 8. bit ile gerçekleştireceğiz:

    Eğer karşı tarafa iletilen bir sayı zaten tekse, o sayının başına `0`
    ekleyeceğiz. Böylece sayının teklik-çiftlik durumu değişmemiş olacak. Ama eğer
    iletilecek sayı çiftse, o sayının başına `1` ekleyeceğiz. Böylece çift sayıyı,
    sistemimizin gerektirdiği şekilde, tek sayıya çevirmiş olacağız.

Örnek olarak `0110111` sayısını verelim. Bu sayıda toplam beş adet `1` var. Yani
bu sayı bir tek sayı. Dolayısıyla bu sayının başına bir adet `0` ekliyoruz::
    
    0 0110111
    
Böylece sayımızın teklik-çiftlik durumu değişmemiş oluyor. Karşı taraf bu sayıyı
aldığında `1`'lerin miktarına bakarak bu verinin doğru iletildiğinden emin
oluyor. 

Bir de şu sayıya bakalım::
    
    1111011
    
Bu sayıda toplam altı adet `1` sayısı var. Yani bu sayı bir çift sayı. Bir
sayının sistemimiz tarafından 'hatasız' olarak kabul edilebilmesi için bu
sayının bir tek sayı olması gerekiyor. Bu yüzden biz bu sayıyı tek sayıya
çevirmek için başına bir adet `1` sayı ekliyoruz::
    
    1 1111011
    
Böylece sayımızın içinde toplam yedi adet `1` sayısı olmuş ve böylece sayımız
tek sayıya dönüşmüş oluyor. 

Teknik olarak ifade etmemiz gerekirse, yukarıda yaptığımız kontrol türüne 'eşlik
denetimi' (*parity check*) adı verilir. Bu işlemi yapmamızı sağlayan bit'e ise
'eşlik biti' (*parity bit*) denir. İki tür eşlik denetimi bulunur: 

    #. Tek eşlik denetimi (*odd parity check*)
    #. Çift eşlik denetimi (*even parity check*)
    
Biz kendi sistemimizde hata kontrol mekanizmasını bütün verilerin bir 'tek sayı'
olması gerekliliği üzerine kurduk. Yani burada bir 'tek eşlik denetimi'
gerçekleştirmiş olduk. Elbette bütün verilerin bir çift sayı olması gerekliliği
üzerine de kurabilirdik bu sistemi. Yani isteseydik 'çift eşlik denetimi' de
yapabilirdik. Bu tamamen bir tercih meselesidir. Bu tür sistemlerde yaygın
olarak 'tek eşlik denetimi' kullanıldığı için biz de bunu tercih ettik.

Bu örneklerden de gördüğünüz gibi, toplam 8 bitlik kapasitemizin 7 bitini veri
aktarımı için, kalan 1 bitini ise alınıp verilen bu verilerin doğruluğunu
denetlemek için kullanıyoruz. Elbette kullandığımız hata kontrol mekanizması
epey zayıf bir sistemdir. Ama, iletişim sistemleri arasında verilerin hatasız
bir şekilde aktarılıp aktarılamadığını kontrol etmeye yarayan bir sistem olan
eşlik denetiminin, bugün bilgisayarın belleklerinde (RAM) dahi kullanılmaya
devam ettiğini söylemeden geçmeyelim...

Karakterlerin Temsili
***********************

Yukarıda anlattıklarımızdan da gördüğünüz gibi, sistemimizi kullanarak 7 bit
üzerinden toplam 127 sayı gönderebiliyoruz. Tabii ki sistemimiz 8 bit olduğu
için 1 bit de boşta kalıyor. İşte boşta duran bu 1 biti ise eşlik denetimi için
kullanıyoruz. Ama elbette alıcı ile verici arasında sayı alışverişi yapmak pek
de heyecan uyandırıcı bir faaliyet değil. Karşı tarafa sayısal mesajlar yerine
birtakım sözel mesajlar iletebilsek herhalde çok daha keyifli olurdu...

Şunu asla unutmayın. Eğer bir noktadan başka bir noktaya en az iki farklı sinyal
yolu ile birtakım sayısal verileri gönderebiliyorsanız aynı şekilde sözel
verileri de rahatlıkla gönderebilirsiniz. Tıpkı düşük voltaj ve yüksek voltaj
değerlerini sırasıyla `0` ve `1` sayıları ile temsil ettiğiniz gibi,
karakterleri de bu iki sayı ile temsil edebilirsiniz. Yapmanız gereken tek şey
hangi sayıların hangi karakterlere karşılık geleceğini belirlemekten ibarettir.
Mesela elimizde sayılarla karakterleri eşleştiren şöyle bir tablo olduğunu
varsayalım:

   +--------+----------+---------+----------+---------+-----------+--------+----------+
   | sayı   | karakter | sayı    | karakter | sayı    | karakter  | sayı   | karakter |
   +========+==========+=========+==========+=========+===========+========+==========+
   | 0      | 'a'      | 1       | 'b'      | 10      | 'c'       | 11     | 'd'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+
   | 100    | 'e'      | 101     | 'f'      | 110     | 'g'       | 111    | 'h'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 1000   | 'i'      | 1001    | 'j'      | 1010    | 'k'       | 1011   | 'l'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 1100   | 'm'      | 1101    | 'n'      | 1110    | 'o'       | 1111   | 'p'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 10000  | 'q'      | 10001   | 'r'      | 10010   | 's'       | 10011  | 't'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 10100  | 'u'      | 10101   | 'v'      | 10110   | 'w'       | 10111  | 'x'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 11000  | 'y'      | 11001   | 'z'      | 11010   | 'A'       | 11011  | 'B'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 11100  | 'C'      | 11101   | 'D'      | 11110   | 'E'       | 11111  | 'F'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 100000 | 'G'      | 100001  | 'H'      | 100010  | 'I'       | 100011 | 'J'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 100100 | 'K'      | 100101  | 'L'      | 100110  | 'M'       | 100111 | 'N'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 101000 | 'O'      | 101001  | 'P'      | 101010  | 'Q'       | 101011 | 'R'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 101100 | 'S'      | 101101  | 'T'      | 101110  | 'U'       | 101111 | 'V'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+    
   | 110000 | 'W'      | 110001  | 'X'      | 110010  |  'Y'      | 110011 | 'Z'      |
   +--------+----------+---------+----------+---------+-----------+--------+----------+

    
Bu tabloda toplam `52` karakter ile `52` sayı birbiriyle eşleştirilmiş durumda.
Mesela vericiden `0` sinyali geldiğinde bu tabloya göre biz bunu 'a' harfi
olarak yorumlayacağız. Örneğin karşı tarafa 'python' mesajını iletmek için
sırasıyla şu sinyalleri göndereceğiz::
    
    1111, 11000, 10011, 111, 1110, 1101
    
Gördüğünüz gibi, elimizdeki 127 sayının 52'sini harflere ayırdık ve elimizde 75
tane daha sayı kaldı. Eğer isterseniz geri kalan bu sayıları da birtakım başka
karakterlere veya işaretlere ayırarak, alıcı ve verici arasındaki bütün
iletişimin eksiksiz bir şekilde gerçekleşmesini sağlayabilirsiniz. Örneğin şöyle
bir tablo oluşturabilirsiniz:

   +--------+----------+---------+----------+---------+-----------+---------+----------+
   | sayı   | karakter | sayı    | karakter | sayı    | karakter  | sayı    | karakter |
   +========+==========+=========+==========+=========+===========+=========+==========+
   | 0      |  '0'     | 1       | '1'      | 10      | '2'       | 11      | '3'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 100    |  '4'     | 101     | '5'      | 110     | '6'       | 111     | '7'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+    
   | 1000   |  '8'     | 1001    | '9'      | 1010    | 'a'       | 1011    | 'b'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+  
   | 1100   |  'c'     | 1101    | 'd'      | 1110    | 'e'       | 1111    | 'f'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 10000  |  'g'     | 10001   | 'h'      | 10010   | 'i'       | 10011   | 'j'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 10100  |  'k'     | 10101   | 'l'      | 10110   | 'm'       | 10111   | 'n'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 11000  |  'o'     | 11001   | 'p'      | 11010   | 'q'       | 11011   | 'r'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 11100  |  's'     | 11101   | 't'      | 11110   | 'u'       | 11111   | 'v'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+  
   | 100000 |  'w'     | 100001  | 'x'      | 100010  | 'y'       | 100011  | 'z'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 100100 |  'A'     | 100101  | 'B'      | 100110  | 'C'       | 100111  | 'D'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 101000 |  'E'     | 101001  | 'F'      | 101010  | 'G'       | 101011  | 'H'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 101100 |  'I'     | 101101  | 'J'      | 101110  | 'K'       | 101111  | 'L'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 110000 |  'M'     | 110001  | 'N'      | 110010  | 'O'       | 110011  | 'P'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 110100 |  'Q'     | 110101  | 'R'      | 110110  | 'S'       | 110111  | 'T'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+    
   | 111000 |  'U'     | 111001  | 'V'      | 111010  | 'W'       | 111011  | 'X'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 111100 |  'Y'     | 111101  | 'Z'      | 111110  | '!'       | 111111  | '"'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+  
   | 1000000|  '#'     | 1000001 | '$'      | 1000010 | '%'       | 1000011 | '&'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 1000100|  "'"'    | 1000101 |''('      | 1000110 |')'        | 1000111 | '*'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+
   | 1001000|  '+'     | 1001001 | ','      | 1001010 | '-'       | 1001011 | '.'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 1001100|  '/'     | 1001101 | ':'      | 1001110 | ';'       | 1001111 | '<'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+   
   | 1010000|  '='     | 1010001 | '>'      | 1010010 | '?'       | 1010011 | '@'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 1010100|  '['     | 1010101 | '\\'     | 1010110 | ']'       | 1010111 | '^'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+ 
   | 1011000|  '_'     | 1011001 | ''       | 1011010 | '{'       | 1011011 | ''       |
   +--------+----------+---------+----------+---------+-----------+---------+----------+  
   | 1011100|  '}'     | 1011101 | '~'      | 1011110 | ' '       | 1011111 | 't'      |
   +--------+----------+---------+----------+---------+-----------+---------+----------+    
   | 1100000|  '\n'    | 1100001 | '\r'     | 1100010 | '\x0b'    | 1100011 | '\x0c'   |
   +--------+----------+---------+----------+---------+-----------+---------+----------+

Aslında yukarıda anlattığımız sayı-karakter eşleştirme işleminin, ta en başta
yaptığımız sinyal-sayı eşleştirme işlemiyle mantık olarak aynı olduğuna
dikkatinizi çekmek isterim.

Sistemimizi tasarlarken, iletilen iki farklı sinyali `0` ve `1` sayıları ile
temsil etmiştik. Yani bu sinyalleri `0` ve `1`'ler halinde kodlamıştık. Şimdi
ise bu sayıları karakterlere dönüştürüyoruz. Yani yine bir kodlama (*encoding*)
işlemi gerçekleştiriyoruz.

Baştan beri anlattığımız bu küçük iletişim modeli, sayıların ve karakterlerin
nasıl temsil edilebileceği konusunda bize epey bilgi verdi. Bu arada, yukarıda
anlattığımız sistem her ne kadar hayali de olsa, bu sisteme benzeyen sistemlerin
tarih boyunca kullanıldığını ve hatta bugün kullandığımız bütün iletişim
sistemlerinin de yukarıda anlattığımız temel üzerinde şekillendiğini belirtmeden
geçmeyelim. Örneğin telgraf iletişiminde kullanılan Mors alfabesi yukarıda tarif
ettiğimiz sisteme çok benzer. Mors alfabesi, kısa ve uzun sinyallerle
karakterlerin eşleştirilmesi yoluyla oluşturulmuştur. Mors sisteminde farklı
sinyaller (tıpkı bizim sistemimizde olduğu gibi) farklı harflere karşılık gelir:

    .. image:: ../images/misc/morse.png
       :target: _images/morse.png
       :align: center 
       :width: 400px
       :height: 400px

Mors alfabesinin bizim oluşturduğumuz sisteme mantık olarak ne kadar benzediğine
dikkat edin. Bu sistemin benzeri biraz sonra göstereceğimiz gibi, modern
bilgisayarlarda da kullanılmaktadır.
