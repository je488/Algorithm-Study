import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    info = input().rstrip()
    cnt = 0
    res = 0
    for i in range(len(info)):
        if cnt >= i:
            cnt += int(info[i])
        else:
            res += (i - cnt)
            cnt += (int(info[i]) + i - cnt)
    print(f'#{tc} {res}')
