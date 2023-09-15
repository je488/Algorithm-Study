#이것이 취업을 위한 코딩테스트다 - 112p
#dx, dy는 왼쪽(L), 오른쪽(R), 위(U), 아래(D)로 이동하기 위한 행과 열의 증가치
#이동 계획을 move에 저장하고 하나씩 move_type의 값과 비교하여 이동 방향 확인
#이동 방향에 해당하는 dx, dy를 더해 이동 후의 좌표 a, b 구하기
#이동 후의 좌표가 정사각형 공간을 벗어나면 무시하므로 a, b가 1과 n 사이인지 확인
#공간을 벗어나지 않으면 x, y에 이동 후 좌표를 대입하여 이동 수행
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
move = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']
for m in move:
    for i in range(len(move_type)):
        if m == move_type[i]:
            a = x + dx[i]
            b = y + dy[i]
    if 1 <= a <= n and 1 <= b <= n:
        x, y = a, b
print(x, y)
