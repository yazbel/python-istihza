Olaylar
#######

Olaylardan önceki bölümlerde bahsetmiştik, ancak detaylı olarak anlatmamıştık. Bu bölümde olaylardan biraz daha detaylı bir şekilde bahsedeceğiz. Öncelikle olay nedir tanımlamaya çalışalım. Bir olay, kullanıcı etkileşimi sonucu oluşabilen durumların tümüne denir. Örneğin kullanıcının bir butona tıklaması, bir pencere aracının üzerine mouse ile gelmesi, bir pencere aracından mouse tıklamasını kaldırması veya bir pencere aracını seçmesi(checkbox gibi araçlar) bütün hepsi birer olay olarak ele alınır. 

Kullanıcı taraflı gerçekleşmeyen, ancak birer olay olarak ele alınan durumlar da vardır. Örneğin bir resmin yüklenmeye başlaması, yüklenmesinin bitmesi durumları da birer olaydır. Bunlara da yeri geldiğinde değineceğiz.

Olaylar, kullanıcı hareketlerini yorumlamanın iyi bir yoludur. Bu hareketleri yorumlamak için, fonksiyonlarımızı ilgili olaylara bağlamalıyız. Örneğin kullanıcı butona bastığı zaman şu fonksiyonum çalışsın, ben de gerekli bilgileri alarak işlem yapayım.

Şimdi bazı belli başlı olayları inceleyelim.

Clock Olayları
==============

Clock ile ilgili daha önce bir örnek yapmıştık. Clock sınıfı, belirtilen süre sonunda bir fonksiyon çalıştırmak üzere tasarlanmıştır. İşte bu süre sonunda fonksiyonu çalıştırması, bir olay olarak ele alınıyor. Clock için zamanlayıcı da diyebiliriz.

Clock sınıfını iki şekilde kullanabiliriz. Birincisi, fonksiyonun sadece bir kez çağrılması. Yani belirtilen süre sonunda, fonksiyon çalıştırılır ve işlem tamamlanır. Bir örnekle görelim

.. code-block:: python
	
	# coding: utf-8

	from kivy.app import App
	from kivy.clock import Clock
	from kivy.uix.label import Label

	class Program(App):
	    def build(self):

	        self.yazi = Label(text = "Merhaba")

	        Clock.schedule_once(self.degistir,3) # 3 saniye sonra, self.degistir adlı fonksiyonu çalıştır

	        return self.yazi

	    def degistir(self,event):
	        self.yazi.text = "Dünya"


	Program().run()

Program başladıktan 3 saniye sonra, ekrandaki "Merhaba" yazısı, "Dünya" yazısıyla değiştirilecektir. Böylece işlem tamamlanmış olacaktır. 

Clock sınıfının bir başka kullanımı ise, belli aralıklarla sürekli çalışmasıdır. Fonksiyonu çalıştırır, sonra belirtilen süre kadar bekler ve sonra tekrar çalıştırır. Bunu, siz sonlandırana kadar veya program kapanana kadar yapmaya devam eder. Saat örneği, bu kullanım için çok iyi bir örnektir.

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.clock import Clock
	from kivy.uix.label import Label
	import datetime

	class Program(App):
	    def build(self):
	        self.yazi = Label(text = "Merhaba",markup = True)

	        Clock.schedule_interval(self.degistir,1) # 1 saniye sonra, self.degistir adlı fonksiyonu çalıştır

	        return self.yazi

	    def degistir(self,event):
	        zaman = datetime.datetime.now()
	        self.saat = "[size=25sp]{}:{}:{}[/size]".format(zaman.hour,zaman.minute,zaman.second)
	        self.yazi.text = self.saat


	Program().run()

Programda kullandığımız datetime modülü, zaman bilgisini elde etmek içindir. Dikkat ettiyseniz, sürekli çalışmasını istediğimizde Clock.schedule_interval() kullanıyoruz. Bir saniye aralıkla çalışmasını sağlayarak, ekranda zaman bilgisini göstermiş olduk. 

Her iki kullanım şeklinde dikkat etmemiz gereken şey, çalıştırılacak olan fonksiyonun mutlaka bir argüman almasıdır. Burda kullandığımız "self" dışında alması gereken bir argüman olduğunu görüyoruz. Bu argüman, belirlediğimiz zamanın kendisidir.

Eğer tanımladığınız bir Clock nesnesini kaldırmak isterseniz;

.. code-block:: python

	# Tanımladık
	self.event = Clock.schedule_interval(self.fonk,2)
	self.event2 = Clock.schedule_once(self.fonk2,5)

	# Ve bunları kaldırıyoruz
	self.event.cancel()
	Clock.unschedule(self.event2)

Girdi Olayları
==============

Kullanıcı girdisi sonucu oluşan olaylardır. Tıklama, basılı halde sürükleme, bırakma, mouse tekerleği hareketi gibi hareketler sonucu oluşan olaylardır. Daha önce buna benzer olayları bazı pencere araçlarımızda ele almıştık. Bunlardan birisi Button sınıfıydı. Bir butonun üzerine tıklanması on_press, bırakılma olayı da on_release ile dinleniyordu. 

Genelde bir pencere aracının sahip olduğu olaylar, ilgili `API <https://kivy.org/doc/stable/api-index.html>`_ kaynağında bulunur. Böylece kaynağa bakarak, ele almak istediğimiz olayları bind() yardımıyla bağlayabiliriz. Basit bir örnek yapalım isterseniz

.. code-block:: python

	# coding: utf-8

	from kivy.app import App
	from kivy.uix.boxlayout import BoxLayout
	from kivy.uix.textinput import TextInput

	class Program(App):
	    def build(self):

	        self.metin_kutusu = TextInput()
	        self.metin_kutusu.bind(text = self.kontrol)

	        return self.metin_kutusu


	    def kontrol(self,instance,value):
	        print(value)
	        
	Program().run()

TextInput pencere aracı üzerinde herhangi bir yazı yazıldığında çalışacak olan kontrol fonksiyonumuzu tanımladık. Bu fonksiyon iki adet parametre alıyor(self hariç). Bunlardan instance, pencere aracının kendisi, diğeri ise bunun içerdiği metindir. Herhangi bir karakter girişinde kontrol fonksiyonumuz çağrılacaktır. Bağlama işlemini de bind() ile yaptığımıza dikkat edin.

Bunun gibi birçok pencere aracının sahip olduğu olayları API kaynağından inceleyebilirsiniz. Biz de yeri geldiğinde bunlara değineceğiz ve kullanacağız. 

