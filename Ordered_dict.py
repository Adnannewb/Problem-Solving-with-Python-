from collections import OrderedDict

n = int(input())
item_list = OrderedDict()

for _ in range(n):
    item_name, net_price = input().rsplit(" ", 1)
    net_price = int(net_price)
    item_list[item_name] = item_list.get(item_name, 0) + net_price

for item_name, net_price in item_list.items():
    print(item_name, net_price)