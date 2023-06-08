.. meta:: :author: Buğra İşgüzar <biisguzar@gmail.com>
          :description: Bu bölümde Python'daki f-string yapısından ve özelliklerinden
           söz edeceğiz.
          :keywords: python, f-string, formatted string

.. highlight:: py3

****************
f-string
****************

Daha önceki bölümlerde **format()** fonksiyonuyla karakter dizilerini nasıl biçimlendirebileceğimizi görmüştük. 3.6 sürümü ile Python'a eklenen f-string yapısı da buna benzer bir şekilde çalışıyor. Öncelikle format() fonksiyonunu nasıl kullandığımızı hatırlayalım::

        isim = 'Buğra'
        print('Selam {kime}!'.format(kime=isim))

Burada öncelikle *isim* adında bir değişken tanımladık ve bu değişkene *Buğra* değerini atadık. Daha sonra da *'Selam {isim}!'* diye bir karakter dizisini ekrana yazdırdık. format() fonksiyonunu kullanarak Python'a yazdırma işlemini yapmadan önce karakter dizimizdeki *kime* kısımını *isim* değişkeninin değeri ile değiştirmesi gerektiğini söyledik.

format() fonksiyonumuz kendisine verdiğimiz değerleri kapsama alanı içerisinde uygun yerlere yerleştirir. Hatırlarsanız format() fonksiyonunu ilgilendiren kısımları süslü parantezlerin içine yazıyorduk. Yukarıdaki örneği şu şekilde de yapabiliriz::

        isim = 'Buğra'
        print('Selam {}!'.format(isim))

Bu sefer format() fonksiyonuna belirli bir yer göstermediğimiz için sırasıyla ilgili alanlara verdiğimiz parametreleri dolduracak. Zaten bir parametre ve bir alan olduğu için yukarıdaki örnekle aynı çıktıyı alacağız. format() fonksiyonunu bu kadar hatırlamak yeter, hadi f-string'lere geçelim!

Kullanım
********

String nedir hepimiz biliyoruz, Türkçeye karakter dizisi olarak çeviriyoruz. Bu yapıya da f-string diyoruz çünkü bu yapıyı kullanmak istediğimiz stringin (karakter dizisinin) başına **f** veya **F** ekliyoruz. Yani bir ön ek ekleyerek Python'a artık onun normal, sıradan bir karakter dizisi olmadığını ve bir ön işlemden geçmesi gerektiğini belirtiyoruz::

        "Selam Dünya!" # Normal bir karakter dizisi
        f"Selam Dünya!" # Bu artık bir f-string

.. note:: f-string'leri kullanabilmeniz için Python 3.6 ya da daha yeni bir sürüm kullanmamız gerektiğini unutmayalım!

Bu örnekte f-string'imizin normal bir karakter dizisinden farkı yok gibi görünüyor. Aslında şuanlık bir farkı yok. Çünkü biz **f-string**'in özelliklerini henüz kullanmadık. Yukarıda format() fonksiyonu için yazdığımız örneği bir de f-string için yazalım::

        >>> isim = 'Buğra'
        >>> print(f'Selam {isim}!')

Bu örneği de çalıştırdığınızda yukarıdaki örneklerin çıktılarıyla aynı çıktıyı verdiğini göreceksiniz. Ama çok daha düzenli bir görünümle elde ettik bu sefer aynı çıktıyı. format() fonksiyonuna ilgileneceği kısımları, işlem yapacağı kısımları, süslü parantezler ile belirttiğimizi biliyoruz. f-string için de aynı şey geçerli ancak ufak bir farkla. Artık harici bir işlem yapılıp karakter dizimiz düzenlenmiyor, işlemler doğrudan karakter dizimiz içinde gerçekleştirilip yerini kendi alıyor! 

Bir örnek daha hazırlayalım ve üzerinde konuşalım::

        >>> isim = 'Buğra'
        >>> yas = 18
        >>> f'Onun adı {isim} ve o {yas} yaşında.'
        'Onun adı Buğra ve o 18 yaşında.'

Aynı örneği format() fonksiyonu ile de yazıp arasındaki farka bakalım::

        >>> isim = 'Buğra'
        >>> yas = 18
        >>> "Onun adı {} ve o {} yaşında.".format(isim, yas)
        'Onun adı Buğra ve o 18 yaşında.'

Yukarıdaki kodu en basit haliyle değişken isimleri kullanmadan yazdım, yani değişkenleri sırasıyla ilgili yerlere yerleştirecek. Buna rağmen f-string örneğimizdekinden çok daha uzun oldu ve okunabilirlik azaldı.

Aynı zamanda f-string'lerin içinde Python işlemleri de yapabiliriz::

        >>> birinci_rakam = 5
        >>> ikinci_rakam = 3
        >>> f'Rakamların toplamı {birinci_rakam + ikinci_rakam} eder.'
        'Rakamların toplamı 8 eder.'

Hadi sadece toplama işlemi yapan bir hesap makinesi yapalım::

        birinci_sayi = int(input('Birinci sayıyı girin: '))
        ikinci_sayi = int(input('İkinci sayıyı girin: '))

        print(f'Sayıların toplamı {birinci_sayi + ikinci_sayi} eder.')

Kullanıcının girdiği sayıları toplayan bir hesap makinesi yaptık. Az önce f-string'lerin içinde Python kodu yazabildiğimizi öğrenmiştik. Bu bilgimizi de kullanıp bu basit programı daha güncel hale getirelim::

        >>> f'Sayıların toplamı { int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: ")) } eder.'
        Birinci sayıyı girin: 10
        İkinci sayıyı girin: 7
        'Sayıların toplamı 17 eder.'

