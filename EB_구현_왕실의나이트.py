#이것이 취업을 위한 코딩테스트다 - 117p
#x, y에 현재 나이트의 위치 입력받기
#x의 경우 a부터 h로 주어지므로 ord 함수를 이용하여 숫자로 바꿔주기
#steps는 나이트가 이동할 수 있는 8가지 방향의 행과 열의 증가치
#xx, yy는 이동하려는 위치의 좌표로 각각 1과 8사이이면 이동이 가능하므로 res += 1
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
s = input().rstrip()
x = ord(s[0]) - ord('a') + 1
y = int(s[1])
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
res = 0
for step in steps:
    xx = x + step[0]
    yy = y + step[1]
    if 1<=xx<=8 and 1<=yy<=8:
        res += 1
print(res)
