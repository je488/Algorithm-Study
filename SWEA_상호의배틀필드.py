import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dir_cmd = ['U', 'D', 'L', 'R']
dir_shape = ['^', 'v', '<', '>']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    n = int(input())
    cmd = list(input().rstrip())
    for i in range(h):
        for j in range(w):
            if a[i][j] in dir_shape:
                x, y = i, j
                d = a[i][j]
    for c in cmd:
        if c == 'S':
            b_idx = dir_shape.index(d)
            bdx, bdy = dx[b_idx], dy[b_idx]
            bx, by = x, y
            while 0 <= bx < h and 0 <= by < w:
                if a[bx][by] == '#':
                    break
                if a[bx][by] == '*':
                    a[bx][by] = '.'
                    break
                bx += bdx
                by += bdy
        else:
            m_idx = dir_cmd.index(c)
            mdx, mdy = dx[m_idx], dy[m_idx]
            d = dir_shape[m_idx]
            if 0 <= x + mdx < h and 0 <= y + mdy < w and a[x+mdx][y+mdy] == '.':
                a[x][y] = '.'
                x += mdx
                y += mdy
            a[x][y] = d
    print(f'#{tc}', end=' ')
    for i in a:
        print(*i, sep='')