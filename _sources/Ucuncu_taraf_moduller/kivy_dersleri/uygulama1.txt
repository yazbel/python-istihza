Uygulama 1 - Resim Görüntüleyici
################################

Şimdiye kadar öğrendiklerimiz ile örnek bir uygulama yapma zamanı geldi. Çünkü uygulamadıkça öğrenmemiz eksik kalır. O yüzden bir örnek yapalım

Örneğimiz bir resim görüntüleyici. Bir klasör içinde bulunan resimleri listeler, sonra bunları ileri ve geri butonlarına bastıkça görüntüler. Planımız ise şöyle. Girişte bir yazı ve bir progressbar olacak. Resimler yüklenirken progressbar üzerinde yüklenme durumu gösterilecek. Tabi, resimler az olduğunda çok hızlı bir şekilde yüklenecek. Ancak örnekte de bulunsun diye bir progressbar eklemek istedim. 

Resimlerimiz yüklendikten sonra, ekrandaki yazıyı ve progressbar'ı kaldırıp yerine ana ekranımızı koyacağız. Bunu da ayrı bir fonksiyon içinde yaptık. O zaman şimdi kodumuzu görelim, sonra da incelemeye başlayalım

.. code-block:: python

	# -*- coding: utf-8 -*-
	# Resim Görüntüleyici
	# Yazbel

	from kivy.app import App
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.label import Label
	from kivy.uix.button import Button
	from kivy.uix.widget import Widget
	from kivy.uix.image import Image
	from kivy.clock import Clock
	from kivy.uix.progressbar import ProgressBar
	import os

	class Program(App):
	    
	    def resimYukle(self,dosya_yolu):
	        # Format listesi
	        liste = ["png","gif","jpeg","jpg"]

	        # Dosyaların listesini alma
	        dosyaListesi = os.listdir(dosya_yolu)
	        self.sayac = 0
	        self.bar.max = len(dosyaListesi)
	        self.bar.value = 0
	        
	        # Resim dosyalarını tespit etme
	        for i in dosyaListesi:
	            if(i.split(".")[-1] in liste):
	                self.resimListesi.append(i)
	                
	            self.sayac += 1
	            self.bar.value = self.sayac

	        # Resimlerin yüklenmesi bittikten sonra, görüntüleme ekranını başlatmak üzere
	        # self.basla fonksiyonuna git
	        self.yukleniyor.text = "Resimler yüklendi"
	        Clock.schedule_once(self.basla,1.5)

	    def build(self):
	        self.resimYolu = "resim/"
	        self.resimListesi = list()
	        self.resimSirasi = 0
	        
	        self.yukleniyor = Label(text = "Resimler yükleniyor...")
	        self.bar = ProgressBar()
	        
	        self.govde = BoxLayout(orientation = "vertical")
	        self.govde.add_widget(self.yukleniyor)
	        self.govde.add_widget(self.bar)
	        
	        # Resimleri yüklemek üzere, self.resimYukle fonksiyonuna git
	        Clock.schedule_once(lambda event = None:self.resimYukle(self.resimYolu),1)
		
	        return self.govde

	    def basla(self,event = None):
	        # Ekrandaki tüm araçları kaldırıyoruz
	        self.govde.clear_widgets()

	        # Ve yeni araçlarımızı ekliyoruz
		self.bilgi = Label(text = "[color=#05f]Yazbel[/color] Resim Görüntüleyici",
				       markup = True,
				       size_hint_y = .1)
		self.resim = Image(source = self.resimYolu+self.resimListesi[0],
				   allow_stretch = True,
				   keep_ratio = True)


	        # Geri ve ileri butonlarını taşıyan BoxLayout
	        self.butonBar = BoxLayout(size_hint_y = .15)
	        
	        self.ileri = Button(text = "ileri",
	                            size_hint_x = .2,
	                            on_release = self.ileriYukle
	                            )
	        
	        self.geri = Button(text = "geri",
	                           size_hint_x = .2,
	                           on_release = self.geriYukle)

	        self.butonBar.add_widget(self.geri)
	        self.butonBar.add_widget(Widget())
	        self.butonBar.add_widget(self.ileri)

		self.govde.add_widget(self.bilgi)
		self.govde.add_widget(self.resim)
		self.govde.add_widget(self.butonBar)


	    def ileriYukle(self,event = None):
	        self.resimSirasi += 1

	        # Eğer resim sırası listemizin boyutunu aşmamışsa
	        if(self.resimSirasi < len(self.resimListesi)):
	            try:
	                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
	                self.bilgi.text = self.resimListesi[self.resimSirasi]
	            except Exception as e:
	                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

	        # Eğer liste boyutunu aşmışsa, bunu sıfırlıyoruz
	        else:
	            try:
	                self.resimSirasi = 0
	                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
	                self.bilgi.text = self.resimListesi[self.resimSirasi]
	                
	            except Exception as e:
	                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

	    
	    def geriYukle(self,event = None):
	        self.resimSirasi -= 1

	        # Eğer resim sırası listemizin boyutunun altına düşmemişse
	        if(self.resimSirasi >= 0):
	            try:
	                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
	                self.bilgi.text = self.resimListesi[self.resimSirasi]
	            except Exception as e:
	                print(e)
	                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

	        # Eğer düşmüşse, yani negatif olduysa
	        # sırayı listenin sonuna alıyoruz
	        else:
	            try:
	                self.resimSirasi = len(self.resimListesi)-1
	                self.resim.source = self.resimYolu+self.resimListesi[self.resimSirasi]
	                self.bilgi.text = self.resimListesi[self.resimSirasi]
	            except Exception as e:
	                print(e)
	                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])
	                
	Program().run()

