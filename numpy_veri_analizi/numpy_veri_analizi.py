###########
# data analysis with python

# NumPy
# Pandas
# Veri Görselleştirme / Matplotlib & Seaborn
# Gelişmiş Fonksiyonel Keşifçi Veri Analizi ( Advanced Functional Exploratory Data Analysis )



# 1- NumPy ile başlayalım
# NumPy numerik python anlamına gelir, numerik işlemleri daha hızlı ve daha kolay yapabilriz
# örnek olarak 2 listeyi birbiri ile numpy kullanmadan çarpalım

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# bunun için bir döngü oluşturmamız lazım
# boş bir liste oluştualım

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
ab

# gördüğünüz gibi python kurallarına göre bu işlemi yaptık.
# numpy kullanarak daha koşay bir şekilde yapabiliriz
# önce numpy kütüphanesini indirielim

import numpy as np

a = [1, 2, 3, 5]
b = [2, 3, 4, 6]

a = np.array([1, 2, 3, 5])
b = np.array([2, 3, 4, 6])
a * b

# görüldüğü gibi np.array metodu ile bu listeleri matematiksel işlem yapılabilir hale getirdik
# a * b gibi kısa bir işlem yazarak sonuca ulaştık.



############
# Şimdi numpy array'leri oluşturmayı öğreneceğiz

import numpy as np

np.array([1, 3, 5, 7])
# oluşturduk, şimdi tipine bakalım

type(np.array([1, 3, 5, 7]))
# numpy.ndarray olarak çıkt. bu tip bizim nunpy array'imizdir.

np.zeros(10, dtype=int)
# burada da 10 adet 0 sayısı üret dedik. dtype kısmına float yazdığımız için ondalıklı oluşturdu.

np.random.randint(0, 15, size=10)
# burada da 0 ile 15 arasında rastgele 10 adet int seç(randint)(random)

np.random.normal(10, 4, (2, 3))
# burada da ortalaması 10 standart sapması 4 olan ve 2x3 boyutunda bir array oluşturduk.



###########
#numpy array özellikleri

# ndim = boyut sayısı
# shape = boyut bilgisi
# size = toplam eleman sayısı
# dtype = array veri tipi

import numpy as np

a = np.random.randint(0, 10, size=5)
a.ndim   # boyutu 1 çıktı. çünkü 1 boyutlu
a.shape  # (5,) tek boyutlu ve 5 elamana sahip
a.size   # toplam elemans ayısı 5 dir
a.dtype  # int64 tip bilgisidir

b = np.random.normal(10, 4, (3, 4))
b.ndim   # 2 boyutlu
b.shape  # (3,4) 3 satır 4 sütün-kolon
b.size   # toplam 12 elamana sahip
b.dtype  # float64


############
# reshaping (yeniden şekillendirme)

np.random.randint(0, 15, size=9).reshape(3,3)
# yada

 a = np.random.randint(0, 15, size=9)
 a.reshape(3,3)

 # normalde 0 ile 15 arasında 9 elemanlı (1,9) olurken reshape ile 3,3 şeklinde yeniden şekillendirdik.
 # burada dikkat edilmesi gerekn ise şudur
 # 3,3 yapınca 9 elemanalı olması gerekir, eğer size=9 olmasaydı işlem çalışmayacaktı.

 ################
 # İndex seçimi yapmayı öğrenelim

import numpy as np

a = np.random.randint(0, 20, size=5)

a
a[0]  # a arrayinin 0.indeksini getir
a[3]  # a arrayinin 3.indeksini getir
a[0:3]  # a arrayinin 0 dan 3. indeksine kadar getir(dilimle)

b = np.random.randint(5, 25, size=(3,4))      # 5 ile 25 arasındakileri kullanarak 3,4  matrix oluştur

b

b[0, 0]      # burada 1.satır ve 1.sütundaki elemanı getirdi.

b[1, 2]      # burada 2.satır ve 3.sütundakş elemanı getirdi

b[2, 3] = 999

b           # burada 3. satır 4. sütun 999 oalrak değiştirildi.

b[2, 3] = 2.9

b           # burada da değer 2 olarak güncellendi çğnkğ int değerler üzerinde çalışıyoruz

b[:, 1]     # burada tüm satırları ve 2.sütunu seç dedik. yani bunların keşimini getirdi

b[1, :]     # burada da 2.satırı ve tüm sütunları getir dedik. 2.satırın tüm elemanalrı geldi

b[0:2, 0:3] # burada satırlar için 0'dan 2'ye kadar git, sütunlar için de 0'dan 3'e kadar git ve göster. (e kadarda sonuncusu dahil değildir.



################
# Fancy İndex
# bir numpy array ine liste girerek eleman seçmemizi sağlar


v = np.arange(0, 30, 3)
v[0]
v[1]
v[2]

# burada v köşeli parantrezi ile lsite içindeki değerleri görebiliriz.
# fancy İndex ile de

catch = [1, 2, 3]

v[catch]
# bize istediğimiz değerleri toplu olarak seçmemizi sağlar.
# burada catch 1,2,3 diye bir liste oluşturduk
# v köşeli paranteazi ile çağırınca bize 1. 2. ve 3. değerleri gösterdi


##############
# numpy da koşullu işlemler ( Conditions Numpy )

v = np.arange(0, 20, 3)

# bu v arrayında sadece 11 den küçükleri görmek istiyoruz.
# numpy olmasaydı bunu böyle yapacaktık;

new_v = []

for i in v:
    if i < 11:
        new_v.append(i)
new_v

# görüldüğü gibi for döngüsü ile bunu böyle yaptık.
# fakat fancy ile daha kolay, şöyle ki:

v < 11  # diye bir sorgulama yaparız. Lsitedeki tğm verileri sorgular ve true, false cevabı çıkarır

v[v < 11]  # şeklinde tekrar işleme alınca, bize 11 den küçük olan v array'ının içindeki elemanları getirir.
# fancy kullanaraj çok kolay bir şekilde buna ulaşbiliriz



#######
# matematiksel işlemler

v = np.array([1,2,3,4,5])
v / 5
v * 5
v ** 2'
### numpy array haline dönüştürdüğümüz listeyi 5' e bölüp tüm elemanlkara bunu uygulayabiliriz

np.subtract(v, 1)      # tüm elemanlardan 1 çıkart
np.add(v,1)            # tüm elemanlara 1 ekle
np.mean(v)             # tüm değerlerin ortalamasını al
np.sum(v)              # tüm derğerlein toplamı
np.min(v)              # en küçük değer
np.max(v)              # en büyük değer
np.var(v)              # ????



