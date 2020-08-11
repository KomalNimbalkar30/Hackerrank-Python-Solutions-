import sys
n=int(sys.stdin.readline())
l=[]
for i in range(n):
    a=sys.stdin.readline().strip().split()
    for i in range(len(a)):
        b=int(a[i])
        l.append(b)


print(min(l))

