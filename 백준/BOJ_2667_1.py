import sys
from functools import reduce
from collections import Counter
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def DFS(x, y, cnt):
    group[x][y] = cnt
    for d in range(4):
        xx, yy = x + dx[d], y + dy[d]
        if 0 <= xx < n and 0 <= yy < n:
            if a[xx][yy] == 1 and group[xx][yy] == 0:
                DFS(xx, yy, cnt)

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]
group = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            DFS(i, j, cnt)

ans = reduce(lambda x, y : x+y, group)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str, ans)))