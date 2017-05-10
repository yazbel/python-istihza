.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

***********************************
Nesne Tabanlı Programlama (OOP)
***********************************

Bu bölümde, programlama faaliyetlerimizin önemli bir kısmını oluşturacak olan
nesne tabanlı programlama yaklaşımına bir giriş yaparak, bu yaklaşımın temel
kavramlarından biri olan sınıflara değineceğiz. Bu bölümde amacımız, sınıflar
üzerinden hem nesne tabanlı programlamayı tanımak, hem bu yaklaşıma ilişkin
temel bilgileri edinmek, hem de etrafımızda gördüğümüz nesne tabanlı yapıların
büyük çoğunluğunu anlayabilecek seviyeye gelmek olacaktır. Bu bölümü
tamamladıktan sonra, nesne tabanlı programlamayı orta düzeyde bildiğimizi iddia
edebileceğiz.

Giriş
******

Şimdiye kadar Python programlama dili ile ilgili olarak gördüğümüz konulardan
öğrendiğimiz çok önemli bir bilgi var: Aslına bakarsak, bu programlama dilinin
bütün felsefesi, 'bir kez yazılan kodların en verimli şekilde tekrar tekrar
kullanılabilmesi,' fikrine dayanıyor. 

Şimdi bir geriye dönüp baktığımızda, esasında bu fikrin izlerini ta ilk
derslerimize kadar sürebiliyoruz. Mesela değişkenleri ele alalım. Değişkenleri
kullanmamızdaki temel gerekçe, bir kez yazdığımız bir kodu başka yerlerde
rahatça kullanabilmek. Örneğin, ``isim = 'Uzun İhsan Efendi'`` gibi bir
tanımlama yaptıktan sonra, bu `isim` değişkeni aracılığıyla `'Uzun İhsan
Efendi'` adlı karakter dizisini her defasında tekrar tekrar yazmak zorunda
kalmadan, kodlarımızın her yanında kullanabiliyoruz.

Aynı fikrin fonksiyonlar ve geçen bölümde incelediğimiz modüller için de geçerli
olduğunu bariz bir şekilde görebilirsiniz. Gömülü fonksiyonlar, kendi
tanımladığımız fonksiyonlar, hazır modüller, üçüncü şahıs modülleri hep belli
bir karmaşık süreci basitleştirme, bir kez tanımlanan bir prosedürün tekrar
tekrar kullanılabilmesini sağlama amacı güdüyor. 

İşte bu fikir nesne tabanlı programlama ve dolayısıyla 'sınıf' (*class*) adı
verilen özel bir veri tipi için de geçerlidir. Bu bölümde, bunun neden ve nasıl
böyle olduğunu bütün ayrıntılarıyla ele almaya çalışacağız.

Bu arada, İngilizcede *Object Oriented Programming* olarak ifade edilen
programlama yaklaşımı, Türkçede 'Nesne Tabanlı Programlama', 'Nesne Yönelimli
Programlama' ya da 'Nesneye Yönelik Programlama' olarak karşılık bulur. Biz bu
karşılıklardan, adı 'Nesne Tabanlı Programlama' olanı tercih edeceğiz.

Unutmadan, nesne tabanlı programlamaya girmeden önce değinmemiz gereken bir şey
daha var. Eğer öğrendiğiniz ilk programlama dili Python ise, nesne tabanlı
programlamayı öğrenmenin (aslında öyle olmadığı halde) zor olduğunu düşünebilir,
bu konuyu biraz karmaşık bulabilirsiniz. Bu durumda da kaçınılmaz olarak kendi
kendinize şu soruyu sorarsınız: Acaba ben nesne tabanlı programlamayı öğrenmek
zorunda mıyım?

Bu sorunun kısa cevabı, eğer iyi bir programcı olmak istiyorsanız nesne tabanlı
programlamayı öğrenmek zorundasınız, olacaktır.

Uzun cevap ise şu: 

Nesne tabanlı programlama, pek çok yazılım geliştirme yönteminden yalnızca
biridir. Siz bu yöntemi, yazdığınız programlarda kullanmak zorunda değilsiniz.
Nesne tabanlı programlamadan hiç yararlanmadan da faydalı ve iyi programlar
yazabilirsiniz elbette. Python sizi bu yöntemi kullanmaya asla zorlamaz. Ancak
nesne tabanlı programlama yaklaşımı program geliştirme alanında oldukça yaygın
kullanılan bir yöntemdir. Dolayısıyla, etrafta nesne tabanlı programlama
yaklaşımından yararlanılarak yazılmış pek çok kodla karşılaşacaksınız. Hiç
değilse karşılaştığınız bu kodları anlayabilmek için nesne tabanlı programlamayı
biliyor ve tanıyor olmanız lazım. Aksi halde, bu yöntem kullanılarak
geliştirilmiş programları anlayamazsınız.

Mesela, grafik bir arayüze sahip (yani düğmeli, menülü) programların ezici
çoğunluğu nesne tabanlı programlama yöntemiyle geliştiriliyor. Grafik arayüz
geliştirmenizi sağlayacak araçları tanımanızı, öğrenmenizi sağlayan kitaplar ve
makaleler de bu konuları hep nesne tabanlı programlama yaklaşımı üzerinden
anlatıyor.

.. warning:: Yalnız bu söylediğimizden, nesne tabanlı programlama sadece grafik
 arayüzlü programlar geliştirmeye yarar gibi bir anlam çıkarmamalısınız. Nesne
 tabanlı programlama, komut arayüzlü programlar geliştirmek için de kullanışlı
 bir programlama yöntemidir.

Sözün özü, nesne tabanlı programlamadan kaçamazsınız! İyi bir programcı olmak
istiyorsanız, kendiniz hiç kullanmasanız bile, nesne tabanlı programlamayı
öğrenmek zorundasınız. Hem şimdi nesne tabanlı programlamaya dudak bükseniz
bile, bunu kullandıkça ve size sağladığı faydaları gördükçe onu siz de
seveceksiniz...

Sınıflar
*********

Nesne tabanlı programlamanın temelinde, yukarıdaki giriş bölümünde de adını
andığımız 'sınıf' (*class*) adlı bir kavram bulunur. Bu bölümde, bu temel
kavramı hakkıyla ele almaya çalışacağız.

Peki tam olarak nedir bu sınıf denen şey?

Çok kaba ve oldukça soyut bir şekilde tanımlayacak olursak, sınıflar, nesne
üretmemizi sağlayan veri tipleridir. İşte nesne tabanlı programlama, adından da
anlaşılacağı gibi, nesneler (ve dolayısıyla sınıflar) temel alınarak
gerçekleştirilen bir programlama faaliyetidir.

'Hiçbir şey anlamadım!' dediğinizi duyar gibiyim. Çünkü yukarıdaki tanım,
'nesne' ne demek, 'sınıf' ne anlama geliyor gibi sorulara cevap vermiyor. Yani
programcılık açısından 'nesne' ve 'sınıf' kelimelerini burada ne anlamda
kullandığımızı, yukarıdaki tanıma bakarak kestiremiyoruz. Eğer siz de bu
fikirdeyseniz okumaya devam edin...

Sınıflar Ne İşe Yarar?
**************************

Buraya gelene kadar Python'da pek çok veri tipi olduğunu öğrendik. Mesela önceki
derslerimizde incelediğimiz listeler, demetler, karakter dizileri, sözlükler ve
hatta fonksiyonlar hep birer veri tipidir. Bu tiplerin, verileri çeşitli
şekillerde evirip çevirmemizi sağlayan birtakım araçlar olduğunu biliyoruz. İşte
sınıflar da, tıpkı yukarıda saydığımız öteki veri tipleri gibi, verileri
manipüle etmemizi sağlayan bir veri tipidir.

Peki bu bölümde ele alacağımız 'sınıf' (*class*) veri tipi ne işe yarar? 

Dilerseniz bunu basit bir örnek üzerinde anlatmaya çalışalım.

Diyelim ki, kullanıcının girdiği bir kelimedeki sesli harfleri sayan bir kod
yazmak istiyorsunuz. Bu amacı gerçekleştirebilmek için yazabileceğiniz en basit
kod herhalde şu olacaktır::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    for harf in kelime:
        if harf in sesli_harfler:
            sayaç += 1
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, sayaç))
    
Düzgün bir şekilde çalışan, gayet basit kodlardır bunlar. Ayrıca amacımızı da
kusursuz bir şekilde yerine getirir. Üstelik kodlardaki bütün öğeler tek bir
isim/etki alanı (*namespace*, *scope*) içinde bulunduğu için, bunlara erişimde
hiçbir zorluk çekmeyiz. Yani mesela `sesli_harfler`, `sayaç`, `kelime`, `harf`,
`mesaj` değişkenlerine kodlar içinde her yerden erişebiliriz.

.. note:: Eğer isim/etki alanı ile ilgili söylediğimiz şeyi anlamadıysanız
 endişe etmeyin. Birazdan vereceğimiz örnekle durumu daha net kavrayacaksınız.

Ancak bu kodların önemli bir dezavantajı, kodlarda benimsediğimiz yaklaşımın
genişlemeye pek müsait olmamasıdır. Daha doğrusu, yukarıdaki kodlara yeni kodlar
ekledikçe programımız karmaşık hale gelecek, kodları anlamak zorlaşacaktır.

Kod yapısını biraz olsun rahatlatmak için bazı önlemler alabiliriz. Mesela
kullanıcı tarafından girilen kelimedeki bir harfin sesli olup olmadığını
denetleyen kodları bir fonksiyon içine alarak, o kısmı daha belirgin hale
getirebiliriz::

    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
    
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, sayaç))
    
Burada, kontrol ettiğimiz harfin `sesli_harfler` adlı değişken içinde bulunup
bulunmamasına göre `True` veya `False` çıktısı veren, ``seslidir()`` adlı bir
fonksiyon tanımladık. Eğer kontrol ettiğimiz harf `sesli_harfler` değişkeni
içinde geçiyorsa, yani bu bir sesli harf ise, ``seslidir()`` fonksiyonu `True`
çıktısı verecektir. Aksi durumda ise bu fonksiyondan `False` çıktısı alacağız.
Böylece sesli harf kontrolü yapmak istediğimiz her yerde yalnızca ``seslidir()``
fonksiyonunu kullanabileceğiz. Bu da bize, bir kez yazdığımız kodları tekrar
tekrar kullanma imkanı verecek.

Eğer yukarıdaki kodları daha da genel amaçlı bir hale getirmek istersek, sayacı
artıran kodları da bir fonksiyon içine almayı düşünebiliriz::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
        
    def artır():
        global sayaç
        for harf in kelime:
            if seslidir(harf):
                sayaç += 1     
        return sayaç
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, artır()))
       
Hatırlarsanız, ilk başta yazdığımız kodların en büyük avantajının, kodlarda
geçen bütün öğelerin tek bir isim/etki alanında bulunması olduğunu söylemiştik.
Bu sayede bütün öğelere her yerden erişebiliyorduk. Yukarıdaki kodlarda ise
birden fazla isim/etki alanı var:

    #. `sesli_harfler`, `sayaç`, `kelime` ve `mesaj` değişkenlerinin bulunduğu
       global isim/etki alanı.
    #. ``seslidir()`` fonksiyonunun lokal isim/etki alanı.
    #. ``artır()`` fonksiyonunun lokal isim/etki alanı.
    
Bildiğiniz gibi, global isim alanında bulunan değişkenlere her yerden
**ulaşabiliyoruz**. Ancak bunları her yerden **değiştiremiyoruz**. Yani mesela
global isim alanında bulunan `sayaç` değişkeninin değerini, ``seslidir()``
fonksiyonu içinden görüntüleyebiliriz.

