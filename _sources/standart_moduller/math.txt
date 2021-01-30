.. meta::
   :description: Bu bölümde math modülünü inceleyeceğiz.
   :keywords: python, math, modülü

.. highlight:: py3

***************
math Modülü
***************

math modülü matematiksel işlemler yapmanızı kolaylaştırmak için
yazılmış bir modüldür.

math.ceil()
************

Verilen ondalıklı sayıyı bir üst sayıya çevirir. Sayı eğer
tam sayı ise `__ceil__` fonksiyonundan yararlanır.
::

    >>> math.ceil(32.05)
    33
    >>> math.ceil(2.98)
    3

math.copysign()
****************

Aldığı iki parametreden ikincisinin işaretini birincisine verir.
::

    >>> math.copysign(25,-12)
    -25.0
    >>> math.copysign(-12,-15)
    -12.0
    >>> math.copysign(-245,54)
    245.0

math.fabs()
************

Verilen değerin mutlak değerini alır. Gömülü fonksiyonlardan 
`abs`'den küçük bir farkı var. Çıktısını tam sayı olarak değil 
ondalıklı sayı olarak döndürüyor.
::

    >>> math.fabs(-28)
    28.0
    >>> abs(-28)
    28

math.factorial()
****************

Verilen sayının faktoriyelini döndürüyor. Eğer verilen değer 
pozitif tam sayı değilse `ValueError` hatası veriyor.
::

    >>> math.factorial(5)
    120
    >>> math.factorial(-5)
    Traceback (most recent call last):
    File "<pyshell#10>", line 1, in <module>
        math.factorial(-5)
    ValueError: factorial() not defined for negative values

math.floor()
*************

`ceil` fonksiyonunun tam tersi bir işleve sahip. Verilen ondalıklı 
sayıyının bir altındaki tam sayıyı döndürür. Sayı eğer tam sayı ise
`__floor__` fonksiyonundan faydalanır. `int` fonksiyonundan farkı
negatif sayılarda ortaya çıkıyor.
::

    >>> math.floor(25.42)
    25
    >>> math.floor(-12.25)
    -13
    >>> int(-12.25)
    -12

math.fmod()
***********

Verdiğiniz birinci parametrenin ikinci parametreye bölümünden kalanı buluyor.
`%` operatöründen farkı negatif sayılarda ortaya çıkıyor.
::

    >>> math.fmod(45,2)
    1.0
    >>> math.fmod(45,14)
    3.0
    >>> math.fmod(45,-14)
    3.0
    >>> 45%-14
    -11

math.frexp()
************

Bu fonksiyon aşağıdaki işlemin `m` ve `e` parametrelerini 
bulmaya yarıyor. `m` değerinin mutlak değeri 0,5 ve 1 arasında
bir değer alıyor.
::

    x = m * 2 ** e

Örnek::

    >>> math.frexp(1)
    (0.5, 1)
    >>> math.frexp(8)
    (0.5, 4)

math.fsum()
***********

`sum` fonksiyonuna çok benziyor. `sum` fonksiyonundaki bir açığı
kapatıyor. `sum` fonksiyonu ondalıklı sayılarla çalışırken 
biraz sorun çıkarabiliyor.
::

    >>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    0.9999999999999999
    >>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    1.0

math.gcd()
***********

Verilen iki sayının EBOB'unu veriyor.
::

    >>> math.gcd(45,70)
    5
    >>> math.gcd(24,-24)
    24
    >>> math.gcd(36,12)
    12

math.trunc()
************

`int` fonksiyonu ile aynı işi yapıyor.
::

    >>> math.trunc(15.12)
    15
    >>> math.trunc(-15.12)
    -15
    >>> math.trunc(0.24)
    0
    >>> int(0)
    0
    >>> int(-15.12)
    -15

math.e
*******

euler sabitini tutan bir değişken. Değeri: `2.718281…`

math.pi
********

pi sayısını tutan değişken. Değeri: `3.141592…`.

math.tau
**********

tau sabitini tutan değişken. Değeri pi sayısının iki katı.
::

    >>> math.pi*2==math.tau
    True

math.exp()
***********

euler sabitinin kuvvetini alır. Yani yaptığı iş şudur:`math.e ** x`
::

    >>> math.exp(2)
    7.38905609893065

math.expm1()
*************

