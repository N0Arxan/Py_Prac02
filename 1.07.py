nums = input("inter 3 numbers:1,2,3 \n")
nums = nums.split(",")
nums = list(map(int,nums))

max = nums[0]
for i in  range(len(nums)) :
    if max < nums[i]:
        max=nums[i]

print(max)
