# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

ele, size=input().split()
lst=combinations_with_replacement(sorted(ele),int(size))
for i in lst:
    print(''.join(i))
