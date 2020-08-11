n,m = map(int, input().split())
rows = [input() for _ in range(n)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)
