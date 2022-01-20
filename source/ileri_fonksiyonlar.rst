.. meta::
   :description: Bu bölümde fonksiyonlar konusunu inceleyeceğiz.
   :keywords: python, fonksiyon, lambda, recursive, decorator, closure,
              özyinelemeli, bezeyiciler, kapalı fonksiyonlar ,
              nested , nonlocal , nested function , iç ,
              iç içe , iç içe fonksiyonlar, generator, üreteç , yield ,
              iterate , iterator, yield from

.. highlight:: py3


*************************
İleri Düzey Fonksiyonlar
*************************

Buraya gelinceye kadar fonksiyonlara ilişkin epey söz söyledik. Artık Python
programlama dilinde fonksiyonlara dair hemen her şeyi bildiğimizi rahatlıkla
söyleyebiliriz. Zira bu noktaya kadar hem fonksiyonların temel (ve orta düzey)
özelliklerini öğrendik, hem de 'gömülü fonksiyon' kavramını ve gömülü
fonksiyonların kendisini bütün ayrıntılarıyla inceledik. Dolayısıyla yazdığımız
kodlarda fonksiyonları oldukça verimli bir şekilde kullanabilecek kadar
fonksiyon bilgisine sahibiz artık.

Dediğimiz gibi, fonksiyonlara ilişkin en temel bilgileri edindik. Ancak
fonksiyonlara dair henüz bilmediğimiz şeyler de var. Ama artık Python
programlama dilinde geldiğimiz aşamayı dikkate alarak ileriye doğru bir adım
daha atabilir, fonksiyonlara dair ileri düzey sayılabilecek konulardan da söz
edebiliriz.

İlk olarak 'lambda fonksiyonlarını' ele alalım.

Lambda Fonksiyonları
********************

Şimdiye kadar Python programlama dilinde fonksiyon tanımlamak için hep `def`
adlı bir ifadeden yararlanmıştık. Bu bölümde ise Python programlama dilinde
fonksiyon tanımlamamızı sağlayacak, tıpkı `def` gibi bir ifadeden daha söz
edeceğiz. Fonksiyon tanımlamamızı sağlayan bu yeni ifadeye `lambda` denir. Bu
ifade ile oluşturulan fonksiyonlara ise 'lambda fonksiyonları'...

Bildiğiniz gibi Python'da bir fonksiyonu `def` ifadesi yardımıyla şöyle
tanımlıyoruz::

    >>> def fonk(param1, param2):
    ...     return param1 + param2

Bu fonksiyon, kendisine verilen parametreleri birbiriyle toplayıp bize bunların
toplamını döndürüyor::

    >>> fonk(2, 4)

    6

Peki aynı işlemi lambda fonksiyonları yardımıyla yapmak istersek nasıl bir yol
izleyeceğiz?

Dikkatlice bakın::

    >>> fonk = lambda param1, param2: param1 + param2

İşte burada tanımladığımız şey bir lambda fonksiyonudur. Bu lambda fonksiyonunu
da tıpkı biraz önce tanımladığımız def fonksiyonu gibi kullanabiliriz::

    >>> fonk(2, 4)

    6

Gördüğünüz gibi lambda fonksiyonlarını tanımlamak ve kullanmak hiç de zor değil.

Lambda fonksiyonlarının neye benzediğinden temel olarak bahsettiğimize göre
artık biraz daha derine inebiliriz.

Lambda fonksiyonları Python programlama dilinin ileri düzey fonksiyonlarından
biridir. Yukarıdaki örnek yardımıyla bu lambda fonksiyonlarının nasıl bir şey
olduğunu gördük. Esasında biz buraya gelene kadar bu lambda fonksiyonlarını hiç
görmemiş de değiliz. Hatırlarsanız daha önceki derslerimizde şöyle bir örnek kod
yazmıştık::

    harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    çevrim = {i: harfler.index(i) for i in harfler}

    isimler = ["ahmet", "ışık", "ismail", "çiğdem",
               "can", "şule", "iskender"]

    print(sorted(isimler, key=lambda x: çevrim.get(x[0])))

Burada ``sorted()`` fonksiyonunun `key` parametresi içinde kullandığımız ifade
bir lambda fonksiyonudur::

    lambda x: çevrim.get(x[0])

Peki lambda fonksiyonları nedir ve ne işe yarar?

Lambda fonksiyonlarını, bir fonksiyonun işlevselliğine ihtiyaç duyduğumuz, ama
konum olarak bir fonksiyon tanımlayamayacağımız veya fonksiyon tanımlamanın zor
ya da meşakkatli olduğu durumlarda kullanabiliriz. Yukarıdaki örnek kod, bu
tanıma iyi bir örnektir: ``sorted()`` fonksiyonunun `key` parametresi bizden bir
fonksiyon tanımı bekler. Ancak biz elbette oraya `def` ifadesini kullanarak
doğrudan bir fonksiyon tanımlayamayız. Ama `def` yerine `lambda` ifadesi
yardımıyla `key` parametresi için bir lambda fonksiyonu tanımlayabiliriz.

Eğer yukarıdaki kodları 'normal' bir fonksiyonla yazmak isteseydik şu kodları
kullanabilirdik::

    harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    çevrim = {i: harfler.index(i) for i in harfler}

    isimler = ["ahmet", "ışık", "ismail", "çiğdem",
               "can", "şule", "iskender"]

    def sırala(eleman):
        return çevrim.get(eleman[0])

    print(sorted(isimler, key=sırala))

Burada lambda fonksiyonu kullanmak yerine, ``sırala()`` adlı bir fonksiyon
kullandık.

Eğer yukarıda 'lambda' ile yazdığımız örneği ``sırala()`` fonksiyonu ile
yazdığımız örnekle kıyaslarsanız lambda fonksiyonlarında hangi parçanın neye
karşılık geldiğini veya ne anlama sahip olduğunu rahatlıkla anlayabilirsiniz.

Gelin bir örnek daha verelim:

Diyelim ki bir sayının çift sayı olup olmadığını denetleyen bir fonksiyon yazmak
istiyorsunuz. Bunun için şöyle bir fonksiyon tanımlayabileceğimizi
biliyorsunuz::

    def çift_mi(sayı):
        return sayı % 2 == 0

Eğer ``çift_mi()`` fonksiyonuna parametre olarak verilen bir sayı çift ise
fonksiyonumuz `True` çıktısı verecektir::

    print(çift_mi(100))

    True

Aksi halde `False` çıktısı alırız::

    print(çift_mi(99))

    False

İşte yukarıdaki etkiyi lambda fonksiyonları yardımıyla da elde edebiliriz.

Dikkatlice bakın::

    >>> çift_mi = lambda sayı: sayı % 2 == 0
    >>> çift_mi(100)

    True

    >>> çift_mi(99)

    False

Başka bir örnek daha verelim. Diyelim ki bir liste içindeki bütün sayıların
karesini hesaplamak istiyoruz. Elimizdeki liste şu:

    >>> l = [2, 5, 10, 23, 3, 6]

Bu listedeki sayıların her birinin karesini hesaplamak için şöyle bir şey
yazabiliriz::

    >>> for i in l:
    ...     print(i**2)

    4
    25
    100
    529
    9
    36

Veya şöyle bir şey::

    >>> [i**2 for i in l]

    [4, 25, 100, 529, 9, 36]

Ya da ``map()`` fonksiyonuyla birlikte lambda'yı kullanarak şu kodu
yazabiliriz::

    >>> print(*map(lambda sayı: sayı ** 2, l))

    4 25 100 529 9 36

Son örnekte verdiğimiz lambda'lı kodu normal bir fonksiyon tanımlayarak şöyle
de yazabilirdik::

    >>> def karesi(sayı):
    ...     return sayı ** 2
    ...
    >>> print(*map(karesi, l))

    4 25 100 529 9 36

Sözün özü, mesela şu kod::

    lambda x: x + 10

Türkçede şu anlama gelir::

    'x' adlı bir parametre alan bir lambda fonksiyonu tanımla. Bu fonksiyon, bu
    'x parametresine 10 sayısını eklesin.

Biz yukarıdaki örneklerde lambda fonksiyonunu tek bir parametre ile tanımladık.
Ama elbette lambda fonksiyonlarının birden fazla parametre de alabileceğini de
biliyorsunuz.

Örneğin::

    >>>  birleştir = lambda ifade, birleştirici: birleştirici.join(ifade.split())

Burada lambda fonksiyonumuz toplam iki farklı parametre alıyor: Bunlardan ilki
`ifade`, ikincisi ise `birleştirici`. Fonksiyonumuzun gövdesinde `ifade`
parametresine ``split()`` metodunu uyguladıktan sonra, elde ettiğimiz parçaları
`birleştirici` parametresinin değerini kullanarak birbirleriyle birleştiriyoruz.
Yani::

    >>> birleştir('istanbul büyükşehir belediyesi', '-')

    'istanbul-büyükşehir-belediyesi'

Eğer aynı işlevi 'normal' bir fonksiyon yardımıyla elde etmek isteseydik şöyle
bir şey yazabilirdik::

    >>> def birleştir(ifade, birleştirici):
    ...     return birleştirici.join(ifade.split())
    ...
    >>> birleştir('istanbul büyükşehir belediyesi', '-')

    'istanbul-büyükşehir-belediyesi'

Yukarıdaki örneklerin dışında, lambda fonksiyonları özellikle grafik arayüz
çalışmaları yaparken işinize yarayabilir. Örneğin::

    import tkinter
    import tkinter.ttk as ttk

    pen = tkinter.Tk()

    btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
    btn.pack(padx=20, pady=20)

    pen.mainloop()

.. note:: Bu kodlardan hiçbir şey anlamamış olabilirsiniz. Endişe etmeyin.
    Burada amacımız size sadece lambda fonksiyonlarının kullanımını göstermek. Bu
    kodlarda yalnızca lambda fonksiyonuna odaklanmanız şimdilik yeterli olacaktır.
    Eğer bu kodları çalıştıramadıysanız https://forum.yazbel.com/ adresinde
    sorununuzu dile getirebilirsiniz.

Bu kodları çalıştırıp 'merhaba' düğmesine bastığınızda komut satırında 'merhaba'
çıktısı görünecektir. Tkinter'de fonksiyonların `command` parametresi bizden
parametresiz bir fonksiyon girmemizi bekler. Ancak bazen, elde etmek istediğimiz
işlevsellik için oraya parametreli bir fonksiyon yazmak durumunda kalabiliriz.
İşte bunun gibi durumlarda lambda fonksiyonları faydalı olabilir. Elbette
yukarıdaki kodları şöyle de yazabilirdik::

    import tkinter
    import tkinter.ttk as ttk

    pen = tkinter.Tk()

    def merhaba():
        print('merhaba')

    btn = ttk.Button(text='merhaba', command=merhaba)
    btn.pack(padx=20, pady=20)

    pen.mainloop()

Burada da lambda yerine isimli bir fonksiyon tanımlayıp, `command` parametresine
doğrudan bu fonksiyonu verdik.

Bütün bu örneklerden gördüğünüz gibi, lambda fonksiyonları son derece pratik
araçlardır. Normal, isimli fonksiyonlarla elde ettiğimiz işlevselliği, lambda
fonksiyonları yardımıyla çok daha kısa bir şekilde elde edebiliriz. Ancak lambda
fonksiyonları normal fonksiyonlara göre biraz daha okunaksız yapılardır. O
yüzden, eğer lambda fonksiyonlarını kullanmaya mecbur değilseniz, bunların
yerine normal fonksiyonları veya yerine göre liste üreteçlerini tercih
edebilirsiniz.

Özyinelemeli (*Recursive*) Fonksiyonlar
****************************************

