'''n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in sc_ar]))'''
count=list(map(int,input().strip().split()))

arr=list(map(int,input().strip().split()))
array1= set(map(int,input().strip().split()))
array2= set(map(int,input().strip().split()))
points=0

for i in arr:
    if i in array1:
        points=points+1
    elif i in array2:
        points=points-1

print(points)
