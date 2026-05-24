from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])

all_combinations = product(*lists)

maximum = 0

for combination in all_combinations:
    final_result = sum(x**2 for x in combination) % M
    
    if final_result > maximum:
        maximum = final_result

print(maximum)