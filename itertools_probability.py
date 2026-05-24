from itertools import combinations
n=int(input())
s=list(input().split())
k=int(input())
desired=0
final_list=list(combinations(s,k))
for item in final_list:
    if('a' in item):
        desired+=1

probability=desired/len(final_list)
print(f"{probability:.4f}")


