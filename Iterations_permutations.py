from itertools import permutations
string,k=input().split()
string=string.upper().strip()
k=int(k)
final_permutations=list(permutations(string,k))
final_permutations=sorted(final_permutations)
for element in final_permutations:
    print("".join(element))