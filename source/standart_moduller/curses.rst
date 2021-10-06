.. meta::
   :description: Bu bölümde curses modülünü inceleyeceğiz.
   :keywords: python, modül, import, curses

.. highlight:: python3

*************
curses Modülü
*************

curses Nedir?
=============

Curses kütüphanesi, metin tabanlı terminaller için terminalden bağımsız bir ekran boyama ve klavye kullanımı kolaylığı sağlar. Bu tip terminaller, VT100s, Linux konsolu ve çeşitli programlar tarafından simüle edilmiş terminallerdir. Ekran terminalleri imleci hareket ettirmek, ekranı kaydırmak ve alanları silmek gibi bazı genel işlemleri yapabilmek için çeşitli kontrol kodlarını destekler. Farklı terminaller geniş ölçüde değişik kodlar kullanırlar ve genellikle kendi küçük tuhaflıkları vardır.

Curses kütüphanesi oldukça temel işlevsellikler sunar, programcıya, örtüşmeyen çoklu metin pencerelerini içeren ekranların soyutlanmasını sağlar. Bir pencerenin içerikleri çeşitli şekillerde değişebilir - bir metin girme, bu metni silme, bu metnin görüntüsünü değiştirme - ve Curses kütüphanesi doğru çıktıyı oluşturabilmek için terminale hangi kontrol kodlarının gönderilmesi gerektiğini çözer. Curses; düğmeler, onay kutuları, veya diyaloglar gibi kullanıcı arayüzü konseptleri sağlamaz; eğer bu gibi özelliklere ihtiyacınız varsa, Urwid gibi bir kullanıcı arayüzü kütüphanesini kullanmayı düşünün.

Curses kütüphanesi ilk olarak BSD Unix için yazılmıştır; AT&T'nin Unix'in sonraki System V sürümleri için bir çok geliştirme ve yeni işlev eklendi. BSD curses artık muhafaza edilmiyor, AT&T'nin açık kaynak uygulama arayüzü olan ncurses onun yerine getirildi. Eğer Linux veya FreeBSD gibi açık kaynak Unix kullanıyorsanız, sisteminiz neredeyse kesinlikle ncurses kullanıyor demektir. Madem hali hazırdaki bir çok ticari Unix sürümü System V kodu üzerine temellenmiş, burada bahsedilen bütün işlevler büyük olasılıkla kullanılabilir olacaktır. Bazı tescilli Unixlerin taşıdığı eski curses sürümleri her özelliği desteklemeyebilir.

Python Curses Modülü
=====================

Python modülü, curses tarafından sağlanan C işlevleri üzerinde basit bir sarıcıdır; eğer C'de curses programlamaya zaten aşinaysanız, bu bilgiyi Python'a taşımak gerçekten kolaydır. En büyük fark, Python arayüzeyinin `addstr()`, `mvaddstr()` ve `mvwaddstr()` gibi değişik C işlevlerini tek bir `addstr()` metodunda birleştirerek işleri daha kolay yoldan halletmesidir. Bunu birazdan biraz daha ayrıntılı bir şekilde göreceğiz.


Bir Curses Uygulamasını Başlatma ve Sonlandırma
================================================

Curses ile bir şey yapmadan önce, curses ilklendirilmelidir. Bu ilklendirme işlemi `initscr()` işlevini çağırarak yapılır. Bu işlev terminal tipini belirler, gerekli bütün kurulum kodlarını terminale gönderir ve çeşitli iç veri yapılarını oluşturur. Eğer başarılı olursa, `initscr()` tüm ekranı temsil eden bir pencere geri döndürür; bu ekrana genellikle C değişkenine karşılık gelen isimden sonra stdscr ismi verilmiştir::

    import curses
    stdscr = curses.initscr()

Genellikle curses uygulamaları tuşları okuyabilmek ve onları sadece belli koşullar altında görüntüleyebilmek için tuşların ekranda otomatik olarak yansımasını devre dışı bırakır. Bunun için `noecho()` işlevini çağırmak gerekir::

    curses.noecho()

Uygulamaların , Enter tuşuna basılmasına ihtiyaç duyulmadan, anında tuşlara tepki vermesi gerekecektir; buna cbreak modu denir, ve tampon girdi moduna zıttır::

    curses.cbreak()

Terminaller genellikle imleç tuşları veya Page Up ve Home gibi gezinme tuşlarını çoklu kaçış dizisi olarak geri dönderir. Uygulamanızı bazı serileri beklemek ve buna göre işlemek için yazabilecekken, curses bunu sizin yapar; `curses.KEY_LEFT` gibi bir özel karakteri geri dönderir. Curses'in bu işlemi yapabilmesi için keypad modunu aktif hale getirmelisiniz::

    stdscr.keypad(True)

Bir curses uygulamasını sonlandırmak yeni bir tanesini başlatmaktan çok daha kolaydır. Aşağıdakileri, curses'e uygun hale getirilmiş terminal ayarlarını tersine çevirmek için çağırmanız gerekebilir::

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

Ardından terminalin ilk işletim modunu yüklemek için `endwin()`'i çağırın::

    curses.endwin()

Şimdi yavaş yavaş örnekler üzerinde curses modülünü daha iyi anlamaya çalışalım.

Örnekler:
=========


Örnek-1:
=========

Ekranın ortasına bir “hello world!” yazısı yerleştirelim.


**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses

    ekran = curses.initscr()
    boyutlar = ekran.getmaxyx()
    ekran.addstr(int(boyutlar[0]/2), int(boyutlar[1]/2 - 6), "hello world!",
                 curses.A_BOLD)
    ekran.refresh()
    ekran.getch()
    curses.endwin()

**Kodların Açıklamaları:**

Önce gerekli modül programın içine aktarılır::

    import curses

Curses ile işlem yapmadan önce mutlaka ekranın tanıtılması gerekiyor::

    ekran = curses.initscr()

Yazıyı ekrana yerleştirmek için satır ve sütun numaralarını yazabileceğimiz gibi, Terminal ekran boyutunun ölçülerini referans alarak bazı özel durumlarda ne yapılması gerektiğini belirtebiliriz::

    boyutlar = ekran.getmaxyx()

Diyelim yazıyı terminal ekranının tam ortasına yerleştirmek istiyoruz, o zaman sütun ve satır parametrelerine ekran ölçülerinin yarısını değer olarak verebiliriz. Ancak *"hello world!"*
ifadesi 12 karakterden oluştuğu için, bu karakter uzunluğunun yarısını satır değerinden çıkarırız::

    ekran.addstr(int(boyutlar[0]/2), int(boyutlar[1]/2 - 6), "hello world!",
                 curses.A_BOLD)

Ekranı tazeleyelim::

    ekran.refresh()

Karakterleri yakalayalım::

    ekran.getch()

Herhangi bir tuşa basılınca ekran sonlansın::

    curses.endwin()

Örnek-2:
=========