Bu bölümde, lambda fonksiyonlarının ardından, yine Python'ın ileri düzey
konularından biri olan 'özyinelemeli fonksiyonlar'dan söz edeceğiz. İngilizcede
*recursive functions* olarak adlandırılan özyinelemeli fonksiyonların, Python
programlama dilinin anlaması en zor konularından biri olduğu söylenir. Ama bu
söylenti sizi hiç endişelendirmesin. Zira biz burada bu çapraşık görünen konuyu
size olabildiğince basit ve anlaşılır bir şekilde sunmak için elimizden gelen
bütün çabayı göstereceğiz.

O halde hemen başlayalım...

Şimdiye kadar Python'da pek çok fonksiyon gördük. Bu fonksiyonlar kimi zaman
Python programcılarınca tanımlanıp dile entegre edilmiş 'gömülü fonksiyonlar'
(*builtin functions*) olarak, kimi zamansa o anda içinde bulunduğumuz duruma ve
ihtiyaçlarımıza göre bizzat kendimizin tanımladığı 'el yapımı fonksiyonlar'
(*custom functions*) olarak çıktı karşımıza.

Şimdiye kadar öğrendiğimiz bütün bu fonksiyonların ortak bir noktası vardı. Bu
ortak nokta, şu ana kadar fonksiyonları kullanarak yaptığımız örneklerden de
gördüğünüz gibi, bu fonksiyonlar yardımıyla başka fonksiyonları çağırabiliyor
olmamız. Örneğin::

    def selamla(kim):
        print('merhaba', kim)

Burada ``selamla()`` adlı bir fonksiyon tanımladık. Gördüğünüz gibi bu fonksiyon
``print()`` adlı başka bir fonksiyonu çağırıyor. Burada sıradışı bir şey yok.
Dediğimiz gibi, şimdiye kadar zaten hep böyle fonksiyonlar görmüştük.

Python fonksiyonları, yukarıdaki örnekte de gördüğünüz gibi, nasıl başka
fonksiyonları çağırabiliyorsa, aynı şekilde, istenirse, kendi kendilerini de
çağırabilirler. İşte bu tür fonksiyonlara Python programlama dilinde 'kendi
kendilerini yineleyen', veya daha teknik bir dille ifade etmek gerekirse
'özyinelemeli' (*recursive*) fonksiyonlar adı verilir.

Çok basit bir örnek verelim. Diyelim ki, kendisine parametre olarak verilen bir
karakter dizisi içindeki karakterleri teker teker azaltarak ekrana basan bir
fonksiyon yazmak istiyorsunuz. Yani mesela elinizde 'istihza' adlı bir karakter
dizisi var. Sizin amacınız bu karakter dizisini şu şekilde basan bir fonksiyon
yazmak::

    istihza
    stihza
    tihza
    ihza
    hza
    za
    a

Elbette bu işi yapacak bir fonksiyonu, daha önce öğrendiğiniz döngüler ve başka
yapılar yardımıyla rahatlıkla yazabilirsiniz. Ama isterseniz aynı işi
özyinelemeli fonksiyonlar yardımıyla da yapabilirsiniz.

Şimdi şu kodlara dikkatlice bakın::

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print(s)
            return azalt(s[1:])

    print(azalt('istihza'))

Bu kodlar bize yukarıda bahsettiğimiz çıktıyı verecek::

    istihza
    stihza
    tihza
    ihza
    hza
    za
    a

Fonksiyonumuzu yazıp çalıştırdığımıza ve bu fonksiyonun bize nasıl bir çıktı
verdiğini gördüğümüze göre fonksiyonu açıklamaya geçebiliriz.

Bu fonksiyon ilk bakışta daha önce öğrendiğimiz fonksiyonlardan çok da farklı
görünmüyor aslında. Ama eğer fonksiyonun son kısmına bakacak olursanız, bu
fonksiyonu daha önce öğrendiğimiz fonksiyonlardan ayıran şu satırı görürsünüz::

    return azalt(s[1:])

Gördüğünüz gibi, burada ``azalt()`` fonksiyonu içinde yine ``azalt()``
fonksiyonunu çağırıyoruz. Böylece fonksiyonumuz sürekli olarak kendi kendini
yineliyor. Yani aynı fonksiyonu tekrar tekrar uyguluyor.

Peki ama bunu nasıl yapıyor?

Nasıl bir durumla karşı karşıya olduğumuzu daha iyi anlamak için yukarıdaki
kodları şu şekilde yazalım::

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print(list(s))
            return azalt(s[1:])

Burada fonksiyonun her yinelenişinde, özyinelemeli fonksiyona parametre olarak
giden karakter dizisinin nasıl değiştiğini birazcık daha net olarak görebilmek
için karakter dizisi içindeki karakterleri bir liste haline getirip ekrana
basıyoruz::

    print(list(s))

Bu kodları çalıştırdığımızda şu çıktıyı alacağız::

    ['i', 's', 't', 'i', 'h', 'z', 'a']
    ['s', 't', 'i', 'h', 'z', 'a']
    ['t', 'i', 'h', 'z', 'a']
    ['i', 'h', 'z', 'a']
    ['h', 'z', 'a']
    ['z', 'a']
    ['a']

Yukarıdaki çıktının ilk satırında gördüğünüz gibi, fonksiyon ilk çağrıldığında
listede 'istihza' karakter dizisini oluşturan bütün harfler var. Yani
fonksiyonumuz ilk çalışmada parametre olarak karakter dizisinin tamamını alıyor.
Ancak fonksiyonun her yinelenişinde listedeki harfler birer birer düşüyor.
Böylece özyinelemeli fonksiyonumuz parametre olarak karakter dizisinin her
defasında bir eksiltilmiş biçimini alıyor.

Yukarıdaki sözünü ettiğimiz düşmenin yönü karakter dizisinin başından sonuna
doğru. Yani her defasında, elde kalan karakter dizisinin ilk harfi düşüyor.
Düşme yönünün böyle olması bizim kodları yazış şeklimizden kaynaklanıyor. Eğer
bu kodları şöyle yazsaydık::

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print(list(s))
            return azalt(s[:-1])

Harflerin düşme yönü sondan başa doğru olacaktı::

    ['i', 's', 't', 'i', 'h', 'z', 'a']
    ['i', 's', 't', 'i', 'h', 'z']
    ['i', 's', 't', 'i', 'h']
    ['i', 's', 't', 'i']
    ['i', 's', 't']
    ['i', 's']
    ['i']

Burada, bir önceki koddaki ``azalt(s[1:])`` satırını ``azalt(s[:-1])`` şeklinde
değiştirdiğimize dikkat edin.

Fonksiyonun nasıl işlediğini daha iyi anlamak için, 'istihza' karakter dizisinin
son harfinin her yineleniş esnasındaki konumunun nasıl değiştiğini de
izleyebilirsiniz::

    n = 0

    def azalt(s):
        global n
        mesaj = '{} harfinin {}. çalışmadaki konumu: {}'
        if len(s) < 1:
            return s
        else:
            n += 1
            print(mesaj.format('a', n, s.index('a')))
            return azalt(s[1:])

    azalt('istihza')

Bu kodlar şu çıktıyı verir::

    a harfinin 1. çalışmadaki konumu: 6
    a harfinin 2. çalışmadaki konumu: 5
    a harfinin 3. çalışmadaki konumu: 4
    a harfinin 4. çalışmadaki konumu: 3
    a harfinin 5. çalışmadaki konumu: 2
    a harfinin 6. çalışmadaki konumu: 1
    a harfinin 7. çalışmadaki konumu: 0

Gördüğünüz gibi 'istihza' kelimesinin en sonunda bulunan 'a' harfi her defasında
baş tarafa doğru ilerliyor.

Aynı şekilde, kodları daha iyi anlayabilmek için, fonksiyona parametre olarak
verdiğimiz 'istihza' kelimesinin her yinelemede ne kadar uzunluğa sahip olduğunu
da takip edebilirsiniz::

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print(len(s))
            return azalt(s[:-1])

Bu fonksiyonu 'istihza' karakter dizisine uyguladığımızda bize şu çıktıyı
veriyor::

    7
    6
    5
    4
    3
    2
    1

Gördüğünüz gibi, fonksiyonun kendini her yineleyişinde karakter dizimiz
küçülüyor.

Bu durum bize özyinelemeli fonksiyonlar hakkında çok önemli bir bilgi veriyor
esasında:

Özyinelemeli fonksiyonlar; büyük bir problemin çözülebilmesi için, o problemin,
problemin bütününü temsil eden daha küçük bir parçası üzerinde işlem
yapabilmemizi sağlayan fonksiyonlardır.

Yukarıdaki örnekte de bu ilkeyi uyguluyoruz. Yani biz 'istihza' karakter
dizisinin öncelikle yalnızca ilk karakterini düşürüyoruz::

    s[1:]

Daha sonra da bu yöntemi özyinelemeli bir şekilde uyguladığımızda, 'istihza'
karakter dizisinin her defasında daha küçük bir parçası bu yöntemden
etkileniyor::

    azalt(s[1:])

Yani fonksiyonumuz ilk olarak 'istihza' karakter dizisinin ilk harfi olan 'i'
harfini düşürüyor. Sonra 'stihza' kelimesinin ilk harfi olan 's' harfini
düşürüyor. Ardından 'tihza' kelimesinin ilk harfi olan 't' harfini düşürüyor ve
kelime tükenene kadar bu işlemi devam ettiriyor.

Peki ama bunu nasıl yapıyor?

Şimdi yukarıdaki fonksiyondaki şu kısma dikkatlice bakın::

    if len(s) < 1:
        return s

İşte burada özyinelemeli fonksiyonumuzun, karakter dizisi üzerinde ne kadar
derine inmesi gerektiğini belirliyoruz. Buna göre, karakter dizisinin uzunluğu
1'in altına düştüğünde eldeki karakter dizisini döndürüyoruz. Yani karakter
dizisinin uzunluğu 1'in altına düştüğünde elde kalan karakter dizisi boş bir
karakter dizisi olduğu için o boş karakter dizisini döndürüyoruz. Eğer istersek
elbette bu durumda başka bir şey de döndürebiliriz::

    def azalt(s):
        if len(s) < 1:
            return 'bitti!'
        else:
            print(s)
            return azalt(s[1:])

İşte ``if len(s) < 1:`` bloğunun bulunduğu bu kodlara 'dip nokta' adı veriyoruz.
Fonksiyonumuzun yinelene yinelene (veya başka bir ifadeyle 'dibe ine ine')
geleceği en son nokta burasıdır. Eğer bu dip noktayı belirtmezsek fonksiyonumuz,
tıpkı dipsiz bir kuyuya düşmüş gibi, sürekli daha derine inmeye çalışacak,
sonunda da hata verecektir. Ne demek istediğimizi daha iyi anlamak için
kodlarımızı şöyle yazalım::

    def azalt(s):
        print(s)
        return azalt(s[1:])

Gördüğünüz gibi burada herhangi bir dip nokta belirtmedik. Bu kodları
çalıştırdığımızda Python bize şöyle bir hata mesajı verecek::

    RuntimeError: maximum recursion depth exceeded

Yani::

    ÇalışmaZamanıHatası: Azami özyineleme derinliği aşıldı

Dediğimiz gibi, özyinelemeli fonksiyonlar her yinelenişte sorunun (yani üzerinde
işlem yapılan parametrenin) biraz daha derinine iner. Ancak bu derine inmenin de
bir sınırı vardır. Bu sınırın ne olduğunu şu kodlar yardımıyla
öğrenebilirsiniz::

    >>> import sys
    >>> sys.getrecursionlimit()

