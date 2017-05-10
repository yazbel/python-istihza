.. meta:: :description: Bu bölümde nesne tabanlı programlamadan söz edeceğiz. 
          :keywords: python, python3, nesne, oop, sınıf, class, miras alma, 
           inheritance, nesne yönelimli programlama, nesne tabanlı programlama,
           object oriented programming, self, instantiation, instance, örnek,
           örneklendirme, örnekleme
           
.. highlight:: py3

*******************************************
Nesne Tabanlı Programlama (Devamı)
*******************************************

Nesne tabanlı programlamaya ilişkin bu son bölümde önceki derslerde incelemeye
fırsat bulamadığımız ileri düzey konulardan söz edeceğiz.

İnşa, İlklendirme ve Sonlandırma
*********************************

Python'da bir sınıfın ömrü üç aşamadan oluşur: 

    #. İnşa (*Construction*)
    #. İlklendirme (*initialization*)
    #. Sonlandırma (*destruction*)
    
Biz bundan önceki derslerimizde ilklendirme sürecinin nasıl yürüdüğünü
görmüştük. Bu dersimizde ise, ilklendirme sürecine de tekrar değinmekle
birlikte, özellikle inşa ve sonlandırma süreçlerini ele alacağız.

Önceki derslerimizden de bildiğimiz gibi, Python'da bir sınıfı ilklendirmek için
``__init__()`` adlı bir metottan yararlanıyoruz. Ancak, adının aksine,
ilklendirme, sınıfların oluşturulmasına ilişkin ilk basamak değildir. Python,
bir sınıfın ilklendirilmesinden önce o sınıfı inşa eder. Bu inşa işleminden
sorumlu metodun adı ise ``__new__()``'dur. Gelin bu metodu yakından tanımaya
çalışalım.

__new__() Metodu
=====================

Bildiğiniz gibi, Python'da basit bir sınıfı şu şekilde tanımlıyoruz::
    
    class Sınıf():
        def __init__(self):
            print('merhaba sınıf!')

Burada ``__init__()`` metodu, sınıfımız örneklenir örneklenmez hangi işlemlerin
yapılacağını gösteriyor. Yani mesela ``sınıf = Sınıf()`` gibi bir kod yardımıyla
``Sınıf()`` adlı sınıfı örneklediğimiz anda ne olacağını bu ``__init__()``
metodu içinde tanımlıyoruz::
    
    >>> # Yukarıdaki kodların `sınıf.py` adlı bir dosyada olduğunu varsayalım
    >>> import sınıf
    >>> snf = sınıf.Sınıf()
    
    merhaba sınıf!
    
Gördüğünüz gibi, tam da ``__init__()`` metodunda tanımladığımız şekilde,
sınıfımızı örneklediğimiz anda ekrana 'merhaba sınıf' çıktısı verildi.

Ancak yukarıda da belirttiğimiz gibi, bir sınıf örneklendiğinde çalışan ilk
metot aslında ``__init__()`` değildir. Python bu süreçte alttan alta
``__new__()`` adlı başka bir metodu çalıştırır. Gelin bunu kanıtlayalım::
    
    class Sınıf():
        def __new__(cls):
            pass
            
        def __init__(self):
            print('merhaba sınıf')  
            
Bu sınıfı örneklediğinizde, bir önceki kodların aksine, ekrana 'merhaba sınıf'
yazısı çıktı olarak verilmeyecektir. İşte bunun sebebi, Python'ın öntanımlı
``__new__()`` metodunun üzerine yazıp, o metodun işlevselliğini ortadan
kaldırmış olmanızdır. Eğer ``__new__()`` metodunun öntanımlı davranışını taklit
etmek isterseniz yukarıdaki kodları şu şekilde yazmalısınız::
    
    class Sınıf():
        def __new__(cls, *args, **kwargs):
            return object.__new__(cls, *args, **kwargs)
            
        def __init__(self):
            print('merhaba sınıf')
            
Burada yaptığımız şeyin aslında temel olarak basit bir miras alma işleminden
ibaret olduğunu görüyor olmalısınız. Bildiğiniz gibi, Python'daki bütün
sınıflar, eğer başka bir sınıfı miras olarak almıyorlarsa, otomatik olarak
``object`` sınıfını miras alırlar. Yani aslında yukarıdaki sınıf tanımını Python
şöyle görür::
    
    class Sınıf(object):
        ...
        
Burada ``object`` taban sınıf olmuş oluyor. Bu taban sınıfın ``__new__()``
metodunun sahip olduğu işlevselliği ``Sınıf`` adlı alt sınıfa aktarabilmek için
taban sınıfı kendi ``__new__()`` metodumuz içinde çağırıyoruz::
    
    class Sınıf():
        def __new__(cls, *args, **kwargs):
            return object.__new__(cls, *args, **kwargs)
            
İşte eğer bir sınıfın inşa edilme sürecinin nasıl işleyeceğini kontrol etmek
isterseniz bu ``__new__()`` metodunun üzerine yazarak metodu değişikliğe
uğratabilirsiniz::
    
    class Sınıf():
        def __new__(cls, *args, **kwargs):
            print('Yeni sınıf inşa edilirken lütfen bekleyiniz...')
            return object.__new__(cls, *args, **kwargs)
            
        def __init__(self):
            print('merhaba sınıf')
            
Ancak bu noktada şunu belirtmeden de geçmeyelim. ``__new__()`` metodu, sık sık
muhatap olmanız gereken bir metot değil. ``__new__()`` metodunu kullanarak
yapacağınız pek çok şeyi aslında doğrudan ``__init__()`` metodu aracılığıyla da
yapabilirsiniz. 


