"""  GİRİLEN SAYI TEK mi ÇİFT mi?

sayi=int(input(" bir sayı giriniz : "))

if sayi %2==0 :
    print("girilen sayı çift ",)
else:
    print("girilen sayı tek ")
"""

"""GİRİLEN SAYI POZİTİF mi NEGATİF mi

sayi=int(input(" bir sayı giriniz : "))

if sayi>0 :
    print("girilen sayı POZİTİF ")
elif sayi<0 :
    print("girilen sayı NEGATİF ")
else :
    print("sayı sıfıra eşit ")
"""

"""
x=1
while x<=100:
    if x%2==0:
        print("sayı çift -->"+str(x))
    else:
        print("sayı  tek -->"+str(x))
    x+=1
"""

bilet_T=50
bilet_S=20
bilet=input("Bilet tiyatro için mi Sinema içinmi T/S : ")
ogrenci=input("ögrenci mi Tam mı? O/T : ")

if bilet.upper()=="T":
    if ogrenci.upper()=="O":
        print("Tiyatro bilet fiyatı (ogrenci): " + str(bilet_T-(bilet_T/5)) + " TL")
    else:
        print("Tiyaro bilet fiyatı : " + str(bilet_T) + " TL")
else:
    if ogrenci.upper()=="O":
        print("Sinema bilet fiyatı (ogrenci): " + str(bilet_S-(bilet_S/5)) + " TL")
    else:
        print("Sinema bilet fiyatı : " + str(bilet_S) + " TL")  
