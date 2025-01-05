# Belgelerin İnşası

Bu belgeler [reStructuredText](http://docutils.sourceforge.net/rst.html) formatında yazılmış ve [Sphinx](http://www.sphinx-doc.org/) kullanılarak oluşturulmuştur. Belgeleri derlemek için öncelikle Sphinx'i kurmanız gerekmektedir. Sphinx, Python 3.10 ve üzeri sürümleri destekler.

Belgelere katkıda bulunmayı düşünüyorsanız önce [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasını incelemenizi öneririz.

## Gereksinimler ve Kurulum

### Debian/Ubuntu

1. **Gerekli Araçlar:**
   - Python 3.10 veya daha üstü sürüm
   - `pip`
   - `make`

2. **Kurulum Adımları:**

Projenin kök dizinine gidin ve gerekli kütüphaneleri şu komutla yükleyin:

```shell
python3 -m pip install -r requirements.txt
```

Daha sonra belgeleri derlemek için şu komutu çalıştırın:

```shell
make html
```

Belgeleri inşa ettikten sonra, `/scripts/move_documents.py` betiği, `/build/` dizinindeki gerekli dosyaları `/docs/` dizinine taşıyacaktır:

```shell
python3 ./scripts/move_documents.py
```

Sonuç olarak, oluşturulan belgeleri görüntülemek için `/docs/index.html` dosyasını tarayıcınızda açabilirsiniz.

---

### Windows

1. **Gerekli Araçlar:**
   - Python 3.10 veya daha üstü sürüm
   - PATH ortam değişkenine eklenmiş `python.exe`

2. **Kurulum Adımları:**

Projenin kök dizinine gidin ve gerekli kütüphaneleri şu komutla yükleyin:

```shell
python -m pip install -r requirements.txt
```

Yüklemenin başarılı olduğunu doğrulamak için aşağıdaki komutu çalıştırarak Sphinx sürümünü kontrol edin:

```shell
sphinx-build --version
```

Belgeleri inşa etmek için şu komutu çalıştırın:

```shell
make.bat html
```

Belgeler oluşturulduktan sonra, `/scripts/move_documents.py` betiği ile dosyaları taşıyın:

```shell
python scripts/move_documents.py
```

Oluşturulan belgeleri görmek için `/docs/index.html` dosyasını tarayıcınızda açabilirsiniz.

---

### Diğer İşletim Sistemleri

Farklı işletim sistemlerinde Sphinx'in kurulumu hakkında detaylı bilgi için [Sphinx'in resmi kurulum belgelerini](https://www.sphinx-doc.org/en/master/usage/installation.html) inceleyebilirsiniz.

---

## Diğer Formatlarda Belgeleri İnşa Etme

Sphinx ile belgeleri farklı formatlarda oluşturabilirsiniz. Aşağıdaki adımları izleyerek belgeleri ihtiyaçlarınıza uygun şekilde inşa edebilirsiniz.

### Tek Parça HTML

Debian/Ubuntu'da:

```shell
make singlehtml
```

Windows'ta:

```shell
make.bat singlehtml
```

Oluşturulan HTML dosyası `/build/singlehtml/index.html` yolunda bulunacaktır.

---

### EPUB

Debian/Ubuntu'da:

```shell
make epub
```

Windows'ta:

```shell
make.bat epub
```

EPUB dosyası `/build/epub/Yazbel Python Belgeleri.epub` olarak kaydedilecektir.

---

### PDF

PDF formatında belgeleri oluşturmak için bir TeX dağıtımı (ör. [MikTeX](https://miktex.org/) veya [TeX Live](https://www.tug.org/texlive/)) kurmanız gereklidir. Bu dağıtımlar genellikle ek eklentilerle birlikte kurulur ve yaklaşık 800 MB disk alanı gerektirir.

> **Windows Kullanıcıları için:** Eğer [`winget`](https://github.com/microsoft/winget-cli) kuruluysa, MikTeX'i şu komutlarla yükleyebilirsiniz:
> 
> ```shell
> winget install MiKTeX.MiKTeX
> winget install StrawberryPerl.StrawberryPerl # MikTeX ayrıca bir Perl kurulumu gerektirir
> ```

TeX dağıtımı kurulduktan sonra `pdflatex` uygulamasının PATH ortam değişkeninde yer aldığından emin olun.

Belgeleri PDF formatında oluşturmak için:

- **Debian/Ubuntu:**
  ```shell
  make latexpdf
  ```

- **Windows:**
  ```shell
  make.bat latexpdf
  ```

Oluşturulan PDF dosyası `/build/latex/yazbelpythonbelgeleri.pdf` yolunda bulunacaktır.

---
