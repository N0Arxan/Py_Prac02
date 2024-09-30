print ("Ax^2+Bx+C \n")
A = int(input("insert A : "))
B = int(input("insert B : "))
C = int(input("insert C : "))

delta = B**2 - 4*A*C

if delta == 0 :
    x1 = -1*B/2*A
    print("x1 and x2 are the same =" , x1)
elif delta > 0 :
    x1 = -1*B + delta / 2*A
    x2 = -1*B - delta / 2*A
    print(x1,"=X1\n",x2 ,"=X2")
else :
    print ("your equation dosent have answer")
