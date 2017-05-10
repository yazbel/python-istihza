.. meta::
   :description: Bu bölümde Python programlama dilinde yazdığımız kodlara nasıl 
    yorum ve açıklama cümleleri ekleyeceğimizi öğreneceğiz.
   :keywords: python, python2, python3, yorum, açıklama, comment out
   
.. highlight:: python3

***************************
Yorum ve Açıklama Cümleleri
***************************

Python'la ilgili şimdiye kadar öğrendiğimiz bilgileri kullanarak yazabileceğimiz
en karmaşık programlardan biri herhalde şöyle olacaktır::
    
    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu"
    şehir   = "İstanbul"

    print("isim           : ", isim,    "\n", 
          "soyisim        : ", soyisim, "\n",
          "işletim sistemi: ", işsis,   "\n",
          "şehir          : ", şehir,   "\n", 
          sep="")

Yukarıdaki kodları rahatlıkla anlayabildiğinizi zannediyorum. Ama isterseniz
yine de bu kodları satır satır inceleyelim:

İlk olarak `isim`, `soyisim`, `işsis` ve `şehir` adında dört farklı değişken
tanımladık. Bu değişkenlerin değeri sırasıyla `Fırat`, `Özgül`, `Ubuntu` ve
`İstanbul`.

Daha sonra da tanımladığımız bu değişkenleri belli bir düzen içinde
kullanıcılarımıza gösterdik, yani ekrana yazdırdık. Elbette bu iş için
``print()`` fonksiyonunu kullandık. Bildiğiniz gibi, ``print()`` birden fazla
parametre alabilen bir fonksiyondur. Yani ``print()`` fonksiyonunun parantezleri
içine istediğimiz sayıda öğe yazabiliriz.

Eğer ``print()`` fonksiyonunun yukarıdaki kullanımı ilk bakışta gözünüze
anlaşılmaz göründüyse, fonksiyonda geçen ve ne işe yaradığını anlayamadığınız
öğeleri, bir de çıkartarak yazmayı deneyebilirsiniz bu fonksiyonu.

Python'la yazılmış herhangi bir programın tam olarak nasıl işlediğini anlamanın
en iyi yolu program içindeki kodlarda bazı değişiklikler yaparak ortaya çıkan
sonucu incelemektir. Örneğin ``print()`` fonksiyonunda `sep` parametresinin
değerini boş bir karakter dizisi yapmamızın nedenini anlamak için, fonksiyondaki
bu `sep` parametresini kaldırıp, programı bir de bu şekilde çalıştırmayı
deneyebilirsiniz.

Yukarıdaki örnekte bütün öğeleri tek bir ``print()`` fonksiyonu içine yazdık.
Ama tabii eğer isterseniz birden fazla ``print()`` fonksiyonu da
kullanabilirsiniz. Şöyle::

    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu"
    şehir   = "İstanbul"

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

Yukarıdaki kodlarla ilgili birkaç noktaya daha dikkatinizi çekmek istiyorum:

Birincisi, gördüğünüz gibi kodları yazarken biraz şekil vererek yazdık. Bunun
sebebi kodların görünüş olarak anlaşılır olmasını sağlamak. Daha önce de
dediğimiz gibi, Python'da doğru kod yazmak kadar, yazdığınız kodların anlaşılır
olması da önemlidir. Bu sebepten, Python'la kod yazarken, mesela kodlarımızdaki
her bir satırın uzunluğunun 79 karakteri geçmemesine özen gösteriyoruz. Bunu
sağlamak için, kodlarımızı yukarıda görüldüğü şekilde belli noktalardan bölmemiz
gerekebilir.

Esasında yukarıdaki kodları şöyle de yazabilirdik::

    isim = "Fırat"
    soyisim = "Özgül"
    işsis = "Ubuntu"
    şehir = "İstanbul"

    print("isim: ", isim, "\n", "soyisim: ", soyisim, "\n", 
    "işletim sistemi: ", işsis, "\n", "şehir: ", şehir, "\n", sep="")

Ancak bu şekilde kod yapısı biraz karmaşık görünüyor. Ayrıca parantez içindeki
öğeleri yan yana yazdığımız için, `isim:`, `soyisim:`, `işletim sistemi:` ve
`şehir:` ifadelerini alt alta düzgün bir şekilde hizalamak da kolay
olmayacaktır.

