n1=int(input())
s1=set(input().split())
n2=int(input())
s2=set(input().split())

s=set()
s=len(s1.intersection(s2))
print(s, (s1.intersection(s2)))
