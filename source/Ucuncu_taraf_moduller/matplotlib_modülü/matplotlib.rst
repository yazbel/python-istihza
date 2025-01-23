Matplotlib
==========

Matplotlib, Python ile kullanılan bir veri görselleştirme kütüphanesidir. Kısaca bu kütüphane grafik çizdirebilmemize yarayan bir kütüphanedir. Finans uygulamaları, veri analizi, matematiksel fonksiyonların grafiklerinin çizimi, yapay zeka ve kişisel projeler gibi birçok şeyde kullanılabilir.

Yapabileceğiniz bazı örnek projeler:
-------------------------------------

1. **Hisse Senedi Analizi:**
   - Hisse senedi fiyatlarını çizgi grafikleriyle görselleştirme.
   - Hareketli ortalamaları hesaplayıp grafik üzerinde gösterme.
   
2. **İklim Verisi Analizi:**
   - Sıcaklık ve yağış verilerini zaman içinde grafikleme.
   - Farklı bölgelerin iklim verilerini karşılaştırma.
   
3. **Makine Öğrenmesi Modeli Değerlendirme:**
   - Modelin eğitim ve test performansını grafiklerle gösterme.
   - Sınıflandırma problemlerinde karar sınırlarını çizme.
   
4. **Kişisel Bütçe Takibi:**
   - Aylık harcamaları pasta grafikleriyle görselleştirme.
   - Gelir ve giderleri çubuk grafiklerle karşılaştırma.
   
5. **Eğitimde Kavram Görselleştirme:**
   - Matematiksel fonksiyonların grafiklerini çizme.
   - İstatistiksel dağılımları gösterme.

Aynı zamanda kullanabileceğiniz grafik çeşitleri:
------------------------------------------------

- **Çizgi Grafiği (Line Chart)**
- **Çubuk Grafiği (Bar Chart)**
- **Yığılmış Çubuk Grafiği (Stacked Bar Chart)**
- **Histogram (Histogram)**
- **Dağılım Grafiği (Scatter Plot)**
- **Pasta Grafiği (Pie Chart)**
- **Alan Grafiği (Area Chart)**
- **Kutu Grafiği (Box Plot)**
- **Isı Haritası (Heatmap)**
- **Kutup Grafiği (Polar Plot)**
- **Saplama Grafiği (Stem Plot)**
- **Adım Grafiği (Step Plot)**
- **Çizgi ve Çubuk Birleşimi (Combination of Line and Bar Chart)**
- **Hata Çubukları Grafiği (Error Bar Plot)**
- **Balon Grafiği (Bubble Chart)**
- **3D Çizgi Grafiği (3D Line Plot)**
- **3D Dağılım Grafiği (3D Scatter Plot)**
- **3D Yüzey Grafiği (3D Surface Plot)**
- **3D Çubuk Grafiği (3D Bar Chart)**
- **Dalgalı Çizgi Grafiği (Filled Line Plot)**
- **Likert Grafiği (Likert Chart)**
- **Paralel Koordinat Grafiği (Parallel Coordinates Plot)**
- **Çift Eksenli Grafik (Dual-Axis Plot)**
- **Yoğunluk Grafiği (Density Plot)**
- **Violin Grafiği (Violin Plot)**
- **Halka Grafiği (Donut Chart)**
- **Akış Grafiği (Streamgraph)**
- **Bölge Grafiği (Contour Plot)**
- **Vektör Alanı Grafiği (Quiver Plot)**
- **Ağaç Haritası (Treemap)**

Kurulum
--------

.. code-block:: jsx

   pip install matplotlib

Matplotlib kurulumunu kontrol etme
------------------------------------

.. code-block:: python

   print(matplotlib.__version__)

   # Örneğin şu anki versiyon 3.9.2

Kullanım
--------

Önce kısa bir örnek yapalım, böylece aklımızda Matplotlib'in ne olduğu hakkında daha net bir şey oluşacak. Aşağıdaki kodu direkt olarak kopyalayıp çalıştırın, ardından pyplot'u ve diğerlerini öğrenmeye devam edelim.

.. code-block:: python

   import matplotlib
   import matplotlib.pyplot as plt

   plt.plot([1, 2, 3], [4, 5, 6])
   plt.show()


Çalıştırdığınız zaman oluşan grafikte sol altta işaretler göreceksiniz. Kısaca bahsetmek gerekirse:

