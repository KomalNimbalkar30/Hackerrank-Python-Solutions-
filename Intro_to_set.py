def average(array):
    # your code goes here
    array=set(array)
    n= len(array)
    sum1=0
    sum1=sum(array)
    return(sum1/n)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
