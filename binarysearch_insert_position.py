# nums=[1,3,4,5,8,9,14,15,19,20,21]
nums=[1,3,5,6]
#Bruteforce Solution
# def insertpostion(nums,target):
#     n=len(nums)
#     for i in range(0,n):
#         if(nums[i]>target):
#             return i
# print(insertpostion(nums,16))

#optimal solution
def insertpostionopt(nums,target):
    n=len(nums)
    l_bound=n
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            l_bound=mid
            high=mid-1
        else:
            low=mid+1
    return l_bound

print("Optimal solution: ",insertpostionopt(nums,0))