.. meta::
   :description: Bu bölümde timeit modülünü inceleyeceğiz.
   :keywords: python, modül, import, timeit

*************
timeit Modülü
*************

**Kaynak Kodu:** https://github.com/python/cpython/blob/3.5/Lib/timeit.py
**Belge Kaynağı:** https://docs.python.org/3.5/library/timeit.html

Bu modül küçük kod parçalarının çalışma sürelerini ölçmeyi sağlar. Hem komut satırı arayüzüne hem de çağrılabilir bir arayüze sahiptir. Çalışma sürelerini ölçmek için birçok ortak tuzaktan kaçınır. Tim Peters'in O'Reilly tarafından yayımlanan Python Cookbook kitabının "Algoritmalar" bölümünün girişine de göz atın.

Temel Örnekler
==============

Takip eden örnek, komut satırı arayüzünün üç değişik deyimi nasıl karşılaştırdığını gösteriyor::

    python3 -m timeit '"-".join(str(n) for n in range(100))'
    10000 loops, best of 3: 29 usec per loop

    python3 -m timeit '"-".join([str(n) for n in range(100)])'
    10000 loops, best of 3: 25.3 usec per loop

    python3 -m timeit '"-".join(map(str, range(100)))'
    10000 loops, best of 3: 20 usec per loop

Bu, Python arayüzünden şu kodlarla gerçekleştirilebilir::

    import timeit

    timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    0.30339929000001575

    timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    0.2637243290000697

    timeit.timeit('"-".join(map(str, range(100)))', number=10000)
    0.2151021940001101

timeit sadece komut satırı arayüzü kullanıldığında yineleme sayısını otomatik olarak belirleyecektir. Örnekler bölümünde gelişmiş örnekler bulabilirsiniz.

Python Arayüzü
===============

Modül, üç kolaylık fonksiyonu ve bir topluluk sınıfı tanımlar:

**timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)**

    Verili ifadeyle, kurulum koduyla ve timer fonksiyonuyla bir Timer örneği oluşturun ve onun 	`timeit()` yöntemini çalıştırma sayıları ile çalıştırın. İsteğe bağlı globals bağımsız değişkeni, kodun çalıştırılacağı ad alanını belirtir.

    Sürüm 3.5'de değiştirildi: İsteğe bağlı globals bağımsız değişkeni eklendi.

**timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000, globals=None)**

    Verili ifadeyle, kurulum koduyla ve timer fonksiyonuyla bir Timer örneği oluşturun ve onun 	`repeat()` yöntemini tekrarlanma sayısı ve çalıştırma sayıları ile çalıştırın.  İsteğe bağlı globals bağımsız değişkeni, kodun çalıştırılacağı ad alanını belirtir.

    Sürüm 3.5'de değiştirildi: İsteğe bağlı globals bağımsız değişkeni eklendi.

**timeit.default_timer()**

    Her zaman `time.perf_counter()` olan varsayılan zamanlayıcı

    Sürüm 3.3'de değiştirildi: Şimdi varsayılan sayıcı `time.perf_counter()`

