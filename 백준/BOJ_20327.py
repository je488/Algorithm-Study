#BOJ_16935.py 코드 활용
#op1, op2, op3, op4 함수는 BOJ_16935.py의 코드와 같음(ans의 크기만 조정)
#op_1_to_4(a, k, sx, sy, length)는 1번부터 4번까지의 연산을 수행하는 함수
#a는 원래 배열, k는 수행해야 하는 연산의 번호
#sx와 sy는 각 부분 배열의 왼쪽 위칸, length는 부분 배열의 크기
#부분 배열을 b에 복사한 뒤 1번 ~ 4번 연산 수행 후 원래 배열에 다시 값 넣기
#op5은 op1의 소스 코드 활용
#부분 배열을 하나의 칸으로 생각하기 위해 부분 배열의 가장 왼쪽 위칸을 기준으로 값 바꾸기
#x1, y1은 원래 위치의 왼쪽 위칸이고 x2, y2는 바뀌어야 하는 곳의 왼쪽 위칸
#x1, y1은 op1에서 i, j이고 x2, y2는 op1에서 n-i-1, j
#같은 방식으로 op6, op7, op8은 각각 op2, op3, op4의 소스 코드 활용
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def op1(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n-i-1][j]
    return ans

def op5(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count-i-1) * sub_size
            y2 = j * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def op2(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[i][n-j-1]
    return ans

def op6(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = i * sub_size
            y2 = (sub_count-j-1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def op3(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[n-j-1][i]
    return ans

def op7(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = (sub_count-j-1) * sub_size
            y2 = i * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def op4(a):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = a[j][n-i-1]
    return ans

def op8(a, l):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i * sub_size
            y1 = j * sub_size
            x2 = j * sub_size
            y2 = (sub_count-i-1) * sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def op_1_to_4(a, k, sx, sy, length):
    b = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            b[i][j] = a[sx+i][sy+j]

    if k == 1:
        b = op1(b)
    elif k == 2:
        b = op2(b)
    elif k == 3:
        b = op3(b)
    elif k == 4:
        b = op4(b)

    for i in range(length):
        for j in range(length):
            a[sx+i][sy+j] = b[i][j]

n, r = map(int, input().split())
size = (1 << n)
a = [list(map(int, input().split())) for _ in range(size)]
for _ in range(r):
    k, l = map(int, input().split())
    sub_size = (1 << l)
    if 1 <= k <= 4:
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                op_1_to_4(a, k, i, j, sub_size)
    elif 5 <= k <= 8:
        if k == 5:
            a = op5(a, l)
        elif k == 6:
            a = op6(a, l)
        elif k == 7:
            a = op7(a, l)
        elif k == 8:
            a = op8(a, l)

for i in range(size):
    print(' '.join(map(str, a[i])))
