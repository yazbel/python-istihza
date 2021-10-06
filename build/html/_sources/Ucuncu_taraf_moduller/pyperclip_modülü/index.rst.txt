****************
Pyperclip Modülü
****************

Bu modül pano işlemleri ile alakalıdır. Kopyala-yapıştır gibi işlemleri yapmamızı sağlar.

Kurulum
=======

Bu modülü kurmak için komut satırına aşağıdaki kodları vermelisiniz:

	pip install pyperclip

Modül kurulumunda bir hata ile karşılaşırsanız forum.yazbel.com’dan destek alabilirsiniz.


Kullanım
========

copy
--------

Bu fonksiyon panoya veri kopyalamanızı sağlar. Aldığı tek argüman kopyalanacak veridir.

Örnekler:

.. code-block:: python


	from pyperclip import copy
	copy("Bu veri panoya kopyalanacak veridir.")

copy fonksiyonunu çalıştırdıktan sonra metnimiz panoya kopyalanmış olacak. Dilerseniz test edebilirsiniz.

paste
---------

Bu fonksiyon o anda panodaki veriyi almamızı sağlar. Fonskiyon panodaki veriyi döndürür.

.. code-block:: python


	from pyperclip import paste
	result = paste()
	print(result)

Gördüğünüz kodlar o anda panoda bulunan veriyi ekrana yazdıracaktır.. Eğer panoda veri yoksa boş karakter dizisi döndürülür.

waitForPaste
----------------

Panoda veri varsa veriyi döndürür, eğer yoksa panoya veri gelene kadar bekler, geldiğinde döndürür.

.. code-block:: python


	from pyperclip import waitForPaste
	print("Panoda veri varsa ekrana yazdirilacak, yoksa gelene kadar beklenecek.")
	result = waitForPaste()
	print(result)

waitForNewPaste
----------------------

Bu fonksiyon da yukarıdakine benzer. O an panoda veri varsa bile, yeni veri gelene kadar bekler. Panodaki veride bir değişiklik olduğu an yeni veri döndürülür.

.. code-block:: python


	from pyperclip import waitForNewPaste
	print("Panoya yeni veri geldigi an ekrana yazdirilacak.")
	result = waitForNewPaste()
	print(result)


NotImplementedError Hatası
=============================

Eğer GNU/Linux dağıtımlarından birini kullanıyorsanız, modülümüzü kullanırken NotImplementedError hatası alabilirsiniz. Bu sorunu çözmek için aşağıdaki yöntemlerden sadece bir tanesini uygulamanız yeterlidir.


1. Yöntem
----------

xsel aracını kurabilirsiniz. Eğer Debian tabanlı bir dağıtım kullanıyorsanız;


.. code-block::


	sudo apt-get install xsel


Eğer Fedora kullanıyorsanız;


.. code-block::


	sudo dnf install xsel



2. Yöntem
----------

xclip aracını kurabilirsiniz. Eğer Debian tabanlı bir dağıtım kullanıyorsanız;


.. code-block::


	sudo apt-get install xclip


Eğer Fedora kullanıyorsanız;


.. code-block::


	sudo dnf install xcode



3. Yöntem
----------

Sisteminize Gtk kurabilirsiniz:

.. code-block::


	pip install Gtk

4. Yöntem
----------

Sisteminize PyQt4 kurabilirsiniz.

.. code-block::


	pip install PyQt4