import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def num_xy(n):
    g_cnt = 0
    g_total = 0
    num = n
    while True:
        g_cnt += 1
        g_total += g_cnt
        num -= g_cnt
        if num <= 0:
            x = g_cnt - (g_total - n)
            y = 1 + (g_total - n)
            break
    return x, y

def xy_num(x, y):
    group = x + y - 1
    total = 0
    for i in range(1, group+1):
        total += i
    return total - (y-1)

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    x1, y1 = num_xy(p)
    x2, y2 = num_xy(q)
    x = x1 + x2
    y = y1 + y2
    ans = xy_num(x, y)
    print(f'#{tc} {ans}')