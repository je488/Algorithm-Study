#비트 연산 이용
#문제에서는 1 <= x <= 20이나 코드에서는 0 <= x <= 19로 구현 -> x에서 1 빼기
#1 ~ N까지의 집합을 사용하기 위해서는 공간이 2배 더 필요하고 각종 연산을 변형해서 사용해야 함
#따라서 1 ~ N을 0 ~ N-1로 변형해서 사용
#s에 x를 추가 : s | (1 << x)
#s에서 x를 제거 : s & ~(1 << x)
#s에 x가 있는지 검사(결과가 0이면 없고 0이 아니면 있음) : s & (1 << x)
#s에서 x를 토글(0이면 1로, 1이면 0으로) : s ^ (1 << x)
#s를 0부터 n-1까지 전체 집합으로 만들기 : (1 << n) - 1
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
m = int(input())
n = 20
s = 0
for _ in range(m):
    op, *num = input().split()
    if len(num) > 0:
        x = int(num[0]) - 1
    if op == 'add':
        s = (s | (1 << x))
    elif op == 'remove':
        s = (s & ~(1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        if res > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle':
        s = (s ^ (1 << x))
    elif op == 'all':
        s = (1 << n) - 1
    else:
        s = 0
