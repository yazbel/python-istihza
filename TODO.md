# Belgelerdeki hatalar

* [`input.rst`](sphinx_source/input.rst) dosyasındaki `Dolayısıyla ``input()`` fonksiyonuyla gelen
karakter dizisini bir sayıyla çarpmaya kalkarsak hata alıyoruz.` bölümü düzeltilmeli.

* [``dosyalarin_metot_ve_nitelikleri.rst``](sphinx_source/dosyalarin_metot_ve_nitelikleri.rst) dosyasındaki `f.seek(f.tell())` koduna ihtiyaç duyulmasının sebebi [CPython'daki bir bug](https://stackoverflow.com/questions/34879318/why-isnt-truncate-defaulting-properly-to-the-current-position-for-files). Bunun belirtilmesi ve konunun doğru anlatılması lazım.


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
