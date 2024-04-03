import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
h, w, x, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h+x)]
for i in range(h):
    for j in range(w):
        a[i+x][j+y] -= a[i][j]
print(a)
for i in range(h):
    print(*a[i][:w])