İşte biz özyinelemeli fonksiyonlarımızda dip noktayı mutlaka belirterek,
Python'ın fonksiyonu yinelerken ne kadar derine inip nerede duracağını
belirlemiş oluyoruz.

Şimdi son kez, yukarıdaki örnek fonksiyonu, özyineleme mantığını çok daha iyi
anlamanızı sağlayacak bir şekilde yeniden yazacağız. Dikkatlice bakın::

    def azalt(s):
        if len(s) < 1:
            return s
        else:
            print('özyineleme sürecine girerken:', s)
            azalt(s[1:])
            print('özyineleme sürecinden çıkarken:', s)

    azalt('istihza')

Burada, fonksiyon kendini yinelemeye başlamadan hemen önce bir ``print()``
satırı yerleştirerek `s` değişkeninin durumunu takip ediyoruz::

    print('özyineleme sürecine girerken:', s)

Aynı işlemi bir de fonksiyonun kendini yinelemeye başlamasının hemen ardından
yapıyoruz::

    print('özyineleme sürecinden çıkarken:', s)

Yukarıdaki kodlar bize şu çıktıyı verecek::

    özyineleme sürecine girerken: istihza
    özyineleme sürecine girerken: stihza
    özyineleme sürecine girerken: tihza
    özyineleme sürecine girerken: ihza
    özyineleme sürecine girerken: hza
    özyineleme sürecine girerken: za
    özyineleme sürecine girerken: a
    özyineleme sürecinden çıkarken: a
    özyineleme sürecinden çıkarken: za
    özyineleme sürecinden çıkarken: hza
    özyineleme sürecinden çıkarken: ihza
    özyineleme sürecinden çıkarken: tihza
    özyineleme sürecinden çıkarken: stihza
    özyineleme sürecinden çıkarken: istihza

Gördüğünüz gibi fonksiyon özyineleme sürecine girerken düşürdüğü her bir
karakteri, özyineleme sürecinden çıkarken yeniden döndürüyor. Bu, özyinelemeli
fonksiyonların önemli bir özelliğidir. Mesela bu özellikten yararlanarak şöyle
bir kod yazabilirsiniz::

    def ters_çevir(s):
        if len(s) < 1:
            return s
        else:
            ters_çevir(s[1:])
            print(s[0])

    ters_çevir('istihza')

Yazdığımız bu kodda ``ters_çevir()`` fonksiyonu, kendisine verilen parametreyi
ters çevirecektir. Yani yukarıdaki kod bize şu çıktıyı verir::

    a
    z
    h
    i
    t
    s
    i

Burada yaptığımız şey çok basit: Yukarıda da söylediğimiz gibi, özyinelemeli
fonksiyonlar, özyineleme sürecine girerken yaptığı işi, özyineleme sürecinden
çıkarken tersine çevirir. İşte biz de bu özellikten yararlandık. Fonksiyonun
kendini yinelediği noktanın çıkışına bir ``print()`` fonksiyonu yerleştirip,
geri dönen karakterlerin ilk harfini ekrana bastık. Böylece `s` adlı
parametrenin tersini elde etmiş olduk.

Ancak eğer yukarıdaki kodları bu şekilde yazarsak, fonksiyondan dönen değeri her
yerde kullanamayız. Mesela yukarıdaki fonksiyonu aşağıdaki gibi kullanamayız::

    def ters_çevir(s):
        if len(s) < 1:
            return s
        else:
            ters_çevir(s[1:])
            print(s[0])

    kelime = input('kelime girin: ')
    print('Girdiğiniz kelimenin tersi: {}'.format(kelime)

Fonksiyonumuzun daha kullanışlı olabilmesi için kodlarımızı şöyle yazabiliriz::

    def ters_çevir(s):
        if len(s) < 1:
            return s
        else:
            return ters_çevir(s[1:]) + s[0]

    kelime = input('kelime girin: ')
    print('Girdiğiniz kelimenin tersi: {}'.format(ters_çevir(kelime)))

Burada bizim amacımızı gerçekleştirmemizi sağlayan satır şu::

    return ters_çevir(s[1:]) + s[0]

İlk bakışta bu satırın nasıl çalıştığını anlamak zor gelebilir. Ama aslında son
derece basit bir mantığı var bu kodların. Şöyle düşünün: ``ters_çevir()``
fonksiyonunu özyinelemeli olarak işlettiğimizde, yani şu kodu yazdığımızda::

    return ters_çevir(s[1:])

...döndürülecek son değer boş bir karakter dizisidir. İşte biz özyinelemeden
çıkılırken geri dönen karakterlerin ilk harflerini bu boş karakter dizisine
ekliyoruz ve böylece girdiğimiz karakter dizisinin ters halini elde etmiş
oluyoruz.

Yukarıdaki işlevin aynısını, özyinelemeli fonksiyonunuzu şöyle yazarak da elde
edebilirdiniz::

    def ters_çevir(s):
        if not s:
            return s
        else:
            return s[-1] + ters_çevir(s[:-1])

    print(ters_çevir('istihza'))

Burada aynı iş için farklı bir yaklaşım benimsedik. İlk olarak, dip noktasını şu
şekilde belirledik::

    if not s:
        return s

Bildiğiniz gibi, boş veri tiplerinin bool değeri ``False``'tur. Dolayısıyla
özyineleme sırasında `s` parametresinin uzunluğunun 1'in altına düşmesi, `s`
parametresinin içinin boşaldığını gösterir. Yani o anda `s` parametresinin bool
değeri ``False`` olur. Biz de yukarıda bu durumdan faydalandık.

Bir önceki kodlara göre bir başka farklılık da şu satırda::

    return s[-1] + ters_çevir(s[:-1])

Burada benimsediğimiz yaklaşımın özü şu: Bildiğiniz gibi bir karakter dizisini
ters çevirmek istediğimizde öncelikle bu karakter dizisinin en son karakterini
alıp en başa yerleştiririz. Yani mesela elimizdeki karakter dizisi 'istihza'
ise, bu karakter dizisini ters çevirmenin ilk adımı bunun en son karakteri olan
'a' harfini alıp en başa koymaktır. Daha sonra da geri kalan harfleri tek tek
tersten buna ekleriz::

    düz:  istihza
    ters: a + z + h + i + t + s + i

İşte yukarıdaki fonksiyonda da yaptığımız şey tam anlamıyla budur.

Önce karakter dizisinin son harfini en başa koyuyoruz::

    return s[-1]

Ardından da buna geri kalan harfleri tek tek tersten ekliyoruz::

    return s[-1] + ters_çevir(s[:-1])

Özyinelemeli fonksiyonlara ilişkin olarak yukarıda tek bir örnek üzerinde epey
açıklama yaptık. Bu örnek ve açıklamalar, özyinelemeli fonksiyonların nasıl
çalıştığı konusunda size epey fikir vermiş olmalı. Ancak elbette bu
fonksiyonları tek bir örnek yardımıyla tamamen anlayamamış olabilirsiniz. O
yüzden gelin isterseniz bir örnek daha verelim. Mesela bu kez de basit bir sayaç
yapalım::

    def sayaç(sayı, sınır):
        print(sayı)
        if sayı == sınır:
            return 'bitti!'
        else:
            return sayaç(sayı+1, sınır)

.. note:: Bu fonksiyonun yaptığı işi elbette başka şekillerde çok daha kolay bir
    şekilde halledebilirdik. Bu örneği burada vermemizin amacı yalnızca özyinelemeli
    fonksiyonların nasıl işlediğini göstermek. Yoksa böyle bir işi özyinelemeli
    fonksiyonlarla yapmanızı beklemiyoruz.

Yukarıdaki fonksiyona dikkatlice bakarsanız aslında yaptığı işi çok basit bir
şekilde gerçekleştirdiğini göreceksiniz.

Burada öncelikle ``sayaç()`` adlı bir fonksiyon tanımladık. Bu fonksiyon toplam
iki farklı parametre alıyor: `sayı` ve `sınır`.

Buna göre fonksiyonumuzu şöyle kullanıyoruz::

    print(sayaç(0, 100))

Burada `sayı` parametresine verdiğimiz `0` değeri sayacımızın saymaya kaçtan
başlayacağını gösteriyor. `sınır` parametresine verdiğimiz `100` değeri ise kaça
kadar sayılacağını gösteriyor. Buna göre biz `0`'dan `100`'e kadar olan sayıları
sayıyoruz...

Gelin şimdi biraz fonksiyonumuzu inceleyelim.

İlk olarak şu satırı görüyoruz fonksiyon gövdesinde::

    print(sayı)

Bu satır, özyinelemeli fonksiyonun her yinelenişinde `sayı` parametresinin
durumunu ekrana basacak.

Sonraki iki satırda ise şu kodları görüyoruz::

    if sayı == sınır:
        return 'bitti!'

Bu bizim 'dip nokta' adını verdiğimiz şey. Fonksiyonumuz yalnızca bu noktaya
kadar yineleyecek, bu noktanın ilerisine geçmeyecektir. Yani `sayı`
parametresinin değeri `sınır` parametresinin değerine ulaştığında özyineleme
işlemi de sona erecek. Eğer böyle bir dip nokta belirtmezsek fonksiyonumuz
sonsuza kadar kendini yinelemeye çalışacak, daha önce sözünü ettiğimiz
'özyineleme limiti' nedeniyle de belli bir aşamadan sonra hata verip çökecektir.

Sonraki satırlarda ise şu kodları görüyoruz::

    else:
        return sayaç(sayı+1, sınır)

Bu satırlar, bir önceki aşamada belirttiğimiz dip noktaya ulaşılana kadar
fonksiyonumuzun hangi işlemleri yapacağını gösteriyor. Buna göre, fonksiyonun
her yinelenişinde `sayı` parametresinin değerini 1 sayı artırıyoruz.

Fonksiyonumuzu ``sayaç(0, 100)`` gibi bir komutla çalıştırdığımızı düşünürsek,
fonksiyonun ilk çalışmasında `0` olan sayı değeri sonraki yinelemede `1`,
sonraki yinelemede `2`, sonraki yinelemede ise `3` olacak ve bu durum `sınır`
değer olan `100`'e varılana kadar devam edecektir. `sayı` parametresinin değeri
`100` olduğunda ise dip nokta olarak verdiğimiz ölçüt devreye girecek ve
fonksiyonun kendi kendisini yinelemesi işlemine son verilecektir.

Biz yukarıdaki örnekte yukarıya doğru sayan bir fonksiyon yazdık. Eğer yukarıdan
aşağıya doğru sayan bir sayaç yapmak isterseniz yukarıdaki fonksiyonu şu şekle
getirebilirsiniz::

    def sayaç(sayı, sınır):
        print(sayı)
        if sayı == sınır:
            return 'bitti!'
        else:
            return sayaç(sayı-1, sınır)

    print(sayaç(100, 0))

Burada, önceki fonksiyonda `+` olan işleci `-` işlecine çevirdik::

    return sayaç(sayı-1, sınır)

Fonksiyonumuzu çağırırken de elbette `sayı` parametresinin değerini `100`
olarak, `sınır` parametresinin değerini ise `0` olarak belirledik.

Bu arada, daha önce de bahsettiğimiz gibi, özyinelemeli fonksiyonlar,
özyinelemeye başlarken döndürdükleri değeri, özyineleme işleminin sonunda tek
tek geri döndürür. Bu özelliği göz önünde bulundurarak yukarıdaki fonksiyonu şu
şekilde de yazabilirdiniz::

    def sayaç(sayı, sınır):
        if sayı == sınır:
            return 'bitti!'
        else:
            sayaç(sayı+1, sınır)
            print(sayı)

    print(sayaç(0, 10))

Dikkat ederseniz burada ``print(sayı)`` satırını özyineleme işlevinin çıkışına
yerleştirdik. Böylece `0`'dan `10`'a kadar olan sayıları tersten elde ettik.
Ancak tabii ki yukarıdaki anlamlı bir kod yazım tarzı değil. Çünkü
fonksiyonumuzun yazım tarzıyla yaptığı iş birbiriyle çok ilgisiz. Sayıları
yukarı doğru saymak üzere tasarlandığı belli olan bu kodlar, yalnızca bir
``print()`` fonksiyonunun özyineleme çıkışına yerleştirilmesi sayesinde yaptığı
işi yapıyor...

Yukarıda verdiğimiz örnekler sayesinde artık özyinelemeli fonksiyonlar hakkında
en azından fikir sahibi olduğumuzu söyleyebiliriz. Gelin isterseniz şimdi
özyinelemeli fonksiyonlarla ilgili (biraz daha mantıklı) bir örnek vererek bu
çetrefilli konuyu zihnimizde netleştirmeye çalışalım.

Bu defaki örneğimizde iç içe geçmiş listeleri tek katmanlı bir liste haline
getireceğiz. Yani elimizde şöyle bir liste olduğunu varsayarsak::

    l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

Yazacağımız kodlar bu listeyi şu hale getirecek::

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Bu amacı gerçekleştirebilmek için şöyle bir fonksiyon yazalım::

    def düz_liste_yap(liste):
        if not isinstance(liste, list):
            return [liste]
        elif not liste:
            return []
        else:
            return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])

    l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

    print(düz_liste_yap(l))

