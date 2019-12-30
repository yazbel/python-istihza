########################
Kivy Programlamaya Giriş
########################

Bu yazıyla Kivy derslerine giriş yapacağız. Önce klasik başlangıç olan "merhaba dünya" örneği yapacağız ve sırayla kodumuzu inceleyeceğiz.


Bundan önceki yazılarda da bahsettiğimiz gibi, Kivy ile programlamadan verim almak istiyorsanız Python sınıflar konusunda temel bilginiz olmalıdır. Çünkü genelde sınıfları kullanacağım ve bu yüzden yazdığım kodları(her ne kadar açıklama yapsam da) anlayabilmek için, temel de olsa, bilgili olmanız gerekir. Burdan, "Kivy sınıflar ile kullanılmak zorundadır" anlamı çıkmasın. Zaten sınıf yapısı çok zor değil, biraz pratik yaparak mantığını kavrayabilirsiniz.

Kivy kütüphanesini sıkıntısız bir şekilde kurduğunuzu varsayarak ilk örneğimize geçiş yapıyoruz. 

Herhangi bir açıklama yapmadan önce hemen kodları verelim


.. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Program(App):
	    def build(self):
	        yazi = Label(text = "Merhaba Dünya")
	
	        return yazi
	
	
	Program().run()
	

Kodu kaydedip çalıştırdığınızda ekranda, karşınıza aşağıdaki gibi bir pencere çıkacaktır.

.. image:: images/merhaba.png

Şimdi sıra ile kodumuzu inceleyelim. İlk iki satır, her programın başına yazılan klasik satırlardır. Sadece ilk satır Linux için geçerli.


Sonraki satırda

.. code-block:: python

	from kivy.app import App

programın belkemiğini oluşturan App sınıfını import ediyoruz. Ana pencere bu sınıf yardımıyla oluşturulur, programa dair tanımlamalar genelde bu sınıf ile yapılır.


Bir sonraki satır

.. code-block:: python

	from kivy.uix.label import Label

ekranda yazı göstermemizi sağlayan Label sınıfını import ettik, yani kullanmak üzere içeriye aktardık. Artık gerekli sınıfları import ettiğimize göre ana programımızı tanımlayabiliriz


Bir sonraki satırda, Program adında bir sınıf oluşturduk ve App sınıfından miras aldık. Miras almak demek, önceden oluşturulan sınıfı tekrar kullanmak üzere bir sınıfa katmak, eklemek.


Yani biz burda programımızı oluşturabilmek için App sınıfını, kendi ana sınıfımıza miras aldık ve kullanmaya başladık. Ve sınıfımızda build adında bir metot tanımladık. Bu metot, programımız çalıştığında ekranda gösterilecek ana düzeni, bileşenleri geri döndürür. Genelde bir pencere düzeni geri döndürülür. Biz şimdilik basit bir şekilde ekranda yazı göstermek istedik ve bunu geri döndürdük. İleride pencere düzenlerini gördüğümüzde onları geri döndüreceğiz. Şimdilik örneğimize bakalım


Şimdiye kadar yaptıklarımız, ihtiyacımız olan şeyleri import etmek, ana sınıfımızı oluşturmak, ekranda gösterilecek nesneleri geri döndürmek. Artık programımızı çalıştırmamız gerekiyor. Bunu da Program().run() kısmında yaptık.


Kv Dili
=======

Kivy programlarını geliştirmek için geliştirilen bir dildir. Kullanımı basittir. Yukarıda yaptığımız programı bir de kv dili ile gerçekleştirelim.


Öncelikle ana dosyamızı hazırlıyoruz. Benim ana dosyamın adı main.py . Ve bu dosyamın yanına bir tane program.kv dosyası oluşturuyorum. Ana sınıfımın ismi neyse, kv dosyama onun adını verdim. main.py dosyamın içerisine aşağıdaki kodları yazıyorum

  .. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	
	class Program(App):
	    pass
	
	Program().run()


Şimdi program.kv dosyasının içerisine şunları yazalım. Amacımız ekranda merhaba dünya yazmak

.. code-block:: python
	
	Label:
	    text:"Merhaba Dünya"
	

Programımızın build tarafından geri döndürülecek olan pencere düzenini, kv dili yardımıyla oluşturduk. Yapmamız gereken main.py dosyamızı çalıştırmak ve sonucu görmek.


kv dili kullanırken, aynen Python'da  olduğu gibi girintilemeye dikkat etmelisiniz. Aksi taktirde hata verecektir. Kv dili, Kivy ile programlama yaparken oldukça kolaylık sağlar. Biz de derslerimizde bazen yaptığımız örnekleri kv diliyle de yapacağız. Bir programı birinci bölümdeki gibi sınıflarla da yazabilirsiniz, kv dili yardımıyla da yazabilirsiniz. Hatta bazı kısımları kv diliyle de yazabilirsiniz. Yerine göre değişecektir, illa ki kv diline ihtiyacınız olacaktır.


Uygulama Özellikleri
====================

Yazdığımız Kivy programının bazı niteliklerini değiştirebiliriz. Örneğin, siz yukarıda programı çalıştırdığınızda programın başlığını henüz tanımlamadığınız için pencerenin başlığı ana sınıfın adı ile aynıdır. İsterseniz bunu değiştirebilirsiniz.

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Program(App):
	    def build(self):
	        self.title = "Yazbel"
	        
	        return Label(text = "Merhaba Dünya")
	
	Program().run()
	
Kivy'de bir program başlarken, ekrana pencere çizilmeden önce birtakım metotlar çalışır. Bunlardan birisi on_start() metodu. Bu metot içerisine, ekrana pencere çizilmeden önce yani programımız başlamadan yapmak istediğimiz tanımlamaları yazabiliriz. Örneğin başlığı burada tanımlayabiliriz, ya da veritabanımız varsa bağlantıları burada başlatabiliriz. Kullanımına dair basit bir örnek

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Program(App):
	    def on_start(self):
	        self.title = "Yazbel"
	
	    def build(self):
	        return Label(text = "Merhaba Dünya")
	
	Program().run()
	

Ancak dikkat edilmesi gereken bir durum var. on_start() metodu, build() metodu çalıştırıldıktan sonra çağrılır. 

Kivy uygulamamızda belli olaylarda çalışan başka metotlar da var.


.. role:: red

:red:`on_stop()`: Bu metot, programımız sona erdiğinde çalıştırılır. Böylece son olarak yapmak istediğimiz işlemleri(örneğin açık dosyaları kapatmak) burada yapabiliriz


:red:`on_pause()`: android veya ios üzerinde programımız arkaplana alındığında bu metot çalıştırılır.


:red:`on_resume()`: Kullanıcı arkaplana aldığı uygulamamıza tekrar dönerse bu metot çalıştırılır.


Şimdi bunların hepsini birarada kullandığımız bir örnek görelim ve konuyu bitirelim

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Program(App):
	    def on_start(self):
	        self.title = "Yazbel"
	        # bir takım işlemler...
	
	    def on_stop(self):
	        # Uygulama kapatılırken...
	        pass
	
	    def on_pause(self):
	        # Uygulama arkaplana alınırken...
	        # Burda return True yapmanız gerekiyor
	        return True
	
	    def on_resume(self):
	        # Tekrar giriş yapıldığında yazımızı değiştiriyoruz
	        self.yazi.text = "Programa tekrar hoşgeldiniz"
	
	    def build(self):
	        self.yazi = Label(text = "Merhaba Dünya")
	        return self.yazi
	
	Program().run()
