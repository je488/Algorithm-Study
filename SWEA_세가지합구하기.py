import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
res = list()
for tc in range(1, T+1):
    n = int(input())
    s1 = n * (n+1) // 2
    s2 = n * n
    s3 = n * (n+1)
    res.append(f'#{tc} {s1} {s2} {s3}')
for r in res:
    print(r)
