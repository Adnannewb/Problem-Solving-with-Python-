num=int(input("Enter number to check palindrome: "))
n=num
result=0
while(n>0):
    ld=n%10
    result=result*10 +ld  #it is also a reverse number 
    n=n//10
if(num==result):
    print("YES , It's a Palindrome.") 
else:
    print("It's not a Palindrome.")       