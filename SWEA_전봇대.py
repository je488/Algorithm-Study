import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list()
    res = 0
    for i in range(n):
        a, b = map(int, input().split())
        li.append([a, b])
    for j in range(n):
        for k in range(j+1, n):
            a1, b1 = li[j]
            a2, b2 = li[k]
            if (a1-a2) * (b1-b2) < 0:
                res += 1
    print(f'#{tc} {res}')
