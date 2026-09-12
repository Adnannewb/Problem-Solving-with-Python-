
t=int(input())
for _ in range(t):
    
    flag=True
    n=int(input())
    arr=list(map(int,input().split()))
    new_arr=[]
    i=0
    j=n-1
    last_num=float('inf')
    while(i<=j):
        if(arr[i]>last_num or arr[j]>last_num):
            flag=False
            break
        else:
            if(arr[i]>=arr[j]):
                new_arr.append(arr[i])
                last_num=arr[i]
                i+=1
            else:
                new_arr.append(arr[j])
                last_num=arr[j]
                j-=1
    
    if flag:
        print("Yes")
    else:
        print("No")

