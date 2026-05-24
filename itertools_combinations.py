from itertools import combinations
string,k=input().split()
string=sorted(string.upper().strip())
k=int(k)
final_combinations=[]

for i in range(1, k + 1):
    final_combinations+=list(combinations(string,i))
    i+=1
for element in final_combinations:
    print("".join(element))
    