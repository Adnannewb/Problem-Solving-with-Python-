nums=[55,32,-87,99,3,67]
n=len(nums)

#using sorting
# nums.sort()
# print(nums[n-2])

#Better solution
# largest=float("-inf")
# second_largest=float("-inf")
# for i in range(0,n):
#     largest=max(largest,nums[i])
# for i in range(0,n):
#     if(nums[i]>second_largest and nums[i]!=largest):
#         second_largest=max(second_largest,nums[i])
# print(second_largest)  

#Optimal Solution
largest=float("-inf")
second_largest=float("-inf")
for i in range(0,n):
    if(nums[i]>largest):
        second_largest=largest
        largest=nums[i]
    elif(nums[i]>second_largest and nums[i]!=largest):
        second_largest=nums[i]
print(second_largest)            