#box는 박스(로봇)가 있는지 없는지 체크하는 리스트로 박스가 있으면 True, 없으면 False
#zero는 내구도가 0인 칸의 개수
#슬라이싱을 이용하여 한 칸 회전 구현 -> a = a[-1:] + a[:-1], box = box[-1:] + box[:-1]
#box[n-1]이 True이면 즉, 내려가는 위치에 박스가 있으면 박스 내리기(False로 값 바꿔주기)
#n-1칸은 내리는 위치로 박스가 존재할 수 없음
#따라서 n-2칸부터 0칸까지 박스 존재 여부와 내구도를 검사하여 박스 이동시키기
#만약 현재 칸에 박스가 있고 다음 칸에 박스가 없으며 내구도가 1 이상이면 박스 이동
#박스 이동시 box[i]는 False가 되고 box[i+1]은 True가 되며 i+1칸의 내구도는 1 감소
#i+1칸의 내구도가 0이면 zero += 1
#0부터 n-1까지 -> 방향으로 이동했으므로 n-1칸에 박스가 있는지 체크 후 있으면 박스 내리기
#박스를 올리기 전에 0칸의 내구도를 검사하여 1 이상이면 박스 올리기
#박스를 올리면 box[0]은 True가 되고 0칸의 내구도는 1 감소, 0칸의 내구도가 0이면 zero += 1
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
box = [False] * (2*n)
zero = 0
t = 1
while True:
    a = a[-1:] + a[:-1]
    box = box[-1:] + box[:-1]
    if box[n-1]:
        box[n-1] = False
    for i in range(n-2, -1, -1):
        if box[i]:
            if box[i+1] == False and a[i+1] > 0:
                box[i] = False
                box[i+1] = True
                a[i+1] -= 1
                if a[i+1] == 0:
                    zero += 1
    if box[n-1]:
        box[n-1] = False
    if a[0] > 0:
        box[0] = True
        a[0] -= 1
        if a[0] == 0:
            zero += 1
    if zero >= k:
        print(t)
        break
    t += 1
