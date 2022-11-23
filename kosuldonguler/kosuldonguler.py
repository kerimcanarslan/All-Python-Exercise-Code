# koşullar #conditions

#  true or false

1 == 1
# true cevabı aldık

1 == 2
#false cevabı aldık.

# if eğer demektir

if 1 == 1:
    print("hello")

# 1 diğer 1 e eşitse ekrana hello yazdır dedik ve yazdı





number = 11
if number == 10:
    print("number is 10")

#burada number kelimesne 11 sayısını atadık. sonrada number kelşmesi 10 mu diye sorgulama yaptık.
# eğer number kelimesş 10 ise ekrana number is 10 yaz diye komut verdik.
# fakat ekran tamamen boş öalıltı. çünkü number 11 di

number = 11
if number == 11:
    print("number is 11")

# burada ise sorgulama doğru olduğu için number is 11 yazıldı ekrana

# şimdi else ifadesini kontrol edeceğiz.
# if koşulunda eğer bu doğru ise çalıştır diye komut veriyoruz. ama doğru değilse de başka bir şey yap

#else koşulu

def number_chek(number):
    if number == 10:
        print("yes true answer")

number_chek(10)

# bu şekilde verdiğimiz sayı 10 ise ekrana yes true answer yazıyor.
# Fakat başka bir sayı yazınca komut çalışıyor fakat herhangi bir şey yazmıyor

def number_chek(number):
    if number == 10:
        print("yes true answer")
    else:
        print("wrong asnwer")

number_chek(11)

# burada sayımız doğru ise yes true answer yazar, değilse wrong answer yazacaktır.


# elif komutu ile karşılaştırma yapabilriz

def number_chek(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
        #elif eklenerek daha çok seçenekle de karşılaştırılabilir
    else:
        print("equeal to 10")
        # eğer bunlardan hiç birisi ise sayı 10 dur. o zaman 10 yazdır.

number_chek(10)

# grüldüğü gibi girilen tüm değerlere karşılık verilebilecek cevaplar fonk. da mevcut



# döngüler #LOOPS

# for loop

students = ["jhon", "mark", "venessa", "mariam"]

students[0]
students[1]

for studentname in students:     # students listsinde gez, gezerken çıkan sonuçlara stutendname de ve listele
    print(studentname)
# burada students listesi içindeki verilerin tamamını yazdırmak için;
# stutendname olarak adlandırıyoruz ve ve stutendts listesi içinden çekiyoruz,,

# burada yazılan isimleri büyütmek içinse; .upper metodu

for studentname in students:
    print(studentname.upper())
# görüldüğü gibi isimler artık büyük harfle yazılacaktır.


salaries = [1000, 2000, 2500, 3500, 5000]

for salary in salaries:
    print(salary)

# bu maaşlara yüzde 20 zam uygulamak istiyoruz diyelim,

for salary in salaries:
    print(salary * 1.20)

for salary in salaries:
    print(int(salary * 1.20))

# hemen bir fonksiyon oluşturalım. Maaş ve yapılmak istenen zam oranunu girince yenşi maaşı göstersin

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

new_salary(1000, 50)


new_salary(1500, 20)
 # bunu genele vurup tüm listede yapmak için


salaries = [1000, 2000, 2500, 3500, 5000]

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

for salary in salaries:
    print(new_salary(salary, 20))


# şimdi maaşı 3000 altında olanlara farklı bşr zam, üstünde olanara farklı bşr zam yapalım.

salaries = [1000, 2000, 2500, 3500, 5000]

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 20))
    else:
        print(new_salary(salary, 30))



# Mülakat sorusu ve uygulama


# before = "hi my name is john and i am learning python"
# after = "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

# öyle bir program yazın kı girilen string ifadenin değerlerinden
# çift olanı büyük yapsın, tek olanı küçük yapsın. Küçükse de küçük bıraksın
# boyut bilgisi için;

len("hi my name is john and i am learning python")
# 43 adet karakter vardır. bunu range içine alırsak bize aralığı vercektşir
range(len("hi my name is john and i am learning python"))
# 0 ile 43 arasında değerleri vardır diye cvevap verdi.
# range ile for döngüsünde gezme ihityacımızı karşılayacağız.

# çift olanları bulmak için 2 ye bölümünden kalanalra bakarız.
# eğer 4 % 2 == 0 ise o ifade çifttir.


def alternating(string):
    new_string = ""
    # girilen stringin indexlerinde gez
    for string_index in range(len(string)):
        # sırası gelen index çift ise bunu yap. (yukarıdaki boş new_string'in içine ekle +=)
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # sırası gelen index tek ise bunu yap
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("hi my name is john and i am learning python")

#break, while ve continue

salaries1 = [1000, 2000, 3000, 4000, 5000]

for maas in salaries1:
    if maas == 3000:
        break
    print(maas)

# break kullanarak döngüyü durdurduk. Maaş 3000 e eşitse orada dur dedik.
# çıktı olarak 1000 ve 2000 çıktı sadece


