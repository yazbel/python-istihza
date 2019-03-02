.. meta::
   :description: Python 3.x'te bezeyiciler (Decoratorlar)
   :keywords: python, fonksiyonlar, decoratorlar, bezeyiciler
.. highlight:: py3

Fonksiyonlarda Bezeyicilerin (Decorator) Kullanımı
**************************************************

Bu bölüme kadar fonksiyonları nasıl kullanabileceğimizi işlemiştik. 
Bu yazıda bezeyicilerin nasıl çalıştığını, bezeyicilerin ne olduğunu ve
ve kendimize özgü bezeyicileri nasıl oluşturabileceğimizi anlayacağız.

Python'da fonksiyonlar birinci sınıf nesnelerdir, Python'daki her
şey gibi. Yani fonksiyonlar da her nesne gibidir. Bezeyiciler de
bu özellikten yararlanarak çalışırlar. Şimdi fonksiyonların
yapabileceklerinden bir kaç tanesini öğrenelim.


Fonksiyonlar diğer değişkenler tarafından referanslanabilir
***********************************************************

Python'da "Merhaba, dünya!" yazdıran bir fonksiyon örneği::
   
   def mrb_dunya():
      print("Merhaba, dünya!")

   mrb_dunya()

   # Çıktı: Merhaba, dünya!

Biz bu fonksiyonu başka bir değişkene referanslayarak, o değişkenin merhaba dünya demesini sağlayabiliriz::

   dunyaci = mrb_dunya
   
Şimdide dunyaci fonksiyonunu çağıralım::

   dunyaci()

   # Çıktı: Merhaba, dünya!

Gördüğümüz kadarıyla dunyaci fonksiyonuda "Merhaba, dünya!" çıktısını verdi. Niye?

Niye olduğuna bir bakalım. mrb_dunya'yı çağırmadan yazdırırsak ne olur?::

   print(mrb_dunya)

Çıktısı `<function mrb_dunya at 0x7f7ffe024c80>` şeklinde birşey olacaktır. Çıktısı bize demeye çalışıyor ki, 
mrb_dunya fonksiyonu belleğin 0x7f7ffe024c80 lokasyonunda bulunmaktadır. Muhtemelen 0x7f7ffe024c80
çıktısı sizin çıktınız ile aynı olmayacaktır çünkü sizin bilgisayarınızda o fonksiyon belleğinizin farklı bir lokasyonunda depolanmış
olabilir. Şimdi mrb_dunya fonksiyonun nerde olduğunu bildiğimize göre dunyacı fonksiyonuna da bir bakalım::

   print(dunyaci)

Çıktı `<function mrb_dunya at 0x7f41c77cebf8>`. Garip değil mi? Normalde `<function mrb_dunya at 0x7f41c77cebf8>` olmaması gerek çünkü fonksiyonumuzun adı mrb_dunya değil. İşte işler sandığımız gibi olmuyor. Python "dunyaci = mrb_dunya" yerinde mrb_dunya
bellekteki mrb_dunya fonksiyonuna yönlendirdi, yani `0x7f41c77cebf8`'e. O yüzden Python onu mrb_dunya fonksiyonu olarak gördü. Fakat dikkatli olursak, mrb_dunya ile dunyaci fonksiyonun lokasyonları aynı değil. Çünkü iki fonksiyonun aynı yerde olması 
mümkün değil. Belleğin farklı bir yerindeki fonksiyon, başka fonksiyona yönlendiriyor. Yani 0x7f41c77cebf8 olan bir fonksiyon aslında 0x7f576e924bf8 lokasyonundaki bir fonksiyonu çağırıyor. Şimdi sonrakine geçelim.

Fonksiyonlar argüman olarak verilebilir
***************************************
Örnek olarak::
   
   def fonksiyonCagir(fonksiyon):
      print("Fonksiyon çağrılıyor!")

      fonksiyon()

   fonksiyon(mrb_dunya)

Bu programın çıktısı sırayla "Fonksiyon çağrılıyor!" "Merhaba, dünya!" yazdırmak olacaktır. Yukarıda gösterdiğimiz gibi
Python fonksiyon = mrb_dunya yaptı ve onu çağırınca 0x7f576e924bf8 lokasyonundaki (mrb_dunya'nın lokasyonundaki) fonksiyonu
çağırdı.


Fonksiyonların içinde fonksiyon oluşturulabilir
***********************************************
Örnek Olarak::
   
   def merhabaDe():
      def merhabaci():
         print("Merhaba istihza!")
      merhabaci()

Yukardaki örnekte merhabaci fonksiyonu *merhabaDe* fonksiyonunun içinde tanımladık.
Bu Python'da geçerli bir davranıştır. *merhabaDe* fonsksiyonunu çağırdığımızda, *merhabaci*
fonksiyonu *merhabaDe* fonksiyonun içinde tanımlanıp çağrılıyor.

Eğer *merhabaci* fonksiyonunu *merhabaDe* fonksiyonun dışında çağırmaya çalışırsak, Python
bize bir hata verecektir çünkü *merhabaci* fonksiyonu *merhabaDe* fonksiyonun dışında tanımlanmamıştır.

Bezeleyiciler (Decoratorlar)
****************************

Bezeleyiciler, fonksiyonlarımızı veya nesnelerimizi modifiye etmemizi sağlayan çağrılabilir nesnelerdir.

Çağrılabilir objeleri örnek verecek olursak, fonksiyonlar ve objeleri örnek verebiliriz.

Bunu bir örnek ile anlayalım::

   def bezeleyici(fonksiyon):
      def wrapper():
         print("Wrapper fonksiyonumuz başladı")
         fonksiyon() # Bezeleyici ile aldığımız fonksiyonu çağırıyoruz
         print("Wrapper fonksiyonu bitti.")
      return wrapper

   def merhaba():
      print("Merhaba!")

   merhaba = bezeleyici(merhaba)

   merhaba()

   # Wrapper Fonksiyonumuz başladı
   # Merhaba!
   # Wrapper fonksiyonu bitti.

Şeklinde bir programımız olacaktır. Peki bu bezeleyici fonksiyonları
daha okunabilir bir şekilde çağırabilir miyiz? Tabiki::
   
   @bezeleyici
   def merhaba():
      print("Merhaba!")

   merhaba()

Yukarıdaki program ile bir önceki programımız ile aynı çıktıyı verecektir.
Mantık aynı: fonksiyonu al, çağır. Fakat bu sefer fonksiyon tanımlandıktan sonra
hemen argüman olarak verip, çağırıyoruz. Peki bezeyicilere argüman verebilir miyiz?::
   
   def baslik(fonksiyon):
      def wrapper(basligimiz):
         print(basligimiz)
         fonksiyon()

   @baslik()
   def makale(basligimiz):
      print("Python 3.7 ile dataclasses gibi birçok güzel özellik eklendi.")

   makale("Python 3.7")

   # Python 3.7
   # Python 3.7 ile dataclasses gibi birçok güzel özellik eklendi.

Gördüğümüz kadarıyla oldukça basit. bezeyiciler ne işe diye soracak isek, bazı fonksiyonlara istediğiniz
özelliği eklemede veya Flask gibi frameworklerde kullanıldığını unutmayın. Hadi sonraki dersimize geçelim :)
