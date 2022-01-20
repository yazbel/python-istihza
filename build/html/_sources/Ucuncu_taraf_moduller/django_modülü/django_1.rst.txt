.. meta::
   :description: Bu bölümde django ile site yapmaya başlayacağız.
   :keywords: python, django, çeviri

.. highlight:: python3

******************************
İLK DJANGO PROJENİ YAZ, part 1
******************************

Bir örnekle öğrenmeye başlayalım. Bu örnekte basit bir anket uygulaması oluşturacağız.
Uygulama iki kısımdan oluşacak:

	#. Anketlerin oylanması için herkese açık bir site
	#. Anketleri düzenlemek veya ekleyip silmek için bir admin paneli

Senin Djangoyu yüklediğini varsayıyoruz. Komut isteminde aşağıdaki komutu çalıştırarak Djangonun yüklü olup olmadığına ve Django sürümüne ulaşabilirsin::

	python -m django --version

Eğer Django yüklüyse yüklü olan versiyonu görmelisin. Eğer değilse "No module named django" yazısı ile karşılaşmalısın.

Bir proje oluştur
==================

Komut satırında cd komutuyla komutunuzu saklamak istediğiniz dizine gidin ve aşağıdaki kodu çalıştırın::

	django-admin startproject mysite

Bu kod bulunduğunuz dizinde mysite dizinini yaratacak.
Şimdi `startproject` komutunun oluşturduklarına bakalım::

	mysite/
	    manage.py
	    mysite/
	        __init__.py
	        settings.py
	        urls.py
	        wsgi.py

En dışardaki `mysite/` dizini, projeniz için sadece bir kapsayıcıdır. Adı Django için önemli değil. Beğendiğiniz herhangi bir şeyle yeniden adlandırabilirsiniz.
`manage.py`: Komut satırından django projesiyle etkileşime geçmenizi sağlayan bir programdır.
İçerideki `mysite/` dizini , projeniz için gerçek bir python paketidir.
`mysite/init.py`: Boş bir python dosyasıdır. mysite/ dizininin python paketi olmasını sağlar.
`mysite/setting.py`: Django projesinin ayarları ile ilgili bir dosya.
`mysite/urls.py`: Projeniz için URL'leri barındıran dosya.
`mysite/wsgi.py`: WSGI uyumlu web sunucuları için projenize hizmet edecek bir giriş noktası.

Geliştirme sunucusu
====================

Şimdi django projemizin çalışıp çalışmadığını kontrol edelim. Komut satırında dışarıdaki `mysite` dizinine gidin ve aşağıdaki kodu çalıştırın::

	python manage.py runserver

Çıktı olarak şunu görmelisin::

	Performing system checks...

	System check identified no issues (0 silenced).

	You have unapplied migrations; your app may not work properly until they are applied.
	Run 'python manage.py migrate' to apply them.

	April 29, 2018 - 15:50:53
	Django version 2.0, using settings 'mysite.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

.. Note:: Veritabanıyla ilgili uyarıyı dikkate almayın.

Django geliştirme sunucusunu başlattınız.

Kullanılan portu değiştirme
============================

`runserver` komutu geliştirme sunucusu için standart olarak 8000 portunu kullanır.
Eğer bu portu değiştirmek isterseniz bunu komuta argüman olarak verin. Mesela aşağıdaki komut 8080 portunda geliştirme sunucusunu çalıştırıyor::

	python manage.py  runserver 8080

Eğer sunucunun IP adresini değiştirmek isterseniz port ile birlikte belirtin. Örnek olarak kullanılabilir tüm IP'leri dinlemek istiyorsanız şu kodu çalıştırın::

	python manage.py runserver 0:8000

Yukarıda yazdığımız kodda 0'ın anlamı 0.0.0.0 (Yani bir kısaltma).

Bir anket uygulaması oluşturalım
=================================

Artık proje ortamımız kuruldu. Çalışmaya başlayabiliriz.
Django'da yazdığımız her uygulama bir python paketinden oluşur ve Django'da uygulamanın dizini otomatik olarak oluşturulur. Bu sayede dizin oluşturmakla uğraşacağımız zamanda kod yazabiliriz.
Bir uygulama oluşturmak için komut satırında `manage.py` ile aynı dizine gelin ve şu komutu yazın::

	python manage.py startapp polls

`polls` isimli bir dizin oluşturulacak. Bakaklım içinde neler var::

	polls/
	    __init__.py
	    admin.py
	    apps.py
	    migrations/
	        __init__.py
	    models.py
	    tests.py
	    views.py

Bu dizin anket uygulamamızın merkezi olacak.

İlk view'ımızı yazalım
=======================

Hadi yazmaya başlayalım. Şimdi `polls/views.py` açın ve şu kodları yazın::

	from django.http import HttpResponse
	def index(request):
	    return HttpResponse("Hello, world. You're at the polls index.")

Bu Django'da yazılabilecek en basit view. Artık bu view ı çağırabilmek için bir URL haritasına ihtiyacımız var ve URL haritası için de URL şemasına.
polls dizininde `urls.py` isimli bir dosya oluşturarak uygulamanın URL şemasını da oluşturmuş oluruz.(Dosya Gezgininden kendiniz urls.py isimli bir python modülü oluşturun.)  Uygulama dizini son olarak şöyle görünmeli::

	polls/
	    __init__.py
	    admin.py
	    apps.py
	    migrations/
	        __init__.py
	    models.py
	    tests.py
	    views.py
	    urls.py

Şimdi de yeni oluşturduğumuz polls dizinindeki urls.py dosyasında şu kodlar yazılı olmalı::

	from django.urls import path
	from . import views

	urlpatterns = [
	    path('', views.index, name='index'),
	]

Burada oluşturduğumuz URL şemasını gerçek Url şemasında tanıtmanın vakti geldi. Bunun için mysite dizinindeki urls.py dosyasında include fonksiyonunu içe aktarıp  url listesini aktarmada kullanacağız. Sonuç olarak mysite dizinindeki urls.py dosyanız şu hale gelmeli::

	from django.contrib import admin
	from django.urls import include, path

	urlpatterns = [
	    path('polls/', include('polls.urls')),
	    path('admin/', admin.site.urls),
	]

Artık index view'ını bir dizine bağladınız. Test etmenin vakti geldi. Komut satırında şu kodu çalıştırın::

	python manage.py runserver

`include()` fonksiyonu diğer URL şemalarına ulaşmamıza izin verir. Django include ile karşılaştığında eşleşen URL'yi kalan işlemler için verilen URL şemasına gönderir.
