.. _Widgets: https://kivy.org/doc/stable/guide/widgets.html

######################
Temel Pencere Araçları
######################

Bu bölümde, Kivy içerisinde bulunan pencere araçlarından bahsedeceğiz. Bu bölüm, Kivy API kaynaklarından yardım alarak oluşturulmuştur. Kivy dökümanlarında `Widgets`_ sayfasına bakabilirsiniz

Tüm pencere araçları Widget sınıfından türetilmiştir. Widget boş bir pencere aracıdır. Siz de isterseniz Widget sınıfını kullanarak kendi pencere aracınızı oluşturabilirsiniz. Biz de yeri geldiğinde burada Widget ile ilgili örnekler yapacağız. 

Pencere araçları kullanıcı ile iletişim imkanı verir, görsel arayüzü anlamlı kılar. Boş pencere hiçbir anlam ifade etmez, ancak pencere araçlarıyla anlamlı olur. Pencere araçlarını iki kısımda anlatmayı düşünüyoruz. Birinci kısımda buton,yazı,metin kutusu gibi temel pencere araçlarını anlatacağız. 

İkinci kısımda ileri seviye pencere araçlarından bahsedeceğiz. Android tarzı menüler, slayt pencereleri, popup pencereleri gibi araçları ikinci kısımda anlatacağız

Tabi ki bunlar Kivy dökümanlarında ikiye ayrılmış değil, sadece burada anlatım için benimsenmiştir. Amaç yazıların daha düzgün ve anlamlı bir şekilde sıralanmasıdır. 

Öyleyse başlayalım

Label
=====

kivy.uix.label.Label

Bildiğiniz gibi Label, ekranda yazı göstermeyi sağlayan bir pencere aracıdır. Nasıl import edeceğimizi ve nasıl kullanabileceğimizi bir örnekle görelim

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba ben bir yazıyım :)")
	
	        return yazi
	
	    
	Yazbel().run()

Label sınıfıyla birlikte kullanabileceğimiz bazı özellikleri birer örnek ve kısa bir açıklama ile aşağıda belirteceğim.

font_size
---------

Yazının boyutunu pixel cinsinden ifade etmeyi sağlar. Varsayılan olarak 15 sp'dir

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba ben bir yazıyım :)",
	                     font_size = "25sp")
	
	        return yazi
	
	    
	Yazbel().run()
	

halign
------

Yazıyı sağa,sola veya ortaya hizalamak için kullanılır. Varsayılan olarak "left" değerini alır. Verebilinecek değerler; left,right,center

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba ben bir yazıyım :)\nSağa yaslı bir yazı...",
	                     font_size = "25sp",
	                     halign = "right")
	
	        return yazi
	
	    
	Yazbel().run()


color
-----

Yazının rengini değiştirmek için kullanılır. Liste veya demet olarak değer alır. RGBA cinsinden değer alabilir. Varsayılan değer: [1,1,1,1]

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba\nben bir yazıyım",
	                     font_size = "25sp",
	                     color = [0,.3,.9,1])
	
	        return yazi
	
	    
	Yazbel().run()

bold - italic
-------------

Yazıyı kalın ve eğik göstermek için kullanılır. 

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba\nben bir yazıyım",
	                     font_size = "25sp",
	                     color = [0,.3,.9,1],
	                     bold = True,
	                     italic = True)
	
	        return yazi
	
	    
	Yazbel().run()
	

line_height
-----------

Satır arası genişliği ayarlamak için kullanılır. Varsayılan değeri 1'dir.

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Merhaba\nben bir yazıyım",
	                     font_size = "25sp",
	                     color = [0,.3,.9,1],
	                     line_height = 2)
	
	        return yazi
	
	    
	Yazbel().run()
	

markup
------

Daha önce HTML tag'leri kullandıysanız markup kullanımını anlamanız gayet kolay olacaktır. Ancak kullanmadıysanız da sorun değil. Zira kolaydır. markup, tag'ler yardımı ile yazınızı biçimlendirmenizi sağlar. Kullanılabilir tag'ler şunlardır.


[b][/b]: Kalın yazı

[i][/i]: İtalic yazı

[u][/u]: Altı çizili yazı

[s][/s]: Üstü çizili yazı

[font=][/font]: Font belirleme. İnternetten indirdiğiniz font dosyasının adını verebilirsiniz. Font dosyası ile programınız aynı klasörde olmalı.