Bu fonksiyonu yukarıdaki iç içe geçmiş listeye uyguladığınızda istediğiniz
sonucu aldığınızı göreceksiniz.

İlk bakışta yukarıdaki kodları anlamak biraz zor gelmiş olabilir. Ama endişe
etmenize gerek yok. Zira biz bu kodları olabildiğince ayrıntılı bir şekilde
açıklayacağız.

İlk olarak dip noktamızı tanımlıyoruz her zamanki gibi::

    if not isinstance(liste, list):
        return [liste]

Fonksiyonumuzun temel çalışma prensibine göre liste içindeki bütün öğeleri tek
tek alıp başka bir liste içinde toplayacağız. Eğer liste elemanları üzerinde
ilerlerken karşımıza liste olmayan bir eleman çıkarsa bu elemanı ``[liste]``
koduyla bir listeye dönüştüreceğiz.

Önceki örneklerden farklı olarak, bu kez kodlarımızda iki farklı dip noktası
kontrolü görüyoruz. İlkini yukarıda açıkladık. İkinci dip noktamız şu::

    elif not liste:
        return []

Burada yaptığımız şey şu: Eğer özyineleme esnasında boş bir liste ile
karşılaşırsak, tekrar boş bir liste döndürüyoruz. Peki ama neden?

Bildiğiniz gibi boş bir listenin 0. elemanı olmaz. Yani boş bir liste üzerinde
şu işlemi yapamayız::

    >>> a = []
    >>> a[0]

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Gördüğünüz gibi, boş bir liste üzerinde indeksleme işlemi yapmaya
kalkıştığımızda hata alıyoruz. Şimdi durumu daha iyi anlayabilmek için
isterseniz yukarıdaki kodları bir de ikinci dip noktası kontrolü olmadan yazmayı
deneyelim::

    def düz_liste_yap(liste):
        if not isinstance(liste, list):
            return [liste]
        else:
            return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])

    l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

    print(düz_liste_yap(l))

Bu kodları çalıştırdığımızda şu hata mesajıyla karşılaşıyoruz::

    Traceback (most recent call last):
      File "deneme.py", line 9, in <module>
        print(düz_liste_yap(l))
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
      File "deneme.py", line 5, in düz_liste_yap
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
    IndexError: list index out of range

Gördüğünüz gibi, biraz önce boş bir liste üzerinde indeksleme yapmaya
çalıştığımızda aldığımız hatanın aynısı bu. Çünkü kodlarımızın ``else`` bloğuna
bakarsanız liste üzerinde indeksleme yaptığımızı görürsünüz::

    return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])

Elbette boş bir liste ``liste[0]`` veya ``liste[1:]`` gibi sorgulamalara
``IndexError`` tipinde bir hata mesajıyla cevap verecektir. İşte böyle bir
durumda hata almamak için şu kodları yazıyoruz::

    elif not liste:
        return []

Böylece özyineleme esnasında boş bir listeyle karşılaştığımızda bu listeyi şu
şekle dönüştürüyoruz::

    [[]]

Böyle bir yapı üzerinde indeksleme yapılabilir::

    >>> a = [[]]
    >>> a[0]

    []

Dip noktaya ulaşılana kadar yapılacak işlemler ise şunlar::

    return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])

Yani listenin ilk öğesine, geri kalan öğeleri teker teker ekliyoruz.

Gelin bir örnek daha verelim::

    def topla(sayilar):
        if len(sayilar) < 1:
            return 0
        else:
            ilk, son = sayilar[0], sayilar[1:]
            return ilk+topla(son)

Bu fonksiyonun görevi, kendisine liste olarak verilen sayıları birbiriyle
toplamak. Biz bu işi başka yöntemlerle de yapabileceğimizi biliyoruz, ama bizim
burada amacımız özyinelemeli fonksiyonları anlamak. O yüzden sayıları birbiriyle
toplama işlemini bir de bu şekilde yapmaya çalışacağız.

Elimizde şöyle bir liste olduğunu varsayalım::

    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Böyle bir durumda fonksiyonumuz `55` çıktısı verir.

Gelelim bu fonksiyonu açıklamaya...

Her zamanki gibi ilk olarak dip noktamızı tanımlıyoruz::

    if len(sayilar) < 1:
        return 0

Buna göre `sayilar` adlı listenin uzunluğu 1'in altına düşünce `0` değerini
döndürüyoruz. Burada `0` değerini döndürmemizin nedeni, listede öğe kalmadığında
programımızın hata vermesini önlemek. Eğer `0` dışında başka bir sayı
döndürürsek bu sayı toplama işleminin sonucuna etki edecektir. Toplama işleminin
sonucunu etkilemeyecek tek sayı `0` olduğu için biz de bu sayıyı döndürüyoruz.

Taban noktaya varılıncaya kadar yapılacak işlemler ise şunlar::

    ilk, son = sayilar[0], sayilar[1:]
    return ilk+topla(son)

Burada amacımız, listenin ilk sayısı ile listenin geri kalan öğelerini tek tek
birbiriyle toplamak. Bunun için `sayilar` adlı listenin ilk öğesini, listenin
geri kalanından ayırıyoruz ve ilk öğeyi `ilk`; geri kalan öğeleri ise `son` adlı
bir değişkene gönderiyoruz::

    ilk, son = sayilar[0], sayilar[1:]

Sonra da ilk öğeyi, geri kalan liste öğeleri ile tek tek topluyoruz. Bunun için
de ``topla()`` fonksiyonunun kendisini `son` adlı değişken içinde tutulan liste
öğelerine özyinelemeli olarak uyguluyoruz::

    return ilk+topla(son)

Böylece liste içindeki bütün öğelerin toplam değerini elde etmiş oluyoruz.

Bu arada, yeri gelmişken Python programlama dilinin pratik bir özelliğinden söz
edelim. Gördüğünüz gibi sayıların ilk öğesini geri kalan öğelerden ayırmak için
şöyle bir kod yazdık::

    ilk, son = sayilar[0], sayilar[1:]

Aslında aynı işi çok daha pratik bir şekilde de halledebilirdik. Dikkatlice
bakın::

    ilk, *son = sayilar

Böylece `sayilar` değişkenin ilk öğesi `ilk` değişkeninde, geri kalan öğeleri
ise `son` değişkeninde tutulacaktır. İlerleyen derslerde 'Yürüyücüler'
(*Iterators*) konusunu işlerken bu yapıdan daha ayrıntılı bir şekilde söz
edeceğiz.



İç İçe (*Nested*) Fonksiyonlar
********************************

Bu bölümde iç içe fonksiyonların ne olduklarını ve nasıl kullanılabileceklerini
inceleceğiz.

İç İçe Fonksiyonlar Nedir?
=============================

İsminden anlayabileceğimiz gibi içe içe olan birden fazla fonksiyonumuz
olunca bunlara *nested*, yani iç içe fonksiyonlar diyoruz.
Aşağıdaki gibi iki fonksiyonumuz olduğunu düşünelim::

	def fonk1():
		def fonk2():
			...

Burada ``fonk1`` kapsayıcı (*enclosing*) veya dış fonksiyonumuz, ``fonk2`` ise içerideki (*nested*) yani iç
fonksiyonumuz oluyor. İç içe fonksiyonlarımızın ilginç özellikleri olduğunu
söyleyebiliriz. Ayrıca bu fonksiyonları iyice anlamak, ileride üreteçleri
(diğer bir adı ile yürüyücüleri) de daha iyi anlamamızı sağlayacaktır.

İç içe fonksiyonları anlamanın en iyi yolu örnek üzerinden gitmektir.
Şimdi şöyle bir fonksiyon tanımlayalım::

    def yazıcı():
        def yaz(mesaj):
            print(mesaj)
        return yaz

Kodu çalıştırıp etkileşimli kabuğu kullanalım::

	>>> y = yazıcı()
	>>> y("Merhaba")
	Merhaba
	>>> type(y)
	<class 'function'>
	>>> y
	<function yazıcı.<locals>.yaz at 0x00000210D9235558>

Şimdi bu çıktılarımızı inceleyelim. ``yazıcı`` fonksiyonumuz çağrıldığında değer olarak
``yaz`` fonksiyonunu çeviriyor. Bu ``yaz`` fonksiyonu da ``yazıcı`` fonksiyonumuzun
içerisinde tanımladığı için bizim **iç** fonksiyonumuz oluyor. ``yazıcı`` ise
**kapsayıcı** fonksiyonumuz. ``y("Merhaba")`` komutu çağırıldığında ekrana ``Merhaba``
yazılıyor. Çünkü ``y``'ye atanan değer olan ``yaz`` fonksiyonunun yaptığı iş
buydu. Dikkat ederseniz ``y``'nin türünün de ``function`` olduğunu görebilirsiniz.
Son çıktımızda ise alışılmışın dışında bir ``<locals>`` ifadesi görüyoruz.
Şimdi biraz bunun üzerine konuşacağız.

Normalde bir fonksiyon yazdığımızda ve bu fonksiyon başka bir fonksiyonun içerisinde
olmadığında, programı çalıştırıldığımızda ve kod işleme sırası bu fonksiyona geldiğinde
fonksiyonumuz tanımlanmış olur. Yani bu fonksiyonun ne olduğu, ne yapacağı
artık Python yorumlayıcısı tarafından bilinmektedir. Ayrıca bu fonksiyondan sadece bir tane
vardır. Örneğin fonksiyonumuz şu şekilde ise::

    def fonk():
        pass

Her ``fonk()`` yazdığımızda aynı fonksiyon çağrılır. Dikkat edin, aynı işlemler yapılır
demiyorum. Aynı fonksiyon çağrılır. Yapacağı işlem burada bizim için önemli değil.

Şimdi de iç içe fonksiyon tanımımıza ve şu ``<locals>`` kelimesine bakalım.
İlk önce::

    def yazıcı():
        def yaz(mesaj):
            print(mesaj)
        return yaz

