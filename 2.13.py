sum = 1
diff = 1
i = 0
while diff > 0.001:
    i += 1
    n = 2**i
    n2 = 2**(i+1)
    res = 1/n
    res2 = 1/n2
    diff = res-res2
    sum = sum + res 
print(sum)