- **Ev (Home) İkonu**: Grafiği başlangıç görünümüne sıfırlar. Eğer grafik üzerinde yakınlaştırma veya kaydırma yaptıysanız, bu düğme grafiği ilk haline geri döndürür.
- **Geri (Back) ve İleri (Forward) İkonları**: Görünüm geçmişinde gezinmenizi sağlar. Örneğin, yakınlaştırma veya kaydırma işlemlerinden önceki bir görünüme dönmek için "Geri", tekrar ilerlemek için "İleri" kullanılır.
- **Dörtlü Ok (Pan/Zoom) İkonu**: Grafiği fare yardımıyla hareket ettirmenizi (pan) veya belirli bir bölgeyi yakınlaştırmanızı sağlar.
- **Zoom (Büyüteç İkonu)**: Seçim yaparak belirli bir bölgeye yakınlaştırma yapar. Seçtiğiniz alan odaklanır.
- **Ayar Çubukları (Three Horizontal Bars)**: Bu ikon, grafiğin **yer kaplama düzenini** ayarlamanızı sağlar. Bu ikon, grafik üzerinde alt grafiklerin (subplots) düzenini, özellikle **grafiklerin boyutlarını** değiştirmek için kullanılır. Grafiğin ve alt grafiklerin kenar boşluklarını ve boyutlarını ayarlamak için bu simgeye tıklayarak, etkileşimli olarak düzenleme yapabilirsiniz. İkinci grafikte gösterdiğim buydu.
- **Kaydet (Disket İkonu)**: Grafiği bir görüntü dosyası (ör. PNG, JPG) olarak kaydetmenize olanak tanır.

Pyplot
-------

Kullanıcıların grafikler oluşturmasını, düzenlemesini ve görüntülemesini kolaylaştırır. pyplot modülü, grafik oluşturma işlemlerini basit hale getirir. Örneğin ilk yaptığımız örnekte kullanmıştık.

`plt.plot()`, `plt.show()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()` gibi fonksiyonlar, grafiklerinizi oluşturmak ve özelleştirmek için kullanılır.

.. code-block:: python

   import matplotlib.pyplot as plt

   # Basit bir çizgi grafiği oluşturma
   plt.plot([1, 2, 3], [4, 5, 6])  # İlk değer x, ikinci değer ise y değeridir.
   plt.title('Basit Çizgi Grafiği')  # Başlık eklemek
   plt.xlabel('X Ekseni')  # X eksenine isim vermek. Örneğin yıllara göre araba sayısı üretimini anlatıyorsanız ona göre isimler verebilirsiniz.
   plt.ylabel('Y Ekseni')
   plt.show()  # Grafiğimizin gösterilmesini sağlar.

Figure
------

Bir kağıt gibi düşünebilirsiniz; birden fazla grafik içerebilir ve ayrıca bu kağıdın büyüklüğünü ayarlayabilirsiniz.

.. code-block:: python

   fig = plt.figure(figsize=(10, 5))  # 10x5 inç boyutunda bir kağıt oluştur

Axes
-----

Grafiğimizin ekrandaki hangi bölgede olacağını belirler.

.. code-block:: python

   ax = fig.add_subplot(122)  # 1---> Satır Sayısı
                               # 2---> Sütun Sayısı
                               # 3: Aşağıdaki hangi bölgede olacağını belirlediğimiz kısım burasıdır.

   +-------+-------+
   |   1   |   2   |
   +-------+-------+
   |   3   |   4   |
   +-------+-------+

   1. Alt Grafik: fig.add_subplot(221) ile oluşturulur. Bu, yukarıdaki sol köşedeki alanı temsil eder.
   2. Alt Grafik: fig.add_subplot(222) ile oluşturulur. Bu, yukarıdaki sağ köşedeki alanı temsil eder.
   3. Alt Grafik: fig.add_subplot(223) ile oluşturulur. Bu, aşağıdaki sol köşedeki alanı temsil eder.
   4. Alt Grafik: fig.add_subplot(224) ile oluşturulur. Bu, aşağıdaki sağ köşedeki alanı temsil eder.

Aynı zamanda subplot oluşturmak için kullanılan bir yöntem daha var.

.. code-block:: python

   ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)

   1. Toplam 6 satır ve 1 sütunluk bir ızgara tanımlanmış.
   2. Bu alt grafik, ızgaranın ilk satırında (0, 0) konumunda başlar.
   3. rowspan: Sadece 1 satır boyunca yer kaplar.
   4. colspan: Sadece 1 sütun boyunca yer kaplar.

