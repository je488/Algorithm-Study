#격자판의 정중앙을 기준으로 상하좌우(시계방향) 탐색 -> 4개의 가지로 뻗어나감
#dx, dy는 격자판(li)에서 위, 오른쪽, 아래, 왼쪽을 탐색하기 위한 행과 열의 인덱스 증가치
#ch는 이미 더한 li의 값을 중복해서 더하지 않기 위해 방문여부를 체크하는 리스트
#L은 레벨로 n//2와 같아지면 반복문 탈출
#Q의 길이만큼 반복하고 Q에서 popleft()로 값이 나올 때마다 4번 반복(상하좌우)
#상하좌우로 탐색한 좌표를 이전에 방문하지 않았을 때만 res에 값 누적
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
res = 0
Q = deque()
ch[n//2][n//2] = 1
res += li[n//2][n//2]
Q.append((n//2, n//2))
L = 0
while True:
    if L == n // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                res += li[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(res)
