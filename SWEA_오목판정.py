import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def isFive(li):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if li[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    r = i + dr[k]
                    c = j + dc[k]
                    while 0 <= r < n and 0 <= c < n and li[r][c] == 'o':
                        cnt += 1
                        r += dr[k]
                        c += dc[k]
                        if cnt == 5:
                            return 'YES'
    return 'NO'
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    print(li)
    print(f'#{tc} {isFive(li)}')