Öncelikle, programımız başlar başlamaz yazıyı ve progressbar'ı ekliyoruz sonra da resimlerin yüklenmesi için self.resimYukle fonksiyonuna gidiyoruz. 

.. code-block:: python

    def resimYukle(self,dosya_yolu):
        # Format listesi
        liste = ["png","gif","jpeg","jpg"]

        # Dosyaların listesini alma
        dosyaListesi = os.listdir(dosya_yolu)
        self.sayac = 0
        self.bar.max = len(dosyaListesi)
        self.bar.value = 0
        
        # Resim dosyalarını tespit etme
        for i in dosyaListesi:
            if(i.split(".")[-1] in liste):
                self.resimListesi.append(i)
                
            self.sayac += 1
            self.bar.value = self.sayac

        # Resimlerin yüklenmesi bittikten sonra, görüntüleme ekranını başlatmak üzere
        # self.basla fonksiyonuna git
        self.yukleniyor.text = "Resimler yüklendi"
        Clock.schedule_once(self.basla,1)

Bu fonksiyonda ilk olarak, hangi resim formatlarını göstereceğimizi bir listede tuttuk. Farklı resim formatları da ekleyebilirsiniz. Biz şimdilik bu 4 formatı tercih ettik. Bu formatlar dışındaki resimleri dikkate almayacaktır.

Formatlarımızı tanımladıktan sonra, os.listdir() yardımıyla hangi klasördeki resimleri göstermek istiyorsak, o klasördeki dosyaları liste olarak elde ediyoruz. Bakın resimleri değil, dosyaları diyorum. Çünkü os.listdir() sadece verilen dizindeki dosyaların listesini verir. Bu listeden resim dosyalarını, bizim belirlediğimiz formatta olanları, ayırt etmek bizim işimiz. 

Bu yüzden hemen aşağısında for döngüsü ile bu listenin elemanlarını tek tek kontrol ettik, ve uzantısı bizim belirttiğimiz uzantılardan biriyle eşleşiyorsa, self.resimListesi adlı listemize ekledik. 

Tüm resimleri tespit ettikten sonra, 1 saniye sonra self.basla fonksiyonuna gidiyoruz. Bu fonksiyonda, ekrandaki tüm araçları self.govde.clear_widgets() ile temizledik ve yeni araçlarımızı ekledik. 

.. code-block:: python

    def basla(self,event = None):
        # Ekrandaki tüm araçları kaldırıyoruz
        self.govde.clear_widgets()

        # Ve yeni araçlarımızı ekliyoruz
        self.bilgi = Label(text = "[color=#05f]Yazbel[/color] Resim Görüntüleyici",
			       markup = True,
			       size_hint_y = .1)
	    self.resim = Image(source = self.resimYolu+os.sep+self.resimListesi[0],
			   allow_stretch = True,
			   keep_ratio = True)


        # Geri ve ileri butonlarını taşıyan BoxLayout
        self.butonBar = BoxLayout(size_hint_y = .15)
        
        self.ileri = Button(text = "ileri",
                            size_hint_x = .2,
                            on_release = self.ileriYukle
                            )
        
        self.geri = Button(text = "geri",
                           size_hint_x = .2,
                           on_release = self.geriYukle)

        self.butonBar.add_widget(self.geri)
        self.butonBar.add_widget(Widget())
        self.butonBar.add_widget(self.ileri)

		self.govde.add_widget(self.bilgi)
		self.govde.add_widget(self.resim)
		self.govde.add_widget(self.butonBar)

