nums=[7,8,1,2,3,4,5,6]

#bruteforce Solition

# def minimum(nums):
#     n=len(nums)
#     mini=float("inf")
#     for i in range(0,n):
#         mini=min(mini,nums[i])
#     return mini
# print(minimum(nums))

#optimal Solution

def minimum(nums):
    n=len(nums)
    mini=float("inf")
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]<=nums[high]):
            mini=min(nums[mid],mini)
            high=mid-1
        else:
            mini=min(mini,nums[low])
            low=mid+1
    return mini
print(minimum(nums))