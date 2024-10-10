n = int(input("inter n :"))
cn = 0
m = int(input("inter m :"))

for i in range(1,m+1):
    if m % i == 0 and cn < n:
        print(i)
        cn += 1