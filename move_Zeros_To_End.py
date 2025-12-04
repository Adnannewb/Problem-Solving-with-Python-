nums=[0,1,0,2,4,3,0,0,3,5,1]

# Bruteforce solution

# def zerosToEnd(nums):
#     n=len(nums)
#     temp=[]
#     for i in range(0,n):
#         if(nums[i]!=0):
#             temp.append(nums[i])
#     for i in range(0,len(temp)):
#         nums[i]=temp[i]
#     for i in range(len(temp),n):
#         nums[i]=0

#     return nums
# print(zerosToEnd(nums))   


# Optimal Solution

# def zerosToEnd(nums):
#     n=len(nums)
#     if(n==1):return nums
#     i=0
#     while(i<n):
#         if(nums[i]==0):
#             break
#         i+=1
#     j=i+1
#     while(j<n):
#         if(nums[j]!=0):
#             nums[j],nums[i]=nums[i],nums[j]
#             i+=1
#         j+=1    
#     return nums
# print(zerosToEnd(nums))  