1. **Yerleşim Esnekliği**:
   - `plt.subplot`: Grafikler sabit ve eşit boyutlarda bölgelere yerleştirilir.
   - `plt.subplot2grid`: Grafiklerin boyutları ve yerleşimi (satır ve sütun kaplama) esnek şekilde tanımlanabilir.

2. **Kullanım Amacı**:
   - `plt.subplot`: Basit ve simetrik düzenler için uygundur.
   - `plt.subplot2grid`: Daha karmaşık ve özelleştirilmiş düzenler oluşturmak için uygundur.

3. **Kod Karmaşıklığı**:
   - `plt.subplot`: Daha basit ve hızlı.
   - `plt.subplot2grid`: Daha fazla kod yazımı gerektirir ama daha esnektir.

**Ne zaman ne kullanılır?**

- **Basit bir ızgara düzeni gerekiyorsa** → `plt.subplot`
- **Farklı boyutlarda veya asimetrik düzenler gerekiyorsa** → `plt.subplot2grid`

Bu subplotları hizalamak istersek bu kodu kullanmamız gerek:

.. code-block:: python

   plt.subplots_adjust(left=0.11, bottom=0.24, right=0.90, top=0.90, wspace=0.2, hspace=0)

### Özet: Farklar ve İlişkiler

- **Figure**: Büyük kağıt (tuval). Bir veya daha fazla resim yapabilirsin.
- **Axes**: Kağıt üzerindeki belirli bir alan (kutu). Bu alanda resim yaparsın.
- **Plot**: Gerçek resim. Bu alanda çizdiğin çizgi, nokta veya çubuk.

Çizgi Grafikleri (Line Graphs)
-------------------------------

.. code-block:: python

   import matplotlib.pyplot as plt

   # 1. Adım: Büyük Kağıt (Figure) Oluştur
   fig = plt.figure(figsize=(10, 5))  # 10x5 inç boyutunda bir kağıt oluştur

   # 2. Adım: Kutu (Axes) Oluştur
   ax = fig.add_subplot(111)  # Kağıdın üzerinde bir kutu oluştur

   # 3. Adım: Veri Noktalarını Belirle
   x = [1, 2, 3, 4, 5]  # Sınav numaraları (1. sınav, 2. sınav, vb.)
   y = [75, 85, 80, 90, 95]  # Öğrencinin aldığı notlar

   # 4. Adım: Resmi (Plot) Çiz
   ax.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2)  # Çizgi grafiği oluştur

   # 5. Adım: Başlık ve Etiketler Ekle
   ax.set_title('Öğrencinin Sınav Notları', fontsize=16)  # Grafiğe başlık ekle
   ax.set_xlabel('Sınav Numarası', fontsize=12)  # X eksenine etiket ekle
   ax.set_ylabel('Not', fontsize=12)  # Y eksenine etiket ekle

   # 6. Adım: Grafiği Göster
   plt.grid(True)  # Izgara çizgilerini ekle
   plt.show()  # Grafiği göster

1. **Büyük Kağıt (Figure)**: `fig = plt.figure(figsize=(10, 5))` ile 10x5 inç boyutunda bir kağıt oluşturuyoruz. Bu, grafiğimizin tüm alanını temsil ediyor.
2. **Kutu (Axes)**: `ax = fig.add_subplot(111)` ile kağıdın üzerinde bir kutu oluşturuyoruz. Bu kutu, grafiğimizin çizileceği alanı belirliyor.
3. **Veri Noktaları**: `x` ve `y` listeleri, sınav numaralarını ve öğrencinin aldığı notları temsil ediyor. Bu veriler, grafiğimizde gösterilecek.
4. **Resmi (Plot) Çiz**: `ax.plot(x, y, ...)` ile belirlediğimiz veri noktalarını bir çizgi ile birleştiriyoruz. `marker='o'` ile her bir veri noktasını bir daire ile gösteriyoruz.
5. **Başlık ve Etiketler**: `ax.set_title()`, `ax.set_xlabel()`, ve `ax.set_ylabel()` ile grafiğimize başlık ve eksen etiketleri ekliyoruz. Bu, grafiğimizin neyi temsil ettiğini anlamamıza yardımcı oluyor.
6. **Grafiği Göster**: `plt.show()` ile grafiğimizi ekranda gösteriyoruz. `plt.grid(True)` ile ızgara çizgilerini ekleyerek grafiği daha okunabilir hale getiriyoruz.