Bunu teyit edelim::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    def seslidir(harf):
        print('sayaç değişkeninin değeri şu anda: ', sayaç)
        return harf in sesli_harfler
        
    def artır():
        global sayaç
        for harf in kelime:
            if seslidir(harf):
                sayaç += 1     
        return sayaç
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, artır()))
    
Gördüğünüz gibi, global isim alanındaki `sayaç` değişkeninin değerini
``seslidir()`` fonksiyonu içinde kullanabildik. Ama eğer bu değişken üzerinde
değişiklik yapacaksak ilave adımlar atmak zorundayız. Dolayısıyla, mesela
``artır()`` fonksiyonunun etki alanından, global etki alanındaki `sayaç`
değişkeni üzerinde değişiklik yapabilmek için ``global`` deyimini kullanmamız
gerekiyor. Bu şekilde, global isim alanında bulunan `sayaç` adlı değişkenin
değerini artırabiliyoruz.
    
Dikkat ederseniz, ``artır()`` fonksiyonunda iki tane global değişken var:
`sayaç` ve `kelime`. Ama biz bunlardan yalnızca `sayaç` değişkenini global
olarak belirledik. Öbür global değişkenimiz `kelime` için ise bu işlemi
yapmadık. Çünkü `kelime` adlı değişkeni değiştirmek gibi bir niyetimiz yok. Biz
bu değişkeni sadece kullanmakla yetiniyoruz. O yüzden bu değişkeni global olarak
belirlemek zorunda değiliz.

Ancak bildiğiniz gibi, ``global`` deyimini kullanmak pek tavsiye edilen bir şey
değil. Eğer siz de bu deyimi kullanmak istemezseniz, yukarıdaki kodları şu
şekilde yazmayı yeğleyebilirsiniz::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
        
    def artır(sayaç):
        for harf in kelime:
            if seslidir(harf):
                sayaç += 1     
        return sayaç
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, artır(sayaç)))
    
Gördüğünüz gibi, bu kodlarda ``global`` deyimini kullanmak yerine, ``artır()``
fonksiyonuna verdiğimiz `sayaç` parametresi üzerinden global isim alanıyla
iletişim kurarak, `sayaç` değişkenini manipüle edebildik. Sadece değerini
kullandığımız global değişken `kelime` için ise özel bir şey yapmamıza gerek
kalmadı.

Bu arada, tabii ki, ``artır()`` fonksiyonunda parametre olarak kullandığımız
kelime `sayaç` olmak zorunda değil. Kodlarımızı mesela şöyle de yazabilirdik::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    kelime = input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
        
    def artır(n):
        for harf in kelime:
            if seslidir(harf):
                n += 1     
        return n
          
    mesaj = '{} kelimesinde {} sesli harf var.'
    print(mesaj.format(kelime, artır(sayaç)))
        
Önemli olan, ``artır()`` fonksiyonunun, bizim global isim alanıyla iletişim
kurmamızı sağlayacak bir parametre alması. Bu parametrenin adının ne olduğunun
bir önemi yok.

Yukarıdaki kodlarda birkaç değişiklik daha yaparak, bu kodları iyice
genişletilebilir hale getirebiliriz::
     
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    def kelime_sor():
        return input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
    
    def artır(sayaç, kelime):
        for harf in kelime:
            if seslidir(harf):
                sayaç += 1
        return sayaç
    
    def ekrana_bas(kelime):
        mesaj = "{} kelimesinde {} sesli harf var."
        print(mesaj.format(kelime, artır(sayaç, kelime)))
    
    def çalıştır():
        kelime = kelime_sor()
        ekrana_bas(kelime)
    
    çalıştır()
    
Bu kodlarda, fonksiyonlara verdiğimiz parametreler yardımıyla, farklı
fonksiyonların lokal etki alanlarında yer alan öğeler arasında nasıl iletişim
kurduğumuza dikkat edin. Bir önceki kodlarda global etki alanında bulunan
`kelime` değişkenini bu kez ``çalıştır()`` fonksiyonunun lokal etki alanı içine
yerleştirdiğimiz için, ``artır()`` fonksiyonu içindeki `kelime` değişkeni boşa
düştü. O yüzden, bu değişkeni ``artır()`` fonksiyonuna bir parametre olarak
verdik ve ``ekrana_bas()`` fonksiyonu içinde bu fonksiyonu çağırırken, hem
`sayaç` hem de `kelime` argümanlarını kullandık.

Ayrıca, kullanıcıya kelime sorup, aldığı kelimeyi ekrana basan kod parçalarını,
yani programımızı başlatan kodları ``çalıştır()`` başlığı altında toplayarak bu
kısmı tam anlamıyla 'modüler', yani esnek ve takılıp çıkarılabilir bir hale
getirdik.

Gördüğünüz gibi, yazdığımız kodların olabildiğince anlaşılır ve yönetilebilir
olmasını sağlayabilmek için, bu kodları küçük birtakım birimlere böldük. Bu
şekilde hem hangi işlevin nerede olduğunu bulmak kolaylaştı, hem kodların
görünüşü daha anlaşılır oldu, hem de bu kodlara ileride yeni özellikler eklemek
basitleşti. Unutmayın, bir programcının görevi yalnızca çalışan kodlar yazmak
değildir. Programcı aynı zamanda kodlarının okunaklılığını artırmak ve bakımını
kolaylaştırmakla da yükümlüdür.

Bu bakımdan, programcı ile kod arasındaki ilişkiyi, yazar ile kitap arasındaki
ilişkiye benzetebilirsiniz. Tıpkı bir programcı gibi, yazarın da görevi aklına
gelenleri bir kağıda gelişigüzel boca etmek değildir. Yazar, yazdığı kitabın
daha anlaşılır olmasını sağlamak için kitabına bir başlık atmalı, yazdığı
yazıları alt başlıklara ve paragraflara bölmeli, ayrıca noktalama işaretlerini
yerli yerinde kullanarak yazılarını olabildiğince okunaklı hale getirmelidir.
Bir ana başlığı ve alt başlıkları olmayan, sadece tek bir büyük paragraftan
oluşan, içinde hiçbir noktalama işaretinin kullanılmadığı bir makaleyi okumanın
veya bu makaleye sonradan yeni bir şeyler eklemenin ne kadar zor olduğunu
düşünün. İşte aynı şey bir programcının yazdığı kodlar için de geçerlidir. Eğer
yazdığınız kodları anlaşılır birimlere bölmeden ekrana yığarsanız bu kodları ne
başkaları okuyup anlayabilir, ne de siz ileride bu kodlara yeni işlevler
ekleyebilirsiniz.

Python programlama dili, kodlarınızı olabildiğince anlaşılır, okunaklı ve
yönetilebilir hale getirmeniz için size pek çok araç sunar. Önceki derslerde
gördüğümüz değişkenler, fonksiyonlar ve modüller bu araçlardan yalnızca
birkaçıdır. İşte bu bölümde inceleyeceğimiz sınıflar da kodlarımızı
ehlileştirmek için kullanacağımız son derece faydalı araçlardır.

Birazdan, 'sınıf' denen bu faydalı araçları enine boyuna inceleyeceğiz. Ama
gelin isterseniz, anlatmaya devam etmeden önce, verdiğimiz son kodları biraz
daha kurcalayalım.

Hatırlarsanız, geçen bölümde, yazdığımız Python kodlarının aynı zamanda hem
bağımsız bir program olarak hem de bir modül olarak kullanılabileceğini
söylemiştik.

Mesela, yukarıdaki kodları `sayac.py` adlı bir dosyaya kaydettiğimizi
varsayarsak, bu programı komut satırı üzerinden ``python sayac.py`` gibi bir
kodla çalıştırabiliyoruz. Biz bu programı bu şekilde komut satırı üzerinden veya
üzerine çift tıklayarak çalıştırdığımızda, bu kodları bağımsız bir program
olarak çalıştırmış oluyoruz. Gelin bir de bu kodları bir modül olarak nasıl içe
aktaracağımızı inceleyelim.

Şimdi, `sayac.py` programının bulunduğu dizin altında Python komut satırını
başlatalım ve orada şu komutu vererek `sayac` modülünü içe aktaralım::
    
    >>> import sayac
    
Bu komutu verdiğimiz anda, `sayac.py` programı çalışmaya başlayacaktır. Ancak
bizim istediğimiz şey bu değil. Biz `sayac.py` programının çalışmaya başlamasını
istemiyoruz. Bizim istediğimiz şey, bu `sayac.py` dosyasını bağımsız bir program
olarak değil, bir modül olarak kullanmak ve böylece bu modül içindeki nitelik ve
fonksiyonlara erişmek. Tam bu noktada şöyle bir soru aklımıza geliyor: Acaba bir
insan neden bir programı modül olarak içe aktarmak istiyor olabilir?

Bir Python dosyasına modül olarak erişmek istemenizin birkaç sebebi olabilir.
Mesela bir program yazıyorsunuzdur ve amacınız yazdığınız kodların düzgün
çalışıp çalışmadığını test etmektir. Bunun için, programınızı etkileşimli kabuk
ortamına bir modül olarak aktarıp, bu modülün test etmek istediğiniz kısımlarını
tek tek çalıştırabilirsiniz. Aynı şekilde, kendi yazdığınız veya başkası
tarafından yazılmış bir program içindeki işlevsellikten başka bir program içinde
de yararlanmak istiyor olabilirsiniz. İşte bunun için de, ilgili programı, başka
bir program içinden çağırarak, yani o programı öteki program içine bir modül
olarak aktararak, ilgili modül içindeki işlevleri kullanabilirsiniz.

Diyelim ki biz, yukarıda yazdığımız `sayac.py` adlı dosya içindeki kodların
düzgün çalışıp çalışmadığını kontrol etmek istiyoruz. Bunun için `sayac.py`
dosyasındaki kodlarda şu değişikliği yapalım::
    
    sesli_harfler = 'aeıioöuü'
    sayaç = 0
    
    def kelime_sor():
        return input('Bir kelime girin: ')
    
    def seslidir(harf):
        return harf in sesli_harfler
    
    def artır(sayaç, kelime):
        for harf in kelime:
            if seslidir(harf):
                sayaç += 1
        return sayaç
    
    def ekrana_bas(kelime):
        mesaj = "{} kelimesinde {} sesli harf var."
        print(mesaj.format(kelime, artır(sayaç, kelime)))
    
    def çalıştır():
        kelime = kelime_sor()
        ekrana_bas(kelime)
    
    if __name__ == '__main__':
        çalıştır()
        
Gördüğünüz gibi, burada ``çalıştır()`` fonksiyonunu ``if __name__ ==
'__main__'`` bloğuna aldık. Buna göre, eğer `__name__` niteliğinin değeri
`'__main__'` ise ``çalıştır()`` fonksiyonu işlemeye başlayacak. Aksi halde
herhangi bir şey olmayacak.

Şimdi `sayac.py` programını komut satırı üzerinden ``python sayac.py`` gibi bir
komutla çalıştırın. Programınız normal bir şekilde çalışacaktır. Çünkü,
bildiğiniz gibi, bir Python programı bağımsız bir program olarak
çalıştırıldığında `__name__` niteliğinin değeri `'__main__'` olur.
Dolayısıyla da ``çalıştır()`` fonksiyonu işlemeye başlar.

Şimdi de etkileşimli kabuğu tekrar açın ve şu komutu vererek modülü içe
aktarın::
    
    >>> import sayac
    
