nums=[6,9,1,2,4,15,6,3]
target=13
n=len(nums)

#bruteforce

# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if(nums[i]+nums[j])==target:
#             print([i,j])
#             break
        
#Optimal Solution
hashmap=dict()
for i in range(0,n):
    remaining=target-nums[i]
    if(remaining in hashmap):
        print([hashmap[remaining],i])
        break
    else:
        hashmap[nums[i]]=i    