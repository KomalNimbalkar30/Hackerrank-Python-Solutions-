# Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
k=input()

import re
pattern = re.compile(k)

r = pattern.search(S)
if not r: print ("(-1, -1)")
while r:
    #print(r.start(), r.end())
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)
