.. meta::
   :description: Python 3.x'te bezeyiciler (Decoratorlar)
   :keywords: python, fonksiyonlar, decoratorlar, bezeyiciler
.. highlight:: py3

Fonksiyonlarda Bezeyicilerin (Decorator) Kullanımı
**************************************************

Bu bölüme kadar fonksiyonları nasıl kullanabileceğimizi işlemiştik. 
Bu yazıda bezeyicilerin nasıl çalıştığını, bezeyicilerin ne olduğunu ve
ve kendimize özgü bezeyicileri nasıl oluşturabileceğimizi anlayacağız.

Python'daki her şey nesnedir, fonksiyonlar dahil. Ama nasıl?
Pythonda fonksiyonlar birinci sınıftır, yani bu da demek oluyor ki
fonksiyonlar bir değişken tarafından referanslanabilir, listelere eklenebilir,
argüman olarak alınabilir vb. Python'daki sayılar da birer birinci sınıf nesnedir.
Yani sayılar da yapabileceğiniz her şeyi (Metodları hariç, çünkü fonksiyon nesneleri
ile sayı nesneleri aynı nesne değildir.) yapabilirsiniz. Şimdi örneklere başlayalım.

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

Niye olduğunu bi bakalım. mrb_dunya'yı çağırmadan yazdırırsak ne olur?::

   print(mrb_dunya)

Çıktısı `<function mrb_dunya at 0x7f7ffe024c80>` şeklinde birşey olacaktır. Çıktısı bize demeye çalışıyor ki, 
mrb_dunya fonksiyonu belleğin belleğin 0x7f7ffe024c80 lokasyonunda bulunmaktadır. Muhtemelen 0x7f7ffe024c80
çıktısı aynı olmayacaktır çünkü sizin bilgisayarda o fonksiyon belleğinizin farklı bir lokasyonunda depolanmış
olabilir. Şimdi mrb_dunya fonksiyonun nerde olduğunu bildiğimize göre dunyacı fonksiyonunada bi' bakalım::

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

Bu programın çıktısı sırayla "Fonksiyon çağrılıyor!" "Merhaba, dünya!" yazdırmak olacaktır. Yukarda gösterdiğimiz gibi
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
Bu Pythonda geçerli bir davranıştır. *merhabaDe* fonsksiyonunu çağırdığımızda, *merhabaci*
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

Yukardaki program ile bir önceki programımız ile aynı çıktıyı verecektir.
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
