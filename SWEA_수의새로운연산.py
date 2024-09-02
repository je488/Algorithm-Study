#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw(문제링크)
#num_xy()는 숫자를 좌표로 바꾸는 함수, xy_num()은 좌표를 숫자로 바꾸는 함수
#좌표의 합이 같은 것끼리 그룹으로 묶기 -> (1, 1) / (1, 2) (2, 1) / (1, 3) (2, 2) (3, 1)
#위의 좌표를 숫자로 나타내면 1 / 2 3 / 4 5 6
#각 그룹의 첫번째 값의 x좌표는 1, y좌표는 그룹 번호 ex) 3번 그룹의 첫번째 값 좌표는 (1, 3)
#그룹마다 숫자의 개수는 1씩 증가하고 좌표의 합도 1씩 증가
#그룹 내에서 숫자가 1 증가할 때마다 x좌표는 1씩 증가하고 y좌표는 1씩 감소
#k번 그룹일 때 그룹 내에서 x좌표는 1부터 k까지 1씩 증가하고 y좌표는 k부터 1까지 1씩 감소
#g_cnt는 그룹 번호, g_total은 1번부터 g_cnt번 그룹까지 숫자의 개수 및 g_cnt번 그룹의 마지막 숫자
#ex) n = 9일 때 g_cnt = 4이므로 n은 4번 그룹, g_total = 10이므로 4번 그룹의 마지막 숫자는 10
#ex) n이 속한 그룹의 x좌표는 1부터 4까지 1씩 증가하고 y좌표는 4부터 1까지 1씩 감소
#ex) g_total - n = 1이므로 n의 x좌표는 g_cnt - 1 = 3, y좌표는 1 + 1 = 2
#각 그룹의 번호는 각 그룹의 좌표의 합 - 1
#ex) x = 5, y = 3일 때 좌표가 속한 그룹은 5 + 3 - 1 = 7이므로 7번 그룹
#ex) 1부터 7까지 모두 더해서 7번 그룹의 최댓값을 구하면 28
#ex) y좌표는 그룹의 번호부터 1까지 1씩 감소하므로 y좌표가 3이면 7번 그룹의 끝에서 3번째 숫자
#ex) 따라서 그룹의 최댓값 - (y - 1)로 좌표의 숫자값을 구하면 28 - (3 - 1) = 26
#참고 : https://florescene.tistory.com/399
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
