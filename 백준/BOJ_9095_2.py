import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
d = [0] * 11
d[0] = 1
for i in range(1, 11):
    if i - 1 >= 0:
        d[i] += d[i - 1]
    if i - 2 >= 0:
        d[i] += d[i - 2]
    if i - 3 >= 0:
        d[i] += d[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])