[size=][/size]: Yazı boyutu

[color=#RGB][/color]: Renkli yazı

[ref=deger][/ref]: Yazıya bir link ekler. Bu link'e tıklandığı zaman, belirlenen fonksiyona gönderilecektir. 

[anchor=name]: Yazıya ekleyerek, yazının sol üst köşesine göre koordinat bilgisi almayı sağlar. yazi.anchors ile erişilebilir. 

[sub][/sub]: alt simge olarak yazmayı sağlar. Logaritmik gösterimlerde kullanılabilir.

[sup][/sup]: üst simge olarak yazmayı sağlar. Üslü sayıların yazımında kullanabiliriz


Şimdi bunları bir örnek içerisinde görelim.

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        string = """
	[size=20]
	[color=#090]Renkli[/color]
	[size=15]Size 15[/size]
	[i]italic[/i]
	[b]bold[/b]
	[ref=Link]Tıkla[/ref]
	[u]Altı çizili[/u]
	[s]Üstü çizili[/s]
	[font=Pacifico]Font[/font]
	2[sup]8[/sup]
	log[sub]2[/sub]10
	[/size]
	"""
	        # Tüm yazıyı [size=20] [/size] arasına alarak boyutunu arttırdım
	        
	        yazi = Label(text = string,markup = True)
	        # markup = True değerini vermezseniz yazınız tag'lerle birlikte yorumlanmaz
	        # yani tag'ler etkisiz hale gelir
	        # kapatmak için, markup = False değerini vermelisiniz
	
	        yazi.bind(on_ref_press = self.tikla)
	        # ref ile belirlediğimiz yazıya tıklandığı zaman
	        # self.tikla metodumuz çalışacaktır
	        # Burada amaç, ref ile belirlediğimiz yazıya tıklandığı zaman
	        # hangi metodun çalışacağını belirlemektir.
	        # bu bir olaydır. Olayları ileride göreceğiz
	        # şimdilik bu örneği anlamanız yeterli
	        
	        return yazi
	
	    def tikla(self,nesne,deger):
	        print("Deger: {}".format(deger)) # [ref=deger] kısmındaki deger'i yazdırır
	        
	Yazbel().run()
	


Örnekte kullandığım Pacifico font'unu internet üzerinden kolaylıkla temin edebilirsiniz. İndirdikten sonra programın ana dosyasının yanına koymanız gerekiyor. Yoksa font dosyasının bulunamadığına dair hata mesajıyla karşılaşırsınız.


Yazınızın özelliklerine sonradan erişebilir, isterseniz bunları değiştirebilirsiniz. yazi.ozellik şeklinde ilgili özelliğe erişebilir, yazi.ozellik = yeni_deger ile de yeni değerini verebilirsiniz. Örneğin, bir yazının içeriğini ve rengini değiştirelim

.. code-block:: python
	
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from kivy.app import App
	from kivy.uix.label import Label
	
	class Yazbel(App):
	    def build(self):
	
	        yazi = Label(text = "Eski değer..",
	                     color = [0,.3,.9,1])
	
	        yazi.text = "Yeni değer.."
	        yazi.color = [1,0,0,1]
	
	        return yazi
	    
	Yazbel().run()
	
	
Label ile ilgili daha fazla bilgi için `Kivy Label`_ sayfasını ziyaret edebilirsiniz

.. _Kivy Label: https://kivy.org/doc/stable/api-kivy.uix.label.html

Button
======

kivy.uix.button.Button

Button pencere aracı, butonlar oluşturmayı sağlar ve kivy.uix.button içerisinde bulunur. Bir butona tıklandığı zaman olaylar meydana gelir. Mesela butona tıklanma olayı, basılı tutulma olayı, butonu bırakma olayı vs hepsi birer olaydır ve event olarak adlandırılır. Event ingilizce olay,hareket demektir. Butonlar olaylarla anlam kazanır. Bir butonun tıklanma olayını fonksiyonlar yardımıyla dinleriz, olay gerçekleştiği zaman fonksiyonumuz da çalışmış olur. Biz de bu fonksiyon içerisinde yapılmasını istediğimiz işlemleri yazarız. 

Kivy içerisinde butonlar, birer Label sayılabilirler. Label'den farkı tıklanabilir araçlardır. Onun dışında Label ile birlikte kullanılan tüm özellikleri Button sınıfıyla birlikte kullanabiliriz. Elbette bir Label'den fazlasına sahiptir. Bunları da birazdan inceleyeceğiz. Öncelikle bir butonun nasıl oluşturulduğunu ve bu butonun olaylarını(örneğin butona tıklama) nasıl dinleyeceğimizi görelim.

.. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	from kivy.app import App
	from kivy.uix.button import Button
	from kivy.uix.boxlayout import BoxLayout

	class Yazbel(App):

		def build(self):
			self.govde = BoxLayout(orientation = "vertical")

			self.yazi = Label(text = "Bildiri Ekranı")
			self.buton = Button(text = "Tıkla",size_hint_y = .3)

			self.buton.bind(on_press = self.press) 
			# Basılma olayını self.press fonksiyonuna bağladık
			# Yani butona basıldığı anda self.press fonksiyonumuz çalışacaktır

			self.buton.bind(on_release = self.release)
			# Bırakılma olayını self.release fonksiyonuna bağladık
			# Yani buton bırakıldığı anda self.release fonksiyonumuz çalışacaktır

			self.govde.add_widget(self.yazi)
			self.govde.add_widget(self.buton)

			return self.govde

		def press(self,nesne):
			self.yazi.text = "Buton'a basıldı"

		def release(self,nesne):
			self.yazi.text = "Buton bırakıldı"

Şimdi kodu inceleyelim. İlk olarak gerekli sınıflarımızı import ettik. Bir tane BoxLayout pencere düzeni oluşturduk, içerisine de yazımızı ve butonumuzu ekledik. Butonumuzun yazımıza göre dikeyde daha az yer kaplaması için size_hint_y parametresine .3 değerini verdik. 

Sonra, butonumuzun bind() metodu ile on_press olayını, self.press fonksiyonumuza bağladık. Fonksiyon ismini istediğiniz şekilde belirleyebilirsiniz. Ancak dikkat etmeniz gereken şey, fonksiyonun aldığı parametrelerdir. Fonksiyonumuz self hariç bir tane daha parametre alır. Bu parametre, olayın kaynağı olan pencere aracıdır. Dolayısıyla butona tıkladığımızda olayın kaynağı bu buton oluyor.

Button sınıfına dair bazı özellikleri tanımlamayalım

background_color
----------------

Butonumuzun arkaplan rengi. (r,g,b,a) formatında değer alır. 

.. code-block:: python

	buton = Button(text = "Buton", background_color = [1,1,0,1])

veya

.. code-block:: python

	buton.background_color = [1,1,0,1]

background_normal
-----------------

Butonun basılı olmadığı durumdaki arkaplan resmi. Resmin adını yazmanız yeterlidir. Resminiz ana program ile aynı klasörde olmalıdır. Eğer bir alt klasörde ise, mesela images klasöründe ise "images/resim.png" yazmalısınız

.. code-block:: python

	buton = Button(text = "Buton",background_normal = "resim.png")

veya

.. code-block:: python

	buton.background_normal = "resim.png"

background_down
---------------

Butona basılı haldeki arkaplan resmi. background_normal ile aynıdır. 

.. code-block:: python

	buton = Button(text = "Buton",background_down = "resim.png")

veya

.. code-block:: python

	buton.background_down = "resim.png"


disabled
--------

Butonun aktif olup olmama durumu. True değeri verilirse buton deaktif hale gelecektir. Bu durumda butona tıklama yapılamaz. Eğer False değeri verilirse buton aktif hale gelecektir

.. code-block:: python

	buton = Button(text = "Buton",disabled = True)

veya

.. code-block:: python

	buton.disabled = True

background_disabled_normal
--------------------------

Buton aktif olmadığı durumdaki arkaplan resmi

.. code-block:: python

	buton = Button(text = "Buton",background_disabled_normal = "resim.png")

veya

.. code-block:: python

	buton.background_disabled_normal = "resim.png"


background_disabled_down
------------------------

Buton aktif olmadığı durumda, butona basıldığı zaman belirlenen arkaplan resmi

.. code-block:: python

	buton = Button(text = "Buton",background_disabled_down = "resim.png")

veya

.. code-block:: python

	buton.background_disabled_down = "resim.png"

border
------

Butonun kenar genişlikleri. [alt,sağ,üst,sol] formatında değer alır. Varsayılan değeri [16,16,16,16]

.. code-block:: python

	buton = Button(text = "Buton",border = [2,2,2,2])

veya

.. code-block:: python

	buton.border = [2,2,2,2]


Button sınıfıyla ilgili daha detaylı bilgi için https://kivy.org/doc/stable/api-kivy.uix.button.html

TextInput
=========

kivy.uix.textinput.TextInput

TextInput, kullanıcıdan girdi almayı sağlar, programlarda çok kullandığımız metin kutularıdır. Tek satırlı, çok satırlı, yıldızlı girdi alma ve daha birçok işlem için kullanılabilir. Aynı zamanda CTRL+C, CTRL+Z gibi kısayol tuşları da kullanılabilir.

kivy.uix.textinput modülü içerisinde yer alır. Hatırlarsanız BoxLayout konusunda bir `örnek <layout.html#target>`__ yapmıştık. Bu örnek kullanıcıdan nick ve şifre almak üzere tasarlanmıştı ama henüz birşey yapamıyordu. İşte şimdi bu yazdığımız örneği kullanılabilir hale getireceğiz. 

Öncelikle örneğimizi tekrar yazalım

.. code-block:: python
	
	from kivy.app import App
	from kivy.uix.label import Label
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.button import Button
	from kivy.uix.textinput import TextInput

	class Program(App):
	    def build(self):

	        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz

	        self.ilkSatir = BoxLayout()
	        self.ikinciSatir = BoxLayout()

	        self.nick = Label(text = "Nick")
	        self.nickKutu = TextInput()

	        self.sifre = Label(text = "Şifre")
	        self.sifreKutu = TextInput()

	        self.buton = Button(text = "Giriş Yap")


	        self.ilkSatir.add_widget(self.nick)
	        self.ilkSatir.add_widget(self.nickKutu)

	        self.ikinciSatir.add_widget(self.sifre)
	        self.ikinciSatir.add_widget(self.sifreKutu)

	        # Şimdi hepsini ana düzene yerleştiriyoruz

	        self.anaDuzen.add_widget(self.ilkSatir)
	        self.anaDuzen.add_widget(self.ikinciSatir)
	        self.anaDuzen.add_widget(self.buton)

	        return self.anaDuzen

	Program().run()

Nick aldığımız metin kutusunu tek satırlı hale getirmeliyiz. Yani kullanıcı Enter'a bastığı zaman alt satıra geçmemeli. Bunun için

.. code-block:: python
	
	nickKutu = TextInput(multiline = False)

yazmamız yeterli. Böylece artık alt satıra geçmeyecek, sağa doğru yazmaya devam edecektir. Bu arada eğer multiline değeri "False" ise, kullanıcı Enter'a bastığında metin kutusu odaktan çıkacaktır. 

Şimdi de parolayı aldığımız kutucuğu tek satırlı hale getirelim ve yazılanların görünmemesi için parolayı yıldızlı hale getirelim.

.. code-block:: python

	sifreKutu = TextInput(multiline = False, password = True)

Böylece kullanıcı şifresini girdiğinde, yazdığı karakter değil yıldız görünecektir. Varsayılan olarak yıldızdır. Değiştirmek isterseniz;

.. code-block:: python

	sifreKutu = TextInput(multiline = False,password = True,pasword_mask = "?")

Ya da

.. code-block:: python

	sifreKutu.password_mask = "?"

Şimdi de butonumuza olay ekleyelim. Yani butona basıldığı zaman kutulardaki bilgileri alsın ve kontrol etsin. Eğer bilgiler doğru olursa "Giriş başarılı" yazsın, hatalıysa "Hatalı Giriş" yazsın.

Kodumuzu yeniden yazacak olursak

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.label import Label
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.button import Button
	from kivy.uix.textinput import TextInput

	class Program(App):
	    def build(self):

	        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz

	        self.ilkSatir = BoxLayout()
	        self.ikinciSatir = BoxLayout()

	        self.nick = Label(text = "Nick")
	        self.nickKutu = TextInput(multiline = False)

	        self.sifre = Label(text = "Şifre")
	        self.sifreKutu = TextInput(multiline = False,
	                              password = True,
	                              password_mask = "?")

	        self.buton = Button(text = "Giriş Yap")
	        self.buton.bind(on_press = self.kontrol) # Butonumuza tıklama olayı ekledik


	        self.ilkSatir.add_widget(self.nick)
	        self.ilkSatir.add_widget(self.nickKutu)

	        self.ikinciSatir.add_widget(self.sifre)
	        self.ikinciSatir.add_widget(self.sifreKutu)

	        # Şimdi hepsini ana düzene yerleştiriyoruz

	        self.anaDuzen.add_widget(self.ilkSatir)
	        self.anaDuzen.add_widget(self.ikinciSatir)
	        self.anaDuzen.add_widget(self.buton)

	        return self.anaDuzen

	    def kontrol(self,event = None):
	        if(self.nickKutu.text == "admin" and self.sifreKutu.text == "12345"):
	            print("Giriş Başarılı")

	        else:
	            print("Hatalı Giriş")
	        

	Program().run()

Programı çalıştırıp kullanıcı adını "admin" ve parolayı "12345" olarak girerseniz "Giriş Başarılı" yazılacaktır. Ancak ikisinden herhangi birini yanlış yazarsanız "Hatalı Giriş" yazılacaktır. 

Kutulardaki metinleri kutu.text niteliği yardımıyla aldık. Bu bir String değerdir ve eğer kullanıcıdan sayı aldığımızda bunun String olarak bize verildiğini ve bunu Integer'a çevirmemiz gerektiğini unutmayalım.

TextInput Girdilerini Kontrol Etme
----------------------------------

TextInput aracımıza girilen girdileri kontrol etmek istersek, TextInput.insert_text() metodunun üzerine yazmalıyız. Yani bu sınıfı miras alıp insert_text() metodunu kendimize göre tekrar yazmalıyız. Hemen bir örnekle bunu görelim

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.textinput import TextInput

	class MyInput(TextInput):

	    def insert_text(self,substring,from_undo = False):
	        s = substring.upper()
	        return super(MyInput,self).insert_text(s,from_undo)

	    

	class Program(App):

	    def build(self):
	        return MyInput()

	Program().run()

Programımıza girilen karakter ister küçük ister büyük olsun, her zaman büyük olarak metin kutusuna eklenecektir. Peki bunu nasıl yaptık? Öncelikle TextInput() sınıfını miras aldık. Miras alma işlemini nesne yönelimli programlamadan biliyor olmanız gerekiyor. Kısaca miras alma, önceden yazılan bir sınıfı yeni yazılan sınıfa katma, onun özelliklerini de kullanmaktır. Biz burada kendimize ait bir metin kutusu yapmak istediğimiz için, ilk olarak TextInput sınıfını miras aldık. 

Bu sınıf, girilen yazıları inser_text() metoduyla işlediği için, biz de bu metodu yeniden yazdık. Böylece bir karakter girildiği zaman TextInput sınıfının insert_text() metodu değil, bizim yazdığımız sınıfın insert_tex() metodu çalışacaktır. Böylece biz de gelen karakterleri işleyebileceğiz. Girilen karakter "substring" argümanıyla gelir. Bunu işleyip üst sınıfa işlenmiş olarak göndereceğiz. Biz de burada gelen karakter upper() metoduyla büyük karaktere dönüştürdük ve üst sınıfın insert_text() metodunu değiştirilmiş karakterle birlikte çağırdık. Miras aldığımız sınıfın metodunu çağırmak için super() metodundan yararlanıyoruz. 

Bir karakteri değiştirdiğimiz gibi, bu karakterin yazılmamasını da sağlayabiliriz. Diyelim ki "j" harfinin hiç girilmemesini istiyorsunuz, bu durumda "j" harfinin girilmesini şu şekilde engelleyebilirsiniz.

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.textinput import TextInput

	class MyInput(TextInput):

	    def insert_text(self,substring,from_undo = False):
	        if(substring.lower() == "j"):
	            return False
	        else:
	            return super(MyInput,self).insert_text(substring,from_undo)

	    

	class Program(App):

	    def build(self):
	        return MyInput()

	Program().run()

Programa büyük "J" harfi de girilebileceği için, gelen büyük karakteri küçülterek kontrol edip, hiçbir şekilde bu harfin girişine izin vermiyoruz.

Şimdi, TextInput ile birlikte kullanabileceğimiz bazı nitelikleri ve olayları inceleyelim.

selection_text
--------------

TextInput üzerinde bir yazı seçildiği zaman, bu seçili yazıya selection_text ile erişebiliriz. Böylece seçili yazı üzerinde işlemler yapabiliriz.

focus
-----

TextInput üzerine odaklanıldığı zaman veya odaktan ayrıldığı zaman meydana gelen olay. Örnek kullanım

.. code-block:: python

	def on_focus(instance, value):
		if value:
			print('Odaklanıldı', instance)
		else:
			print('Odaktan çıktı', instance)
	
	textinput = TextInput()
	textinput.bind(focus=on_focus)

copy(veri<str>)
---------------

Copy fonksiyonu, kopyalama hafızasına verilen "veri" değerini kopyalar. "veri" argümanı String olmalıdır. Eğer "veri" argümanı verilmezse, o anda metin kutusu üzerinde seçili olan metni hafızaya kopyalar. 

.. code-block:: python

	metinKutusu.copy()

Ya da 

.. code-block:: python

	metinKutusu.copy("kopyala")

cut()
-----

Copy ile aynı işi yapmakla beraber, kopyaladığı metni metin kutusundan siler, yani bildiğimiz kesme işlemini yapar.

paste()
-------

Kopyalama hafızasındaki metni, metin kutusuna o andaki cursor pozisyonuna yerleştirir. 

readonly 
--------

Eğer metin kutusundaki ifadenin kullanıcı tarafından değiştirilmesini istemiyorsanız, readonly niteliğine True değerini vermelisiniz. Böylece kullanıcılar metin kutusundaki metni değiştiremeyecek ancak okuyup kopyalayabilecektir. 

.. code-block:: python

	metinKutusu.readonly = True

tab_width
---------

Tab tuşunun varsayılan değeri 4'tür. Eğer bu değeri değiştirmek isterseniz tab_width parametresine bu değeri sayı olarak vermelisiniz. 

text
----

TextInput içerisindeki metinde bir değişiklik olduğu zaman, bir "text" olayı meydana gelir. Bu olayı aşağıdaki örnekteki gibi ele alabiliriz

.. code-block:: python

	def on_text(instance, value):
	    print("TextInput metni değişti: {}".format(value))

	textinput = TextInput()
	textinput.bind(text=on_text)


CheckBox
========

kivy.uix.checkbox.CheckBox

Onay kutuları, genelde bir seçeneğin seçilip seçilmeyeceği veya birden fazla seçenek arasından bir tanesinin seçilmesi gerektiği durumlarda kullanılır. Örneğin, internet sitelerinde üye girişi yaparken bize sorulan "Hesabımı Hatırla" sorusunun yanında bir tane onay kutusu vardır. Seçili olduğunda, bir sonraki girişiniz otomatik yapılacaktır demektir. Eğer seçili olmazsa tarayıcı kapandığı zaman bilgileriniz artık hatırlanmayacaktır.

Çoklu seçime örnek verecek olursak, formlarda cinsiyet sorulduğu zaman Bay-Bayan şeklinde iki seçenekten birisinin seçilmesi gerektiği durumlarda kullanılır. Kivy, bu iki aracı da kullanabilmemiz için bize sunmuştur. Şimdi bunları nasıl kullanacağımızı görelim. Önceki yazılarda yazdığımız örneğe bir de onay kutusu ekleyelim

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.label import Label
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.button import Button
	from kivy.uix.textinput import TextInput
	from kivy.uix.checkbox import CheckBox

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.label import Label
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.button import Button
	from kivy.uix.textinput import TextInput

	class Program(App):
	    def build(self):

	        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz

	        self.ilkSatir = BoxLayout()
	        self.ikinciSatir = BoxLayout()

	        self.nick = Label(text = "Nick")
	        self.nickKutu = TextInput(multiline = False)

	        self.sifre = Label(text = "Şifre")
	        self.sifreKutu = TextInput(multiline = False,
	                              password = True,
	                              password_mask = "?")

	        self.buton = Button(text = "Giriş Yap")
	        self.buton.bind(on_press = self.kontrol) # Butonumuza tıklama olayı ekledik


	        self.ilkSatir.add_widget(self.nick)
	        self.ilkSatir.add_widget(self.nickKutu)

	        self.ikinciSatir.add_widget(self.sifre)
	        self.ikinciSatir.add_widget(self.sifreKutu)

	        self.onaySatir = BoxLayout(size_hint_y = .3)
	        # onay kutumuzu ve yazımızı tutacak olan BoxLayout
	        # Boyutunu biraz küçülttük :)
	        
	        self.onayYazi = Label(text = "Beni Hatırla")
	        self.onayKutu = CheckBox()

	        self.onaySatir.add_widget(self.onayYazi)
	        self.onaySatir.add_widget(self.onayKutu)

	        # Şimdi hepsini ana düzene yerleştiriyoruz

	        self.anaDuzen.add_widget(self.ilkSatir)
	        self.anaDuzen.add_widget(self.ikinciSatir)
	        self.anaDuzen.add_widget(self.onaySatir)
	        self.anaDuzen.add_widget(self.buton)

	        return self.anaDuzen

	    def kontrol(self,event = None):
	        if(self.nickKutu.text == "admin" and self.sifreKutu.text == "12345"):
	            if(self.onayKutu.active):
	                print("Giriş Başarılı ve bilgileriniz hatırlanacak")
	            else:
	                print("Giriş Başarılı, bilgileriniz hatırlanmayacak")

	        else:
	            print("Hatalı Giriş")


	Program().run()

.. image:: images/examcheck.png
 :align: center

BoxLayout içerisine bir satır daha ekledik. Bu satırımız, "Beni Hatırla" yazısını ve onay kutusunu taşıyor. Girişi kontrol ettiğimiz kontrol() fonksiyonunda onay kutusunun "active" yani seçili olup olmadığını kontrol ettik. Onay kutusunun seçili olup olmadığını "active" niteliğiyle öğrenebiliriz. Eğer True ise, kutu seçili demektir. Eğer False ise, onay kutusu seçili değil demektir.

CheckBox pencere aracını, RadioButton olarak kullanmak isterseniz elinizdeki onay kutularının gruplarına aynı değerleri vermeniz gerekiyor. Örneğin

.. code-block:: python

	kutu1 = CheckBox(group = 1)
	kutu2 = CheckBox(group = 1)

	kutu3 = CheckBox(group = 2)
	kutu4 = CheckBox(group = 2)

kutu1 ve kutu2 aynı grupta olduğu için, biri aktif olduğunda diğeri deaktif olacaktır. 

.. image:: images/check.png
 :width: 300px
 :align: center

CheckBox ile ilgili bazı niteliklere bakalım

color
-----

CheckBox görünümünü(rengini) değiştirmek için kullanılabilir. Liste veya demet olarak parametre alır

active
------

Eğer bir CheckBox'ın aktif olma olayını ele almak isterseniz, bind ile tanımlayıp active parametresine fonksiyonunuzu yazmanız gerekir

.. code-block:: python

	def on_checkbox_active(checkbox, value):
		if value:
			print('Checkbox', checkbox, 'aktif')
		else:
			print('Checkbox', checkbox, 'deaktif')
	
	checkbox = CheckBox()
	checkbox.bind(active=on_checkbox_active)

Fonksiyonunuz iki parametre almalıdır. Birincisi CheckBox'ın kendisi, diğeri aktif olup olmama durumunu belirten boolean bir parametre(True veya False).

Image
=====

kivy.uix.image.Image

Eğer uygulamamızda resim göstermek istersek, Image kullanabiliriz. Kivy ile resimleri kullanmak oldukça kolay. Birden fazla resim formatını destekliyor. Yapmamız gereken sadece gerekli sınıfı import etmek ve resim dosyasının yolunu yazmak. Bir örnekle görelim.

.. code-block:: python

	# coding:utf-8

	from kivy.uix.image import Image
	from kivy.app import App

	class Yazbel(App):

	    def build(self):
	        resim = Image(source = "resim.png")
	        
	        return resim
	    
	Yazbel().run()

resim.png dosyası, programınızın ana dosyası ile aynı dizinde olmalıdır. Aksi takdirde ekranda beyaz boş bir alan gösterilir. Resim gösterildiği zaman, boyutu neyse o şekilde yerleştirilir. Resmin boyutlandırılmasını birazdan nitelikleri incelediğimiz zaman göreceğiz. 

Resimleri sadece bilgisayarınızdaki bir dosyadan değil, aynı zamanda internet üzerinden gösterebilirsiniz. Bunun için AsyncImage kullanılır. Buyrun örnekle görelim :)

