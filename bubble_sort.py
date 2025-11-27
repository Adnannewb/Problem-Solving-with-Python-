# nums=[5,8,1,6,9,8,4]
# def bubble_sort(nums):
#     n=len(nums)
#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):            #average and worst case scenario
#             if(nums[j]>nums[j+1]):
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
# bubble_sort(nums)
# print(nums)  

nums=[1, 4, 5, 6, 8, 8, 9]
def bubble_sort(nums):
    n=len(nums)
    is_sort=False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):            #Best Case Scenario
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_sort=True
        if(is_sort==False):
            print("break")
            break        
bubble_sort(nums)
print(nums)                