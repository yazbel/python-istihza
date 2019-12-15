.. meta::
   :description: Bu bölümde threading modülünü inceleyeceğiz.
   :keywords: python, modül, import, threading

.. highlight:: python3

****************
threading Modülü
****************

**Kaynak Kodu:** https://hg.python.org/cpython/file/3.5/Lib/threading.py

Bu modül; düşük seviyeli `_thread` modülü üzerine, yüksek seviyeli iş parçacığı yürütüm ara yüzleri inşa eder. Ayrıca `queue` modülüne de bakınız.

`dummy_threading` modülü, `_thread`'in kayıp olmasından ötürü `threading`'in kullanılamadığı durumlar için sağlanmıştır.

**Not:** Aşağıda listelenmemişken, Python 2.x serilerindeki bu modülün bazı metotlarının ve fonksiyonlarının kullandığı camelCase isimler hala bu modül tarafından desteklenmektedir.

Bu modül aşağıdaki fonksiyonları tanımlar:

**threading.active_count()**

    Hazır çalışmakta olan iş parçacığı (Thread) nesnelerinin sayısını geri döndürür. Geri dönen değer `enumerate()` tarafından döndürülen listenin uzunluğuna eşittir.

**threading.current_thread()**

    Çağıranın kontrol dizesine karşılık gelen iş parçacığı nesnesini geri döndürür. Eğer çağıranın kontrol dizesi `threading` modülü vasıtasıyla oluşturulmamışsa, işlevselliği sınırlandırılmış bir kukla (dummy) iş parçacığı (thread) nesnesi geri döndürülür.

