#이것이 취업을 위한 코딩테스트다 - 120p
#dx, dy는 위(북), 오른쪽(동), 아래(남), 왼쪽(서)로 이동하기 위한 행과 열의 증가치
#ch는 중복으로 방문하지 않기 위해 방문 여부를 체크하는 리스트
#turn은 네 방향을 모두 탐색했는지 확인하는 변수로 이동하지 않고 회전할 때마다 1증가
#turn_left() 함수를 이용하여 왼쪽으로 회전
#북, 동, 남, 서가 순서대로 0, 1, 2, 3이므로 왼쪽으로 회전할 때마다 d -= 1(d가 -1이면 3)
#바라보는 방향에 따라 dx, dy를 더해 이동할 좌표 a, b 구하기
#a, b가 이전에 방문한 적이 없고 육지인 경우 이동하고 그렇지 않으면 다시 왼쪽으로 회전
#turn이 4가 되어 네 방향 모두 갈 수 없는 경우 뒤로 이동(현재 방향에 해당하는 dx, dy 빼기)
#뒤가 바다로 막혀있어 이동할 수 없으면 break(이동 종료)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch[x][y] = 1
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
res = 1
turn = 0
while True:
    turn_left()
    a = x + dx[d]
    b = y + dy[d]
    if ch[a][b] == 0 and map[a][b] == 0:
        ch[a][b] = 1
        x, y = a, b
        res += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        a = x - dx[d]
        b = y - dy[x]
        if map[a][b] == 0:
            x, y = a, b
        else:
            break
        turn = 0
print(res)
