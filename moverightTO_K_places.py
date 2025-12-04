nums=[5,9,1,7,10,3]

#Brute force slution 
# def rotateright(nums,k):
#     n=len(nums)
#     k=k%n
#     for _ in range(0,k):
#         e=nums.pop()
#         nums.insert(0,e)
#     return nums
# print(rotateright(nums,3))    

#Better solution
# def rotateright(nums,k):
#     n=len(nums)
#     k=k%n
#     nums[:]=nums[n-k:]+nums[:n-k]
#     return nums
# print(rotateright(nums,3))  

#Optimal Solution

def reverse(nums,left,right):
    while(left<right):
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
def rotateright(nums,k):
    n=len(nums)
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)
    return nums
print(rotateright(nums,5)) 