Şeklinde kapsayıcı fonksiyonumuzu tanımlamış oluyoruz. Dikkat ederseniz sadece kapsa-
yıcı fonksiyonun tanımlandığını söyledim. Artık ``yazıcı`` fonksiyonunun, Python yorum-
layıcısı tarafından ne yapacağı, nasıl çalışacağı biliniyor. Ancak ``yaz`` fonksiyonu için
aynı şeyleri söyleyemeyiz. Sonuç olarak bir fonksiyon çağırılmadan içerisindeki
komutlar çalışmaz. Eğer ``def yaz...`` komutu çalışmaz ise de ``yaz`` fonksiyonumuz tanımlanmış
olmaz. Yani şu anda ``yaz`` fonksiyonumuz tanımlanmamıştır. Peki ne zaman tanımlanacaktır?
Tabii ki de ``yazıcı`` fonksiyonumuzu çağırdığımız zaman. Çünkü dediğimiz gibi,
yazıcı fonksiyonu çağrılmadığı sürece ``def yaz...`` bölümü çalışmıyor. Python yorumlayıcısı
programımız çalışırken ``yazıcı`` fonksiyonunun *ne yapacağını* bilir, dolayısı ile de
``yaz`` fonksiyonununun *nasıl tanımlanacağını* bilir. Ancak ``yaz`` fonksiyonu
tanımlanmadan önce *ne yapacağını* bilemez. Buradan önemli
yerlere varacağımız için bu kısmın anlaşılması gerekiyor. Şimdi şunu söyleyebiliriz ki
``yazıcı`` fonksiyonumuzu her çağırdımızda ``yaz`` sınıfı en baştan tanımlanır.
Bu da ``yazıcı`` fonksiyonumuzu her çağırışımızda yeni tanımlanan ``yaz`` fonksiyonunun
farklı ve tek olduğu anlamına gelir. Yani kapsayıcı olan ``yazıcı`` fonksiyonu
sadece bir tane iken döndürdüğü ``yaz`` fonksiyonu birden fazla ve farklı oluyor.
Yani ``yazıcı`` fonksiyonumuzu her çağırdığımızda sadece o çağırışımıza özel bir
``yaz`` fonksiyonu elde ediyoruz. İşte bu ``<locals>`` kelimesi buradan geliyor.
Yani::

	>>> y
	<function yazıcı.<locals>.yaz at 0x00000210D9235558>

Bu demek oluyor ki bizim ``y`` değişkenimiz, daha önceki bir ``yazıcı`` fonksiyonunun çağrısına
ait, yani onun içinde tanımlanan bir ``yaz`` fonksiyonudur. ``locals`` da zaten
yerel değişkenler anlamına gelir. Yani buradaki ``yaz`` fonksiyonu, daha önce çağırdığımız
``yazıcı`` fonksiyonunun içinde tanımlanan yerel bir değişkendir. Tanımlanan her ``yaz``
fonksiyonunun farklı olduğunu şu şekilde de görebiliriz::

	>>> y = yazıcı()
	>>> b = yazıcı()
	>>> y
	<function yazıcı.<locals>.yaz at 0x00000210D9235558>
	>>> b
	<function yazıcı.<locals>.yaz at 0x00000210D920E678>
	>>> id(y)
	2271385703768
	>>> id(b)
	2271385544312

Gördüğünüz gibi farklı ``yaz`` fonksiyonlarının hafızada saklandığı yerler de
farklı oluyor...

Bu konuda biraz daha ilerlemeden önce bilmemiz gereken başka şeyler de var.
Biraz da onlar hakkında konuşalım.

'nonlocal' Deyimi
==================

``nonlocal`` deyimi *yerel olmayan* anlamına gelir. Kullanım amacı ``global`` deyimi
ile benzerdir. Ancak bunu kullanmamız küresel yani global değişkenlere ulaşmamızı değil,
yerel olmayan değişkenlere ulaşmamızı sağlar. Ayrıca bu deyimi sadece iç içe fonksiyonlarda kullanabiliriz. Tabii bunu böyle söyleyince bir şey anlaşılmıyor. Örnek vermek lazım::

    def kapsayıcı_fonk():
        non_local_değişken = 1

        def iç_fonk():
            non_local_değişken = 2
            print(non_local_değişken)

        return iç_fonk

Burada iç içe bir fonksiyon yapısına sahibiz. Şimdi bu kodumuzu çalıştırıp
etkileşimli kabukta denemeler yapalım::

	>>> dönüş_fonksiyonu = kapsayıcı_fonk()
	>>> dönüş_fonksiyonu()
	2

Gördüğünüz gibi ``1`` yazılmadı. Yani kapsayıcı fonksiyona ait olan ``non_local_değişken``
ile iç fonksiyonumuza ait olan ``non_local_değişken`` farklılar. Aynı bu örnekte::

	a = 1

    def fonk():
        a = 2
        print(a)


    >>> fonk()
    2

küresel ``a`` değişkeni ile ``fonk`` fonksiyonuna ait ``a`` değişkeninin farklı olması gibi.
Peki biz burada fonksiyon içinde de küresel ``a``'yı kullanmak istersek nasıl yaparız?
Bir şey yapmamıza gerek yok, zaten fonksiyon kendi içinde ``a`` değişkenini bulamayınca global alana bakacaktır::

    a = 1

    def fonk():
        print(a)


    >>> fonk()
    1

Fakat eğer küresel olan `a` değişkenini değiştirmek istiyorsanız bildiğiniz gibi ``global`` deyimini kullanmamız lazım::

    a = 1

    def fonk():
        global a
        a += 1
        print(a)


    >>> fonk()
    2
    >>> a
    2

İşte aynı bunun gibi::

    def kapsayıcı_fonk():
        non_local_değişken = 1

        def iç_fonk():
            non_local_değişken = 2
            print(non_local_değişken)

        return iç_fonk

Örneğimizde de ``iç_fonk``'un içinde ``kapsayıcı_fonk``'a ait olan ``non_local_değişken``
değişkenini değiştirmek istersek bunu da ``nonlocal`` deyimi ile şöyle yapabiliriz::

    def kapsayıcı_fonk():
        non_local_değişken = 1

        def iç_fonk():
            nonlocal non_local_değişken
            non_local_değişken += 1
            print(non_local_değişken)

        return iç_fonk


    >>> dönüş_fonksiyonu = kapsayıcı_fonk()
    >>> dönüş_fonksiyonu()
    2

Tabii bu değişkeni değiştirmek gibi bir amacımız yoksa, sadece kullanmak isteseydik şöyle de yapabilirdik ve ``nonlocal`` deyimine gerek kalmazdı::

    def kapsayıcı_fonk():
        non_local_değişken = 1

        def iç_fonk():
            print(non_local_değişken)
        return iç_fonk


    >>> dönüş_fonksiyonu = kapsayıcı_fonk()
    >>> dönüş_fonksiyonu()
    1

Gördüğünüz gibi ``nonlocal`` ifadesi iç içe fonksiyonlar ile çalışırken iç fonksiyonda,
kapsayıcı fonksiyonunun değişkenlerini değiştirmemizi sağlıyor. Artık bu bilgiyi kullanarak
şöyle bir fonksiyon oluşturabiliriz::

    def yazıcı(mesaj):
        def yaz():
            nonlocal mesaj
            mesaj += " Dünya"
            print(mesaj)
        return yaz


    >>> y = yazıcı("Merhaba")
    >>> y()
    Merhaba Dünya

``nonlocal`` deyiminin nasıl kullanıldığını bildiğiniz için örneğimizi anladığınızı
düşünüyorum. Burda yaptığımız tek farklı şey ``nonlocal`` deyimi ile birlikte
kullandığımız nesnenin ``yazıcı`` fonksiyonunun parametresi olması. Bunu yapmamızda
bir sakınca yoktur. Sonuç olarak ``mesaj`` parametresi, normalde de ``yazıcı`` fonksiyonu
içerisinde bir değişken gibi kullanılmaktadır. Ancak şunu da unutmayalım ki aynı
``global`` ifadesini kullanırken olduğu gibi ``nonlocal`` ifadesinde de eğer
daha üst bir alandaki değişkenin üzerinde bir değer atama işleci kullanmayacaksak
``nonlocal`` ifadesini kullanmamıza gerek yoktur. Yani değişkeni ``nonlocal`` ifadesi
olmadan da kullanabiliriz, ancak değerini değiştiremeyiz. Eğer yukarıdaki kodda ``nonlocal``
ifadesini kullanmazsak hata alırız::

    def yazıcı(mesaj):
        def yaz():
            mesaj += " Dünya"
            print(mesaj)
        return yaz

    >>> y = yazıcı("Merhaba Dünya")
    >>> y()
    Traceback (most recent call last):
      File "<pyshell#1>", line 1, in <module>
        y()
      File "C:\Users\Dinçel\Desktop\istihza.py", line 3, in yaz
        mesaj += " Dünya"
    UnboundLocalError: local variable 'mesaj' referenced before assignment

Sonuç olarak kapsayıcı fonksiyona ait değişkenleri, iç fonksiyonumuzda değiştirebilmek
için ``nonlocal`` ifadesine ihtiyacımız vardır.

Şimdi en başta konuştuğumuz ``<locals>`` konusuna geri dönüyoruz. İç fonksiyonun,
çağırılan kapsayıcı fonksiyonun yerel değişkenlerinden biri olduğunu ve
her seferinde yeniden tanımlandığını, bu yüzden de aynı işi yapsalar da
aslında farklı olan fonksiyonlar elde ettiğimizi konuşmuştuk. Ancak her seferinde
yeniden tanımlanan tek şey iç fonksiyon değildir. Kapsayıcı fonksiyonun içindeki
her değişken, dış fonksiyonun her çağırılışında baştan tanımlanır.
Bunu şu örnek üzerinden anlamaya çalışalım::

    def sayıcı():
        sayı = 0
        def say():
            nonlocal sayı
            sayı += 1
            return sayı
        return say

Kodumuzu kısaca incelersek ``say`` fonksiyonunda ``sayı`` değişkenini ``nonlocal``
hale getiriyoruz. Aynı zamanda ``say`` fonksiyonu her çağırıldığında ``sayı`` değiş-
kenini de bir arttırıp değer olarak döndürüyoruz. Şimdi kodumuzu çalıştıralım::

    >>> s = sayıcı()
    >>> type(s)
    <class 'function'>
    >>> s
    <function sayıcı.<locals>.say at 0x000001FD2213ED38>
    >>>
    >>> s()
    1
    >>> s()
    2
    >>> s()
    3
    >>> s()
    4

Gördüğünüz gibi ilginç bir şekilde ``sayıcı`` fonksiyonu çalışmış ve bitmiştir,
ancak içerisinde bulunan ``sayı`` değişkeni silinmemiştir ve geri döndürülen
``say`` fonksiyonu tarafından kullanılmaya devam etmektedir. Yani biz göremesek de
``sayı`` değişkeni hala bir yerlede saklanılıyordur. Peki normalde bir fonksiyonun
çalışması bitince yerel değişkenleri silinmez mi? Tabii ki silinir. Ancak burada ``say``
fonksiyonu içinde ``sayı`` değişkenini ``nonlocal`` hale getirmiş oluyoruz. Yani aslında
biz ``sayı`` değişkenini kullanmaya devam ediyoruz. Eee şimdi Python kalkıp da bizim
kullanacağımız bir değişkeni silse ayıp olur. O da bunu yapmıyor zaten. Ancak
``sayı`` değişkeni iç fonksiyon olan ``say`` fonksiyonunda hiç kullanılmasaydı silinirdi. Aslında bu
örnekteki kilit olaylardan biri de ``sayı`` değişkeninin sadece bir defa tanımlanması
ve bu tanımın aynı ``say`` fonksiyonunda olduğu gibi ``sayıcı`` fonksiyonumuzun sadece bir çağırılışına özgü olması. Buradan iki sonuca varıyoruz:

