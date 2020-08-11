# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=int(input())
s1=set(input().split())
n2=int(input())
s2=set(input().split())

s=set()
s=len(s1.symmetric_difference(s2))#a^b The roll numbers of students who have subscriptions to English or French newspapers but not both are:
print(s)
