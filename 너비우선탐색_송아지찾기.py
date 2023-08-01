#BFS(너비우선탐색) : 레벨 탐색(0레벨 -> 1레벨 -> 2레벨 -> ...), 큐 이용
#큐에 루트 노드 넣기 -> popleft() -> 루트 노드와 간선 하나로 연결된 노드들 모두 큐에 넣기(탐색)
#popleft() -> 나온 노드와 간선 하나로 연결된 노드들 큐에 넣기 -> 반복
#앞으로 1, 뒤로 1, 앞으로 5로 이동할 수 있으므로 3개의 가지로 뻗어나감
#dis의 인덱스가 좌표 지점, dis의 값은 좌표 지점까지 몇 번만에 갈 수 있는지 점프횟수를 담은 리스트
#ch는 이미 방문한 좌표를 다시 방문하지 않기 위해 방문여부를 체크하는 리스트
#큐에 노드(next)를 넣을 때 popleft()로 나온 now 즉, 부모의 dis값에 +1해서 dis[next]에 저장
#출발점에서 부모 노드까지 점프하는 횟수 + 1 -> 출발점에서 자식 노드까지 점프하는 횟수
#큐에서 처음으로 e(도착점)값이 나오면 break해서 반복문 탈출 -> dis[e]가 정답
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
s, e = map(int, input().split())
dQ = deque()
dQ.append(s)
dis[s] = 0
ch[s] = 1
while dQ:
    now = dQ.popleft()
    if now == e:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[e])
