from collections import defaultdict
n,m=map(int,input().split())
A=[]
B=[]
for _ in range(n):
    A.append(input())
for _ in range(n):
    B.append(input())
positions = defaultdict(list)
for idx,word in enumerate(A,start=1):
    positions[word].append(idx)

for word in B:
    if positions[word]:
        print(" ".join(map(str,positions[word])))
    else:
        print('-1')
        