Belki bu basit kodlarda çok fazla dikkati çekmiyordur, ama özellikle büyük
boyutlu programlarda kodlarımızı hem yapı hem de görüntü olarak olabildiğince
anlaşılır bir hale getirmek hem kodu okuyan başkaları için, hem de kendimiz için
büyük önem taşır. Unutmayın, bir programı yazdıktan 5-6 ay sonra geri dönüp
baktığınızda kendi yazdığınız kodlardan siz dahi hiçbir şey anlamadığınızı
farkedebilirsiniz!

Bir program yazarken kodların olabildiğince okunaklı olmasını sağlamanın bir kaç
yolu vardır. Biz bunlardan bazılarını yukarıda gördük. Ancak bir programı
okunaklı hale getirmenin en iyi yolu kodlar içine bazı yorum cümleleri ekleyerek
kodları açıklamaktır.

İşte bu bölümde, Python programlama dili ile yazdığımız kodlara nasıl yorum ve
açıklama cümleleri ekleyeceğimizi inceleyeceğiz.

Yorum İşareti
***************

Programcılıkta en zor şey başkasının yazdığı kodları okuyup anlamaktır. Hatta
yazılmış bir programı düzeltmeye çalışmak, bazen o programı sıfırdan yazmaktan
daha zor olabilir. Bunun nedeni, program içindeki kodların ne işe yaradığını
anlamanın zorluğudur. Programı yazan kişi kendi düşünüşüne göre bir yol izlemiş
ve programı geliştirirken karşılaştığı sorunları çözmek için kimi yerlerde
enteresan çözümler üretmiş olabilir. Ancak kodlara dışarıdan bakan birisi için o
programın mantık düzenini ve içindeki kodların tam olarak ne yaptığını anlamak
bir hayli zor olacaktır. Böyle durumlarda, kodları okuyan programcının en büyük
yardımcısı, programı geliştiren kişinin kodlar arasına eklediği notlar
olacaktır. Tabii programı geliştiren kişi kodlara yorum ekleme zahmetinde
bulunmuşsa...

Python'da yazdığımız kodları başkalarının da anlayabilmesini sağlamak için,
programımızın yorumlarla desteklenmesi tavsiye edilir. Elbette programınızı
yorumlarla desteklemeseniz de programınız sorunsuz bir şekilde çalışacaktır. Ama
programı yorumlarla desteklemek en azından nezaket gereğidir.

Ayrıca işin başka bir boyutu daha var. Sizin yazdığınız kodları nasıl başkaları
okurken zorlanıyorsa, kendi yazdığınız kodları okurken siz bile
zorlanabilirsiniz. Özellikle uzun süredir ilgilenmediğiniz eski programlarınızı
gözden geçirirken böyle bir sorunla karşılaşabilirsiniz. Programın içindeki bir
kod parçası, programın ilk yazılışının üzerinden 5-6 ay geçtikten sonra size
artık hiçbir şey ifade etmiyor olabilir. Kodlara bakıp, 'Acaba burada ne yapmaya
çalışmışım?' diye düşündüğünüz zamanlar da olacaktır. İşte bu tür sıkıntıları
ortadan kaldırmak veya en aza indirmek için kodlarımızın arasına açıklayıcı
notlar ekleyeceğiz.

Python'da yorumlar `#` işareti ile gösterilir. Mesela bu bölümün ilk başında
verdiğimiz kodları yorumlarla destekleyelim::
    
    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu" #işletim sistemi
    şehir   = "İstanbul"

    #isim, soyisim, işsis ve şehir adlı değişkenleri 
    #alt alta, düzgün bir şekilde ekrana basıyoruz.
    #Uygun yerlerde alt satıra geçebilmek için "\n"
    #adlı kaçış dizisini kullanıyoruz.
    print("isim           : ", isim,    "\n", 
          "soyisim        : ", soyisim, "\n",
          "işletim sistemi: ", işsis,   "\n",
          "şehir          : ", şehir,   "\n", 
          sep="") #parametreler arasında boşluk bırakmıyoruz.

Burada dikkat edeceğimiz nokta her yorum satırının başına `#` işaretini koymayı
unutmamaktır.

Yazdığımız yorumlar Python'a hiç bir şey ifade etmez. Python bu yorumları
tamamen görmezden gelecektir. Bu yorumlar bilgisayardan ziyade kodları okuyan
kişi için bir anlam taşır.

Elbette yazdığınız yorumların ne kadar faydalı olacağı, yazdığınız yorumların
kalitesine bağlıdır. Dediğimiz gibi, yerli yerinde kullanılmış yorumlar bir
programın okunaklılığını artırır, ama her tarafı yorumlarla kaplı bir programı
okumak da bazen hiç yorum girilmemiş bir programı okumaktan daha zor olabilir!
Dolayısıyla Python'da kodlarımıza yorum eklerken önemli olan şey, kaş yapmaya
çalışırken göz çıkarmamaktır. Yani yorumlarımızı, bir kodun okunaklılığını
artırmaya çalışırken daha da bozmayacak şekilde yerleştirmeye dikkat etmeliyiz.

