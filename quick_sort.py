# nums=[4,1,2,3,7,6,8]
nums=[3,1,2,4,1,5,2,6,4]

def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while(i<j):
        while (nums[i]<=pivot and i<=high-1):
            i+=1
        while(nums[j]>=pivot and j>=low+1):
            j-=1
        if(i<j):
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j

def quicksort(nums,low,high):
    if(low<high):
        partition_index=partition(nums,low,high)
        quicksort(nums,low,partition_index-1)
        quicksort(nums,partition_index+1,high)
        
quicksort(nums,0,len(nums)-1)
print(nums)            
        