cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    c = [0,1]
    for i in range(2,n):
        c.append(c[i-2] + c[i-1])
    return(c[0:n])
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
