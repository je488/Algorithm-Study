#n개의 이모티콘을 만드는 데 걸리는 시간의 최솟값을 구하는 문제이므로 BFS 이용
#클립보드의 이모티콘 개수에 따라 클립보드에서 복사하기 연산의 결과가 다름
#화면의 이모티콘 개수(s)와 클립보드의 이모티콘 개수(c)가 중요 -> 정점 (s, c)
#2 <= s <= 1000이므로 s, c를 각각 1000이라고 가정하면 정점의 개수는 100만개 -> BFS로 해결 가능
#복사하는 경우 : (s, c) -> (s, s)
#붙여넣기하는 경우 : (s, c) -> (s+c, c)
#삭제하는 경우 : (s, c) -> (s-1, c)
#sec[s][c] : 화면의 이모티콘 개수와 클립보드의 이모티콘 개수가 s, c가 되기 위해 걸리는 최소 시간
#초는 음수가 될 수 없으므로 sec값이 -1이면 방문X, 0 이상이면 방문했고 그 때 걸리는 최소 시간
#s가 n이면서 sec값이 -1이 아닌 최솟값을 찾아 출력
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
sec = [[-1] * (n+1) for _ in range(n+1)]
Q = deque()
Q.append((1, 0))
sec[1][0] = 0
while Q:
    s, c = Q.popleft()
    if sec[s][s] == -1:
        sec[s][s] = sec[s][c] + 1
        Q.append((s, s))
    if s+c <= n and sec[s+c][c] == -1:
        sec[s+c][c] = sec[s][c] + 1
        Q.append((s+c, c))
    if s-1 >= 0 and sec[s-1][c] == -1:
        sec[s-1][c] = sec[s][c] + 1
        Q.append((s-1, c))
ans = -1
for i in range(n+1):
    if sec[n][i] != -1:
        if ans == -1 or ans > sec[n][i]:
            ans = sec[n][i]
print(ans)
