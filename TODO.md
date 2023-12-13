# Belgelerdeki hatalar

* [`input.rst`](source/input.rst) dosyasındaki `Dolayısıyla ``input()`` fonksiyonuyla gelen
karakter dizisini bir sayıyla çarpmaya kalkarsak hata alıyoruz.` bölümü düzeltilmeli.

* [``dosyalarin_metot_ve_nitelikleri.rst``](source/dosyalarin_metot_ve_nitelikleri.rst) dosyasındaki `f.seek(f.tell())` koduna ihtiyaç duyulmasının sebebi [CPython'daki bir bug](https://stackoverflow.com/questions/34879318/why-isnt-truncate-defaulting-properly-to-the-current-position-for-files). Bunun belirtilmesi ve konunun doğru anlatılması lazım.

* https://python-istihza.yazbel.com/ikili_dosyalar.html dosyasındaki `if data[6:11] in [b"JFIF", b"Exif"]:` kısmına bakılmalı.


# Belgelerdeki eksikler

* Bezeyiciler (decorator) konusunun anlatımı.
* Üreteçler (generators) konusunda daha çok örnek.
* Magic metodlar, diğer bir deyişle dunder metodlar eklenmeli.
* ``Ellipsis`` nesnesi hakkında özet bir anlatım.
* Fonksiyonel programlama örnekleri ve `itertools` modülünün anlatımı.
* `logging` modülünün anlatımı.
* Asenkron programlama.
* Kayan noktalı sayıların (`float`), rasyonel sayıları temsil etmedeki yetersizliğinin ve `decimal` gibi kütüphanelerin anlatımı.
* Basit bir expression parser örneği. Pratt parser kullanılabilir.
* `socket` modülünün anlatımı.
* Metasınıfların anlatımı.
* DataClass'ların anlatımı.


# Belgelerin İnşası

* build klasörünü silip github actions ile inşanın /docs klasörüne değil ayrı bir branch'ın root'una yapılmasını sağlamak.
* Template klasöründeki scriptlerin gözden geçirilip yenilenmesi lazım