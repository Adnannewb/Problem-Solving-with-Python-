nums=[-1,0,1,2,-1,-4]


#Brute force solution
# def threeSum(nums):
#     n=len(nums)
#     resultset=set()
#     for i in range(0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if(nums[i]+nums[j]+nums[k]==0):
#                     temp=[nums[i],nums[j],nums[k]]
#                     temp.sort()
#                     resultset.add(tuple(temp))
#     return [list(ans) for ans in resultset]

# result=threeSum(nums)
# print(result)


#Better Solution
# def threesum(nums):
#     n=len(nums)
#     resultset=set()
#     for i in range(0,n):
#         myset=set()
#         for j in range(i+1,n):
#             third=-(nums[i]+nums[j])
#             if(third in myset):
#                 temp=[nums[i],nums[j],third]
#                 temp.sort()
#                 resultset.add(tuple(temp))
#             myset.add(nums[j])
#     return [list(ans) for ans in resultset]

# result=threesum(nums)
# print(result)

                
#Optimal Solution
def threeSum(nums):
    ans=[]
    n=len(nums)
    nums.sort()
    for i in range(0,n):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        j=i+1
        k=n-1
        while(j<k):
            totalsum=nums[i]+nums[j]+nums[k]
            if(totalsum<0):
                j+=1
            elif(totalsum>0):
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1
    return ans
    
result=threeSum(nums)
print(result)