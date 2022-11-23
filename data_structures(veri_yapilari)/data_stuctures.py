# alıştırma
# sayılardan başlayalım

# sayılar: integer
x = 4
type(x)

#sayılar: float

x = 4.6
type(x)

#sayılar: complex
x = 2j + 1
type(x)

#string

x = "hello ai era"
type(x)

#boolean

True
False

type(True)

# 1==2 eşitmidir diye sorar

1==2

#Listeler (köşeli parantez ile oluşur) option +7

x = ["btc","eth","xrp"]
type(x)

# sözlük oluşturma (dict) (süslü parantez optiona basılı tut +7
x = {"name": "peter", "age": "36"}
type(x)

#Tuple demet veri yapısı, normal parantez ile
x = ("python","ml","ds")
type(x)

#set veri yapısı- kümeler

x = {"python","ml","ds"}
type(x)

# bu veri yapıları (liste, tuple, set ve dictionary aynı zamanda python collections(arrays) olarak tanımlanır

#metodlar

# len() fonksiyonu/len metodu kaç elemandan oluştuğunu gösterir

name = "kerim"
len(name)
len("miuul")
len("kerimcanarslan")

# upper() ve lower() metodları
# upper tüm karakterleri büyük harfe çevirir
# lower tüm karakterleri küçük harfe çevirir

"kerimcanars".upper()
"KERIMCANARS".lower()

#replace karakter değiştirme fonksiyonu

hi = "hello ai era"
hi.replace("l","y")

#split metodu fonkşsyonu bölme işlemi yapar( boşluklara göre böler)

"hello ai era".split()

#strip metodu (baştan ve sondan kırpma işine yarar) boşlukları kırpar ama argğman bölümüne karakter yazılırsa o karakteri kırpar.)
" hello   ".strip()
"hello".strip("o")

#capitalize ilk harfi büyütür

"kerim".capitalize()

#dir("kerim") yazıp çalıştırırsak "kerim" stringi için kullanılabilecek tüm fonksiyonları gösterir.
#ya da dir(str) yazarsak stringler için kullanılabilecek tüm fonk çıkarırı.

# list yani listeler
#değiştirilebilir. sıralıdır. index şeklindedir.

notlar = [1,2,3,4]
type(notlar)

notlar = ["a","b","c"]
type(notlar)

#birden fazla veri yapısı birlikte olabilir.
notlar = [1,2,3,"a","b",True,[1,2,3]]
type(notlar)

#listedeki bir veriye erişmek için
notlar[0]
notlar[4]

#liste içindeki listenin içindekşi veriye ulaşmak
notlar[6][2]

#liste içindeki verinin tipini görmek için
type(notlar[6][1])

#liste içindeki veriyi değişitrmek için
notlar[1] = 0
notlar
notlar[6][0] = "a"
notlar

#liste içinde belirli bir kısmı göster demek için
#notlar[0:4] 0'dan 4'e kadar göster demektir.
notlar[0:4]

#liste metodları görmek için dir(notlar)

dir(notlar)

#en çok append metodu kullanılır
#eleman eklemeyi sağlar #append
 notlar.append(25)
 notlar
 # listenin en sonuna 25 eklendi

#pop metodu ise indexe göre silme işlemi yapar
# notlar listesi içindeki 0.değeri sil komutu altta
notlar.pop(0)
notlar
# notlar listesnin 0. değeri silindi ve normnalde 1.sırada olan değer 0.sıraya geriledi.

#insert komutu indexe gmre ekleme işlemi yapar
#insert komutunda 2 giriş yaparız.
# notlar listesinin 2.değerine 70 ekleme işlemi yapalım

notlar.insert(2,70)
notlar

#böylelikle notlar listesinin 0. ve 1. değerinden hemen sonra gelecek olan 2. değer, artık 70 oldu.
#normalde 2.değer olan a harfi ise 1 basamak gerileyerek 3.değer oldu.


#sözlük yani dictionary metodları Süslü parantez ve : ifadesi ile kullanılır
#değiştirilebilir
#sırasızdır

#key-value şeklinde girilir REG keydir. Regression ise valuedir.

dictionary = {"REG": "regression"}


dictionary = {"REG": "regression",
              "LOG": "logistic regression",
              "CART": "classification and reg"}
dictionary["REG"]

#sözlük içinde liste de tutabiliriz

dictionary = {"REG": ["regression",1,2,"q"],
              "LOG": ["logistic regression",89,88,"b"],
              "CART": ["classification and reg",29,30,"h"]}