.. code-block:: python

	# coding:utf-8

	from kivy.uix.image import Image,AsyncImage
	from kivy.app import App

	class Yazbel(App):

	    def build(self):
	        resim = AsyncImage(source = "https://www.blogger.com/img/blogger-logotype-color-black-1x.png")
	        
	        return resim
	    
	Yazbel().run()

Resim internet üzerinde yüklenirken, resmin halen yüklenmekte olduğunu gösteren bir "loading" gif'i resmin yerinde durur. Resim yüklenince "loading" gif'i kaldırılır. Eğer bu "loading" gif'ini değiştirmek isterseniz, Loader sınıfını import edip, varsayılanı değiştirmeniz gerekir.

.. code-block:: python

	from kivy.loader import Loader # import etme

	Loader.loading_image = "your.gif" # varsayılanı değiştirme


Resmin Boyutlarını Değiştirme
-----------------------------

Bir resmin boyutlarını değiştirebiliriz. Bunun için kv dilinden yardım alabiliriz. 

.. code-block:: python

	Image:
		source:"resim.png"
		width:100
		height:600
		size_hint_x:None
		size_hint_y:None
		keep_ratio:False
		allow_stretch:True
		
Resmin istenilen şekilde boyutlandırılabilmesi için, orantılı boyutlandırma özellikleri None yapılmalıdır. Ve resmin en-boy oranını koruma özelliği False, uzatılma özelliği True yapılmalıdır. Artık resmin boyutlarıyla istediğimiz gibi oynayabiliriz :)


