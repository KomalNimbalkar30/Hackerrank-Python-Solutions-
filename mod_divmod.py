# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=int(input())
print(n//m, n%m, divmod(n,m), sep="\n")
