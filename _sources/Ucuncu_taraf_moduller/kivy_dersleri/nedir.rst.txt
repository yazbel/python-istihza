###########
Kivy Nedir?
###########

Kivy Android'den Windows'a kadar birden fazla işletim sistemini destekleyen bir grafik arayüz kütüphanesidir. 
Açık kaynak kodludur ve %90 Python ile yazılmıştır. Kaynak kodlarını incelemek isterseniz `şu`_ linke tıklayabilirsiniz. Ayrıca bu github adresinde yer alan, Kivy ile ilgili örnekleri de incelemek isterseniz `linke`_ tıklayabilirsiniz.

Kivy çizim işlemlerini SDL2 kullanarak yapmaktadır. Doğal olarak pencere araçları, alışık olduğumuz Android veya diğer mobil pencere araçlarına benzemiyor(görünüm olarak). Kendine has şekilleri var, yani yerel işletim sisteminin grafiklerini kullanmıyor. Ekrana çizilen pencere araçlarının png haline, bilgisayarınızdaki kivy klasörünün altında ulaşabilirsiniz. kivy/data/images altında şöyle bir png dosyası var

.. image:: images/tema.png

Bu png dosyasını kesinlikle silmemelisiniz,boyutlarında kesinlikle oynama yapmamalısınız. Aksi takdirde Kivy pencere araçları ekrana çizilmeyecektir ve hata verecektir.

.. _şu: https://github.com/kivy/kivy
.. _linke: https://github.com/kivy/kivy/tree/master/examples

Kivy ile yazdığınız programları aynen veya birkaç değişiklik ile Android'de, Windows'ta çalıştırabilirsiniz. Yazdığınız programları buildozer yardımı ile paketleyebilirsiniz(android veya ios için). Bunlara yeri geldiğinde değinmeye çalışacağız.

Kivy kullanabilmeniz tabi ki Python temeliniz olmalı ve Kivy'i sisteminize kurmalısınız. Python'da sınıf yapılarını bilmeniz size ekstra bir katkı sağlar. Kivy programlarını nesne yönelimli olarak yazmak, çok daha sağlam ve düzenli programların ortaya çıkmasını sağlar.

Evet, Kivy hakkında biraz bilgi sahibi olduğumuza göre artık Kivy ile programlamaya giriş yapabiliriz...
