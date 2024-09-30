bit1 = int(input("Enter the first bit (0 or 1): "))
bit2 = int(input("Enter the second bit (0 or 1): "))
bit3 = int(input("Enter the third bit (0 or 1): "))


print(bit1, bit2, bit3)


if bit3 == 0:
    bit3 = 1
else:
    bit3 = 0
    if bit2 == 0:
        bit2 = 1
    else:
        bit2 = 0
        if bit1 == 0:
            bit1 = 1
        else:
            bit1 = 0

    
print(bit1, bit2, bit3)

