from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))

lst=list(product(a,b))
for i in lst:
    print(i, end=' ')
