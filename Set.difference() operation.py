# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
s1=set(input().split())
n2=int(input())
s2=set(input().split())

s=set()
s=len(s1.difference(s2))
print(s)
