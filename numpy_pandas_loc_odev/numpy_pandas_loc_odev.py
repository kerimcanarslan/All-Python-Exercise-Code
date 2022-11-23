
##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

###############################

import seaborn as sns
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)    #yaparak artık tüm değişkenleri görebilşiriz
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.head()
df.info()
df.total   # total sütunu içindekileri göstyer
df["total"] # total sütunu içindekileri göster üstteki ile aynıdır
type(df["total"])      #pandas.core.series.Series
df["total"].dtype      # içindekilerin çoğusu float64 dedi

["NUM_" + col.upper() if df[col].dtype == 'float64' else col.upper() for col in df.columns]

# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.head()
df.info()
df.columns


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]



# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']



# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

new_col = [col for col in df.columns if col not in og_list]
new_df = df[new_col]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#







##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df_titanic = sns.load_dataset("titanic")
df_titanic.head()
df_titanic.info()

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df_titanic["sex"].value_counts()



#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.(kaç farklı değişken var onu soruyor)
#########################################

df_titanic.nunique()               # toplam sayı verir
df_titanic["fare"].unique()        # değerler neyse onu gösterşr tek tek
df_titanic["fare"].unique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df_titanic.pclass.unique()        # iksiisi de olur
df_titanic["pclass"].unique()

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df_titanic[["pclass", "parch"]].nunique()       # bu çalışır
df_titanic[["pclass", "parch"]].unique()        # bu çalışmaz

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df_titanic[["embarked"]].info()
df_titanic["embarked"] = df_titanic["embarked"].astype("category")
df_titanic[["embarked"]].info()      # gördüldüğü gibi değişti

#### ya da şöyle;

df_titanic["embarked"] = pd.Categorical(df_titanic["embarked"])            #ama stype daha kolaydır
df_titanic[["embarked"]].info()


#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.       ###bunlrı loc ile de yapabilrsin
#########################################

df_titanic[df_titanic["embarked"] == "C"].head()


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df_titanic[df_titanic["embarked"] != "S"].head()


#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df_titanic[(df_titanic["age"] < 30) & (df_titanic["sex"] == "female")].head()
df_titanic[(df_titanic["age"] < 30) | (df_titanic["sex"] == "female")].head()       #burada da veya koşulu var. tüm yaşı 30dan küçükler + tüm kadınlar


#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df_titanic[(df_titanic["fare"] > 500) | (df_titanic["age"] > 70)].head()

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df_titanic.isnull()             # bu sorudur, cevabı evet hayırıdr
df_titanic.isnull().sum()       # burada hangi değiikende kaç tane boş var ona bakarız

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df_titanic = df_titanic.drop("who", axis=1).head()   # yada
df_titanic.drop("who", axis=1, inplace=True)         # inplace=True yaptığı işlemi kayeder


#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df_titanic[["deck"]].isnull()
df_titanic[["deck"]].isnull().sum()
df_titanic[["deck"]].info()
df_titanic[["deck"]].value_counts()

# en çopk tekrarlanan değer için

df_titanic["deck"].mode()[0]
df_titanic["deck"].mode()                  # burada detayları da veriyor, bize en çok tekrar eden gerektiği için [0] alıyoruz

df_titanic["deck"].fillna(df_titanic["deck"].mode()[0], inplace=True)   # artık boş değerler "C" oldu


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df_titanic[["age"]].isnull()
df_titanic[["age"]].isnull().sum()     # 177 ader boş değer var

df_titanic["age"].fillna(df_titanic["age"].median(), inplace=True)

df_titanic[["age"]].isnull()
df_titanic[["age"]].isnull().sum()     # artık boş değer yok, hepsi median oldu

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

df_titanic.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})


#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df_titanic["age_flag"] = df_titanic["age"].apply(age_30)
df_titanic["age_flag1"] = df_titanic["age"].apply(lambda x: age_30(x))
df_titanic["age_flag2"] = df_titanic["age"].apply(lambda x: 1 if x < 30 else 0)



#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df_tips = sns.load_dataset("tips")
df_tips.head()
df_tips.info()


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df_tips.groupby("time").agg({"total_bill": ["min", "max", "mean", "count", "sum"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df_tips.groupby(["time", "day"]).agg({"total_bill": ["min", "max", "mean", "count", "sum"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

df_tips[(df_tips["time"] == "Lunch") & (df_tips["sex"] == "Female")].groupby("day").agg({"total_bill": ["min", "max", "mean"],
                                                                                         "tip": ["min", "max", "mean"]})

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################
df_tips.loc[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10), "total_bill"].mean()     ### loc kullanmadan da yapılabilir
df_tips[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10)]["total_bill"].mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################


df_tips["total_bill_tip_sum"] = df_tips["total_bill"] + df_tips["tip"]
df_tips.head()


#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

new_tips_df = df_tips.sort_values("total_bill_tip_sum", ascending=False).iloc[0:30]
new_tips_df


################# ÖDEV 1

import seaborn as sns
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)    #yaparak artık tüm değişkenleri görebilşiriz
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.head()
df.info()
df.total   # total sütunu içindekileri göstyer
df["total"] # total sütunu içindekileri göster üstteki ile aynıdır
type(df["total"])      #pandas.core.series.Series
df["total"].dtype      # içindekilerin çoğusu float64 dedi

["NUM_" + col.upper() if df[col].dtype == 'float64' else col.upper() for col in df.columns]



################ ÖDEV 2


################ ÖDEV 3


################# PANDA
