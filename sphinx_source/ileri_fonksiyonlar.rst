.. meta::
   :description: Bu bölümde fonksiyonlar konusunu inceleyeceğiz. 
   :keywords: python, fonksiyon, lambda, recursive, decorator, closure,
              özyinelemeli, bezeyiciler, kapalı fonksiyonlar 

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
    Eğer bu kodları çalıştıramadıysanız http://www.istihza.com/forum adresinde
    sorununuzu dile getirebilirsiniz.
    
Bu kodları çalıştırıp 'deneme' düğmesine bastığınızda komut satırında 'merhaba'
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
    print('Girdiğiniz kelimenin tersi: {}'.format(ters_çevir('istihza')))
    
Fonksiyonumuzun daha kullanışlı olabilmesi için kodlarımızı şöyle yazabiliriz::
    
    def ters_çevir(s):
        if len(s) < 1:
            return s
        else:
            return ters_çevir(s[1:]) + s[0]
              
    kelime = input('kelime girin: ')
    print('Girdiğiniz kelimenin tersi: {}'.format(ters_çevir('istihza')))
    
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

