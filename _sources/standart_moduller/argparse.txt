.. meta::
   :description: Bu bölümde argparse modülünü inceleyeceğiz.
   :keywords: python, python3, argparse

===============
argparse Modülü
===============
--------
Giriş
--------

Yazdığımız her uygulama grafik arayüzüne sahip olmaz. Bazı uygulamalar komut satırına daha uygundur ve bu uygulamalar bazı parametrelere ihtiyaç duyar. argparse modülü kullanıcıdan aldığımız parametreler için yardım mesajları, nasıl kullanıldığına yönelik mesajları üretir. Ayrıca bu modül kullanıcı geçersiz parametre girerse uygun hata mesajını bastırır.

Ayrıştırıcı Oluşturmak
=======================
İlk olarak modülümüzü dahil etmemiz gerekiyor. Modülümüzü dahil ettikten sonra ayrıştırıcımız için nesne oluşturuyoruz.::

    import argparse

Ardından `ArgumentParser` üzerinden yeni bir nesne oluşturuyoruz.::

    ayristirici = argparse.ArgumentParser(description='Bu uygulama bazı işler yapıyor.')

Artık argümanlar ekleyebiliriz.

Argüman Eklemek
======================

`ArgumentParser` nesnesine gerekli tüm bilgileri verdikten sonra, `add_argument()` fonksiyonu ile argümanları ekleyebiliriz.

Örnek::

    ayristirici.add_argument('-i', '--ilk_arguman', nargs='+', required=False, help="Bu ilk argümandır")
    ayristirici.add_argument('-a', '--ikinci_arguman', required=False, help="Bu ikinci argümandır")

İki argümanımızı eklemiş olduk. Şimdi `ayristirici.print_help()` ile çıktımızı bastıralım ve inceleyelim.


**Not: Normal şartlarda argparse modülü komut satırı için uygundur ancak etkileşimli kabukta çalışırken sonuçları
görmek için argparse modülünün print_help() fonksiyonunu kullanacağız.**

Argüman Ayrıştırmak
======================

`ArgumentParser` nesnesi `parse_args()` fonksiyonu yardımıyla argümanları ayrıştırmamıza sağlar.
Etkileşimli kabuğumuza::

    ayristirici.parse_args(['-a', '7'])

yazalım ve çıktımızı inceleyelim.

Çıktımız::

    Namespace(ikinci_arguman='7')

`parse_args` fonksionuna biz '-a' parametresine vermemize rağmen ayrıştırıcımız bize argümanin ikinci ismini ve ona atadığımız değeri -7- verdi.

----------------------
ArgumentParser Nesnesi
----------------------

Temel olarak `ArgumentParser` nesnemizin yapısı::

    class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)

Yeni bir `ArgumentParser` nesnesi oluşturulduğunda alacağı tüm argümanlar anahtar kelime -keyword- olarak iletilmeli.


Argümanlar ve Açıklamaları
================================

* prog: Uygulamanın adı (varsayılan: sys.argv[0])
* usage: Uygulamanın kullanım amacını açıklayan bir metin. (varsayılan: Uygulamaya eklenen parametrelerden oluşur)
* description: Argüman yardımından önce ekrana çıkar açıklama metni (varsayılan: `None`)
* epilog: Argüman yardımından sonra ekrana çıkan açıklama metni (varsayılan: `None`)
* parents: Farklı bir ArgumentParser nesnesinin sahip olduğu argümanları dahil eder.
* formatter_class: Yardım çıktılarını kişiselleştirir.
* prefix_chars: İsteğe bağlı argümanların önüne konulan karakteri ayarlar. (varsayılan: `-`)
* fromfile_prefix_chars: Ek argümanların okunması gereken dosyayı önekleyen karakter kümesi. (varsayılan: `None`)
* argument_default: Argümanlar için global değer. (varsayılan: `None`)
* conflict_handler: Çakışan argümanlar için çözüm stratejisi. (genellikle gereksiz)
* add_help: -h / --help seçeneğini ayrıştırıcıya ekler. (varsayılan: `True`)
* allow_abbrev: Kısaltmalar net değilse uzun seçeneklerin kısaltılmasını sağlar. (Varsayılan: `None`)


prog argümanı
-----------------

`ArgumentParser` nesnesi varsayılan olarak `sys.argv[0]` çıktısını uygulama ismi olarak kullanır. Bu genellikle tercih edilen bir yöntemdir çünkü çoğu zaman uygulama ismi ile dosya ismi aynı olur.

`ilkuygulama.py` isimli bir dosya oluşturalım ve içine kodlarımızı yazalım::

    import argparse
    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', help='foo yardım')
    print(ayristirici.print_help())


Çıktımız::

    usage: ilkprogram.py [-h] [--foo FOO]

    optional arguments:
    -h, --help  show this help message and exit
    --foo FOO   foo help

Gördüğümüz gibi uygulama ismimiz ekrana çıktı ancak biz uygulamamızın ismini farklı kullanmak istiyorsak? O zaman `ArgumentParser` nesnesine `prog` parametresini uygulama ismini verelim::

    import argparse
    ayristirici = argparse.ArgumentParser(prog='Bu benim ilk uygulamam')
    ayristirici.add_argument('--foo', help='foo yardım')
    print(ayristirici.print_help())

Çıktımız::

    usage: Bu benim ilk uygulamam [-h] [--foo FOO]

    optional arguments:
    -h, --help  show this help message and exit
    --foo FOO   foo yardım

