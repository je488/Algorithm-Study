#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b9AkKACkBBASw(문제링크)
#1 * 1 타일 n개를 이용하여 r * c 크기의 직사각형 타일을 만들어야 하므로 r * c <= n
#r = 1, c = 2일 때와 r = 2, c = 1일 때의 tmp값은 같으므로 c는 1이 아닌 r부터 반복
#r * c <= n인 경우에만 tmp값을 구하므로 tmp는 항상 0 이상
#따라서 정답(ans)을 -1로 초기화한 뒤 가장 먼저 구한 tmp값을 ans에 할당
#이후로는 이전에 구한 ans와 tmp를 비교해서 더 작은 값을 ans에 할당하여 최솟값 구하기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    ans = -1
    for r in range(1, n+1):
        c = r
        while r * c <= n:
            tmp = a * abs(r - c) + b * (n - r * c)
            if ans == -1:
                ans = tmp
            else:
                ans = min(ans, tmp)
            c += 1
    print(f'#{tc} {ans}')
