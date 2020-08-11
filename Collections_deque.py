# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n=int(input())
d = deque()

for _ in range(n):
    s=input().split()
    if s[0]=='append':
        d.append(s[1])
    elif s[0]=='appendleft':
        d.appendleft(s[1])
    elif s[0]=='pop':
        d.pop()
    elif s[0]=='popleft':
        d.popleft()
    elif s[0]=='extend':
        d.extend(s[1])
    elif s[0]=='remove':
        d.remove(s[1])
    elif s[0]=='reverse':
        d.reverse()
    elif s[0]=='rotate':
        d.rotate(s[1])


for i in d:
    print(i,end=' ')