Yorum İşaretinin Farklı Kullanımları
************************************

Yukarıda yorum (`#`) işaretini kullanarak, yazdığımız Python kodlarını nasıl
açıklayacağımızı öğrendik. Python'da yorum işaretleri çoğunlukla bu amaç için
kullanılır. Yani kodları açıklamak, bu kodları hem kendimiz hem de kodları
okuyan başkaları için daha anlaşılır hale getirmek için... Ama Python'da `#`
işareti asıl amacının dışında bazı başka amaçlara da hizmet edebilir.

Etkisizleştirme Amaçlı
=======================

Dediğimiz gibi, yorum işaretinin birincil görevi, tabii ki, kodlara açıklayıcı
notlar eklememizi sağlamaktır. Ama bu işaret başka amaçlar için de
kullanılabilir. Örneğin, diyelim ki yazdığımız programa bir özellik eklemeyi
düşünüyoruz, ama henüz bu özelliği yeni sürüme eklemek istemiyoruz. O zaman
şöyle bir şey yapabiliriz::
    
    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu"
    şehir   = "İstanbul"
    #uyruğu = "T.C"

    print("isim           : ", isim,    "\n", 
          "soyisim        : ", soyisim, "\n",
          "işletim sistemi: ", işsis,   "\n",
          "şehir          : ", şehir,   "\n", 
          #"uyruğu        : ", uyruğu,  "\n",
          sep="")

Burada, programa henüz eklemek istemediğimiz bir özelliği, yorum içine alarak
şimdilik iptal ediyoruz yani etkisizleştiriyoruz (İngilizcede bu yorum içine
alma işlemine *comment out* deniyor). Python yorum içinde bir kod bile yer alsa
o kodları çalıştırmayacaktır. Çünkü Python `#` işareti ile başlayan satırların
içeriğini görmez (``#!/usr/bin/env python3`` ve ``# -*- coding: utf-8 -*-``
satırları hariç).

Peki eklemek istemediğimiz özelliği yorum içine almaktansa doğrudan silsek olmaz
mı? Elbette olur. Ama programın daha sonraki bir sürümüne ilave edeceğimiz bir
özelliği yorum içine almak yerine silecek olursak, vakti geldiğinde o özelliği
nasıl yaptığımızı hatırlamakta zorlanabiliriz! Hatta bir süre sonra programımıza
hangi özelliği ekleyeceğimizi dahi unutmuş olabiliriz. 'Hayır, ben hafızama
güveniyorum!' diyorsanız karar sizin.

Yorum içine alarak iptal ettiğiniz bu kodları programa ekleme vakti geldiğinde
yapacağınız tek şey, kodların başındaki `#` işaretlerini kaldırmak olacaktır.
Hatta bazı metin düzenleyiciler bu işlemi tek bir tuşa basarak da gerçekleştirme
yeteneğine sahiptir. Örneğin IDLE ile çalışıyorsanız, yorum içine almak
istediğiniz kodları fare ile seçtikten sonra `Alt+3` tuşlarına basarak ilgili
kodları yorum içine alabilirsiniz. Bu kodları yorumdan kurtarmak için ise ilgili
alanı seçtikten sonra `Alt+4` tuşlarına basmanız yeterli olacaktır (yorumdan
kurtarma işlemine İngilizcede *uncomment* diyorlar).

Süsleme Amaçlı
===============

Bütün bunların dışında, isterseniz yorum işaretini kodlarınızı süslemek için
dahi kullanabilirsiniz::
    
    #######################################################
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #                    FALANCA v.1                      #
    #                Yazan: Keramet Su                    #
    #                  Lisans: GPL v2                     #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #######################################################

    isim    = "Fırat"
    soyisim = "Özgül"
    işsis   = "Ubuntu"
    şehir   = "İstanbul"

    print("isim           : ", isim,    "\n", 
          "soyisim        : ", soyisim, "\n",
          "işletim sistemi: ", işsis,   "\n",
          "şehir          : ", şehir,   "\n", 
          sep="")

Yani kısaca, Python'un görmesini, çalıştırmasını istemediğimiz her şeyi yorum
içine alabiliriz. Unutmamamız gereken tek şey, yorumların yazdığımız
programların önemli bir parçası olduğu ve bunları mantıklı, makul bir şekilde
kullanmamız gerektiğidir.
