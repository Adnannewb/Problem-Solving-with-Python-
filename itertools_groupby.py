from itertools import groupby
string=input().upper()

for key, group in groupby(string):
    print(f"({len(list(group))}, {key})",end=" ")