#bu sözlüğün içinde bulunan bir listenin içinde ki bir değere ulaşmak istersek;

dictionary["CART"][0]

#burada sözlük içinde CART kelimesinin karşılığında bulunan liste içinden 0.değeri göster dedik.

#key sorgulama da yapabilriiz
#YSA in dictionary diye soru sorduğumuzda bize evet yada hayır diyecekti.

"YSA" in dictionary
"CART" in dictionary
29 in dictionary["CART"]  #burada ise Sözlğk içindeki CART kelimesinin karşılığında bulunan listede ya da value değerinde 29 var mı diye sorduk ve cevap evet.

#dictionary["CART"] ile dictionary.get("CART") aynı işlemi yapar

dictionary["CART"]
dictionary.get("CART")

#göründüğü üzere aynu sonuca vardık.


#value değerini değiştirmek için

dictionary["CART"] = ["a","b",3,4,"d"]
dictionary

#tüm keylere erişmek için

#dictionary.keys() yaptığımızda tüm key ler karşımıza çıkar
dictionary.keys()

#tüm value değerlerine erişmek için

dictionary.values()

# key ve value çiftlerine tuple olarak erişebilir miyiz? evet

dictionary.items()

#key ve value değerlerini güncelleyebilmek için

dictionary.update({"REG": [11,2]})
dictionary


#yeni bir key value eklemek yani sözlğklte hiç olmayan bir şeyi eklemek

dictionary.update({"RTE": ["q", 1]})
dictionary

#böylece en altta yeni bir key ve karşısında yeni bir value oluştu.



#demet-tuple- listenin kardeşidir. liste köşeli parantez tuple normal parantez
#deiştirilemez
#kapsayıcı(saklama yapar
#sıralıdır.

t = ("a","g",2,5,7,4)
type(t)

#t[0] köşeli parantez kullanarak 0.elamanı çağırırız
#t[0:3] diyerek 0.dan 3. elemana kadar göster demiş oluruz.

t[0]
t[0:3]

#tuple fonksşyonunda değerleri listedeki gibi değişemeyiz.
#t[0] = 12 yapıp çalıştırırsak hata verecektir. tuple fonkşsyoununda başta verdiğimiz değerler değişmez.

t[0] = 12

#fakat bunu önce list fonksiyonuna dönüştürüp sonra değeri değiştirebiliriz. bunu yapmak için şunu kullanırız;

t = list(t)
type(t)

#artık t tuple ımız list oldu. Şimdi değişikliği yapaılım,,

t[0] = "abd"
t

#artık t listemizin 0.değeri abd oldu. şimdi tekrar tuple formuna dönüştürelim
t = tuple(t)
type(t)
t


# set fonksiyonu kümeler gibi düşenelim
# değiştirilebilirdir
# sırasız ve eşsizdir
# kapsayıcıdır.

# iki kümenin farkı alınırken difference()

set1 = set([1,3,5])
set2 = set([1,3,6])

#set1 de olup set2 de olmayanlar nelerdir?

set1.difference(set2)

#set2 de olup set1 de olmayanlar nelerdir?

set2.difference(set1)


#bir kümede varken diğer kümede olmayan yani simetrik farkı alınan değerleri görmek içim;

set1.symmetric_difference(set2)

#set1 den 5 değeri set2 den ise 6 değerini bize gösterdi. Bunun tam tersi de aynı sonucu vercektir.

#bu iki kğmenşn kesişimini görmek için intersection() komutu

set1 = set([1,3,5])
set2 = set([1,3,6])

set1.intersection(set2)
# tam tersini yapınca da bu şekilde yanıt alacağız

#iki kğmenşn birleşimi için de union komutu kullanırız

set1.union(set2)

# elimizdeki bu iki kümenin kesişimşi boş mu? sorusu için isdisjoint() komutu kullanılır

set1.isdisjoint(set2)

# ilk küme ikinci kümenin alt kümesi midir? sorusu için issubset() komutu kullanılır

set1 = set([1,3,5])
set2 = set([1,2,3,4,5,6])

set1.issubset(set2)

#cevap evet. Çğünkü 1,3,5 değerleri set 2 de de var. ama tam tersini sorunca cevap false çıkar.
#çünkü 2,4,6 değerleri set1 içinde yer almaz

set2.issubset(set1)

# issubset komutu ile hemen hemen aynı soruyu soran issuperset komutudur. ama zıt cevaplar çıkar.
# issuperser() komutu ilk küme ikinci kümeyi kapsıyor mu?

set1.issuperset(set2)

#görüldüğü gibi set1 set2 yi içinde kapsamıyor

