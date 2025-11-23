from math import sqrt
num=int(input("Enter number to see it's factors: "))
n=num
result=[]

#Brute force solution 
# for i in range(1,num+1):
#     if(num%i==0):
#         result.append(i)
# print(result)

#Better solution 
# for i in range(1,num//2+1):
#     if(num%i==0):
#         result.append(i)
# result.append(num)        
# print(result)

#Optimal Solution 
for i in range(1,int(sqrt(n))+1):
    if(num%i==0):
        result.append(i)
        if(n//i !=i):
            result.append(n//i)
result.sort()
print(result)            
            