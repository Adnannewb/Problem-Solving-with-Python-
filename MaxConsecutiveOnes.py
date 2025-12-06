nums=[1,1,0,1,0,1,1,1,1,0,1,1,1]
maxones=0
n=len(nums)
count=0
for i in range(0,n):
    if(nums[i]==1):
        count+=1
    else:
        maxones=max(count,maxones)
        count=0
    if(i==n-1):
        maxones=max(count,maxones)
        
print(maxones)