**threading.get_ident()**

    Şimdiki iş parçacığının (Thread'in) iş parçacığı tanımlayıcısını (thread identifier’ı) geri döndürür. Bu, sıfır olmayan bir tam sayıdır. Değerinin doğrudan bir anlamı yoktur; sihirli bir çerez olarak kullanılmak üzere tasarlanmıştır, örneğin iş parçacıklarına özgü verilerden oluşan bir sözlüğü dizinlemek için.

    Sürüm 3.3.'de gelmiştir.

**threading.enumerate()**

    Hazır çalışmakta olan bütün iş parçacığı (Thread) nesnelerinin listesini geri döndürür. Liste daemonic (kullanıcının doğrudan kontrolünde olmayıp arka planda çalışan) iş parçacıklarını, `current_thread()` tarafından oluşturulmuş dummy (kukla) iş parçacıklarını ve ana iş parçacığını içerir. Listeye sonlandırılmış iş parçacıkları ve henüz başlatılmamış iş parçacıkları dâhil edilmez.

**threading.main_thread()**

    Ana iş parçacığı (main-thread) nesnesini geri döndürür. Normal durumlarda, ana iş parçacığı Python yorumlayıcısı tarafından başlatılmış olan iş parçacığıdır.

    Sürüm 3.4.'de gelmiştir.

**threading.settrace(func)**

    Threading modülünden başlatılan bütün iş parçacıkları için bir tane izleyici fonksiyon ayarlar. Func yazan yere, her bir iş parçacığı için, `run()` metodu çağrılmadan önce, `sys.settrace()` gelecektir.

**threading.setprofile(func)**

    Threading modülünden başlatılan bütün iş parçacıkları için bir tane kesit fonksiyonu ayarlar. Func yazan yere, her bir iş parçacığı için, `run()` metodu çağrılmadan önce, `sys.setprofile()` gelecektir.

**threading.stack_size([size])**

    Yeni iş parçacıkları oluştururken, kullanılan iş parçacığı yığın boyutunu geri döndürür. Seçeneğe bağlı olan *size* argümanı daha sonradan oluşturulacak iş parçacıkları için yığın boyutunu belirtir ve -platform kullanımında veya ön tanımlı ayar olarak- değeri 0 veya 32,768 (32 KiB)'den büyük pozitif bir tamsayı olmalıdır. Eğer *size* argümanı tanımlanmazsa, değeri 0 olur. Eğer iş parçacığının yığın boyutunun değiştirilmesi desteklenmezse, bir `RuntimeError` hatası yükseltilir. Eğer tanımlanmış yığın boyutu geçersiz ise, `ValueError` hatası yükseltilir ve yığın boyutu değiştirilmemiş olur. 32 KiB, yorumlayıcıya yeterli yığın alanı temin etmek için yığın boyutunun desteklenen geçerli minimum değeridir. Bazı platformların, yığın boyutunun değeri üzerinde, kendilerine özgü bir takım sınırlamaları vardır. Örneğin yığın boyutunun 32 KiB'den büyük olmasının gerekliliği veya sistem hafıza sayfası boyutunun katlarının paylaştırılmasının gerekliliği gibi - platform belgesi daha fazla bilgi vermesi için referans gösterilebilir - (4 KiB'lik sayfalar yaygındır; yığın boyutunun 4096'nın katları olarak kullanılması, daha özel bilgilerin olmaması durumunda önerilen bir yaklaşımdır.) Kullanılabilen platformlar: Windows, POSIX iş parçacığı ile çalışan sistemler.

Bu modül ayrıca aşağıdaki sabiti de tanımlar:

**threading.TIMEOUT_MAX**

    `Lock.acquire()`, `RLock.acquire()`, `Condition.wait()` vb. gibi engelleyici fonksiyonların zaman aşımı parametreleri için maksimum değere izin verilir.

    Sürüm 3.2'de gelmiştir.

Bu modül aşağıdaki kısımda ayrıntıları verilen birkaç sınıfı tanımlar.

Bu modülün tasarımı yaklaşık olarak Java'nın threading modeli üzerine temellenmiştir. Ancak bununla birlikte, Java'daki her nesnenin temel davranışında olan kilit ve durum değişkenleri, Python'da ayrı nesnelerdir. Python'daki Thread sınıfı Java'daki Thread sınıfının davranışını bir alt set olarak destekler; şimdilik ne bir öncelik, ne bir iş parçacığı grubu vardır. İş parçacıkları yok edilemez, durdurulamaz, yasaklanamaz, devam ettirilemez ve sonlandırılamaz. Java'nın Thread sınıfının statik metotları, uygulandığında, modül düzeyindeki fonksiyonlarla eşleştirilir.
Aşağıda açıklanmış metotların hepsi otomatik olarak çalıştırılır.


Yerel İş Parçacığı (Thread-Local) Verisi
=========================================

Yerel iş parçacığı (thread-local) verisi, değeri iş parçacığı olarak belirlenmiş bir değerdir. Yerel iş parçacığı verisini yönetmek için, sadece yerel sınıftan (veya bir alt sınıftan) bir tane örnek oluşturulur ve özellikler bu sınıfta tutulur::

    yerel_veri = threading.local()
    yerel_veri.x = 1

Ayrı iş parçacıkları için örneğin değeri değişik olacaktır.

**class threading.local**

    Yerel iş parçacığı verisini temsil eden sınıftır.

    Daha fazla ayrıntı ve geniş örnekler için, *_threading_local* modülünün belge dizisine bakın.

İş Parçacığı (Thread) Nesneleri
================================

İş parçacığı (thread) sınıfı, ayrı iş parçacıklarını kontrol eden bir etkinliği temsil eder. Bu etkinliği belirtmek için iki yol vardır: yapıcıya, çağrılabilir bir nesne atamak veya bir alt sınıfta `run()` metodunu iptal etmek. Yapıcı dışında hiçbir metot bir alt sınıfta iptal edilmemelidir. Başka bir deyişle, bu sınıfın sadece `__init__()` ve `run()` metotları iptal edilir.

Bir iş parçacığı (thread) nesnesi oluşturulduğunda, bu nesnenin etkinliği, iş parçacığının `start()` metodu çağrılarak başlatılmalıdır. Bu ayrılmış bir iş parçacığının kontrolündeki `run()` metodunu çalıştırır.

Bir iş parçacığı (thread) başlatıldığında, iş parçacığı 'canlanmış' olarak kabul edilir. Normalde bu iş parçacığının `run()` metodu sonlandığında, iş parçacığının canlılığı da sonlanır - veya yürütülemeyen bir beklenti yükseltilir-. İş parçacığının canlı olup olmadığını `is_alive()` metodu test eder.

Diğer iş parçacıkları, bir iş parçacığının `join()` metodunu çağırabilir. Bu metot, çağrılan iş parçacığını, `join()` metodu çağrılan iş parçacığı sonlana kadar engeller.

Bir iş parçacığının bir ismi vardır ve ismi yapıcıya atanabilir ve 'name' özelliği vasıtasıyla okunabilir veya değiştirilebilir.

Bir iş parçacığı *daemon iş parçacığı (=daemon thread)* olarak işaretlenir. Bu işaretin önemi, sadece daemon iş parçacığı kaldığında bütün Python programının sonlanmasıdır. İşaretin başlangıç değeri, oluşturulmuş olan iş parçacığından miras alınır. İşaret, daemon özelliği (property) veya daemon'un yapıcı argümanı tarafından ayarlanabilir.

**Not:** Daemon iş parçacıkları bilgisayar kapatıldığında ani bir şekilde sonlanır. Açılmış dosyalar, veritabanı hareketleri gibi birçok kaynak, düzgün bir şekilde serbest bırakılmayabilir. Eğer iş parçacıklarının düzgün bir şekilde durmasını istiyorsanız, onları non-daemonic (daemonic olmayacak şekilde) ayarlayın ve Event gibi uygun bir sinyal mekanizması kullanın.

Python programında bir tane ana iş parçacığı (main-thread) nesnesi vardır ve bu nesne başlangıçtaki iş parçacığının kontrol edilmesine yarar. Bu nesne bir daemon iş parçacığı değildir.

Kukla iş parçacığı nesnelerinin (dummy thread objects) oluşturulma ihtimali vardır. Bunlar yabancı olarak kabul edilebilecek, kontrolleri threading modülünün dışında olan C kodları gibi iş parçacıklarıdır. Kukla iş parçacıklarının sınırlı işlevsellikleri vardır; daima canlı ve daemonic özelliktedirler ve `join()` ve diğerleri ile kullanılamazlar. Yabancı iş parçacıklarının sonlandırılmalarının saptanmasının imkânsız olduğu sürece asla silinemezler.

**class.threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *,**
    **daemon=None)**

	Bu yapıcı her zaman anahtar kelime argümanlarıyla birlikte çağrılmalıdır. Argümanlar şunlardır:

	    **group:** Değeri, `None` olmalıdır. `ThreadGroupClass` uygulandığında, gelecekteki genişletme için saklanır.

	    **target:** Değeri, `run()` metodu tarafından çalıştırılan, çağrılabilir bir nesnedir. Değeri ön tanımlı olarak `None` olur ve değeri `None` olursa hiçbir şeyin çağrılmayacağı anlamına gelir.

	    **name:** İş parçacığının ismidir. Ön tanımlı değeri özel olarak "Thread-N" biçiminden yapılmıştır. Buradaki N'nin değeri küçük ondalık bir sayıdır.

       	    **args:** Hedefin yürütülmesi için demet veri tipinde bir argümandır. Ön tanımlı olarak boş bir demet verisidir.

	    **kwargs:** Hedefin yürütülmesi için sözlük veri tipinde bir anahtar kelime argümanıdır. Ön tanımlı olarak boş bir sözlük verisidir.

 	    **daemon:** Eğer değeri `None` değilse, daemon, bir iş parçacığının bariz bir şekilde daemonic olup olmadığını ayarlar. Şayet değeri ön tanımlı olarak bırakılırsa (yani değeri `None` olursa), daemonic özellik o andaki aktif iş parçacığından miras alınır.

	    Eğer bir alt sınıf yapıcıyı iptal ederse, iş parçacığı ile bir işlem yapmadan önce, temel sınıfın yapıcısının (`Thread.__init__()`'in) çalıştırılmış olduğundan emin olunması gerekir.

  	    Sürüm 3.3.'de değiştirildi. Daemon argümanı eklendi.

	**start()**

            İş parçacığının etkinliğini başlatır.

            Her bir iş parçacığı için bir kez çağrılması gerekir. Ayrılmış iş parçacığı kontrolü içinde, `run()` metodunun çalıştırılmasını ayarlar.

            Bir iş parçacığı için, bu metot birden çok çağrıldığında, bir `RuntimeError` hatası yükseltir.

	**run()**

	    İş parçacığının etkinliğini temsil eder.

	    Bu metodu, bir alt sınıfta iptal edebilirsiniz. Standart `run()` metodu, *target* argümanı olarak bilinen nesnenin yapıcısına atanmış çağrılabilir nesneyi, varsa *args* ve kwargs* argümanlarından alınan ardışık ve anahtar kelimeli argümanlarla birlikte sırasıyla çalıştırır.

	**join(timeout=None)**

            İş parçacığı sonlana kadar bekler. Bu; `join()` metodu çağrılan iş parçacığı ya normal olarak, ya yürütülemeyen bir beklenti vasıtasıyla ya da seçeneğe bağlı zaman aşımı gerçekleşip sonlana kadar, çağrılan başka bir iş parçacığını bloke eder.

            *timeout* (zaman aşımı) argümanı hazır olduğunda ve değeri `None` olmadığında, işlemin zaman aşımını saniye olarak belirten, kayan noktalı bir sayı olmalıdır. `join()` her zaman `None` değerini geri döndürdüğü için, bir zaman aşımının gerçekleşip gerçekleşmediğine karar vermek için `join()` sonrasında `is_alive()` metodunu çağırın. Şayet iş parçacığı halen canlı ise, `join()`’in çağrılması zaman aşımına uğrar.

            timeout argümanı hazır olmadığında ve değeri `None` olmadığında, işlem, iş parçacığı sonlana kadar bloke olacaktır.

            Bir iş parçacığı için birçok kez `join()` metodu çağrılabilir.

            Bir girişim, hali hazırdaki iş parçacığını bir çıkmaza sokarsa,  `join()` metodu bir `RuntimeError` hatası yükseltir. Aynı hata, bir iş parçacığı başlatılmadan önce `join()` metodu çağrılırsa da yükseltilir.

        **Name**

            Sadece tanımlama amaçları için bir karakter dizisi (string) kullanılır. Bir anlamı yoktur. Çoklu iş parçacıklarına aynı isim verilebilir. Başlangıç ismi yapıcı tarafından ayarlanır.

        **getName()**

        **setName()**

            İsim için eski program uygulama ara yüzü alıcısı/ayarlayıcısı. Name özelliği (property) yerine doğrudan bunu kullanın.

        **ident**

            İş parçacığının tanıtlayıcısıdır veya eğer bir iş parçacığı başlatılmamışsa değeri `None`’dır. Değeri sıfır olmayan bir tamsayıdır. Daha fazla bilgi için `_thread.get_ident()` fonksiyonuna bakın. İş parçacığı tanıtlayıcıları, bir iş parçacığı sonlandığında ve başka bir tanesi oluşturulduğunda geri dönüştürülebilir. İş parçacığı sonlandıktan sonra bile tanıtlayıcı kullanılabilir.

        **is_alive()**

            Bir iş parçacığının aktif olup olmadığının öğrenilmesini sağlar.

            Bu metot; `run()` metodunun başlamasından önce ve `run()` metodunun sonlanmasına kadar `True` değerini geri döndürür. `enumerate()` modül fonksiyonu bütün canlı iş parçacıklarının bir listesini geri döndürür.

        **daemon**

            Bir iş parçacığının, bir daemon iş parçacığı olup olmadığının belirleyen bir boolean (`True` veya `False`) değeridir. Bu özellik `start()` metodu çağrılmadan önce ayarlanmalıdır aksi halde bir `RuntimeError` hatası yükseltilir. Başlangıçtaki değeri, oluşturulan iş parçacığından miras alınır; ana iş parçacığı bir daemon iş parçacığı değildir, böylece ana iş parçacığı içinde oluşturulan bütün iş parçacıklarının daemon değeri ön tanımlı olarak `False` olur.

            Geriye, cansız, daemon olmayan iş parçacıkları kaldığında, bütün Python programı sonlandırılır.

        **isDaemon()**

        **setDaemon()**

            Daemonun eski alıcı/ayarlayıcı program uygulama ara yüzü; bir özellik olarak kullanmak yerine doğrudan bunu kullanın.

**CPython Uygulaması Hakkında Ayrıntı:** CPython’da, Global Yorumlayıcı Kilidinden (Global Interpreter Lock) ötürü yalnızca bir adet iş parçacığı bir kere Python kodunu çalıştırabilir (belirli performans odaklı kütüphanelerin bu kısıtlamanın üstesinden gelmesine rağmen). Eğer uygulamanızın çok çekirdekli makinelerin hesaplama kaynaklarından daha fazla yararlanmasını istiyorsanız `multiprocessing`’i veya `concurrent.futures.ProcessPoolExecutor`’u kullanmanız tavsiye edilir. Yine de çoklu girdi/çıktı görevlerini eş zamanlı olarak çalıştırmak istiyorsanız, `threading` bunun için halen uygun bir modeldir.

Lock (Kilit) Nesneleri
=======================

Bir ilkel kilit, kilitlendiğinde belirli bir iş parçacığına ait olmayan, bir eşzamanlama ilkelidir. Bu kilit, Python’da, doğrudan `_thread` uzantı modülünden uyarlanan,  hali hazırda kullanılabilir olan en düşük seviyedeki eşzamanlama ilkelidir.

Bir ilkel kilitin “kilitli (=locked)” ve “kilitli değil (=unlocked)” olmak üzere iki tane durumu vardır. Bu kilit oluşturulurken “kilitli değil” durumundadır. Kilidin iki tane temel metodu vardır; `acquire()` ve `release()`. Kilidin durumu “kilitli değil” olduğunda, `acquire()` durumu “kilitli” hale çevirir ve acil olarak geri döndürülür. Kilidin durumu “kilitli” olduğunda, bir başka iş parçacığında `release()` çağrılıp, durumu “kilitli değil” şeklinde değiştirene kadar, `acquire()` iş parçacığını bloke eder, daha sonra `acquire()` çağrısı kilidi “kilitli” şeklinde sıfırlar ve geri döndürür. `release()` metodu, kilit sadece “kilitli” durumda iken çağrılmalıdır; bu metot, kilidin durumunu “kilitli değil” diye değiştirir ve acil olarak geri döndürülür. Şayet bir girişim kilitli olmayan bir kilidi serbest bırakmaya çalışırsa, bir adet `RuntimeError` hatası yükseltilir.

Kilitler ayrıca içerik yönetim protokolünü de desteklerler.

Birden fazla iş parçacığı `acquire()` ile bloke edilip, kilit durumlarının “kilitli değil” şeklinde  değişmesi beklendiğinde, sadece bir iş parçacığının kilidi, `release()` çağrısıyla “kilitli değil” durumuna getirilir; bekleyen iş parçacıklarından hangisinin getirileceği tanımlı değildir ve uygulamalara bağlı olarak değişiklik gösterebilir.

Tüm metotlar otomatik olarak yürütülür.

**Class threading.Lock**

    Sınıf, ilkel kilit nesnelerini uyarlar. Bir kez bir iş parçacığına kilit kazandırıldığında, sonraki girişimler, kilit serbest bırakılana kadar, iş parçacığını bloke eder; herhangi bir iş parçacığı kilidi serbest bırakabilir.

    Sürüm 3.3.’de değiştirildi. Kurucu fonksiyondan bir sınıfa değiştirildi.

    **acquire(blocking=True, timeout=-1)**

        Bloklayan veya bloklamayan bir kilit kazandırır.

        *blocking* argümanı `True` olarak (ön tanımlı değerdir) çağrıldığında, kilit serbest bırakalana kadar iş parçacığını bloke eder ve sonra kilidi tekrar “kilitli” konuma getirir ve `True` değerini geri döndürür.

        *blocking* argümanı `False` olarak çağrıldığında, iş parçacığını bloke etmez. Şayet bir çağrı *blocking*’i `True` olarak ayarlarsa, iş parçacığını bloke eder ve acil olarak `False` değerini geri döndürür; diğer türlü, kilidi “kilitli” duruma getirir ve `True` değerini döndürür.

        Kayan noktalı *timeout* (zaman aşımı) argümanı pozitif bir değer alarak çağrıldığında, en çok *timeout* argümanında belirtilen değere kadar, kilitlenemediği sürece iş parçacığını bloke eder. *timeout* argümanının -1 olması sınırsız bir bekleme süresi olacağını belirtir. Blocking argümanı `False` ayarlandığında, bir *timeout* argümanı belirlemek yasaklanmıştır.

        İş parçacığı başarıyla kilitlenmişse, geri dönen değer `True` olur, şayet başarıyla kilitlenmemişse `False` olur (örneğin zaman aşımına uğramışsa).

        Sürüm 3.2.’de değiştirildi. *timeout* parametresi yenidir.

        Sürüm 3.2.’de değiştirildi. Kilitleme POSIX’te sinyaller tarafından şimdi iptal edilebilir.

    **release()**

        Bir kilidi serbest bırakır. Bu metot, kilitlenmiş bir iş parçacığı hariç her iş parçacığından çağrılabilir.

        Kilit “kilitli” duruma getirildiğinde, onu “kilitli değil” şeklinde değiştirir ve geri döndürür. Eğer başka iş parçacıkları, kilitlerinin “kilitli değil” şeklinde değişmelerini bekleyerek bloke edilmişse, ilerlemek için kesin olarak bir tanesine izin verin.

        Kilitli olmayan bir kilit çağrıldığında, bir `RuntimeError` hatası yükseltilir.

        Bu metot ile geri dönen bir değer yoktur.

Rlock (Yeniden Girilir Kilit) Nesneleri
========================================

Bir yeniden girilir kilit, aynı iş parçacığı tarafından bir çok kere kullanıma sokulabilen bir eş zamanlama ilkelidir. Dahili olarak, bu kilit, ilkel kilitlerin kullandığı kilitli/kilitli değil durumuna ilaveten “sahip olunan iş parçacığı” ve “recursion (öz yineleme)” kavramlarını kullanır. Kilitli durumda, bazı iş parçacıkları bu kilide sahip olurken; kilitli olmadığı durumda, hiçbir iş parçacığı bu kilide sahip değildir.
Kilidi kilitlemek için, iş parçacığı bu kilidin `acquire()` metodunu çağırır; bu işlem iş parçacığının kilide sahip olduğunu bir kez geri döndürür. Kilidi açmak için, iş parçacığı kilidin `release()` metodunu çağırır. `acquire()` / `release()` çağrı çiftleri iç içe geçebilir; sadece son `release()` çağrısı (en dıştaki çağrı çiftinden olan `release()`) kilidi “kilitli değil” duruma getirir ve `acquire()` ile bloklanmış diğer iş parçacığının ilerlemesi için izin verir.

Yeniden girilir kilitler ayrıca içerik yönetim protokolünü desteklerler.

**Class threading.Rlock**

    Bu sınıf yeniden girilir kilit nesnelerini uygular. Bir yeniden girilir kilit, onu edinmiş bir iş parçacığı tarafından serbest bırakılmalıdır. Bir iş parçacığı bir kez yeniden girilir bir kilidi edindiğinde, aynı iş parçacığı kilidi engellemeden tekrar edinebilir; iş parçacığı, kilidi her edinmesine karşılık bir kez onu serbest bırakmalıdır.

    `Rlock`’ın, platform tarafından desteklenen, `Rlock` sınıfının elle tutulur en etkili versiyonunu geri döndüren bir kurucu fonksiyonu olduğunu not edin.

    **acquire(blocking=True, timeout=-1)**

        Bloklayan ve bloklamayan bir kilit edinin.

        Argümansız çağrıldığında: Eğer bu iş parçacığı zaten kilide sahipse, öz-yineleme seviyesini 1 derece arttırır ve ani bir şekilde geri döndürür. Diğer türlü, eğer başka bir iş parçacığı bu kilide sahipse, kilit çözülene kadar iş parçacığını engeller. Eğer bir kez -hiç bir iş parçacığının sahibi olmadığı- bir kilit açılmışsa, sahibini yakalar, öz-yineleme değerini 1 olarak ayarlar ve geri döndürülür. Eğer birden fazla iş parçacığı kilit açılana kadar engelleniyorsa, her seferinde sadece bir tane iş parçacığı bu kilide sahip olacaktır. Bu durumda geri dönen bir değer olmaz.

        *blocking* argümanı `True` olarak ayarlanıp çağrılırsa, argümansız çağrıldığında yaptıklarının aynısını yapar ve `True` değeri geri döndürülür.

        *blocking* argümanı `False` olarak ayarlanıp çağrılırsa, iş parçacığını bloke etmez. Eğer argümanı olmayan bir çağrı engellenirse, hızlı bir şekilde `False` değeri geri döndürülür; diğer türlü, argümansız çağrıldığında yaptıklarının aynısını yapar ve `True` değeri geri döndürülür.

        *timeout* argümanı pozitif bir kayan noktalı sayı olarak ayarlanıp çağrılırsa, iş parçacığı *timeout* argümanında belirlenen saniye kadar kilidi tekrar edinemediği sürece engellenir. Kilit edinilmişse `True` değerini geri döner, *timeout* zamanı dolmuşsa `False` değeri geri döner.

        Sürüm 3.2.’de değiştirildi. *timeout* parametresi yenidir.

    **release()**

        Bir kilidi serbest bırakır, öz yineleme (recursion) seviyesini azaltır. Öz yineleme değeri, azaltımdan sonra sıfır olursa, (hiç bir iş parçacığı tarafından sahip olunmayan) kilidi "kilitli değil" şeklinde sıfırlar ve diğer iş parçacıkları kilidin açılmasını beklemek için engellenirse, bu iş parçacıklarından kesinlikle bir tanesine işlenmesi için izin verir. Eğer öz yineleme seviyesi azaltımdan sonra halen sıfır olmamışsa, kilit "kilitli" duruma gelir ve çağrılan iş parçacığı tarafından sahiplenilir.

        Bu yöntemi sadece çağrılan iş parçacığı bir kilide sahip olduğu zaman çağırın. Eğer kilit, açık durumda ise, bu yöntemi çağırmak bir `RuntimeError` hatası yükseltir.

        Geri dönen bir değer yoktur.

Condition (Durum) Nesneleri
============================

Bir durum değişkeni her zaman bir kilitle ilişkilidir; bu değişken içeri aktarılabilir veya varsayılan olarak bir tane oluşturulabilir. Bir tanesini içeri aktarmak, bir kaç durum nesnesi aynı kilidi ortaklaşa kullandığında kullanışlıdır. Kilit, durum nesnesinin bir parçasıdır: onu ayrı olarak izleyemezsiniz.

Bir durum nesnesi, içerik yönetim protokolüne uyar: Ekli engelleme süresi için durum değişkenini `with` deyimi ile birlikte kullanmak ilgili kilidi elde edilmesini sağlar. `acquire()` ve `release()` yöntemleri ayrıca bahsi geçen kilitle ilgili olan yöntemleri çağırır.

Diğer yöntemler tutulan kilitle birlikte çağrılmalıdır. `wait()` yöntemi kilidi serbest bırakır ve sonra iş parçacığı onu `notify()` veya `notify_all()` ile çağırıp uyandırana kadar, iş parçacığını engeller. Bir kez uyandırıldığında, `wait()` onu yeniden edinir ve geri döndürür. Ayrıca bir zaman aşımı süresi belirlemek de mümkündür.

`notify()` yöntemi, eğer iş parçacıklarının herhangi biri bekliyorsa, durum değişkenini bekleyen iş parçacıklarından birisini uyandırır. `notify_all()` yöntemi ise durum değişkenini bekleyen bütün iş parçacıklarını uyandırır.

**Not:** `notify()` ve `notify_all()` yöntemleri kilitleri serbest bırakmaz; bu, `notify()` veya `notify_all()`'u çağırmış ve sonunda kilidin sahiplğinden feragat eden bir iş parçası veya iş parçacıkları uyandırıldığında, `wait()` çağrısı ile acil olarak geri döndürülmeyecekleri anlamına gelir.

Durum nesneleri kullanan tipik programlama stillinde kilit, bazı paylaşılan durumlara erişimi senkronize etmek için kullanılır; belirli durum değişimleriyle ilgili olan iş parçacıkları, `notify()` veya `notify_all()`'u çağırırken, bekleyenler için olası istenilen bir duruma göre durumu değiştirdiklerinde, istenen durumu görene kadar tekrar tekrar `wait()` yöntemini çağırır. Örneğin; takip eden kod, sınırsız bir tampon kapasitesine sahip genel bir üretici-tüketici durumudur::

    # Bir item'i tüketir
    with cv:
        while not an_item_is_available():
            cv.wait()
        get_an_available_item()

    # Bir item'i üretir
    with cv:
        make_an_item_available()
        cv.notify()

`while` döngüsü uygulamanın durumunu kontrol etmek için gereklidir, çünkü `wait()` keyfi olarak uzun bir sürede geri dönebilir ve `notify()` çağrısını bildiren koşul, hiç bir zaman doğru olmayabilir. Bu çoklu iş parçacığı programlamaya özgü bir durumdur. `wait_for()` yöntemi durum kontrolünü otomatik hale getirmek ve zaman aşımı hesaplamalarını kolaylaştırmak için kullanılır::

    # Bir item'i tüketir
    with cv:
        cv.wait_for(an_item_is_available)
        get_an_available_item()

Sadece bir veya bir kaç bekleyen iş parçacığının, durum değişmesiyle ilgili olup olmamadıklarına göre `notify()` ve `notify_all()` arasında seçim yapın. Örneğin, tipik bir üretici-tüketici durumunda, bir itemi tampona eklemek sadece bir tüketici iş parçacığının uyandırılmasını gerektirir.

**class threading.Condition(lock=None)**

    Bu sınıf durum değişkeni nesnelerini sağlar. Bir durum değişkeni bir veya birden çok iş parçacığının, başka bir iş parçacığı tarafından onaylanana kadar, beklemesine izin verir.

    Eğer *lock* argümanı veriliyse ve değeri `None` değilse, bir `Lock` veya `RLock` nesnesi olmalıdır ve temel kilit olarak kullanılmalıdır.Diğer türlü, yeni bir `RLock` nesnesi oluşturulur ve temel kilit olarak kullanılır.

    Sürüm 3.3'de değiştirildi: Kurucu fonksiyondan bir sınıfa değiştirildi.

    **acquire(*args)**

        Temel kilidi edinir. Bu yöntem temel kilit üzerinde ilgili yöntemi çağırır; geri dönen değer, yöntem neyi geri döndürüyorsa o olur.

    **release()**

        Temel kilidi serbest bırakır. Bu yöntem temel kilit üzerinde ilgili yöntemi çağırır; geri dönen bir değeri yoktur.

    **wait(timeout=None)**

        Onaylanana veya zaman aşımına uğrayana kadar bekler. Eğer çağıran iş parçacığı bu kilidi edinmemişse, bu yöntem çağrıldığında bir `RuntimeError` hatası yükseltilir.

        Bu yöntem temel kilidi serbest bırakır ve sonra başka bir iş parçacığının içindeki aynı durum değişkeni için `notify()` veya `notify_all()` çağrısı tarafından uyandırılana kadar veya seçime bağlı zaman aşımı gerçekleşene kadar iş parçacığını engeller. Bir kez uyandırıldığında veya zaman aşımına uğradığında, kilidi yeniden edinir ve geri döndürür.

        *timeout* argümanı belirlenmiş ve değeri `None` olmadığında, değeri, işlemin zaman aşımı süresini saniyelerle belirten kayan noktalı bir sayı olmalıdır.

        Temel kilit `RLock` olduğunda, `release()` yöntemi kullanılarak serbest bırakılamaz, çünkü bu durum birden çok kez öz yinelemeli olarak elde edildiğinden kilidi açmaz. Bunun yerine, `RLock` sınıfının iç arayüzü, öz yinelemeli olarak bi çok defa elde edilse bile gerçekten kitler. Sonra diğer bir iç arayüz, kilit yeniden edinildiğinde ön yineleme seviyesini yeniden düzenlemek için kullanılır.

        Belirli bir zaman aşımına uğramadığı sürece, geri dönen değer `True` olur, bu durumda ise geri dönen değer `False` olur.

        Sürüm 3.2'de değiştirildi: Önceden yöntem hep `None` değerini geri döndürüyordu.

    **wait_for(predicate, timeout=None)**

        Bir durum doğru değerlendirene kadar bekler, *predicate (=yüklem)* sonucu bir boolean değer olarak yorumlanacak olan, çağrılabilir bir şey olmalıdır. *timeout* argümanı maksimum bekleme zamanı olarak sağlanmıştır.

        Bu araç yöntemi `wait()`'i  yüklem sağlanana kadar veya zaman aşımı oluşana kadar tekrar tekrar çağırabilir. Geri dönen değer yüklemin son geri dönen değeridir ve yöntem zaman aşımına uğrarsa `False` olarak değerlendirilir.

        *timeout* özelliğini yok saymak, bu yöntemi çağırmak kabaca aşağıdakini yazmakla eşdeğerdir::

            while not predicate():
                cv.wait()

        Bu yüzden, aynı kural `wait()` ile aynı şekilde kullanılır: Kilit çağrıldığında tutulur ve geri döndürmede yeniden elde edilir. Yüklem, tutulan kilit ile  değerlendirilir.

        Sürüm 3.2'de gelen yeni bir özellik.

    **notify(n=1)**

        Ön-tanımlı olarak, varsa bu durumu bekleyen bir iş parçacığını uyandırır. Eğer çağrılan iş parçacığı bu yöntem çağrıldığında daha önce kilidi edinmemişse, bir `RuntimeError` hatası yükseltilir.

        Bu yöntem en fazla *n* tane durum değişkenini bekleyen iş parçacığını uyandırır; hiç bir iş parçacığı beklemiyorsa, işlem yapılmaz.

        Hali hazırdaki uygulama, eğer en az *n* tane iş parçacığı bekliyorsa, kesinlikle *n* tane iş parçacığını uyandırır. Ancak, bu davranışa
        güvenmek pek güvenilir değildir. İleride, iyileştirilmiş bir uygulama zaman zaman *n* taneden fazla iş parçacığı uyandırabilir.

        **Not:** Uyandırılmış bir iş parçacığı, kilidi yeniden elde edinceye kadar `wait()` tarafından geri dönmez. `notify()` kilidi serbest bırakmıyorsa, çağıranı serbest bırakmalıdır.

    **notify_all()**

        Bu durumu bekleyen bütün iş parçacıklarını uyandırır. Bu yöntem `notify()` gibi davranır, fakat bir tanesi yerine, bekleyen bütün iş parçacıklarını uyandırır. Eğer bu yöntem çağrıldığında, çağıran iş parçacığı kilidi daha önce edinmemişse, bir `RuntimeError` hatası yükseltilir.

Semaphore Nesneleri
====================

Bu, bilgisayar bilimi tarihindedeki en eski senkronizasyon ilkellerinden biridir, Hollandalı bilgisayar bilimcisi Edsger W. Dijkstra tarafından icat edilmiştir (`acquire()` ve `release()` yerine `P()` ve `V()` isimlerini kullanıyordu.).

Bir semafor, her `acquire()` çağrısında azaltılan ve her `release()` çağrısında arttırılan içsel bir sayacı yönetir. Sayaç sıfırın altına hiç
bir zaman inemez; `acquire()` bu sayacın sıfır olduğunu bulursa, iş parçacığını başka bir iş parçacığı `release()`'i çağırana kadar engeller.

Semaforlar ayrıca içerik yönetim protokülünü desteklerler.

**class threading.Semaphore(value=1)**

    Bu sınıf semafore nesnelerini uygular. Bir semafor `release()`'in çağrılma sayısından, `acquire()`'in çağrılma sayısını çıkartan ve bir başlangıç değerini eklemekle temsil edilen bir sayacı yönetir. `acquire()`, sayacı negatif bir sayı yapmadan geri döndürene kadar, eğer gerekliyse iş parçacığını engelleyebilir. Eğer verili değilse, *value* argümanının değeri ön-tanımlı olarak 1'dir.

    Seçeneğe bağlı argüman, iç sayacın başlangıc değerini verir; ön-tanımlı olarak değeri 1'dir. Eğer *value* argümanının değerine 1'den az bir sayı verilirse, `ValueError` hatası yükseltilir.

    Sürüm 3.3'de değiştirildi. Kurucu fonksiyondan bir sınıfa değiştirildi.

    **acquire(blocking=True, timeout=None)**

        Bir semafor elde eder.

        Argümanlar olmadan çağrıldığında: eğer iç sayaç girişte sıfırdan büyükse, onu bir birim azaltır ve acilen geri döner. Eğer girişte değeri sıfır ise, başka bir iş parçacığı `release()`'i çağırıp değerini sıfırdan daha büyük bir sayı yapana kadar, engeller. Bu uygun bir kilitleyici ile birlikte yapılır böylece bir çok `acquire()` çağrıları engellenir, `release()` bunlardan kesinlikle bir tanesini uyandıracaktır. Uygulama bir tanesini rastgele seçer, böylece engellenmiş iş parçacıkları uyandırıldığında oluşan düzene güvenmemek gerekir. `True` değeri geri döner (veya süresiz olarak engeller).

        *blocking* argümanı `False` olarak ayarlanmış bir şekilde çağrılırsa, iş parçacığını engellemez. Eğer argümansız bir çağrı iş parçacığını engellerse, acil olarak `False` değerini geri döndürür; diğer türlü, argümansız olarak çağrıldığının aynısını yapar ve `True` değerini geri döndürür.

        *timeout* argümanı `None`'dan farklı bir şey olacak şekilde çağrılırsa, en fazla *timeout* argümanındaki belirtilen saniye kadar iş parçacığını engeller. Eğer bu arada elde etme başarılı bir şekilde tamamlanmamışsa, `False` değerini geri döndürür. Diğer türlü, `True` değerini geri döndürür.

    **release()**

        Bir semaforu serbest bırakır, iç sayacı bir birim arttırır. Girişte sıfır olduğunda ve diğer bir iş parçacığı, sayacın tekrar sıfırdan büyük bir sayı olmasını beklediğinde, bu iş parçacığını uyandırır.

**class threading.BoundedSemaphore(value=1)**

    Bu sınıf, bağlanmış semafor nesnesini uygular. Bağlanmış semafor, hali hazırdaki değerin, ilk değeri aşmadığından emin olmak için kontrol eder. Eğer aşmışsa, `ValueError` hatası yükseltilir. Bir çok durumda semaforlar sınırlı kapasiteli kaynakları korumak için kullanılır. Eğer semafor birden fazla kez serbest bırakılmışsa, bu bir bug olduğuna işarettir. Eğer verili değilse, *value* argümanının ön-tanımlı değeri 1'dir.

    Sürüm 3.3'de değiştirildi. Kurucu fonksiyondan sınıfa değiştirildi.

**Semafor Örneği**

Semaforlar genellikle sınırlı kapasiteli kaynakları korumak için kullanılır, örneğin, bir veritabanı sunucusunda. Kaynağın boyutunun sabit olduğu hangi durumda olursa olsun, bağlanmış bir semafor kullansanız iyi olur. Çalışan iş parçacıklarını oluşturmadan önce, ana iş parçacığınız semaforu başlatacaktır::

    maxconnections = 5
    # ...
    pool_sema = BoundedSemaphore(value=maxconnections)

Bir kez oluşturulduğunda, çalışan iş parçacıkları semafor'un `acquire()` ve `release()` yöntemlerini, sunucuya bağlanmaya ihtiyaç duyduklarında çağırır::

    with pool_sema:
        conn = connectdb()
        try:
            # ... bağlantıyı kullan ...
        finally:
            conn.close()

Bağlanmış semaforun kullanılması, elde edildiğinden daha fazla serbest bırakılması gibi bir programlama hatasını tespit edememe şansını azaltır.

Event (Olay) Nesneleri
======================

Bu, iş parçacıkları arasındaki iletişim için en basit mekanizmadır: Bir iş parçacığı bir olayı sinyal eder ve diğer iş parçacığı da bunu bekler.

Bir olay nesnesi `set()` yöntemi ile değeri `True` olan ve `clear()` yöntemiyle de değeri `False` olan bir iç işareti yönetir. `wait()` yöntemi işaretin değeri `True` olana kadar iş parçacığını engeller.

**class threading.Event**

    Bu sınıf olay nesnelerini uygular. Bir olay, `set()` yöntemi ile değeri `True` olan v `clear()` yöntemiyle de değeri `False` olan bir işareti yönetir. `wait()` yöntemi iş parçacığını, işaretin değeri `True` olana kadar engeller. İşaretin değeri ilk olarak `False`'dur.

    Sürüm 3.3'de değiştirildi. Kurucu bir fonksiyondan bir sınıfa değiştirildi.

    **is_set()**

        Sadece iç işaret `True` olduğunda `True` değerini geri döndürür.

    **set()**

        İç işareti `True` olaak ayarlar. `True` olmasını bekleyen bütün iş parçacıkları uyandırılır. `wait()`'i çağıran iş parçacığı, bir kez işaret `True` olursa, bir daha engellenmeyecektir.

    **clear()**

        İç işareti `False` olarak sıfırlar. Sonradan, `wait()`'i çağıran iş parçacıkları, `set()`, iç işareti tekrar `True` yapana kadar engellenecektir.

    **wait(timeout=None)**

        İç işaret `True` olana kadar iş parçacığını engeller. Eğer girişte iç işaret `True` olursa, acil olarak geri döner. Diğer türlü, başka bir iş parçacığı, işareti `True` yapmak için `set()`'i çağırana kadar veya seçime bağlı *timeout* süresi dolana kadar, iş parçacığını engeller.

        *timeout* argümanı kullanılarak çağrıldığında ve değeri `None` olmadığında, değeri, işlemin zaman aşımı süresini saniyelerle belirten kayan noktalı bir sayı olmalıdır.

        Bu yöntem, ancak iç işaretin değeri `True` olarak ayarlanmışsa, `True` değerini geri döndürür, `wait()` çağrısından önce veya çağrı başladıktan sonra, *timeout* değeri verilmemişse ve işlem zaman aşımına uğramamışsa her zaman `True` değerini geri döndürür.

        Sürüm 3.1'de değiştirildi: Daha önceden, bu yöntem her zaman `None` değerini geri döndürürdü.

Timer (Zamanlayıcı) Nesneleri
==============================

Bu sınıf, sadece belirli bir zaman geçtikten sonra çalıştırılan bir eylemi, -bir zamanlayıcıyı- temsil eder. `Timer`, `Thread`'in bir alt sınıfı olup, ayrıca özel bir iş parçacığı oluşturma işlevi örneğidir.

Zamanlayıcılar, tıpkı iş parçacıkları gibi `start()` yöntemi çağrılarak başlatılır. Zamanlayıcı (eylemi başlamadan önce) `cancel()` yöntemi çağrılarak durdurulabilir. Zamanlayıcının eyleminin gerçekleşmesininden önce bekleyeceği aralık, kullanıcının tanımladığı aralık olmayabilir.

Örneğin::

    def hello():
        print("hello, world")

    t = Timer(30.0, hello)
    t.start()  # 30 saniye sonra, "hello, world" yazısı ekrana bastırılacak.

**class threading.Timer(interval, function, args=None, kwargs=None)**

    *interval (=aralık)* argümanında belirtilen saniyelerden sonra, *args* argümanları ve *kwargs* anahtar argümanlarıyla birlikte çalışan bir fonksiyonun atandığı bir zamanlayıcı oluşturur. Eğer *args*, `None` (ön-tanımlı değeri bu) ise, boş bir liste kullanılacaktır. Eğer *kwargs*, `None` ise (ön-tanımlı değeri bu) ise, boş bir sözlük kullanılacaktır.

    Sürüm 3.3'de değiştirildi: Kurucu fonksiyondan sınıfa değiştirildi.

    **cancel()**

        Zamanlayıcıyı durdurur ve zamanlayıcının eyleminin çalıştırılmasını iptal eder. Bu sadece eğer zamanlayıcı halen kendi bekleme evrendiseyse çalışır.

Barrier (Engel) Nesneleri
==========================

Sürüm 3.2'de gelen yeni bir özelliktir.

Bu sınıf, birbirini bekleme ihtiyacında olan sabit sayıdaki iş parçacıklarının kullanması için basit senkronizasyon ilkelleri sağlar. Her bir iş parçacığı `wait()` yöntemini çağırarak engeli aşmaya çalışır ve bütün iş parçacıkları aynı çağrıyı yapana kadar da iş parçacıkları engellenir. Bu noktada bütün iş parçacıkları aynı anda serbest bırakılır.

Engel aynı sayıdaki iş parçacıkları için bir çok kez tekrar kullanılabilir.

Aşağıdaki örnek, bir istemci ve sunucu iş parçacını senkronize etmek için basit bir yoldur::

    b = Barrier(2, timeout=5)

    def server():
        start_server()
        b.wait()
        while True:
            connection = accept_connection()
            process_server_connection(connection)

    def client():
        b.wait()
        while True:
            connection = make_connection()
            process_client_connection(connection)

**class threading.Barrier(parties, action=None, timeout=None)**

    Bir partide bulunan değişik sayıdaki iş parçacığı için bir engel nesnesi oluşturur. *action* argümanı yazıldığında, iş parçacıklarından biri tarafından, serbest bırakıldığı zaman çağrılan, çağrılabilir bir şeydir. *timeout* argümanı belirtilmediği zaman değeri `wait()` yöntemi için ön tanımlı değeridir.

    **wait(timeout=None)**

        Engeli geçer. İş parçacıkları partisi engele doğru bu fonksiyonu çağırmışsa, aynı anda hepsi birden serbest bırakılır. Eğer bir *timeout* değeri belirlenirse, sınıf yapıcısına verilmiş herhangi bir tercih için kullanılır.

        Geri dönen değer, 0 ile parti sayısının 1 eksiği arasında bir tamsayıdır, her bir iş parçacığı için değişebilir. Bu, bir takım özel idare işleri yapacak olan bir iş parçacığını seçmek için kullanılabilir. Örneğin::

            i = barrier.wait()
            if i == 0:
                # Sadece bir iş parçacığı bunu bastırmaya ihtiyaç duyar.
                print("engel geçildi")

        Eğer yapıcıya bir tane *action* sağlanmışsa, iş parçacıklarından bir tanesi serbest bırakılmadan önce onu çağırmış olacaktır. Bu çağrım bir hata yükseltirse, engel kırılan durumun içine yerleştirilir.

        Eğer çağrı zaman aşımına uğrarsa, engel kırılan durumun içine yerleştirilir.

        Bu yöntem, beklenildiği gibi, eğer engel kırılmışsa veya iş parçacığı beklerken sıfırlanmışsa, `BrokenBarrierError` hatası yükseltebilir.

    **reset()**

        Engeli ön-tanımlı değerine, boş duruma geri döndürür. Onu bekleyen her iş parçacığı `BrokenBarrierError` hatasını alır.

        Durumu bilinmeyen bazı iş parçacıkları olduğunda, bu fonksiyonun bazı dış senkronizasyonlara ihtiyaç duyabileceğini not edin. Eğer bir engel kırıldığında, onu terk edip, yeni bir tane oluşturmak daha iyi bir yoldur.

    **abort()**

        Bir engeli kırılmış bir duruma sokar. Bu, canlı veya ileride çağrılacak bütün çağrıları `BrokenBarrierError` hatasıyla başarısızlığa uğramaları için `wait()`'i yöntemini çağırır. Bunu, eğer uygulamayı çıkmazdan kurtarmak için, iptal edilmeye ihtiyaç duyuyorsa kullanın.

        Bu, iş parçacıklarından bir tanesinin ters gitmesine karşı hassas bir *timeout* değeri ile oluşturulmuş bir engeli otomatik olarak korumak için tercih edilebilir.

    **parties**

        Engeli geçmesi gereken iş parçacığı sayısıdır.

    **n_waiting**

        Hali hazırda engelde bekleyen iş parçacığı sayısıdır.

    **broken**

        Eğer engel kırılan durumun içindeyse, değeri `True` olan bir boolean verisidir.

**exception threading.BrokenBarrierError**

    Bu beklenti, `RuntimeError`'un bir alt sınıfıdır, `Barrier` nesnesi sıfırlandığında veya kırıldığında yükseltilir.

Kilitleri, Durumları ve Semaforları `with` deyimi ile birlikte kullanmak
=========================================================================

Bu modül tarafından sağlanan, `acquire()` ve `release()` fonksiyonuna sahip bütün nesneler içerik yönetimi olarak `with` deyimi için kullanılabilir.  `acquire()` yöntemi, engellemeye girildiğinde, `release()` yöntemi de engellemeden çıkıldığında çağrılacaktır. Bundan ötürü aşağıdaki kodlar::

    with some_lock:
        # Bir şeyler yap...

şu işlemin dengidir::

    some_lock.acquire()
    try:
        # Bir şeyler ya...
    finally:
        some_lock.release()

Hali hazırda, `Lock`, `RLock` `Condition`, `Semaphore` ve `BoundedSemapgore` nesneleri `with` deyimi içerik yönetimi olarak kullanılabilir.

Örnekler:
==========

**Örnek-1:**

Thread'ı kullanmanın en kolay yolu; onu bir hedef fonksiyonuyla örnekleyip, `start()` fonksiyonunu çağırarak çalıştırmaktır.

**Kodlar**::

    #/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading


    def f():  # Thread'in iş fonksiyon.
        print("iş")


    for i in range(4):
        t = threading.Thread(target=f)
        t.start()

**Kodların Açıklamaları:**

Yukarıdaki kodlarda, *f* isminde bir tane fonksiyon oluşturulmuş ve içine "iş" string verisini ekrana yazdıran bir *print()* fonksiyonu dahil edilmiştir. Daha sonra `for` döngüsünü kullanarak, dört tane iş parçacığı nesnesi örneği oluşturulmuştur. Bütün iş parçacıklarının hedef fonksiyonu, *f*'tir. Ve bu program çalıştırıldığında dört kere ekrana "iş" yazısı yazdırılır.

**Örnek-2:**

Bir iş parçacığı oluşturmak ve hangi işi yapacağını söylemek için argüman atamak kullanılacak yollardan birisidir. İkinci örnekte `thread`'in sonradan bastıracağı bir sayı argümanı fonksiyonda tanımlanmıştır.

**Kodlar**::

    #/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading


    def f(sayi):
        print("iş {}".format(sayi))


    for i in range(4):
        t = threading.Thread(target=f, args=(i, ))
        t.start()

**Kodların Açıklamaları:**

Bir iş parçacığı oluştururken, iş parçacığının etkin olacağı fonksiyonun eğer bir fonksiyon parametresi varsa, onu *args* parametresine yazarak, iş parçacığının hedefi olmasını sağlayabiliriz.


**Örnek-3:**

İş parçacıklarını adlanırmak veya tanıtmak için Örnek-2'de olduğu gibi argümanları kullanmak oldukça gereksizdir. Ancak bu demek değildir ki argüman kullanmak gereksizdir. Sadece iş parçacığının ismini belirtirken bu yöntemi kullanmak gereksizdir demek istiyorum. Yoksa argümanlara ihtiyaç duyacağımız çok fazla durumla karşılaşmamız mümkün. Şundan bahsetmek istiyorum; her `Thread` örneğinin ismiyle birlikte, iş parçacığı oluşturulduğunda değişen, rastgele bir değeri vardır. `Thread`'leri isimlendirmek, sunucu işlemleriyle, birçok farklı hizmet işlerinin birlikte yürütülmesinde kolaylık sağlar.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading
    import time


    def f():
        print(threading.currentThread().getName(), "Başlıyor")
        time.sleep(2)
        print(threading.currentThread().getName(), "Bitiyor")


    def g():
        print(threading.currentThread().getName(), "Başlıyor")
        time.sleep(5)
        print(threading.currentThread().getName(), "Bitiyor")


    t1 = threading.Thread(name="Birinci servis", target=f)
    t2 = threading.Thread(name="İkinci servis", target=g)
    t3 = threading.Thread(target=f)
    t4 = threading.Thread(target=g)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

**Kodların Açıklamaları:**

Bu örnekteki şu kısma bir bakalım::

    def f():
        print(threading.currentThread().getName(), "Başlıyor")
        time.sleep(2)
        print(threading.currentThread().getName(), "Bitiyor")

*f()* fonksiyonu çağrıldığında, ismi neyse o şekilde "filanca Başlıyor" şeklinde bir yazı ekrana bastırılacak. Sonra 2 saniye bekledikten sonra "filanca Bitiyor" şeklinde bir yazı ekrana bastırılacak.

Ancak bu durumu iş parçacığı nesnesini tanımlarken değiştirebiliyoruz. Yani::

    t1 = threading.Thread(name="Birinci servis", target=f)
    t2 = threading.Thread(name="İkinci servis", target=g)

yukarıda olduğu gibi iş parçacığını tanımladığımızda, t1 ve t2 iş parçacıklarına kendimiz isim vermiş oluyoruz. Bu isimleri vermediğimizde iş parçacığının ismi *Thread-1* şeklinde bir isme sahip olur. t3 ve t4 isimli iş parçacıklarının *name* argümanının yazılmamış olduğuna dikkat edin. Bu iki iş parçacığının ismimleri dolayısıyla *Thread-1* ve *Thread-2* olacaktır.

**Örnek-4:**

Şimdi gelin threading'i daha rahat anlayabileceğimiz bir örnek oluşturalım. Bildiğiniz gibi herhangi bir `tkinter` uygulamasını çalıştırabilmemiz için `mainloop()` fonksiyonunu çağırmamız gerekiyor. Ve bu fonksiyon, programı sonlandıran herhangi bir işlem tanımlanmamışsa, sürekli çalışır durumda oluyor. Peki biz aynı anda bir tanesi `tkinter`'e ait olan iki tane döngüyü aynı anda çalıştıramaz mıyız? Elbette çalıştırabiliriz, işte cevabı:

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    try:
        import Tkinter as tk
    except ImportError:
        import tkinter as tk
    import threading

    root = tk.Tk()
    entry = tk.Entry(master=root)
    entry.grid(row=0, column=0)


    def f():
        button = tk.Button(master=root, text="Button")
        while True:
            if entry.get() == "":
                button.grid_forget()
            else:
                button.grid(row=1, column=0)


    t1 = threading.Thread(target=f)
    t1.daemon = True
    t1.start()
    t1.join(1)
    root.mainloop()

**Kodların Açıklamaları:**

Bu örneği çalıştırdığınızda, göreceksiniz ki, *entry* widgetine yazı yazdığınızda *button* widgeti beliriyor, *entry* widgeti boş olduğunda ise ortadan kayboluyor. Bu işlem basit bir denetleme işlemidir ve tahmin edeceğiniz gibi fonksiyonun içindeki `while` döngüsü bu işe yarıyor. *t1* isimli `threading` örneğini oluşturduktan sonra onun *daemon* özelliğinin değerini `True` olarak değiştirdiğimizi görüyorsunuz. Bu işlemi yapmaktaki amacımız, programı sonlandırdığımızda, geriye sadece *daemonic* iş parçacıklarının kalmasını sağlamak ve böylece programdan çıkmamızı sağlamak. Eğer bu *daemon* özelliğini aktif hale getirmemiş olsaydık, `tkinter` penceresini kapattığımız halde, programın sonlanmadığını görürdük. `t1.join(1)` kodu da, bu iş parçacığının 1 saniye sonrası sonlanmasını istediğimizi belirtir.

**Örnek-5:**

Şimdi de `Lock` nesnesiyle alakalı bir örnek yapalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading


    def f():
        print("f fonksiyonu")


    def g():
        print("g fonksiyonu")


    def h():
        print("h fonksiyonu")


    t1 = threading.Thread(target=f)
    t2 = threading.Thread(target=g)
    t3 = threading.Thread(target=h)
    lock = threading.Lock()
    lock.acquire()
    t1.start()
    lock.acquire(blocking=True, timeout=3)
    t2.start()
    lock.acquire(blocking=True, timeout=1)
    t3.start()

**Kodların Açıklamaları:**

Önce gerekli modülü programın içine aktardık::

    import threading

Sonra farklı iş parçacıklarının çağıracağı üç tane fonksiyon tanımladık::

    def f():
        print("f fonksiyonu")


    def g():
        print("g fonksiyonu")


    def h():
        print("h fonksiyonu")

Daha sonra fonksiyonları iş parçacıklarının hedefihaline getirdik::

    t1 = threading.Thread(target=f)
    t2 = threading.Thread(target=g)
    t3 = threading.Thread(target=h)

Sonra kilit nesnemizi oluşturduk ve kilit nesnemizin `acquire()` fonksiyonunu argümansız olarak çağırdık. Eğer argümanlı çağırsaydık da değişen bir şey olmazdı, çünkü kilit bir sonraki `acquire()` fonksiyonunu çağırdığımız zaman engellemeye başlayacak::

    lock = threading.Lock()
    lock.acquire()

*t1* isimli iş parçacığını başlattık; engellenmeden çalışmaya başladı::

    t1.start()

Ve şimdi `lock.acquire()` yöntemini *blocking* ve *timeout* argümanlarıyla birlikte çağıralım. Bu yöntemi `t1.start()`'ı çağırmadan önce ikinci kez çağırsaydık o zaman, *t1* iş parçacığı da engellenecekti. *timeout* parametresine *3* yazalım. Yani 3 saniyeliğine diğer işlemleri engellesin::

    lock.acquire(blocking=True, timeout=3)

Üç saniye geçtikten sonra t2 iş parçacığını başlatalım::

    t2.start()

`lock.acquire()` fonksiyonunu bir kez daha çağırabiliriz, bu kez 1 saniyeliğine diğer görevleri engellesin::

    lock.acquire(blocking=True, timeout=1)

Ve son olarak da *t3* iş parçacığını başlatalım::

    t3.start()

Yukarıdaki örnekte, ekrana önce "f fonksiyonu" yazıldı, "f fonksiyonu" yazısı ekrana yazdırıldıktan üç saniye sonra ekrana "g fonksiyonu" yazıldı, ve "g fonksiyonu" ekrana yazdırıldıktan bir saniye sonra da "h fonksiyonu" ekrana yazıldı.

**Örnek-6:**
Şimdi de `acquire()` yöntemini bir kez yazarak, bu yöntemden sonra gelen işlemlerin engellenmediği bir örnek yazalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading


    class Thread(threading.Thread):
        def __init__(self, lock):
            threading.Thread.__init__(self)
            self.lock = lock

        def run(self):
            self.lock.acquire()
            print("{} kilidi edindi.".format(self.name))
            # self.lock.acquire(blocking=True, timeout=3)
            self.lock.release()
            print("{} kilidi serbest bıraktı.".format(self.name))


    __lock__ = threading.Lock()
    t1 = Thread(lock=__lock__)
    t2 = Thread(lock=__lock__)
    t1.start()
    t2.start()

**Kodların Açıklamaları:**

Her zamanki gibi önce modülümüzü programın içine aktaralım::

    import threading

Şimdi de `threading.Thread`'i miras alan bir sınıf oluşturalım. Ve bu sınıfın *lock* isminde bir tane de özelliği olsun::

    class Thread(threading.Thread):
        def __init__(self, lock):
            threading.Thread.__init__(self)
            self.lock = lock

Bildiğiniz gibi `threading.Thread()`'in `run()` isimli bir yöntemi var. Bu yöntemi *override* yapalım, yani modülün `run()` yöntemi yerine bizim yazacağımız `run()` yöntemi kullanılsın. Bu yöntem, ilk olarak `self.lock.acquire()` fonksiyonunu çağırsın. Hemen altında, iş parçacığının kilidi edindiğine dair mesajı ekrana yazdıran `print()` fonksiyonunu çağıralım. Bir altındaki yoruma alınmış `# self.lock.acquire(blocking=True, timeout=3)` kısmı, yorumdan çıkarırsanız, alttaki işlemlerin çalışabilmesi için üç saniye beklemek zorunda kalırsınız. `self.lock.release()` ile de kilidi serbest bırakıyoruz. ve `run()` fonksiyonunun son satırında da kilidin serbest bırakıldığına dair mesajı ekrana bastıran bir print()` fonksiyonu çağıralım::

        def run(self):
            self.lock.acquire()
            print("{} kilidi edindi.".format(self.name))
            # self.lock.acquire(blocking=True, timeout=3)
            self.lock.release()
            print("{} kilidi serbest bıraktı.".format(self.name))

Sınıfı oluşturduk, örnekleri oluşturmadan önce kilidimizi oluşturalım::

    __lock__ = threading.Lock()

Şimdi de iş parçacıklarımızı oluşturup onları başlatalım::

    t1 = Thread(lock=__lock__)
    t2 = Thread(lock=__lock__)
    t1.start()
    t2.start()

**Örnek-7:**

Şimdi de `RLock` ile ilgili bir örnek yapalım. `Lock` ile `RLock` arasındaki en belirgin fark, `Lock`'ın kilidini bir başka iş parçacığı açabilir olması, oysa `RLock`'ın kilidini, kilidi edinmiş olan iş parçacığının açması gerekir.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading


    class Thread(threading.Thread):
        def __init__(self, lock):
            threading.Thread.__init__(self)
            self.lock = lock

        def run(self):
            self.lock.acquire(blocking=True, timeout=3)
            print("{} çalışıyor.".format(self.name))
            self.lock.acquire(blocking=True, timeout=1)
            print("{} çalışması bitti.".format(self.name))


    __lock__ = threading.RLock()
    t1 = Thread(lock=__lock__)
    t2 = Thread(lock=__lock__)
    t1.start()
    t2.start()


**Kodların Açıklamaları:**

Her zamanki gibi önce `threadin` modülünü programın içine aktarıyoruz::

    import threading

*lock* parametresi olan ve `threading.Thread()` sınıfını miras alan bir sınıf oluşturuyoruz::

    class Thread(threading.Thread):
        def __init__(self, lock):
            threading.Thread.__init__(self)
            self.lock = lock

Yine `run()` yöntemini *override* edelim. Bu `run()` fonksiyonu altında çağırdığımız ilk fonksiyon `self.lock.acquire(blocking=True, timeout=3)` fonksiyonudur. Bu fonksiyon kilidi edinecek olan ilk iş parçacığına uygulanmaz. Bir sonraki satırda, iş parçacığının çalıştığına dair ekrana bir yazı yazdırıyoruz (`print("{} çalışıyor.".format(self.name))`). Onun da altında kilidi `self.lock.acquire(blocking=True, timeout=1)` fonksiyonu ile bir daha ediniyoruz. Bir iş parçacığı RLock kilidini ikinci kez kendi işlemlerini engellemeden elde edebilir. Ve `run()` yönteminin son satırında da çalışmanın bittiğine dair ekrana bir yazı yazdırıyoruz (`print("{} çalışması bitti.".format(self.name))`)::

        def run(self):
            self.lock.acquire(blocking=True, timeout=3)
            print("{} çalışıyor.".format(self.name))
            self.lock.acquire(blocking=True, timeout=1)
            print("{} çalışması bitti.".format(self.name))

Sınıfı oluşturduk, örnekleri oluşturmadan önce kilidimizi oluşturalım::

    __lock__ = threading.RLock()

Şimdi de iş parçacıklarımızı oluşturup onları başlatalım::

    t1 = Thread(lock=__lock__)
    t2 = Thread(lock=__lock__)
    t1.start()
    t2.start()

**Not:** Bu örnekte RLock kilidine sahip olan iş parçacığı *t1*'dir. Dolayısıyla kilidi sadece o açabilir. Bu örneği çalıştırdığınızda, *t1* iş parçacığının kilit edindiğini ama serbest bırakmadığını görüyoruz. Eğer *t1* bu kilidi serbest bıraksaydı, iş parçacıkları arasında bekleme süresi olmayacaktı.


**Örnek-8:**

Şimdi de `Condition()` ile ilgili bir örnek yapalım. Bu örnekte bir üretici bir de tüketici iş parçacığı oluşturacağız.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import time
    import threading


    class Uretici(threading.Thread):
        def __init__(self, condition, liste):
            threading.Thread.__init__(self)
            self.condition = condition
            self.liste = liste

        def run(self):
            count = 1
            while count < 10:
                self.condition.acquire()
                print("{} condition'u edindi.".format(self.name))
                self.liste.append(count)
                print("{} listeye {} tarafından eklendi."
                      .format(count, self.name))
                self.condition.notify()
                print("condition {} tarafından bildirildi.".format(self.name))
                self.condition.release()
                print("condition {} tarafından serbest bırakıldı."
                      .format(self.name))
                count += 1
                time.sleep(0.5)


    class Tuketici(threading.Thread):
        def __init__(self, condition, liste):
            threading.Thread.__init__(self)
            self.condition = condition
            self.liste = liste

        def run(self):
            while True:
                self.condition.acquire()
                print("{} condition'u edindi.".format(self.name))
                while True:
                    if self.liste:
                        sayi = self.liste.pop()
                        print("{}, {} {}".format(
                            sayi, self.name,
                            "tarafından listeden düşürüldü."))
                        break
                    print("condition {} {}".format(
                        self.name, "tarafından bekletiliyor."))
                    self.condition.wait()
                self.condition.release()
                print("condition {} {}".format(
                    self.name,
                    "tarafından serbest bırakıldı."))


    __condition__ = threading.Condition()
    __liste__ = []
    t1 = Uretici(condition=__condition__, liste=__liste__)
    t2 = Tuketici(condition=__condition__, liste=__liste__)
    t1.start()
    t2.start()

**Kodların Açıklamaları:**

Her zamanki gibi önce gerekli modülleri programın içine aktarıyoruz::

    import time
    import threading

Şimdi, `threading.Thread` sınıfının özelliklerini miras alan bir üretici sınıf tanımlayalım; bu sınıftan bir örnek türetilmek istendiği zaman kullanıcı *condition* argümanını ve *liste* argümanını girmek zorunda kalsın::

    class Uretici(threading.Thread):
        def __init__(self, condition, liste):
            threading.Thread.__init__(self)
            self.condition = condition
            self.liste = liste

Bu sınıfın bir tane `run()` metodu zaten mevcut ama biz bu `run()` metodunu değiştirelim::

        def run(self):

Bu `run()` yönteminde aşağıdakiler yapılsın:

    1. *count* isimli daha sonra `self.liste`'ye eklenmek üzere bir değişken tanımlayalım::

            count = 1

    2. Bir tane döngü oluşturalım, bu döngü *count*, 10'dan küçük olduğu sürece devam etsin::

            while count < 10:

    3. Döngü içinde iş parçacığı `Condition`'u edinsin ve ekrana da `Condition`'u elde ettiğine dair bir yazı yazdırılsın::

                self.condition.acquire()
                print("{} condition'u edindi.".format(self.name))

    4. İş parçacığı şimdi de *count* değişkenini `self.liste`'ye eklesin ve ekrana bu işlemle ilgili bir yazı yazdırılsın::

                self.liste.append(count)
                print("{} listeye {} tarafından eklendi."
                      .format(count, self.name))

    5. Sonra, iş parçacığı, durumunu bildirsin ve bildirildiğine dair ekrana bir yazı yazdırılsın::

                self.condition.notify()
                print("condition {} tarafından bildirildi.".format(self.name))


    6. Şimdi de iş parçacığı `Condition`'u serbest bıraksın ve serbest bıraktığına dair ekrana bir yazı yazdıralım::

                self.condition.release()
                print("condition {} tarafından serbest bırakıldı."
                      .format(self.name))

    7. *count* değişkenini 1 birim arttıralım ve `time.sleep(0.5)` fonksiyonunu çağırarak işlemler arasında biraz zaman geçmesini bekleyelim::

                count += 1
                time.sleep(0.5)

Şimdi de, `threading.Thread` sınıfının özelliklerini miras alan bir tüketici sınıf tanımlayalım; yine bu sınıftan bir örnek türetilmek istendiği zaman kullanıcı *condition* argümanını ve *liste* argümanını girmek zorunda kalsın::

    class Tuketici(threading.Thread):
        def __init__(self, condition, liste):
            threading.Thread.__init__(self)
            self.condition = condition
            self.liste = liste

Bu sınıfın da bir tane `run()` metodu zaten mevcut ama biz bu `run()` metodunu değiştirelim::

        def run(self):

Bu `run()` yönteminde aşağıdakiler yapılsın:

    1. Sonsuz bir döngü oluşturalım, bu döngü içerisindeki tüketici iş parçacığı `Condition`'u elde etsin ve elde ettiğine dair bilgiyi ekrana yazdıralım::

            while True:
                self.condition.acquire()
                print("{} condition'u edindi.".format(self.name))

    2. Bir tane daha sonsuz döngü oluşturalım, Bu döngüde de bir koşul oluşturalım, koşulumuz `self.liste` `True` değeri veriyorsa olsun ve bu koşul altında *sayi* isimli bir değişkeni `self.liste`'den düşürelim. Ekrana da iş parçacığının bu sayıyı listeden düşürdüğünün bilgisini yazdıralım, sonra da bu koşul altındaki döngüden çıkılsın::

                while True:
                    if self.liste:
                        sayi = self.liste.pop()
                        print("{}, {} {}".format(
                            sayi, self.name,
                            "tarafından listeden düşürüldü."))
                        break

    3. Yine ikinci döngünün içindeyken her zaman `Condition`'u bekletelim ve beklediğine dair yazı ekrana yazdırılsın, şayet bunu yapmazsak, döngü başa sardığında iş parçacığı `Condition`'u tekrar edinir ve program orada donup kalır::

                    print("condition {} {}".format(
                        self.name, "tarafından bekletiliyor."))
                    self.condition.wait()

    4. İlk döngümüzün içinde `Condition`'u serbest bırakalım. Bu örnekte `Condition()`u serbest bırakmazsak, bir sorunla karşılaşmayız. Ama iki tane tüketici olduğu durumlarda  `while` döngüsünü kırabilecek bir durum oluşturabiliriz ve döngü kırıldıktan sonra iş parçacığı kilidi hala tutmaya devam ediyor olabilir, bu yüzden kilidi serbest bırakmak gerekir::

                self.condition.release()
                print("condition {} {}".format(
                    self.name,
                    "tarafından serbest bırakıldı."))

Ve son olarak `Condition()`, `Uretici()`, `Tüketici()` sınıflarından birer örnek ve boş bir liste oluşturalım. `Condition()` sınıfından oluşturduğumuz örnek ve listeyi `Uretici()` ve `Tuketici()` sınıflarından oluşturduğumuz örneklere argüman olarak yazalım. Sonra da iş parçacıklarını çalıştıralım::

    __condition__ = threading.Condition()
    __liste__ = []
    t1 = Uretici(condition=__condition__, liste=__liste__)
    t2 = Tuketici(condition=__condition__, liste=__liste__)
    t1.start()
    t2.start()

**Not:** Bu örneği çalıştırdığımızda `Uretici()` sınıf örneği boş listeye 9 tane eleman ekleyecek ve `Tuketici()` sınıf örneği ise listeye eklenen bu elemanları tek tek silecek. Ve son olarak `Tuketici()` sınıfı kendisini beklemeye alacak.

**Örnek-9:**

Şimdi de `Semaphore()` nesnesiyle alakalı bir örnek yapalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import time
    import threading

    semaphore = threading.Semaphore()


    def f():
        print("f fonksiyonu başlıyor.")
        semaphore.acquire()
        print("f fonksiyonu semaforu edindi.")
        for i in range(5):
            print("f fonksiyonu '{}' itemini işliyor.".format(i))
            time.sleep(1)
        semaphore.release()
        print("f fonksiyonu semaforu serbest bırakıyor.")
        print("f fonksiyonu bitiyor.")


    def g():
        print("g fonksiyonu başlıyor")
        while not semaphore.acquire():
            print("Semafor henüz kullanılamıyor.")
            time.sleep(1)
        else:
            print("g fonksiyonu semaforu edindi.")
            for i in range(5):
                print("g fonksiyonu '{}' itemini işliyor.".format(i))
                time.sleep(1)
        semaphore.release()
        print("g fonksiyonu semaforu serbest bırakıyor.")


    t1 = threading.Thread(target=f)
    t2 = threading.Thread(target=g)
    t1.start()
    t2.start()

**Not:** Bu örnekte kullanılan `Semaphore()` nesnesi yerine, `Lock()`, `RLock`, `Condition()` ve `BoundedSemaphore()` nesnelerini de kullanabilirsiniz. Bu örnek `BoundedSemaphore()` ve `Condition()` nesneleri için pek uygun bir örnek olmasa da, `Lock()`, `RLock` nesneleri için bu örneği kullanmakta bir sakınca yok.

**Kodların Açıklamaları:**

Önce modüllerimizi programın içine aktaralım::

    import time
    import threading

Şimdi `Semaphore()` nesnesinden bir tane örnek oluşturalım::

    semaphore = threading.Semaphore()

Bu örnekte `f()` ve `g()` isimli iki tane fonksiyon kullanacağız. Önce `f()` fonksiyonunu oluşturalım, fonksiyon çağrılır çağrılmaz, ekrana bir yazı yazdırılsın::

    def f():
        print("f fonksiyonu başlıyor.")

Daha sonra iş parçacığı semaforu edinsin ve elde ettiğine dair bir yazı ekrana yazdırılsın::

        semaphore.acquire()
        print("f fonksiyonu semaforu edindi.")

Şimdi de fonksiyon içinde basit bir işlem tanımlayalım::

        for i in range(5):
            print("f fonksiyonu '{}' itemini işliyor.".format(i))
            time.sleep(1)

İş parçacığı semaforu serbest bıraksın ve serbest bıraktığına dair ekrana bir yazı yazdırılsın, son olarak da fonksiyonun çalışmasının bittiğine dair ekrana bir yazı yazdırılsın::

        semaphore.release()
        print("f fonksiyonu semaforu serbest bırakıyor.")
        print("f fonksiyonu bitiyor.")

Şimdi de `g()` fonksiyonunu oluşturalım. Fonksiyon çağrıldığında, fonksiyonun başladığına dair bir yazı ekrana yazdırılsın::

    def g():
        print("g fonksiyonu başlıyor")

İş parçacığı bu kilidi edinmediği sürece ekrana bir yazı yazdırılsın. Ancak `acquire()` fonksiyonunun *blocking* argümanını `False` yapmadığımız için bu yazı ekrana yazdırılmayacaktır. İsterseniz bir de `acquire(blocking=None)` yazarak örneği bir daha çalıştırın::

        while not semaphore.acquire():
            print("Semafor henüz kullanılamıyor.")
            time.sleep(1)

Eğer iş parçacığı semaforu edindiyse aşağıdaki işlemler yapılsın::

        else:
            print("g fonksiyonu semaforu edindi.")
            for i in range(5):
                print("g fonksiyonu '{}' itemini işliyor.".format(i))
                time.sleep(1)

Son olarak bu iş parçacığı da semaforu serbest bıraksın::

        semaphore.release()
        print("g fonksiyonu semaforu serbest bırakıyor.")

**Örnek-10:**

Şimdi de `BoundedSemaphore()` ile ilgili bir örnek yapalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import threading
    import time


    def f(item, bs):
        bs.acquire()
        time.sleep(1)
        print(item)
        bs.release()


    bounded_semaphore = threading.BoundedSemaphore(value=2)
    for i in range(10):
        t = threading.Thread(target=f, args=(i, bounded_semaphore))
        t.start()

**Kodların Açıklamaları:**

Yine her zamanki gibi önce modülleri programın içine aktaralım::

    import threading
    import time

Şimdi de bir tane `f()` fonksiyonu tanımlayalım. Bu fonksiyonun *item* ve *bs* isminde iki tane argümanı olsun. *item* argümanını for listesindeki her bir eleman için, *bs* argümanını da semaphore için kullanacağız::

    def f(item, bs):

Fonksiyonu çağıran iş parçacığı bağlanmış semaforu elde etsin, sonra 1 saniye bekleyelim ve `for` döngüsünün elemanını ekrana yazdıralım, son olarak da bağlanmış semaforu serbest bırakalım::

        bs.acquire()
        time.sleep(1)
        print(item)
        bs.release()

Şimdi `global` alanda bir tane bağlanmış semafor oluşturalım ve *value* argümanına 2 yazalım::

    bounded_semaphore = threading.BoundedSemaphore(value=2)

Son olarak bir tane `for` döngüsü içinde 10 tane iş parçacığı oluşturalım. Bu iş parçacıklarının *args* argümanında, listenin o sıradaki elemanı ve tanımladığımız bağlanmış semafor olsun::

    bounded_semaphore = threading.BoundedSemaphore(value=2)
    for i in range(10):
        t = threading.Thread(target=f, args=(i, bounded_semaphore))
        t.start()

**Not:** Bu örneği çalıştırdığınızda, ekrana sayıların ikişer ikişer yazdırıldığını göreceksiniz. Bunun olmasını sağlayan, bağlanmış semaforun
*value* değerinin 2 olarak yazılmasıdır.

**Örnek-11:**

Şimdi de `Event()` ile alakalı bir örnek yapalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import time
    import threading


    class Uretici(threading.Thread):
        def __init__(self, event, liste):
            threading.Thread.__init__(self)
            self.event = event
            self.liste = liste

        def run(self):
            count = 1
            while count < 10:
                self.liste.append(count)
                print("{} listeye {} tarafından eklendi."
                      .format(count, self.name))
                self.event.set()
                print("event {} tarafından ayarlandı.".format(self.name))
                self.event.clear()
                print("event {} tarafından temizlendi.".format(self.name))
                count += 1
                time.sleep(0.5)


    class Tuketici(threading.Thread):
        def __init__(self, event, liste):
            threading.Thread.__init__(self)
            self.event = event
            self.liste = liste

        def run(self):
            while True:
                if self.liste:
                    sayi = self.liste.pop()
                    print("{}, {} tarafından listeden düşürüldü."
                          .format(sayi, self.name))
                self.event.wait()


    __event__ = threading.Event()
    __liste__ = []
    t1 = Uretici(event=__event__, liste=__liste__)
    t2 = Tuketici(event=__event__, liste=__liste__)
    t1.start()
    t2.start()

**Kodların Açıklamaları:**

Modüllerimi programın içine aktaralım::

    import time
    import threading

Şimdi `Uretici` isminde, *event* ve *liste* argümanlarına sahip, `threading.Thread()` sınıfından türetilmiş bir sınıf oluşturalım::

    class Uretici(threading.Thread):
        def __init__(self, event, liste):
            threading.Thread.__init__(self)
            self.event = event
            self.liste = liste

Bu sınıfa `run()` isminde bir tane fonksiyon ekleyelim. Bildiğiniz gibi bu fonksiyon `threading.Thread()` sınıfına ait olan bir fonksiyon, dolayısıyla burada yine yazacağımız fonksiyon, orjinal fonksiyonun üzerine yazılacak::

        def run(self):

Fonksiyonda *count* isminde bir tane değişken kullanacağız. Bu değişken 10'dan küçük olduğu sürece *while* döngüsü çalışmaya devam edecek::

            count = 1
            while count < 10:

Şimdi listemize *count* değişkenini ekleyelim ve ekrana *count*'un listeye eklendiğine dair bir yazı yazdıralım::

                self.liste.append(count)
                print("{} listeye {} tarafından eklendi."
                      .format(count, self.name))

Şimdi `Event()` sınıfının önce `set()` fonksiyonunu sonra da `clear()` fonksiyonunu çağıralım, her bir işlem için ekrana bir yazı yazdıralım::

                self.event.set()
                print("event {} tarafından ayarlandı.".format(self.name))
                self.event.clear()
                print("event {} tarafından temizlendi.".format(self.name))

*count* değişkeni 1 birim artsın ve `time.sleep(0.5)` fonksiyonu ile 0.5 saniye bekleyelim::

                count += 1
                time.sleep(0.5)

Şimdi de benzer şekilde `Tuketici` sınıfımızı oluşturalım::

    class Tuketici(threading.Thread):
        def __init__(self, event, liste):
            threading.Thread.__init__(self)
            self.event = event
            self.liste = liste

Bu sınıfın `run()` metodunda da tanımlayalım::

        def run(self):

Yine bir döngü oluşturalım ve `self.liste` mevcut olduğu sürece, listeden *sayi* ismindeki değişken düşürülsün ve ekrana bu sayının düşürüldüğüne dair bir yazı yazdırılsın::

            while True:
                if self.liste:
                    sayi = self.liste.pop()
                    print("{}, {} tarafından listeden düşürüldü."
                          .format(sayi, self.name))

Ve `Event()` sınıfının `wait()` fonksiyonunu çağıralım. Bu fonksiyon, yapacak hiç bir işlem kalmadığında beklemeye devam edilmesini sağlayacak::

                self.event.wait()

`Event()`, `Uretici()` ve `Tuketici()` sınıflarından birer örnek oluşturalım ayrıca boş bir liste tanımlayalım son olarak da iş parçacıklarımızı başlatalım::

    __event__ = threading.Event()
    __liste__ = []
    t1 = Uretici(event=__event__, liste=__liste__)
    t2 = Tuketici(event=__event__, liste=__liste__)
    t1.start()
    t2.start()

**Not:** Bu örneği çalıştırdığınızda, `Uretici()` 9 tane elemanı listeye eklerken, `Tuketici()`'de bu listeye eklenen elemanları listeden silecek. Listeden silinecek bir şey kalmayınca da `Tuketici()` kendisini beklemeye alacak.

**Örnek-12:**

Şimdi de `Barrier()` nesnesiyle alakalı bir örnek yapalım.

**Kodlar**::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import time
    import random
    import threading


    def f(b):
        time.sleep(random.randint(2, 10))
        print("{} iş parçacığının uyandırıldığı tarih: {}"
              .format(threading.current_thread().getName(), time.ctime()))
        b.wait()
        print("{} iş parçacığının engeli geçtiği tarih: {}"
              .format(threading.current_thread().getName(), time.ctime()))


    barrier = threading.Barrier(3)
    for i in range(3):
        t = threading.Thread(target=f, args=(barrier,))
        t.start()

**Kodların Açıklamaları:**

Her zamanki gibi önce gerekli modülleri programın içine aktaralım::

    import time
    import random
    import threading

Şimdi *b* argümanına sahip, *f* isminde bir tane fonksiyon oluşturalım. Bu fonksiyonda önce `time.sleep(random.randint(2, 10))` fonksiyonunu çağırarak 2 ile 10 saniye arasında belirsiz bir süre bekleneceğini belirtelim. Daha sonra ekrana iş parçacığının uyandırıldığı tarih ekrana yazdırılsın, sonra da `Barrier()` nesnemizin `wait()` yöntemini çağıralım, son olarak da iş parçacığının engeli geçtiği tarih ekrana yazdırılsın::

    def f(b):
        time.sleep(random.randint(2, 10))
        print("{} iş parçacığının uyandırıldığı tarih: {}"
              .format(threading.current_thread().getName(), time.ctime()))
        b.wait()
        print("{} iş parçacığının engeli geçtiği tarih: {}"
              .format(threading.current_thread().getName(), time.ctime()))

Fonksiyonu oluşturduktan sonra *barrier* isminde bir tane `Barrier()` nesnesi örneği oluşturalım. Bu nesnenin argümanına 3 vermemizin sebebi, 3 tane iş parçacığı ile çalışıyor olmamızdır::

    barrier = threading.Barrier(3)

Son olarak bir `for` döngüsü oluşturalım, bu `for` döngüsü 3 tane `threading.Thread()` örneği üretsin ve döngü içinde bu örnekleri başlatalım::

    barrier = threading.Barrier(3)
    for i in range(3):
        t = threading.Thread(target=f, args=(barrier,))
        t.start()

**Not:** `Barrier()` nesnesinin özelliğine göre, oluşturulan bu iş parçacıklarının uyandırılma zamanları farklı olsa da, iş parçacıkları aynı anda engeli aşarlar.











