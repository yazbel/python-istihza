# Belgelerin İnşası

Buradaki belgeler [reStructuredText](http://docutils.sourceforge.net/rst.html) formatında yazılmış ve [Sphinx](http://www.sphinx-doc.org/) kullanılarak derlenmiştir. Belgeleri derlemek için öncelikle Sphinx'i kurmalısınız. Sphinx, Python'un 3.10 ve daha yukarı versiyonlarını desteklemektedir.

Belgelere katkıda bulunmayı planlıyorsanız önce [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasına başvurun.

## Debian/Ubuntu

Bir Python3.10+ sürümünün, `pip`'in ve `make`'in sisteminizde kurulu olduğundan emin olduktan sonra projenin kök dizinine gidip bu komut ile gerekli kütüphaneleri kurabilirsiniz:

```shell
python3 -m pip install -r requirements.txt
```

Daha sonra yine projenin kök dizinde bu komutu çalıştırarak belgeleri inşa edebilirsiniz:

```shell
make html
```

Belgeleri inşa ettikten sonra `/scripts/move_documents.py` betiği `/build/` içindeki gerekli dosya ve klasörleri `/docs/` içine taşıyacaktır:

```shell
python3 ./scripts/move_documents.py
```

Bu şekilde inşa ettiğiniz dökümanı görüntülemek için `/docs/index.html` dosyasını tarayıcınız ile açabilirsiniz.

## Windows

Python'un 3.10 veya daha yüksek bir sürümünün bilgisayarınızda kurulu olduğundan ve `python.exe`'nin PATH'de bulunduğundan emin olduktan sonra projenin kök dizinine gidip bu kodu ``cmd.exe``'de çalıştırarak gerekli kütüphaneleri kurabilirsiniz:

```shell
python -m pip install -r requirements.txt
```

Yükleme işlemi başarıyla gerçekleşmiş ise şu komut size Sphinx'in versiyonunu verecektir:

```shell
sphinx-build --version
```

Daha sonra yine projenin kök dizinde bu komutu çalıştırarak belgeleri inşa edebilirsiniz:

```shell
make.bat html
```

Belgeleri inşa ettikten sonra `/scripts/move_documents.py` betiği `/build/` içindeki gerekli dosya ve klasörleri `/docs/` içine taşıyacaktır:

```shell
python scripts/move_documents.py
```

Bu şekilde inşa ettiğiniz dökümanı görüntülemek için `/docs/index.html` dosyasını tarayıcınız ile açabilirsiniz.

## Diğer işletim sistemleri

Diğer işletim sistemlerinde Sphinx kurulumu ve ayrıntılı bilgi için [buraya](https://www.sphinx-doc.org/en/master/usage/installation.html) bakabilirsiniz.

---

## Belgeleri diğer formatlarda inşa etme

Önce yukarıdaki adımları takip edip Sphinx'in kurulumunu gerçekleştirin.

Belgeleri diğer formatlarda inşa ettikten sonra da `/scripts/move_documents.py` betiğini çalıştırmayı unutmayın.

### Tek parça HTML olarak inşa etme

Debian/Ubuntu'da:

```shell
make singlehtml
```

Windows'ta:

```shell
make.bat singlehtml
```

HTML dosyası `/build/singlehtml/` dizininde `index.html` adı ile oluşacaktır.

### EPUB olarak inşa etme

Debian/Ubuntu'da:

```shell
make epub
```

Windows'ta:

```shell
make.bat epub
```

EPUB dosyası `/build/epub/` dizininde `Yazbel Python Belgeleri.epub` adı ile oluşacaktır.

### PDF olarak inşa etme

Belgeleri PDF olarak inşa edebilmek için ``pdflatex`` uygulamasına ihtiyacınız olacak. [MikTeX](https://miktex.org/) veya [TeX Live](https://www.tug.org/texlive/) gibi bir TeX dağıtımını indirerek bu uygulamayı edinebilirsiniz. Bu dağıtımların belgerin inşası için gerekli eklentiler ile birlikte 800 Megabyte gibi bir disk alanı kaplayabileceğini unutmayın. TeX dağıtımının kurulumunda bir problem yaşarsanız [buraya](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder) başvurabilirsiniz.

> Eğer Windows kullanıyorsanız ve [`winget`](https://github.com/microsoft/winget-cli) CLI uygulamasına sahipseniz MikTeX dağıtımını indirmek için bu yolu da izleyebilirsiniz:
>
> ```shell
> winget install MiKTeX.MiKTeX
> winget install StrawberryPerl.StrawberryPerl # MiKTeX aynı zamanda bir Perl kurulumu gerektirir
> ```

Uygun bir TeX dağıtımını kurduktan sonra `pdflatex`'in bulunduğu dizinin PATH'de bulunduğundan emin olun.

Debian/Ubuntu'da:

```shell
make latexpdf
```

Windows'ta:

```shell
make.bat latexpdf
```

Herhangi bir hata oluşmazsa PDF dosyası `/build/latex/` dizininde `yazbelpythonbelgeleri.pdf` adı ile oluşacaktır.
