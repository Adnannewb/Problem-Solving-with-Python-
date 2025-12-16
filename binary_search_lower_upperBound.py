#find the smallest index of lower and upper bound of a target.
nums=[1,1,1,2,2,3,3,5,6,7,7,7,9,12,12,13]

def lowerbound(nums,target):
    n=len(nums)
    l_bound=n
    low,high=0,n-1
    while(low<high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            l_bound=mid
            high=mid-1
        else:
            low=mid+1
    return l_bound
print("smallest index of lower bound :",lowerbound(nums,3))       


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
print("smallest index of upper bound :",upperbound(nums,3)) 