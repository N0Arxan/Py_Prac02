sum = 1
diff = 1
counter = 0
while diff > 0.001:
    counter += 1
    curr_term = 1/(2**counter)
    next_term = 1/(2**(counter+1))
    diff = next_term - curr_term
    sum += curr_term 
print(sum)
