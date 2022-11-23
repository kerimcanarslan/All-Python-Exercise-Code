


################### GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ

# 1-) GENEL RESİM

import seaborn as sns
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")

df.head()
df.info()
df.shape
df.columns
df.index
df.describe().T
df.isnull().any()
df.isnull().values.any()
df.isnull().sum()
df.dtypes



### bunlara bakarak genel resime bakarız.
# fakat bunları kendimiz için tanımlayalım


def check_df(dataframe, head=5):
    print("#"*9 + " SHAPE-BOYUT-ŞEKİL " + "#"*9)
    print(dataframe.shape)
    print("#"*9 + " DTYPE " + "#"*9)
    print(dataframe.dtypes)
    print("#" * 9 + " HEAD " + "#" * 9)
    print(dataframe.head(head))
    print("#" * 9 + " TAİL " + "#" * 9)
    print(dataframe.tail(head))
    print("#" * 9 + " NA-BOŞ DEĞER " + "#" * 9)
    print(dataframe.isnull().sum())
    print("#" * 9 + " QUANTİLES-NİCELLER " + "#" * 9)
    print(dataframe.describe().T)


check_df(df)

df_tips = sns.load_dataset("tips")

check_df(df_tips)

# görüldüğü gibi df_tips veri setinin genel resmini çıkardık.
# Sağda inceleyebilriz


# 1-) KATEGORİK DEĞİŞKEN ANALİZİ (ANALYSIS OF CATEGORICAL VARIABLES)

import seaborn as sns
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")

df["sex"].value_counts()
df["sex"].unique()      # male ve female 2 adet
df["sex"].nunique()     # direkt 2 oalrak cevap verdi. Genelde 10 üstünde
                        # olursa bu sayısal değişken olur.


### kategordik değişkenleri sayısal değişkenlerden ayırmamız lazım
### bunun için value_counts() metodunu sık sık kullanacağız.

################## ÖNCELİKLE


### Verinin infosunu ve tip bilgisini kontol edelim

df.info()

### 14 adet değişkenimiz vardır. Bunlar object, category, bool, int64,float64
### biz kategorik değişkenleri almak ve İNT VE FLOAT oolarak görünen
### sinsi değişkenleri de bulmamız lazım.
### yani numerik ama aslında kategorik olanları çekmemiz lazım
### cat_col = kategorik kolonlar

cat_col = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

### değişkenler arasından kategorik olanları aldık ama numerik olupta kategorik olanlar hala bizimle değil
### bunun için yeni bir num_but_cat = numerik ama kategrik değişkendir
### df colums ta gez. int ve float olanalrı al. bunların nuniqe değerlerini sorgula.
### 10'dan düşükse kategoriktir. Listeye al

num_but_cat = [col for col in df.columns if df[col].dtypes in ["int", "float"] and df[col].nunique() < 10]

### fakat kategorik görünüp te sayısal olanlar olabilir. bunları ayıklayalım

cat_but_num = [col for col in cat_col if df[col].nunique() > 10]
# ya da
cat_but_num = [col for col in df.columns if df[col].nunique() > 10 and str(df[col].dtypes) in [["category", "object", "bool"]]]

### görüldüğü gibi kategorik görünen ama kategorig olmayan herhangi bir değer bulşunmaıd.
### bulunsaydı onları dor döngüsü ile çıkarırdık.

## şimdi üstte bulduğumuz tüm cat değerleri birleştirelim

cat_cols = cat_col + num_but_cat
# cat_col artık tüm kategorik değişkenleri barındırır.

df[cat_col].head()
# bunu doğrulamak için;
df[cat_col].nunique()         ### max 7 değer var çok güzel


######################################################
#### Şimdi öyle bir fonk yazalım ki, kendisine girilen kategorik değişkenlerin
#### value_counts() 'una baksın. Değerleri ve toplam sayısını bize göstersin
#### Bir de bunları yüzdelik olarak hesaplayıp bize göstersin. ÖRnek;

df["survived"].value_counts()                      # 549 adet "0" ve 342 adet "1"
100 * df["survived"].value_counts() / len(df)      # "0" değeri %61.62 "1" değeri 38.38

#bunu fonk. haline getirelim

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#############################")


cat_summary(df, "survived")

### şimdi bunu bişr döngüye sokarak tüm kategorik değişkenler için bakalım

for col in cat_cols:
    cat_summary(df, col)

### Böylece tüm kategorik değişkenlerin aldığı değerleri ve kaç adet oldukları
### ve yüzdelik hesaplamaarının hepsini çıktı olarak aldık.


#######################################
### OLAYA DAHA FARK  BAKALIM VE ÇIKTILARI GRAFİK OLARAK İSTEYELİM
# plot=False # ön tanımlı argüman False, yani değer girilmezse yoksay. dğer girilirse gerçkeliştir

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#############################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "survived", plot=True)

# istediğimiz gibi çalıştı: fakat döngüde çalıacak mı?

for col in cat_cols:
    cat_summary(df, col, plot=True)

# Bool değişkeninde hata verdi. Çünkü bool değişkeni 2 sınıfa ayrıldığı için
# bu tarz grafiklerde kullanılmaz. Bu yüzden bool değişkenlerini int'e dönüştürüp
# işleme öyle devam etmeliyiz

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("# Bu AMK evladı bu tarz grafiklerde çalışmaz, önce int'e çevir sonra gel")
    else:
        cat_summary(df, col, plot=True)

######## gördüğünüz gibi bool dışındadkileri çalıştırdı.


### diyelim ki değiştirmek de istiyoruz. döngğü içine ekleyelişm hemen

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


########## gördüğnüz gibi bunu dah çözdük



