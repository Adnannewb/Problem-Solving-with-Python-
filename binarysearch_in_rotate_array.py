# nums=[17,18,20,13,4,5,6,7,8,10,11,13,14,16]


#Bruteforce Solution

# def search(nums,target):
#     n=len(nums)
#     for i in range(0,n):
#         if(nums[i]==target):
#             return i
#     return -1
# print(search(nums,4))

nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
#Optimal Solution
#without Duplicates

# def search(nums,target):
    
#     n=len(nums)
#     low,high=0,n-1
#     while(low<=high):
#         mid=(low+high)//2
#         if(nums[mid]==target):
#             return mid
#         if(nums[mid]<=nums[high]):
#             if(nums[mid]<=target<=nums[high]):
#                 low=mid+1
#             else:
#                 high=mid-1
#         else:
#             if(nums[low]<=target<nums[mid]):
#                 high=mid-1
#             else:
#                 low=mid+1
#     return -1
# print(search(nums,2))


# with duplicates
def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # IMPORTANT: duplicates case
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1

        # Left half sorted
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
print(search(nums,2))