Dört Grafiğin Örneği

---------------------


Aşağıda, dört farklı grafiğin yer aldığı bir örnek bulunmaktadır. Buradaki `marker` ifadeleri, alttaki çıktıda gördüğünüz üzere üçgen, kare gibi işaretlemeler koyar.

.. code-block:: python


   import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot modülünü içe aktarır. Grafik çizimi için gerekli fonksiyonları sağlar.


   # Manuel olarak oluşturulmuş diziler

   x = [1, 2, 3, 4, 5]  # X eksenindeki değerler

   y1 = [2, 3, 5, 7, 11]  # İlk grafik için Y eksenindeki değerler (Veri 1)

   y2 = [1, 4, 6, 8, 10]  # İkinci grafik için Y eksenindeki değerler (Veri 2)

   y3 = [5, 3, 4, 2, 1]  # Üçüncü grafik için Y eksenindeki değerler (Veri 3)

   y4 = [10, 20, 15, 25, 30]  # Dördüncü grafik için Y eksenindeki değerler (Veri 4)


   # Grafiklerin oluşturulması

   fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 satır ve 2 sütundan oluşan bir grafik düzeni oluşturur. Boyutunu 10x8 inç olarak ayarlar.


   # İlk grafik

   axs[0, 0].plot(x, y1, 'r-', marker='o', label='Veri 1')  # x ve y1 dizileri ile kırmızı bir çizgi çizer. Veri noktalarını daire ile gösterir.
   axs[0, 0].set_title('Grafik 1')  # Grafiğin başlığını ayarlar.
   axs[0, 0].set_xlabel('X Ekseni')  # X ekseninin etiketini ayarlar.
   axs[0, 0].set_ylabel('Y Ekseni')  # Y ekseninin etiketini ayarlar.
   axs[0, 0].legend()  # Grafikteki veri serisini açıklayan bir gösterge ekler.


   # İkinci grafik

   axs[0, 1].plot(x, y2, 'g-', marker='s', label='Veri 2')  # x ve y2 dizileri ile yeşil bir çizgi çizer. Veri noktalarını kare ile gösterir.
   axs[0, 1].set_title('Grafik 2')  # Grafiğin başlığını ayarlar.
   axs[0, 1].set_xlabel('X Ekseni')  # X ekseninin etiketini ayarlar.
   axs[0, 1].set_ylabel('Y Ekseni')  # Y ekseninin etiketini ayarlar.
   axs[0, 1].legend()  # Grafikteki veri serisini açıklayan bir gösterge ekler.


   # Üçüncü grafik

   axs[1, 0].plot(x, y3, 'b-', marker='^', label='Veri 3')  # x ve y3 dizileri ile mavi bir çizgi çizer. Veri noktalarını üçgen ile gösterir.
   axs[1, 0].set_title('Grafik 3')  # Grafiğin başlığını ayarlar.
   axs[1, 0].set_xlabel('X Ekseni')  # X ekseninin etiketini ayarlar.
   axs[1, 0].set_ylabel('Y Ekseni')  # Y ekseninin etiketini ayarlar.
   axs[1, 0].legend()  # Grafikteki veri serisini açıklayan bir gösterge ekler.

    # Dördüncü grafik

   axs[1, 1].plot(x, y4, 'm-', marker='d', label='Veri 4')  # x ve y4 dizileri ile mor bir çizgi çizer. Veri noktalarını altıgen ile gösterir.
   axs[1, 1].set_title('Grafik 4')  # Grafiğin başlığını ayarlar.
   axs[1, 1].set_xlabel('X Ekseni')  # X ekseninin etiketini ayarlar.
   axs[1, 1].set_ylabel('Y Ekseni')  # Y ekseninin etiketini ayarlar.
   axs[1, 1].legend()  # Grafikteki veri serisini açıklayan bir gösterge ekler.


   # Grafiklerin düzenlenmesi

   plt.tight_layout()  # Grafiklerin düzenini otomatik olarak ayarlar, böylece başlıklar ve etiketler çakışmaz.
   plt.show()  # Tüm grafikleri ekranda gösterir.



Sütun Grafikleri (Bar Charts)
-------------------------------

Bu sefer `plt.bar()` kullanıyoruz. 

`plt.text()` fonksiyonu ile çubukların üstüne değerler yazıyoruz.

### Tek Kategorili Çubuk Grafiği

