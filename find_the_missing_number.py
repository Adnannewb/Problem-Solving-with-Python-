nums=[9,6,4,2,3,5,7,0,1]

#Brute force solution 

# def missingnumber(nums):
#     n=len(nums)
#     for i in range(0,n+1):
#         if(i not in nums):
#             return i
# print(missingnumber(nums))

#Better solution
# def missingnumber(nums):
#     n=len(nums)
#     freq={}
#     for i in range(0,n):
#         freq[i]=0
#     for num in nums:
#         freq[num]=1
#     for k,v in freq.items():
#         if(v==0):
#             return k
# print(missingnumber(nums))

#Optimal Solution
def missingnumber(nums):
    n=len(nums)
    Totalsum=(n*(n+1))/2
    # print(Totalsum)
    return int(Totalsum-sum(nums))
print(missingnumber(nums))