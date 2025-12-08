nums=[1,99,101,98,2,5,3,100,1,1]

#Brute Force
# def Longest(nums):
#     n=len(nums)
#     max_count=0
#     for i in range(0,n):
#         num=nums[i]
#         count=1
#         while(num+1 in nums):
#             count+=1
#             num+=1
#         max_count=max(max_count,count)
#     return max_count
# print(Longest(nums))

#Better Solution

# def longest(nums):
#     nums.sort()
#     n=len(nums)
#     last_smaller=float("-inf")
#     mostlong=0
#     count=0
#     for i in range(0,n):
#         num=nums[i]
#         if(num-1==last_smaller):
#             count+=1
#             last_smaller=num
#         elif(nums !=last_smaller):
#             count=1
#             last_smaller=num
#     mostlong=max(mostlong,count)
#     return mostlong

# print(longest(nums))

#Optimal Solution

def longestseq(nums):
    setnums=set(nums)
    print(setnums)
    n=len(setnums)
    longest=0
    for num in setnums:
        if(num-1 not in setnums):
            x=num
            count=1
            while(num+1 in setnums):
                count+=1
                num+=1
            longest=max(longest,count)
    return longest
print(longestseq(nums))
    