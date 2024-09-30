Min = int(input("enter the minutes : "))
Tar = input("which Tarifa (D/N/P) : ")

if Tar == "N" or Tar=="n" :
    cent = Min*10
elif Tar == "D" or Tar== "d":
    cent = Min*15
elif Tar == "P" or Tar == "p" :
    cent = Min * 25
else :
    print("tarifa not defind")

print (str(cent/100)+" Euro your account")