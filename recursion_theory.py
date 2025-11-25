#Q1: Print Anirudh 4 times 

#Head Recursion
# count=0
# def function():
#     global count
#     if (count==4):
#         return
#     print("Anirudh")
#     count+=1
#     function()

# function()
#without count using parameters
# def func(x,n):
#     if(n==0):
#         return
#     print(x)
#     func(x,n-1)
# func(15,4)    
    

#Tail Recursion
# count=0
# def function():
#     global count
#     if (count==4):
#         return
#     print("Anirudh")
#     count+=1
#     function()
# function()    


#Q2.Print 1 to n 

# def func(i,n):
#     if(i==n+1):
#         return
#     print(i)     #HEAD
#     func(i+1,n)
# func(1,5)    

# def func(i,n):
#     if(i==0):
#         return
#     func(i-1,n)
#     print(i)     #TAIL
# func(5,5)    

#Q3.1 to n  sum 

# def func(sum,i,n):
#     if(i>n):
#         print(sum)
#         return
#     func(sum+i,i+1,n)   #Parametarized Recursion 
# func(0,1,4)    

# def func(n):
#     if(n==1):
#         return 1
#     return n+func(n-1)
# sum=func(4)   #Functional Recursion
# print(sum)
    
    
#Q4.Factorial of number n 

# def func(n):
#     if(n==1):
#         return 1
#     return n*func(n-1)
# factorial=func(6)
# print(factorial)

#Q5. Reverse an array between 2 to 5 index . 
nums=[2,4,1,7,6,3,8,9,5] #reverse only 2 to 5 index

def reverselist(nums,left,right):
    if(left>=right):
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverselist(nums,left+1,right-1)
reverselist(nums,2,5)
print(nums)    

#using loop 
left,right=2,5
while(left<right):
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)    
    