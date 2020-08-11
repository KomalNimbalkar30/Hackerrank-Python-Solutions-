n = int(input())
s = set(map(int, input().split()))
op_no=int(input())

for _ in range(op_no):

    a = list(input().strip().split())
    #print(a) to understand operations

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print (sum(s))    