Sürekli y ekseninin ortasında bulunan ama x ekseni boyunca hareket eden bir “hello world!” yazısı oluşturalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time

    ekran = curses.initscr()
    boyutlar = ekran.getmaxyx()
    for i in range(boyutlar[1] - len("hello world!")):
        ekran.clear()
        ekran.addstr(int(boyutlar[0]/2), i, "hello world!", curses.A_BOLD)
        ekran.refresh()
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Modülleri programın içine aktaralım::

    import curses
    import time

Her zamanki gibi önce ekran tanıtılır::

    ekran = curses.initscr()

Yine ekranımızın maksimum boyutlarını tanımlayalım::

    boyutlar = ekran.getmaxyx()

Yazının terminal ekranında, bir animasyon gibi hareket etmesini istiyorsak, bir for döngüsü içinde sütun ve satırları anlık olarak değiştirebiliriz::

    for i in range(boyutlar[1] - len("hello world!")):

Ekranı temizleyelim::

        ekran.clear()

Sürekli y ekseninin ortasında olan ve x ekseninin i parametresine göre değişen *"hello world!"* yazısını kalın harflerle ekrana hareketli bir şekilde bastıralım::

        ekran.addstr(int(boyutlar[0]/2), i, "hello world!", curses.A_BOLD)

Ekranı tazeleyelim::

        ekran.refresh()

`time.sleep()` fonksiyonunu tanımlamadığınızda ne olacağını görmek için fonksiyonu yoruma alın::

        time.sleep(0.05)

Ve programdan terminali eski haline getirecek şekilde çıkalım::

    curses.endwin()

Örnek-3:
=========


x ve y eksenleri boyunca hareket eden bir “hello world!” yazısı oluşturalım. Dilerseniz bu uygulamayı bir ekran koruyucu olarak da kullanabilirsiniz.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time

    ekran = curses.initscr()
    boyutlar = ekran.getmaxyx()
    ekran.nodelay(1)
    q = -1
    x, y = 0, 0
    dusey, yatay = 1, 1
    while q < 0:
        ekran.clear()
        ekran.addstr(y, x, "hello world!", curses.A_BOLD)
        ekran.refresh()
        y += dusey
        x += yatay
        if y == boyutlar[0] - 1:
            dusey = -1
        elif y == 0:
            dusey = 1
        if x == boyutlar[1] - len("hello world!") - 1:
            yatay = -1
        elif x == 0:
            yatay = 1
        q = ekran.getch()
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Bu örnekte kullanacağımız gerekli modülleri programın içine aktaralım::

    import curses
    import time

Her zamanki gibi önce ekranı tanıtalım::

    ekran = curses.initscr()

Ekranın maksimum boyutlarını alalım::

    boyutlar = ekran.getmaxyx()

`nodelay()`'in parametresi *1 (True)* olursa yazımız ekranda hareket edebilir, *0 (False)* olursa da yazı sabit bir şekilde durur::

    ekran.nodelay(1)

Döngü değişkenini tanımlıyoruz. Bu değişken basılan her tuşu temsil edecek. Böylece herhangi bir tuşa bastığımızda programdan çıkabiliriz::

    q = -1

Döngüyle birlikte değişecek olan ekran satır ve sütun değerlerini ilk etapta 0 olarak belirliyoruz::

    x, y = 0, 0

Satır ve sütunların değerleri, biri düşey diğeri yataya müdahele edecek değişkenlere göre değiştirilecek. Bu yüzden *dusey* ve *yatay* isminde iki tane değişken oluşturalım::

    dusey, yatay = 1, 1

Şimdi döngümüzü oluşturmaya geçelim::

    while q < 0:

Döngü her başa sardığında ekran temizlensin::

        ekran.clear()

Ekrandaki yazı hep kalın harflerle *"hello world!"* yazısı olsun::

        ekran.addstr(y, x, "hello world!", curses.A_BOLD)

Ekranı tazeleyelim::

        ekran.refresh()

Döngüyle birlikte *x* ve *y*'nin değerleri *dusey* ve *yatay* değişkenlerine göre arttırılır::

        y += dusey
        x += yatay

Şayet *y* maksimum değerine ulaşırsa, *dusey* değişkeni -1'e eşitlenir. Böylece negatif y yönünde hareket edebiliriz::

        if y == boyutlar[0] - 1:
            dusey = -1

Şayet *y* minimum değerine ulaşırsa, *dusey*' değişkeni 1'e eşitlenir. Böylece pozitif y yönünde hareket edebiliriz::

        elif y == 0:
            dusey = 1

Şayet *x* maksimum değerine ulaşırsa, *yatay* değişkeni -1'e eşitlenir. Böylece negatif x yönünde hareket edebiliriz::

        if x == boyutlar[1] - len("hello world!") - 1:
            yatay = -1

Şayet *x* minimum değerine ulaşırsa, *yatay* değişkeni 1'e eşitlenir. Böylece pozitif x yönünde hareket edebiliriz::

        elif x == 0:
            yatay = 1

Ekranda bir tuşa bastığımız zaman programdan çıkabilmemiz için, *q* değişkeninin bütün harfleri temsil etmesini sağlayalım::

        q = ekran.getch()

Ekrandaki yazının hareketliliği `time.sleep()` fonksiyonu ile biraz azaltalım::

        time.sleep(0.05)

Ve normal terminal ekranına geri dönelim::

    curses.endwin()

Örnek-4
========

'asdw' tuşlarıyla hareket eden bir "hello world!" yazısı oluşturalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time

    ekran = curses.initscr()
    curses.noecho()
    boyutlar = ekran.getmaxyx()
    ekran.nodelay(1)
    q = -1
    x, y = 0, 0
    while q != ord("q"):
        ekran.clear()
        ekran.addstr(y, x, "hello world!", curses.A_BOLD)
        ekran.refresh()
        q = ekran.getch()
        if q == ord("w") and y > 0:
            y -= 1
        elif q == ord("s") and y < boyutlar[0] - 1:
            y += 1
        elif q == ord("a") and x > 0:
            x -= 1
        elif q == ord("d") and x < boyutlar[1] - len("hello world!") - 1:
            x += 1
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Bu örnekte kullanacağımız modülleri içe aktaralım::

    import curses
    import time

Yine her zamanki gibi önce ekranı oluşturalım::

    ekran = curses.initscr()

Bastığımız tuş ekrana yansımasın diye, `curses.noecho()` fonksiyonunu kullanacağız. Farkı görmek için bu fonksiyonu yoruma alın::

    curses.noecho()

Yine ekran boyutlarını alalım::

    boyutlar = ekran.getmaxyx()

Hareketi sağlamak için `nodelay()` fonksiyonunun değerini 1 olarak ayarlayalım::

    ekran.nodelay(1)

Her tuşu temsil edecek olan *q* değişkenimizi tanımlayalım::

    q = -1

Bu sefer ekrandaki yazının değişen konumlarını *x* ve *y* değerlerine göre belirleyelim. Başlangıç
değerlerini 0, 0 yazıyoruz::

    x, y = 0, 0

