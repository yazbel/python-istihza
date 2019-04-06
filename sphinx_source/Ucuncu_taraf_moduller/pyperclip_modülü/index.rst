****************
Pyperclip Modülü
****************

Bu modül pano işlemleri ile alakalıdır. Kopyala-yapıştır gibi işlemleri yapmamızı sağlar.

Kurulum
=======

Bu modülü kurmak için komut satırına aşağıdaki kodları vermelisiniz:

	pip install pyperclip

Modül kurulumunda bir hata ile karşılaşırsanız forum.yazbel.com’dan destek alabilirsiniz.

.. note:: Eğer GNU/Linux'te kurulum aşamasında "İşletim sisteminiz x-copy özelliğini desteklemiyor." uyarısı alırsanız uyarıdan sonraki talimatları uygulayarak bu sorunu aşabilirsiniz. 

Kullanım
========

Bu modülün kullanımı çok basittir. Örneklerle başlayalım:

.. code-block:: python

	from pyperclip import copy, paste
	copy(“Pyperclip”)
	paste()
	‘Pyperclip’

Gördüğünüz üzere pek bir detay yok. copy() ile panoya kopyalayın, paste() ile panodaki veriyi alın. 


