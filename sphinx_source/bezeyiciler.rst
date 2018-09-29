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
argüman olarak alınabilir vb. Python'daki sayılarda birer birinci sınıf nesnedir.
Yani sayılarda yapabileceğiniz her şeyi (Metodları hariç, çünkü fonksiyon nesneleri
ile sayı nesneleri aynı nesne değildir.) yapabilirsiniz. Şimdi örneklere başlayalım.

Fonksiyonlar diğer değişkenler tarafından referanslanabilir
***********************************************************

Python'da "Merhaba, dünya!" yazdıran bir fonksiyon örneği::
   
   def mrbDunya():
      print("Merhaba, dünya!")

   mrbDunya()

   # Çıktı: Merhaba, dünya!

Biz bu fonksiyonu başka bir değişkene referanslayarak, o değişkenin merhaba dünya demesini sağlayabiliriz::

   dunyaci = mrbDunya
   
Şimdide dunyaci fonksiyonunu çağıralım::

   dunyaci()

   # Çıktı: Merhaba, dünya!

Gördüğümüz kadarıyla dunyaci fonksiyonuda "Merhaba, dünya!" çıktısını verdi. Niye?

Niye olduğunu bi bakalım. mrbDunya'yı çağırmadan yazdırırsak ne olur?::

   print(mrbDunya)

Çıktısı `<function mrbDunya at 0x7f7ffe024c80>` şeklinde birşey olacaktır. Çıktısı bize demeye çalışıyor ki, 
mrbDunya fonksiyonu belleğin belleğin 0x7f7ffe024c80 lokasyonunda bulunmaktadır. Muhtemelen 0x7f7ffe024c80
çıktısı aynı olmayacaktır çünkü sizin bilgisayarda o fonksiyon belleğinizin farklı bir lokasyonunda depolanmış
olabilir. Şimdi mrbDunya fonksiyonun nerde olduğunu bildiğimize göre dunyacı fonksiyonunada bi' bakalım::

   print(dunyaci)

Çıktı `<function mrbDunya at 0x7f41c77cebf8>`. Garip değil mi? Normalde `<function mrbDunya at 0x7f41c77cebf8>` olmaması gerek çünkü fonksiyonumuzun adı mrbDunya değil. İşler sandığımız gibi dönmüyor. Python "dunyaci = mrbDunya" yerinde mrbDunya
bellekteki mrbDunya fonksiyonuna yönlendirdi, yani `0x7f41c77cebf8`'e. O yüzden Python onu mrbDunya fonksiyonu olarak gördü. Fakat dikkatli olursak, mrbDunya ile dunyaci fonksiyonun lokasyonları aynı değil. Çünkü iki fonksiyonun aynı yerde olması 
mümkün değil. Belleğin farklı bir yerindeki fonksiyon, başka fonksiyona yönlendiriyor. Yani 0x7f41c77cebf8 olan bir fonksiyon aslında 0x7f576e924bf8 lokasyonundaki bir fonksiyonu çağırıyor. Şimdi sonrakine geçelim.

Fonksiyonlar argüman olarak verilebilir
***************************************
Örnek olarak::
   
   def fonksiyonCagir(fonksiyon):
      print("Fonksiyon çağrılıyor!")

      fonksiyon()

   fonksiyon(mrbDunya)

Bu programın çıktısı sırayla "Fonksiyon çağrılıyor!" "Merhaba, dünya!" yazdırmak olacaktır. Yukarda gösterdiğimiz gibi
Python fonksiyon = mrbDunya yaptı ve onu çağırınca 0x7f576e924bf8 lokasyonundaki (mrbDunya'nın lokasyonundaki) fonksiyonu
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

   def bezeleyiciFonksiyon(fonksiyon):
      def wrapper():
         print("Wrapper fonksiyonumuz başladı")
         fonksiyon() # Bezeleyici ile aldığımız fonksiyonu çağırıyoruz
         print("Wrapper fonksiyonu bitti.")
      return wrapper

   def merhaba():
      print("Merhaba!")

   merhaba = bezeleyiciFonksiyon(merhaba)

   merhaba()

   # Wrapper Fonksiyonumuz başladı
   # Merhaba!
   # Wrapper fonksiyonu bitti.

Şeklinde bir programımız olacaktır. Peki bu bezeleyici fonksiyonları
daha okunabilir bir şekilde çağırabilir miyiz? Tabiki::
   
   @bezeleyiciFonksiyon
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
