.. meta::
   :description: Bu bölümde formları ve kalıp viewları öğreneceğiz.
   :keywords: form, forms,Django, generic views, kalıp view,
   
.. highlight:: python3

******************************
İLK DJANGO PROJENİ YAZ, part 4
******************************

Basit bir form yazalım
**********************

Hadi bir `<form>` etiketi içerecek şekilde anket detay 
şablonumuzu ("polls/detail.html") güncelleyelim::

    <h1>{{ question.question_text }}</h1>

    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

    <form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
    <input type="submit" value="Vote">
    </form>

Hızlı bir özet:

- Yukarıdaki şablon, her soru seçimi için bir radyo düğmesi görüntüler. 
  Her radyo düğmesinin değeri, ilişkili soru seçiminin ID'sidir. 
  Her radyo düğmesinin adı "choice" dır. Bunun anlamı, biri radyo 
  düğmelerinden birini seçip formu gönderdiğinde POST yöntemi ile şu veri 
  yollanır: `choice=#ID#`. Burada `ID` değeri seçilen butonun `id`'sidir. 
  HTML formları böyle çalışır.

- Formun `action` değerini `{% url 'polls:vote' question.id %}` olarak ayarladık. 
  ve `method="post"` ayarını da ekledik. `method="post"` yazmak çok önemli
  (Alternatifi: `method="get"`). Çünkü sunucu tarafıyla yapılan veri alışverişinin 
  yönteminini belirler. Bir veri alışverişi yapan bir form oluşturduğunda 
  hep `method="post"` kullan.Bu Django'ya özel bir durum değil, iyi bir Web 
  geliştirme yöntemi.

- `forloop.counter` değişkeni içinde bulunduğu `for` döngüsünün kaç kez 
  döndüğünü tutar.

- Bir POST formu oluşturduğumuzdan (bu verileri değiştirme etkisi 
  yapabilir), Siteler Arası İstek Sahteciliği (Cross Site Request Forgeries) 
  konusunda endişelenmemiz gerekir. Neyse ki, çok fazla endişelenmenize gerek yok, 
  çünkü Django buna karşı korumak için kullanımı kolay bir sistemle 
  birlikte geliyor.Kısacası, dahili URL’leri hedef alan tüm POST formları, 
  `{% csrf_token%}` şablon etiketini kullanmalıdır.

Şimdi, gönderilen verileri işleyen ve onunla bir şeyler yapan bir Django 
viewı oluşturalım. Hatırla, part 3'te anket uygulaması için bu 
satırı içeren bir URLconf oluşturduk::

    path('<int:question_id>/vote/', views.vote, name='vote'),

Ayrıca göstermelik bir `vote` viewı yazmıştık. Hadi gerçek bir viewa 
çevirelim::

    from django.http import HttpResponse, HttpResponseRedirect
    from django.shortcuts import get_object_or_404, render
    from django.urls import reverse

    from .models import Choice, Question
    # ...
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Soru oylama formunu tekrar göster
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # POST verileriyle başarılı bir şekilde ilgilendikten sonra 
            # daima bir HttpResponseRedirect döndürün. Bu, bir kullanıcı
            # geri düğmesine basarsa verilerin iki kez gönderilmesini önler.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


Bu kod, henüz görmediğimiz bazı şeyleri içeriyor:

- `request.POST`, gönderilen verilere anahtar adına göre erişmenizi sağlayan, 
  sözlük benzeri bir nesnedir. Bu durumda, `request.POST['choice']` seçilen seçeneğin kimliğini 
  bir karakter dizisi olarak döndürür. `request.POST` değerleri her zaman 
  karakter dizisidir.

.. Note:: Django’nun GET verilerine aynı şekilde erişmek için de 
    `request.GET` sağladığını unutmayın. Ancak verilerin yalnızca 
    bir POST çağrısı yoluyla değiştirilmesini sağlamak için kodumda 
    `request.POST` açıkça kullanıyoruz.

- POST verilerinde seçim yapılmadıysa, `request.POST['choice']` `KeyError` hatası 
  verir. Yukarıdaki kod `KeyError`'u kontrol eder ve seçim yapılmadığı takdirde 
  soru formunu hata mesajı ile yeniden görüntüler.

- Seçim sayısını artırdıktan sonra, kod normal bir `HttpResponse` yerine bir 
  `HttpResponseRedirect` döndürür. `HttpResponseRedirect` tek bir argüman alır: 
  kullanıcının yönlendirileceği URL.

- Bu örnekte `HttpResponseRedirect` yapıcısında `reverse` fonksiyonunu 
  kullanıyoruz. Bu fonksiyon, görüntüleme işinde bir URL'yi sabit olmaktan 
  kurtarmanıza yardımcı olur. Çalıştırmak istediğimiz viewın adı ve bu 
  viewa işaret eden URL modelinin değişken kısmı verilir. Bu durumda, 
  part 3'te kurduğumuz URLconf'u kullanarak, bu `reverse` çağrısı bir karakter 
  dizisi döndürür. Bunun gibi::

    '/polls/3/results/'

