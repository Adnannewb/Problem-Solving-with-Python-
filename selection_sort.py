nums=[5,7,8,4,1,6,9,2]
# def selection_sort(nums):
#     n=len(nums)
#     for i in range(0,n):
#         min_index=i
#         for j in range(i+1,n):
#             if(nums[j]<nums[min_index]):      # Ascending Order
#                 min_index=j
#         nums[i],nums[min_index]=nums[min_index],nums[i]
                
# selection_sort(nums)
# print(nums)

def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if(nums[j]>nums[max_index]):        #Descending Order
                max_index=j
        nums[i],nums[max_index]=nums[max_index],nums[i]
                
selection_sort(nums)
print(nums)