Uygulamamızın ismi değişti.



usage argümanı
-----------------

Yazdığımız uygulamaya kullanıcı için küçük bir açıklama eklemek isteyebiliriz. Bu işlem için `usage` argümanı bize yetişiyor.

Hemen kodumuzu deneyelim.::

    import argparse
    ayristirici = argparse.ArgumentParser(usage='Bu uygulama şimdilik tek parametre alıyor. ')
    ayristirici.add_argument('--parametre', help='parametre yardım')
    print(ayristirici.print_help())

Çıktımız::

    usage: Bu uygulama şimdilik tek parametre alıyor.
    optional arguments:
    -h, --help            show this help message and exit
    --parametre PARAMETRE
                            parametre yardım

Eğer biz `usage` parametresini kullanmasaydık o zaman uygulamamız varsayılan olarak tüm parametrelerin sıralı halini kullanacaktı.::

    usage: ilkprogram.py [-h] [--parametre PARAMETRE]
    optional arguments:
    -h, --help            show this help message and exit
    --parametre PARAMETRE
                            parametre yardım

description argümanı
------------------------

`description` argümanı ile uygulamamız için kısa bilgi ve nasıl çalıştığı hakkında açıklama sunar.
Yardım mesajı ve parametreler arasında açıklama sunar.

Kodumuzu yazalım::

    import argparse
    ayristirici = argparse.ArgumentParser(description='Uygulama hakkında açıklama metni')
    ayristirici.add_argument('--parametre', help='parametre yardım')
    print(ayristirici.print_help())

Çıktımız::

    usage: ilkprogram.py [-h] [--parametre PARAMETRE]

    Uygulama hakkında açıklama metni

    optional arguments:
    -h, --help            show this help message and exit
    --parametre PARAMETRE
                          parametre yardım


**Varsayılan olarak çıktımız belli bir alana sığdırılır ancak bunu değiştirmek isterseniz `formatter_class` argümanı kullanılır.**


epilog argümanı
------------------

Yazdığımız bazı uygulamalar daha fazla açıklamaya ihtiyaç duyabilir. Bunun için `epilog` parametresini kullanırız.

Örnek::

    import argparse
    ayristirici = argparse.ArgumentParser(epilog='Uygulama hakkında ikinci açıklama')
    ayristirici.add_argument('--parametre', help='parametre yardım')
    print(ayristirici.print_help())

Çıktımız::

    usage: ilkprogram.py [-h] [--parametre PARAMETRE]

    optional arguments:
    -h, --help            show this help message and exit
    --parametre PARAMETRE
                          parametre yardım

    Uygulama hakkında ikinci açıklama

**Varsayılan olarak çıktımız belli bir alana sığdırılır ancak bunu değiştirmek isterseniz `formatter_class` argümanı kullanılır.**

parents argümanı
---------------------

Bazı durumlarda, argüman ayrıştırıcılar ortak argüman kümesini paylaşabilir. Argüman tanımlarını tekrarlamak yerine ortak argümanları bir kere tanımlayarak tanımlayıp `parents` argümanı ile farklı ayrıştırıcılarda kullanabiliriz.
`parents` argümanı `ArgumentParser` nesnesi alır.
Python dosyamızı açalım ve bu kodu yazalım::

    import argparse
    ana_ayristirici = argparse.ArgumentParser(add_help=False)
    ana_ayristirici.add_argument('--ilk_arguman')
    ana_ayristirici.add_argument('--ikinci_arguman')

    ikinci_ayristirici = argparse.ArgumentParser(parents=[ana_ayristirici])
    ikinci_ayristirici.add_argument('ucuncu_arguman')
    print(ikinci_ayristirici.print_help())

Çıktımız::

    usage: ilkprogram.py [-h] [--ilk_arguman ILK_ARGUMAN]
                     [--ikinci_arguman IKINCI_ARGUMAN]
                     ucuncu_arguman
    positional arguments:
    ucuncu_arguman

    optional arguments:
      -h, --help            show this help message and exit
      --ilk_arguman ILK_ARGUMAN
      --ikinci_arguman IKINCI_ARGUMAN


`parents` argümanı ile `ana_ayristirici` mızın argümanlarını `ikinci_ayristiri` mizda kullanmış olduk.

**NOT: Ana ayrıştırıcımıza `add_help=False` eklememiz gerekir çünkü her iki ayrıştırıcımız `-h/--help` argümanına sahip olur ve bu çakışma sebebiyle uygulamamız `raise` hatası verir.**

``add_help`` argümanını kaldırıp kodumuzu çalıştıralım::

    Traceback (most recent call last):
      File "ilkprogram.py", line 7, in <module>
        ikinci_ayristirici = argparse.ArgumentParser(parents=[ana_ayristirici])
      File "/usr/lib/python3.7/argparse.py", line 1681, in __init__
        self._add_container_actions(parent)
      File "/usr/lib/python3.7/argparse.py", line 1450, in _add_container_actions
        group_map.get(action, self)._add_action(action)
      File "/usr/lib/python3.7/argparse.py", line 1580, in _add_action
        action = super(_ArgumentGroup, self)._add_action(action)
      File "/usr/lib/python3.7/argparse.py", line 1390, in _add_action
        self._check_conflict(action)
      File "/usr/lib/python3.7/argparse.py", line 1529, in _check_conflict
        conflict_handler(action, confl_optionals)
      File "/usr/lib/python3.7/argparse.py", line 1538, in _handle_conflict_error
        raise ArgumentError(action, message % conflict_string)
    argparse.ArgumentError: argument -h/--help: conflicting option strings: -h, --help