**class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)**

    Küçük kod parçalarının çalışma hızının zamanlaması için sınıf.

    Yapıcı; zamanlamanın yapılması için bir ifade, kurulum için fazladan bir ifade ve zamanlama fonksiyonu alır. Her ifadenin varsayılan değeri `pass` olur; timer fonksiyonu platforma bağımlıdır (`docstring` modülüne bakınız). Ayrıca *stmt* ve *setup*, birbirlerinden ';' işareti ile ayrılan çok sayıda ifadeyi içerebilir veya çok satır başı olan dizi değişkenlerini içermedikçe yeni satırları içerebilir.  Deyim 	varsayılan olarak timeit'in ad alanında yürütülecektir; bu davranış, global alana bir isim alanı geçirerek kontrol edilebilir.

    Birinci ifadenin çalışma hızını ölçmek için `timeit()` yöntemini kullanın. `repeat()`, `timeit()` yöntemini bir çok kez çağırmak ve sonuç listesini geri döndürmek için bir kolaylıktır. *setup* parametresinin çalışma zamanı, bütün çalışma zamanından hariç tutulmuştur.

    *stmt* ve *setup* parametreleri argümansız çağrılabilen nesneler alabilir. Bu, çağrıları, sonradan 	`timeit()` fonksiyonuyla çalıştırılacak şekilde, timer fonksiyonunun içine gömer. Bu durumda ilave fonksiyon çağrıları nedeniyle zamanlama yükünün biraz daha fazla olacağını unutmayın.

    Sürüm 3.5'de değiştirildi: İsteğe bağlı olarak globals parametresi eklendi.

    **timeit(number=1000000)**

        Ana ifadenin zaman sayısıyla ilgili çalışmaları. Bu, bir kez setup ifadesini çalıştırır ve sonra ana ifadeyi birkaç kez çalıştırmak için, float tipinde saniyelerle ölçülen zamanı geri döndürür. Döngünün kaç kez tekrar edileceğini argüman belirler, varsayılan değeri bir milyondur. Ana ifade, setup ifadesi ve timer fonksiyonu yapıcıya geçirilmek için kullanılırlar.

        **Not:** Varsayılan olarak, `timeit()` fonksiyonu zamanlama süresince *garbage collection*'u etkisiz bırakır. Bu yaklaşımın avantajı, bağımsız zamanlamaları daha çok karşılaştırılabilir yapmaktır. Dezavantajı ise, garbage collection (çöp toplayıcısı), ölçüm esnasında fonksiyonun performansının önemli bir parçası olabilir. Böylece garbage collection (çöp toplayıcısı) *setup* değişkeninin (stringinin) ilk ifadesi olarak yeniden aktif edilebilir. Örneğin::

            timeit.Timer("for i in range(10): oct(i)", "gc.enable()").timeit()

    **repeat(repeat=3, number=1000000)**

	`timeit()`'i bir kaç kez çağırır.

	Bu `timeit()`'i tekrar çağıran, sonuçları listeleyen bir kolaylık fonksiyonudur. Birinci argüman `timeit()`'in kaç kez çağrılacağını belirler. İkinci parametre ise `timeit()`'in argümanıdır.

	**Not:** Sonuç vektörlerinden alınan değerlerin aritmetik ortalamasını ve standart sapmasını rapor olarak sunmada cazip bir yöntemdir. Ancak bu çok kullanışlı değildir. Tipik bir durumda, en küçük değer, makinenin verili kod parçasını ne kadar hızlı şekilde çalıştırdığına dair zayıf bir göstergedir; sonuç vektörleri içindeki yüksek değerler Python'ın hızının değişkenliğinden kaynaklanmaz, ancak diğer işlemlerin 	tutarlı zamanlama çalışmasına karışmasından kaynaklanır. Yani en düşük değer sizin ilgilenmeniz gereken tek değer olabilir. Ondan sonra, bütün vektöre bakıp istatistik yerine sağ duyuya başvurabilirsiniz.

    **print_exc(file=name)**

        Zamanlama kodunun geri izini bastırmaya yardımcı olur.

	Tipik kullanım::

	    t = Timer(...)		#try/except bloğunun dışında
	    try:
                t.timeit(...)		# ya da t.repeat(...)
	    except Exception:
		t.print_exc()

	Standart geri izinin avantajı, derlenen şablondaki kaynak çizgilerinin görüntülenecek olmasıdır. İsteğe bağlı *file* argümanı geri izinin nereye gönderileceğini belirler, varsayılan değeri `sys.stderr`'dir.

Komut Satırı Arayüzü
=====================

Bir program olarak komut satırı arayüzünden çağrılırken şu yapı kullanılır::

    python -m timeit [-n N] [-r N] [-u U] [-s S] [-t] [-c] [-h] [statement ...]

Takip eden seçenekler::

    -n N, --number=N

	İfadenin kaç kez çalıştırılacağını belirler.

    -r N, --repeat=N

	timer'ın kaç kez tekrar edileceğini (varsayılan değeri 3) belirler.

    -s S, --setup=S

	Bir kez ilksel olarak çalıştırılacak ifadeyi (varsayılan değeri `pass`) belirler.

    -p, --process

	Duvar saati zamanını değil de, işlem zamanını ölçer. Varsayılan değeri `time.perf_counter()` yerine `time.process_time()`'dir.

	Sürüm 3.3'de gelmiş yeni bir özellik.

    -t, --time

	(onaylanmamış) `time.time()`'ı kullanır.

    -u, --unit=U

	Zamanlayıcı çıktısının zaman birimini belirler; usec, msec veya sec birimleri seçilebilir.

	Sürüm 3.5'de gelmiş yeni bir özellik.

    -c, --clock

	(onaylanmamış) `time.clock()`'u kullanır.

    -v --verbose

	Ham zamanlama sonuçlarını bastırır, daha fazla basamak kesinliği için tekrarlar.

    -h -help

	Kısa bir kullanım mesajı bastırır ve sonlanır.

Çok satırlı ifadeler, her bir satırı ayrı bir ifade argümanı olacak şekilde verilebilir; girintili çizgiler, bir argümanın tırnak işaretleri içine alınarak ve önde gelen boşluklarla kullanılabilir.

Şayet *-n* değeri girilmezse, uygun döngü sayısı, toplam süre 0.2 saniye olana kadar onun üstleri olacak şekilde hesaplanır.