Şimdi döngümüzü oluşturmaya geçelim. *q* tuşuna basılmadığı sürece döngü devam etsin::

    while q != ord("q"):

Döngü her başa sardığında `clear()` ile yine ekranı temizleyelim::

        ekran.clear()

Ekranın y, x konumuna "hello world!" stringini kalın harfli olacak şekilde ekleyelim::

        ekran.addstr(y, x, "hello world!", curses.A_BOLD)

Ekranı tazeleyelim::

        ekran.refresh()

*q* tuşunun bütün tuşları temsil etmesini sağlayalım::

        q = ekran.getch()

Şayet kullanıcı *w* tuşuna basarsa ve *y*'nin değeri 0'dan büyükse, *y*'nin değeri 1 birim azalsın::

        if q == ord("w") and y > 0:
            y -= 1

Şayet kullanıcı *s* tuşuna basarsa ve *y*'nin değeri maksimum değerinden küçükse, *y*'nin değeri 1 birim arttırılsın::

        elif q == ord("s") and y < boyutlar[0] - 1:
            y += 1

Şayet kullanıcı *a* tuşuna basarsa ve *x*'in değeri 0'dan büyükse, *x*'in değeri 1 birim azalsın::

        elif q == ord("a") and x > 0:
            x -= 1

Şayet kulanıcı *d* tuşuna basarsa ve *x*'in değeri maksimum değerinden küçükse; *x*'in değeri 1 birim arttırılsın::

        elif q == ord("d") and x < boyutlar[1] - len("hello world!") - 1:
            x += 1

`time.sleep()`'i niye kullandığımızı merak ediyorsanız, bu kodu yoruma ekleyin ve farkı gözlemleyin::

        time.sleep(0.05)

Ve bizi programdan terminali bozmadan çıkaracak olan komutu yazmayı unutmuyoruz::

    curses.endwin()

Örnek-5:
=========

"asdw" tuşlarıyla hareket eden ve "1, 2, 3" tuşlarıyla renk değiştiren bir "hello world!" yazısı oluşturalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time

    ekran = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    boyutlar = ekran.getmaxyx()
    ekran.nodelay(1)
    g = 1
    q = -1
    x, y = 0, 0
    while q != ord("q"):
        ekran.clear()
        ekran.addstr(y, x, "hello world!", curses.color_pair(g))
        ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)
        ekran.refresh()
        q = ekran.getch()
        if q in range(49, 52):
            g = int(chr(q))
        if q == ord("w") and y > 0:
            y -= 1
        elif q == ord("s") and y < boyutlar[0] - 1:
            if y == boyutlar[0] - 2 and x == boyutlar[1] - \
                    len("hello world!"):
                pass
            else:
                y += 1
        elif q == ord("a") and x > 0:
            x -= 1
        elif q == ord("d") and x < boyutlar[1] - len("hello world!"):
            if y == boyutlar[0] - 1 and x == boyutlar[1] - \
                    len("hello world!") - 1:
                pass
            else:
                x += 1
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Her zamanki gibi kullanacağımız modülleri programın içine aktaralım::

    import curses
    import time

Yine önce ekranı tanımlıyoruz::

    ekran = curses.initscr()

Herhangi bir renklendirme işlemine geçmeden önce renklendirmeyi başlatmamız gerekiyor::

    curses.start_color()

Şimdi renk çiftlerini sıralarını belirterek oluşturmaya geçebiliriz::

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

Yine bastığımız herhangi bir tuş ekranda yansıma oluşturmasın::

    curses.noecho()

Maksimum ekran boyutlarını bir değişkene kaydedelim::

    boyutlar = ekran.getmaxyx()

Yine ekrandaki harekette bir gecikme olmaması için `nodelay()`'in parametresini 1 olarak ayarlıyoruz::

    ekran.nodelay(1)

Yukarıda tanımladığımız renk çiftlerini kullanabilmek için bir değişken tanımlayalım. Bu değişken sayesinde renk çiftlerine, sıra numarası sayesinde erişebileceğiz::

    g = 1

Şimdi de her zamanki gibi her tuşu temsil edecek *q* değişkenimizi tanımlayalım::

    q = -1

Ekrana yazıyı yine *x* ve *y* değerlerine göre yerleştireceğiz. 0'a 0 *"hello world!"* yazısının başlangıç değerleri olsun::

    x, y = 0, 0

Döngümüzü tanımlayalım. Döngü *q* tuşuna basılmadığı sürece devam etsin::

    while q != ord("q"):

Her zamanki gibi ekranımızı tamamen temizleyelim::

        ekran.clear()

Ekranın *y* ve *x* konumuna *"hello world!"* yazısını yerleştirelim. Aşağıdaki `curses.color_pair(g)`'deki *g* birazdan tanımlayacağımız tuşlara bastığımızda renk değiştirmeye yarayacak::

        ekran.addstr(y, x, "hello world!", curses.color_pair(g))

İmleci ekranın en sonuna götürelim. Bu fonksiyonu kullanmadığımız zaman oluşacak olan farkı görebilmek için fonksiyonu yoruma alın::

        ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)

Ekranı tazeleyelim::

        ekran.refresh()

*q* bütün tuşları temsil ediyor olsun::

        q = ekran.getch()

`chr(49)`'dan `chr(52)`'ye kadar olan karakterler 1, 2 ve 3'tür. Şayet kullanıcı bu tuşlara basarsa *g* değişkeni değişecek ve böylece *"hello world!"* yazımız farklı renklere sahip olacak::

        if q in range(49, 52):
            g = int(chr(q))

Şayet kullanıcı *w* tuşuna basarsa ve *y*'nin değeri 0'dan büyükse, *y* değişkeninin değeri 1 birim azalsın::

        if q == ord("w") and y > 0:
            y -= 1

Şayet kullanıcı *s* tuşuna basarsa ve *y*'nin değeri maksimum değerin 1 birim eksiğinden küçükse::

        elif q == ord("s") and y < boyutlar[0] - 1:

Yukarıdaki koşul altında şayet *y* maksimum değerinden 2 birim küçükse ve *x*'de maksimum değere ulaşmışsa, hiç bir işlem yapılmasın::

            if y == boyutlar[0] - 2 and x == boyutlar[1] - len("hello world!"):
                pass

Aksi taktirde, *y* değişkeninin değeri 1 birim artsın::

            else:
                y += 1

Şayet kullanıcı *a* tuşuna basarsa ve *x*'in değeri 0'dan büyükse, *x* değişkeninin değeri 1 birim azalsın::

        elif q == ord("a") and x > 0:
            x -= 1

Şayet kullanıcı *d* tuşuna basarsa ve *x*'in değeri maksimum değerden küçükse::

        elif q == ord("d") and x < boyutlar[1] - len("hello world!"):

Şayet yukarıdaki koşul altında *y*'nin ve *x*'in değerleri max değerlerinden 1 birim küçüğüne eşitse; hiç bir işlem yapılmasın::

            if y == boyutlar[0] - 1 and x == boyutlar[1] - len("hello world!") - 1:
                pass

