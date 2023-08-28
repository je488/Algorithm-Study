import sys
from collections import defaultdict
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    line = defaultdict(set)
    res = 0
    for _ in range(m):
        x, y = map(int, input().split())
        line[x].add(y)
        line[y].add(x)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i in line[j] and j in line[k] and k in line[i]:
                    res += 1
    print(f'#{tc} {res}')
