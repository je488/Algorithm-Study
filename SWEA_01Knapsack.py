#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBJAVpqrzQDFAWr(문제링크)
#n <= 100이므로 백트래킹을 이용하면 시간복잡도가 O(2^n) = 2^100으로 1억보다 크기 때문에 시간 초과
#따라서 다이나믹 프로그래밍을 이용하여 해결
#dp[i][j] : i번째 물건까지 고려하고 가방의 부피가 j일 때 최대가 되는 가치의 합
#현재 물건의 부피가 v일 때 v > j인 경우 현재 물건을 가방에 넣을 수 없음
#따라서 dp[i][j] = dp[i-1][j] (이전 물건까지 고려하고 가방 부피가 j인 최대 가치 합)
#현재 물건의 부피가 v일 때 v <= j인 경우 현재 물건을 가방에 넣을지 말지 결정
#현재 물건을 가방에 넣는 경우: dp[i][j] = dp[i-1][j-v] + c
#현재 물건을 가방에 넣으려면 이전 물건까지 넣었을 때 가방의 부피가 j-v여야 함
#dp[i-1][j-v] + c : 이전 물건까지 고려하고 가방 부피가 j-v일 때 최대 가치 합 + 현재 물건의 가치
#현재 물건을 가방에 넣지 않는 경우: dp[i][j] = dp[i-1][j]
#가방에 넣는 경우와 넣지 않는 경우 중 최대 가치의 합이 더 큰 것을 dp[i][j]에 넣기
#따라서 dp[i][j] = max(dp[i-1][j], dp[i-1][j-v] + c)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        v, c = map(int, input().split())
        for j in range(1, k+1):
            if v <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v] + c)
            else:
                dp[i][j] = dp[i-1][j]
    print(f'#{tc} {dp[n][k]}')