Bu defa programımız çalışmaya başlamadı. Çünkü bu kez, programımızı bir modül
olarak içe aktardığımız için, `__name__` niteliğinin değeri `'__main__'` değil,
ilgili modülün adı oldu (yani bizim örneğimizde `sayac`). 

Böylece `__name__` niteliğinin farklı durumlarda farklı bir değere sahip
olmasından yararlanarak, programınızın farklı durumlarda farklı tepkiler
vermesini sağlamış olduk.

`sayac` modülünü içe aktardıktan sonra, bu modülün içinde neler olduğunu nasıl
kontrol edebileceğinizi biliyorsunuz::
    
    >>> dir(sayac)
    
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
     '__name__', '__package__', '__spec__', 'artır', 'ekrana_bas', 
     'kelime_sor', 'sayaç', 'sesli_harfler', 'seslidir', 'çalıştır']
     
Bu listede, `sayac` modülüne ait bütün nitelik ve fonksiyonları görebiliyoruz.
Bunları, başka modüllerde olduğu gibi kullanma imkanına sahibiz.

Mesela bu listede görünen ``seslidir()`` fonksiyonunu kullanalım::
    
    >>> sayac.seslidir('ö')
    
    True
    
    >>> sayac.seslidir('ç')
    
    False
    
Gördüğünüz gibi, `sayac.py` içinde tanımladığımız ``seslidir()`` fonksiyonunu,
rastgele harflerin birer sesli harf olup olmadığını denetlemek için de
kullanabiliyoruz. Bu şekilde aynı zamanda ``seslidir()`` fonksiyonunun düzgün
bir şekilde çalışıp çalışmadığını, sesli olan ve olmayan harfleri başarılı bir
şekilde birbirinden ayırt edip edemediğini de test etmiş oluyoruz.

Devam edelim::
    
    >>> sayac.sesli_harfler
    
    'aeıioöuü'
    
Modüllerin ne kadar faydalı araçlar olabileceğini bu örnek gayet net bir şekilde
gösteriyor. Eğer ileride sesli harfleri kullanmamızı gerektiren başka bir
program yazacak olursak, bu harfleri yeniden tanımlamak yerine, `sayac.py`
dosyasından içe aktarabiliriz. 

Bütün bu örnekler sayesinde, sınıfları daha iyi anlamamızı sağlayacak altyapıyı
oluşturmuş, bir yandan da eski bilgilerimizi pekiştirmiş olduk. Dilerseniz,
sınıfları anlatmaya geçmeden önce, yukarıda verdiğimiz kodları sınıflı bir yapı
içinde nasıl ifade edebileceğimizi de görelim.

Elbette aşağıdaki kodları anlamanızı şu aşamada sizden beklemiyoruz. Bu bölümün
sonuna vardığımızda, zihninizde her şey berraklaşmış olacak. Siz şimdilik sadece
aşağıdaki kodlara bakın ve hem okunaklılık hem de yönetilebilirlik bakımından bu
kodların bize ne gibi faydalar sağlıyor olabileceğine dair fikir yürütmeye
çalışın. Anlamadığınız kısımlar olursa bunları geçin gitsin. Anladığınız
kısımlar ise yanınıza kâr kalsın.

::
    
    class HarfSayacı:      
        def __init__(self):
            self.sesli_harfler = 'aeıioöuü'
            self.sayaç = 0
            
        def kelime_sor(self):
            return input('Bir kelime girin: ')
            
        def seslidir(self, harf):
            return harf in self.sesli_harfler
            
        def artır(self):
            for harf in self.kelime:
                if self.seslidir(harf):
                    self.sayaç += 1             
            return self.sayaç
            
        def ekrana_bas(self):
            mesaj = "{} kelimesinde {} sesli harf var."
            sesli_harf_sayısı = self.artır()
            print(mesaj.format(self.kelime, sesli_harf_sayısı))
            
        def çalıştır(self):
            self.kelime = self.kelime_sor()
            self.ekrana_bas()
    
    if __name__ == '__main__':
        sayaç = HarfSayacı()
        sayaç.çalıştır()

Hakkında herhangi bir fikre sahip olmadığınız bir kod parçasını anlamanın en iyi
yolu, anlamadığınız kısmı kodlardan çıkarıp, kodları bir de o şekilde
çalıştırmaktır. Mesela yukarıdaki `__init__`, `self` ve `class` gibi öğelerin
ismini değiştirin, bunları kodlardan çıkarın veya başka bir yere koyun. Elde
ettiğiniz sonuçları gözlemleyerek bu kodlar hakkında en azından bir fikir sahibi
olabilirsiniz. 
        
Gelin isterseniz, henüz yukarıdaki kodları anlayabilecek kadar sınıf bilgisine
sahip olmasak da, bu kodları şöyle bir üstünkörü gözden geçirerek, bu kodların
programcılık deneyimimiz açısından bize ne gibi bir katkı sunuyor olabileceğini
anlamaya çalışalım.

Yukarıdaki kodlarda dikkatimizi çeken ilk şey, bu kodların son derece derli
toplu görünüyor olmasıdır. Öyle ki, `HarfSayacı` adlı sınıf içindeki
fonksiyonlar sanki ipe dizilir gibi dizilmiş.

`HarfSayacı` adlı sınıf ile bu sınıf yapısı içinde yer alan fonksiyonlar
arasındaki ilişki gayet net bir şekilde görünüyor. Eğer ileride bu sayaca yeni
bir işlev eklemek istersek, neyi nereye yerleştirmemiz gerektiği çok açık.
Mesela ilerde bu kodlara sesli harflerle birlikte bir de sessiz harf denetim
işlevi eklemek istersek, gerekli değişiklikleri kolayca yapabiliriz::
    
    class HarfSayacı:      
        def __init__(self):
            self.sesli_harfler = 'aeıioöuü'
            self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
            self.sayaç_sesli = 0
            self.sayaç_sessiz = 0
            
        def kelime_sor(self):
            return input('Bir kelime girin: ')
            
        def seslidir(self, harf):
            return harf in self.sesli_harfler
        
        def sessizdir(self, harf):
            return harf in self.sessiz_harfler
            
        def artır(self):
            for harf in self.kelime:
                if self.seslidir(harf):
                    self.sayaç_sesli += 1 
                if self.sessizdir(harf):
                    self.sayaç_sessiz += 1
            return (self.sayaç_sesli, self.sayaç_sessiz)
            
        def ekrana_bas(self):
            sesli, sessiz = self.artır()
            mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
            print(mesaj.format(self.kelime, sesli, sessiz))
            
        def çalıştır(self):
            self.kelime = self.kelime_sor()
            self.ekrana_bas()

    if __name__ == '__main__':
        sayaç = HarfSayacı()
        sayaç.çalıştır()
    
Ayrıca sınıflı kodlarda, farklı etki alanları ile iletişim kurmak, sınıfsız
kodlara kıyasla daha zahmetsizdir. Sınıflı ve sınıfsız kodlarda fonksiyonlara
verdiğimiz parametreleri birbirleri ile kıyaslayarak bu durumu kendiniz de
görebilirsiniz.

Sınıflı yapıların daha pek çok avantajlı yönü vardır. İşte biz bu bölümde
bunları size tek tek göstermeye çalışacağız.
    
Sınıf Tanımlamak
******************

Nesne tabanlı programlama yaklaşımı, özellikle birtakım ortak niteliklere ve
davranış şekillerine sahip gruplar tanımlamak gerektiğinde son derece
kullanışlıdır. Mesela şöyle bir örnek düşünün: Diyelim ki çalıştığınız
işyerinde, işe alınan kişilerin kayıtlarını tutan bir veritabanınız var. Bir
kişi işe alındığında, o kişiye dair belli birtakım bilgileri bu veritabanına
işliyorsunuz. Mesela işe alınan kişinin adı, soyadı, unvanı, maaşı ve buna
benzer başka bilgiler...

Çalışmaya başlayacak kişileri temsil eden bir 'Çalışan' grubunu, bu grubun
nitelikleri ile faaliyetlerini tutacak yapıyı ve bu grubun bütün öğelerinin
taşıyacağı özellikleri nesne tabanlı programlama yaklaşımı ile kolayca
kodlayabilirsiniz.

Aynı şekilde, mesela yazdığınız bir oyun programı için, bir 'Asker' grubunu
nesne tabanlı programlama mantığı içinde tanımlayarak, bu grubun her bir
üyesinin sahip olacağı nitelikleri, kabiliyetleri ve davranış şekillerini
kodlayabilir; mesela askerlerin sağa sola nasıl hareket edeceklerini, hangi
durumlarda puan/enerji/güç kazanacaklarını veya kaybedeceklerini, bir asker ilk
kez oluşturulduğunda hangi özellikleri taşıyacağını ve aklınıza gelebilecek
başka her türlü özelliği tek tek belirleyebilirsiniz.

Amacınız ne olursa olsun, atmanız gereken ilk adım, ilgili sınıfı tanımlamak
olmalıdır. Zira fonksiyonlarda olduğu gibi, bir sınıfı kullanabilmek için de
öncelikle o sınıfı tanımlamamız gerekiyor. Mesela, yukarıda bahsettiğimiz işe
uygun olarak, `Çalışan` adlı bir sınıf tanımlayalım::
    
    class Çalışan:
        pass
        
Yukarıdaki, boş bir sınıf tanımıdır. Hatırlarsanız fonksiyonları tanımlamak için
`def` adlı bir ifadeden yararlanıyorduk. İşte sınıfları tanımlamak için de
`class` adlı bir ifadeden yararlanıyoruz. Bu ifadenin ardından gelen
`Çalışan` kelimesi ise bu sınıfın adıdır.

Eğer arzu ederseniz, yukarıdaki sınıfı şu şekilde de tanımlayabilirsiniz::
    
    class Çalışan():
        pass
        
Yani sınıf adından sonra parantez kullanmayabileceğiniz gibi, kullanabilirsiniz
de. Her ikisi de aynı kapıya çıkar. Ayrıca sınıf adlarında, yukarıda olduğu gibi
büyük harf kullanmak ve birden fazla kelimeden oluşan sınıf adlarının ilk
harflerini büyük yazıp bunları birleştirmek adettendir. Yani::
    
    class ÇalışanSınıfı():
        pass
        
Veya parantezsiz olarak::
    
    class ÇalışanSınıfı:
        pass
        
Gördüğünüz gibi sınıf tanımlamak fonksiyon tanımlamaya çok benziyor.
Fonksiyonları tanımlarken nasıl `def` deyimini kullanıyorsak, sınıfları
tanımlamak için de `class` deyimini kullanıyoruz.

Örnek olması açısından, yukarıda bahsettiğimiz 'Asker' grubu için de bir sınıf
tanımlayalım::
    
    class Asker:
        pass
        
... veya::
    
    class Asker():
        pass

Python'da sınıfları nasıl tanımlayacağımızı öğrendiğimize göre, bu sınıfları
nasıl kullanacağımızı incelemeye geçebiliriz.

Sınıf Nitelikleri
********************

Yukarıda, boş bir sınıfı nasıl tanımlayacağımızı öğrendik. Elbette
tanımladığımız sınıflar hep boş kalmayacak. Bu sınıflara birtakım nitelikler
ekleyerek bu sınıfları kullanışlı hale getirebiliriz. Mesela::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        
Burada `unvanı` ve `kabiliyetleri` adlı iki değişken tanımladık. Teknik
dilde bu değişkenlere 'sınıf niteliği' (*class attribute*) adı verilir. 