Aksi taktirde, *x* değişkeninin değeri 1 birim arttırılsın::

            else:
                x += 1

`time.sleep()`'in neden kullanıldığını öğrenmek için bu fonksiyonun başına yorum satırı işareti getirin::

        time.sleep(0.05)

Ve programdan çıkıldığında terminal tekrar eski haline getirilsin::

    curses.endwin()

Örnek-6:
=========

"asdw" tuşlarıyla hareket eden, "1, 2, 3" tuşlarıyla renkleri değişen, "b" tuşu ile kalınlaşıp inceleşen ve "r" tuşuyla arka plan rengi ön plan rengi haline gelen bir "hello world!" yazısı oluşturalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time
    ekran = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    boyutlar = ekran.getmaxyx()
    ekran.nodelay(1)
    bold = 0
    reverse = 0
    b = [curses.A_NORMAL, curses.A_BOLD]
    r = [curses.A_NORMAL, curses.A_REVERSE]
    g = 1
    q = -1
    x, y = 0, 0
    while q != ord("q"):
        ekran.clear()
        ekran.addstr(y, x, "hello world!",
                     curses.color_pair(g) | b[bold] | r[reverse])
        ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)
        ekran.refresh()
        q = ekran.getch()
        if q in range(49, 52):
            g = int(chr(q))
        elif q == 98:
            bold = 1 - bold
        elif q == 114:
            reverse = 1 - reverse
        if q == ord("w") and y > 0:
            y -= 1
        elif q == ord("s") and y < boyutlar[0] - 1:
            if y == boyutlar[0] - 2 and x == boyutlar[1] - \
                    len("hello world!"):
                pass
            else:
                y += 1
        elif q == ord("a") and x > 0:
            x -= 1
        elif q == ord("d") and x < boyutlar[1] - len("hello world!"):
            if y == boyutlar[0] - 1 and x == boyutlar[1] - \
                    len("hello world!") - 1:
                pass
            else:
                x += 1
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Yine örnek uygulamamızda kullanacağımız modülleri içe aktaralım::

    import curses
    import time

Gördüğünüz gibi ilk olarak hep ekranı tanımlıyoruz::

    ekran = curses.initscr()

Örnek uygulamada renk kullanacağız yine. Bu yüzden renk çiftlerini tanımlamadan önce aşağıdaki fonksiyonu kesin kullanmamız gerekiyor::

    curses.start_color()

Şimdi 3 tane renk çifti oluşturalım::

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

Bastığımız tuşlar yine ekranda yansıma oluşturmasın::

    curses.noecho()

Ekranın maksimum *x* ve *y* değerlerini alalım::

    boyutlar = ekran.getmaxyx()

Animasyonumuzun ekranda görüntülenmesinin gecikmemesi için yine `nodelay()`'in parametresini 1 olarak ayarlıyoruz::

    ekran.nodelay(1)

Bu sefer kalınlaştırma işlemini bir tuş yardımıyla yapacağız. Bunun için *bold* isimli bir değişken oluşturalım ve değerini 0 yapalım::

    bold = 0

*"hello world!"* yazısının arka plan rengini ön plana, ön plan rengini ise arka plana çevirmek için *reverse* isminde bir değişken oluşturalım ve değerini 0 yapalım::

    reverse = 0

*b* tuşuna basılınca iki ayrı işlem yapılsın: Metin kalınlaştırılmışsa inceltilsin, yok eğer inceltilmişse kalınlaştırılsın. Bu işlem için bir liste oluşturalım::

    b = [curses.A_NORMAL, curses.A_BOLD]

Aynı şekilde *reverse* işlemi için de birbirinin tersi olan değişkenleri barındıran bir liste oluşturalım::

    r = [curses.A_NORMAL, curses.A_REVERSE]

Tanımladığımız renk çiftlerini kullanabilmek için yine *g* isimli bir değişken kullanacağız ve bu değişkenin değerini 1 olarak belirleyelim::

    g = 1

Yine ekrandaki her tuşu temsil eden bir *q* değişkeni oluşturalım::

    q = -1

*x* ve *y*'nin başlangıç değerlerini belirtelim::

    x, y = 0, 0

Yine *q* tuşuna basılınca sonlanan bir döngü oluşturalım::

    while q != ord("q"):

Ekranı temizleyelim yine::

        ekran.clear()

*"hello world!* yazısını ilgili tuşlara basılınca aktif hale gelecek biçimlendirme özellikleriyle birlikte ekrana ekleyelim::

        ekran.addstr(y, x, "hello world!",
                     curses.color_pair(g) | b[bold] | r[reverse])

İmleci ekranın sağ alt köşesine yerleştirelim::

        ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)

Ekranı tazeleyelim::

        ekran.refresh()

*q* bütün tuşları temsil etsin::

        q = ekran.getch()

`chr(49)`'dan `chr(52)`'ye kadar olan karakterler 1, 2 ve 3'tür. Şayet kullanıcı bu tuşlara basarsa *g* değişkeni değişecek ve böylece *"hello world!"* yazımız farklı renklere sahip olacak::

        if q in range(49, 52):
            g = int(chr(q))

Kullanıcı *b* tuşuna basarsa, *bold* değişkeninin değerini `1 - bold` yapalım. Böylece *bold* 0 iken *bold* 1 olur, *bold* 1 iken de *bold* 0 olur. Bu şekilde yukarıda tanımladığımız *b* listesinin iki elemanını da aktif hale getirmiş oluruz::

        elif q == 98:
            bold = 1 - bold

Kullanıcı "r" tuşuna basarsa, *reverse*'in değeini `1 - reverse` yapalım. Yine aynı şekilde *reverse* 0 iken *reverse* 1 olur, *reverse* 1 iken de *reverse* 0 olur. Böylece yukarıda tanımladığımız *r* listesinin iki elemanını da aktif hale getiririz::

        elif q == 114:
            reverse = 1 - reverse

Eğer kullanıcı *w* tuşuna basarsa ve *y*'nin değeri 0'dan büyükse, *y* değişkeninin değeri 1 birim azaltılsın::

        if q == ord("w") and y > 0:
            y -= 1

Şayet kullanıcı *s* tuşuna basarsa ve *y*'nin değeri maksimum değerin 1 birim eksiğinden küçükse::

        elif q == ord("s") and y < boyutlar[0] - 1:

Yukarıdaki koşul altında, şayet *y*, maksimum değerinden 2 birim küçükse ve *x*'de maksimum değere ulaşmışsa, hiç bir işlem yapılmasın::

            if y == boyutlar[0] - 2 and x == boyutlar[1] - len("hello world!"):
                pass

Aksi taktirde, *y* değişkeninin değeri 1 birim arttırılsın::

            else:
                y += 1

Şayet kullanıcı *a* tuşuna basarsa ve *x*'in değeri 0'dan büyükse, *x* değişkeninin değeri 1 birim azaltılsın::

        elif q == ord("a") and x > 0:
            x -= 1

