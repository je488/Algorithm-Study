#시간복잡도는 O((NM) ^ K)
#함수 호출을 K번하고 각각의 함수마다 NM번 반복
#K의 최대값은 4, N과 M의 최대값은 10
#NM ^ K -> NM ^ 4 -> 10*10 ^ 4 = 1억이므로 시간복잡도가 큰 편
#cnt는 선택한 칸의 개수, s는 선택한 칸의 합
#c는 중복(선택)여부를 체크하는 리스트로 이전에 선택하였으면 True, 선택하지 않았으면 False
#dx, dy는 인접한 칸의 좌표 차이(오른쪽, 왼쪽, 아래, 위)
#ok는 선택이 가능하면 True, 가능하지 않으면 False
#각 칸마다 N*M 범위 안에 있는 인접한 칸들을 이전에 선택하지 않았는지 체크
#인접한 칸들 중 하나라도 선택했다면 그 칸은 선택 불가능
#선택한 칸이 같은데, 선택한 순서가 다른 방법을 여러 번 계산
#ex) (0, 1), (1, 0)을 선택 후 (1, 0), (0, 1)을 또 선택 가능
#ans = s에서 ans를 지역변수로 인식 -> if ans < s에서 에러 발생 -> global로 전역변수 표시
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(cnt, s):
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return
    for x in range(n):
        for y in range(m):
            if c[x][y]:
                continue
            ok = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if c[nx][ny]:
                        ok = False
            if ok:
                c[x][y] = True
                go(cnt + 1, s + a[x][y])
                c[x][y] = False
go(0, 0)
print(ans)
