#dx, dy는 오른쪽, 아래, 왼쪽, 위로 이동하기 위한 행과 열의 증가치
#보드를 탐색하며 동전 2개의 현재 위치를 찾아 x1, y1, x2, y2에 저장
#2개의 동전이 위치한 칸(a[i][j])을 빈칸으로 바꿔주기
#x1, y1, x2, y2를 통해 동전의 이동을 알 수 있으므로 a[i][j]칸이 동전이라는 정보는 더이상 의미X
#또한 동전은 오직 빈칸으로만 이동이 가능하므로 동전이 사라지면 빈칸
#step은 버튼을 누른 횟수로 10보다 커지면 -1을 출력해야 하므로 step이 11이 되면 -1 리턴
#x1, y1, x2, y2를 바탕으로 동전이 바깥으로 떨어진 경우 fall1, fall2의 값을 True로 바꿔주기
#fall1, fall2가 모두 True이면 동전 2개가 모두 떨어진 경우이므로 -1 리턴
#fall1, fall2 중 하나만 True이면 현재까지 버튼을 누른 횟수(step) 리턴
#2개의 동전이 각각 (nx1, ny1), (nx2, ny2)로 이동했을 때 이동한 칸이 벽이면 이동 취소
#따라서 이동한 좌표(nx1, ny1, nx2, ny2)를 원래 동전이 있던 좌표(x1, y1, x2, y2)로 다시 이동
#tmp가 -1이면 ans와 비교하지 않고 continue(가능한 경우 중 최소값을 찾아야 하므로)
#ans가 -1이면 최솟값이 없는 경우로 ans가 -1이거나 tmp보다 큰 경우 ans = tmp
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def go(step, x1, y1, x2, y2):
    if step == 11:
        return -1
    fall1 = fall2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans = -1
    for d in range(4):
        nx1, ny1 = x1 + dx[d], y1 + dy[d]
        nx2, ny2 = x2 + dx[d], y2 + dy[d]
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        tmp = go(step+1, nx1, ny1, nx2, ny2)
        if tmp == -1:
            continue
        if ans == -1 or ans > tmp:
            ans = tmp
    return ans

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
x1 = y1 = x2 = y2 = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            a[i][j] = '.'
print(go(0, x1, y1, x2, y2))
