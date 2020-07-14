.. meta::
   :description: Python 3.x'te bezeyiciler (Decoratorlar)
   :keywords: python, fonksiyonlar, decoratorlar, bezeyiciler
.. highlight:: py3

Fonksiyonlarda Bezeyicilerin (Decorator) Kullanımı
**************************************************

.. warning:: Bu makale eksikler içermektedir. İleride güncellenecektir.

Bu bölüme kadar fonksiyonları nasıl kullanabileceğimizi işlemiştik.
Bu yazıda bezeyicilerin nasıl çalıştığını, bezeyicilerin ne olduğunu
kendimize özgü bezeyicileri nasıl oluşturabileceğimizi anlayacağız.

Python'da fonksiyonlar birinci sınıf nesnelerdir, Python'daki her
şey gibi. Yani fonksiyonlar da her nesne gibidir. Bezeyiciler de
bu özellikten yararlanarak çalışırlar. Şimdi fonksiyonların
yapabileceklerinden birkaç tanesini öğrenelim.


Fonksiyonlar diğer değişkenler tarafından referanslanabilir
===========================================================

Python'da "Merhaba, dünya!" yazdıran bir fonksiyon örneği::

   def mrb_dunya():
      print("Merhaba, dünya!")

   mrb_dunya()

   # Çıktı: Merhaba, dünya!

Biz bu fonksiyonu başka bir değişkene referanslayarak, o değişkenin merhaba dünya demesini sağlayabiliriz::

   dunyaci = mrb_dunya

Şimdi de dunyaci fonksiyonunu çağıralım::

   dunyaci()

   # Çıktı: Merhaba, dünya!

Gördüğümüz kadarıyla dunyaci fonksiyonu da "Merhaba, dünya!" çıktısını verdi. Peki niye?

Niye olduğuna bir bakalım. mrb_dunya'yı çağırmadan yazdırırsak ne olur?::

   print(mrb_dunya)

Çıktısı `<function mrb_dunya at 0x7f7ffe024c80>` şeklinde bir şey olacaktır. Çıktısı bize demeye çalışıyor ki,
mrb_dunya fonksiyonu belleğin 0x7f7ffe024c80 lokasyonunda bulunmaktadır. Muhtemelen 0x7f7ffe024c80
çıktısı sizin çıktınız ile aynı olmayacaktır çünkü sizin bilgisayarınızda o fonksiyon belleğinizin farklı bir lokasyonunda depolanmış
olabilir. Şimdi mrb_dunya fonksiyonun nerede olduğunu bildiğimize göre dunyaci fonksiyonuna da bir bakalım::

   print(dunyaci)

Çıktı `<function mrb_dunya at 0x7f41c77cebf8>`. Garip değil mi? Normalde `<function mrb_dunya at 0x7f41c77cebf8>` olmaması gerek çünkü fonksiyonumuzun adı mrb_dunya değil. İşte işler sandığımız gibi olmuyor. Python "dunyaci = mrb_dunya" yapınca mrb_dunya
bellekteki mrb_dunya fonksiyonuna yönlendirdi, yani `0x7f41c77cebf8`'e. O yüzden Python onu mrb_dunya fonksiyonu olarak gördü. Fakat dikkatli olursak, mrb_dunya ile dunyaci fonksiyonun lokasyonları aynı değil. Çünkü iki fonksiyonun aynı yerde olması
mümkün değil. Belleğin farklı bir yerindeki fonksiyon, başka fonksiyona yönlendiriyor. Yani 0x7f41c77cebf8 olan bir fonksiyon aslında 0x7f576e924bf8 lokasyonundaki bir fonksiyonu çağırıyor.

Fonksiyonlar argüman olarak verilebilir
=======================================

Örnek olarak::

   def fonksiyon_cagir(fonksiyon):
      print("Fonksiyon çağrılıyor!")

      fonksiyon()

   fonksiyon_cagir(mrb_dunya)