Burada `3` `question.id` değeridir. Bu yeniden yönlendirilen URL daha sonra 
son sayfayı görüntülemek için 'results' viewını çağırır.

Birisi bir soruya oy verdikten sonra, `vote` viewı sorunun sonuç sayfasına 
yönlendirir. Bu görünümü yazalım::

    from django.shortcuts import get_object_or_404, render


    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})

Bu part 3'te yazdığımız `detail` viewıyla hemen hemen aynı. 
Tek fark şablon adı. Bu gereksizliği daha sonra düzeltiriz.

Şimdi **polls/results.html** şablonunu oluşturalım::

    <h1>{{ question.question_text }}</h1>

    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
    {% endfor %}
    </ul>

    <a href="{% url 'polls:detail' question.id %}">Vote again?</a>

Şimdi tarayıcında `/polls/1/` adresine git ve soruyu oyla. Her oy verdiğinizde 
güncellenen bir sonuç sayfası görmelisiniz. Bir seçim yapmadan formu 
gönderirseniz, hata mesajını görmelisiniz.

Kalıp viewlar kullanalım
************************

`detail` ve `results` viewları çok basitve biraz da gereksizler. Anketlerin 
listesini görüntüleyen index() viewı da onlara benzer bir viewdır.

Bu viewlar, temel bir Web geliştirme durumunu gösterir: Veritabanından 
URL'deki parametreye göre veri almak, şablon yüklemek ve işlenmiş şablonu 
döndürmek. Bu çok yaygın olduğu için Django "Kalıp view" adında bir kolaylık 
sağlar.

Kalıp viewlar, bir uygulama yazmak için Python kodunu yazmanız gerekmediği 
noktaya ortak kalıpları soyutlar.

Kalıp view sistemini kullanmak için anket uygulamamızı düzenleyelim. 
Böylece gereksiz bir takım kodu silebiliriz. Düzenlememizde şu 
adımları uygulayacağız:

    #. URLconf'u değiştir.
    #. Gereksiz viewlardan bazılarını sil.
    #. Django'nun kalıp viewlarını temel alan yeni viewlar yaz.

URLconf'u değiştir
==================

İlk önce, **polls/urls.py** dosyasını açın ve `URLconf`'u şöyle değiştirin::

    from django.urls import path

    from . import views

    app_name = 'polls'
    urlpatterns = [
        path ( '' , views . IndexView . as_view (), name = 'index' ),
        path ( '<int:pk>/' , views . DetailView . as_view (), name = 'detail' ),
        path ( '<int:pk>/results/' , views . ResultsView . as_view (), name = 'results' ),
        path ( '<int:question_id>/vote/' , views . vote , name = 'vote' ),
    ]


İkinci ve üçüncü desenlerin yol dizilerinde eşleşen kalıbın adının 
`<question_id>`'den `<pk>`'ye değiştiğini

Görünümleri değiştir
====================

Şimdi `index`,`detail` ve `results` viewlarını kaldıracağız ve Django’nun 
kalıp viewlarını kullanacağız. Bunu yapmak için **polls/views.py** 
dosyasını aç ve buna benzer şekilde değiştir::

    from django.http import HttpResponseRedirect
    from django.shortcuts import get_object_or_404, render
    from django.urls import reverse
    from django.views import generic

    from .models import Choice, Question


    class IndexView(generic.ListView):
        template_name = 'polls/index.html'
        context_object_name = 'latest_question_list'

        def get_queryset(self):
            """Return the last five published questions."""
            return Question.objects.order_by('-pub_date')[:5]


    class DetailView(generic.DetailView):
        model = Question
        template_name = 'polls/detail.html'


    class ResultsView(generic.DetailView):
        model = Question
        template_name = 'polls/results.html'


    def vote(request, question_id):
        ... # yukarıdakiyle aynı, hiçbir değişiklik yok.

Burada iki kalıp view kullanıyoruz: `ListView` ve `DetailView`. `ListView` 
nesnelerin listesini gösterir. `DetailView` ise belirli bir nesne türünün 
detay sayfasını gösterir.

- Her kalıp viewın hangi modele etki edeceğini bilmesi gerekir. Bu model 
  özniteliği kullanılarak sağlanır.

- DetailView kalıp viewı, URL'den yakalanan birincil anahtar değerinin 
  `pk` olarak adlandırılmasını bekler. Bu nedenle kalıp viewlar için 
  `question_id` ifadesini `pk` olarak değiştirdik.

Varsayılan olarak, DetailView kalıp viewı 
`<app name>/<model name>_detail.html` adlı bir şablon kullanır. Bizim 
durumumuzda **polls/question_detail.html** şablonunu kullanırdı. 
`template_name` özelliği, Django'ya otomatik olarak oluşturulan varsayılan 
şablon adı yerine belirli bir şablon adı kullanmasını bildirmek için 
kullanılır. Bu, `results` viewının ve `detail` viewının, her ikisi de 
sahne arkasındaki DetailView olsa bile, farklı bir şablona sahip olmasını 
sağlar.

Durum `ListView` ve `IndexView` için de aynı.

Sunucuyu çalıştırın ve kalıp viewları temel alan yeni anket uygulamanı dene.