Şayet kullanıcı *d* tuşuna basarsa ve *x*'in değeri maksimum değerden küçükse::

        elif q == ord("d") and x < boyutlar[1] - len("hello world!"):

Yukarıdaki koşul altında, şayet *y*'nin ve *x*'in değerleri maksimum değerlerinden 1 birim küçüğüne eşitse, hiç bir işlem yapılmasın::

            if y == boyutlar[0] - 1 and x == boyutlar[1] - len("hello world!") - 1:
                pass

Aksi taktirde, *x* değişkeninin değeri 1 birim arttırılsın::

            else:
                x += 1

Yine bu `time.sleep()` fonksiyonunun burada neden kullanıldığını görmek için, fonksiyonu yoruma alın ve aradaki farka bakın::

        time.sleep(0.05)

Ve programı yine terminali bozmayacak şekilde sonlandıralım::

    curses.endwin()

Örnek-7:
=========

Yön tuşlarıyla hareket eden, "1, 2, 3" tuşlarıyla renkleri değişen, "b" tuşu ile kalınlaşıp inceleşen ve "r" tuşuyla arka plan rengi ön plan rengi haline gelen bir "hello world!" yazısı oluşturalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses
    import time

    ekran = curses.initscr()
    ekran.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.noecho()
    boyutlar = ekran.getmaxyx()
    ekran.nodelay(1)
    bold = 0
    reverse = 0
    b = [curses.A_NORMAL, curses.A_BOLD]
    r = [curses.A_NORMAL, curses.A_REVERSE]
    g = 0
    q = -1
    x, y = 0, 0
    while q != ord("q"):
        ekran.clear()
        ekran.addstr(y, x, "hello world!",
                     curses.color_pair(g)| b[bold] | r[reverse])
        ekran.move(boyutlar[0] -1, boyutlar[1] - 1)
        ekran.refresh()
        q = ekran.getch()
        if q in range(48, 52):
            g = int(chr(q))
        elif q == 98:
            bold = 1 - bold
        elif q == 114:
            reverse = 1 - reverse
        if q == curses.KEY_UP and y > 0:
            y -= 1
        elif q == curses.KEY_DOWN and y < boyutlar[0] - 1:
            if y == boyutlar[0] - 2 and x == boyutlar[1] - \
                    len("hello world!"):
                pass
            else:
                y += 1
        elif q == curses.KEY_LEFT and x > 0:
            x -= 1
        elif q == curses.KEY_RIGHT and x < boyutlar[1] - len("hello world!"):
            if y == boyutlar[0] - 1 and x == boyutlar[1] - \
                    len("hello world!") - 1:
                pass
            else:
                x += 1
        time.sleep(0.05)
    curses.endwin()

**Kodların Açıklamaları:**

Yine örnek uygulamamızda kullanacağımız modülleri içe aktaralım::

    import curses
    import time

Yine önce ekranı tanımlayalım::

    ekran = curses.initscr()

Şimdi de yön tuşlarının kullanılabilmesi için `keypad()` fonksiyonunu değeri `True` olacak şekilde çağıralım::

    ekran.keypad(1)

Örnek uygulamada renk kullanacağız yine. Bu yüzden renk çiftlerini tanımlamadan önce aşağıdaki fonksiyonu kesin kullanmamız gerekiyor::

    curses.start_color()

Şimdi 3 tane renk çifti oluşturalım::

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

Bastığımız tuşlar yine ekranda yansıma oluşturmasın::

    curses.noecho()

Ekranın maksimum *x* ve *y* değerlerini alalım::

    boyutlar = ekran.getmaxyx()

Animasyonumuzun ekranda görüntülenmesinin gecikmemesi için yine `nodelay()`'in parametresini 1 olarak ayarlıyoruz::

    ekran.nodelay(1)

Bu sefer de kalınlaştırma işlemini bir tuş yardımıyla yapacağız. Bunun için *bold* isimli bir değişken oluşturalım ve değerini 0 yapalım::

    bold = 0

*"hello world!"* yazısının arka plan rengini ön plana, ön plan rengini ise arka plana çevirmek için *reverse* isminde bir değişken oluşturalım ve değerini 0 yapalım::

    reverse = 0

*b* tuşuna basılınca iki ayrı işlem yapılsın: Metin kalınlaştırılmışsa inceltilsin, yok eğer inceltilmişse kalınlaştırılsın. Bu işlem için bir liste oluşturalım::

    b = [curses.A_NORMAL, curses.A_BOLD]

Aynı şekilde *reverse* işlemi için de birbirinin tersi olan değişkenleri barındıran bir liste oluşturalım::

    r = [curses.A_NORMAL, curses.A_REVERSE]

Tanımladığımız renk çiftlerini kullanabilmek için yine *g* isimli bir değişken kullanacağız ve bu değişkenin değerini 1 olarak belirleyelim::

    g = 1

Yine ekrandaki her tuşu temsil eden bir *q* değişkeni oluşturalım::

    q = -1

*x* ve *y*'nin başlangıç değerlerini belirtelim::

    x, y = 0, 0

Yine *q* tuşuna basılınca sonlanan bir döngü oluşturalım::

    while q != ord("q"):

Ekranı temizleyelim yine::

        ekran.clear()

*"hello world!* yazısını, ilgili tuşlara basılınca aktif hale gelecek biçimlendirme özellikleriyle birlikte ekrana ekleyelim::

        ekran.addstr(y, x, "hello world!",
                     curses.color_pair(g) | b[bold] | r[reverse])

İmleci ekranın sağ alt köşesine yerleştirelim::

        ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)

Ekranı tazeleyelim::

        ekran.refresh()

*q* bütün tuşları temsil etsin::

        q = ekran.getch()

`chr(49)`'dan `chr(52)`'ye kadar olan karakterler 1, 2 ve 3'tür. Şayet kullanıcı bu tuşlara basarsa *g* değişkeni değişecek ve böylece *"hello world!"* yazımız farklı renklere sahip olacak::

        if q in range(49, 52):
            g = int(chr(q))

Kullanıcı *b* tuşuna basarsa, *bold* değişkeninin değerini `1 - bold` yapalım. Böylece *bold* 0 iken *bold* 1 olur, *bold* 1 iken de *bold* 0 olur. Bu şekilde yukarıda tanımladığımız *b* listesinin iki elemanını da aktif hale getirmiş oluruz::

        elif q == 98:
            bold = 1 - bold

Kullanıcı "r" tuşuna basarsa, *reverse*'in değeini `1- reverse` yapalım. Yine aynı şekilde *reverse* 0 iken *reverse* 1 olur, *reverse* 1 iken de *reverse* 0 olur. Böylece yukarıda tanımladığımız *r* listesinin iki elemanını da aktif hale getiririz::

        elif q == 114:
            reverse = 1 - reverse

