n1 = int(input())
arr1 = set(list(map(int, input().split())))
n2 = int(input())
arr2 = set(list(map(int,input().split())))

result1 = arr1.difference(arr2)
result2 = arr2.difference(arr1)
result1=set(result1)
result2=set(result2)
result = result1.union(result2)
result=sorted(result)
for i in result:
    print(i)
