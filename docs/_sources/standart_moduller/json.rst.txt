.. meta::
    :description: Bu bölümde JSON modülünün fonksiyonları anlatılıyor.
    :keywords: JSON
.. highlight:: py3

***********
json Modülü
***********

JSON farklı diller arasında iletişimi sağlamak için geliştirilmiş
basit bir veri formatıdır. Bu veri formatı Python'daki sözlük ve
listelere çok benzer. İki tür kullanımı vardır. Birincisi anahtar-değer mantıyla çalışır.
::

    {
        "Ad": "Fırat",
        "Soyad": "Özgül"
    }

JSON ifadelerinde her öğe arasında virgül olmalıdır. Anahtar ve değer ikilisi
arasında ise iki nokta kullanılır.

İkinci kullanımı ise liste tipine çok benzer. Bu kullanımda
anahtar-değer değil, sadece değer verilir.
::

    {
        "Fırat",
        "Özgül"
    }

JSON modülünde 4 ana fonksiyon bulunuyor. Bunlardan ikisi
Python ile JSON oluşturmaya yararken diğer ikisi JSON
verilerini çözmeye yarar. JSON oluşturan fonksiyonlar şu
ikisidir:

    #. json.dump
    #. json.dumps

JSON verilerini çözen iki fonksiyon ise şunlardır:

    #. json.load
    #. json.loads

json.dump ve json.dumps
************************

Bu iki fonksiyonu birlikte yazmak istedim. Çünkü ikisinin
parametreleri neredeyse aynı. Aralarındaki fark ise şu:

    `dump` fonksiyonu çıktıyı illaki bir dosya içine aktarır.
    Yani size al bu senin istediğin JSON çıktısı demez. Bunu diyen
    `dumps` fonksiyonudur. `dumps` fonksiyonu `str` tipinde
    bir değer döndürürken `dump` fonksiyonu hiçbir değer döndürmez.

O yüzden python.org sitesinden alınan şu örneklerde `dump`
yerine `dumps` fonksiyonu kullanılmış.Eğer `dump` fonksiyonunu
kullanacaksanız JSON'a dönüşmesini istediğiniz ifadeden sonra
dosyayı bulunduran değişkeni yazın.
::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Bu fonksiyonların birkaç parametresi var. Şimdi sıra bunların
ne işe yaradığını öğrenmekte.

**skipkeys**

Normalde Python, JSON oluştururken anahtar veya değer basit tipte
(str,int,float...) değilse `TypeError` hatası verir.
Eğer bu parametre `True` (Varsayılan `False`) ise hata vermek yerine o ikiliyi atlar.

**ensure_ascii**

Eğer bu parametre `True` (varsayılan olarak) ise çıktıda ASCII
tablosuna uymayan karakterlerden kaçınır. `False` ise buna dikkat etmez.

::

    >>> import json
    >>> json.dumps(["üzüm"],ensure_ascii=True)
    '["\\u00fcz\\u00fcm"]'
    >>> json.dumps(["üzüm"],ensure_ascii=False)
    '["üzüm"]'

**indent**

Eğer negatif olmayan bir tamsayı veya bir karakter dizisi ise
girintileme sayesinde daha güzel bir çıktı almanızı sağlar.
Eğer 0, negatif sayı veya boş karakter dizisi(`""`) ise her öğeyi yeni
satıra basar. None(varsayılan) ise dip dibe bir çıktı verir.
Pozitif bir sayı verildiğinde onu boşluk sayısı kabul ederek
girintileme yapar. Karakter dizisi ifadesine şu ikisi yeterince açık
bir örnek: `\\t`, `\\n`

.. Note:: Karakter dizisi kullanımı 3.2 sürümü itibari ile başladı.

::

    >>> print(json.dumps({"Özellikler":{"Hız":150,"Ses":"10db"}},indent=None))
    {"\u00d6zellikler": {"H\u0131z": 150, "Ses": "10db"}}
    >>> print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent=4))
    {
        "Ozellikler": {
            "Hiz": 150,
            "Ses": "10db"
        }
    }
    >>> print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent="\n"))
    {

    "Ozellikler": {


    "Hiz": 150,


    "Ses": "10db"

    }
    }
    >>> print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent=0))
    {
    "Ozellikler": {
    "Hiz": 150,
    "Ses": "10db"
    }
    }

**separators**

Bu parametre verilen değeri öğeler arasında ayraç olarak
kullanır. Verilen değer tuple tipinde olmalıdır. Varsayılan olarak
şu kullanılır: `(",", ": ")`
Ancak indent parametresi `None` değerindeyse ilk virgül değeri de iki
nokta gibi sonuna boşluk alır. Yani şu şekilde olur: `(", ", ": ")`
::

    >>> json.dumps({"Elma":42,"Armut":25,"kiraz":65},separators=("?","!"))
    '{"Elma"!42?"Armut"!25?"kiraz"!65}'

json.load ve json.loads
***********************

Bu iki fonksiyon da dump ve dumps gibi birbirine çok benziyor.
Hatta farkları bile neredeyse aynı. load fonksiyonu sadece
dosyadaki JSON verilerini Python verisine çevirirken
loads fonksiyonu veriyi parametre olarak alıyor. dump
ve dumps'da olduğu gibi parametreleri tamamen aynı.

Buraya birkaç örnek kod yazalım.
::

    >>> json.loads('{"mezuniyet": "üniversite", "Bölüm": "Tıp"}')
    {'mezuniyet': 'üniversite', 'Bölüm': 'Tıp'}
    >>> json.loads('["\\u00fcz\\u00fcm"]')
    ['üzüm']

Şimdi de sıra fonksiyonların aldığı parametrelerde.

**object_hook**

Döndürülen değerin veri tipini değiştirmenizi sağlar. Bunu
bir kod ile açıklayalım.
::

    >>> json.loads('{"mezuniyet": "üniversite", "Bölüm": "Tıp"}',object_hook=list)
    ['mezuniyet', 'Bölüm']

Gördüğünüz gibi çıktıyı liste tipinde verdi. Ancak bunu
yapmak için sadece anahtarları aldı.

**object_pairs_hook**

object_pairs_hook, object_hook ile benzer görevler yapıyor.
İkisi arasında öncelik object_pairs_hook'da. Eğer anahtar değer
ilişkisinden oluşan bir JSON verisiyse object_pairs_hook
değilse object_hook parametresi kullanılır.
::

    >>> json.loads('{"Ad": "Fırat", "Soyad": "Özgül"}',object_pairs_hook=str)
    "[('Ad', 'Fırat'), ('Soyad', 'Özgül')]"
    >>> json.loads('["Fırat", "Özgül"]',object_pairs_hook=dict,object_hook=list)
    ['Fırat', 'Özgül']

**parse_int**

int tipindeki değerlerin Python koduna dönüştürülürken hangi
tipin kullanılması gerektiğini belirler. Bunu bir kodla
açıklamak daha kolay olur sanıyorum::

    >>> json.loads('{"Satılan": 54, "Kalan": 46}',parse_int=float)
    {'Satılan': 54.0, 'Kalan': 46.0}

**parse_float**

parse_int parametresinin yaptığını float tipindeki sayılar
için yapar.
::

    >>> json.loads('[23, 45.2, "yazbel", 512.128]',parse_int=bool,parse_float=list)
    [True, ['4', '5', '.', '2'], 'yazbel', ['5', '1', '2', '.', '1', '2', '8']]
