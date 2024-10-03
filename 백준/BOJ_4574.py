#go(z)는 z번째 칸을 채우는 함수
#z는 row-major order로 번호를 매김 -> (x, y)의 경우, z = 9*x + y
#z로는 문제를 풀기 어려우므로 z를 x행 y열로 바꿔주기
#c[i][j]는 i행에 숫자 j가 있으면 True, c2[i][j]는 i열에 숫자 j가 있으면 True
#c3[i][j]는 i번째 작은 정사각형에 숫자 j가 있으면 True
#domino는 도미노의 중복 사용 여부를 체크하는 리스트
#스도쿠와 달리 스도미노쿠는 z번째 칸의 오른쪽 또는 아래에도 수를 넣어야 하므로 dx, dy 필요
#convert(s)는 s를 x행 y열의 형태로 바꿔주는 함수
#square(x, y)는 (x, y)가 몇 번째 작은 정사각형에 속해있는지 구해주는 함수
#can(x, y)는 x행 y열에 num이 올 수 있는지 검사하는 함수(c, c2, c3 이용)
#check(x, y, num, what)은 x행 y열에 what의 값에 따라 num을 놓거나 놓지 않음을 표시해주는 함수
#check_range(x, y)는 x행 y열이 보드의 범위를 벗어나는지 검사하는 함수
#(nx, ny)는 현재 칸(x, y)을 기준으로 오른쪽 또는 아래 칸
#(nx, ny)가 보드의 범위를 벗어나거나 (nx, ny)칸에 숫자가 이미 있으면 continue
#1 ~ 9까지 이중 for문을 이용하여 도미노 만들기
#i == j이거나 domino[i][j] 값이 True이면(이미 그 도미노를 사용한 경우) continue
#can을 이용하여 (x, y)칸에 i, (nx, ny)칸에 j가 올 수 있는지 검사
#올 수 있으면 check를 이용하여 도미노를 놓고 domino와 a의 값을 바꾼 후(준비) go 함수 호출
#함수를 호출한 뒤에는 check를 이용하여 도미노를 삭제하고 domino와 a의 값 원래대로 바꾸기(복원)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = 9
dx = [0, 1]
dy = [1, 0]
def convert(s):
    return (ord(s[0]) - ord('A'), ord(s[1]) - ord('1'))

def square(x, y):
    return (x // 3) * 3 + (y // 3)

def can(x, y, num):
    return not c[x][num] and not c2[y][num] and not c3[square(x, y)][num]

def check(x, y, num, what):
    c[x][num] = what
    c2[y][num] = what
    c3[square(x, y)][num] = what

def check_range(x, y):
    return 0 <= x < n and 0 <= y < n

def go(z):
    if z == 81:
        for i in range(n):
            print(''.join(map(str, a[i])))
        return True
    x = z // n
    y = z % n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for d in range(2):
            nx, ny = x + dx[d], y + dy[d]
            if not check_range(nx, ny):
                continue
            if a[nx][ny] != 0:
                continue
            for i in range(1, 10):
                for j in range(1, 10):
                    if i == j:
                        continue
                    if domino[i][j]:
                        continue
                    if can(x, y, i) and can(nx, ny, j):
                        check(x, y, i, True)
                        check(nx, ny, j, True)
                        domino[i][j] = domino[j][i] = True
                        a[x][y] = i
                        a[nx][ny] = j
                        if go(z+1):
                            return True
                        check(x, y, i, False)
                        check(nx, ny, j, False)
                        domino[i][j] = domino[j][i] = False
                        a[x][y] = 0
                        a[nx][ny] = 0
    return False

tc = 1
while True:
    c = [[False] * 10 for _ in range(10)]
    c2 = [[False] * 10 for _ in range(10)]
    c3 = [[False] * 10 for _ in range(10)]
    domino = [[False] * 10 for _ in range(10)]
    a = [[0] * 9 for _ in range(9)]
    m = int(input())
    if m == 0:
        break
    for i in range(m):
        n1, s1, n2, s2 = input().split()
        n1 = int(n1)
        n2 = int(n2)
        x1, y1 = convert(s1)
        x2, y2 = convert(s2)
        a[x1][y1] = n1
        a[x2][y2] = n2
        domino[n1][n2] = domino[n2][n1] = True
        check(x1, y1, n1, True)
        check(x2, y2, n2, True)
    tmp = input().split()
    for i in range(1, 10):
        s = tmp[i-1]
        x, y = convert(s)
        a[x][y] = i
        check(x, y, i, True)
    print(f'Puzzle {tc}')
    go(0)
    tc += 1
