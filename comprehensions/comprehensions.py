#########
# List Comprehensions

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x


null_list = []

for salary in salaries:
    if salary > 2000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))
print(null_list)


# bnu eski usulde böyle yapıyorduk.
# işlemleri daha da kısaltmak için comprehensions kullnacağız. bunu şu şekilde yapabilriz.
# köşeli bir parantez açarak başlar ve işlemleri sıralarız.

[new_salary(salary * 2) if salary > 2000 else new_salary(salary * 3) for salary in salaries]

# yukarudaki kalıpta şunu yaptık.
# sırası ile önce eğer maaşımız 2000'den büyükse salary*2 yapıyoruz.
# else ise yani değilse de salary * 3 yapıyoruz
# sonrada for döngüsü içine sokarak köşeli parantezi kapatıyoruz
# köşelş parantez içinde bu işlemleri yaptığımzı için bize direkt sonuç çıkar.



# mesela maaşlar listesini iki ile çarpmak için de yapabiliriz

[salary * 2 for salary in salaries]

# eğer sadece if kullanılacaksa if kısmı sağ tarafta sonda kullanılmalıdır.
# eğer if ve else yapısı birlikte kullanılırsa if else yapısı en başta yani sağda kullanılır

[salary * 3 for salary in salaries if salary < 2500]

[salary * 3 if salary < 2500 else salary * 2 for salary in salaries]

# buradaki örnekte if ve else yapısının kullanımını gördük.


students = ["Jhon", "Mark", "Venessa", "Mariam", "Ahmet", "Mehmet"]
students_no = ["Jhon", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]

# burada in yerine not in kullanarak işlemi tam tersine çevirebiliriz

[student.lower() if student not in students_no else student.upper() for student in students]

# artık istenmeyen öğrenciler listesinde bulunan jhon ve venessa büyük harfe yazar, diğer öğrenciler küçük harfle yazar.
# böylece 6-7 satırda yaptırğımız işlemşi sadece 1 satırda halledebildik.

########
# dict comprehensions

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

dictionary.keys() #key değerlerini liste içinde gösterir
dictionary.values() #value değerlerini liste içinde gösterir
dictionary.items() #değerleri liste içinde tek tek tuple olarak gösterir

{k: v ** 2 for k, v in dictionary.items()}
# burada şunu yaptık.
# dictonary sözlüğünü tuple yaparak(items) içinde gez emri verdik.
# içindeki verilere keys yani "k" Values yani "v" demesini istedik.
# k değerlerini sabit bırakarak v değerlerinin karesini aldık.
# bunuda yine süslü parantez içinde sözlğk olarak dışarı yazıdrdık.
# şimdi ise key değerleini değişip(küçük büyük yapıp) v değerini sabit bıraklaım.

{k.upper(): v for k, v in dictionary.items()}
# burada da k değerini büyük harfe çevirerek v değeri ile oynamadık.


# comprehensions ile mülakat sorusu

# Amaç: çift sayıların karesi alınaraj bir sözlüğe eklenmek istenmektedir.
# key'ler orijinal değer, value'lar ise değiştirilmiş değer olacak.

# önce eski yöntem ve döngüler kullanarak yapalım.
# range ile 0'dan 10 a kadar sayılar oluşturalım

numbers = range(10)
new_dict = {}  # burada boş bir sözlük oluşturduk. Çünkü çıktılarımızı bunun içine atacağız.

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2 #hayat kurtaran# burada köşelş parantez kullanarak key bölümüne n değerini olduğu gibi yaz demiş olduk. Eşittirden sonra da value değerinin karesini aldık.

new_dict

#şimdi bunu dict comprehensions ile yapalım.

numbers = range(10)
new_dict = {}

{n: n ** 2 for n in numbers if n % 2 == 0}




#############   list ve Dict comprehensions uygulamaları


# Bir veri setindeki değişken isimleri değiştirmek

# veri seti içindeki değişken isimlerini değiştirmek(büyük-küçük) yapmak için) ;
# eski usul ile yapmayı deneyelim

import seaborn as sns  # seaborn kütüphanesini indir ve sns olarak tanımla.
df = sns.load_dataset("car_crashes") # sns içinden "car_crashes" veri setini indir ve bunu df(data_frame) olarak keydet.
df.columns # df.columns komutu ile df veri setindeki değişkenleri yazdırır.


# burada total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev'
# değişkenler mevcuttur. Buradaki değişkenleri büyük harf yapıp veri seti içine kaydedelim.
# bu eski yöntem;

A =[]

for col in df.columns:
    A.append(col.upper())

A     # A listesini yazdırınca değişkenlerin büyüdüğünü gördük.
# veri setine (df) eklenmesi için

df.columns = A
df.columns
# df.columns a tekrar bakınca değişkenlerin büyüfğünüğ görebiliriz.

