# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

ele,size= input().split()
size=int(size)


lst=(list(permutations(sorted(ele),2)))

for i in lst:
    print(''.join(i))
