nums=[2,4,6,7,9,11,18,19]

#iterative solution
def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return -1
print(binarysearch(nums,2))

#Recursive solution

def binarysearch(nums,low,high,target):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(nums[mid]==target):
        return mid
    elif(nums[mid]<target):
        return binarysearch(nums,mid+1,high,target)
    else:
        return binarysearch(nums,low,mid-1,target)
    
print(binarysearch(nums,0,len(nums)-1,19))