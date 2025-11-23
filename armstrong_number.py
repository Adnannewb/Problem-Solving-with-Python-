num=input("Enter number to check Armstrong Number: ")
n=int(num)
digit=len(num)
result=0
while(n>0):
    ld=n%10
    result=result+ ld**digit
    n=n//10

if(int(num)==result):
    print("YES , It's an Armstrong number.") 
else:
    print("It's not an Armstrong number.")     