.. code-block:: python

   import matplotlib.pyplot as plt

   # Veriler
   kategoriler = ['A', 'B', 'C', 'D']
   degerler = [10, 15, 7, 12]

   # Tek kategorili çubuk grafiği
   plt.figure(figsize=(8, 5))  # Grafik boyutunu ayarla
   plt.bar(kategoriler, degerler, color='skyblue')  # Çubuk grafiği oluştur
   plt.title('Tek Kategorili Çubuk Grafiği')  # Başlık
   plt.xlabel('Kategoriler')  # X ekseni etiketi
   plt.ylabel('Değerler')  # Y ekseni etiketi

   # Değerleri çubukların üstüne yaz
   for i, v in enumerate(degerler):
       plt.text(i, v + 0.5, str(v), ha='center', color='black')

   plt.show()  # Grafiği göster

### İki Kategorili Çubuk Grafiği

.. code-block:: python

   import matplotlib.pyplot as plt

   # Veriler
   kategoriler = ['A', 'B', 'C', 'D']
   degerler = [10, 15, 7, 12]

   # İki kategorili çubuk grafiği
   plt.figure(figsize=(8, 5))  # Grafik boyutunu ayarla
   plt.bar(kategoriler, degerler, color='skyblue')  # Çubuk grafiği oluştur
   plt.title('İki Kategorili Çubuk Grafiği')  # Başlık
   plt.xlabel('Kategoriler')  # X ekseni etiketi
   plt.ylabel('Değerler')  # Y ekseni etiketi

   # Değerleri çubukların üstüne yaz
   for i, v in enumerate(degerler):
       plt.text(i, v + 0.5, str(v), ha='center', color='black')

   plt.show()  # Grafiği göster


Pasta Grafikleri (Pie Charts)
-------------------------------

.. code-block:: python

   import matplotlib.pyplot as plt

   # Veriler
   kategoriler = ['Elma', 'Muz', 'Portakal', 'Çilek']
   degerler = [30, 25, 20, 25]  # Her bir kategorinin oranları

   # Pasta grafiği
   plt.figure(figsize=(8, 6))  # Grafik boyutunu ayarla
   plt.pie(degerler, labels=kategoriler, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])  
   # autopct: dilimlerin yüzdesini gösterir, colors: dilimlerin renklerini ayarlar

   plt.title('Meyve Dağılımı')  # Başlık
   plt.axis('equal')  # Pastanın elips görünmesini engellemek için x ve y değerlerini eşit tutar.
   plt.show()  # Grafiği göster

Buradaki `autopct`, her dilimin yüzdesini gösterir. Örneğin `%1.1f%%` formatı, yüzdeleri bir ondalık basamakla gösterir. 25.0, 25.3 gibi yazılmasını sağlar.

Dağılım Grafiği (Scatter Plots)
---------------------------------

Aşağıda, bir dağılım grafiği oluşturmak için kullanılan bir örnek bulunmaktadır:

.. code-block:: python

   import matplotlib.pyplot as plt

   # Örnek veri
   x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # X değerleri
   y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Y değerleri
   sizes = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]  # Nokta boyutları
   colors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # Nokta renkleri

   plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
   plt.title('Dağılım Grafiği')
   plt.xlabel('X Değeri')
   plt.ylabel('Y Değeri')
   plt.colorbar(label='Renk Değeri')  # Renk çubuğu
   plt.show()


Histogramlar
------------

.. code-block:: python

   import matplotlib.pyplot as plt

   # Örnek veri
   data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 9, 10]  # Veriler

   plt.hist(data, bins=5, color='skyblue', edgecolor='black')  # Histogram oluştur
   plt.title('Histogram')
   plt.xlabel('Değerler')
   plt.ylabel('Frekans')
   plt.show()

Grafiklerin Özelleştirilmesi
----------------------------

Aşağıda grafiklerinize kendi isteklerinize göre dizayn etmek isterseniz kullanabileceğiniz kodları açıklamaları ile birlikte sıraladım.

