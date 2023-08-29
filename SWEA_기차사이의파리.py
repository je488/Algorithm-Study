#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWajaTmaZw4DFAWM(문제링크)
#두 기차가 충돌하면 파리가 죽으므로 두 기차가 충돌하기까지 걸린 시간 구하기 -> time
#기차가 충돌하기까지 걸린 시간을 이용해 파리가 죽기 전까지 이동한 거리 구하기 -> res
#거리 = 속력 * 시간
#time = 기차 사이의 거리 / (A의 속력 + B의 속력)
#res = 파리의 속력 * time
#실행시간을 단축하기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = []
T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)
    res = f * time
    ans.append(f'#{tc} {res:.10f}')
for a in ans:
    print(a)
