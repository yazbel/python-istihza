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

## Belgelerden çevrimdışı iken faydalanmak

Çevrimdışı olarak kullandığınız belgelerin zaman ile güncelliğini yitirip https://python-istihza.yazbel.com/ adresindeki belgelerin gerisinde kalabileceğini unutmayın.

### PDF olarak indirme

[`/docs/YazbelPythonProgramlamaDiliBelgeleri.pdf`](/docs/YazbelPythonProgramlamaDiliBelgeleri.pdf) dosyasını [bu](https://python-istihza.yazbel.com/YazbelPythonProgramlamaDiliBelgeleri.pdf) link aracılığı ile indirip kullanabilirsiniz.

### EPUB olarak indirme

[`/docs/YazbelPythonProgramlamaDiliBelgeleri.epub`](/docs/YazbelPythonProgramlamaDiliBelgeleri.epub) dosyasını [bu](https://python-istihza.yazbel.com/YazbelPythonProgramlamaDiliBelgeleri.epub) link aracılığı ile indirip kullanabilirsiniz.

### Tek parça HTML olarak indirme

[`/docs/YazbelPythonProgramlamaDiliBelgeleri.html`](/docs/YazbelPythonProgramlamaDiliBelgeleri.html) dosyasını [bu](https://python-istihza.yazbel.com/YazbelPythonProgramlamaDiliBelgeleri.html) link aracılığı ile indirip kullanabilirsiniz.

### Siteyi kaynaktan indirme

Bu veri havuzunu cihazınıza indirebilir ve [`/docs/index.html`](/docs/index.html) dosyasını tarayıcınız ile açabilirsiniz. Bu size belgeleri çevrimiçi olarak kullanmak ile aynı deneyimi sunacaktır.  

## Belgeleri inşa etme

Buradaki belgeler [reStructuredText](http://docutils.sourceforge.net/rst.html) formatında yazılmış ve [Sphinx](http://www.sphinx-doc.org/) kullanılarak derlenmiştir.
Belgeleri derlemek için öncelikle Sphinx'i kurmalısınız. Sphinx, Python'un 3.6 ve daha yukarı versiyonlarını desteklemektedir.
Belgelere katkıda bulunmayı planlıyorsanız önce [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasına başvurun.

### Debian/Ubuntu

Bir Python3.6+ sürümünün, `pip`'in ve `make`'in sisteminizde kurulu olduğundan emin olduktan sonra projenin kök dizinine gidip bu komut ile gerekli kütüphaneleri kurabilirsiniz:

```shell
$ python3 -m pip install -r requirements.txt
```

Daha sonra yine projenin kök dizinde bu komutu çalıştırarak belgeleri inşa edebilirsiniz:

```shell
$ make html
```

Belgeleri inşa ettikten sonra `/scripts/move_documents.py` betiği `/build/` içindeki gerekli dosya ve klasörleri `/docs/` içine taşıyacaktır:

```shell
$ python3 ./scripts/move_documents.py
```

Bu şekilde inşa ettiğiniz dökümanı görüntülemek için `/docs/index.html` dosyasını tarayıcınız ile açabilirsiniz.

### Windows

Python'un 3.6 veya daha yüksek bir sürümünün bilgisayarınızda kurulu olduğundan ve `python.exe`'nin PATH'da bulunduğundan emin olduktan sonra projenin kök dizinine gidip bu kodu ``cmd.exe``'de çalıştırarak gerekli kütüphaneleri kurabilirsiniz:

```shell
> python -m pip install -r requirements.txt
```

Yükleme işlemi başarıyla gerçekleşmiş ise şu komut size Sphinx'in versiyonunu verecektir:

```shell
> sphinx-build --version
```

Daha sonra yine projenin kök dizinde bu komutu çalıştırarak belgeleri inşa edebilirsiniz:

```shell
> make.bat html
```

Belgeleri inşa ettikten sonra `/scripts/move_documents.py` betiği `/build/` içindeki gerekli dosya ve klasörleri `/docs/` içine taşıyacaktır:

```shell
> python scripts/move_documents.py
```

Bu şekilde inşa ettiğiniz dökümanı görüntülemek için `/docs/index.html` dosyasını tarayıcınız ile açabilirsiniz.

### Diğer işletim sistemleri

Diğer işletim sistemlerinde Sphinx kurulumu ve ayrıntılı bilgi için [buraya](https://www.sphinx-doc.org/en/master/usage/installation.html) bakabilirsiniz.

## Nasıl yardım alabilirim?

Her zaman [YazBel forumu](https://forum.yazbel.com/)nun [Python kategorisi](https://forum.yazbel.com/c/python)nde bir
konu açarak aklınızdaki soruları sorabilirsiniz. Topluluk size yardım etmekten mutluluk duyacaktır.

## Nasıl yardım edebilirim?

Belgelere ekleme yaparak veya yazım ve bilgi yanlışlarını düzelterek yardım edebilirsiniz:

- Topluluk tarafından eksikliği hissedilen bazı konular ve belgelerdeki düzeltilmesi gereken hatalar [issues](https://github.com/yazbel/python-istihza/labels/help%20wanted) 
sayfasında listelenmiş halde bulunuyor. Bu konular üzerinde çalışma yapabilirsiniz.

- Belgelerde değişiklik yaparak çekme isteği (pull request) gönderebilirsiniz. Yazım yanlışları ve küçük hatalar için
GitHub arayüzünü kullanabilirsiniz ancak daha büyük ve karmaşık düzeltmeler için veri havuzunu bilgisayarınıza çekmeli,
daha sonrasında düzeltmeleri yapmalı ve belgeleri inşa edip çekme isteği göndermelisiniz. Her iki durumda da kısa ve öz bir
işleme mesajı (commit message) yazdığınıza emin olmalısınız.

- Eğer bir yanlış gördünüz ancak bir sebepten ötürü düzeltmeyi kendiniz yapmak istemediyseniz, bu hatayı bildirerek de
yardım edebilirsiniz. Bunun için veri havuzunun [konular (issues)](https://github.com/yazbel/python-istihza/issues)
dizininde bir konu açın, başlık ve açıklama kısmına ilgili metinleri yazın ve gönderin. Başlık kısmının kısa ve öz
olmasına dikkat edin.

## Lisans

[`LICENSE`](LICENSE) dosyasında da belirtildiği üzere bu
belgelerin lisansı **Creative Commons Atıf-GayriTicari-AynıLisanslaPaylaş 3.0 Yerelleştirilmemiş (CC BY-NC-SA 3.0)**
lisansıdır. Daha fazla bilgi için lütfen dosyanın içeriğine bakınız.