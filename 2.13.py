sum = 1
diff = 1
counter = 0
power_of_2 = 1

while diff > 0.001:
    counter += 1
    power_of_2 *= 2
    curr_term = 1/ (power_of_2)
    next_term = 1/ (power_of_2 * 2)
    diff = curr_term - next_term
    print(diff)
    sum += curr_term 

print(sum)