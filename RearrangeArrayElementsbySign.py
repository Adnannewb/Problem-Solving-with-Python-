nums=[5,10,-3,-1,-10,6]

#brute force 

# def rearrange(nums):
#     n=len(nums)
#     pos=[]
#     neg=[]
#     for i in range(n):
#         if(nums[i]>=0):
#           pos.append(nums[i])
#         else:
#             neg.append(nums[i])
#     for i in range(len(pos)):
#         nums[2*i]=pos[i]
#         nums[2*i+1]=neg[i]
#     return nums
# print(rearrange(nums))  

#Optimal solution
def rearrange(nums):
    n=len(nums)
    i=0
    j=1
    result=[0]*n
    for k in range(n):
        if(nums[k]>=0):
            result[i]=nums[k]
            i+=2
        else:
            result[j]=nums[k]
            j+=2
    return result
print(rearrange(nums))    