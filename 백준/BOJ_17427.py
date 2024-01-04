import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
res = 0
for i in range(1, n+1):
    res += (n // i) * i
print(res)