#N * M의 모든 칸에 모든 테트로미노 놓아보기
#테트로미노는 기본도형 5개를 회전 또는 대칭하여 총 19가지
#i, j는 각 테트로미노의 기준칸(왼쪽 위) 좌표
#각각의 테트로미노를 N * M에 놓을 수 있는지 확인 후 놓을 수 있으면 합 계산
#구한 합(tmp)이 이전에 구해놓은 정답(ans)보다 크면 ans값 바꿔주기
#테트로미노를 N * M에 놓을 수 있는 방법은 기준칸을 N * M에 놓을 수 있는 방법의 수와 같음
#따라서 각각의 방법은 NM가지 -> O(NM)
#테트로미노는 총 19가지이므로 총 시간 복잡도는 O(19NM) = O(NM)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if j+3 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
            if ans < tmp: ans = tmp
        if i+3 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j-1 >= 0:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
            if ans < tmp: ans = tmp
        if i-1 >= 0 and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            if ans < tmp: ans = tmp
        if i-1 >= 0 and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j-1 >= 0:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            if ans < tmp: ans = tmp
        if j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                tmp2 = tmp + a[i-1][j+1]
                if ans < tmp2: ans = tmp2
            if i+1 < n:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2: ans = tmp2
        if i+2 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2: ans = tmp2
            if j-1 >= 0:
                tmp2 = tmp + a[i+1][j-1]
                if ans < tmp2: ans = tmp2
print(ans)
