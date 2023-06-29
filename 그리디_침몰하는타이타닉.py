#몸무게가 가벼운 순으로 정렬
#가장 가벼운 몸무게와 가장 무거운 몸무게를 합했을 때 최대 몸무게보다 작으면 둘 다 탈출
#최대 몸무게보다 크면 가장 무거운 몸무게만 탈출(가장 작은 몸무게랑 더했을 때 최대 몸무게를 넘었으니 다른 몸무게와 더했을 때도 최대 몸무게를 넘음)
#사람이 한명만 남았을 경우 weight[0], weight[-1] 둘 다 같은 값이므로 논리적 오류 발생, 두 번 pop()해서 에러가 발생할 수 있음
#따라서, if문을 추가하여 한명만 남았을 경우 구명보트를 1개 추가하고 반복문 탈출
#리스트는 pop(0)을 하면 값(자료)들이 모두 앞으로 당겨지는 비효율적 연산을 함
#데크는 큐와 달리 popleft()를 하면 값들이 움직이지 않고 포인터 변수가 그 다음 값을 가리킴 -> 데크를 import 하여 사용
#데크는 앞, 뒤에서 모두 pop, append 가 가능함
import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] <= m:
        weight.popleft()
        weight.pop()
        cnt += 1
    else:
        weight.pop()
        cnt += 1
print(cnt)
