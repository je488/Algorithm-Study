#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB(문제링크)
#s, e는 특정 행에서 더해야 하는 범위의 시작점과 끝점
#행마다 s부터 e까지의 값을 ans에 더하기
#행을 기준으로 중간까지는 s, e의 간격이 벌어지고 중간 이후부터는 s, e의 간격이 다시 좁아짐
#따라서 행이 n//2(행의 중간 인덱스)보다 작은 경우 s -= 1, e += 1 -> 시작점과 끝점의 간격 넓히기
#행이 n//2보다 크거나 같은 경우 s += 1, e -= 1 -> 시작점과 끝점의 간격 좁히기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = 0
    s, e = n//2, n//2
    for i in range(n):
        for j in range(s, e+1):
            ans += a[i][j]
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {ans}')
