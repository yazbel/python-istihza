.. meta::
   :description: Bu bölümde django ile site yapmaya baþlayacaðýz.
   :keywords: python, django, çeviri
   
.. highlight:: python3

*****************************************
ÝLK DJANGO PROJENÝ YAZ, part 1
*****************************************

**Kaynak Kodu:** https://docs.djangoproject.com/en/2.0/intro/tutorial01/

Bir örnekle öðrenmeye baþlayalým. Bu örnekte basit bir anket uygulamasý oluþturacaðýz.
Uygulama iki kýsýmdan oluþacak:

	#. Anketlerin oylanmasý için herkese açýk bir site 
	#. Anketleri düzenlemek veya ekleyip silmek için bir admin paneli

Senin Djangoyu yüklediðini varsayýyoruz. Komut isteminde aþaðýdaki komutu çalýþtýrarak Djangonun yüklü olup olmadýðýna ve Django sürümüne ulaþabilirsin::

	python -m django --version

Eðer Django yüklüyse yüklü olan versiyonu görmelisin. Eðer deðilse "No module named django" yazýsý ile karþýlaþmalýsýn.

Bir proje oluþtur
==================

Komut satýrýnda cd komutuyla komutunuzu saklamak istediðiniz dizine gidin ve aþaðýdaki kodu çalýþtýrýn::

	django-admin startproject mysite

Bu kod bulunduðunuz dizinde mysite dizinini yaratacak.
Þimdi `startproject` komutunun oluþturduklarýna bakalým::

	mysite/
	    manage.py
	    mysite/
	        __init__.py
	        settings.py
	        urls.py
	        wsgi.py

En dýþardaki `mysite/` dizini, projeniz için sadece bir kapsayýcýdýr. Adý Django için önemli deðil. Beðendiðiniz herhangi bir þeye yeniden adlandýrabilirsiniz.
`manage.py`: Komut satýrýndan django projesiyle etkileþime geçmenizi saðlayan bir programdýr.
Ýçerideki `mysite/` dizini , projeniz için gerçek bir python paketidir.
`mysite/init.py`: Boþ bir python dosyasýdýr. mysite/ dizininin python paketi olmasýný saðlar.
`mysite/setting.py`: Django projesinin ayarlarý ile ilgili bir dosya.
`mysite/urls.py`: Projeniz için URL'leri barýndýran dosya.
`mysite/wsgi.py`: WSGI uyumlu web sunucularý için projenize hizmet edecek bir giriþ noktasý.

Geliþtirme sunucusu
====================

Þimdi django projemizin çalýþýp çalýþmadýðýný kontrol edelim. Komut satýrýnda dýþarýdaki `mysite` dizinine gidin ve aþaðýdaki kodu çalýþtýrýn::

	python manage.py runserver

Çýktý olarak þunu görmelisin::

	Performing system checks...

	System check identified no issues (0 silenced).

	You have unapplied migrations; your app may not work properly until they are applied.
	Run 'python manage.py migrate' to apply them.

	April 29, 2018 - 15:50:53
	Django version 2.0, using settings 'mysite.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

.. Note:: Veritabanýyla ilgili uyarýyý dikkate almayýn.

Django geliþtirme sunucusunu baþlattýnýz.

Kullanýlan portu deðiþtirme
============================

`runserver` komutu geliþtirme sunucusu için standart olarak 8000 portunu kullanýr. 
Eðer bu portu deðiþtirmek isterseniz bunu komuta argüman olarak verin. Mesela aþaðýdaki komut 8080 portunda geliþtirme sunucusunu çalýþtýrýyor::

	python manage.py  runserver 8080

Eðer sunucunun IP adresini deðiþtirmek isterseniz port ile birlikte belirtin. Örnek olarak kullanýlabilir tüm IP'leri dinlemek istiyorsanýz þu kodu çalýþtýrýn::

	python manage.py runserver 0:8000

Yukarýda yazdýðýmýz kodda 0'ýn anlamý 0.0.0.0 (Yani bir kýsaltma).

Bir anket uygulamasý oluþturalým
=================================

Artýk proje ortamýmýz kuruldu. Çalýþmaya baþlayabiliriz.
Django'da yazdýðýmýz her uygulama bir python paketinden oluþur ve Django'da uygulamanýn dizini otomatik olarak oluþturulur. Bu sayede dizin oluþturmakla uðraþacaðýmýz zamanda kod yazabiliriz.
Bir uygulama oluþturmak için komut satýrýnda `manage.py` ile ayný dizine gelin ve þu komutu yazýn::

	python manage.py startapp polls

`polls` isimli bir dizin oluþturulacak. Bakaklým içinde neler var::
	
	polls/
	    __init__.py
	    admin.py
	    apps.py
	    migrations/
	        __init__.py
	    models.py
	    tests.py
	    views.py

Bu dizin anket uygulamamýzýn merkezi olacak.

Ýlk view'ýmýzý yazalým
=======================

Hadi yazmaya baþlayalým. Þimdi `polls/views.py` açýn ve þu kodlarý yazýn::

	from django.http import HttpResponse
	def index(request):
	    return HttpResponse("Hello, world. You're at the polls index.")

Bu Django'da yazýlabilecek en basit view. Artýk bu view ý çaðýrabilmek için bir URL haritasýna ihtiyacýmýz var ve URL haritasý için de URL þemasýna.
polls dizininde `urls.py` isimli bir dosya oluþturarak uygulamanýn URL þemasýný da oluþturmuþ oluruz.(Dosya Gezgininden kendiniz urls.py isimli bir python modülü oluþturun.)  Uygulama dizini son olarak þöyle görünmeli::

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

Þimdi de yeni oluþturduðumuz polls dizinindeki urls.py dosyasýnda þu kodlar yazýlý olmalý::

	from django.urls import path
	from . import views

	urlpatterns = [
	    path('', views.index, name='index'),
	]

Burada oluþturduðumuz URL þemasýný gerçek Url þemasýnda tanýtmanýn vakti geldi. Bunun için mysite dizinindeki urls.py dosyasýnda include fonksiyonunu içe aktarýp  url listesini aktarmada kullanacaðýz. Sonuç olarak mysite dizinindeki urls.py dosyanýz þu hale gelmeli::

	from django.contrib import admin
	from django.urls import include, path
	
	urlpatterns = [
	    path('polls/', include('polls.urls')),
	    path('admin/', admin.site.urls),
	]

Artýk index view'ýný bir dizine baðladýnýz. Test etmenin vakti geldi. Komut satýrýnda þu kodu çalýþtýrýn::

	python manage.py runserver

`include()` fonksiyonu diðer URL þemalarýna ulaþmamýza izin verir. Django include ile karþýlaþtýðýnda eþleþen URL'yi kalan iþlemler için verilen URL þemasýna gönderir.