Bu fonksiyonda yabancı olduğumuz bir kod yok sanırım.Kullandığımız tüm pencere araçlarını daha önce gördük. Sadece butonBar içine eklediğimiz bir adet boş widget var. Onu da iki butonun arasını doldurmak için ekledik. Eklemeseydik de olurdu tabi. 

Butonlarımızı ekledik ve ileri butonuna tıklandığı zaman, self.ileriYukle fonksiyonumuzun çalışmasını sağladık.

.. code-block:: python

    def ileriYukle(self,event = None):
        self.resimSirasi += 1

        # Eğer resim sırası listemizin boyutunu aşmamışsa
        if(self.resimSirasi < len(self.resimListesi)):
            try:
                self.resim.source = self.resimYolu+os.sep+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer liste boyutunu aşmışsa, bunu sıfırlıyoruz
        else:
            try:
                self.resimSirasi = 0
                self.resim.source = self.resimYolu+os.sep+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
                
            except Exception as e:
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

İlk olarak resimSirasi değişkenini 1 arttırıyoruz ve sonra da bu değerin listemizin boyutunu aşıp aşmadığını kontrol ediyoruz. Çünkü eğer boyutunu aşarsa, "liste boyutu aşıldı" hatası alabiliriz. Bu yüzden eğer boyutu aştıysa, değerini tekrardan 0 yapıyoruz

Geri butonumuz için de benzer şeyleri yapıyoruz

.. code-block:: python

    def geriYukle(self,event = None):
        self.resimSirasi -= 1

        # Eğer resim sırası listemizin boyutunun altına düşmemişse
        if(self.resimSirasi >= 0):
            try:
                self.resim.source = self.resimYolu+os.sep+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

        # Eğer düşmüşse, yani negatif olduysa
        # sırayı listenin sonuna alıyoruz
        else:
            try:
                self.resimSirasi = len(self.resimListesi)-1
                self.resim.source = self.resimYolu+os.sep+self.resimListesi[self.resimSirasi]
                self.bilgi.text = self.resimListesi[self.resimSirasi]
            except Exception as e:
                print(e)
                self.bilgi.text = "Yuklenemedi: {}".format(self.resimListesi[self.resimSirasi])

Burada farklı olarak, resimSirasi değerinin eksiye düşüp düşmediğini kontrol ettik. Eksiye düştüyse, tekrar listenin sonuna alıyoruz. Böylece bir döngü içinde resimlerin görüntülenmesini sağladık.

Örnekte bulunan os.sep, bulunduğunuz işletim sisteminde kullanılan dizin ayracını verir. Linux kullanıyorsanız, "/" Windows kullanıyorsanız "\\" veya "\" olarak belirlenir. Örnekte kullanmamızın sebebi, resim yolu ve resim adını birleştirdiğimizde araya dizin ayracı koymak. Eğer koymazsak, resmin bulunamadığına dair hata alırız.

.. code-block:: python

	>>> resimYolu+os.sep+resim
	"resim/resim.jpg"

	>>> resimYolu+resim
	"resimresim.jpg"

Ben örnekte görüntülemek istediğim resimleri, program ile aynı klasörde bulunan "resim" adlı klasöre koydum. Eğer aynı klasörde bulunmayan başka bir klasörü listelemek isterseniz, tam dizini vermeniz gerekiyor. Yani "C:\\resimler" gibi.

Programın görüntüsü şöyle

.. image:: images/uygulama-1.png

Gayet güzel çalışıyor. Kodu elimden geldiği kadar anlaşılır yazmaya çalıştım. Eğer anlamadığınız bir kısım olursa, veya hata olduğunu düşündüğünüz bir kısım varsa `Forum`_ üzerinden ulaşabilirsiniz.

.. _Forum: https://forum.yazbel.com
