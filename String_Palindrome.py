s=input("Enter your string to check palindrome: ").strip()

# def palindrome(s,left,right):
#     while(left<right):                #Using LOOP
#         if(s[left]!=s[right]):         
#             return False
#         else:
#             left+=1  
#             right-=1
#         return True
# result=palindrome(s,0,len(s)-1)
# if(result):
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")            



def palindrome(s,left,right):
    if(left>=right):
        return True
    if(s[left]!=s[right]):
        return False
    return palindrome(s,left+1,right-1)    #Using Recursion 

result=palindrome(s,0,len(s)-1)
if(result):
    print("PALINDROME")
else:
    print("NOT PALINDROME")  