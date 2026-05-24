from itertools import product

list1=[int(i)for i in input().split(" ")]
list2=[int(i)for i in input().split(" ")]
cartesian_product=list(product(list1,list2))

for element in cartesian_product:
    print(element,end="")