nums=[1,0,-1,0,-2,2]


#Brute force solution
# def fourSum(nums):
#     target=0
#     n=len(nums)
#     resultset=set()
#     for i in range(0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     if(nums[i]+nums[j]+nums[k]+nums[l]==target):
#                         temp=[nums[i],nums[j],nums[k],nums[l]]
#                         temp.sort()
#                         resultset.add(tuple(temp))
#     return [list(ans) for ans in resultset]

# result=fourSum(nums)
# print(result)


#Better Solution
# def foursum(nums):
    
#     target=0
#     n=len(nums)
#     resultset=set()
#     for i in range(0,n):
#         myset=set()
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 fourth=-(nums[i]+nums[j]+nums[k])
#                 if(fourth in myset):
#                     temp=[nums[i],nums[j],nums[k],fourth]
#                     temp.sort()
#                     resultset.add(tuple(temp))
#                 myset.add(nums[k])
#     return [list(ans) for ans in resultset]

# result=foursum(nums)
# print(result)

                
#Optimal Solution
def fourSum(nums):
    target=0
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

    return ans
    
result=fourSum(nums)
print(result)