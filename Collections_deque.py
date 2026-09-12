from collections import deque
d=deque()
op_list={}
n=int(input())
for _ in range(n):
    parts=input().split()
    op=parts[0]
    if op=="append":
        d.append(parts[1])
    elif(op=="appendleft"):
        d.appendleft(parts[1])
    elif(op=="pop"):
        d.pop()
    elif(op=="popleft"):
        d.popleft()

print(*d)
    