Biraz önce, sınıf tanımlamayı öğrenirken sınıf tanımlamanın fonksiyon
tanımlamaya çok benzediğini söylemiştik. Gerçekten de öyledir. Ancak
fonksiyonlarla sınıflar arasında (başka farkların dışında) çok önemli bir fark
bulunur. Bildiğiniz gibi, bir fonksiyonu tanımladıktan sonra, o fonksiyonun
işlemeye başlaması için, o fonksiyonun mutlaka çağrılması gerekir. Çağrılmayan
fonksiyonlar çalışmaz. Mesela yukarıdaki sınıfa benzeyen şöyle bir fonksiyon
tanımladığımızı düşünün::
    
    def çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        
        print(kabiliyetleri)
        print(unvanı)
        
Bu fonksiyonun çalışması için, kodlarımızın herhangi bir yerinde bu fonksiyonu
çağırmamız lazım::
    
    çalışan()
    
Ancak sınıflar farklıdır. Bunu görmek için yukarıdaki fonksiyonu bir sınıf
haline getirelim::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        
        print(kabiliyetleri)
        print(unvanı)
        
Bu kodları mesela `deneme.py` adlı bir dosyaya kaydedip çalıştırdığınızda,
`unvanı` ve `kabiliyetleri` değişkenlerinin değerinin ekrana
basıldığını göreceksiniz.

Aynı şey, yukarıdaki kodların bir modül olarak içe aktarıldığı durumlarda da
geçerlidir. Yani yukarıdaki kodların `deneme.py` adlı bir dosyada bulunduğunu
varsayarsak, bu modülü şu komutla içe aktardığımızda, sınıfı kodlarımızın
herhangi bir yerinde çağırmamış olmamıza rağmen sınıf içeriği çalışmaya
başlayacaktır::
    
    >>> import deneme
    
    []
    işçi

Eğer sınıf niteliklerinin ne zaman çalışacağını kendiniz kontrol etmek
isterseniz, bu nitelikleri sınıf dışında kullanabilirsiniz::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
    
    print(Çalışan.kabiliyetleri)
    print(Çalışan.unvanı)
    
Burada ``Çalışan()`` adlı sınıfın niteliklerine nasıl eriştiğimize dikkat edin.
Gördüğünüz gibi, sınıf niteliklerine erişmek için doğrudan sınıfın adını
parantezsiz bir şekilde kullanıyoruz. Eğer sınıf adlarını parantezli bir şekilde
yazarsak başka bir şey yapmış oluruz. Bundan biraz sonra bahsedeceğiz. Biz
şimdilik, sınıf niteliklerine erişmek için sınıf adlarını parantezsiz
kullanmamız gerektiğini bilelim yeter.

Hatırlarsanız, bu bölüme başlarken, nesne tabanlı programlama yaklaşımının,
özellikle birtakım ortak niteliklere ve davranış şekillerine sahip gruplar
tanımlamak gerektiğinde son derece kullanışlı olduğunu söylemiştik. Gelin
isterseniz yukarıdaki ``Çalışan()`` sınıfına birkaç nitelik daha ekleyerek bu
iddiamızı destekleyelim::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        maaşı = 1500
        memleketi = ''
        doğum_tarihi = ''
        
Burada belli `kabiliyetleri`, `unvanı`, `maaşı`, `memleketi` ve `doğum_tarihi`
olan bir ``Çalışan()`` sınıfı tanımladık. Yani 'Çalışan' adlı bir grubun ortak
niteliklerini belirledik. Elbette her çalışanın memleketi ve doğum tarihi farklı
olacağı için sınıf içinde bu değişkenlere belli bir değer atamadık. Bunların
birer karakter dizisi olacağını belirten bir işaret olması için yalnızca
`memleketi` ve `doğum_tarihi` adlı birer boş karakter dizisi tanımladık.

Yukarıda tanımladığımız sınıf niteliklerine, doğrudan sınıf adını kullanarak
erişebileceğimizi biliyorsunuz::
    
    print(Çalışan.maaşı)
    print(Çalışan.memleketi)
    print(Çalışan.doğum_tarihi)
    
Eğer isterseniz bu sınıfa yeni sınıf nitelikleri de ekleyebilirsiniz::
    
    Çalışan.isim = 'Ahmet'
    Çalışan.yaş = 40
    
Gayet güzel... 

Ancak burada şöyle bir sorun var: Biz yukarıdaki gibi doğrudan sınıf adını
kullanarak öğelere eriştiğimizde kodlarımız tek kullanımlık olmuş oluyor. Yani
bu şekilde ancak tek bir ``Çalışan()`` nesnesi ('nesne' kavramına ilerde
değineceğiz), dolayısıyla da tek bir çalışan oluşturma imkanı elde edebiliyoruz.
Ama biz, mantıken, sınıf içinde belirtilen özellikleri taşıyan, Ahmet, Mehmet,
Veli, Selim, Selin ve buna benzer, istediğimiz sayıda çalışan
oluşturabilmeliyiz. Peki ama nasıl?

Sınıfların Örneklenmesi 
************************

Biraz önce şöyle bir sınıf tanımlamıştık::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        maaşı = 1500
        memleketi = ''
        doğum_tarihi = ''
        
Daha önce de söylediğimiz gibi, sınıflar belli birtakım ortak özelliklere sahip
gruplar tanımlamak için biçilmiş kaftandır. Burada da, herbir çalışan için ortak
birtakım nitelikler tanımlayan ``Çalışan()`` adlı bir sınıf oluşturduk. Ancak
elbette bu sınıfın bir işe yarayabilmesi için, biraz önce de değindiğimiz gibi,
bu sınıfı temel alarak, bu sınıfta belirtilen nitelikleri taşıyan birden fazla
sınıf üyesi meydana getirebilmemiz lazım.

Şimdi dikkatlice bakın::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        maaşı = 1500
        memleketi = ''
        doğum_tarihi = ''
        
    ahmet = Çalışan()
    
Burada sınıfımızı `ahmet` adlı bir değişkene atadık.
    
İşte bu işleme teknik dilde 'örnekleme' veya 'örneklendirme' (*instantiation*)
adı verilir. Bu işlemi fonksiyon çağırma ile kıyaslayabiliriz: Python
programlama dilinde bir fonksiyonu kullanışlı hale getirme işlemine 'çağırma',
bir sınıfı kullanışlı hale getirme işlemine ise 'örnekleme' adı veriyoruz.

Örnekleme kavramını daha iyi anlayabilmek için başka bir sınıf daha
oluşturalım::
    
    class Asker():
        rütbesi = 'Er'
        standart_teçhizat = ['G3', 'kasatura', 'süngü', 'el bombası']
        gücü = 60
        birliği = ''
        
Burada da belli birtakım niteliklere sahip ``Asker()`` adlı bir sınıf
tanımladık. Bu sınıfın niteliklerine doğrudan sınıf adını kullanarak
erişebileceğimizi biliyorsunuz::
    
    Asker.rütbesi
    Asker.standart_teçhizat
    Asker.gücü
    Asker.birliği
    
Ama bu sınıfın bir işe yarayabilmesi için, bu sınıfa bir 'referans' oluşturmamız
lazım, ki daha sonra bu sınıfa bu referans üzerinden atıfta bulunabilelim. Yani
bu sınıfı çağırırken buna bir isim vermeliyiz, ki bu isim üzerinden sınıfa ve
niteliklerine erişebilelim.
    
Mesela bu sınıfa daha sonra atıfta bulunabilmek amacıyla, bu sınıf için `mehmet`
adlı bir referans noktası oluşturalım::
    
    mehmet = Asker()
    
İşte, teknik olarak ifade etmemiz gerekirse, sınıfları bir isme atama işlemine
örnekleme (veya örneklendirme) adı veriyoruz.

Burada `ahmet` ve `mehmet`, ait oldukları sınıfların birer 'sureti' veya başka
bir deyişle 'örneği'dir (*instance*). `mehmet`'in, ``Asker()`` adlı sınıfın bir
örneği, `ahmet`'inse ``Çalışan()`` adlı sınıfın bir örneği olması demek,
`mehmet`'in ve `ahmet`'in, ilgili sınıfların bütün özelliklerini taşıyan birer
üyesi olması demektir.

.. warning:: Bu bağlamda 'örnek' kelimesini 'misal' anlamında kullanmadığımıza
 özellikle dikkatinizi çekmek isterim. Türkçede 'örnek' kelimesi ile
 karşıladığımız 'instance' kavramı, nesne tabanlı programlamanın önemli teknik
 kavramlarından biridir.
 
Biz bir sınıfı çağırdığımızda (yani ``Asker()`` veya ``Çalışan()`` komutunu
verdiğimizde), o sınıfı örneklemiş oluyoruz. Örneklediğimiz sınıfı bir değişkene
atadığımızda ise o sınıfın bir örneğini çıkarmış, yani o sınıfın bütün
özelliklerini taşıyan bir üye meydana getirmiş oluyoruz. 

Bu arada, elbette bu teknik terimleri ezberlemek zorunda değilsiniz. Ancak nesne
tabanlı programlamaya ilişkin metinlerde bu terimlerle sık sık
karşılaşacaksınız. Eğer bu terimlerin anlamını bilirseniz, okuduğunuz şey
zihninizde daha kolay yer edecek, aksi halde, sürekli ne demek olduğunu
bilmediğiniz terimlerle karşılaşmak öğrenme motivasyonunuza zarar verecektir.

Esasında nesne tabanlı programlamayı öğrencilerin gözünde zor kılan şey, bu
programlama yaklaşımının özünden ziyade, içerdiği terimlerdir. Gerçekten de
nesne tabanlı programlama, pek çok çetrefilli teknik kavramı bünyesinde
barındıran bir sistemdir. Bu nedenle öğrenciler bu konuya ilişkin bir şeyler
okurken, muğlak kavramların arasında kaybolup konunun esasını gözden
kaçırabiliyor. Eğer nesne tabanlı programlamaya ilişkin kavramları hakkıyla
anlarsanız, bu yaklaşıma dair önemli bir engeli aşmışsınız demektir. 

Öte yandan, nesne tabanlı programlamaya ilişkin kavramları anlamak sadece Türkçe
okuyup yazanlar için değil, aynı zamanda İngilizce bilip ilgili makaleleri özgün
dilinden okuyanlar için de zor olabilir. O yüzden biz bu bölümde, kavramların
Türkçeleri ile birlikte İngilizcelerini de vererek, İngilizce bilenlerin özgün
metinleri okurken konuyu daha iyi anlamalarını sağlamaya çalışacağız.
Dolayısıyla, bir kavramdan bahsederken onun aslının ne olduğunu da belirtmemiz,
İngilizce bilip de konuyu daha ileri bir düzeyde araştırmak isteyenlere kolaylık
sağlayacaktır.

Ne diyorduk? Eğer elimizde şöyle bir kod varsa::
    
    class Sipariş():
        firma = ''
        miktar = 0
        sipariş_tarihi = ''
        teslim_tarihi = ''
        stok_adedi = 0
        
        
    jilet = Sipariş()   
    
Burada `class`, sınıfı tanımlamamıza yarayan bir öğedir. Tıpkı fonksiyonlardaki
`def` gibi, sınıfları tanımlamak için de `class` adlı bir parçacığı
kullanıyoruz.

`Sipariş` ise, sınıfımızın adı oluyor. Biz sınıfımızın adını parantezli veya
parantezsiz olarak kullanma imkanına sahibiz.

