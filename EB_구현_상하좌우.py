import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
move = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']
for m in move:
    for i in range(len(move_type)):
        if m == move_type[i]:
            a = x + dx[i]
            b = y + dy[i]
    if 1 <= a <= n and 1 <= b <= n:
        x, y = a, b
print(x, y)
