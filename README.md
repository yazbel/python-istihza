# YazBel Python Belgeleri

[https://python-istihza.yazbel.com](https://python-istihza.yazbel.com)

Bu belgeler [Python](https://www.python.org/) programlama dilinin 3. sürümünü anlatmaktadır ve
[istihza.com](http://www.istihza.com/)'da yer alan, [Fırat Özgül](http://www.kodlab.com/AuthorDetail.aspx?ID=50)'ün
yazdığı [Python 3 belgeleri](http://belgeler.istihza.com/py3/)nden oluşturulmuştur.

## Belgeler neden buraya kopyalandı?

Bu belgeler buraya kopyalanmadan bir süre önce Fırat Özgül, istihza.com projesinin sonlanacağını istihza.com forumunda
[duyurdu](http://www.istihza.com/forum/viewtopic.php?f=50&t=3849). Proje sonlandığında elbette
belgeler kaybolmayacak; internette bir yerlerde bulunabilir olacaklar. istihza.com topluluğu da Python'ı öğrenmekten ve
öğretmekten vazgeçmeyecek. Ancak belgelerin sadece bulunabilir olmaları değil, zamanla gelişmeleri de gerekli; Python
dili sürekli gelişiyor ve güncellenmeyen belgeler bir süre sonra eksik ve yanlış bilgileri içermeye mahkum olacaktır.
Bu veri havuzu sayesinde belgeler, kaynak kodu ile birlikte, bulunabilir ve en önemlisi de geliştirilebilir olacak.
Hatta bu gelişime siz de dahil olabilirsiniz!

Bu arada proje sonlandığında bu belgede istihza.com'a verilen bağlantıların çalışmayabileceğini de unutmamalısınız.

## Belgeleri inşa etme

Buradaki belgeler [reStructuredText] formatında yazılmış ve [Sphinx] kullanılarak derlenmiştir.
Belgeleri derlemek için öncelikle Sphinx'i kurmalısınız. Sphinx, Python'un 3.6 ve daha yukarı versiyonlarını desteklemektedir.


#### Debian/Ubuntu için kurulum

Sphinx'i Debian veya Ubuntu'da şu komutla kurabilirsiniz:

```shell
$ apt install python3-sphinx
```

Daha sonra `python-istihza/` dizinine gidip bu komutla belgeleri inşa edebilirsiniz:

```shell
$ make html
```

Belgeleri inşa ettikten sonra `move.py` betiği `python-istihza/build/html` içindeki dosyaları `python-istihza/` dizinine çıkaracaktır ve `python-istihza/build` klasörünü silecektir:

```shell
> python move.py
```

#### Windows için kurulum

[Python](https://www.python.org/downloads/)'un bilgisayarınızda kurulu olduğundan ve `pip.exe`'nin PATH'da bulunduğundan emin olduktan sonra bu kodu ``CMD``'de çalıştırarak Sphinx'i kurabilirsiniz:

```shell
> pip install sphinx
```

Yükleme işlemi başarıyla gerçekleşmiş ise şu komut size Sphinx'in versiyonunu verecektir:

```shell
> sphinx-build --version
```

Daha sonra `python-istihza/` dizinine gidip bu komutla belgeleri inşa edebilirsiniz:

```shell
> make.bat html
```

Belgeleri inşa ettikten sonra `move.py` betiği `python-istihza/build/html` içindeki dosyaları `python-istihza/` dizinine çıkaracaktır ve `python-istihza/build` klasörünü silecektir:

```shell
> python move.py
```


#### Diğer işletim sistemleri

Diğer işletim sistemlerinde Sphinx kurulumu ve ayrıntılı bilgi için [buraya](https://www.sphinx-doc.org/en/master/usage/installation.html) bakabilirsiniz.

## Nasıl yardım alabilirim?

Her zaman [YazBel forumu](https://forum.yazbel.com/)nun [Python kategorisi](https://forum.yazbel.com/c/python)nde bir
konu açarak aklınızdaki soruları sorabilirsiniz. Topluluk size yardım etmekten mutluluk duyacaktır.

## Nasıl yardım edebilirim?

Birçok şekilde yardım edebilirsiniz:

- Belgelerde değişiklik yaparak çekme isteği (pull request) gönderebilirsiniz. Yazım yanlışları ve küçük hatalar için
GitHub arayüzünü kullanabilirsiniz ancak daha büyük ve karmaşık düzeltmeler için veri havuzunu bilgisayarınıza çekmeli,
daha sonrasında düzeltmeleri yapıp çekme isteği göndermelisiniz. Her iki durumda da kısa ve öz bir
işleme mesajı (commit message) yazdığınıza emin olmalısınız.

- Eğer bir yanlış gördünüz ancak bir sebepten ötürü düzeltmeyi kendiniz yapmak istemediyseniz, bu hatayı bildirerek de
yardım edebilirsiniz. Bunun için veri havuzunun [konular (issues)](https://github.com/yazbel/python-istihza/issues)
dizininde bir konu açın, başlık ve açıklama kısmına ilgili metinleri yazın ve gönderin. Başlık kısmının kısa ve öz
olmasına dikkat edin.

## Lisans

[`LICENSE`](https://github.com/yazbel/python-istihza/blob/master/LICENSE) dosyasında da belirtildiği üzere bu
belgelerin lisansı **Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 3.0 Yerelleştirilmemiş (CC BY-NC-SA 3.0)**
lisansıdır. Daha fazla bilgi için lütfen dosyanın içeriğine bakınız.

[reStructuredText]: http://docutils.sourceforge.net/rst.html
[Sphinx]: http://www.sphinx-doc.org/