Eğer kullanıcı yukarı ok tuşuna basarsa ve *y*'nin değeri 0'dan büyükse; *y* değişkeninin değeri 1 birim azaltılsın::

        if q == curses.KEY_UP and y > 0:
            y -= 1

Şayet kullanıcı aşağı ok tuşuna basarsa ve *y*'nin değeri maksimum değerin 1 birim eksiğinden küçükse::

        elif q == curses.KEY_DOWN and y < boyutlar[0] - 1:

Yukarıdaki koşul altında, şayet *y*, maksimum değerinden 2 birim küçükse ve *x*'de maksimum değere ulaşmışsa, hiç bir şey yapılmasın::

            if y == boyutlar[0] - 2 and x == boyutlar[1] - len("hello world!"):
                pass

Aksi taktirde; *y* değişkeninin değeri 1 birim arttırılsın::

            else:
                y += 1

Şayet kullanıcı sol ok tuşuna basarsa ve *x*'in değeri 0'dan büyükse, *x* değişkeninin değeri 1 birim azaltılsın::

        elif q == curses.KEY_LEFT and x > 0:
            x -= 1

Şayet kullanıcı sağ ok tuşuna basarsa ve *x*'in değeri maksimum değerden küçükse::

        elif q == curses.KEY_RIGHT and x < boyutlar[1] - len("hello world!"):

Yukarıdaki koşul altında, şayet *y*'nin ve *x*'in değerleri maksimum değerlerinden 1 birim küçüğüne eşitse, hiç bir şey yapılmasın::

            if y == boyutlar[0] - 1 and x == boyutlar[1] - len("hello world!") - 1:
                pass

Aksi taktirde *x* değişkeninin değeri 1 birim arttırılsın::

            else:
                x += 1

Yine bu `time.sleep()` fonksiyonunun burada neden kullanıldığını görmek için, fonksiyonu yoruma alın ve aradaki farka bakın::

        time.sleep(0.05)

Ve programı yine terminali bozmayacak şekilde sonlandıralım::

    curses.endwin()

Örnek-8:
=========

Bu örnekte ekrana hazır bir metin eklemek yerine Türkçe karakterler eklemeye çalışalım. Ve ayrıca eklediğimiz karakterleri silmek veya bir alt satıra geçmek için yeni işlemler tanımlayalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import curses

    ekran = curses.initscr()
    ekran.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    boyutlar = ekran.getmaxyx()
    q = -1
    x, y = 0, 0
    xy = []
    karakterler = []


    def karakter_ekle(karakter, num1, num2):
        global x, y
        ekran.addstr(y, x, karakter, curses.color_pair(1))
        x += 1
        karakterler.remove(num1)
        karakterler.remove(num2)


    while q != 27:
        q = ekran.getch()
        ekran.refresh()
        karakterler.append(q)
        if boyutlar[1] - x == 1:
            xy.append((y, x - 1))
            y += 1
            x = 0
        if q == 263:
            if x == 0:
                if y != 0:
                    y -= 1
                    try:
                        x = xy[len(xy) - 1][1]
                        xy.pop(len(xy) - 1)
                    except IndexError:
                        x = boyutlar[1] - 1
                    ekran.delch(y, x)
                else:
                    pass
            else:
                ekran.delch(y, x - 1)
                x -= 1
        elif q == 10:
            xy.append(curses.getsyx())
            ekran.addstr(y, x, chr(10), curses.color_pair(1))
            y += 1
            x = 0
        elif q == 261:
            if boyutlar[1] - x == 1:
                y += 1
                x = 0
            else:
                x += 1
                ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 260:
            if x == 0:
                if y != 0:
                    y -= 1
                    x = 78
                else:
                    pass
            else:
                x -= 1
                ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 259:
            if y != 0:
                y -= 1
                ekran.addstr(y, x, "", curses.color_pair(1))
            else:
                pass
        elif q == 258:
            if y != boyutlar[0] - 1:
                y += 1
                ekran.addstr(y, x, "", curses.color_pair(1))
            else:
                pass
        elif q == 195:
            ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 196:
            ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 197:
            ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 167:
            karakter_ekle("\u00e7", 195, 167)
        elif q == 159:
            if 196 in karakterler:
                karakter_ekle("\u011f", 196, 159)
            elif 197 in karakterler:
                karakter_ekle("\u015f", 197, 159)
        elif q == 177:
            karakter_ekle("\u0131", 196, 177)
        elif q == 182:
            karakter_ekle("\u00f6", 195, 182)
        elif q == 188:
            karakter_ekle("\u00fc", 195, 188)
        elif q == 135:
            karakter_ekle("\u00c7", 195, 135)
        elif q == 158:
            if 196 in karakterler:
                karakter_ekle("\u011e", 196, 158)
            elif 197 in karakterler:
                karakter_ekle("\u015e", 197, 158)
        elif q == 176:
            karakter_ekle("\u0130", 196, 176)
        elif q == 150:
            karakter_ekle("\u00d6", 195, 150)
        elif q == 156:
            karakter_ekle("\u00dc", 195, 156)
        else:
            ekran.addstr(y, x, chr(q), curses.color_pair(1))
            x += 1
    curses.endwin()

**Kodların Açıklamaları:**

Her zamanki gibi önce gerekli modülü programın içine aktarıyoruz::

    import curses

Bildiğiniz gibi curses ile işlem yapmaya geçmeden önce ekranı tanıtmamız gerekiyor::

    ekran = curses.initscr()

Bu çalışmada tanımlanmamasına rağmen *BACKSPACE* gibi bazı özel klavye tuşlarını kullanacağımız için önce `keypad()` fonksiyonunu çağırmalıyız::

    ekran.keypad(1)

Yine bildiğiniz gibi yazıları renklendirmek için önce renklendiriciyi başlatmamız gerekiyor::

    curses.start_color()

Şimdi bir tek tane renk çifti oluşturalım::

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

Bastığımız tuşların ekranda yansıma oluşturmaması için `curses.noecho()` fonksiyonunu kullanalım::

    curses.noecho()

Ekranın maksimum boyutlarını bir değişkene atayalım::

    boyutlar = ekran.getmaxyx()

Yine her tuşu temsil edecek *q* değişkenimizi tanımlayalım::

    q = -1

Şimdi de satır ve sütun değeri olarak kullanacağımız değişkenleri tanımlayalım::

    x, y = 0, 0

Her bir satırı bir liste içinde tutacağız. Her satırda hangi sütunda kaldığımızı bilmemiz gerekiyor çünkü karakter silme işleminde bize lazım olacak::

    xy = []

