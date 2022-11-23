##########
# pandas veri analizi

##############
# Pandas serileri
# tek boyutlu index barındıran veri tipidir           # pandas df ise çok boyutlu index barındıran veri tipidir

import pandas as pd

s = pd.Series([10, 20, 30, 40])
s

type(s)
s.dtype

#tip bilgisi pandas.core.seri çıktı

#görüldüğü gibi çıktımızı lsite halinde aldık.
# üstelik indexleri ile birlikte

s.index  #deyince RangeIndex(start=0, stop=4, step=1) şeklinde 0.indexten başlayıp 4.indexe kadar 1'er 1'er giden indexlere sahip)
s.dtype  #int64 çıkar
s.size   # toplam eleman sayısı 4
s.ndim   # tek boyutludur
s.values # sadece value değerlerini almamızı sağlar, indexleri göstermez.
### burada çıktı array parantezinde verilir yani numpy ve ndarray biçiminde çıkar

type(s.values)
s.head   # ilk 5 değeri göster
s.head(3) # ilk 3 değeri göster
s.tail(3)  # sondan 3 değeri göster

#########
# Pandas ile dışarıdan veri okuma

a = pd.read_csv("dosya_konumu/neredeyse")
# dediğimizde bir .cvs dosyasını açıp okur
# read.exel diyerek exelden de okuyabilriiz.


###
# Veriye hızlı bakış

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.index
df.columns      #değişkenler, kolonlar


# pandas cheatsheet aratarak pandas için tüm fonk. metodları öğrenebiliriz

######## Önemli
df.describe().T   # describe().T metodu elimizdeki veri setinin özetini bize gösterir.
# Kaç değer kullanıldığı, ortlamaları, stadart sapmaları, min ve yüzdelik ve max değerleini gösterir.

df.isnull().values  # içi boş olan değerler var mı? yok mu
df.isnull().values.any()   # veriler içinde hiç boş (1 tane bile) bırakılan değer var mı diye souruyoruz, cevap evet
df.isnull().sum()   # burada değişkenlerde kaç adet boş veri/eksik veri var onu sorguluyoruz
# görüldüğü gibi en çok deck verisinde eksik var

# bir df içindeki değişkenlerden bir tanesinde kaç tane değer var görmek istiyoruz
# mesela bu df içinde cinsiyet verisini detaylı görmek istiyotu

df["sex"].head()  # bu şekilde bize ilk 5 veriyi verdi. Biz kaç adet erkek kaç adet kadın var onu öğrenmek istiyoruz

df["sex"].value_counts()  # böylece 577 male 314 female olduğunu gördük

##############
# Pandas seçim işlemleri

import pandas as pd

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index  #dediğimizde 0'dan başlayıp 891'e kadar 1'er 1'er arttığını görüyoruz. Burada index bilgisine erşiyoruz
df[0:25]  # 0.indexten 25.indexe kadar göster dedik

# bir df den veri yada index silmek istersek;

df.drop(1, axis=0).head()   # burada axis=0 satırlar arasından demek. Baştaki 1 ise index bilgisi
# sonuç olarak satırlar içinden 1.index tamamen silindi. head komutu ile gözlem yapıyoruz

delete_indexes = [1, 3, 5, 7]  # burada delete indexes adında bir lsite oluşturduk,

df.drop(delete_indexes, axis=0).head()  # deete index lsitesinde bulunan 1,3,5,7 değerlerini drop metodunda kullanarak o indexleri sildik.
# artık 1.3.5. ve 7. index yok. Bunu kaydetmedik

df.drop(delete_indexes, axis=0, inplace=True)


# burada df değişiyor ama kayıt edilmediği için tekrar df çağırıldğında eski hali gelir.
# bir sonraki işlenmlerde bunu kaydetmek için 2 yol var;
# 1. si  df = df.drop(delete_indexes, axis=0) diyerek yeni df yi kaydetmek
# 2. si ise df.drop(delete_indexes, axis=0, inplace=True) inplace=True metodu ile kaydederek devam edebilriz

