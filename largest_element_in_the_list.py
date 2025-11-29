# nums=[55,32,-87,99,3,67]
nums=[-4,-2,0,-200,-100]
n=len(nums)
largest=float("-inf")
print(largest)
for i in range(0,n):
    largest=max(largest,nums[i])
    # if(largest<nums[i]):
    #     largest=nums[i]
print(largest)    
    