Bu programın çıktısı sırayla "Fonksiyon çağrılıyor!" ve "Merhaba, dünya!" olacaktır. Yukarıda gösterdiğimiz gibi
Python fonksiyon = mrb_dunya yaptı ve onu çağırınca 0x7f576e924bf8 lokasyonundaki (mrb_dunya'nın lokasyonundaki) fonksiyonu
çağırdı.


Fonksiyonların içinde fonksiyon oluşturulabilir
===============================================

Örnek olarak::

   def merhaba_de():
      def merhabaci():
         print("Merhaba istihza!")
      merhabaci()

Yukarıdaki örnekte merhabaci fonksiyonu *merhaba_de* fonksiyonunun içinde tanımladık.
Bu Python'da geçerli bir davranıştır. *merhaba_de* fonsksiyonunu çağırdığımızda, *merhabaci*
fonksiyonu *merhaba_de* fonksiyonunun içinde tanımlanıp çağrılıyor.

Eğer *merhabaci* fonksiyonunu *merhaba_de* fonksiyonunun dışında çağırmaya çalışırsak, Python
bize bir hata verecektir çünkü *merhabaci* fonksiyonu *merhaba_de* fonksiyonunun dışında tanımlanmamıştır.

Bezeyici (Decoratorlar)
=======================

Bezeyici, fonksiyonlarımızı veya nesnelerimizi modifiye etmemizi sağlayan çağrılabilir nesnelerdir.

Çağrılabilir objelere örnek verecek olursak, fonksiyonlar ve objeleri örnek verebiliriz. Bunu "callable"
fonksiyonu ile kontrol edebilirsiniz, örneğin::

    def f():
        ...

    print(callable(f))
    #=> True

ya da objemizin "__call\__" magic metodunun var olup olmadığını kontrol ederek de anlayabilirsiniz.

Şimdi bezeyici fonksiyonları bir örnek ile anlayalım::

   def bezeyici(fonksiyon):
      def wrapper():
         print("Wrapper fonksiyonumuz başladı")
         fonksiyon() # Bezeyici ile aldığımız fonksiyonu çağırıyoruz
         print("Wrapper fonksiyonu bitti.")
      return wrapper

   def merhaba():
      print("Merhaba!")

   merhaba = bezeyici(merhaba)

   merhaba()

   # Wrapper Fonksiyonumuz başladı
   # Merhaba!
   # Wrapper fonksiyonu bitti.

Şeklinde bir çıktımız olacaktır. Peki bu bezeyici fonksiyonları
daha okunabilir bir şekilde çağırabilir miyiz? Tabii ki::

   @bezeyici
   def merhaba():
      print("Merhaba!")

   merhaba()

Yukarıdaki program, bir önceki programımız ile aynı çıktıyı verecektir.
Mantık aynı; fonksiyonu al, çağır. Fakat bu sefer fonksiyonu tanımlandıktan sonra
hemen argüman olarak verip, çağırıyoruz. Peki bezeyicilere argüman verebilir miyiz?::

   def baslik(fonksiyon):
      def wrapper(basligimiz):
         print(basligimiz)
         fonksiyon(basligimiz)
      return wrapper

   @baslik
   def makale(basligimiz):
      print("Python 3.7 ile dataclasses gibi birçok güzel özellik eklendi.")

   makale("Python 3.7")

   # Python 3.7
   # Python 3.7 ile dataclasses gibi birçok güzel özellik eklendi.

veya onun çıktısını alarak çıktının üzerinde işlemler uygulayabiliriz::

   def iki_ile_carp(fonksiyon):
       def wrapper():
           cikti = fonksiyon()

           print(cikti * 2)
       return wrapper

Gördüğümüz kadarıyla oldukça basit. Bezeyiciler ne işe yarayacak diye soracak olur isek, bazı fonksiyonlarda istediğiniz
özelliği eklemede veya Flask gibi frameworklerde kullanıldığını unutmayın. Hadi sonraki dersimize geçelim :)