#########ÖNEMLİ
# değişkeni İndexe çevirmek (mesela yaş değişkenini index yaparak küçükten büyüğe sıralama)

df["age"].head()  # burada yaş bilgilerini seçiyoruz

df.age.head()     # bu da alternatif bir kullanımdır

df.index = df["age"]    #burada age bilgisini index olarak tanıttık. Artık age index olacak ama değişkenlerden silmemiz lazım

df.index

df.drop("age", axis=1).head()  # drop ile age sütünnu (axis=1) sildik. NOT: Axis=0 satır demek Axis=1 sütun demek

şimdi bunu kaydedelim

df.drop("age", axis=1, inplace=True)
df.head()

# kayıt yaptıktan sonra bakıyoruz ki değişkenler(sütun) arasından age silinmiş. Ve İndex kısmında age değerlerimiz var

##şimdi tam tersini yaparak index bilgisini değişkene dönüştürebilir möiyiz?


##############
# İndexi değişkene çevirmek

df.index #baktığımızda 891 şndex değerimiz var hepsi age. Bu sferr tam tersini yapalım

df["age"] = df.index    #burada df["age"] demek normalde age değişkenini göster demek. Fakat biz bunu sildiğimiz için bu hata verir
# df["age"] karşılığı boş olduğıu için biz df.index e eşitliyoruz. Yani artık 891 index bilgimiz aynı zamanda değişken olarak age altında listelenecek
# hemen bakalım

df.head()

# ama şimdide index bilgisi age kaldı. Bunu silmek istiyoruz.
# fakat bunu yapmamnın daha kolay bir yolu var. buna da 2. ve kolay olan yol diyelim

df.drop("age", axis=1, inplace=True)
df.head()

#şuan age sadece index olarak kaldı, değişkenler kısmında yok.
# biz index olan age'yi değişken yapıp index'ten kaldırmak için;

df.reset_index().head()  # yağtığımızda df eski haline döndü
df = df.reset_index()    # diyerek kaydedebilriz

#df.reset_index() şuınu yapar;  indexe kaydedilen veriyi siler ve onu değişken olarak tekrar ekler. Eğer indexte bulunan
# veri aynı zamanda değişkenlerin içinde de varsa kod hata verir. Önce değişkenler içinden o verinin silinmesi lazımdır





###########
# Değişkenler üzerinde işlemler

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()  # burada değişkenler arasında ... var ve aradaki bazı değişkenler görünmez. Tüm değişkenleri görmek için;

pd.set_option('display.max_columns', None)    #yaparak artık tüm değişkenleri görebilşiriz
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
df.head()
.set_option()
# değişken sorgulama

"age" in df   # df içinde age adında bir değişken var mı sorusudur

# şimdi buna bakalım

df["age"].head()
type(df["age"].head())    #######Önemli   : Burada bu age değişkeninin tipi Series olarak çıktı

df[["age"]].head()
type(df[["age"]].head())  #######  : Burada age değişkeninin tipi ise DataFrame çıktı.

######## Önemli
# bazı işlemnlerde pandas bizden Series olarak isteyecektir. Bu durumda Tek köşeli parantez kullancağız
# bazı işlemlerde ise pandas bizden DataFrame oalrak isteycektirç Bu durumda 2 adet köşeli parantez kullancağız


name = "VBO_Bootcamp"
type = "new_term"
f"Name:{name} type:{type}"


string = "abracadabra"
group = []

for index, letter in enumerate(string):
    if index * 2 % 2 == 0:
        A = group.append(letter)



## İloc ve loc yapısı
#iloc: integer based selection (0'dan 3'e kadar seç) [0:3]
#loc:  label based selection (0'dan 3'de dahil seç) [0:3]

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
# 0'dan 3.satıra kadar gitti, 3.indeksi almadı.

df.loc[0:3]
# 0'dan 3.satıra kadar gifdip 3.satırı da aldı. toplam 4 inddex bilgisi var.

# satırlarda 0'dan 3 e kadar girmek istiyorum ama belirbi değişkeni istiyorum sadece. yani sadece yaş sütununun ilk 3 indexini istiyorum

