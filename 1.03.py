minu = int(input("enter the minutes : "))

if minu > 3 :
    minu -= 3
    price = minu*15
    price +=30
    print (price)
else : 
    print("30")
