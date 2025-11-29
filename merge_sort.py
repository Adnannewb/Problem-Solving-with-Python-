nums=[3,1,2,4,1,5,2,6,4]

def mergesort(nums):
    length=len(nums)
    if(length<=1):
        return nums
    mid=length//2
    left_nums=nums[:mid]
    right_nums=nums[mid:]
    left=mergesort(left_nums)
    right=mergesort(right_nums)
    return merge(left,right)

def merge(left,right):
    result=[]
    n,m=len(left),len(right)
    i,j=0,0
    while(i<n and j<m):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if(i<n):
        while(i<n):
            result.append(left[i])
            i+=1
    if(j<m):
        while(j<m):
            result.append(right[j])
            j+=1
    return result            
                    
sorted_nums=mergesort(nums)      #TC=NLogN  
print(sorted_nums)