Bu belgeler topluluk desteğiyle geliştirilmektedir. Bu sebeple katkılarınız çok değerlidir.

### Gereklilikler

`make html` komutununun çalışabilmesi için ***make***, ***Python*** ve ***Sphinx***'in sisteminizde kurulu olması gerekmektedir.

Bu araçları Ubuntu'da şu komutla kurabilirsiniz:

```sudo apt install make python3 python3-sphinx```

Eğer Windows kullanıyorsanız, Windows Store uygulamasından Ubuntu'yu yükleyip, WSL üzerinden Ubuntu kullarak aynı komut ile kurulumu gerçekleştirebilirsiniz.

### Katkıda Bulunmak

Katkıda bulunmak için [sphinx_source](sphinx_source) dizini altındaki ***rst*** uzantılı dosyaları değiştirmelisiniz.

Daha sonra ***sphinx_source*** dizini içerisinde iken aşağıdaki komut ile rst dosyalarından yeni HTML dosyalarını oluşturabilirsiniz.

```make html```

HTML dosyalarını oluşturduktan sonra bunları ***build/html*** dizini altından kopyalayıp ana dizine yapıştırmanız ve bu şekilde commit etmeniz gerekmektedir. Aşağıdaki komut ile ***build/html*** dizini içerisindeki yeni HTML dosyalarını ana dizine kopyalayabilirsiniz.

```cp -R build/html/* ./```

Katkılarınız için teşekkürler. 
