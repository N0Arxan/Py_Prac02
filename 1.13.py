a:int = int(input("enter a"))
b:int = int(input("enter b"))
c:int = int(input("enter c"))
d:int = int(input("enter d"))

print(f'{a}/{c} + {b}/{d} = \n')
try:
   res = (a/c) + (b/d)

   print(res)
except ZeroDivisionError:
   print("you cant divide somthing by zero idiot")