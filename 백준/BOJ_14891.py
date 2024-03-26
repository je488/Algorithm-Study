#1. 톱니바퀴의 연쇄 회전을 구현하기 위해 각각의 톱니바퀴가 어떤 방향으로 회전하는지 조사
#ex) 0번 반시계(-1), 1번 시계(1), 2번 그대로(0), 3번 그대로(0)
#2. 1번의 결과에 따라 각각의 톱니바퀴 회전
#톱니바퀴마다 8개의 톱니를 가지고 있으므로 12시 방향의 톱니부터 0 ~ 7까지 번호 붙이기
#a[i][j] : i번 톱니바퀴에서 j번 톱니의 극
#문제에서는 톱니바퀴의 번호가 1 ~ 4지만 코드에서는 톱니바퀴의 번호가 0 ~ 3이므로 no -= 1
#d는 각각의 톱니바퀴가 어떤 방향으로 회전하는 지 저장(1이면 시계, -1이면 반시계, 0이면 회전X)
#no번 톱니바퀴가 회전할 때 no번의 왼쪽과 오른쪽에 있는 톱니들도 회전하는지 조사
#ex) no번 톱니바퀴의 왼쪽에 있는 톱니바퀴들을 조사할 때
#ex) i번째 톱니바퀴와 i+1번째 톱니바퀴가 맞닿은 극이 다르면 -> if a[i][2] != a[i+1][6]:
#ex) i번째 톱니바퀴를 i+1번째 톱니바퀴가 회전하는 반대방향으로 회전 -> d[i] = -d[i+1]
#ex) 극이 같으면 i번째 톱니바퀴는 회전하지 않고 나머지 톱니바퀴들도 회전하지 않으므로 break
#d의 값을 바탕으로 각각의 톱니바퀴 회전
#시계 방향이면 1차원 배열의 값이 오른쪽으로 한칸씩 이동, 반시계 방향이면 왼쪽으로 한칸씩 이동
#톱니바퀴를 회전시킨 후 각각의 톱니바퀴의 12시 방향의 값(a[i][0])에 따라 점수 계산
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = 4
a = [list(input()) for _ in range(n)]
k = int(input())
for _ in range(k):
    no, dir = map(int, input().split())
    no -= 1
    d = [0] * n
    d[no] = dir
    for i in range(no-1, -1, -1):
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    for i in range(no+1, n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1:
            tmp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = tmp
        elif d[i] == -1:
            tmp = a[i][0]
            for j in range(0, 7):
                a[i][j] = a[i][j+1]
            a[i][7] = tmp
ans = 0
for i in range(n):
    if a[i][0] == '1':
        ans |= (1 << i)
print(ans)
