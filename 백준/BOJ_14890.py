#각각의 행, 열을 1차원 배열에 넣어서 경사로를 놓거나 놓지 않고도 지나갈 수 있는지 검사
#go는 각각의 행, 열에 대해 지나갈 수 있는지 검사하는 함수(지나갈 수 있으면 True, 없으면 False)
#c는 경사로를 중복해서 놓지 않기 위해 체크하는 리스트
#i번 칸에 경사로를 놓았으면 c[i]값은 True, 놓지 않았으면 False
#하나의 행 또는 열에서 높이가 다른 것이 발견되면 경사로를 놓을 수 있는지 검사
#높이가 다른데 차이가 1이 아닌 경우 경사로를 놓을 수 없으므로 False 리턴
#경사로는 왼쪽 방향이나 오른쪽 방향으로 놓을 수 있음
#i-1번칸이 i번칸보다 작은 경우에는 왼쪽 방향, 큰 경우에는 오른쪽 방향에 경사로 놓기
#경사로를 놓다가 범위를 벗어나는 경우 False 리턴
#낮은 칸의 높이가 모두 같지 않거나 l개가 연속되지 않는 경우 False 리턴
#경사로를 이미 놓은 곳에 또 놓는 경우 False 리턴
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(a, l):
    n = len(a)
    c = [False] * n
    for i in range(1, n):
        if a[i-1] != a[i]:
            diff = abs(a[i] - a[i-1])
            if diff != 1:
                return False
            if a[i-1] < a[i]:
                for j in range(1, l+1):
                    if i-j < 0:
                        return False
                    if a[i-1] != a[i-j]:
                        return False
                    if c[i-j]:
                        return False
                    c[i-j] = True
            else:
                for j in range(l):
                    if i+j >= n:
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True

n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    d = a[i]
    if go(d, l):
        ans += 1
for j in range(n):
    d = [a[i][j] for i in range(n)]
    if go(d, l):
        ans += 1
print(ans)