.. code-block:: python

   import matplotlib.pyplot as plt

   # 1. Grafik Elemanları

   # Başlık Ekleme
   plt.title('Grafik Başlığı')  # Grafiğin üst kısmına başlık ekler.

   # Eksen Etiketleri Ekleme
   plt.xlabel('X Ekseni')  # X eksenine etiket ekler.
   plt.ylabel('Y Ekseni')  # Y eksenine etiket ekler.

   # Lejant Ekleme
   plt.legend(['Veri 1', 'Veri 2'])  # Grafikteki veri serilerini açıklayan bir gösterge ekler.

   # Yazı Tipi ve Boyut Ayarları
   plt.title('Grafik Başlığı', fontsize=14, fontweight='bold')  # Başlık için yazı tipi boyutu ve kalınlık ayarı.
   plt.xlabel('X Ekseni', fontsize=12)  # X ekseni etiketi için yazı tipi boyutu.
   plt.ylabel('Y Ekseni', fontsize=12)  # Y ekseni etiketi için yazı tipi boyutu.

   # Renk Ayarları
   plt.title('Grafik Başlığı', color='blue')  # Başlık rengini mavi yapar.

   # 2. Renkler ve Stiller

   # Yerleşik Renk Paletleri
   plt.plot(x, y, color='red')    # Kırmızı renk ile çizgi çizer.
   plt.plot(x, y, color='green')  # Yeşil renk ile çizgi çizer.

   # Özel Renk Kullanımı
   plt.plot(x, y, color='#FF5733')  # Hex kodu ile özel bir renk kullanır.

   # Stil Ayarları
   plt.style.use('ggplot')  # ggplot stilini kullanarak grafiğin görünümünü değiştirir.

   # 3. Alt Grafikler (Subplots)
   fig, axs = plt.subplots(2, 2)  # 2x2 düzeninde alt grafikler oluşturur.

   # Grid Tabanlı Düzenlemeler
   fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 düzen ve boyut ayarı.

   # 4. Özel Şekiller ve Anotasyonlar

   # Ok Ekleme
   plt.annotate('', xy=(x2, y2), xytext=(x1, y1),  # Okun uç noktaları
                arrowprops=dict(arrowstyle='->', color='black'))  # Okun stili ve rengi.

   # Metin Kutusu Ekleme
   plt.text(x, y, 'Metin Kutusu', fontsize=10, color='red')  # Belirtilen noktaya metin kutusu ekler.

   # İşaretleme Ekleme
   plt.scatter(x, y, color='blue', label='İşaretleme')  # Belirtilen noktalara işaretleme ekler.

Buradaki bazı değerleri kendi isteğinize göre değiştirebilirsiniz. Örneğin `plt.style.use('ggplot')` kısmında ggplot yerine “**fivethirtyeight**”, “dark_background” gibi farklı değerler girebilirsiniz.

Bu stiller arka plan rengi, çizgi rengi gibi değerleri değiştirerek farklı sonuçlar ortaya koyabilir. İyi bir görsellik isterseniz deneyerek kendinize uygun olanı seçebilirsiniz.


Canlı Grafik Oluşturmak
------------------------

Öncelikle `örnek.txt` adlı bir dosya oluşturalım. Örnek olarak bunu kullanabilirsiniz:

.. code-block:: text

   1,1
   2,2
   3,3
   4,4
   5,5
   6,6
   7,7

Ardından yazacağımız kod:

.. code-block:: python

   import matplotlib.pyplot as plt  # Grafik çizimi için matplotlib'in pyplot modülü
   import matplotlib.animation as animation  # Animasyon oluşturmak için matplotlib'in animation modülü
   from matplotlib.animation import FuncAnimation  # FuncAnimation sınıfını içe aktar
   from matplotlib import style  # Grafik stillerini kullanmak için

   # Grafik stilini ayarla
   style.use('fivethirtyeight')  # 'fivethirtyeight' stilini kullanarak grafiğin görünümünü ayarlıyoruz

   # Yeni bir figür oluştur
   fig = plt.figure()  # Grafik için bir figür nesnesi oluştur. fig değişkenini bize FuncAnimationa bir değer olarak gireceğimiz için gerekli.
   # Alt grafik (subplot) oluştur
   ax1 = fig.add_subplot(111)  # 1x1'lik bir ızgarada 1. alt grafiği oluştur

   # Animasyon için güncelleme fonksiyonu
   def animate(i):
       # 'örnek.txt' dosyasını oku
       graph_data = open('örnek.txt', 'r').read()  # Dosyayı okur ve içeriğini bir string olarak alır
       lines = graph_data.split('\n')  # Satırları ayırarak bir liste oluşturur
       xs = []  # X değerlerini saklamak için boş bir liste oluştur
       ys = []  # Y değerlerini saklamak için boş bir liste oluştur

       # Her bir satırı işle
       for line in lines:
           if len(line) > 1:  # Satırın boş olmadığından emin ol
               x, y = line.split(',')  # Satırı virgüle göre ayırarak x ve y değerlerini al
               xs.append(float(x))  # X değerini float tipine çevirip listeye ekle
               ys.append(float(y))  # Y değerini float tipine çevirip listeye ekle
       
       ax1.clear()  # Önceki verileri sil
       ax1.plot(xs, ys)  # Yeni X ve Y değerleri ile grafiği çiz

   # FuncAnimation ile animasyonu başlat
   ani = FuncAnimation(fig, animate, interval=1000)  # Her 1000 milisaniyede bir 'animate' fonksiyonunu çağırarak animasyonu oluştur

   # Grafiği göster
   plt.show()  # Grafiği ekranda göster

