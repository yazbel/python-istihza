#######
Kurulum
#######

Burada çok detaylı olarak kurulumu anlatmayacağız. Gerekli linkleri vereceğim, eğer yine de kurulumda sorun yaşarsanız forumda konu açarak belirtebilirsiniz.


Kuruluma başlamadan önce dikkat edilmesi gereken bir durum var. Eğer Kivy ile programlama yapacaksanız, bilgisayarınızda Python kurulu olmalıdır.


Kivy'in desteklediği sürümleri açıklayacak olursak;


Python 2.7 >= Kivy < Python 3.0

Python 3.4 >= Kivy


Python 2.7 sürümünden Python 3.0 sürümüne kadar, aynı zamanda Python 3.4 sürümünden itibaren ileri sürümlerde destekleniyor. Bu bilgiye göre, Python sürümünüzün Kivy programlama için uygun olup olmadığını tespit edebilirsiniz.


İşletim sisteminize göre kurulum için, aşağıda verdiğim kılavuz sayfalarına bakabilirsiniz.


Windows için kurulum:

https://kivy.org/docs/installation/installation-windows.html


Linux için kurulum:

https://kivy.org/docs/installation/installation-linux.html


OS X için kurulum

https://kivy.org/docs/installation/installation-osx.html


Türkçe kaynak:

http://kivy-tr.readthedocs.io/tr/latest/kurulum.html


Kivy kütüphanesini kurduysanız, bir sorun olup olmadığını test etmek için şöyle basit bir program yazalım. Ekrana boş bir pencere çıkaralım.


   .. code-block:: python
	
	# -*- coding: utf-8 -*-

	from kivy.app import App
	
	App().run()

Kodu kaydedip çalıştırırsanız, ekrana boş bir siyah pencere çıkacaktır. Güzel, artık Kivy ile programlamaya başlayabiliriz :)


Yukarıda da yazdığım gibi, detaylı olarak anlatmadık. Çünkü birden fazla platform için yazılmış bir kütüphane olduğu için, her birine ayrılmış anlatım sayfaları ile yetindik. Yine de bir sorununuz olursa, kuramazsanız foruma konu açabilirsiniz. Kivy resmi kaynaklarında bulunan kurulum kılavuzu için `şu`_ bağlantıya tıklayabilirsiniz.

.. _şu: https://kivy.org/doc/stable/installation/installation.html