Türkçe karakterlerin olduğu tuşlara bastığımız sırada, q'nun 1'den fazla değeri olur. Mesela *Enter* tuşu için konuşacak olursak karakter değeri 10'dur. `elif q == 10:` durumunda yapılması gerekeni rahatça belirleyebiliriz. Ama aynı durum Türkçe karakterler için geçerli değildir. Örneğin *ç* tuşuna basılınca yapılması gereken işlemleri belirtmek için şöyle bir koşul tanımlamamız gerekir: `elif q == 196:` durumunda bir şey yap. Sonra da `elif q == 159:` durumunda bir şey yap. Çünkü *ç* harfine bastığımız zaman iki tane karakter değeri oluşur. Bunlardan birisi *196* diğeri *159*'dur. Aynı durum diğer Türkçe karakterler için de geçerlidir. Mesela *ı* harfine basınca oluşan karakter değerleri *196* ve *177* olur. O halde karakter değerlerinden birisinin *196* olduğu birden fazla tuş var. İşte bu tuş kombinasyonlarını birbirlerinden ayırmak için bir liste kullanacağız::

    karakterler = []

Türkçe karakterleri bir fonksiyon yardımıyla ekrana eklemeye çalışalım. Buradaki *karakter* parametresi, Türkçe harfin unicode kodu; num1 ve num2 parametreleri ise karakterin değerleridir::

    def karakter_ekle(karakter, num1, num2):

Fonksiyonumuzun içine global alandaki *x*, ve *y* değişkenlerini çekelim::

        global x, y

Global alandan aldığımız ekrana ait *y*, *x* konumuna karakteri ekleyelim::

        ekran.addstr(y, x, karakter, curses.color_pair(1))

Her Türkçe karakteri ekledikten sonra, x'in konumunu 1 birim arttıralım ki yeni girilecek karakter için kullanılabilir yeni bir hücre oluşsun::

        x += 1

Daha sonra da karakterler listesinden bu tuşu temsil eden değerleri silelim ki, bir sonraki Türkçe
karakteri ekrana eklemek istediğimizde sorun çıkmasın::

        karakterler.remove(num1)
        karakterler.remove(num2)

Şimdi de, *ESC* tuşuna basılmadığı sürece çalışan bir döngü oluşturalım::

    while q != 27:

*q* bütün tuşları temsil etsin::

        q = ekran.getch()

Ekranı tazeleyelim::

        ekran.refresh()

Her tuşa bastığımızda karakterler listesine *q* değeri eklensin::

        karakterler.append(q)

Eğer bir satırın sonuna gelinmişse, *xy* satır listesine bu satırı ekleyelim::

        if boyutlar[1] - x == 1:
            xy.append((y, x - 1))

Aynı zamanda y değişkeninin değeri 1 birim artsın ki bir alt satıra, x değişkeninin değeri de 0'a eşitlensin ki satır başına geçelim::

            y += 1
            x = 0

Eğer kullanıcı *BACKSPACE* tuşuna basarsa ve koşul altında eğer *x* değişkeninin değeri 0'a eşitse::

        if q == 263:
            if x == 0:

Yukarıdaki her iki koşulun altında eğer *y* değişkeninin değeri 0'a eşit değilse, *y* değişkeninin değeri 1 birim azaltılsın::

                if y != 0:
                    y -= 1

Ayrıca x'in değeri bir önceki satırın bittiği x değerine eşitlenmeye çalışılsın ve satır listesinden bir önceki satır silinsin::

                    try:
                        x = xy[len(xy) - 1][1]
                        xy.pop(len(xy) - 1)

Bu işlem yapılırken bir sıra hatası oluşmasını bekliyoruz, bu durumda x'in değeri maksimum x değerine eşitlensin::

                    except IndexError:
                        x = boyutlar[1] - 1

Her halükarda ekranın y, x konumundan bu karakter silinsin::

                    ekran.delch(y, x)

*BACKSPACE* tuşuna basıldığı koşulun altında, eğer *x* değikeninin değeri 0'a eşitse ve eğer *y* değişkeninin değeri de 0'a eşitse, hiç bir işlem yapılmasın::

                else:
                    pass

*BACKSPACE* tuşuna basıldığı koşulun altında ve eğer *x* değikeninin değeri 0'a eşit değilse, ekranın *y*, *x - 1* konumundan bu karakter silinsin ve *x* değişkeninin değeri 1 birim azaltılsın::

            else:
                ekran.delch(y, x - 1)
                x -= 1

Eğer kullanıcı *enter* tuşuna basarsa: *xy* satır listesine o andaki *y*, *x* değerlerini ekleyelim, ekrana *"\n"* kaçış dizisi eklensin, *y* değikeninin değeri 1 birim arttırılsın ve *x* değişkeninin değeri 0'a eşitlensin yani yeni satırın başına geçilsin::

        elif q == 10:
            xy.append(curses.getsyx())
            ekran.addstr(y, x, chr(10), curses.color_pair(1))
            y += 1
            x = 0

Eğer kullanıcı sağ ok tuşuna basarsa ve *x* değişkeni maksimum değerine ulaştıysa, *y* değişkenin değeri 1 birim arttırılsın ve *x* değişkeninin değeri 0'a eşitlensin. Yani yeni bir satıra geçilsin. Yok eğer *x* değişkeni maksimum değerine ulaşmadıysa, *x* değişkeninin değeri 1 birim arttırılsın ve ekrana boş bir string verisi eklensin::

        elif q == 261:
            if boyutlar[1] - x == 1:
                y += 1
                x = 0
            else:
                x += 1
                ekran.addstr(y, x, "", curses.color_pair(1))

Eğer kullanıcı sol ok tuşuna basarsa, *x* değişkeninin değeri 0'a eşitse ve *y* değişkeninin değeri 0'a eşit değilse, *y* değişkeninin değeri 1 birim azaltılsın, *x* değişkeninin değeri 78 olarak ayarlansın, şayet hem *x* hem de*y* değişkeninin değeri 0'a eşitse hiç bir işlem yapılmasın. *x* değişkeninin değeri 0'a eşit değilse, *x* değişkenin değeri 1 birim azaltılsın ve ekranın *yx* konumuna boş bir string eklensin::

        elif q == 260:
            if x == 0:
                if y != 0:
                    y -= 1
                    x = 78
                else:
                    pass
            else:
                x -= 1
                ekran.addstr(y, x, "", curses.color_pair(1))

Eğer kullanıcı yukarı ok tuşuna basarsa ve *y* değişkeninin değeri 0'a eşit değilse, *y* değişkeninin değeri 1 birim azaltılsın ve ekranın *yx* konumuna boş bir string yerleştirilsin. Eğer *y* değişkeninin değeri 0'a eşitse, hiç bir işlem yapılmasın::

        elif q == 259:
            if y != 0:
                y -= 1
                ekran.addstr(y, x, "", curses.color_pair(1))
            else:
                pass

Eğer kullanıcı aşağı ok tuşuna basarsa ve *y* değişkeni maksimum değerine eşit değilse, *y* değişkeninin değeri 1 birim arttırılsın ve ekranın *yx* konumuna boş bir string yerleştirilsin. Eğer *y* değişkeni ekranın maksimum *y* değerine gelmişse, hiç bir işlem yapılmasın::

        elif q == 258:
            if y != boyutlar[0] - 1:
                y += 1
                ekran.addstr(y, x, "", curses.color_pair(1))
            else:
                pass