* ``sayıcı`` sınıfını birden fazla defa çağırsak bile geri döndürülen her ``say`` fonksiyonu ekrana sayıları hep sırayla yazdıracaktır. Çünkü her ``say`` fonksiyonu kendisini tanımlayan ``sayıcı`` çağırılışına ait olan ``sayı`` değişkenini kullanmaktadır.
* Her ``say`` fonksiyonunun kullandığı ``sayı`` değişkeni sadece bir defa ``0`` olarak tanımlanmakta ve daha sonra ``say`` fonksiyonumuzu her çağırışımızda artmaktadır.

Evet dediğimiz gibi farklı ``say`` fonksiyonları farklı ``sayı`` değişkenlerini kullanıyor::

    >>> s = sayıcı()
    >>> s()
    1
    >>> s()
    2
    >>> s()
    3
    >>> s()
    4
    >>>
    >>> s2 = sayıcı()
    >>> s2()
    1
    >>> s2()
    2
    >>> s2()
    3
    >>> s2()
    4

Eğer bu örnekleri anlamakta zorluk çektiyseniz bunun çalışma mantığı olarak şunun ile aynı olduğunu söyleyebiliriz::

    sayı = 0
    def say():
        global sayı
        sayı += 1
        print(sayı)

    >>> s = say
    >>> s()
    1
    >>> s()
    2
    >>> s()
    3
    >>> s()
    4

``global`` deyimi ile yaptığımız bu örneğin ``nonlocal`` ile yaptığımız örnekten belki de en önemli
farkı, ``nonlocal`` örneğinde ``sayı`` değişkenine doğrudan erişememizdir. Ama ``sayı`` değişkenini ``say`` fonksiyonu tarafından kullanılmaktadır. Ancak bizim ``sayı`` değişkenine bizzat erişememiz, gördüğümüz gibi, silindiği anlamına gelmiyor...


İç İçe Fonksiyonların Kullanım Alanları
========================================

Şu ana kadar iç içe fonksiyonların nasıl tanımlandığını ve nasıl çalıştığını öğrendik.
Ancak öğrenme aşamasında olduğumuz için buraya kadar hep basit örnekler verdik.
Şimdi bazı işe yarar örnekler vereceğiz ve ne zaman içe içe fonksiyon kullanıp ne zaman normal fonksiyonlar
kullanmamızın daha doğru olacağını konuşacağız.

Öncelikle şunu söyleyelim ki iç içe fonksiyonların en fazla kullanıldığı yer bezeyicilerdir.
Bu daha sonra göreceğimiz bir konu ancak orada iç içe fonksiyonları çok fazla kullanacağız, haberiniz olsun.

İç içe fonksiyonlar bazı işlemleri daha verimli yapmamızı sağlayabileceği gibi bazı işlemleri de
(yanlış veya gereksiz yere kullanırsak) yavaşlatırlar. Mesela şu fonksiyona bakalım::

    def işlem_yap(sayı, bölen, *eklenenler):
        sonuç = sayı / bölen

        for i in eklenenler:
            sonuç += i

        return sonuç

Bu fonksiyonumuz aldığı ``sayı`` parametresini ``bölen`` parametresi ile böldükten sonra geriye kalan bütün parametreleri sonuca ekleyip geri döndürüyor. ``*eklenenler``'in ne anlama geldiğini zaten daha önce öğrenmiştik. şimdi bu fonksiyonu kullanalım::

    >>> işlem_yap(10, 2, 5, 7)
    17.0
    >>> işlem_yap(8, 4, 1, 3)
    6.0

Şimdi diyelim ki biz yazdığımız programda farklı ``sayı`` ve ``bölen`` parametreleri ile hep aynı ``eklenenler`` parametrelerini kullanacağız. Yani şunun gibi işlemler yapacağız::

    >>> işlem_yap(4, 2, 1, 4, 5)
    12.0
    >>> işlem_yap(60, 12, 1, 4, 5)
    15.0
    >>> işlem_yap(48, 4, 1, 4, 5)
    22.0
    >>> işlem_yap(12, 6, 3, 6, 2)
    13.0
    >>> işlem_yap(12, 4, 3, 6, 2)
    14.0
    >>> işlem_yap(105, 15, 3, 6, 2)
    18.0

Burada görebileceğimiz gibi aynı ``eklenenler`` değerleri çoklukla kullanılıyor. Böyle bir durumda toplama işlemini her seferinde gerçekleştirmemiz gereksiz oluyor. Bu işlemin sadece bir defa yapılmasını şu şekilde sağlayabiliriz::

	def işlem_yapıcı(*eklenenler):
	    ekle = 0
	    for i in eklenenler:
	        ekle += i

	    def işlem(sayı, bölen):
	        return sayı/bölen + ekle

	    return işlem

Bu kodumuzda ``işlem_yapıcı`` fonksiyonu hep aynı olacağı için değişmeyecek olan ``eklenenler`` parametresini sadece bir defa alıyor ve hepsini topluyor, daha sonra ``işlem`` fonksiyonunu geri döndürüyor. ``işlem`` fonksiyonunu çağırdığımızda da ``sayı`` ve ``bölen`` parametrelerini veriyoruz ve işlemin sonucu bize geri dönüyor. İlk yaptığımız işlemleri bir de böyle kullanalım::

	>>> işlemci = işlem_yapıcı(1, 4, 5)
	>>> işlemci2 = işlem_yapıcı(3, 6, 2)
	>>> işlemci(4, 2)
	12.0
	>>> işlemci(60, 12)
	15.0
	>>> işlemci(48, 4)
	22.0
	>>> işlemci2(12, 6)
	13.0
	>>> işlemci2(12, 4)
	14.0
	>>> işlemci2(105, 15)
	18.0

Artık gerekli işlemi yapacak fonksiyonu sadece bir defa oluşturuyoruz ve sürekli onu kullanıyoruz. Bu da aynı parametrelerin sürekli fonksiyona parametre olarak yollanmasını engelliyor ve gerekli işlemlerin sadece bir defa yapılmasını sağlıyor. Kendi yazdığınız kodlarda herhangi bir amaç ile bir fonksiyon oluşturduğunuzda ve bu fonksiyonu da kullanırken bunun gibi bir durum ile karşılaştırdığımızda artık iç içe fonksiyonları kullanarak kodu nasıl daha verimli hale getireceğiniz hakkında aklınızda bir fikir oluşmuştur diye düşünüyorum.

Şimdi de bir fonksiyon oluştururken o fonksiyonun içinde kod tekrarları yaptığımız fark ettiğimizi varsayalım. Böyle bir durumda bu kod tekrarlarını da azaltmak için bir fonksiyon daha yazmamız iyi olacaktır. Yani::

	def dosyadaki_karakter_sayısı(dosya, karakter):
	    sonuç = 0

	    if type(dosya) == str:
	        with open(dosya, "r") as f:
	            veri = f.read()
	            for i in veri:
	                if i == karakter:
	                    sonuç += 1
	    else:
	        veri = dosya.read()
	        for i in veri:
	            if i == karakter:
	                sonuç += 1

	    return sonuç

Elimizde bir dosyayı okuyacak ve bu dosyadaki belli bir karakterin sayını döndürecek bir fonksiyon var. Ama bu fonksiyon ``dosya`` parametresi olarak hem dosyanın ismini hem de açılmış bir dosyanın kendisini alabiliyor. `if type(dosya) == str:` kısmı ``dosya``
değişkeninin türünün ``str`` olup olmadığını kontrol ediyor, eğer öyleyse dosyayı açıyoruz ve okuyoruz. Öyle değilse dosyayı direkt okuyoruz. Dikkat ederseniz daha sonra yapılan işlemler aynı, yani::

    for i in veri:
        if i == karakter:
            sonuç += 1

kısmı iki defa tekrar ediyor. Hatırlarsanız bir karakter dizisinin içinde herhangi bir karakterin kaç defa geçtiğini öğrenmek için ``count`` metodundan faydalanabiliriz::

	>>> "merhaba".count("a")
	2

Ama burada örneğimiz anlaşılsın diye bunu kendimiz yapıyoruz.

Şimdi yukarıdaki tekrar eden yeri şu şekilde ayrı bir fonksiyon haline getirebiliriz::

	def karakter_sayısı(karakter_dizisi, karakter):
	    sayaç = 0
	    for i in karakter_dizisi:
	        if i == karakter:
	            sayaç += 1
	    return sayaç

	def dosyadaki_karakter_sayısı(dosya, karakter):
	    if type(dosya) == str:
	        with open(dosya, "r") as f:
	            return karakter_sayısı(f.read(), karakter)
	    else:
	        return karakter_sayısı(dosya.read(), karakter)

Artık karakter dizisinin içinde bir karakterin kaç defa geçtiğini bulmak için ``karakter_sayısı`` sayısı adlı fonksiyon yararlanıyoruz. Ancak bizim bu fonksiyonu tanımlama sebebimiz `dosyadaki_karakter_sayısı` fonksiyonunda yaptığımız bir işlemi yerine getirmekdi. Eğer ``karakter_sayısı`` fonksiyonunu programımızda sadece ``dosyadaki_karakter_sayısı`` fonksiyonu içinde kullanacaksak bu fonksiyonu global alanda tanımlamamıza gerek yokü, `dosyadaki_karakter_sayısı` fonksiyonunun içinde de tanımlayabiliriz::

	def dosyadaki_karakter_sayısı(dosya, karakter):

	    def karakter_sayısı(karakter_dizisi):
	        sayaç = 0
	        for i in karakter_dizisi:
	            if i == karakter:
	                sayaç += 1
	        return sayaç

	    if type(dosya) == str:
	        with open(dosya, "r") as f:
	            return karakter_sayısı(f.read())
	    else:
	        return karakter_sayısı(dosya.read())

Ayrıca bu şekilde ``karakter_sayısı`` fonksiyonunun ``karakter`` şeklinde bir parametreye ihtiyacı kalmadı, zaten
`dosyadaki_karakter_sayısı` fonksiyonunun içindeki ``karakter`` değişkenine erişebiliyor. İç içe fonksiyonları bunun gibi durumlarda da kullanabiliriz.


Üreteçler (*Generators*)
**************************

Biz üreteçlerle az çok tanışıyoruz. Liste üreteçleri olsun, sözlük üreteçleri
olsun bu konu hakkında bir şeyler öğrenmiştik. Ancak biz üreteçlerimizi hep
şunun gibi tanımlamıştık::

	>>> listem = [i for i in range(10)]
	>>> listem
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Dikkat ederseniz burada ``i for i in range(10)`` kısmı (nasıl ``lambda`` fonksiyonlar normal yolla tanımlanan fonksiyonlardan farklı bir söz dizimi kullanıyorsa) normal kodlardan biraz farklı bir söz dizimi kullanıyor. Bu söz dizimi ile karmaşık
algoritmalar oluşturmak zordur, çoğunlukla da mümkün değildir. Zaten bunun bulunma sebebi
karmaşık algoritmalarda kullanılması değil, kısa işlerde yazım kolaylığı sağlamasıdır.
Yani bu yazım şekli, bazı fonksiyonların ``lambda`` olarak tanımlanması gibi,
üreteç tanımlamanın sadece kısa bir yoludur. Peki aslında üreteçler nasıl
tanımlanır? Şimdi gelin bu konuyu inceleyelim.

Üreteçlere Giriş
==================

Üreteçler, fonksiyonlara benzer şekilde tanımlanır. Hatta tek farkının ``yield``
adındaki bir ifade olduğunu söyleyebiliriz. Hatırlarsanız iç içe fonksiyonlar
konusunda üreteçler konusuna birkaç defa atıfta bulunmuştuk.
Bu yüzden aynı işi yapacak iç içe bir fonksiyon ile bir üreteci karşılaştırarak
konuya başlamak istiyorum::

    def fonksiyon_sayıcı():
        sayı = 0
        def say():
            nonlocal sayı
            sayı += 1
            return sayı
        return say

    def üreteç_sayıcı():
        sayı = 0
        while True:
            sayı += 1
            yield sayı

