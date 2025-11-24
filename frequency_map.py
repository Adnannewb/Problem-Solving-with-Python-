nums=[5,6,7,7,1,9,111,1,1,5,1,1]
freq_map=dict()
# for i in range(len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#     else:
#         freq_map[nums[i]]=1
# x=int(input("Which number frequency you wannna check :"))
# print(freq_map[x])            

#Better code 
for i in range(len(nums)):
    freq_map[nums[i]]=freq_map.get(nums[i],0)+1
x=int(input("Which number frequency you wannna check :"))
print(freq_map[x]) 