formatter_class argümanı
----------------------------

`ArgumentParser` nesnesi alternatif bir biçimlendirme sınıfı tanımlayıp, yardım mesajlarını kişiselleştirilmesine izin verir.
Şimdilik dört sınıfa sahiptir.::

  class argparse.RawDescriptionHelpFormatter
  class argparse.RawTextHelpFormatter
  class argparse.ArgumentDefaultsHelpFormatter
  class argparse.MetavarTypeHelpFormatter

`RawDescriptionHelpFormatter` ve `RawTextHelpFormatter` metinsel açıklamaların nasıl görüneceği üzerinde daha fazla kontrol sağlar.
Varsayılan olarak `ArgumentParser` nesnesi `description` ve `epilog` için satır kaydırma özelliğine sahiptir.

Kodumuzu deneyelim::

    import argparse

    ayristirici = argparse.ArgumentParser(
        description='''Uzunca bir açıklama
        yazıyoruz ve alt satıra inelim.''',
        epilog='''
                Uygulama sonu açıklama
                metnimiz.''')
    ayristirici.print_help()


Çıktımız::

    usage: ilkprogram.py [-h]

    Uzunca bir açıklama yazıyoruz ve alt satıra inelim.

    optional arguments:
      -h, --help  show this help message and exit

    Uygulama sonu açıklama metnimiz.

