#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc(문제링크)
#dir_cmd, dir_shape는 위, 아래, 왼쪽, 오른쪽을 나타내는 방향 명령과 방향 모양 리스트
#dx, dy는 위, 아래, 왼쪽, 오른쪽으로 이동하기 위한 행과 열의 증가치
#인덱스로 dir_cmd, dir_shape, dx, dy에 접근할 수 있도록 순서를 위, 아래, 왼쪽, 오른쪽으로 통일
#게임 맵(a)에서 전차를 찾아 전차의 위치를 x, y에 저장하고 전차의 현재 방향을 d에 저장
#포탄을 발사할 때 전차는 움직이지 않고 포탄만 발사해야 하므로 포탄의 좌표를 따로 생성 -> bx, by
#전차의 방향에 따라 포탄이 이동하므로 전차의 방향을 나타내는 인덱스를 찾아 b_idx에 저장
#b_idx를 바탕으로 포탄이 전차의 방향으로 이동하기 위한 행과 열의 증가치를 bdx, bdy에 저장
#포탄은 강철이나 벽돌에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진
#따라서 while문을 이용하여 게임 맵을 벗어날 때까지 포탄이 이동하고 강철이나 벽에 충돌 시 break
#입력이 S가 아닌 경우 전차가 이동해야 하므로 입력받은 방향을 나타내는 인덱스를 찾아 m_idx에 저장
#m_idx를 바탕으로 전차가 입력받은 방향으로 이동하기 위한 행과 열의 증가치를 mdx, mdy에 저장
#(x+mdx, y+mdy)는 이동해야 하는 좌표로 게임 맵을 벗어나지 않고 평지이면 이동
#(x+mdx, y+mdy)로 이동 시 현재 위치를 평지로 바꾸고 전차의 위치 변경
#이동할 수 없는 경우 현재 위치에서 전차의 방향만 바꿔주기
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
