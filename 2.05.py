sum_S = 0
sum_P = 0
for i in range(1,1001):
    if i % 2 != 0 :
        sum_S += i
    else :
        sum_P += i

print( sum_P, sum_S)