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