Sınıfın gövdesinde tanımladığımız şu değişkenler birer sınıf niteliğidir (*class
atribute*)::
    
    firma = ''
    miktar = 0
    sipariş_tarihi = ''
    teslim_tarihi = ''
    stok_adedi = 0    

``jilet = Sipariş()`` komutunu verdiğimizde ise, biraz önce tanımladığımız
sınıfı örnekleyip (*instantiation*), bunu `jilet` adlı bir örneğe (*instance*)
atamış oluyoruz. Yani `jilet`, ``Sipariş()`` adlı sınıfın bir örneği olmuş
oluyor. Bir sınıftan istediğimiz sayıda örnek çıkarabiliriz::
    
    kalem = Sipariş()
    pergel = Sipariş()
    çikolata = Sipariş()   
    
Bu şekilde ``Sipariş()`` sınıfını üç kez örneklemiş, yani bu sınıfın bütün
özelliklerini taşıyan üç farklı üye meydana getirmiş oluyoruz.
    
Bu sınıf örneklerini kullanarak, ilgili sınıfın niteliklerine (*attribute*)
erişebiliriz::
    
    kalem = Sipariş()
    
    kalem.firma
    kalem.miktar
    kalem.sipariş_tarihi
    kalem.teslim_tarihi
    kalem.stok_adedi
    
Bildiğiniz gibi, eriştiğimiz bu nitelikler birer sınıf niteliği olduğu için,
sınıfı hiç örneklemeden, bu niteliklere doğrudan sınıf adı üzerinden de
erişebilirdik::
    
    Sipariş.firma
    Sipariş.miktar
    Sipariş.sipariş_tarihi
    Sipariş.teslim_tarihi
    Sipariş.stok_adedi
    
Özellikle, örneklenmesine gerek olmayan, yalnızca bir kez çalışacak sınıflarda,
sınıf niteliklerine örnekler üzerinden değil de doğrudan sınıf adı üzerinden
erişmek daha pratik olabilir. Ancak yukarıda olduğu gibi, tek bir sınıftan,
ortak niteliklere sahip birden fazla üye oluşturmamız gereken durumlarda sınıfı
bir örneğe atayıp, sınıf niteliklerine bu örnek üzerinden erişmek çok daha
akıllıca olacaktır. Ancak her koşulda sınıfların niteliklerine doğrudan sınıf
adları üzerinden erişmek yerine örnekler üzerinden erişmeyi tercih etmenizin de
hiçbir sakıncası olmadığını bilin.

Gelin şimdi yukarıda öğrendiklerimizi kullanarak ufak tefek uygulama çalışmaları
yapalım.

Sınıfımız şu olsun::
    
    class Sipariş():
        firma = ''
        miktar = 0
        sipariş_tarihi = ''
        teslim_tarihi = ''
        stok_adedi = 0
        
Bildiğiniz gibi, ufak tefek kod çalışmaları yapmak için Python'ın etkileşimli
kabuğu son derece uygun bir ortamdır. O halde yukarıdaki sınıfı `sipariş.py`
adlı bir dosyaya kaydedelim, bu dosyanın bulunduğu konumda bir etkileşimli
kabuk ortamı açalım ve `sipariş.py` dosyasını bir modül olarak içe aktaralım::
    
    >>> import sipariş
    
Böylece `sipariş` modülü içindeki nitelik ve metotlara erişim sağladık. Bunu
teyit edelim::
    
    >>> dir(sipariş)
    
    ['Sipariş', '__builtins__', '__cached__', '__doc__', '__file__', 
     '__loader__', '__name__', '__package__', '__spec__']
     
``Sipariş()`` adlı sınıfı listenin en başında görebilirsiniz. O halde gelin bu
sınıfı örnekleyerek kullanılabilir hale getirelim::
    
    >>> gofret = sipariş.Sipariş()
    
Elbette ``Sipariş()`` adlı sınıf `sipariş` adlı modül içinde bulunduğundan, bu
sınıfa `sipariş` önekiyle erişiyoruz. Tabii biz isteseydik modülü şu şekilde de
içe aktarabilirdik::
    
    >>> from sipariş import Sipariş
    
Böylece ``Sipariş()`` sınıfına öneksiz olarak erişebilirdik::
    
    >>> gofret = Sipariş()
    
Ancak mevcut isim alanını kirletmemek ve bu alanı nereden geldiği belli olmayan
birtakım nitelik ve metotlarla doldurmamak için biz ``import modül_adı``
biçimini tercih ediyoruz. Aksi halde, bu kodları okuyanlar, ``Sipariş()`` adlı
sınıfın `sipariş` adlı bir modüle ait olduğunu anlamayacak, bu sınıfı ilk olarak
mevcut dosya içinde bulmaya çalışacaklardır. Ama biz modül adını sınıf adına
eklediğimizde modülün nereden geldiği gayet açık bir şekilde anlaşılabiliyor.
Böylece hem kodları okuyan başkalarının işini hem de birkaç ay sonra kendi
kodlarımıza tekrar bakmak istediğimizde kendi işimizi kolaylaştırmış oluyoruz.

Neyse... Lafı daha fazla dolandırmadan kaldığımız yerden devam edelim...

Sınıfımızı şu şekilde içe aktarmış ve örneklemiştik::
    
    >>> import sipariş
    >>> gofret = sipariş.Sipariş()
    
Gelin şimdi bir de `gofret` örneğinin (*instance*) içeriğini kontrol edelim::
    
    >>> dir(gofret)
    
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
     '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', 
     '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
     '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'firma', 
     'miktar', 'sipariş_tarihi', 'stok_adedi', 'teslim_tarihi']
     
Gördüğünüz gibi, sınıf içinde tanımladığımız bütün sınıf nitelikleri (`firma`,
`miktar`, `sipariş_tarihi`, `stok_adedi` ve `teslim_tarihi`) bu liste içinde
var. 

Bu sınıf niteliklerinden, adı `firma` olanı kullanarak siparişin hangi firmadan
yapılacağını belirleyebiliriz::
    
    >>> gofret.firma = 'Öz İstihza ve Şerikleri Gıda, Ticaret Anonim Şirketi'
    
Böylece, sınıf içindeki bir niteliğe yeni bir değer atamış olduk. İsterseniz
şipariş miktarını da belirleyelim::
    
    >>> gofret.miktar = 1000
    
Öteki sınıf niteliklerini de ihtiyacınıza göre ayarlayabilir, hatta bu sınıfa
yeni nitelikler de ekleyebilirsiniz.

Gelin isterseniz pratik olması bakımından bir örnek daha verelim.

Elimizde şöyle bir sınıf olsun::
    
    class Çalışan():
        kabiliyetleri = []
        unvanı = 'işçi'
        maaşı = 1500
        memleketi = ''
        doğum_tarihi = ''
        
Burada `kabiliyetleri`, `unvanı`, `maaşı`, `memleketi` ve `doğum_tarihi` adlı
beş adet değişken tanımladık. Teknik dilde bu değişkenlere 'sınıf niteliği'
(*class attribute*) adı verildiğini biliyorsunuz.

``Çalışan()`` sınıfı içindeki niteliklere erişmek için birkaç tane örnek
çıkaralım::
    
    ahmet = Çalışan()
    mehmet = Çalışan()
    ayşe = Çalışan()
    
Bu şekilde ``Çalışan()`` sınıfının üç farklı örneğini oluşturmuş olduk. Bu
sınıfın niteliklerine, oluşturduğumuz bu örnekler üzerinden erişebiliriz::
    
    print(ahmet.kabiliyetleri)
    print(ahmet.unvanı)
    
    print(mehmet.maaşı)
    print(mehmet.memleketi)
    
    print(ayşe.kabiliyetleri)
    print(ayşe.doğum_tarihi)

Çıkardığımız örnekler aracılığıyla sınıf nitelikleri üzerinde değişiklik de
yapabiliyoruz::
    
    ahmet.kabiliyetleri.append('prezantabl')
        
Şimdi burada bir duralım. Çünkü burada çok sinsi bir sorunla karşı karşıyayız.
Dikkatlice bakın.

``Çalışan()`` sınıfı için bir `ahmet` örneği oluşturalım::
    
    ahmet = Çalışan()
    
Buna 'prezantabl' kabiliyetini ekleyelim::
    
    ahmet.kabiliyetleri.append('prezantabl')
    
Bu kabiliyetin eklendiğini teyit edelim::
    
    print(ahmet.kabiliyetleri)
    
Şimdi ``Çalışan()`` sınıfının bir başka örneğini oluşturalım::
    
    selim = Çalışan()
    
Bu örneğin kabiliyetlerini kontrol edelim::
    
    print(selim.kabiliyetleri)
    
Gördüğünüz gibi, yalnızca `ahmet` örneğine eklemek istediğimiz 'prezantabl'
kabiliyeti `selim` örneğine de eklenmiş. Ancak normal şartlarda arzu edilen bir
şey değildir bu. Zira bu durum aslında programımızdaki bir tasarım hatasına
işaret eder. Peki ama bu durumun sebebi nedir?

Hatırlarsanız, sınıf niteliklerinden bahsederken, bu niteliklerin önemli bir
özelliğinin, sınıf çağrılmadan çalışmaya başlamaları olduğunu söylemiştik. Sınıf
niteliklerinin bir başka önemli özelliği de, bu niteliklere atanan değerlerin ve
eğer yapılabiliyorsa bu değerler üzerinde sonradan yapılan değişikliklerin o
sınıfın bütün örneklerini etkiliyor olmasıdır. Eğer ilgili sınıf niteliği;
karakter dizisi, demet ve sayı gibi değiştirilemeyen (*immutable*) bir veri tipi
ise bu sınıf niteliği üzerinde zaten değişiklik yapamazsınız. Yaptığınız şey
ancak ilgili sınıf niteliğini yeniden tanımlamak olacaktır. Ancak eğer sınıf
niteliği, liste, sözlük ve küme gibi değiştirilebilir (*mutable*) bir veri tipi
ise bu nitelik üzerinde yapacağınız değişiklikler bütün sınıf örneklerine
yansıyacaktır. Yazdığınız program açısından bu özellik arzu ettiğiniz bir şey
olabilir veya olmayabilir. Önemli olan, sınıf niteliklerinin bu özelliğinin
farkında olmanız ve kodlarınızı bu bilgi çerçevesinde yazmanızdır. Mesela
yukarıdaki örnekte `kabiliyetleri` listesine eklenen öğelerin bütün örneklere
yansıması istediğimiz bir şey değil. Ama eğer sınıfımız şöyle olsaydı::
    
    class Çalışan():
        personel_listesi = []
        
Burada `personel_listesi` adlı bir sınıf niteliği tanımladık. Eğer bu listenin,
personele eklenen bütün elemanları barındırmasını planlıyorsak bu listenin her
örneklemede büyümesi elbette istediğimiz bir şey olacaktır.

Peki o halde biz değerinin her örnekte ortak değil de her örneğe özgü olmasını
istediğimiz nitelikleri nasıl tanımlayacağız? Elbette sınıf nitelikleri yerine
örnek nitelikleri denen başka bir kavramdan yararlanarak...
        
Örnek Nitelikleri
******************

Şimdiye kadar öğrendiklerimiz, sınıflarla faydalı işler yapmamız için pek
yeterli değildi. Sınıflar konusunda ufkumuzun genişleyebilmesi için, sınıf
niteliklerinin (*class attributes*) yanısıra, nesne tabanlı programlamanın
önemli bir parçası olan örnek niteliklerinden (*instance attributes*) de söz
etmemiz gerekiyor. Hem örnek niteliklerini öğrendikten sonra, bunların sınıf
nitelikleri ile arasındaki farkları görünce sınıf niteliklerini de çok daha iyi
anlamış olacaksınız.

