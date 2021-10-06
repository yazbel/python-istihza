.. meta::
   :description: Bu bölümde içerik işlemcileri konusunu inceleyeceğiz.
   :keywords: python, python3, django, içerik işlemcileri


==================
İçerik İşlemcileri
==================

------------------------
İçerik İşlemcileri Nedir
------------------------

Dilden bağımsız olarak yazdığımız her uygulama DRY (Don't Repeat Yourself, Kendini Tekrar Etme) ilkesine sahip olmalıdır.
Bu sayede yazılan kodların okunabilirliği daha yüksek, fazlalıkları ve karmaşıklıkları daha az olur.

Django yazılım iskeletinde içerik işlemcileri bu işe yarar. Bir kere tanımlanan değişken o proje içinde
oluşturulan tüm uygulamalarda kullanılabilir.

Oluşturduğumuz her içerik işlemcisi bir `anahtar(lar)-değer(ler)` şeklinde dönmelidir. Bu değer tipi Python dilinin
sahip olduğu veri tipi olan `sözlük`\ tür.

-------------------------------------
İçerik İşlemcileri Nasıl Oluşturulur?
-------------------------------------

Öncelikle bir Django projesi ve projemiz için bir uygulama oluşturuyoruz. Oluşturduğumuz uygulamanın içine `context_processors.py`
isimli bir dosya oluşturuyoruz. Bundan sonra oluşturduğumuz tüm içerik işleyicilerini bu dosya altında toplayacağız. Son olarak oluşturduğumuz `context_processors.py` dosyasını
`settings.py` dosyasının altında projemize bildirmemiz gerekir. Bunun için `settings.py` dosyasını açıp

.. code-block:: python

    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]

bu kısmı buluyoruz. Ardından kendi oluşturacağımız içerik işleyicilerini diğerlerinin yanına ekliyoruz. Bu ekleme sırasında sözdizimi önemlidir ve bu şekilde olmalıdır.
`uygulama_adi.içerik_işlemcisi_dosya_adi.içerik_işlemcisi_adi`
Yeni hali aşağıdaki gibi olmalı.

.. code-block:: python


    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'deneme.context_processors.ilk_islec',
            ],
        },
    },
    ]


İlk işlecimiz basit olması amacıyla isim ve ülke döndürsün. Bunun için `context_processors.py` ve ilk işlecimizi yazalım. Yazacağımız işleçler fonksiyon şeklinde olmalıdır ve bu fonksiyon `request` parametresini dışarıdan almalıdır.


.. code-block:: python

    def ilk_islec(request):
        isim = "Mehmet"
        ulke = "Türkiye"

        return {'isim': isim, 'ulke': ulke}


Bu şekilde ilk işlecimizi yazdık şimdi `isim` ve `ulke` adında iki tane anahtar değer döndürdük. Bu değerleri istediğimiz HTML sayfasında kullanabiliriz.
Denemek için `templates` klasörü altında `index.html` oluşturalım ardından HTML dosyasmıza aşağıdaki kodu yazalım.

.. code-block:: python

    <!DOCTYPE html>
    <html>
    <head>
        <title>Django - İçerik İşlemcileri</title>
    </head>
    <body>

    <p>Merhaba, benim adım {{ isim }} ve şu an bu ülkedeyim: {{ ulke }} </p>

    </body>
    </html>

HTML sayfasımızı oluşturduktan
sonra view oluşturacağız. Bunun için oluşturduğumuz uygulamanın alt dizininde bulunan `views.py` dosyasına

.. code-block:: python

    from django.shortcuts import render

    def view(request):
        return render(request, 'index.html')

Şeklinde basit bir view fonksiyonu ekleyelim. Son olarak `urls.py` dosyasına yazdığımız view için URL yolu ekleyeceğiz.

.. code-block:: python

    from django.urls import path
    from deneme.views import view

    urlpatterns = [
        path('index', view),
    ]

Tüm yapacağımız bu kadar! Artık tarayıcıda oluşturduğumuz sayfayı çalıştırınca anahtarlarımızın yerinde değişkenlerimiz var.

--------------------------------------------
İçerik İşlemcileri Nerelerde Kullanılabilir?
--------------------------------------------

Django ile proje geliştirirken kullanıcının tarayıcıda göreceği HTML kısımlarını ortak olan kısımlarını tek bir noktadan
çekebiliriz. Böylece ortak bir blok değiştiği zaman tüm sayfaları tekrar düzeltmeye gerek kalmaz. Bunu yapmak için oluşturduğumuz tüm view'lere
ana tema blogumuzu, tüm sayfalarda ortak olan diğer blok parçalarının yollarını içerik işlecinde tanımlayabiliriz.

İçerik İşlemcimiz:

.. code-block:: python

    def template_path(request):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    components_dir = os.path.join(base_dir, 'templates/components/')
    base_component = os.path.join(components_dir, 'base_components/base.html')
    common_components = os.path.join(components_dir, 'common_components/')
    archive = os.path.join(common_components, 'archive.html')
    quick_links = os.path.join(common_components, 'quick_links.html')
    search_not_found = os.path.join(common_components, 'search_not_found.html')
    social_account = os.path.join(common_components, 'social_account.html')
    tag_cloud = os.path.join(common_components, 'tag_cloud.html')
    blockquote = os.path.join(common_components, 'blockquote.html')

    return {'base_components': base_component, 'archive': archive, 'quick_links': quick_links,
            'search_not_found': search_not_found, 'social_account': social_account, 'tag_cloud': tag_cloud,
            'blockquote': blockquote}

HTML Sayfamız::

    {% extends base_components %}
    {% block title %}İletişime Geç {% endblock %}
    {% block s_content %}
        <!-- s-content
        ================================================== -->
        <section class="s-content s-content--narrow">
            <div class="row">
                <div class="s-content__header col-full">
                    <h1 class="s-content__header-title">
                        İletişime Geç </h1>
                </div> <!-- end s-content__header -->
                <div class="col-full s-content__main">
                    <h3>Merhaba De :)</h3>
                    <p class="lead">Sosyal medya hesapları üzerinden bana ulaşabilirsin. </p>
                    <ul class="s-content__author-social" style="display: flex; justify-content: center">
                        {% for i in social %}
                            <li>
                                <a href="{{ i.sm_url }}" target="_blank"><i class="{{ i.sm_icon_class }}"
                                                                            style="font-size: 48px"
                                                                            aria-hidden="true"></i></a>
                            </li>
                        {% endfor %}
                    </ul>
                </div> <!-- end s-content__main -->
            </div> <!-- end row -->
        </section> <!-- s-content -->
        <{% endblock %}


Örnek HTML sayfamızda `{% extends base_components %}` ile `base_components` değişkenini içerik işlemcisinde tanımlamıştık, bu sayede bir daha
dosya adresini yazmamıza gerek kalmaz. Bunun yerine her view'de dosya yolunu yazabilirdik ancak dosyamızın yolu değişirse tüm view fonksiyonlarında
dosya yolunu değiştirmek zorunda kalacaktık.

Genel olarak kullanım şekli böyle oluyor.

Bu makale için hazırladığım koda `bu adres`_  üzerinden ulaşabilir, bu kodu detaylı olarak inceleyebilirsiniz.

.. _bu adres: https://github.com/mehmetkiran/context_processors_django