allow_stretch
-------------

Resmimizin bulunduğu alanı tam olarak doldurmasını istiyorsak kullanabiliriz. Değer olarak True veya False alabilir. True değeri verildiğinde, bulunduğu alana göre boyutu arttırılır. Ancak en-boy oranı korunur. Örneğin, eni boyundan büyük olan bir resim, boyutu arttığı zaman da eni boyundan büyük olacaktır. 

keep_ratio
----------

allow_stretch ile birlikte, en-boy oranını korumadan bulunduğu alanı tam olarak doldurmasını istersek, keep_ratio değerini False yapmalıyız. Bu parametre de, True veya False olarak iki değer alır.

anim_delay
----------
Eğer yüklediğiniz resim bir gif ise(veya başka bir animasyon formatı), resim kareleri arasında geçiş süresini anim_delay ile ayarlayabilirsiniz. Varsayılan olarak 0.25'tir. Yani saniyede 4 kare. 

anim_loop
---------

Gif dosyamızın kaç kere döngüye gireceğini belirtebiliriz. Örneğin gif'in sadece 1 kez çalışmasını istersek,

.. code-block:: python

	resim.anim_loop = 1

yazmalıyız. Böylece gif resmimiz bir kere çalışacak ve duracaktır. Varsayılan olarak 0'dır ve -1 değeri verilirse duracaktır

