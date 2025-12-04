nums=[5,3,9,8,1,4,6,-1,100]
target=int(input("Enter the value you want to search: "))
for i in range(0,len(nums)):
    if(nums[i]==target):
        print(i+1)