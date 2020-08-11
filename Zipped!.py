# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
lst_marks=[]
for i in range(m):
    lst_marks+=[map(float,input().split())]

for i in zip(*lst_marks):
    print(sum(i)/m)

