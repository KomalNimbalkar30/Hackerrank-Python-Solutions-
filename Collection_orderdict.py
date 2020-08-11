from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
  *item, price = input().split()
  item = ' '.join(item)
  od.setdefault(item, 0)
  od[item] = od[item] + int(price)
for k,v in od.items():
  print(k , v)


  
'''
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

'''
