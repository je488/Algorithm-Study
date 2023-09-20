import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
s = input().rstrip()
x = ord(s[0]) - ord('a') + 1
y = int(s[1])
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
res = 0
for step in steps:
    xx = x + step[0]
    yy = y + step[1]
    if 1<=xx<=8 and 1<=yy<=8:
        res += 1
print(res)
