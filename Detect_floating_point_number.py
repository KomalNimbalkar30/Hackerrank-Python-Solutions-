# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input().strip())
for _ in range(n):
    ans=False
    try:
        string=input().strip()
        number=float(string)
        ans=True
        number=int(string)
        ans=False
    except:
        pass
    print(ans)