df.iloc[0:3, "age"]
# yaparsak hata alırız çünkü iloc integer ister. iloc ile bunu şöyle yapabilriz
df.iloc[0:3, 3:4]
# yaparsak bize sadece yaş bilgisinin sütunu çıkar. ilk 3 index ya da
df.iloc[0:3, 0:4]
# yaparsak da bize ilk 3 index satırı ve ilk 4 sütun çıkar. surv, pclass, sex ve age hepsinin ilk 3 indexini görğrüzü

#bunu loc ile yapmak istersek;

df.loc[0:3, "age"]
# loc label based olduğu için 3.indexte dahil olacak şekilde toplam 4 adet age bilgisi verdi.

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]
#yaparak age, embarked ve alive durumunu da ahep birlikte alanbilriz.



#################
# koşullu seçimler/işlemler

# bu Df te yaşı 50'den büyüklleri seçmek istiyoruz.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
# dersek yaşı 50 den büyük olanalrı seçer.
# toplam kaç kişşi var ona bakalım

df[df["age"] > 50]["age"].count()
# yaptığımızda yaşı 50 den büyük olanları ayırdık ve age sütununda ki verileri saydırdık. Toıplam 64 veri çıktı

# yaşı 50 üzerinde olanlar arasında bir seçim yapmak için; yaşı 50'den büyük olanları class larını getir

df.loc[df["age"] > 50, "class"].head()

df.loc[df["age"] > 50, ["age", "class"]].head()  # burada yaşları ile bilrikte çıktı aldık.

# burada koşul sadece 50'den büyük olması. Çıktı üerinden eleme yaparak filtre yapıyoruz aslında
# fakat bizden 2 veya daha fazla koşul birlşkte istenirse??
# mesela yaşı 50'den büyük ve sadece erkek olanların yaş ve class bilgisi istenirse?

df.loc[ (df["age"] >50) & (df["sex"] == "male"), ["age", "class"]].head()

# burada (df["age"] >50) & (df["sex"] == "male") koşullarını ayrı ayrı parantez içine alıp & ile birbirine bağladık.
# sonrasımda virgül ile aynı şekilde fevam ettik.

# bir tane daha koşul ekleyelim.

df.loc[ (df["age"] >50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["age", "class", "embark_town"]].head()

# okunabililirği yüksek olması için şöyle yaaprız.

df.loc[ (df["age"] >50)
        & (df["sex"] == "male")
        & (df["embark_town"] == "Cherbourg"),
        ["age", "class", "embark_town"]].head()
# görüldüğü gibi daha okunaklı. kısaca yaşı 50 den büyük ve Cherbourg'tan binen erkeklerin listesi

# biraz daha çirkinleştirelim. southampton ya da cherbougt dan binenlere bakalım
# yada komutu option tire |
# koşulların her biri parantez içinde olması lazım

df.loc[ (df["age"] >50)
        & (df["sex"] == "male")
        & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
        ["age", "class", "embark_town"]].head()


new_df = df.loc[ (df["age"] >50)
        & (df["sex"] == "male")
        & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
        ["age", "class", "embark_town"]]

new_df["embark_town"].count()   # 44 değer var, detaylı bakalım

new_df["embark_town"].value_counts()   # 35 adet southampton 9 adet cherbourg varmış

#################
# toplulaştırma ve gruplaştırma

# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()


# yaş ortlaması istiyorsak
df["age"].mean()
# yaş ortalaması 29.69 çıktı. ama cinsiyete göre ayrı ayrı istersek?

df.groupby("sex")["age"].mean()

# kadınların 27 erkeklerin 30 çıkar

# ama biz agg ile bunu yapmak istiyotruz ve daha çok çıktı istiyoruz

df.groupby("sex").agg({"age": "mean"})
# yaşların toplamını da isterse?
df.groupby("sex").agg({"age": ["mean", "sum"]})

# bunu hayatta kalma oranının ortalaması ile birlikte isterse?

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

# burada cins. göre yaş ortalamaları, toplamları ve hayatta kalma oranları gösterir. Kadınların %74 ü hayatta kalırken erkeklerin %18 i hayatta aklmıl

# şimdi cinsiyete göre gemiye binenler arasında hangi şehi,rlerden binen yolcuların yaşlarının ortalaması ve hayatta kalma oraını alalım

df.groupby(["sex", "embark_town"]).agg({"age": "mean", "survived": "mean"})

# veriyi cinsiyet ve binilen şehir olarak grupladıktan sonra bunlar arasından yaş ve hayatta kalma oranlarının ortalamasını alıyrız

#class bilgisnmi de istersek?

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean", "survived": "mean"})

# bu ortalamaların kaçar kişi olduğunu görmek için


df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean", "survived": "mean", "sex": "count"})

# okunuşu kolaylaştırmak için

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": "mean",
    "survived": "mean",
    "sex": "count"})