__init__ Fonksiyonu ve self
*******************************

Buraya gelene kadar, sınıflar ile ilgili verdiğimiz kod parçaları yalnızca sınıf
niteliklerini içeriyordu. Mesela yukarıda tanımladığımız ``Çalışan()`` sınıfı
içindeki `unvanı` ve `kabiliyetleri` adlı değişkenlerin birer sınıf
niteliği olduğunu biliyoruz.

Sınıf nitelikleri dışında, Python'da bir de örnek nitelikleri bulunur. 

Bildiğiniz gibi, Python'da sınıf niteliklerini tanımlamak için yapmamız gereken
tek şey, sınıf tanımının hemen altına bunları alelade birer değişken gibi
yazmaktan ibarettir::
    
    class Sınıf():
        sınıf_niteliği1 = 0
        sınıf_niteliği2 = 1
        
Örnek niteliklerini tanımlamak için ise iki yardımcı araca ihtiyacımız var:
``__init__()`` fonksiyonu ve `self`. 

Bu iki aracı şu şekilde kullanıyoruz::
    
    class Çalışan():
        def __init__(self):
            self.kabiliyetleri = []
            
Bu arada, ``__init__()`` fonksiyonunun nasıl yazıldığına dikkat ediyoruz. `init`
kelimesinin sağında ve solunda ikişer adet alt çizgi (`_`) bulunduğunu gözden
kaçırmıyoruz. Ayrıca, ``__init__()`` fonksiyonunu `def` ifadesine bitişik
yazmamaya da bilhassa özen gösteriyoruz.     

'init' kelimesinin solunda ve sağında bulunan alt çizgiler sizi sakın
ürkütmesin. Aslında ``__init__()``, alelade bir fonksiyondan başka bir şey
değildir. Bu fonksiyonun öteki fonksiyonlardan tek farkı, sınıflar açısından
biraz özel bir anlam taşıyor olmasıdır. Bu özel fonksiyonun görevi, sınıfımızı
örneklediğimiz sırada, yani mesela ``ahmet = Çalışan()`` gibi bir komut
verdiğimiz anda oluşturulacak nitelikleri ve gerçekleştirilecek işlemleri
tanımlamaktır. Bu fonksiyonun ilk parametresi her zaman `self` olmak zorundadır.
Bu açıklama ilk anda kulağınıza biraz anlaşılmaz gelmiş olabilir. Ama hiç endişe
etmeyin. Bu bölümün sonuna vardığınızda bu iki öğeyi, adınızı bilir gibi biliyor
olacaksınız.

Hatırlarsanız, sınıf niteliklerini anlatırken bunların önemli bir özelliğinin,
sınıfın çağrılmasına gerek olmadan çalışmaya başlaması olduğunu söylemiştik::
    
    class Çalışan():
        selam = 'merhaba'
        print(selam)
        
Bu kodları çalıştırdığımız anda ekrana 'merhaba' çıktısı verilecektir. Örnek
nitelikleri ise farklıdır::
    
    class Çalışan():
        def __init__(self):
            self.kabiliyetleri = []
            print(self.kabiliyetleri)
            
Bu kodları çalıştırdığınızda herhangi bir çıktı almazsınız. Bu kodların çıktı
verebilmesi için sınıfımızı mutlaka örneklememiz lazım::
    
    class Çalışan():
        def __init__(self):
            self.kabiliyetleri = []
            print(self.kabiliyetleri)
            
    Çalışan()
    
Çünkü `self.kabiliyetleri` bir sınıf niteliği değil, bir örnek niteliğidir.
Örnek niteliklerine erişebilmek için de ilgili sınıfı mutlaka örneklememiz
gerekir. Ayrıca sınıf niteliklerinin aksine, örnek niteliklerine sınıf adları
üzerinden erişemeyiz. Yani `self.kabiliyetleri` adlı örnek niteliğine erişmeye
yönelik şöyle bir girişim bizi hüsrana uğratacaktır::
    
    Çalışan.kabiliyetleri
    
Bu örnek niteliğine erişmek için örneklendirme mekanizmasından yararlanmamız
lazım::
    
    Çalışan().kabiliyetleri #parantezlere dikkat!   
    
Gelin isterseniz, örneklendirme işlemini daha kullanışlı bir hale getirmek için,
örneklendirdiğimiz sınıfı bir örneğe atayalım, yani bu sınıfın bir örneğini
çıkaralım::
                
    ahmet = Çalışan()

``ahmet = Çalışan()`` kodu yardımıyla, ``Çalışan`` sınıfının bir örneğini
çıkardık ve buna `ahmet` adını verdik. İşte tam bu anda ``__init__()``
fonksiyonu çalışmaya başladı ve `ahmet` örneği için, `kabiliyetleri` adlı boş
bir örnek niteliği oluşturdu. 

Peki yukarıda kodlarımızı yazarken ``__init__()`` fonksiyonuna parametre olarak
verdiğimiz ve `kabiliyetleri` listesinin başında kullandığımız `self` kelimesi
ne oluyor?

Öncelikle bilmemiz gereken şey, `self` kelimesinin, Python programlama dilinin
söz diziminin gerektirdiği bir öğe olduğudur. Bu kelime, ``Çalışan()`` adlı
sınıfın örneklerini temsil eder. Peki 'self kelimesinin bir sınıfın örneklerini
temsil ediyor olması' ne anlama geliyor?

Bildiğiniz gibi, bir sınıfın örneğini şu şekilde çıkarıyoruz::
    
    ahmet = Çalışan()
    
Bu `ahmet` örneğini kullanarak, ``Çalışan()`` sınıfının içindeki `kabiliyetleri`
adlı örnek niteliğine sınıf dışından erişebiliriz::
    
    print(ahmet.kabiliyetleri)
    
İşte `self` kelimesi, yukarıdaki kodda yer alan `ahmet` kelimesini temsil
ediyor. Yani ``ahmet.kabiliyetleri`` şeklinde bir kod yazabilmemizi sağlayan
şey, ``__init__()`` fonksiyonu içinde belirttiğimiz `self` kelimesidir. Eğer bu
kelimeyi kullanmadan şöyle bir kod yazarsak::
    
    class Çalışan():
        def __init__():
            kabiliyetleri = []
            
...artık aşağıdaki kodlar yardımıyla `kabiliyetleri` niteliğine erişemeyiz::
            
    ahmet = Çalışan()
    print(ahmet.kabiliyetleri)

Şimdi aynı kodları bir de şöyle yazalım::
    
    class Çalışan():
        def __init__(self):
            kabiliyetleri = []
            
    ahmet = Çalışan()
    print(ahmet.kabiliyetleri)
    
Burada ``__init__()`` fonksiyonunda ilk parametre olarak `self`'i belirttik. Ama
`kabiliyetleri` niteliğinin başına `self` eklemedik. Dolayısıyla yazdığımız
kodlar yine hata verdi. Çünkü, ``ahmet.kabiliyetleri`` şeklinde
ifade ettiğimiz kodlardaki ``ahmet`` kelimesini karşılayacak herhangi bir
öğe sınıf içinde bulunmuyor...

Bu arada, örnek isimlerini (mesela `ahmet`) yalnızca örnek niteliklerine erişmek
için kullanmıyoruz. Bunları aynı zamanda sınıf niteliklerine erişmek için de
kullanabiliyoruz. Dolayısıyla eğer yukarıdaki sınıf tanımı içinde,
`self.kabiliyetleri` adlı *örnek niteliği*'nin yanısıra `personel` adlı bir
*sınıf niteliği* de bulunsaydı::
    
    class Çalışan():
        personel = ['personel']
        
        def __init__(self):
            self.kabiliyetleri = []
            
Şu kodları yazdığımızda::
            
    ahmet = Çalışan()
    print(ahmet.personel)  
    
...o sınıf niteliğine erişebilirdik. Ancak eğer ``__init__()`` fonksiyonu
altındaki `kabiliyetleri` niteliğine erişmek istiyorsak, bu niteliğin başına
`self` kelimesini getirerek, bu niteliği bir *örnek niteliği* haline getirmeli
ve böylece, ``ahmet.kabiliyetleri`` kodundaki ``ahmet`` kelimesini temsil edecek
bir öğeyi sınıf içinde oluşturmalıyız.

Bu süreç tam olarak şöyle işler:

Biz ``ahmet.kabiliyetleri`` şeklinde bir komut verdiğimizde, Python ilk olarak
ilgili sınıfın ``__init__()`` fonksiyonu içinde `kabiliyetleri` adlı bir örnek
niteliği arar. Elbette Python'ın bu örnek niteliğini bulabilmesi için,
``__init__()`` fonksiyonu içinde, bu fonksiyonun ilk parametresi ile aynı öneki
taşıyan bir niteliğin yer alması gerekir. Yani eğer ``__init__()`` fonksiyonunun
ilk parametresi `self` ise, Python bu fonksiyon içinde `self.kabiliyetleri` adlı
bir *örnek niteliği* bulmaya çalışır. Eğer bulamazsa, Python bu kez
`kabiliyetleri` adlı bir *sınıf niteliği* arar. Eğer onu da bulamazsa tabii ki
hata verir...

Gelin isterseniz bu mekanizmayı teyit edelim::
    
    class Çalışan():
        kabiliyetleri = ['sınıf niteliği']
        
        def __init__(self):
            self.kabiliyetleri = ['örnek niteliği']

Gördüğünüz gibi, burada aynı adı taşıyan bir sınıf niteliği ile bir örnek
niteliğimiz var. Python'da hem sınıf niteliklerine, hem de örnek niteliklerine
örnek isimleri üzerinden erişebileceğimizi söylemiştik. Yani eğer örneğimizin
ismi `ahmet` ise, hem `kabiliyetleri` adlı sınıf niteliğine hem de
`self.kabiliyetleri` adlı örnek niteliğine aynı şekilde erişiyoruz::
            
    ahmet = Çalışan()
    print(ahmet.kabiliyetleri)
    
Peki ama acaba yukarıdaki kodlar bize örnek niteliğini mi verir, yoksa sınıf
niteliğini mi?

Böyle bir durumda, yukarıda bahsettiğimiz mekanizma nedeniyle,
``self.kabiliyetleri`` şeklinde ifade ettiğimiz örnek niteliği, `kabiliyetleri`
adlı sınıf niteliğini gölgeler. Bu yüzden de ``print(ahmet.kabiliyetleri)``
komutu, örnek niteliğini, yani `self.kabiliyetleri` listesini verir. Yukarıdaki
kodları çalıştırarak siz de bu durumu teyit edebilirsiniz. Zira bu kodlar bize,
`self.kabiliyetleri` listesinin değeri olan 'örnek niteliği' çıktısını
verecektir...

Peki ya siz sınıf niteliği olan `kabiliyetleri` listesine erişmek isterseniz ne
olacak? 
    
İşte bunun için, sınıf örneğini değil de, sınıf adını kullanacaksınız::
    
    class Çalışan():
        kabiliyetleri = ['sınıf niteliği']
        
        def __init__(self):
            self.kabiliyetleri = ['örnek niteliği']
    
    #sınıf niteliğine erişmek için
    #sınıf adını kullanıyoruz
    print(Çalışan.kabiliyetleri)
    
    #örnek niteliğine erişmek için
    #örnek adını kullanıyoruz
    ahmet = Çalışan()
    print(ahmet.kabiliyetleri)
       
