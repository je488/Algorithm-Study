import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    li = list()
    res = ''
    for _ in range(5):
        s = input().rstrip()
        li.append(s)
    for i in range(15):
        for j in range(5):
            if i < len(li[j]):
                res += li[j][i]
    print(f'#{tc} {res}')
