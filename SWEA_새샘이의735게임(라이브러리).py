import sys
from itertools import combinations
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = list()
T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    res = set()
    for c in combinations(li, 3):
        res.add(sum(c))
    res = sorted(res, reverse=True)
    ans.append(f'#{tc} {res[4]}')
for a in ans:
    print(a)