Ancak elbette, aynı adı taşıyan bir sınıf niteliği ile bir örnek niteliğini aynı
sınıf içinde tanımlamak daha baştan iyi bir fikir değildir, ama yazdığınız bir
sınıf yanlışlıkla aynı ada sahip sınıf ve örnek nitelikleri tanımlamanız
nedeniyle beklenmedik bir çıktı veriyorsa, siz Python'ın bu özelliğinden
haberdar olduğunuz için, hatanın nereden kaynaklandığını kolayca
kestirebilirsiniz.

Sözün kısası, Python'ın söz dizimi kuralları açısından, eğer bir örnek
niteliği tanımlıyorsak, bu niteliğin başına bir `self` getirmemiz gerekir.
Ayrıca bu `self` kelimesini de, örnek niteliğinin bulunduğu fonksiyonun
parametre listesinde ilk sıraya yerleştirmiş olmalıyız. Unutmayın, örnek
nitelikleri sadece fonksiyonlar içinde tanımlanabilir. Fonksiyon dışında örnek
niteliği tanımlayamazsınız. Yani şöyle bir şey yazamazsınız::
    
    class Çalışan():
        self.n = 0
        
        def __init__(self):
            self.kabiliyetleri = []    
            
Çünkü `self` kelimesi ancak ve ancak, içinde geçtiği fonksiyonun parametre
listesinde ilk sırada kullanıldığında anlam kazanır. 

Bu noktada size çok önemli bir bilgi verelim: Python sınıflarında örnek
niteliklerini temsil etmesi için kullanacağınız kelimenin `self` olması şart
değildir. Bunun yerine istediğiniz başka bir kelimeyi kullanabilirsiniz.
Mesela::

    class Çalışan():
        def __init__(falanca):
            falanca.kabiliyetleri = []
        
Dediğimiz gibi, `self` kelimesi, bir sınıfın örneklerini temsil ediyor. Siz
sınıf örneklerini hangi kelimenin temsil edeceğini kendiniz de
belirleyebilirsiniz. Mesela yukarıdaki örnekte, ``__init__()`` fonksiyonunun ilk
parametresini `falanca` olarak belirleyerek, örnek niteliklerinin `falanca`
kelimesi ile temsil edilmesini sağlamış olduk. Python'da bu konuya ilişkin kural
şudur: Sınıf içindeki bir fonksiyonun ilk parametresi ne ise, o fonksiyon
içindeki örnek niteliklerini temsil eden kelime de odur. Örneğin, eğer şöyle bir
sınıf tanımlamışsak::
    
    class XY():
        def __init__(a, b, c):
            a.örnek_niteliği = []
            
Burada ``__init__()`` fonksiyonunun ilk parametresi `a` olduğu için, örnek
niteliğini temsil eden kelime de `a` olur. Dolayısıyla `örnek_niteliği` adlı
örnek niteliğimizin başına da önek olarak bu `a` kelimesini getiriyoruz.

``__init__()`` fonksiyonunun ilk parametresi `a` olarak belirlendikten sonra,
bu fonksiyon içindeki bütün örnek nitelikleri, önek olarak `a` kelimesini
alacaktır::
    
    class XY():
        def __init__(a, b, c):
            a.örnek_niteliği1 = []
            a.örnek_niteliği2 = 23
            a.örnek_niteliği3 = 'istihza'          

ANCAK! Her ne sebeple olursa olsun, örnek niteliklerini temsil etmek için `self`
dışında bir kelime kullanmayın. Python bu kelimeyi bize dayatmasa da, `self`
kullanımı Python topluluğu içinde çok güçlü ve sıkı sıkıya yerleşmiş bir
gelenektir. Bu geleneği kimse bozmaz. Siz de bozmayın.

Sözün özü, tek başına `self` kelimesinin hiçbir anlamının olmadığını asla
aklınızdan çıkarmayın. Bu kelimenin Python açısından bir anlam kazanabilmesi
için, ilgili fonksiyonun parametre listesinde ilk sırada belirtiliyor olması
lazım. Zaten bu yüzden, dediğimiz gibi, `self` kelimesinin Python açısından bir
özelliği yoktur. Yani şöyle bir kod yazmamızın, Python söz dizimi açısından
hiçbir sakıncası bulunmaz::
    
    class Çalışan():
        def __init__(osman):
            osman.kabiliyetleri = []
            
Çünkü Python, örnek niteliklerini temsil eden kelimenin ne olduğuyla asla
ilgilenmez. Python için önemli olan tek şey, temsil işi için herhangi bir
kelimenin belirlenmiş olmasıdır. Tabii, biz, daha önce de ısrarla söylediğimiz
gibi, örnek niteliklerini `self` dışında bir kelime ile temsil etmeye teşebbüs
etmeyeceğiz ve kodlarımızı şu şekilde yazmaktan şaşmayacağız::
    
    class Çalışan():
        def __init__(self):
            self.kabiliyetleri = []
    
İşte yukarıdaki kodda gördüğümüz `self` parametresi ve `self` öneki,
birbirlerine bağımlı kavramlardır. Fonksiyonun ilk parametresi ne ise, örnek
niteliklerinin öneki de o olacaktır.

Bu arada, örnek niteliklerini anlatmaya başlamadan önce sınıf niteliklerine
ilişkin sinsi bir durumdan söz etmiştik hatırlarsanız. Buna göre, eğer elimizde
şöyle bir kod varsa::
    
    class Çalışan():
        kabiliyetleri = []
        
Biz bu sınıf içindeki `kabiliyetleri` listesine ekleme yaptığımızda, bu durum o
sınıfın bütün örneklerini etkiliyordu.

Yukarıdaki kodları `deneme.py` adlı bir dosyaya kaydettiğimizi varsayarsak::
    
    >>> import deneme
    >>> ahmet = deneme.Çalışan()
    >>> ahmet.kabiliyetleri.append('konuşkan')
    >>> ahmet.kabiliyetleri
    
    ['konuşkan']
    
    >>> mehmet = deneme.Çalışan()
    >>> print(mehmet.kabiliyetleri)
    
    ['konuşkan']
    
İşte bu durumu önlemek için örnek metotlarından yararlanabiliyoruz::
    
    class Çalışan():
        def __init__(self):
            self.kabiliyetleri = []
    

Yukarıdaki kodları yine `deneme.py` adlı bir dosyaya kaydettiğimizi
varsayarsak::
    
    >>> import deneme
    >>> ahmet = deneme.Çalışan()
    >>> ahmet.kabiliyetleri.append('konuşkan')
    >>> ahmet.kabiliyetleri
    
    ['konuşkan']
    
    >>> mehmet = deneme.Çalışan()
    >>> print(mehmet.kabiliyetleri)
    
    []
      
Gördüğünüz gibi, `ahmet` örneğine eklediğimiz 'konuşkan' öğesi, olması gerektiği
gibi, `mehmet` örneğinde bulunmuyor. Birazdan bu konu üzerine birkaç kelam daha
edeceğiz.

Örnek Metotları
******************

Buraya kadar sınıflar, örnekler, sınıf nitelikleri ve örnek nitelikleri
konusunda epey bilgi edindik. Gelin şimdi isterseniz bu öğrendiklerimizi
kullanarak az çok anlamlı bir şeyler yazmaya çalışalım. Böylece hem şimdiye
kadar öğrendiklerimizi gözden geçirmiş ve pekiştirmiş oluruz, hem de bu bölümde
ele alacağımız 'örnek metotları' (*instance methods*) kavramını anlamamız
kolaylaşır::
    
    class Çalışan():
        personel = []
        
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
            
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
            
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
            
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
            
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
                
Sınıfımızı tanımladık. Gelin isterseniz bu kodları açıklamaya başlamadan önce
nasıl kullanacağımızı görelim.

Bildiğiniz gibi, Python kodlarını test etmenin en iyi yolu, bunları etkileşimli
kabuk üzerinde çalıştırmaktır. Özellikle bir program yazarken, tasarladığınız
sınıfların, fonksiyonların ve öteki öğelerin düzgün çalışıp çalışmadığını test
etmek için etkileşimli kabuğu sıklıkla kullanacaksınız.

O halde, yukarıdaki kodları barındıran dosyanın bulunduğu dizin altında bir
etkileşimli kabuk oturumu başlatalım ve dosya adının `çalışan.py` olduğunu
varsayarak kodlarımızı bir modül şeklinde içe aktaralım::
    
    >>> import çalışan
    
Daha sonra sınıfımızın iki farklı örneğini çıkaralım::
            
    >>> ç1 = çalışan.Çalışan('Ahmet')
    
    Ahmet adlı kişi personele eklendi
    
    >>> ç2 = çalışan.Çalışan('Mehmet')
    
    Mehmet adlı kişi personele eklendi
    
Bu şekilde `çalışan` adlı modül içindeki ``Çalışan()`` adlı sınıfı sırasıyla
`'Ahmet'` ve `'Mehmet'` parametreleri ile çağırarak `ç1` ve `ç2` adlı iki farklı
sınıf örneği oluşturmuş olduk. Bu arada, sınıfımızı örneklediğimiz anda
``__init__()`` fonksiyonunun devreye girdiğine dikkat ediyoruz.


``personele_ekle()`` adlı fonksiyonu ``self.personele_ekle()`` şeklinde
``__init__()`` fonksiyonu içinden çağırdığımız için, sınıfımızı
örneklediğimiz anda hem personelin kendisi personel listesine eklendi, hem
de bu kişinin personele eklendiğine dair bir mesaj gösterildi.
    
Tanımladığımız sınıfın niteliklerine, çıkardığımız örnekler üzerinden
erişebiliriz::
    
    >>> ç1.isim
    
    'Ahmet'
    
    >>> ç2.isim
    
    'Mehmet'
    
Yine bu örnekler üzerinden, bu nitelikleri değiştirebiliriz de::
    
    >>> ç1.isim = 'Mahmut'
    >>> ç1.personel[0] = 'Mahmut'
    
Böylece ilk çalışanın ismini 'Mahmut' olarak değiştirdik::
    
    >>> ç1.isim
    
    'Mahmut'
    
    >>> ç1.personel
    
    ['Mahmut', 'Mehmet']
    
Tanımladığımız sınıf içindeki fonksiyonları kullanarak, çalışanlarımıza birkaç
kabiliyet ekleyelim::
    
    >>> ç1.kabiliyet_ekle('prezantabl')
    >>> ç1.kabiliyet_ekle('konuşkan')
    
`ç1` örneğinin kabiliyetlerini görüntüleyelim::
    
    >>> ç1.kabiliyetleri_görüntüle()
    
    Mahmut adlı kişinin kabiliyetleri:
    prezantabl
    konuşkan
    
Şimdi de `ç2` örneğine bir kabiliyet ekleyelim ve eklediğimiz kabiliyeti
görüntüleyelim::
    
    >>> ç2.kabiliyet_ekle('girişken')
    >>> ç2.kabiliyetleri_görüntüle()
    
    Mehmet adlı kişinin kabiliyetleri:
    girişken
    
Gördüğünüz gibi, bir sınıf örneğine eklediğimiz kabiliyet öteki sınıf
örneklerine karışmıyor. Bu, örnek niteliklerinin sınıf niteliklerinden önemli
bir farkıdır. Zira sınıf nitelikleri bir sınıfın bütün örnekleri tarafından
paylaşılır. Ama örnek nitelikleri her bir örneğe özgüdür. Bu özellikten biraz
sonra daha ayrıntılı olarak söz edeceğiz. Biz şimdilik okumaya devam edelim.