Görüldüğü üzere biz alt satıra inmiş olsak bile çıktımız aynı satırda görünüyor. Şimdi uygulamamıza `formatter_class` parametresine `RawDescriptionHelpFormatter` ekleyelim.
Kodumuzu bu şekilde değiştirelim::

    import argparse
    import textwrap

    ayristirici = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
        Uygulama sonu açıklama
        metnimiz. Burası ikinci satırımız.'''))
    ayristirici.print_help()

Çıktımızı inceleyelim::

    usage: ilkprogram.py [-h]

    optional arguments:
      -h, --help  show this help message and exit

    Uygulama sonu açıklama
    metnimiz. Burası ikinci satırımız.

Görüldüğü üzere yazdığımız açıklama metni ikinci satıra geçti.

RawTextHelpFormatter maintains whitespace for all sorts of help text, including argument descriptions. However, multiple
new lines are replaced with one. If you wish to preserve multiple blank lines, add spaces between the newlines.

`ArgumentDefaultsHelpFormatter` sınıfı ile argümanların varsayılan değerleri hakkında bilgi eklenebilir.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ayristirici.add_argument('--ilk_arguman', type=int, default=81, help='Bu argüman varsayılan değeri 81!')
    ayristirici.add_argument('ikinci_argüman', default=[1, 2, 3], help='İkinci argüman yardim mesajı!')
    ayristirici.print_help()

Çıktımız::

    usage: ilkprogram.py [-h] [--ilk_arguman ILK_ARGUMAN] ikinci_argüman

    positional arguments:
      ikinci_argüman        İkinci argüman yardim mesajı! (default: [1, 2, 3])

    optional arguments:
      -h, --help            show this help message and exit
      --ilk_arguman ILK_ARGUMAN
                            Bu argüman varsayılan değeri 81! (default: 81)


Çıktımıza baktığımız zaman yardım mesajlarının yanında varsayılan olarak aldığı değerleri bize gösteriyor.

`MetavarTypeHelpFormatter` sınıfı ile argümanın alacağı değerin tipini ekrana basılır.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(
        formatter_class=argparse.MetavarTypeHelpFormatter)
    ayristirici.add_argument('--a', type=int)
    ayristirici.add_argument('--ikinci_argüman', type=dict)
    ayristirici.print_help()

Çıktımız::

    usage: ilkprogram.py [-h] [--a int] [--ikinci_argüman dict]

    optional arguments:
      -h, --help            show this help message and exit
      --a int
      --ikinci_argüman dict

Çıktımıza baktığımızda hangi argümanın alacağı değer tipi argümanın yanında görünür.

prefix_chars argümanı
--------------------------

Genellikle komut satırı uygulamalrında argümanlar `-` ön ekini alır. (Örnek : `-f` / `--arguman`) Ayrıştırıcımız bazı durumlarda farklı veya ek ön eklere ihtiyaç duyabilir.
Örneğin: `+f` veya `/arguman` `ArgumentParser` nesnemizi oluştururken `prefix_chars` argümanını kullanarak bu isteğimizi sağlarız.
Örnek Kod::

    import argparse

    ayristirici = argparse.ArgumentParser(prefix_chars='-+')
    ayristirici.add_argument('+f')
    ayristirici.add_argument('++arguman')
    ayristirici.print_help()

Çıktımız::

    usage: ilkprogram.py [-h] [+f F] [++arguman ARGUMAN]

    optional arguments:
      -h, --help         show this help message and exit
      +f F
      ++arguman ARGUMAN


fromfile_prefix_chars argümanı
-----------------------------------

Bazı zamanlar örneğin uzun argüman listelerini içeren bir uygulama yazdığımız zaman, argümanları komut satırında yazmak yerine
bir dosya içerisinde tutmak daha mantıklı olur. `ArgumentParser` nesnesine `fromfile_prefix_chars` argümanı verildiği zaman
daha sonra belirtilen karakterlerden herhangi biriyle başlayan argümanlar dosya olarak kabul edilir ve içerdikleri argümanlar ile değiştirilir.
Kodumuzu yazalım::

    import argparse

    with open('args.txt', 'w') as fp:
        fp.write('-i\nbar')
    ayristirici = argparse.ArgumentParser(fromfile_prefix_chars='@')
    ayristirici.add_argument('-i')
    print(ayristirici.parse_args(['@args.txt']))


Kodumuzu satır satır inceleyelim.

    * `with open(...` satırında `args.txt` dosyasını `w` modunda açıyoruz.
    * `fp.write...` satırında `i` argümanını ekliyoruz ve `i` argümanına `bar` parametresini dosyamıza yazıyoruz.
    * Üçüncü satırımızda `ayristirici` nesnemizi oluşturuyoruz.
    * Ardından `i` argümanını ekliyoruz.
    * Bu satırda `parse_args` komutu ile argümanımızı ve alacağı değerini döndürüyoruz.

Bir dosyadan okunan argümanlar varsayılan
olarak her satırda bir tane olmalı ve komut satırındaki
orijinal dosya başvuru argümanı ile aynı yerdeymiş gibi ele alınmalıdır.
Bu nedenle  örnekte, ['@args.txt'] ifadesi ['-i', 'bar'] ifadesine eşdeğer olarak kabul edilir.

argument_default argümanı
-----------------------------

Genellikle, argüman varsayılanları, varsayılan olarak `add_argument()`
fonksiyonu veya belirli bir ad-değer çiftleri kümesiyle `set_defaults()` fonksiyonunun çağrılmasıyla belirlenir.
Ancak bazı durumlarda bağımsız değişkenler için tek bir ayrıştırıcıyı varsayılan olarak belirlemek yararlı olablir.
Örneğin `parse_args()` çağrıldığında, nitelik oluşturmayı global olarak bastırmak için `argument_default=SUPPRESS`'i kullanırız.
Örnek Kod::

    import argparse

    ayristirici = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    ayristirici.add_argument('--arguman')
    ayristirici.add_argument('-ikinci_arguman')
    print(ayristirici.parse_args(['--arguman', '1', '-ikinci_arguman', 'python']))
    print(ayristirici.parse_args([]))

Çıktımız::

    Namespace(arguman='1', ikinci_arguman='python')
    Namespace()


Çıktımıza baktığımız zaman `parse_args()` fonksiyonuna değer verildiğinde bize ad alanı (namespace) olarak argümanımızı ve aldığı değeri döndürüyor.
İlk ad alanımız istediğimiz gibi çıktıyı verdi ikincisi ise boş şimdi `argument_default=argparse.SUPPRESS`'i kaldıralım ve çıktıyı tekrar kontrol edelim.

Yeni Çıktımız::

    Namespace(arguman='1', ikinci_arguman='python')
    Namespace(arguman=None, ikinci_arguman=None)

Görüldüğü üzere ikinci çıktımız bu sefer argümanın isimlerini ve değerlerini verdi ancak değerleri olmadığı için `None` olarak döndü.

allow_abbrev argümanı
-------------------------

Normal şartlarda `parse_args()` fonksiyonuna argüman listesi verdiğiniz zaman uzun seçeneklerin kısaltmalarını kabul eder. Eğer bu özelliği devre dışı
bırakmak isterseniz `allow_abbrev=False` şeklinde kullanabilirsiniz.

Örnek Kod::

    import argparse

    ayristirici = argparse.ArgumentParser(allow_abbrev=True)
    ayristirici.add_argument('--foobar')
    ayristirici.add_argument('--foonley')
    print(ayristirici.parse_args(['--foon', 'Argüman Değeri']))

Bu kodumuzda `allow_abbrev` değeri `True` çıktımıza baktığımız zaman::

    Namespace(foobar=None, foonley='Argüman Değeri')

`parse_args()` fonksiyonuna `--foon` değeri vermemize rağmen Python devamını tamamladı ve `--foonley` argümanına değeri atadı şimdi `allow_abbrev` değerini `False` yapalım.

Çıktımız::

    usage: ilkprogram.py [-h] [--foobar FOOBAR] [--foonley FOONLEY]
    ilkprogram.py: error: unrecognized arguments: --foon Argüman Değeri


Görüldüğü üzere `ilkprogram.py: error: unrecognized arguments` hatası verdi. Bu hatanın sebebi kısaltma olarak verdiğimiz argümanı Python tanımadı.

conflict_handler argümanı
-----------------------------

`ArgumentParser` nesnesi varsayılan olarak aynı argümanların kullanımına izin vermez. Eğer aynı argümanları kullanmaya denerseniz hata verecektir.
Örnek::

    import argparse

    ayristirici= argparse.ArgumentParser()
    ayristirici.add_argument('-i', '--ilk_argüman', help='eski argümanın yardım metni')
    ayristirici.add_argument('--ilk_argüman', help='yeni argümanın yardım metni')


Çıktımız::

    Traceback (most recent call last):
    ...
        raise ArgumentError(action, message % conflict_string)
    argparse.ArgumentError: argument --ilk_argüman: conflicting option string: --ilk_argüman


İki argüman aynı olduğu için uygulamamız hata verdi.
Bazen (örneğin `parents` argümanını kullandığımız zaman) Aynı argümanların eskisini geçersiz kılmak (üstüne yazmak) kullanışlı olablir. Bu özelliği kullanmak için `conflict_handler` argümanına `resolve` değerini veriyoruz.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(conflict_handler='resolve')
    ayristirici.add_argument('-i', '--ilk_argüman', help='eski argümanın yardım metni')
    ayristirici.add_argument('--ilk_argüman', help='yeni argümanın yardım metni')

    print(ayristirici.print_help())


Çıktımız::

    usage: ilkprogram.py [-h] [-i ILK_ARGÜMAN] [--ilk_argüman ILK_ARGÜMAN]

    optional arguments:
    -h, --help            show this help message and exit
    -i ILK_ARGÜMAN        eski argümanın yardım metni
    --ilk_argüman ILK_ARGÜMAN
                            yeni argümanın yardım metni

**NOT:`ArgumentParser` nesnesi yalnızca yeni verilen argümanın üzerine yazılır. Eğer eski argüman birden farklı seçeneği varsa (`-i/--ilk_argüman` gibi) yeni eklediğiniz hangi argüman ise onun üzerine yazılır. Çıktımıza baktığımız zaman sadece `--ilk_argüman` üzerine yazıldı `-i` argümanının üzerine yazılma olmadı.**

add_help argümanı
----------------------
`ArgumentParser` nesnesi varsayılan olarak ayrıştırıcıların yardım mesajlarını sade şekilde ekrana yazdırır.
Örnek kodumuzu bir metin dosyasına yazıp ardından, terminalde dosyamızın bulunduğu dizinde terminalimizde `python3 ilkprogram.py -h` şeklinde  komutunu çalıştıralım::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('-i', help='Yardım metni')
    ayristirici.parse_args()

Çıktımız::

    usage: ilkprogram.py [-h] [-i I]

    optional arguments:
      -h, --help  show this help message and exit
      -i I        Yardım metni


Görüldüğü üzere argümanlarımız hakkında basitçe bir yardim belgesi ekrana çıktı.
Bazı durumlarda yardım metinlerini devre dışı bırakmak isteyebiliriz. Bu durumda `add_help` argümanına `False` değerini veririz.
Az önce yazdığımız kodu bu şekilde değiştirip terminalden tekrar çalıştıralım.::

    import argparse

    ayristirici = argparse.ArgumentParser(add_help=False)
    ayristirici.add_argument('-i', help='Yardım metni')
    ayristirici.parse_args()

Çıktımız::

    usage: ilkprogram.py [-i I]
    ilkprogram.py: error: unrecognized arguments: -h

Artık yardım metni yok.

**Yardım seçeneği genellikle `-h / --help`'dir. Bunun istisnası, eğer `prefix_chars` argümanı kullanılmışsa ve `-` içermezse,**
**bu durumda `-h / --help` geçerli değildir. Bu durumda, prefix_chars içindeki ilk karakter yardım seçeneklerini ön ek olarak kullanılır:**

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(prefix_chars='+/')
    ayristirici.print_help()

Çıktı::

    usage: ilkprogram.py [+h]

    optional arguments:
       +h, ++help  show this help message and exit



---------------------------
add_argument() Fonksiyonu
---------------------------
::

    ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])



Parametreler ve açıklamaları
=============================

* name veya flags: İsim veya seçenek tanımlamak için oluşturulan dizi. Örnek: `-s`, `--sil` veya `sil`.
* action: Komut satırında rastlanırsa yapılacak eylem.
* nargs: Kullanılması gereken komut satırı argümanlarının sayısı.
* const: Bazı eylem ve nargs seçeneklerinin seçimlerinin gerektirdiği sabit bir değer.
* default: Komut satırında argüman bulunmazsa varsayılan değer.
* type: Argümanın dönüştürüleceği değer türü.
* choices: Argümanlar için izin verilen değerlerin bir aralığı ayarlar.
* required: Argümanın ihmal edilip edilmeyeceği için kullanılır. (yalnızca isteğe bağlı)
* help: Argümanın yaptığı hakkında açıklama.
* metavar: Kullanım mesajlarındaki argüman için bir isim.
* dest: `parse_args()` tarafından döndürülen nesneye eklenecek niteliğin adı.

name veya flags (isim veya bayrak)
-----------------------------------

`Add_argument()` fonksiyonu , -f veya --foo gibi isteğe bağlı bir argüman mı yoksa konumsal bir argüman mı olduğunu bilmesi gerekir.
`Add_argument()` fonksiyonuna iletilen ilk argümanlar bu nedenle bir dizi bayrak veya basit bir argüman adı olmalıdır.
Örneğin isteğe bağlı argüman eklemek için::

    parser.add_argument('-f', '--foo')

Eğer konumsal argüman eklemek istersek::

    parser.add_argument('bar')

Bu şekilde ekleyebiliriz.

`Parse_args()` fobksiyonu çağrıldığında, isteğe bağlı argümanlar `-` ön eki tarafından tanımlanır ve kalan argümanların konumsal olduğu varsayılır:
Kodları yazalım.::

    import argparse

    ayristirici = argparse.ArgumentParser(prog='PROG')
    ayristirici.add_argument('-f', '--foo')
    ayristirici.add_argument('bar')
    print(ayristirici.parse_args(['BAR']))
    print(ayristirici.parse_args(['BAR', '--foo', 'FOO']))
    print(ayristirici.parse_args(['--foo', 'FOO']))

Çıktımız::

    Namespace(bar='BAR', foo=None)
    Namespace(bar='BAR', foo='FOO')
    usage: PROG [-h] [-f FOO] bar
    PROG: error: the following arguments are required: bar

Çıktımıza baktığımız zaman `bar` argümanı konumsal olduğu için ve son `parse_args()` fonksiyonunda kullanmadığımız için uygulamamız hata verdi.

action
--------

`ArgumentParser` nesnesi,argüman eylemleri ile ilişkilendirir.
Bu eylemler, kendisiyle ilişkilendirilmiş komut satırı argümanları ile hemen hemen
her şeyi yapabilir, ancak çoğu eylem yalnızca `parse_args()` fonksiyonunun döndürdüğü nesneye bir nitelik ekler.
`Action` anahtar sözcüğü argümanı, komut satırı argümanlarının nasıl ele alınması gerektiğini belirtir. Bazı sağlanan eylemler:

* `store` - Bu sadece argümanın değerini saklar. Bu varsayılan eylemdir. Örneğin::

   import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--arguman')
    print(ayristirici.parse_args('--arguman 1'.split()))

Çıktımız::

    Namespace(arguman='1')

* `store_const` - `const` anahtar sözcüğü argümanı tarafından belirtilen değeri saklar. `store_const` eylemi, genellikle bir tür bayrak belirten isteğe bağlı değişkenlerle birlikte kullanılır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--arguman', action='store_const', const=42)
    print(ayristirici.parse_args(['--arguman']))

Çıktımız::

    Namespace(arguman=42)


* `store_true` ve `store_false` - Bunlar, sırasıyla `True` ve `False` değerlerini depolamak için kullanılan `store_cost` durumlarıdır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--arguman', action='store_true')
    ayristirici.add_argument('-i', action='store_false')
    ayristirici.add_argument('-y', action='store_false')
    print(ayristirici.parse_args('--arguman -i'.split()))

Çıktımız::

    Namespace(arguman=True, i=False, y=True)

* `append` - Liste saklar ve her argüman değerini listeye ekler. Bir seçeneğin birden çok kez belirtilmesine izin vermek için kullanışlıdır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--arguman', action='append')
    print(ayristirici.parse_args('--arguman 1 --arguman 2'.split()))

Çıktımız::

    Namespace(arguman=['1', '2'])

* `append_const` - Bir listeyi depolar ve `const` anahtar sözcüğü argümanı tarafından belirtilen değeri listeye ekler. ( `const` anahtar sözcüğü argümanı varsayılan olarak `None`dır) `append_const` genellikle birden fazla argüman sabitlerini aynı listeye kaydetmesi gerektiğinde kullanışlıdır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--str', dest='types', action='append_const', const=str)
    ayristirici.add_argument('--dict', dest='types', action='append_const', const=dict)
    print(ayristirici.parse_args('--str --dict'.split()))

Çıktımız::

    Namespace(types=[<class 'str'>, <class 'dict'>])

* `count` - Anahtar kelime argümanının kullanılma sayısını sayar. Bu ayrıntı düzeylerini artırmak için kullanışlıdır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--say', '-s', action='count')
    print(ayristirici.parse_args(['-sss']))

Çıktımız::

    Namespace(say=3)

* `help` - Geçerli ayrıştırıcıdaki tüm seçenekler için eksiksiz yardım mesajı yazdırır ve sonra uygulama sonlanır.
* `version` - Sürüm bilgisi yazdırır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(prog='PROG')
    ayristirici.add_argument('--v', action='version', version='%(prog)s 2.0')
    print(ayristirici.parse_args(['--v']))

Çıktımız::

    PROG 2.0

nargs
------

`ArgumentParser` nesnesi her argümanı tek bir işlem ile ilişkilendirir. `nargs` anahtar sözcüğü bir argümanı farklı sayıda argümanı tek bir işlem ile ilişkilendirir.

* N (tam sayı) - N argümanları komut satırından bir liste halinde alınır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', nargs=3)
    ayristirici.add_argument('bar', nargs=1)
    print(ayristirici.parse_args('c --foo a b d'.split()))

Çıktımız::

    Namespace(bar=['c'], foo=['a', 'b', 'd'])

**nargs=1 bir adet liste elemanı listeler. Bu varsayılan değerden farklıdır**

* `?` Komut satırından bir argüman alınacak ve tek bir öğe olarak üretilecektir. Eğer komut satırında argüman yoksa, varsayılan değer üretilir.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', nargs='?', const='c', default='d')
    ayristirici.add_argument('-b', nargs='?', default='d')
    print(ayristirici.parse_args(['-b', '--foo', 'YY']))
    print(ayristirici.parse_args(['-b', '--foo']))
    print(ayristirici.parse_args([]))

Çıktımız::

    Namespace(b=None, foo='YY')
    Namespace(b=None, foo='c')
    Namespace(b='d', foo='d')


`nargs='?'` bir kullanım alanı daha vardır. Bu alan isteğe bağlı dosya girdi ve çıktılarıdır.
Python Etkileşimli Kabuğumuzda Kodumuzu Yazalım::

    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.parse_args(['input.txt', 'output.txt'])
    parser.parse_args([])

Çıktımız::

    Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
    Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)


* `*` - Mevcut tüm komut satırı argümanları bir liste halinde toplanır. Genel olarak `nargs='*'` ile birden fazla konumsal argüman almanın  bir anlamı olmadığını unutmayın. Ancak birden fazla isteğe bağlı argümanı `nargs='*'` ile almak mümkündür.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', nargs='*')
    ayristirici.add_argument('--bar', nargs='*')
    ayristirici.add_argument('baz', nargs='*')
    print(ayristirici.parse_args('a b --foo x y --bar 1 2'.split()))

Çıktımız::

    Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

Çıktımızı incelediğimiz zaman `baz` bizim konumsal argümanımızdır diğerleri ise isteğe bağlı argümandır. Eğer `baz` argümanından `nargs='*'` kaldırırsak::

    usage: ilkprogram.py [-h] [--foo [FOO [FOO ...]]] [--bar [BAR [BAR ...]]] baz
    ilkprogram.py: error: unrecognized arguments: b

Şeklinde hata verir.

* `+` - `*` gibi davranır. Mevcut tüm komut satırı argümanları bir liste halinde toplanır. Ayrıca, en az bir komut satırı argümanı yoksa, bir hata mesajı oluşturulur.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(prog='PROG')
    ayristirici.add_argument('foo', nargs='+')
    print(ayristirici.parse_args(['a', 'b']))
    print(ayristirici.parse_args([]))

Çıktımız::

    Namespace(foo=['a', 'b'])

    usage: PROG [-h] foo [foo ...]
    PROG: error: the following arguments are required: foo

Çıktımıza baktığımız zaman `parse_args()` fonksiyonuna liste halinde değer gönderince bize ad alanını döndürüyor. Ancak boş bir liste gönderince hata veriyor.

* `argparse.REMAINDER` - Kalan tüm komut satırı argümanları bir liste halinde toplanır. Diğer komut satırı yardımcılarını gönderilen komut satırı yardımcıları için kullanışlıdır.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(prog='PROG')
    ayristirici.add_argument('--foo')
    ayristirici.add_argument('command')
    ayristirici.add_argument('args', nargs=argparse.REMAINDER)
    print(ayristirici.parse_args('--foo B cmd --arg1 XX ZZ'.split()))

Çıktımız::

    Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')

Eğer `nargs` anahtar sözcüğü sağlanmazsa, kullanılan argümanların sayısı `action` tarafından belirlenir. Genellikle bu, tek bir komut satırı argümanının kullanılacağı ve tek bir öğenin
üretileceği anlamına gelir.

const
------

'const` argümanı komut satırından okunamayan ancak 'ArgumentParser()` için gerekli sabit değerleri tutar. En yaygın iki kullanımı vardır.

* `add_argument()` fonksiyonu `action='store_const'` veya `action='append_cost'` ile çağrıldığı zaman bu iki eylem `const` değerini `parse_args()` tarafından döndürülen nesnenin niteliklerine ekler.

* `add_argument()` fonksiyonu isteğe bağlı karakter dizisi (`-f` veya `--foo` gibi) ve `nargs='?'` ile çağrıldığı zaman sıfır veya bir komut satırı argümanı tarafından takip edilebilecek isteğe bağlı argüman oluşturur. Komut satırı argümanları ayrıştırılırken isteğe bağlı seçenek dizesi bağımsız değişken ile karşılaşmazsa `const` değeri kabul edilir.

default
--------

Tüm isteğe bağlı argümanlar ve bazı konumsal argümanlar komut satırında bazen atlanabilir. `default` anahtar sözcüğü argümanı ile eğer argüman değer almazsa varsayılan bir değer atanabilir. Varsayılan olarak `default` `None` değerine sahiptir.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', default=42)
    print(ayristirici.parse_args(['--foo', '2']))
    print(ayristirici.parse_args([]))

Çıktımız::

    Namespace(foo='2')
    Namespace(foo=42)

İlk `parse_args()` fonksiyonunda değer atadığımız için `foo` argümanının yeni değeri `'2'` oluyor ancak ikinci `parse_args()` fonksiyonunda değer olmadığı için varsayılan değerimiz `42` ekrana çıkıyor.
`default` değeri karakter dizisi (string) ise ayrıştırıcı değeri argüman gibi ayırır. Eğer değerin tipi değiştirilmek istenirse `type` kullanılır.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', default=42, type=int)
    print(ayristirici.parse_args(['--foo', '2']))
    print(ayristirici.parse_args([]))

Çıktımız::


    Namespace(foo=2)
    Namespace(foo=42)

Görüldüğü üzere ilk değerimiz karakter dizisi yerine artık tam sayı (int) oldu.

type
------

`ArgumentParser()` nesnesi varsayılan olarak komut satırından okuduğu değerleri karakter dizisi (string) olarak alır. Bazı durumlarda farklı tiplerde değişkenlere ihtiyaç duyarız. Bunun için `type` kullanılır.
Şimdi uygulamamızı çalıştırdığımız dizine `args.txt` dosyası oluşturalım ve kodumuzu çalıştıralım.
Kod::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici .add_argument('foo', type=int)
    ayristirici .add_argument('bar', type=open)
    print(ayristirici .parse_args('2 args.txt'.split()))

Çıktımız::

    Namespace(bar=<_io.TextIOWrapper name='args.txt' mode='r' encoding='UTF-8'>, foo=2)

Çıktıya baktığımız zaman `bar` argümanının dosya hakkında bilgiler içeren bir takım detaylar var ve `foo` ise tam sayı değerine sahip.

choices
--------

Bazen argümanlar belirli değerler ile sınırlandırmak gerekir. Bu durumda `choices` kullanılır. Eğer kullanıcı geçerli argüman verdiyse uygulama devam edeğer ancak
verilen argüman geçersiz ise hata mesajı döner.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('oyun', choices=['tas', 'kagit', 'makas'])
    print(ayristirici.parse_args(['kagit']))
    print(ayristirici.parse_args(['ates']))


Çıktı::

    Namespace(oyun='kagit')
    usage: ilkprogram.py [-h] {tas,kagit,makas}
    ilkprogram.py: error: argument oyun: invalid choice: 'ates' (choose from 'tas', 'kagit', 'makas')

Çıktımıza baktığımız zaman ilk argümanımız geçerli olduğu için bir hata almadık. Ancak ikinci argümanımız geçersiz olduğundan dolayı uygulamamız bize geçerli argümanlar arasında seçim yapmamızı söylüyor.

`required`
-----------

`argparse` modülü genellikle `-f` veya `--foo` gibi isteğe bağlı seçimler ile çalışır ancak bazı durumlarda zorunlu argümanlar vermek gerekebilir. Böyle durumlarda `required=True` kullanılır.

Örnek Kod::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', required=True)
    print(ayristirici.parse_args(['--foo', 'Degisken']))
    print(ayristirici.parse_args([]))

Çıktımız::

    Namespace(foo='Degisken')
    usage: ilkprogram.py [-h] --foo FOO
    ilkprogram.py: error: the following arguments are required: --foo


Çıktımızı incelediğimiz zaman bir değişken atadığımız için uygulama hatasız çalıştı ancak ikincisinde değişken olmadığı için hata verdi.

**NOT:Zorunlu seçimler genellikle kötü form olarak kabul edilir. Çünkü bu parametreler özünde isteğe bağlıdır ve kullanıcılar isteğe bağlı olmasını ister. Mümkün olduğunca kullanmamak gerekir.**

help
-----
`help` değeri karakter dizisi olarak değer alır ve bu değer argümanlar hakkında yardım metinleri içerir. Kullanıcı yardım istediğinde bulununca (genellikle `-h` veya `--help`) yardım metinleri görünür.

Örnek Kod::

    import argparse

    ayristirici= argparse.ArgumentParser()
    ayristirici.add_argument('--foo', help='foo için yardım metni')
    ayristirici.add_argument('bar', help='bar için yardım metni')
    print(ayristirici.parse_args(['-h']))

Çıktımız::

    usage: ilkprogram.py [-h] [--foo FOO] bar

    positional arguments:
      bar         bar için yardım metni

    optional arguments:
      -h, --help  show this help message and exit
      --foo FOO   foo için yardım metni


`help` çeşitli formatlama yöntemlerini içerir. Bu sayede değerlerinizi farklı yerlerde kullanabilirsiniz.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser(prog='merhaba dünya')
    ayristirici.add_argument('bar', default=42,
                             help='bar argümanı için yardım metni ayrıca bu uygulamannın adı: %(prog)s (varsayılan değeri: %('
                                  'default)s)')
    print(ayristirici.print_help())

Çıktımız::

    usage: merhaba dünya [-h] bar

    positional arguments:
      bar          bar argümanı için yardım metni ayrıca bu uygulamannın adı:
                  merhaba dünya (varsayılan değeri: 42)

    optional arguments:
      -h, --help  show this help message and exit

Görüldüğü üzere uygulamamızın adı ve varsayılan değerimiz ekrana basıldı.

metavar
--------
`ArgumentParser()` nesnesi yardım metinlerini oluşturduğu zaman, beklenen her argümana atıfta bulunmak için bir yola ihtiyaç duyar. Varsayılan olarak `ArgumentParser()` nesnesi `dest` değerini her nesnenin "ismi" olarak kullanır.
Varsayılan olarak, konumsal argüman eylemleri için `dest` değeri doğrudan kullanılır ve isteğe bağlı argüman eylemleri için `dest` değeri büyük harfe dönüştürülür.
Örnek Kod::

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo')
    parser.add_argument('bar')
    print(parser.parse_args('X --foo Y'.split()))
    print(parser.print_help())

Çıktımız::

    Namespace(bar='X', foo='Y')
    usage: ilkprogram.py [-h] [--foo FOO] bar

    positional arguments:
      bar

    optional arguments:
      -h, --help  show this help message and exit
    --foo FOO

Ayrıca `metavar` alternatif isim belirtebilir.

Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', metavar='YYY')
    ayristirici.add_argument('bar', metavar='XXX')
    print(ayristirici.print_help())

Çıktımız::

    usage: ilkprogram.py [-h] [--foo YYY] XXX

    positional arguments:
      XXX

    optional arguments:
      -h, --help  show this help message and exit
      --foo YYY

Konumsal argümanımızın ismi `metavar` ile değişti.

**NOT:`metavar` yalnızca ekran ismini değiştirir, `parse_args()` ile kontrol ettiğiniz zaman `dest` değerini kullandığını görebilirsiniz.**

dest
-----

`dest` ile argümanlara kişiselleştirilmiş isimler verebilirsiniz.
Örnek::

    import argparse

    ayristirici = argparse.ArgumentParser()
    ayristirici.add_argument('--foo', dest='bar')
    print(ayristirici.parse_args('--foo XXX'.split()))

Çıktımız::

    Namespace(bar='XXX')

Bu yardım sayfası https://docs.python.org/3/library/argparse.html referans alınarak hazırlanmıştır.