`default_timer()` ölçümleri makinede çalışan diğer programlar tarafından etkilenebilir, bu yüzden hassas ölçüm yapmak gerektiğinde en iyisi, zamanlamayı bir kaç kez tekrar etmek ve en uygun zamanı seçmektir. *-r* seçeneği bu işlem için uygundur; varsayılan üç yineleme sayısı bir çok durumda yeterlidir. CPU süresini ölçmek için `time.process_time()`'ı kullanabilirsiniz.

**Not:** Bir geçiş ifadesi çalıştırmakla ilgili belirli bir temel yük vardır. Buradaki kod bunu gizlemeye çalışmaz fakat siz bunun farkında olmalısınız. Temel yük, programı argümansız çağırarak ölçülebilir ve Python sürümleri arasında farklılıklar gösterir.

Örnekler
========

Sadece başlangıçta bir kez çalıştırılmak üzere bir setup (kurulum) ifadesi kullanılabilir::

    python -m timeit -s 'text = "sample string"; char="g"' 'char in text'
    10000000 loops, best of 3: 0.0482 usec per loop

    python -m timeit -s 'text = "sample string"; char="g"' 'text.find(char)'
    10000000 loops, best of 3: 0.178 usec per loop

Python arayüzü için::

    import timeit

    timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
    0.048954748002870474

    timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
    0.2300617519977095

Aynı işlem timer() sınıfını ve metotlarını kullanarak da yapılabilir::

    import timeit

    t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
    t.timeit()
    0.049284196000371594
    t.repeat()
    [0.051710191000893246, 0.04452369999853545, 0.04527571799917496]

Sonraki örnekler çok satırlı ifadelerin zaman ölçümünün nasıl yapılacağını gösterir. Aşağıdaki örnekte, `hasattr()` ve `try/except`'in maliyeti, nesne özelliklerinin nasıl kaybedilip ortaya konduğunu test etmek için karşılaştırılmıştır::

    python -m timeit 'try:' '  str.__bool__' 'except AttributeError:' '  pass'
    1000000 loops, best of 3: 0.99 usec per loop

    python -m timeit 'if hasattr(str, "__bool__"): pass'
    1000000 loops, best of 3: 0.476 usec per loop

    python -m timeit 'try:' '  int.__bool__' 'except AttributeError:' '  pass'
    1000000 loops, best of 3: 0.966 usec per loop

    python -m timeit 'if hasattr(int, "__bool__"): pass'
    1000000 loops, best of 3: 0.479 usec per loop

Python arayüzü için::

    import timeit

    # özellik kayıp
    s = """\
    try:
        str.__bool__
    except AttributeError:
        pass
    """

    timeit.timeit(stmt=s, number=100000)
    0.08558237599936547

    s = "if hasattr(str, '__bool__'): pass"
    timeit.timeit(stmt=s, number=100000)
    0.0541383109994058

    # özellik mevcut
    s = """\
    try:
        int.__bool__
    except AttributeError:
        pass
    """

    timeit.timeit(stmt=s, number=100000)
    0.011753970000427216

    s = "if hasattr(int, '__bool__'): pass"
    timeit.timeit(stmt=s, number=100000)
    0.016129147999890847


`timeit()`'i tanımladığınız fonksiyonda kullanmak için önemli bir ifade içeren bir setup parametresi geçirebilirsiniz::

    def test():
        """Test fonksiyonu"""
        L = [i for i in range(100)]

    if __name__ == '__main__':
        import timeit
        print(timeit.timeit("test()", setup="from __main__ import test"))
        4.163065000997449

Bir diğer seçenek şimdiki global ad alanı içerisinde çalıştırılacak `globals()`'i genel alan parametrelerine geçirmektir. Bu bireysel olarak içe aktarmaları belirtmeye göre daha kolaydır::

    def f(x):
        return x**2

    def g(x):
        return x**4

    def h(x):
        return x**8

    import timeit
    print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
    1.632076413003233

*timeit*'i kullanarak benzer işlemleri yapan kodlardan hangisinin daha performanslı olduğunu görebilirsiniz::

    python -m timeit '"a" + "b"'
    100000000 loops, best of 3: 0.0183 usec per loop

    python -m timeit '"{}.{}".format("a", "b")'
    1000000 loops, best of 3: 0.215 usec per loop

    python -m timeit '"%s%s" %("a", "b")'
    10000000 loops, best of 3: 0.117 usec per loop

    python -m timeit '"".join(("a", "b"))'
    10000000 loops, best of 3: 0.109 usec per loop

Python arayüzü için::

    import timeit

    timeit.timeit('"a" + "b"', number=1000000)
    0.018340642998737167

    timeit.timeit('"{}{}".format("a", "b")', number=1000000)
    0.3770097929991607

    timeit.timeit('"%s%s" %("a", "b")', number=1000000)
    0.2078534940010286

    timeit.timeit('"".join(("a", "b"))', number=1000000)
    0.1585119779992965





