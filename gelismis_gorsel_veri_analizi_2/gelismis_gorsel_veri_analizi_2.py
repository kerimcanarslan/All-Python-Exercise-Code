##########


# 3-) SAYISAL DEĞİŞKENLER

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()

# Sayısal değişkenlere genel bakuş için describe().T kullanırız

df.describe().T     # survived pclass age sibsp parch fare çıktı olarak geldi.

# şimdi tip bilgileri int ve float olan verileri bulalım.
df.dtypes      #describe komutunun verdiği ile dtypes lar aynı. ama emin olmak için döngüye sokalım
# sayısal değişkenlere num_col diyelim

num_col = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
# num_col = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare'] çıktı

# int ve float oalrak ayırdık ama ; ,nt olup ta 10 değerden daha az olanlar vardır. Onları ayıklamak için

num_cols = [col for col in num_col if df[col].nunique() > 10]
# num_cols =  ['age', 'fare çıktı. demekki 1sadece age ve fare 10 dan daha fazla değere sahip. yeni num col onlar

#bir de kategroik olarak görünen fakat numerik olan değerler varsa?

cat_but_num = [col for col in df.columns if df[col].dtypes not in ["int64", "float64"] and df[col].nunique() > 10]
# boş çıktı yani yok. devam edelim

 # ama biz bunları tek tek yapmak değil de fonk. haline getirmek istiyoruz.



def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df, "age", plot=True)

# quantiles ile yüzdelik değerleri de gördük
## Tüm değerler için bunu yapabilmek için döngü oluşturalım

for col in num_cols:
    num_summary(df, col, plot=True)





# 4-) DEĞİŞKENLERİN YAKALANMASI (ÖNEMLİ)


## KATEGORİK OLANLAR
    cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].dtypes in ["int", "float"] and df[col].nunique() < 10]

    cat_but_num = [col for col in cat_col if df[col].nunique() > 10]
    # ya da
    cat_but_num = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in [["category", "object", "bool"]]]

    cat_cols = cat_col + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_num]

    df[cat_col].head()

    df[cat_col].nunique()  ### max 7 değer var çok güzel


## SAYISAL OLANLAR
    num_col = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

    num_cols = [col for col in num_col if df[col].nunique() > 10]

    cat_but_num = [col for col in df.columns if df[col].dtypes not in ["int64", "float64"] and df[col].nunique() > 10]

# DOCSTRİNG YAZALIM

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kardinal kategorik değişkenlerin isim


    :param dataframe: dataframe
           Değişken isimleri alınmak istenen dataframe'dir.

    :param cat_th: int, float
           Numerik görünen fakat kategorik olan değişkenler için sınıf eşik değeri

    :param car_th: int, float
           Kategorik fakat kardinal değişkenler için eşik değeri

    :return:

           cat_cols: list
                     Kategorik Değişkenler Listesi
           num_cols: list
                     Numerik Değişkenler Listesi
           cat_but_car: list
                     Kategorik görünümlü kardinal değişkenler

    Notes
    -----

    cat_cols + num_cols + cat_but_car = toplam değişken sayısını verecektir.
    num_but_cat cat_cols içinde yer alır
    Return olan 3 liste toplamı toplam değişken sayısına eşittir.

    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].dtypes in ["int", "float"] and df[col].nunique() < cat_th]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > car_th and str(df[col].dtypes) in [["category", "object", "bool"]]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Obvservations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

grab_col_names(df)


# grab_col_names fonk ile içine girilen bir df'in özetini ve değişkenlerin (sayısal-kategorik-kar) ayırdı.


# 4-) HEDEF DEĞİŞKEN ANALİZİ(ANALYSIS OF TARGET VARIABLE)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#############################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kardinal kategorik değişkenlerin isim


    :param dataframe: dataframe
           Değişken isimleri alınmak istenen dataframe'dir.

    :param cat_th: int, float
           Numerik görünen fakat kategorik olan değişkenler için sınıf eşik değeri

    :param car_th: int, float
           Kategorik fakat kardinal değişkenler için eşik değeri

    :return:

           cat_cols: list
                     Kategorik Değişkenler Listesi
           num_cols: list
                     Numerik Değişkenler Listesi
           cat_but_car: list
                     Kategorik görünümlü kardinal değişkenler

    Notes
    -----

    cat_cols + num_cols + cat_but_car = toplam değişken sayısını verecektir.
    num_but_cat cat_cols içinde yer alır
    Return olan 3 liste toplamı toplam değişken sayısına eşittir.

    """
    cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].dtypes in ["int", "float"] and df[col].nunique() < 10]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in [["category", "object", "bool"]]]

    cat_cols = cat_col + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Obvservations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


# fonk. tamam. elimize geçen veriyi önce sayısal ve kategorik olarak ayırıp, özet verisine bakalım

grab_col_names(df)

cat_cols, num_cols, num_but_cat = grab_col_names(df)

## hedef değişkenin kategorik değişkenle ile analizi

df.groupby("sex")["survived"].mean()
    #female    0.742038
    #male      0.188908
    # buradan anlıyoruz ki kadınlar daha çok hayatta kalmış. Kadın olmak hayatta kalmayı etkiliyot

## bu veri setinden bizim hedef değişkenimiz hayatta kalmak olsun.

# kategorik değişkenler için hedef değişkenimizi gösteren bir fonk yazalım

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({f"{target} TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, "survived", "sex")

target_summary_with_cat(df, "survived", "pclass")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)
    print("##############")

# sayısal değişkenler için hedef değişkenimizi gösteren bir fonk yazalım

df.groupby("age")["survived"].mean()  # sayısal değişkenlerde sayısal değişkene göre gruplama yaparsak çok fazla değer çıkar
# bu yüzden tam tersi yapacağız

df.groupby("survived").agg({"age": "mean"})   # böyle olunca isteyebileceğimiz bir veri verdi bize

def target_summary_with_num(dataframe, target, categorical_col):
    print(dataframe.groupby(target).agg({categorical_col: "mean"}))

target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)
    print("##############")





# 5-) KORELASYON ANALİZİ


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv("breast_cancer.csv")
df = df.iloc[:, 1:-1]     # burada ilk veri olan ıd ve son veri olan unnamed i siliyoruz
df.head()




carpim = lambda x: x ** 3

print(carpim(2))