############## önemlş
## pivot table (ön tanımlı değer ortlamadır. aggfunc=".... diyerek değişebilir

# veri setini kırılmlar açısından değerlendirmek

# hayatta kalma verisine ulaşmak istiyotuz
# bunun içinde cinsiyete göre ayrım yapmak istiyorum
# hangi şehirden bindiklerşne göre ayrım yapmak istiyorun

df.pivot_table("survived", "sex", "embarked")     # C,Q ve T şehirlerinden binen kadın ve erkeklerin hayatta kalma oranını verir.

# sırası ile 1. ne görmek istiyoruz
# sırası ile 2. neye göre ayırmak istiyoruz(satırlarda ayır)
# sırası ile 3. neye göre ayırmak istiyoruz(sütunlarda ayır)

df.pivot_table("survived", "sex", "embarked", aggfunc="std")    # artık ortalama değil std alacaktır.


# buna daha fazla değişken eklemek istersek, mesela class değişkennime göre de ayırmak istiyoruz

df.pivot_table("survived", "sex", ["embarked", "class"])

# artrık her şehirden binen yolcuların hem sınıfları hem de cinsiyuetleri ayrılarak verileri göreceğiz

# yaşları da kendi arasında sınıflandırma yaparak yaşlara göre de hayatta kalma analizi yapmak istiyotruz

# pd.cut veya pd.qcut ile yaş değerlerini istediğimiz gibi sınıflandırabiliriz. mesela 0-10 10-18 18-25 vs
# df["new_age"] ile yeni değişken oluşturalın

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", "new_age")     # burada yaş aralığpına ve cinsiyete göre hayatta kalma verisi vardır. Birkaç boyut daha eklersek?

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500)     # alt alta gelmesin diye 500 sütün boyunca göster dedik

############ Önemli
# Apply & Lambda yapıları

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.describe()
type(df.isnull().values.any())
df.isnull().sum()



# apply satır ya da sütünda otomatik olarak fonk. çalıştırma sağlar
# lambda kullan at fonk. tanımlar. daha az for döngüsü kullanmak için kullanırız

df["age2"] = df["age"]*2
df["age3"] = df["age"]*3

(df["age"]/10).head()
df["age2"]/10
df["age3"]/10

#önce döngü kullanarak bunları yapalım

for col in df.columns:
    if "age" in col:
        print(col)

# bakın burada age age2 age3 sütununu bulduruduk

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

# bakın burada bu sütunların hepisni tek tek 10 a böldük. ama kaydetmedik sadece print ettik

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# bakın burada döngüyü çalıştırdıktan sonra df[col] içine hespini kaydettik ve artık güncel değerlerimiz oldu,
# bunları apply ile nasıl yapardık?

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# daha da ilerleyelim

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

# burada loc ile tüm satırları ve içinde age olan sütunları seçtirdik. apply ile de uyguladık

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# burada fonk. x'den x'in ortlamasını çıkardık ve x'in standart sapmasına böldğk. Fakat lambda ile bu uzun oldu. buna fonk yazalım

def standart_scaler(col_name):
    return (col_name - col_name.mean() / col_name.std())

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# bunu kaydetmek içim;

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
df



#############
# birleştirme (join) yöntemleri

