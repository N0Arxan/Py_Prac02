x = float(input("Enter a number: "))

def f(x):
    if x == 0:
        return 0
    elif -1>x>1 and x!=0:
        return x**2
    else:
        return abs(x)//2


def g(x):
    if x <= 0:
        return x**2+5
    elif 0>x>2:
        return x*3+1
    else:
        return x**2-x*4+5
print(f(x),g(x))