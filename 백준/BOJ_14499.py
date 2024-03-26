#dice는 주사위의 6면에 있는 값을 저장
#dx, dy는 순서대로 동, 서, 북, 남으로 이동하기 위한 행과 열의 증가치
#문제에서는 1 ~ 4로 명령을 주지만 코드에서는 dx, dy의 인덱스가 0부터 시작하므로 k에서 1 빼기
#k방향으로 굴렸을 때 지도의 바깥이면 continue로 해당 명령 무시
#지도의 범위 안이면 방향에 따라 주사위 면의 값이 어떻게 바뀌는 지 구하고 주사위 이동시키기
#주사위를 이동시키고 이동한 칸에 써있는 수에 따라 지도의 칸과 주사위 면의 값 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))
dice = [0] * 7
for k in move:
    k -= 1
    nx, ny = x + dx[k], y + dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if k == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    elif k == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    elif k == 2:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    else:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
    x, y = nx, ny
    if a[x][y] == 0:
        a[x][y] = dice[6]
    else:
        dice[6] = a[x][y]
        a[x][y] = 0
    print(dice[1])
