#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY(문제링크)
#ch는 주차공간에 주차가 되어있는지 체크하기 위한 리스트(주차가 되어있지 않다면 값이 0)
#wait은 주차공간이 없을 경우 순서대로 대기하기 위한 리스트
#order는 차량번호 및 출입 정보 리스트(양수면 주차, 음수면 출차, 절댓값은 차량번호)
#tmp가 양수이면서 ch에 0이 없으면(주차공간이 없으면) wait에 추가하여 대기시키기
#tmp가 양수이면서 주차공간이 있으면 ch.index(0)을 이용하여 번호가 가장 작은 주차공간에 주차하기
#ch.index(0)은 ch에서 첫 번째로 발견된 0의 인덱스 반환 -> 가장 작은 번호의 주차위치 반환
#주차할 때 ch의 값을 차량번호로 바꿔서 주차가 되어있음을 표시 -> ch[idx] = tmp
#tmp가 음수이면 나가는 차량이므로 tmp를 양수로 바꾸고 주차한 위치 찾기 -> ch.index(abs(tmp))
#만약 대기 차량이 있을 경우, 주차한 위치에 대기 차량 중 첫번째 차량을 주차시킴
#대기 차량이 없을 경우, 주차한 위치의 값을 0으로 바꿔 주차가 되어있지 않음을 표시
import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    res = 0
    n, m = map(int, input().split())
    fee = [int(input()) for _ in range(n)]
    weight = [int(input()) for _ in range(m)]
    order = [int(input()) for _ in range(2*m)]
    order = deque(order)
    ch = [0] * n
    wait = deque()
    while order:
        tmp = order.popleft()
        if tmp > 0:
            if 0 not in ch:
                wait.append(tmp)
            else:
                idx = ch.index(0)
                ch[idx] = tmp
                res += fee[idx] * weight[tmp - 1]
        elif tmp < 0:
            idx = ch.index(abs(tmp))
            if wait:
                w = wait.popleft()
                ch[idx] = w
                res += fee[idx] * weight[w - 1]
            else:
                ch[idx] = 0
    print(f'#{tc} {res}')
