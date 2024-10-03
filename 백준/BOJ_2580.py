#go(z)는 z번째 칸을 채우는 함수
#z는 row-major order로 번호를 매김 -> (x, y)의 경우, z = 9*x + y
#z로는 문제를 풀기 어려우므로 z를 x행 y열로 바꿔주기
#c[i][j]는 i행에 숫자 j가 있으면 True, c2[i][j]는 i열에 숫자 j가 있으면 True
#c3[i][j]는 i번째 작은 정사각형에 숫자 j가 있으면 True
#square(x, y)는 (x, y)가 몇 번째 작은 정사각형에 속해있는지 구해주는 함수
#a를 탐색하며 이미 숫자가 있으면 새로 숫자를 놓을 수 없게 c, c2, c3의 값을 True로 바꾸기
#z == 81이면 정답을 찾은 경우로 a 출력, z가 81이 아니면 다음 경우
#다음 경우에서 a가 0이면 1 ~ 9까지 검사해서 숫자 놓기, 수가 있으면 아무것도 안하고 넘어가기
#숫자를 놓을 때 c, c2, c3, a의 값을 바꾸고(준비) go 함수 호출
#함수를 호출한 뒤에는 c, c2, c3, a의 값을 원래대로 바꿔주기(복원)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def square(x, y):
    return (x // 3) * 3 + (y // 3)

def go(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // n
    y = z % n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = False
                a[x][y] = 0
    return False

n = 9
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * 10 for _ in range(n)]
c2 = [[False] * 10 for _ in range(n)]
c3 = [[False] * 10 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i, j)][a[i][j]] = True
go(0)