Kullanıcıdan girdileri f-string'in içinde alarak tek satırlık bir hesap makinesi yazmış olduk.

.. note:: f-string'in içinde Python kodu yazmak her zaman en iyi yol olmayabilir.

f-string Formatlama Özellikleri
********************************

f-string ifadelerinde süslü parantezler (``{}``) yazılan ifadenin bir operatörüdür.
f-string içerisinde süslü parantez yazabilmek için genel kaçış karakteri olan ters eğik çizgi (``\``) yerine ``{`` veya ``}`` parantezi 2 defa eklenir::

        >>> fstring = "f-string"
        >>> f"{{ {fstring}: f'{{ifade}}' şeklinde kullanılır. }}"
        "{ f-string: f'{ifade}' şeklinde kullanılır. }"

Formatlanacak ifadeden sonra ``=`` işareti eklenerek değişken adı ile birlikte sahip olduğu değerin ``repr`` hali elde edilebilir. ``print`` ile debug edildiği durumlarda pratik bir şekilde kullanılabilir:

.. code-block:: python

        >>> kaynak = "Python İstihza"
        >>> yıl = "2022"
        >>> f"{kaynak=} {yıl=}"
        kaynak='Python İstihza' yıl='2022'


``f-string`` ile formatlama yapılırken yazılan ifadeden sonra eklenen ``:``'dan sonra ek formatlama işlemleri gerçekleştirilebilir.

``string`` metodlarında anlatılan ``center``, ``ljust``, ``rjust``, ``zfill`` metodlarının f-string içerisinde ``:`` işaretinden sonra karakter uzunluğu yazılarak, belirtilen karakter alanında hizalama yapılabilir:

.. code-block:: python

        >>> istihza = "Python Istihza"
        >>> f"{istihza:^30}"   # "istihza".center(30)
        '        Python Istihza        '
        >>> f"{istihza:-^30}"  # "istihza".center(30, '-')
        '--------Python Istihza--------'
        >>> f"{istihza:30}"    # "istihza".ljust(30)
        'Python Istihza                '
        >>> f"{istihza:>30}"   # "istihza".just(30)
        '                Python Istihza'
        >>> f"{istihza:>030}"  # "istihza".zfill(30)
        '0000000000000000Python Istihza'

.. note:: Etkileşimli kabuk (interactive shell) içinde çıktıları elde etmek için print kullanımasına ihtiyaç yoktur.

``f-string`` ve ``.format`` için genel notasyon şu şekildedir:

.. code-block:: text

        [[dolgu_karakteri]hizalama][işaret][#][0][genişlik][grup_karakteri][.ondalık][veri_tıpı]

        dolgu_karakteri : <her hangi bir karakter> 
        hizalama        : "<" | ">" | "^" | "=" 
        işaret          : "+" | "-" | " " (yalnızca sayı tipi) 
        genişlik        : pozitif sayı 
        grup_karakteri  : "_" | "," (yalnızca sayı tipi) 
        ondalık         : pozitif sayı (yalnızca sayı tipi) 
        veri_tıpı       : "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%" 


Yukarıda verilen örneklerden birini kısaca açıklamak gerekirse:

.. code-block:: text

        f"{istihza:-^30}"
        dolgu_karakteri : -
        hizalama        : ^
        genişlik        : 30


Sayı formatlama örnekleri

.. code-block:: python

        >>> sayı = 123
        >>> f"{sayı:>6}"
        '   123'
        >>> f"{sayı:0>+6}"
        '00+123'
        >>> f"{sayı:0=+6}"
        '+00123'
        >>> f"Binary: {sayı:b} | Octal: {sayı:o} | Hexadecimal: {sayı:x}"
        'Binary: 1111011 | Octal: 173 | Hexadecimal: 7b'
        >>> f"Binary: {sayı:#b} | Octal: {sayı:#o} | Hexadecimal: {sayı:#x}"
        'Binary: 0b1111011 | Octal: 0o173 | Hexadecimal: 0x7b'

        >>> ondalık = 0.123
        >>> f"{ondalık:.2f}"  # f | F ondalık formatlama
        '0.12'
        >>> f"{ondalık:.5f}"  
        '0.12300'
        >>> f"{ondalık:.5g}"  # g | G fazla sıfırlar dahil edilmez
        '0.123'

        >>> sayı = 123456
        >>> f"{sayı:_}"
        '123_456'
        >>> f"{sayı:-^15_}"
        '----123_456----'
        >>> f"{sayı:,}"
        '123,456'

        >>> işlem = 1 / 12
        >>> f"{işlem:.2%}"  # Sonucun 100 ile çarpılmış halini yüzde olarak çıktı verir
        '8.33%'

Formatlama için kullanılan operatörler değişken ile kullanılması durumunda değişkenlerin ``{}`` içine yazılması gerekmektedir.

.. code-block:: python

        >>> selam = "Hello, World!"
        >>> hizalama = {"Sol": "<", "Orta": "^", "Sağ": ">"}
        >>> genişlik = 25
        >>> for hiza, operatör in hizalama.items():
        ...     print(f"{hiza:>5}: '{selam:{operatör}{genişlik}}'")
        ...
         Sol: 'Hello, World!            '
        Orta: '      Hello, World!      '
         Sağ: '            Hello, World!'        
