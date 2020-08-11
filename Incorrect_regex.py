# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    op=True
    try:
        ip=re.compile(input())
    except re.error:
        op=False
    print(op)
