import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    while k < m * n:
        if k % n == y:
            print(k + 1)
            break
        k += m
    else:
        print(-1)