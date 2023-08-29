import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = list()
T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    res = set()
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                res.add(li[i]+li[j]+li[k])
    res = sorted(res, reverse=True)
    ans.append(f'#{tc} {res[4]}')
for a in ans:
    print(a)

