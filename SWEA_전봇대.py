#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS(문제링크)
#두 개의 전선 j, k가 있다고 가정할 때 전선이 교차하려면 한 끝점은 j가 높고 한 끝점은 k가 높으면 됨
#그러기 위해서는 j의 끝점에서 k의 끝점을 뺀 값이 하나는 +고 하나는 -여야 함
#따라서 2개의 끝점의 차를 곱하면 값이 - 즉, 0보다 작아야 함
#j전선이 k전선을 만나는 경우와 k전선이 j전선을 만나는 경우는 교차점이 같음 -> 중복
#중복을 방지하기 위해 2중 for문에서 k의 시작점을 j+1로 설정하여 한 번 체크한 경우를 배제
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list()
    res = 0
    for i in range(n):
        a, b = map(int, input().split())
        li.append([a, b])
    for j in range(n):
        for k in range(j+1, n):
            a1, b1 = li[j]
            a2, b2 = li[k]
            if (a1-a2) * (b1-b2) < 0:
                res += 1
    print(f'#{tc} {res}')
