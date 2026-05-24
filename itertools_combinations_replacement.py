from itertools import combinations_with_replacement
string,k=input().split()
string=sorted(string.upper().strip())
k=int(k)
final_combinations=[]

for i in range(2, k + 1):
    final_combinations+=list(combinations_with_replacement(string,i))
    i+=1
for item in final_combinations:
    print(''.join(item))
    
    