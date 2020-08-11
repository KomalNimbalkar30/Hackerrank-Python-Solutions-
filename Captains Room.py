'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

mlist=list(map(int,input().split()))

for elem in mlist:
    if m.count(elem)<=1:
        print(elem)

'''

K = int(input())
set_S = set()
sumlist_S = 0
for i in input().split():
    I = int(i)
    set_S.add(I)
    sumlist_S += I

print((sum(set_S)*K - sumlist_S)//(K-1))
