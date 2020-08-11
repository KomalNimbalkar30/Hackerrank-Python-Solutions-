# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range (n):
    lst=(input().split())
    try:
        print(int(lst[0])//int(lst[1]))
    except ZeroDivisionError as e:
        print("Error Code: integer division or module by zero")
    except ValueError as e:
        print("Error code: invalid literal for int() with base 10: '$' ")

"---------------------------------------------"
'''
for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

'''

"---------------------------------------------"

'''
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as e:
        print("Error Code:", e)
'''
