import sys
import itertools as it
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n-i) // i
a = list(range(1, n+1))
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * b[L])
    if sum == f:
        print(*tmp)
        break
