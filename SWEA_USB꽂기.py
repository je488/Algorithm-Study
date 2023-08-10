#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXDNEA3aaU0DFAVX(문제링크)
#p는 '처음' USB를 꽂을 때 올바른 면일 확률, q는 USB가 올바른 면일 때 정상적으로 꽂힐 확률
#s1은 1번 뒤집어서 USB가 꽂힐 확률, s2는 2번 뒤집어서 USB가 꽂힐 확률
#s1 : 처음에 올바른 면이 아니어서 뒤집고 정상적으로 꽂히는 경우 -> (1 - p) * q
#s2 : 처음에 올바른 면이나 정상적으로 꽂히지 않아서 뒤집기 -> 올바른 면이 아니므로 실패 ->
#다시 뒤집고 정상적으로 꽂히는 경우 -> p * (1 - q) * q
#p는 처음 꽂을 때만 확률을 따지므로 2번째 꽂을 때부터는 p의 확률을 따질 필요가 없음
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s1 < s2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