Aşağıdaki kodlar Türkçe karakterleri eklemekle ilgilidir. Daha önce belirtildiği gibi Türkçe karakterler iki tane karakter değerine sahip oluyor. Dolayısıyla bir karakteri ekledikten sonra o karakterin değerlerini karakterler listesinden bir karışılıklık olmaması için silmek gerekiyor. Aşağıda tanımlanmış olan 3 koşul da Türkçe karakterlerin 1. değerleridir, bu üç sayısal değerden birisi bütün Türkçe karakterlerde ortak olarak bulunuyor::

        elif q == 195:
            ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 196:
            ekran.addstr(y, x, "", curses.color_pair(1))
        elif q == 197:
            ekran.addstr(y, x, "", curses.color_pair(1))

Aşağıdaki kodlarda hangi koşullarda ekrana Türkçe karakterlerin ekleneceği tanımlanmıştır. Türkçe karakterler doğrudan unicode karakteri olarak eklenecektir:

Küçük *"ç"* harfinin eklenmesini sağlayan koşul::

        elif q == 167:
            karakter_ekle("\u00e7", 195, 167)

Küçük *"ğ"* ve küçük *"ş"* harflerinin eklenmesini sağlayan koşullar::

        elif q == 159:
            if 196 in karakterler:
                karakter_ekle("\u011f", 196, 159)
            elif 197 in karakterler:
                karakter_ekle("\u015f", 197, 159)

Küçük *"ı"* harfininin eklenmesini sağlayan koşul::

        elif q == 177:
            karakter_ekle("\u0131", 196, 177)

Küçük *"ö"* harfinin eklenmesini sağlayan koşul::

        elif q == 182:
            karakter_ekle("\u00f6", 195, 182)

Küçük *"ü"* harfinin eklenmesini sağlayan koşul::

        elif q == 188:
            karakter_ekle("\u00fc", 195, 188)

Büyük *"Ç"* harfinin eklenmesini sağlayan koşul::

        elif q == 135:
            karakter_ekle("\u00c7", 195, 135)

Büyük *"Ğ*" ve büyük *"Ş"* harflerinin eklenmesini sağlayan koşullar::

        elif q == 158:
            if 196 in karakterler:
                karakter_ekle("\u011e", 196, 158)
            elif 197 in karakterler:
                karakter_ekle("\u015e", 197, 158)

Büyük *"İ"* harfinin eklenmesini sağlayan koşul::

        elif q == 176:
            karakter_ekle("\u0130", 196, 176)

Büyük *"Ö"* harfinin eklenmesini sağlayan koşul::

        elif q == 150:
            karakter_ekle("\u00d6", 195, 150)

Büyük *"Ü"* harfinin eklenmesini sağlayan koşul::

        elif q == 156:
            karakter_ekle("\u00dc", 195, 156)

Ve son koşulumuzda Türkçe karakterler haricinde herhangi bir karakterin ekrana nasıl eklenmesi gerektiği tanımlanmıştır. Bu koşulda karakter *yx* konumuna eklenir ve *x* değişkeninin değeri 1 birim arttırılır::

        else:
            ekran.addstr(y, x, chr(q), curses.color_pair(1))
            x += 1

Örnek-9:
=========

Bu örnekte `def`, `if`, `else` gibi bazı özel kelimelerin diğer kelimelerden farklı renge sahip olması için uğraşalım. Örneğin `def`’i *define*’den veya *"def"* den ayırt etmeye çalışalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import re
    import curses
    import keyword

    ekran = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.noecho()
    q = -1
    karakterler = ""
    while q != ord("q"):
        q = ekran.getch()
        ekran.addstr(chr(q), curses.color_pair(1))
        karakterler += chr(q)
        for kw in keyword.kwlist:
            regex1 = re.search("[^'\"]\s{}\s$".format(kw), karakterler)
            regex2 = re.search("^{}\s$".format(kw), karakterler)
            if regex1 or regex2:
                ekran.addstr("{}{} ".format("\b" * (len(kw) + 1), kw),
                             curses.color_pair(2))
                karakterler = ""
    curses.endwin()

**Kodların Açıklamaları:**

Bu örnekte kullanacağımız modülleri programın içine aktaralım::

    import re
    import curses
    import keyword

Her zamanki gibi ekranı tanıtıyoruz::

    ekran = curses.initscr()

Renklendirme işlemine geçmeden önce bildiğiniz gibi renk başlatıcıyı çalıştırıyoruz::

    curses.start_color()

Bu örnekte bir çift Python'a özgü özel karakterler için, bir çift de diğer karakterler için toplam iki çift renk tanımlayalım::

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

Karakterlerin ekranda yansımasını istemiyoruz diyelim::

    curses.noecho()

Her karakteri temsil edecek bir karakter seçelim. Ve değerini -1 yapalım (değerinin ne olduğu bu örnekte pek önemli değil)::

    q = -1

Python'a özgü karakterleri diğer karakterlerden ayırt edebilmek için bir tane string verisi oluşturalım::

    karakterler = ""

*q* değişkeninin `"q"`'ya eşit olmadığı durumda çalışacak döngüyü tanımlayalım::

    while q != ord("q"):

*q* değişkeni her karakteri temsil etsin::

    q = ekran.getch()

Basılan her tuşun karakteri ekrana 1. sıradaki renkle birlikte eklensin::

    ekran.addstr(chr(q), curses.color_pair(1))

Eklenen her bir karakter, *karakterler* değişkenine de eklensin::

    karakterler += chr(q)

keyword.kwlist listesi içindeki Python'a özgü her bir özel ifade için, iki tane düzenli ifade oluşturalım::

    for kw in keyword.kwlist:
        regex1 = re.search("[^'\"]\s{}\s$".format(kw), karakterler)
        regex2 = re.search("^{}\s$".format(kw), karakterler)

Eğer yazdığımız yazı regex1'e veya regex2'ye uyuyorsa, ekrana bu yazı farklı bir renkle yazılsın. Buradaki `"\b" * (len(kw) + 1)` kod parçası *kw* ile temsil edilen kwlistteki her bir özel ifadeden sonra yeni eklenecek karakterin nereye eklenmesi gerektiğini belirtir. Mesela kwlistteki üç harflik bir özel ifade için 4. hücreye yeni bir karakter eklenmesini sağlar. Eğer bu kod parçasını yazıyı ekrana eklerken yazmazsak, yeni eklenen karakterler, özel karakterlerin üzerine yazılır::

        if regex1 or regex2:
            ekran.addstr("{}{} ".format("\b" * (len(kw) + 1), kw),
                         curses.color_pair(2))

Ve *karakterler* stringimizin değerini boş bir string verisine eşitleyelim ki bir sonraki karakter için tekrar kullanabilelim::

        karakterler = ""

Ve son olarak program kapandığında terminali eski haline getirmek için `curses.endwin()` fonksiyonumuzu çağıralım::

    curses.endwin()