Endişe etmeyin. İleride ``üreteç_sayıcı``'nın nasıl çalıştığını inceleyeceğiz.
Şimdilik sadece şuraya odaklanalım::

	>>> type(fonksiyon_sayıcı)
	<class 'function'>
	>>> type(üreteç_sayıcı)
	<class 'function'>

	>>> fonk = fonksiyon_sayıcı()
	>>> üreteç = üreteç_sayıcı()

	>>> type(fonk)
	<class 'function'>
	>>> type(üreteç)
	<class 'generator'>

	>>> fonk()
	1
	>>> fonk()
	2
	>>> fonk()
	3
	>>> fonk()
	4

	>>> next(üreteç)
	1
	>>> next(üreteç)
	2
	>>> next(üreteç)
	3
	>>> next(üreteç)
	4

``fonk`` ve ``üreteç`` değişkenlerini kullanarak elde ettiğimiz sonuçların aynı olduğunu görebiliyorsunuz. Şimdi
bundan faydalanarak tanımlanma şekillerini anlamaya çalışalım.

``fonk`` fonksiyonunun nasıl çalıştığını zaten iç içe fonksiyonlar konusunda gördük.
Şimdi ``next`` fonksiyonu ve ``yield`` deyimi ile alakalı konuşalım. Öncelikle
şunu söylemek gerekir ki ``next`` fonksiyonu, gömülü bir fonksiyondur. Ne işe yaradığını anlamak
için ise ``yield`` deyimini anlamamız gerekiyor. Eğer kodumuzu ve aldığımız
çıktıları incelerseniz ``yield`` deyiminin, ``return`` deyimine bazı yönlerden
benzediğini fark edebilirsiniz. Tabii önemli farklılıklar da var. Bir kere
fark edeceğiniz gibi ``yield`` deyimi hangi değeri döndüreceğimizi
belirliyor. Peki bu döndürme işleminin ``return`` ile değer döndürmekten
ne farkı var? Bir fonksiyonun içinde ``return`` deyimine ulaşıldığında
fonksiyon sonlanır ve fonksiyona ait yerel değişkenler silinir. ``yield`` deyiminde böyle
bir şey söz konusu değildir. Aynı iç içe fonksiyonlarda iç fonksiyonunun dış fonksiyondaki değişkeni kullanması gibi
üreteçlerin de yerel değişkenleri Python tarafından saklanır. Ancak üreteçlerde
belli değişkenler değil, yerel değişkenlerin tamamı saklanır. Şimdi yukarıdaki örnekte şu üç kısma
tekrar bakarsak::

	>>> type(fonksiyon_sayıcı)
	<class 'function'>
	>>> type(üreteç_sayıcı)
	<class 'function'>

	>>> fonk = fonksiyon_sayıcı()
	>>> üreteç = üreteç_sayıcı()

	>>> type(fonk)
	<class 'function'>
	>>> type(üreteç)
	<class 'generator'>

Şunu görüyoruz ki ``üreteç_sayıcı`` aslında bir fonksiyon. Ama alelade bir
fonksiyon değil, çağrıldığında ``generator`` nesnesi döndüren bir fonksiyon.
Yani aynı iç içe fonksiyonlarda önce kapsayıcı fonksiyonu çağırıp dönüş değerini kullandığımız
gibi üreteçlerde de önce üreteci tanımladığımız fonksiyonu çağırıp dönüş değerini
kullanıyoruz. Çünkü aslında üreteç olan nesne, bu döndürülen değerdir. Ve aynı
iç içe fonksiyonlarda olduğu gibi bu durum birbirinden bağımsız ancak aynı işi
yapan değişkenler oluşturmamızı sağlar. Dikkat ederseniz iç içe fonksiyonlar ve
üreteçler, çalışma prensibi açısından benzerler. Ancak üreteçler ``yield`` ifadesininin
kullanımı ile bize daha kullanışlı bir algoritma şekli vermektedir.

Şu ana kadar üreteçlerin nasıl tanımlandığı ve nasıl kullanıldığı hakkında pek de bilgi
vermedik. Yaptığımız şey, iç içe fonksiyonlar ile üreteçlerin, çalışma
prensiblerinin ne kadar benzer olduğuna dikkat çekmek idi. Şimdi ``next`` fonksiyonu ve
``yield`` deyimi hakkında konuşarak kendi üreteçlerimizi nasıl tanımlayacağımıza
bakalım.

Üreteçlerin Tanımlanması
=========================


'yield' Deyimi ve 'next' Fonksiyonu
-----------------------------------------

``next`` fonksiyonunun gömülü bir fonksiyon olduğunu söylemiştik. ``yield`` deyimi da
üretecimizden değer döndürmemizi sağlıyordu. Peki bu işlemler hangi kurallar çerçevesinde
gerçekleşiyor?

Basit bir üreteç tanımlayarak ``yield`` metodunu anlatmaya çalışalım::

	def üreteç():
		yield "Merhaba"
		yield "Dünya"

``return`` deyiminin fonksiyonu sonlandırırken ``yield`` deyimi üretecin çalışmasına ara
verir ve sağındaki değişkeni geriye döndürür. Herhangi bir değer verilmemiş ise ``None`` döndürecektir.
Şimdi kodumuzu çalıştıralım::

	>>> g = üreteç()
	>>> next(g)
	"Merhaba"
	>>> next(g)
	"Dünya"
	>>> next(g)
	Traceback (most recent call last):
	  File "<pyshell#5>", line 1, in <module>
	    next(g)
	StopIteration

Çıktımızı incelersek ``next`` fonksiyonunun, kendisine verilen üretecin kodunu bir ``yield`` deyimine
rastlayana kadar çalıştırdığını, ``yield`` deyimine rastladığında ise deyimin sağındaki
değişkeni döndürdüğünü görebiliriz. Unutmayalım ki bu döndürme işlemini yapan ``next`` fonksiyonudur.
Üretecimizin içinde herhangi bir yönerge kalmadığında ise ``next`` fonksiyonumuz ``StopIteration``
hatası yükseltmektedir.

.. note:: 'next' fonksiyonunun burada yaptığı iş için 'yineleme (iteration)' terimi kullanılır.
          'next' fonksiyonuna parametre olarak verilebilen nesneler ise birer 'yinelenebilir nesne
          (iterable object)'dir. 'generator' sınıfı yinelenebilir nesnelere bir örnektir.

Bir örnek daha yapalım::

    def üreteç():
        print("üreteç ilk defa next fonksiyonu ile kullanıldı.")
        yield "1. yield"
        print("üreteç ikinci defa next fonksiyonu ile kullanıldı.")
        yield "2. yield"
        print("üreteç üçüncü defa next fonksiyonu ile kullanıldı ve bitti.")

    >>> g = üreteç()
    >>> ilk_dönüş = next(g)
    üreteç ilk defa next fonksiyonu ile kullanıldı.
    >>> ikinci_dönüş = next(g)
    üreteç ikinci defa next fonksiyonu ile kullanıldı.
    >>> son_dönüş = next(g)
    üreteç üçüncü defa next fonksiyonu ile kullanıldı ve bitti.
    Traceback (most recent call last):
      File "<pyshell#5>", line 1, in <module>
        next(g)
    StopIteration
    >>>
    >>> ilk_dönüş
    '1. yield'
    >>> ikinci_dönüş
    '2. yield'
    >>> son_dönüş
    Traceback (most recent call last):
      File "<pyshell#0>", line 1, in <module>
        son_dönüş
    NameError: name 'son_dönüş' is not defined

Örneğimiz gayet açık. ``next`` fonksiyonu kendisine verilen üretecin kodunu en sol kaldığı yerden çalıştırmaya devam ediyor, bir ``yield`` ifadesine denk geldiğinde de üretecin çalışması duruyor ve ``next`` fonksiyonu ``yield`` deyiminin sağındaki değeri geri döndürüyor. Tabii ``son_dönüş``'ün ``None`` olmak yerine tanımlanmamış olması da ilginç gelmiş olabilir. Bunu da şu örnekle açıklayabiliriz::

    >>> def hata():
            raise Exception

    >>> dönüş = hata()
    Traceback (most recent call last):
      File "<pyshell#8>", line 1, in <module>
        dönüş = hata()
      File "<pyshell#7>", line 2, in hata
        raise Exception
    Exception
    >>> dönüş
    Traceback (most recent call last):
      File "<pyshell#9>", line 1, in <module>
        dönüş
    NameError: name 'dönüş' is not defined

Gördüğümüz gibi ``son_dönüş`` değişkenimizin tanımlanmamış olmasının sebebi de ``next``
fonksiyonunun değer döndürmek yerine hata yükseltmiş olmasıdır.

Buraya kadar yaptığımız örnekleri iç içe fonksiyonlar ile de kolayca yapabilirdik. Üreteçlerin
önemli bir özelliği de tanımlanırken , fonksiyonlar gibi, her türlü ifade ile kullanılabilmesidir.
Örnek olarak ``while`` döngüsü kullanarak, 1'den başlayarak her yinelediğimizde fibonacci
sayı dizisinin bir sonraki elemanını döndürecek bir üreteç yazalım::

    def fibonacci():
        x = 1
        y = 0
        z = 0
        while True:
            z = y
            y = x
            x = y + z
            yield x

.. note:: Fibonacci dizisi, 0 ve 1 ile başlayan ve her sayının kendisinden önce gelen
		  iki sayının toplanması ile elde edildiği bir sayı dizisidir. İtalyan matematikçi
		  Leonardo Fibonacci'den adını alır. 0, 1, 1 (0+1), 2 (1+1), 3 (1+2), 5 (2+3), 8 (3+5), 13 (5+8), 21 (8+13), 34 (13+21)
		  şeklinde devam eder.

Şimdi bu kodu çalıştıralım::

	>>> f = fibonacci()
	>>> next(f)
	1
	>>> next(f)
	2
	>>> next(f)
	3
	>>> next(f)
	5
	>>> next(f)
	8
	>>> next(f)
	13

Gördüğünüz gibi üretecimiz bize (ilk 0 ve 1 sonrasındaki) fibonacci sayılarını vermektedir. Kodumuzu anlamaya çalışırsak:

* İlk yinelemede, yani ``next`` fonksiyonunu ilk kullanışımızda, ``x``, ``y`` ve ``z`` değişkenleri tanımlanıyor. Daha sonra ``while`` döngüsüne giriliyor. Değişkenlerin değerleri değiştirildikten sonra ``yield x`` deyimine geldiğimiz için ``next`` fonksiyonu ``x`` değerini döndürürerek üretecemizin çalışmasını durduruyor.
* İkinci yinelememizde normal bir kodda olacağı gibi ``while`` döngümüzün başına gidiliyor. Aynı işlemler tekrarlanıyor. Tekrar ``yield`` deyimine geliniyor. ``x`` değeri döndürürülüyor. Üretecimizin çalışması durduruluyor ve aynı şeyler tekrar etmeye devam ediyor.

Üreteçlerin çok güzel özelliklerinden biri de ``for`` döngüsü ile kullanılabilmeleridir.
Örneğin ``fibonacci`` üretecimiz için bunu uygulayalım::

    >>> for i in fibonacci():
        print(i)

    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    ...

.. note:: ``for i in fibonacci()`` ifadesinde ``fibonacci`` fonksiyonunu çağırdığımıza dikkat
		  edin. Sonuçta üretecimizin kendisi ``fibonacci`` fonksiyonu değil, onun döndüreceği değer.

