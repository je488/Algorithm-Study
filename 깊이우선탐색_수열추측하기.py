import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    if L == n and sum == f:
        print(*li)
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                li[L] = i
                ch[i] = 1
                DFS(L+1, sum + (li[L] * b[L]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    ch = [0] * (n+1)
    li = [0] * n
    b = [1] * n
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i
    DFS(0, 0)
