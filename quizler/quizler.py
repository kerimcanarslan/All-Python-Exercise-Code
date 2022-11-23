keyywooo = "abracadabra"
new_group = []

for i, let in enumerate(keyywooo,1):
    if i * 2 % 2 ==0:
        new_group.append(let)

print(new_group)



b = True
type(b)

s = {"python", "machine learning", "data_sciencist"}
type(s)

text = "Thea goal is to turn data into information, and information into insight"

text.upper().split()


lst = ["D", "A", "T", "A", "S", "C", "İ", "E", "N", "C", "E"]

print(lst[0], lst[10])
# eleman sayısı

len(lst)

new_lst = []

for i, v in enumerate(lst):
    if i == 0:
        new_lst.append(v)
    elif i == 10:
        new_lst.append(v)
print(new_lst)

[lst.pop(i) for i, v in enumerate(lst) if i > 3]
print(lst)


for i, v in enumerate(lst):
    if i > 3:
        lst.pop(i)

print(lst)


nw_lst = []

[nw_lst.append(value) for index, value in enumerate(lst) if index < 4]
print(nw_lst)


nw_lst.append(lst[0:4])

nw_lst

lst.pop(8)
lst.append("w")
lst.insert(8, "N")
lst

dict = { 'Christian': ["America", 18],
         'Daisy': ["England", 12],
         'Antonio': ["Spain", 22],
         'Dante': ["Italy", 25]}

dict.keys()
dict.values()

dict.update({'Daisy': ["England", 13]})
dict

dict.update({'Ahmet': ["Turkey, 24"]})
dict

dict.pop('Antonio')
dict


liste = [2, 13, 18, 93, 22]

even_list = []
odd_list = []

def tek_cif(x):
    for i in x:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return odd_list, even_list


tek_cif(liste)

odd_list
even_list


ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, name in enumerate(ogrenciler, 1):
    if i == 1:
        print("Mühendislik Fakültesi 1.öğrenci:", name)
    elif i == 2:
        print("Mühendislik Fakültesi 2.öğrenci:", name)
    elif i == 3:
        print("Mühendislik Fakültesi 3.öğrenci:", name)
    elif i == 4:
        print("Tıp Fakültesi 1.öğrenci:", name)
    elif i == 5:
        print("Tıp Fakültesi 2.öğrenci:", name)
    elif i == 6:
        print("Tıp Fakültesi 3.öğrenci:", name)


ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, name in enumerate(ogrenciler, 1):
    if i < 4:
        print("Mühendislik Fakültesi", i, ".öğrencisi:", name)
    else:
        i = i - 3
        print("Tıp Fakültesi", i, ".öğrencisi:", name)




ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

A = list(zip(ders_kodu, kredi, kontenjan))
A
for i, v in enumerate(A):
    print("Kredisi", A[i][1], "olan", A[i][0], "kodlu dersin kontenjanı", A[i][2], "kişidir")


for kod, kredi, kont in A:
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kont} kişidir")



kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])



def funct(a, b):
    if b.issubset(a):
        print(a & b)
    else:
        print(b - a)


funct(kume1, kume2)


def func2(x, y):
    if x.issuperset(y):
        print(x.intersection(y))
    else:
        print(y.difference(x))



func2(kume1, kume2)




#student_scores_list=['Harry', 37.21,'Berry', 37.21,'Tina', 37.2,'Akriti', 41,'Harsh', 39]
#2. en düşük nota sahip kişilerin adlarını alfabetik sıraya göre yazınız.
#**Liste sırasıyla öğrenci ve aldığı notu ifade etmektedir.
#Not: Listedeki kişi sayısı değişiklik gösterebilir, birden fazla en düşük not veya en düşük ikinci nota sahip kişiler olabilir.

def ikiyibul(a):
    key = list(filter(lambda x: type(x) == str, a))
    value = list(filter(lambda x: type(x) != str, a))
    new_dict = dict(zip(key, value))
    new_dict1 = dict(sorted(new_dict.items(), key=lambda x: x[1]))

    for k, v in new_dict1.items():
        if v == new_value[1]:
            son = print(k)
    return son





student_scores_list = ['Harry', 37.21,'Berry', 37.21,'Tina', 37.2,'Akriti', 41,'Harsh', 39]

key = list(filter(lambda x: type(x) == str, student_scores_list))

value = list(filter(lambda x: type(x) != str, student_scores_list))

new_dict = dict(zip(key, value))


new_list = sorted(list(zip(key, value)), key=lambda x: x[1])

new_dict1 = dict(sorted(new_dict.items(), key=lambda x: x[1]))


new_key = list(new_dict1.keys())
new_value = list(new_dict1.values())
son = []

for k, v in new_list:
    if v == new_value[1]:
        print(k)

ikiyibul(student_scores_list)
