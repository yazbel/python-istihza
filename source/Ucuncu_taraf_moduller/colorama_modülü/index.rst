.. meta::
   :description: Colorama modülünün kullanımı
   :keywords: python, colorama

.. highlight:: python3

###############
Colorama Modülü
###############

Colorama modülü, konsol penceresindeki yazıları renklendirmeyi ve stil vermeyi sağlar.

Kurulum
=======

Varsayılan python’a colorama modülünü kurmak için bilgisayarınızın komut satırına şunları girin:

	pip install colorama

.. Note:: Bu komutları Windows ortamında verebilmek için python’u yola eklemeniz gerekir. Python kurulum aşamasında altta bulunan add to Path seçeneğini işaretlediyseniz python yola eklenmiştir.

Kullanım
========

Colorama modülünü anlayabilmek için basit bir örnek yapalım:

.. code-block:: python

	from colorama import Fore, Back, Style, init
	init(autoreset=True)
	print(Fore.RED + 'sade kırmızı yazı')
	print(Back.GREEN + 'Yeşil arkaplan')
	print(Style.DIM + 'Python')
	print(Style.RESET_ALL)
	print('Tekrar normal haline döndü')

Gördüğünüz üzere colorama modülünün Fore, Back ve Style sınıflarının belirlenmiş nitelikleri ile herhangi bir karakter dizimizi birleştirip yazdırdığımızda niteliğe göre renkli yazılar elde ediyoruz. Fore yazının kendisi, Back arka planı, Style ise stilini ilgilendirir.

Peki neden init fonksiyonunu çağırdık?

İnit bildiğiniz üzere “initalization” (ilklendirme) sözcüğünün kısaltılmışıdır. Buradaki kullanımı da sözcük anlamıyla uyumludur. Yani bizim renklendirme işlemimizde birtakım ayarları yapmamız için bir başlangıçtır. Bunu yapmamız zorunludur. Yapmazsak kodlarımız renklenmeyecek, sadece renk kodu sadece ekrana bastırılacaktır.

Bu noktada bir detaya değinelim: Bu Fore, Back ve Style sınıflarının belirlenmiş nitelikleri aslında alelade bir karakter dizisidir:

.. code-block:: python

	print('\033[31m' + 'sade kırmızı yazı')
	print('\033[30m') # Ve yeniden öntanımlı renge döndük

Gördüğünüz gibi yukarıdakiyle aynı sonucu elde ettik.

Şimdi Fore, Back ve Style sınıflarının en çok kullanılan renk niteliklerini görelim:

	Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

	Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

	Style: DIM, NORMAL, BRIGHT, RESET_ALL

Colorama modülünün termcolor modülü ile kullanımı
-------------------------------------------------

Termcolor modülü colorama modülünü kullanırken işimiz çok kolaylaştırır.

.. code-block:: python

	from colorama import init
	from termcolor import colored
	#termcolor modülü colorama kullandığı için ilklendirme şarttır
	init()

	#İlk parametremiz karakter dizimiz, ikinci parametremiz rengi, üçüncü ise arkaplan rengidir.
	print(colored('Hello, World!', 'green', 'on_red'))
	# colored fonksiyonundan dönen değeri kullanabilmek için yazdırmamız gerekir.

.. note:: termcolor modülü yüklü gelmemektedir, kurulum aşamasındaki kodlarda colorama yerine termcolor yazarak kurabilirsiniz.

Termcolor modülü ile daha fazla bilgi için:  https://pypi.org/project/termcolor/

İnit fonksiyonun argümanları
============================

İnit fonksiyonunun birçok isimli argümanı bulunur:

autoreset=False
---------------

.. code-block:: python

	from colorama import Fore, init
	init(autoreset=False)
	print(Fore.RED + “Bu kırmızı olur ama;”)
	print(“Bunun rengi default’tur”)

.. code-block:: python

	from colorama import Fore, init
	init(autoreset=False) #Böyle yapsak da değişmez: init()
	#çünkü bu zaten öntanımlıdır
	print(Fore.RED+”Artık bundan sonra yazdırılan her şey değiştirilmediği sürece kırmızıdır”)
	print(“mesela bu kırmızı”)

Diğerlerine ihtiyacınızın olmayacağını düşündüğümüz için buraya yazmadık.
Diğer argümanları colorama PyPI sayfasında görebilirsiniz.

