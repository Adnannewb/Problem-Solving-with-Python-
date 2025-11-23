from math import *
num=int(input("Enter number to count digits: "))
n=num
# count=0
# while(n>0):
#     count+=1
#     n=n//10
# print(f"There are {count} digits in the number.")    

#  -----using logarithmic formula ------
count=int(log10(n)+1)
print(f"There are {count} digits in the number.") 