Sınıf örneklerimizin herhangi biri üzerinden personel listesine de
ulaşabileceğimizi biliyoruz::
    
    >>> ç1.personeli_görüntüle()
    
    Personel listesi:
    Mahmut
    Mehmet

Gayet güzel...

Yukarıda anlattıklarımız sınıflar hakkında size epey fikir vermiş olmalı. Konuyu
daha da derinlemesine anlayabilmek için, artık bu sınıfı incelemeye geçebiliriz.

Sınıfımızı önümüze alalım::
    
    class Çalışan():
        personel = []
    
        def __init__(self, isim):
            self.isim = isim
            self.kabiliyetleri = []
            self.personele_ekle()
    
        def personele_ekle(self):
            self.personel.append(self.isim)
            print('{} adlı kişi personele eklendi'.format(self.isim))
    
        def personeli_görüntüle(self):
            print('Personel listesi:')
            for kişi in self.personel:
                print(kişi)
    
        def kabiliyet_ekle(self, kabiliyet):
            self.kabiliyetleri.append(kabiliyet)
    
        def kabiliyetleri_görüntüle(self):
            print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
            for kabiliyet in self.kabiliyetleri:
                print(kabiliyet)
   
Burada öncelikle her zamanki gibi sınıfımızı tanımlıyoruz::
    
    class Çalışan():
        ...
        
Daha sonra bu sınıfa `personel` adlı bir sınıf niteliği ekliyoruz::
    
    class Çalışan():
        personel = []
        
Sınıf niteliklerinin özelliği, o sınıfın bütün örnekleri tarafından paylaşılıyor
olmasıdır. Yani herhangi bir örneğin bu nitelik üzerinde yaptığı değişiklik,
öteki örneklere de yansıyacaktır. Hele bir de bu sınıf niteliği, listeler gibi
değiştirilebilir (*mutable*) bir veri tipi ise, bu durum hiç de istemediğiniz
sonuçlar doğurabilir. Bununla ilgili bir örneği yukarıda vermiştik.
Hatırlarsanız, `kabiliyetleri` adlı, liste veri tipinde bir sınıf niteliği
oluşturduğumuzda, bu listeye eklediğimiz öğeler, hiç istemediğimiz halde öbür
örneklere de sirayet ediyordu. Elbette, sınıf niteliklerinin bu özelliği, o anda
yapmaya çalıştığınız şey açısından gerekli bir durum da olabilir. Mesela
yukarıdaki kodlarda, listelerin ve sınıf niteliklerinin bu özelliği bizim
amacımıza hizmet ediyor. Yukarıdaki sınıfı çalıştırdığımızda, eklenen her bir
kişiyi bu `personel` listesine ilave edeceğiz. Dolayısıyla bu nitelik üzerinde
yapılan değişikliklerin bütün örneklere yansıması bizim istediğimiz bir şey.

Neyse... Lafı daha fazla uzatmadan, kodlarımızı açıklamaya kaldığımız yerden
devam edelim...

Sınıfımızı ve sınıf niteliğimizi tanımladıktan sonra ``__init__()`` adlı özel
fonksiyonumuzu oluşturuyoruz::
    
    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()
        
Bu fonksiyonun özelliği, sınıfın örneklenmesi ile birlikte otomatik olarak
çalıştırılacak olmasıdır. Biz burada, `self.isim` ve `self.kabiliyetleri` adlı
iki adet örnek niteliği tanımladık. Bu örnek niteliklerine sınıfımızın her
tarafından erişebileceğiz.

Yukarıda, tanımladığımız sınıfı nasıl kullanacağımızı gösterirken, ``Çalışan()``
sınıfını şu şekilde örneklediğimizi hatırlıyorsunuz::
    
    >>> ç1 = çalışan.Çalışan('Ahmet')
    
Burada sınıfımızı `'Ahmet'` adlı bir argümanla örneklediğimize dikkatinizi
çekmek isterim. İşte bu argüman, biraz önce ``__init__()`` fonksiyonunu
tanımlarken belirttiğimiz `isim` parametresine karşılık geliyor. Dolayısıyla,
bir sınıfı çağırırken/örneklerken kullanacağımız argümanları, bu ``__init__()``
fonksiyonunun parametreleri olarak tanımlıyoruz.

Daha sonra bu `isim` parametresini, ``__init__()`` fonksiyonunun gövdesi içinde
bir örnek niteliği haline getiriyoruz::
    
    self.isim = isim
    
Bunu yapmamızın gerekçesi, `isim` parametresini sınıfımızın başka bölgelerinde
de kullanabilmek. `self` kelimesini parametremizin başına yerleştirerek, bu
parametreyi sınıfın başka yerlerinden de erişilebilir hale getiriyoruz.

`isim` parametresini, ``self.isim`` kodu yardımıyla bir örnek niteliğine
dönüştürdükten sonra `self.kabiliyetleri` adlı bir başka örnek niteliği daha
tanımlıyoruz. Bu liste, sınıf örneklerine eklediğimiz kabiliyetleri tutacak.

Bunun ardından şöyle bir kod görüyoruz::
    
    self.personele_ekle()
    
Burada, ``personele_ekle()`` adlı bir örnek metoduna (*instance method*) atıfta
bulunuyoruz. Örnek metotları, bir sınıfın örnekleri vasıtasıyla çağrılabilen
fonksiyonlardır. Bu fonksiyonların ilk parametresi her zaman `self` kelimesidir.
Ayrıca bu fonksiyonlara sınıf içinde atıfta bulunurken de yine `self` kelimesini
kullanıyoruz. Tıpkı yukarıdaki örnekte olduğu gibi...

Bir örnek metodu olduğunu söylediğimiz ``personele_ekle()`` fonksiyonunu şu
şekilde tanımladık::
    
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

Burada, bir sınıf niteliği olan `personel` değişkenine nasıl eriştiğimize çok
dikkat etmenizi istiyorum. Daha önce de söylediğimiz gibi, sınıf niteliklerine
sınıf dışındayken
örnekler üzerinden erişebiliyoruz. `self` kelimesi, bir sınıfın örneklerini
temsil ettiği için, bir örnek niteliğine sınıf içinden erişmemiz gerektiğinde
`self` kelimesini kullanabiliriz.

Sınıf niteliklerine, örnekler dışında, sınıf adıyla da erişebileceğinizi
biliyorsunuz. Dolayısıyla isterseniz yukarıdaki kodları şöyle de
yazabilirdiniz::

    def personele_ekle(self):
        Çalışan.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))
        
Bir öncekinden farklı olarak, bu defa sınıf niteliğine doğrudan sınıf adını
(`Çalışan`) kullanarak eriştik.

Ayrıca bu fonksiyonda, bir örnek niteliği olan `self.isim` değişkenine de
erişebiliyor olduğumuza dikkat edin. Unutmayın, `self` sınıfların çok önemli bir
öğesidir. Bu öğeyi kullanarak hem örnek niteliklerine, hem sınıf niteliklerine,
hem de örnek metotlarına ulaşabiliyoruz. Tanımladığımız bu ``personele_ekle()``
adlı örnek metodunu ``__init__()`` fonksiyonu içinden ``self.personele_ekle()``
kodu ile (yani yine `self` kelimesini kullanarak) çağırdığımızı hatırlıyorsunuz.

``personele_ekle()`` fonksiyonunun ardından arka arkaya üç fonksiyon daha
tanımladık::
    
    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)
        
    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)
            
Bu fonksiyonlar da, tıpkı ``personele_ekle()`` gibi, birer örnek metodudur. Bu
örnek metotlarının da ilk parametrelerinin hep `self` olduğuna dikkat ediyoruz.
Örnek metotlarına sınıf dışından örnek isimleri (`ahmet`, `mehmet` gibi)
aracılığıyla, sınıf içinden ise, örnek isimlerini temsil eden `self` kelimesi
aracılığıyla eriştiğimizi biliyorsunuz.

Şimdi bir duralım...

Bu noktaya kadar epey konuştuk, epey örnek verdik. Sınıflar hakkında yeterince
bilgi sahibi olduğumuza göre, nihayet en başta verdiğimiz harf sayacı kodlarını
rahatlıkla anlayabilecek düzeye eriştik::
    
    class HarfSayacı:
        def __init__(self):
            self.sesli_harfler = 'aeıioöuü'
            self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
            self.sayaç_sesli = 0
            self.sayaç_sessiz = 0
    
        def kelime_sor(self):
            return input('Bir kelime girin: ')
    
        def seslidir(self, harf):
            return harf in self.sesli_harfler
    
        def sessizdir(self, harf):
            return harf in self.sessiz_harfler
    
        def artır(self):
            for harf in self.kelime:
                if self.seslidir(harf):
                    self.sayaç_sesli += 1
                if self.sessizdir(harf):
                    self.sayaç_sessiz += 1
            return (self.sayaç_sesli, self.sayaç_sessiz)
    
        def ekrana_bas(self):
            sesli, sessiz = self.artır()
            mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
            print(mesaj.format(self.kelime, sesli, sessiz))
    
        def çalıştır(self):
            self.kelime = self.kelime_sor()
            self.ekrana_bas()
    
    if __name__ == '__main__':
        sayaç = HarfSayacı()
        sayaç.çalıştır()
        
Gelin isterseniz bu kodlara da şöyle bir bakalım...

Burada sınıfımızı şu şekilde tanımladık::
    
    class HarfSayacı:
        ...
        
Sınıf adını parantezli bir şekilde yazabileceğimizi de biliyorsunuz::
    
    class HarfSayacı():
        ...
        
Daha sonra, ``__init__()`` fonksiyonu içinde dört adet örnek niteliği
tanımladık::
    
    self.sesli_harfler = 'aeıioöuü'
    self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
    self.sayaç_sesli = 0
    self.sayaç_sessiz = 0
    
Bunların birer örnek niteliği olduğunu, başlarına getirdiğimiz `self`
kelimesinden anlıyoruz. Çünkü bildiğiniz gibi, `self` kelimesi, ilgili sınıfın
örneklerini temsil ediyor. Bir sınıf içinde örnek niteliklerine ve örnek
metotlarına hep bu `self` kelimesi aracılığıyla erişiyoruz.
        
Bu sınıf içinde, ilk parametreleri `self` olan şu örnek metotlarını görüyoruz::
    
    def kelime_sor(self):
        ...
        
    def seslidir(self, harf):
        ...
        
    def sessizdir(self, harf):
        ...
        
    def artır(self):
        ...
        
    def ekrana_bas(self):
        ...
        
    def çalıştır(self):
        ...

Sınıfla birlikte bütün örnek değişkenlerini ve örnek metotlarını tanımladıktan
sonra programımızı çalıştırma aşamasına geliyoruz::
    
    if __name__ == '__main__':
        sayaç = HarfSayacı()
        sayaç.çalıştır()
        
Buna göre, eğer programımız bağımsız olarak çalıştırılıyorsa öncelikle
``HarfSayacı()`` adlı sınıfı örneklendiriyoruz::
    
    sayaç = HarfSayacı()
    
Daha sonra da `sayaç` örneği üzerinden ``HarfSayacı()`` adlı sınıfın
``çalıştır()`` metoduna erişerek programımızı başlatıyoruz. 

Böylece, Python'da nesne tabanlı programlama ve sınıflara dair öğrenmemiz
gereken bütün temel bilgileri edinmiş olduk. Şu ana kadar öğrendikleriniz
sayesinde, etrafta göreceğiniz sınıflı kodların büyük bölümünü anlayabilecek
durumdasınız. Bir sonraki bölümde, nesne tabanlı programlamanın ayrıntılarına
inmeye başlayacağız. 
