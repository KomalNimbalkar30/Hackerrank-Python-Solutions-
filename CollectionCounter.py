# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


no=int(input())
lst=Counter(list(map(int,input().split())))

n=int(input())

a=[tuple(map(int,input().split()))for i in range(n)]

earning=0

for i in a:
    if i[0] in lst:
        if lst[i[0]] >0:
            earning+=i[1]
    lst[i[0]]-=1

print(earning)
