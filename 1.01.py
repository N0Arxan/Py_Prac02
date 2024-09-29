Min = int(input("enter the minutes : "))
Tar = input("which Tarifa (D/N) : ")

if Tar == "N" or Tar=="n" :
    cent = Min*10
elif Tar == "D" or Tar== "d":
    cent = Min*15
else :
    print("tarifa not defind")

print (str(cent/100)+"Euro your account")
