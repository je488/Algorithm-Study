import sys
import math
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
res = []
for tc in range(1, T+1):
    n = int(input())
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        d = math.ceil(math.sqrt(x*x + y*y) / 20)
        if d == 0:
            score += 10
        elif d <= 11:
            score += (11 - d)
    res.append(f'#{tc} {score}')
for r in res:
    print(r)
