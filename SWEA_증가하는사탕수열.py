#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AY4XhKTKU0IDFARM(문제링크)
#a < b < c를 만족시키기 위해 b에서 먹을 사탕의 개수, a에서 먹을 사탕의 개수 구하기
#사탕을 최소 개수로 먹기 위해 b는 c보다 1이 적게 먹고 a는 b보다 1이 적게 먹기
#따라서 b >= c인 경우 사탕을 b-c+1개 먹고 a >= b인 경우 a-b+1개 먹기
#a, b, c 모두 1 이상이어야 하므로 사탕을 먹은 뒤 a < 1이면 -1 출력
#사탕을 먹은 뒤에는 a < b < c를 만족하므로 가장 작은 a만 1보다 작은지 체크하면 됨
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    ans = 0
    a, b, c = map(int, input().split())
    if b >= c:
        ans += (b-c+1)
        b = c-1
    if a >= b:
        ans += (a-b+1)
        a = b-1
    if a < 1:
        ans = -1
    print(f'#{tc} {ans}')
