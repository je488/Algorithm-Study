import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, value = map(int, input().split())
        res[a][b] = value
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(res[i][j], end=' ')
        print()
