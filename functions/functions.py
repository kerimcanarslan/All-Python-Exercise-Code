#fonkisyonlar

#fonkisyonların ne olduğunu ve argümanlarının ne işe yaradığını görmek için
#?print ya da help(print) yapabiliriz

?print
help(print)

print("a", 2, end=".")

#fonksiyon tanımlama

def calculate(x):
    print(x*2)


calculate(5)
calculate(12)

#iki argümanlı bir fonk. tanımlama

def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)

#artık summer isimli fonk. sırası ile girilen 2 değeri toplayıp bize gösterecektir.


#şşimd docstring(bilgi notu) hazırlayalım.
# def summer kısmının hemen altına """ yazıp entera basınca bize google, numpy ya da txt formatında docstring çıktı.
# prefences tools python kısmından tercih edilen docstring i google seçip devam ediyoruz.
# yeşil yazı ile bize fonkisyonun görevinin en olduğunu yazmamımızı ve arg1 arg2 kısmına neler yazabileceğimizi belirtmemizi istedi.
# buraya istediğiniz kadar şey ekleyebilirsiniz. mesela example yazarak örnek gösterebilir notes yazarak not düşebilrsiniz.

def summer(arg1, arg2):
    """
    sum of two numbers

    Args:
        arg1:  int, float
        arg2:  int, float


    Returns:
        int, float

    """
    print(arg1 + arg2)


help(summer)

?summer

#böyle sorgu yapınca bizim yazdığımız docstring(fonk hakk bilgi notu) çıktı



######
#fonks. statement bölümü yani body(gövde) bölümü
#parametre ya da argüman girmeden de fonk. oluşturabiliriz

def say_hi():
    print("merhaba")
    print("hello")
    print("hi")


say_hi()


#argüman kullanarak da yapabilriz

def say_hi(string):
    print(string)
    print("hello")
    print("hi")


say_hi("miuul")

# iki ifade girilen ve bu iki ifadeyi çarpan, bu ifadeleri ve sonucunu çıktıda veren bir fonk. yapalım


def multiplication(arg1, arg2):
    print(arg1)
    print(arg2)
    argsonuc = arg1 * arg2
    print(argsonuc)

multiplication(7, 10)



#girilen değerleri bir liste içinde saklama fonksiyonu

list_name = []

def add_element(a, b):
    c = a * b
    list_name.append(c)
    print(list_name)

add_element(45, 10)

add_element(45, 10)
add_element(13, 98)
add_element(56, 38)


# ön tanımlı argümanlar (default parameter/arguments)

def divide(a, b):
    print(a / b)

divide(1, 5)

#bu şekilde bölme işlemi yapınca 1/5 i buluyor. Fakat kullanıcı "b" girişini boş bırakırsa program çalışmaz.
#programda bir giriş boş bırakılırsa ne olacağına karar vermek için;

def divide(a, b = 1):
    print(a / b)


divide(1, 5)

#başka bir örnek;

def say_hi(string = "merhaba"):
    print(string)
    print("hello")
    print("hi")

say_hi()

#string girişine hello ya da hi olarak giriş verilirse o şekilde çıkış oluyor.
#ama kullanıcı giriş vermez ya da unutursa otomatik olarak
#ön tanımlı fonks. devreye giriyor ve "merhaba" çıktısını alıyoruz.


#ne zaman fonks. yazılır?

def elk_direk_hesap(varm, moisture, charge):
    a = varm + moisture
    b = charge
    c = a / b
    print(c)

elk_direk_hesap(70, 26, 91)


#burada şehirdeki elektrik direklerinin sıcaklık nem ve şarj bilgileri ile bir katsayı çıkarıp o katsayı üzerinden
#yapılması gerekene karar vermek için oluşturulmuş bir fonk.


# return dediğimiz şeyler çıktıdır
# return fonksiyon çıktılarını tekrar giriş olarak kullanmak

def elk_direk_hesap(varm, moisture, charge):
    a = varm + moisture
    b = charge
    c = a / b
    return (c)

elk_direk_hesap(70, 26, 91)  * 10

# return komutunu kullanarak çıktı üzeridnen matematik işlem yaptırabiliriz.
# yada bunu şöyle yapabilirdik.

def elk_direk_hesap(varm, moisture, charge):
    a = varm * 2
    b = moisture * 2
    c = charge * 2
    output = (a + b) / c

    return a, b, c, output


elk_direk_hesap(70, 26, 91)

a, b, c, output = elk_direk_hesap(70, 26, 91)

# bu şekilde a, b, c yeni değer ataması yaptırdık ve çıktıyı görmeden önce onları da almayı başardık.



#############
#fonks üzerinden fonks çağırma


def elk_direk_hesap(varm, moisture, charge):
    a = varm * 2
    b = moisture * 2
    c = charge * 2
    output = (a + b) / c
    return output


elk_direk_hesap(1, 2, 3)

def standardization(d, e):
    return d * 12 / 111 * e * e



def all_functionss(varm, moisture, charge, e):
    d = elk_direk_hesap(varm, moisture, charge)
    f = standardization(d, e)
    print(f * 10)

all_functionss(1, 2, 3, 4)


# bu programda ilk fonks. ile bir çıktı elde ettik.
# elde ettiğimiz bu çıktı katsayısını başka bir fonks. da kullanacaktık.
# bu yüzden iç içe geçmiş bir fonks. kalıbı yazıp ilk çıktımıza "d" ismi verdik.
# daha sonra "d" yi kullanarak diğer fonks. çalıştırdık.
# diğer fonks. aldığımız çıktıyı da 10 ile çarparak sonuca ulaştık.




#######
#local ve global değişkenler

# local değişken: fonks içinde kalan, sadece fonks içinde kullanılacak olan
# global değişken: fonks dışında da kullanılan, görüntülenebilen değişkendşr

list_kerim = [1, 2, 3]

def add_element_list(a, b):
    c = a * b
    list_kerim.append(c)
    print(list_kerim)

add_element_list(4, 5)

# burada c değişkeni localdir. fonks. içinde kullanılmıştır. fakat fonks. dışına çıkıp yeni listeye bakınca;
# 1,2,3 ve fonks sonucu olan 20 yi görüyoruz. yani c yi global alana gönderdik.
# fakat sağ alt köşede c değişkenine dair bir şey göremiyoruz.