`math.exp` fonksiyonunun yaptığı işten tek farkı sonuçtan `1` çıkarmasıdır.
::

    >>> math.exp(12)
    162754.79141900392
    >>> math.expm1(12)
    162753.79141900392

math.log()
***********

Birinci değerin ikinci değere göre logaritmasını hesaplar.
::

    >>> math.log(10,10)
    1.0
    >>> math.log(25,5)
    2.0
    >>> math.log(5,25)
    0.5

math.log1p()
*************

Verilen sayının bir fazlasının e tabanına göre logaritmasını 
hesaplar.
::

    >>> math.log1p(0)
    0.0
    >>> math.log1p(2)
    1.0986122886681098

math.log2()
************

Verilen sayının `2` tabanında logaritmasını hesaplar.
::

    >>> math.log2(2)
    1.0
    >>> math.log2(42)
    5.392317422778761

math.log10()
*************

Verilen sayının `10` tabanında logaritmasını hesaplar.
::

    >>> math.log10(1000)
    3.0
    >>> math.log10(20)
    1.3010299956639813

math.pow()
**********

`**` ve gömülü fonksiyonlardan `pow` ile aynı işi yapıyor. Yani
birinci sayının ikinci sayıya göre kuvvetini alıyor.
::

    >>> math.pow(2,5)
    32.0
    >>> math.pow(2,0)
    1.0
    >>> pow(2,5)
    32
    >>> pow(2,0)
    1

math.sqrt()
************

Verilen sayının karekökünü hesaplar.
::

    >>> math.sqrt(16)
    4.0
    >>> math.sqrt(225)
    15.0

math.degrees()
***************

Verilen sayıyı radyandan dereceye çevirir.
::

    >>> math.degrees(1.5707963267948966)
    90.0

math.radians()
**************

Verilen sayıyı dereceden radyana çevirir.
::

    >>> math.radians(90)
    1.5707963267948966

math.sin()
***********

Radyan cinsinden verilen sayının sinüsünü hesaplar.
::

    >>> math.sin(math.radians(60))
    0.8660254037844386

math.cos()
**********

Radyan cinsinden verilen parametrenin kosinüsünü hesaplar.

math.tan()
**********

Radyan cinsinden verilen parametrenin tanjantını hesaplar.

math.asin()
***********

Verilen sinüs değerinden radyan cinsinde bir açı döndürür.

math.acos()
************

Verilen kosinüs değerinden radyan cinsinde bir açı döndürür.

math.atan()
************

Verilen tanjant değerinden radyan cinsinde bir açı döndürür.

math.atan2()
************

İlk değere `y` ikinci değere `x` dersek şu işlemin 
sonucunu döndürür: `atan(y/x)`

math.hypot()
*************

İlk değere `x` ikinci değere `y` dersek şu işlemin
sonucunu döndürür: `sqrt(x*x+y*y)`.

math.cosh()
************

Verilen değerin hiperbolik kosinüsünü döndürür.

math.sinh()
************

Verilen değerin hiperbolik sinüsünü döndürür.

math.tanh()
************

Verilen değerin hiperbolik tanjantını döndürür.

math.acosh()
*************

Verilen hiperbolik kosinüs değerinin tersini döndürür.

math.asinh()
*************

Verilen hiperbolik sinüs değerinin tersini döndürür.

math.atanh()
*************

Verilen hiperbolik tanjant değerinin tersini döndürür.


math.gamma()
************

Bu fonksiyon `factorial` fonksiyonuna çok benziyor. Farklarından biri 
verilen sayının bir azının faktoriyelini hesaplamasıdır.
Ancak asıl fark sayı büyüdüğünde ortaya çıkıyor.
::

    >>> math.factorial(12)==math.gamma(13)
    True
    >>> math.factorial(12)
    479001600
    >>> math.gamma(13)
    479001600.0
    >>> math.factorial(35)==math.gamma(36)
    False
    >>> math.factorial(35)
    10333147966386144929666651337523200000000
    >>> math.gamma(36)
    1.0333147966386145e+40

math.lgamma()
*************

Bu fonksiyon daha önce öğrendiğimiz iki fonksiyonu birleştiriyor.
::

    >>> math.lgamma(45)==math.log(math.gamma(45))
    True
    >>> math.log(math.gamma(45))
    125.3172711493569
    >>> math.lgamma(45)
    125.3172711493569