##################
# hadi bunu list comprehensions kullanarak yapaalım

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

#kütüphenemizi ve veri setini indirdik

df.columns = [col.upper() for col in df.columns]
df.columns

# yukarıda 7-8 satırda yaptığımız işlemi sadece 1 satırda yaptık. df.columns içinde gez ve bulduğun her veriye col de
# col ismini verdiğin verileri upper ile büyük harfe çevir. Eşittir df.columns dediğimizde artık ;
# df.columns artık değişecektir. df.colums yazdırdığınızda değişken isimleri artık büyük harf çıkacaktır.

#########
# şimdi ise farklı bir değişiklik yapalım. Değişken isimlerinde
# "INS" olanların başına FLAG ifadesi yazsın
# "INS" olmayanların başında ise NO_FLAG yazsın

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns]

# kolonlarda gez ve bunlara col ismini ver.
# her bir col da ins ifadesi varsa başına flag ekle
# col da ins ifadesi yoksa no_flag ekle
# list comprehensions parantezini kapatarak lsite halinde bize göster.
# bu ifadeyi df.columns a eşitlersek artık df.columns güncel haliyle karşımzıa çıkacaktır.

df.columns = ["FLAG_" + col if "ins" in col else "NO_FLAG_" + col for col in df.columns]
df.columns


# Çok kritik bir dict comprehensions ile yeni bir problem çözelim

# key değerlerimiz string, value değerlerimiz ise bir lsite halişnde olacak. örnek;

#{'total': ['mean', 'min', 'max', 'var']
# 'speeding': ['mean', 'min', 'max', 'var']
# 'alcohol': ['mean', 'min', 'max', 'var']
# 'not_distracted': ['mean', 'min', 'max', 'var']
# 'no_previous': ['mean', 'min', 'max', 'var']
# 'ins_premium': ['mean', 'min', 'max', 'var']
# 'ins_losses': ['mean', 'min', 'max', 'var']
# 'abbrev': ['mean', 'min', 'max', 'var']
#}

# fakat burada abbrev değişkeni sayısal bir değeri temsil etmiyor
# sistem bizden sadece sayısal değerleri istiyor, bu yüzden abbrev'in olmaması gerek

# öncelikle yine verimzii çekelim

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# bu işlmleri öcne uzun yol ile yapalım.

num_col = [col for col in df.columns if df[col].dtype != "O"]
num_col

# görüldüğü gibi isteğimiz sayısal değişkenler çıktı.
# burada df.[col].dtype != "O" ifadesi şu demek
# data frame içinde her col ifadesine bak
# bu ifadelerin dtype'ına bak
# bu dtype'lar Object'e yani ("O") eşit değilse(yani sayısal bir ifade ise) kullanmak için al
# aynı ifadeyi dtype == "O" şeklinde yapsaydık sadece sayısal olmayan ifadeleri getirirdi.
# burada object ifadesi nesne olarak yazılı bir şey oalrak tanımnlanabilir.
 # ilk olarak sorunu çözdğük, sadece sayısal değişknelri aldık.
 # şimdi devam edelim


num_col = [col for col in df.columns if df[col].dtype != "O"]
soz = {}  # bos bir sözlük oluşturduk
agg_list = ['mean', 'min', 'max', 'sum']  # burası da eklememnemiz gereken value değerinin örneği

# şimdi yeni bir şey öğreniyoruz;

for col in num_col:
    soz[col] = agg_list
    soz

    # burada soz u yazdırınca istediğimiz şeye ulaşıyoruz
    # bu ifadeyi ilk defa gördük. Burada soz[col] demek sözlüğün key değerlerine col da bulduklarını yaz demek
    # eşittirden sonrası ise agg_list kısmında, value değerlerimizi agg_list'ten alıp yerine koy demek

# yukarıdaki yöntem uzun yöntemdi.
# şimdi daha kısa olan şekilde yapacağız. dict comprehensions ile yapacağız

num_col = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ['mean', 'min', 'max', 'sum']
sondict = {col: agg_list for col in num_col}
sondict

#bu şekli daha önce görmüştük. burada : ifadesinin sol tarafında key değeri sağ tarafında ise value değeri eklleriz
# şimdi yaptığımız tüm bu işlemlerin ne işe yaradığına bakalım

df[num_col].head()

#head metodu ile kısaca df[num_col] df içindeki sayısal değerlere bakıyopruz

df[num_col].agg(sondict)


# agg metodu ile df[num_col] içerisine en son elde ettiğimiz sondict sözlüğünü ekliyoruz
# böylece dict içinde yazdığımız mean, min, max ve sum fonk.ları tüm veri seti için çalışır ve bize cevap verir
# son olarak her bir kolonun ortalama, max, min ve toplam değerlerini gösterir



num_col_type = [df[col].dtype for col in df.columns]
num_col = [col for col in df.columns if df[col].dtype == "float64"]

