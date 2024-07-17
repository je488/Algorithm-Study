#1번 연산은 배열을 상하 반전시키는 연산으로 열의 위치는 바뀌지 않음
#ans의 0번행은 a의 n-1행, ans의 1번행은 a의 n-1-1행, ..., ans의 i행은 a의 n-i-1행
#따라서 ans[i][j] = a[n-i-1][j]
#2번 연산은 행의 위치가 바뀌지 않으므로 ans의 j열은 a의 m-j-1열 -> ans[i][j] = a[i][m-j-1]
#3번 연산의 경우 ans의 4행은 a의 4열, ans의 i행은 a의 i열, ans의 j열은 a의 n-j-1행
#따라서 ans[i][j] = a[n-j-1][i]
#4번 연산의 경우 ans의 i행은 a의 m-i-1열, ans의 j열은 a의 j행 -> ans[i][j] = a[j][m-i-1]
#5, 6번 연산은 배열을 크기가 n//2 * m//2인 부분 배열로 나누기
#각 그룹에서 같은 위치를 인덱스로 나타낼 때(1번 그룹 기준)
#1번 그룹의 (i, j)는 2번 그룹의 (i, j+m//2), 3번 그룹의 (i+n//2, j+m//2), 4번 그룹의 (i+n//2, j)
#위의 인덱스를 바탕으로 5, 6번 연산 수행
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def op1(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[n-i-1][j]
    return ans

def op2(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = a[i][m-j-1]
    return ans

def op3(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[n-j-1][i]
    return ans

def op4(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = a[j][m-i-1]
    return ans

def op5(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i][j+m//2] = a[i][j]
            ans[i+n//2][j+m//2] = a[i][j+m//2]
            ans[i+n//2][j] = a[i+n//2][j+m//2]
            ans[i][j] = a[i+n//2][j]
    return ans

def op6(a):
    n = len(a)
    m = len(a[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            ans[i+n//2][j] = a[i][j]
            ans[i+n//2][j+m//2] = a[i+n//2][j]
            ans[i][j+m//2] = a[i+n//2][j+m//2]
            ans[i][j] = a[i][j+m//2]
    return ans

n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
func = [op1, op2, op3, op4, op5, op6]
for op in map(int, input().split()):
    a = func[op-1](a)
for row in a:
    print(*row, sep = ' ')
