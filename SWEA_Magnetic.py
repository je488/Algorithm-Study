import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        flag = False
        for j in range(n):
            if board[j][i] == 1:
                flag = True
            elif board[j][i] == 2:
                if flag:
                    res += 1
                    flag = False
    print(f'#{tc} {res}')