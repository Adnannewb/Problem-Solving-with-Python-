nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]

#Bruteforce Solution

# def occurance(nums,target):
#     first,last=-1,-1
#     n=len(nums)
#     for i in range(0,n):
#         if(nums[i]==target):
#             if(first==-1):
#                 first=i
#             last=i
#         elif(nums[i]>target):
#             break
#     return [first,last]

# print(occurance(nums,3))


#Optimal Solution

def lowerbound(nums,target):
    n=len(nums)
    l_bound=-1
    low,high=0,n-1
    while(low<high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            l_bound=mid
            high=mid-1
        else:
            low=mid+1
    return l_bound

def upperbound(nums,target):
    n=len(nums)
    u_bound=n
    low,high=0,n-1
    while(low<high):
        mid=(low+high)//2
        if(nums[mid]>target):
            u_bound=mid
            high=mid-1
        else:
            low=mid+1
    return u_bound
    
def occurance(nums,target):
    l_bound=lowerbound(nums,target)
    if(l_bound==-1):
        return 0
    u_bound=upperbound(nums,target)
    return [l_bound,u_bound-1]

print(occurance(nums,3))