Grafiğimizin güncellendiğini görmek için `örnek.txt` dosyasına veri ekleyin. Örnek olarak `8,8` ekleyebilirsiniz. Ardından dosyayı kaydedin. Buradaki önemli nokta yeni veriyi bir alt satıra yazmanız çünkü yazdığımız kodda dosyadaki her satırı tek tek alıyoruz. Diğer dikkat etmeniz gereken ise virgül kullanmak; bu şekilde birinci veri x verisi, ikinci veri ise y verisi olarak algılanacak çünkü aynı satırdaki verileri virgüle göre ayırarak x ve y verisini alıyoruz. En son olarak dosyayı kaydetmeyi unutmayın.

CSV Dosyasındaki Verileri Görselleştirme
-----------------------------------------

Aşağıda, `örnek.txt` dosyasındaki verileri okuyarak bir çizgi grafiği oluşturmak için kullanılan bir örnek bulunmaktadır:

.. code-block:: python

   import matplotlib.pyplot as plt  
   import csv  # CSV dosyalarını okumak için csv kütüphanesini içe aktar.

   # Boş listeler oluştur, verileri saklamak için kullanılacak.
   x = []  
   y = []  

   # 'örnek.txt' dosyasını okuma modunda aç.
   with open('örnek.txt', 'r') as csvfile:
       # CSV dosyasını okuyacak bir nesne oluştur, virgül ile ayrılmış verileri işler.
       plots = csv.reader(csvfile, delimiter=',')
       
       # Her bir satır için döngü başlat.
       for row in plots:
           # Satırdaki ilk değeri (X) tam sayıya çevirip x listesine ekle.
           x.append(int(row[0]))
           # Satırdaki ikinci değeri (Y) tam sayıya çevirip y listesine ekle.
           y.append(int(row[1]))

   # X ve Y değerlerini kullanarak bir çizgi grafiği çiz.
   plt.plot(x, y, label='CSV Dosyasından Gelen Veriler')

   # X eksenine "x" etiketi ekle.
   plt.xlabel('x')
   # Y eksenine "y" etiketi ekle.
   plt.ylabel('y')
   # Grafikteki etiketleri göster.
   plt.legend()
   # Grafiği ekranda göster.
   plt.show()

İnternetten Veri Çekmek
------------------------

Ticker kelimesi şirketlerin borsadaki sembollerini belirtir. Örneğin bu Apple için ‘AAPL’, Tesla için ‘TSLA’ şeklindedir. Buradaki kullandığımız kütüphane yahoo finance tarafından geliştirlen yfinance kütüphanesi. Burada yahoo finance tarafından sağlanan API kullanılıyor bu bize hisseler ile alakalı sayısal değerleri verecek.

API nedir: API (Application Programming Interface), yazılımlar arasında iletişim ve veri alışverişi sağlamak için kullanılan bir arayüzdür. API'ler, bir uygulamanın veya hizmetin belirli işlevlerine ve verilerine erişim sağlamak için standart bir yöntem sunar.

