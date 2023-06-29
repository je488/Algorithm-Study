import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] <= m:
        weight.popleft()
        weight.pop()
        cnt += 1
    else:
        weight.pop()
        cnt += 1
print(cnt)