for maas in salaries1:
    if maas == 3000:
        continue
    print(maas)

# continue kullandığımızda maas eğer 3000 ise onu saymadan döngüye devam et deriz.
# çıktı olarak 1000,2000,4000 ve 5000 çıkar

for maas in salaries1:
    if maas == 3000:
        continue
    print(maas)

#while döngüsü (olduğu sürece devam et)

number = 1
while number < 5:
    print(number)
    number += 1

# burada number 1 dedik. Number 5'ten küçük olduğu sürece yazdır dedik.
# döngü oluşsun diye s-aldığımız her sonuca +1 ekledik.
# ve 4. döngüden sonra number artık 5 oldu ve işlem durdu.

############
# enumerate: otomatik counter/for loop ile kullan
# aldığımız çıktıların index bilgisi ile birkikte almamızı sağlar

students = ["ahmet", "hakan", "kerim", "merve", "ayşe", "ali"]

for index, studentname in enumerate(students):
    print(index, studentname)
# burada çıktımız şöyle oldu.
#0 ahmet
#1 hakan
#2 kerim
#3 merve
#4 ayşe
#5 ali
# her öğrencinin önünde hangi değerde olduğu yazacak şekişlde çıktı aldık.

# örnek soru: İndexi çift olanları A listesine indexi tek olanları B listsine at

A = []
B = []

for index, studentname in enumerate(students):
    if index % 2 == 0:
        A.append(studentname)
    else:
        B.append(studentname)
print(A)
print(B)


# mülakat sorusu

#########
# divide_students fonk. yaz
# Çift indexte yer alan öğrencileri bir lsiteye al
# tek indexte olan öğrencileri farklı bir listeye al
# fakat bu iki liste tek bir liste olarak return olsun.


students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    print(groups)
    return groups


divide_students(students)

stlist = divide_students(students)
stlist[0]


#############
#ilk mülakat sorusunu enumerate ile yapmayı deniyoruz

a = "hi my name is john and i am learning python"

def alterating_with_enumerate(string):
    new_string = ""
    for i, word in enumerate(string):
        if i % 2 == 0:
            new_string += word.upper()
        else:
            new_string += word.lower()
    print(new_string)
    return new_string

alterating_with_enumerate(a)


#################
#zip konusu
# liste birleştirme

students = ["John", "Mark", "Venessa", "Mariam"]
salaries1 = [1000, 2000, 3000, 4000]
ages = [19, 20, 23, 23]

list(zip(students, salaries1, ages))

# lişste içinde bulunan her bir elemanın aynı sıradaki eşi ile aynı sırada çıktısını almak




#############
# lambda, map, filter, reduce

#lambda kullan at fonks. gibi düünürü

def summer(a, b):
    return a + b
# bu fonksiyon a ve b yi birbiri ile toplayan bir fonk. Bunu def ile yazarız
# şimdi bunu lambda ile yazalım

new_sum = lambda a, b: a + b
# burada new_sum fonk. içine girilen a ve b yi birbiri ile toplar.bunu def kullanmadan daha kolay ve basit bir şekilde yaptık.
new_sum(5, 6)
# cevap 11
new_sum(5, 7) * 3
# cevap 36

# map fonksşyonu
# döngü kullanmadan çıktı almak için kullanılır. Mesela def ve for kullanarak:

salaries1 = [1000, 2000, 3000, 4000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(salaries1)

# sadece def kullanarak bu işlemş yapamadık. burada sadece tek bir değeri gerçekleştirir. listeyi gerçekleştrmez
# bunun için for döngüsüne sokmuştuuk.

def new_salary(x):
    return x * 20 / 100 + x
for salary in salaries1:
    print(new_salary(salary))
# burada for döngüsü kullandık ama kullanmadan map ile yapabiliriz.

salaries1 = [1000, 2000, 3000, 4000]

def new_salary(x):
    return x * 20 / 100 + x

list(map(new_salary, salaries1))

# burada def ile fonk. oluştuırduk. Map i kullanarak şunu demiş olduk.
# map(1, 2)
# 1.değer: al sana bir fonk.
# 2.değer ise : al sana bir değerler listesi
# bu değerleri 1.fonksiyona sok işlem yap.
# tüm değerleri yaptıktan sonra çıktıyı list(map()) içinde bana ver.

####
# şimdi lambda ve map arasındaki ilişkşiye gelelim
# lambda yı kullanarak işlem kalabalığını azaltabiliriz.
# lambda ile def kullanmadan direkt fonk yazıp kullan at fonk. oluşturabilriz.
# örnek

salaries1 = [1000, 2000, 3000, 4000]

list(map(lambda x: x * 20 / 100 + x, salaries1))

# burada hiç bir def fonk. kullanmadan, for döngüsüne sokmadan tüm maaşlara yüzde 20 zam yaptırdık.,,,

## FILTER

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2 == 0, numero))

# burada da numero listesi içinden 2'ye bölümünden kalan 0 olanaları göster demiş olduk.
#



### REDUCE