reload()
--------

Diskten okuduğumuz resmi değiştirdiğimizde, bunu uygulama içinde güncellemek istersek reload() metodunu kullanabiliriz.

ProgressBar
===========

kivy.uix.progressbar.ProgressBar

ProgressBar ile bir işlemin ne kadarının tamamlandığını görsel olarak gösterebiliriz. Kullanımı gayet basit. Basit bir örnek yapalım

.. code-block:: python

	# -*- coding: utf-8 -*-

	from kivy.app import App
	from kivy.uix.progressbar import ProgressBar
	from kivy.clock import Clock

	class Yazbel(App):
	    def build(self):
	        self.bar = ProgressBar(max = 100)
	        self.deger = 0

	        Clock.schedule_once(self.say,1) # 1 ms sonra self.say adlı fonksiyona git

	        return self.bar


	    def say(self,event = None):
	        if(self.deger <= 100):

	            self.bar.value = self.deger
	            self.deger += 5

	            Clock.schedule_once(self.say,.5)

	        
	Yazbel().run()

ProgressBar'mızı tanımladık ve max değerini 100 olarak verdik. Yani eğer barımızın değerini en fazla 100 olarak verebiliriz. Eğer 10 olarak belirleseydik, en fazla 10 değerini verebilirdik. Sonra Clock yardımıyla sayacımız 100 olana kadar döngüye girdik ve barımızın değerini değiştirdik.