Ancak bu örnekte üretecimiz hiç durmuyor. Bazen üreteçlerimizin durmasını isteyebiliriz.
Bunu yapmamız için tek gereken şey üretecimizin durmasını istediğimiz yerde üretecimizi
``return`` etmemizdir. Sonuçta üreteçler de bir tür fonksiyondur ve ``return`` deyimi
fonksiyonları sonlandırır (bu ``return`` deyiminden dönen değer üreteçlerde bize ulaşmaz).
Bu durum ``next`` fonksiyonunun ``StopIteration`` yükseltmesine neden olur.
``for`` döngüsü bu hatayı yakalar ve üretecimizin bittiğini anlar::

    def fibonacci():
        x = 1
        y = 0
        z = 0
        while True:
            z = y
            y = x
            x = y + z
            yield x
            if x > 100:
                return


    >>> for i in fibonacci():
            print(i)

    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    144
    >>>

Gördüğünüz gibi üretecimiz ``100``'den büyük bir tane daha değer yazıp durdu. Tabii burada
fazladan bir ``if`` kullanmak yerine bu şartı ``while``'dan sonra da yazabilirdik::

    def fibonacci():
        x = 1
        y = 0
        z = 0
        while not x > 100:
            z = y
            y = x
            x = y + z
            yield x

Burada da ``x`` değişkeni ``100``'den büyük olduğunda döngümüz bitiyor ve başka kodumuz kalmadığımız için
fonksiyon sonlanıyor. Zaten bir fonksiyonun sonuna ulaşıldığında da biz bir değer döndürmediysek de
``None`` değeri döndürülecektir.

Son olarak parametre alan basit bir üreteç örneği yaparak bir sonraki konuya geçelim.
Unutmayalım ki üreteçler de bir çeşit fonksiyon olduğu için fonksiyon tanımlarken yapabildiğimiz
her şeyi üreteç tanımlarken de kullanabiliriz. Buna parametre vermek ve iç içe
fonksiyonlar oluşturmak da dahildir.

Üretecimiz bir ``sayı`` parametresi alacak ve o ``sayı`` defa ekrana yazı yazdıracak::

    def yaz(sayı):
        for i in range(sayı):
            print("Merhaba Dünya!")
            yield

    y = yaz(4)
    for i in y:
        print(i)

Kodun çıktısı::

	Merhaba Dünya!
	Merhaba Dünya!
	Merhaba Dünya!
	Merhaba Dünya!


'yield from' Deyimi
--------------------

``yield from`` deyimi bir üretecin içinde, başka bir üretecin ``yield`` ile
döndüreceği değerleri tekrar ``yield`` etmek istediğimizde kullanılabilir.
Şöyle bir örnek verelim::

    def üreteç1():
        yield "üreteç1 başladı"
        yield "üreteç1 bitti"

    def üreteç2():
        yield "üreteç2 başladı"
        yield from üreteç1()
        yield "üreteç2 bitti"

    >>> for i in üreteç2():
            print(i)

    üreteç2 başladı
    üreteç1 başladı
    üreteç1 bitti
    üreteç2 bitti
    >>>

Aslında ``yield from`` ile yazdığımız bu örnek şu kod ile eşdeğerdir::

    def üreteç1():
        yield "üreteç1 başladı"
        yield "üreteç1 bitti"

    def üreteç2():
        yield "üreteç2 başladı"
        for i in üreteç1():
            yield i
        yield "üreteç2 bitti"

    >>> for i in üreteç2():
            print(i)

    üreteç2 başladı
    üreteç1 başladı
    üreteç1 bitti
    üreteç2 bitti
    >>>

Yani::

	yield from bir_üreteç

ifadesi bu ifade eş değerdir::

    for i in bir_üreteç:
        yield i


Liste ve Sözlük Üreteçleri Hakkında
============================================================

Üreteçler konusunun başında söylediğimiz şu bilgiyi tekrarlayarak konumuza başlayalım:

	Biz üreteçlerle az çok tanışıyoruz. Liste üreteçleri olsun, sözlük üreteçleri
	olsun bu konu hakkında bir şeyler öğrenmiştik. Ancak biz üreteçlerimizi hep
	şunun gibi tanımlamıştık::

		>>> listem = [i for i in range(10)]
		>>> listem
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	Dikkat ederseniz burada ``i for i in range(10)`` kısmı (nasıl ``lambda`` fonksiyonlar normal yolla tanımlanan fonksiyonlardan farklı bir söz dizimi kullanıyorsa) normal kodlardan biraz farklı bir söz dizimi kullanıyor. Bu söz dizimi ile karmaşık
	algoritmalar oluşturmak zordur, çoğunlukla da mümkün değildir. Zaten bunun bulunma sebebi
	karmaşık algoritmalarda kullanılması değil, kısa işlerde yazım kolaylığı sağlamasıdır.
	Yani bu yazım şekli, bazı fonksiyonların ``lambda`` olarak tanımlanması gibi,
	üreteç tanımlamanın sadece kısa bir yoludur. Peki aslında üreteçler nasıl
	tanımlanır? Şimdi gelin bu konuyu inceleyelim.

Biz önceden üreteçleri şu şekilde kullanmayı biliyorduk::

	>>> listem = [i for i in range(10)]
	>>> listem
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Peki üreteç bu kodun neresinde? Aslında bu yazım oldukça kısaltılmış, yani kolaylaştırılmış
bir yazım şeklidir. Biraz açacak olursak şunu elde ederiz::

	>>> üreteç = (i for i in range(10))
	>>> type(üreteç)
	<class 'generator'>
	>>> listem = list(üreteç)
	>>> listem
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Şimdilik liste kısmını bir kenara koyarak üreteç kısmı ile ilgilenelim.

Gördüğünüz gibi aslında şu yazım şekli::

	>>> üreteç = (i for i in range(10))

Bunun için bir kısaltmadır::

    def üreteç_fonksiyonu():
        for i in range(10):
            yield i

    üreteç = üreteç_fonksiyonu()

Aynı ``lambda`` fonksiyonların normal fonksiyonlar için bir kısaltma olması gibi.

Ancak şuraya dikkat etmek lazım ki::

	üreteç = (i for i in range(10))

Yazdığımızda, elimizde çağırıldığında bize üreteç döndürecek bir fonksiyonumuz yok.
Yani ``üreteç`` değişkenimiz ``generator`` türünde bir nesne ve tek kullanımlık.
Sonuçta üreteçlerin yinelenmesi bir defa bittikten sonra bir daha kullanamayız, çünkü bir defa bittikten sonra hep ``StopIteration`` hatası yükseltirler. Eğer istersek yenisini oluşturabiliriz. ``üreteç`` değişkenimizin yinelenmesi bir defa tamamlandıktan sonra daha fazla onu kullanamayacağımızı şu şekilde görebiliriz::

	>>> üreteç = (i for i in range(5))
	>>> for i in üreteç:
		print(i)
	0
	1
	2
	3
	4
	>>> for i in üreteç:
		print(i)

	>>>

Gördüğünüz gibi ``üreteç`` değişkenimizi bir defa ``for`` döngüsü ile kullandığımızda
ikinci defa kullanamamaktayız. Çünkü ilk döngüde üretecimiz bitene kadar çalıştı
ve en sonunda ``StopIteration`` yükseltti. Artık istediğimiz kadar üretecimizi
kullanmayı deneyelim, ``StopIteration`` yükseltmeye devam edecektir (unutmayalım ki ``for`` döngüsü
``StopIteration`` hatalarını yakalar ve yakaladığında da çalışmayı bırakır) ::

	>>> üreteç = (i for i in range(3))
	>>> next(üreteç)
	0
	>>> next(üreteç)
	1
	>>> next(üreteç)
	2
	>>> next(üreteç)
	StopIteration
	>>> next(üreteç)
	StopIteration

Aynı şey normal yoldan tanımlanan üreteçler için de geçerlidir::

    def üreteç_fonksiyonu():
        for i in range(3):
            yield i


    >>> üreteç = üreteç_fonksiyonu()
    >>> next(üreteç)
    0
    >>> next(üreteç)
    1
    >>> next(üreteç)
    2
    >>> next(üreteç)
    StopIteration
    >>> next(üreteç)
    StopIteration

Buradaki fark üretecimizi bize veren fonksiyonumuz durduğu için yeni bir üreteç oluşturabiliyor
olmamızdır::

	>>> üreteç2 = üreteç_fonksiyonu()
	>>> next(üreteç2)
	0

Ancak şu şekilde bir tanımlama yaptığımızda::

	>>> üreteç = (i for i in range(3))
	>>> type(üreteç)
	<class 'generator'>

Burada elde ettiğimiz üretecin kendisi oluyor, ve bu üreteç de tek kullanımlık. Şimdi
bunların liste üreteçleri ile alakasına geri dönecek olursak::

	>>> üreteç = üreteç_fonksiyonu()
	>>> listem = list(üreteç)
	>>> listem
	[0, 1, 2]

Gördüğünüz gibi aslında normal yoldan tanımlanmış üreteçler, yani ``yield`` ifadesi kullanılarak fonksiyon gibi tanımlanmış üreteçler, de ``list`` fonksiyonuna argüman olarak verilebilir. Aynı
``for`` döngüsünde kullanılabilmesi gibi. Çünkü -kendi geliştirme arayüzünüzü kullanarak
görebilirsiniz- dikkat edersiniz ``list`` fonksiyonunun ilk parametresinin adı ``iterable``'dır.
Türkçe'ye çevirirsek *yinelenebilir*. Biz zaten üreteçlerin yinelenebilir nesnelere örnek olduğunu
söylemiştik. Bu yüzden bütün üreteçleri ``list`` fonksiyonunu kullanarak bir listeye çevirebiliriz.
Buna şu şekilde tanımlanan üreteçler de dahildir::

	>>> üreteç = (i for i in range(3))

Bu yüzden şu kod güzel bir şekilde çalışmaktadır::

	>>> üreteç = (i for i in range(3))
	>>> list(üreteç)
	[0, 1, 2]

Ve şu yazım da yukarıda yazdığımızın daha da kısaltılmış halinden başka bir şey değildir::

	>>> listem = [i for i in range(3)]

Anlattıklarımız sözlük üreteçleri için de geçerlidir. Dikkat edersiniz kısa yoldan üreteç
tanımlamaları ``(i for i in range(3))`` şeklinde, liste tanımlamaları ``[i for i in range(3)]`` şeklinde
ve sözlük tanımlamaları da ``{str(i):i for i in range(3)}`` şeklinde yapılmaktadır. Bu liste tanımlamasını::

	>>> üreteç = (i for i in range(3))
	>>> listem = list(üreteç)

Şu şekilde yazabileceğimiz gibi::

	>>> üreteç = (i for i in range(3))
	>>> listem = []
	>>> for i in üreteç:
		listem.append(i)

Bu sözlük tanımlamasını da::

	>>> üreteç = ((str(i),i) for i in range(3))
	>>> sözlük = dict(üreteç)

Şu şekilde yazabilirdik::

	>>> üreteç = ((str(i),i) for i in range(3))
	>>> sözlük = {}
	>>> for key,value in üreteç:
		sözlük[key] = value

Son örneğimizde üretecimiz her yinelenişinde iki elemanlı bir ``tuple`` döndürüyor ve
bu demetin ilk elemanı ``for`` döngüsü içinde ``key`` değişkenine, ikinci elemanı ise
``value`` değişkenine atanıyor. Şunun gibi de düşünebilirsiniz::

	>>> for key,value in (('0',0), ('1',1), ('2',2)):
		sözlük[key] = value

Evet, artık üreteçler konusunda da kayda değer bilgiler öğrendiğimize göre bir sonraki konumuza geçelim.