.. code-block:: python

   import yfinance as yf  # yfinance kütüphanesini içe aktar
   import matplotlib.pyplot as plt  # matplotlib kütüphanesini içe aktar

   # Apple hisselerini (AAPL) tanımla
   apple = yf.Ticker("AAPL")

   # Hisse senedinin tarihsel verilerini al
   historical_data = apple.history(period="1mo")  # Son 1 ayın verilerini al

   # Kapanış fiyatlarını al
   closing_prices = historical_data['Close']

   # Grafiği çiz
   plt.figure(figsize=(10, 5))  # Grafik boyutunu ayarla
   plt.plot(closing_prices.index, closing_prices.values, label='AAPL Kapanış Fiyatı', color='blue')  # Kapanış fiyatlarını çiz
   plt.title('Apple Hisseleri Kapanış Fiyatları (Son 1 Ay)')  # Başlık
   plt.xlabel('Tarih')  # X ekseni etiketi
   plt.ylabel('Kapanış Fiyatı (USD)')  # Y ekseni etiketi
   plt.xticks(rotation=45)  # X eksenindeki tarih etiketlerini döndür
   plt.legend()  # Grafikteki etiketleri göster
   plt.grid()  # Izgara çizgilerini ekle
   plt.tight_layout()  # Grafik düzenini ayarla
   plt.show()  # Grafiği göster

Zamanın Uyarlanması
-------------------

`time.time()` Unix zaman damgası döndürür. Bu 1 Ocak 1970'den beri kaç saniye geçtiğini belirtir.

`fromtimestamp` metodu, bir zaman damgasını alarak ona karşılık gelen tarih ve saat bilgisini oluşturur. Yani, bir zaman damgasından (timestamp) tarih ve saat bilgisi elde etmek için kullanılır.

.. code-block:: python

   import datetime as dt
   import time 

   example = time.time()
   dt.datetime.fromtimestamp(example)

Bu iki satır numpy kullanarak unix değerlerle dolu olan dizimizi vektörleme yaparak bu dizideki her unixi tarih ay gün saate çeviriyoruz. Numpy kullanmadan önce terminalde şu kodu çalıştırıp numpy kütüphanesini yüklemeniz gerek:

.. code-block:: bash

   pip install numpy

.. code-block:: python

   dateconv = np.vectorize(dt.datetime.fromtimestamp)
   date = dateconv(date)

Numpy vektörleştirmeye bir örnek. Dizideki her sayının karesi alınır.

.. code-block:: python

   import numpy as np

   # Örnek bir fonksiyon
   def square(x):
       return x ** 2

   # Bir dizi oluştur
   array = np.array([1, 2, 3, 4, 5])

   # Fonksiyonu vektörleştir
   vectorized_square = np.vectorize(square)

   # Vektörleştirilmiş fonksiyonu diziye uygula
   squared_array = vectorized_square(array)

   print(squared_array)  # Çıktı: [ 1  4  9 16 25]

Mum Grafikleri
--------------

OHLC yani Open, High, Low, Close = Açılış, En Yüksek, En Düşük, Kapanış değerlerini kullanacağız. Genellikle finansal piyasalar için kullanılır.

Öncelikle gerekli kütüphaneleri yükleyin:

.. code-block:: bash

   pip install mplfinance
   pip install pandas

Aşağıda, OHLC grafiği oluşturmak için kullanılacak bir örnek bulunmaktadır:

.. code-block:: python

   import pandas as pd  # Pandas kütüphanesini veri analizi için içe aktar
   import mplfinance as mpf  # Mplfinance kütüphanesini finansal grafikler için içe aktar

   data = {
       'Date': [  # Tarihleri içeren bir liste
           '2023-01-01', '2023-01-02', '2023-01-03', 
           '2023-01-04', '2023-01-05', '2023-01-06', 
           '2023-01-07', '2023-01-08', '2023-01-09', 
           '2023-01-10'
       ],
       'Open': [100, 102, 101, 103, 105, 107, 106, 108, 110, 109],  # Açılış fiyatları
       'High': [102, 103, 102, 104, 106, 108, 107, 109, 111, 110],  # En yüksek fiyatlar
       'Low': [99, 100, 100, 101, 104, 105, 105, 107, 108, 107],  # En düşük fiyatlar
       'Close': [101, 101, 103, 105, 105, 107, 106, 108, 109, 108],  # Kapanış fiyatları
       'Volume': [1000, 1500, 1200, 1300, 1600, 1700, 1800, 1900, 2000, 2100]  # İşlem hacimleri
   }

   # DataFrame oluşturma
   df = pd.DataFrame(data)  # Sözlükten bir DataFrame oluştur

   # Tarih sütununu datetime formatına çevirme
   df['Date'] = pd.to_datetime(df['Date'])  # Tarihleri datetime formatına çevir
   df.set_index('Date', inplace=True)  # Tarih sütununu indeks olarak ayarla

   # OHLC grafiği çizme
   mpf.plot(df, type='candle', volume=True, title='OHLC Grafiği', style='charles')  # Mum çubuğu grafiği oluştur