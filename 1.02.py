price = int(input("enter a unit price : "))

unit = int(input("enter number of unit :"))

price = price*1.16*unit

if price >= 100 :
    price = price*0.95
    print (str(price)+" your price after a 5% descount and IVA")
else :
    print(str(price)+"your price after IVA")




