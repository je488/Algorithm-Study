import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, a, b, c):
    global res
    if L == n:
        if a != b and b != c and c != a:
            cha = max(a, b, c) - min(a, b, c)
            if cha < res:
                res = cha
    else:
        DFS(L+1, a+coin[L], b, c)
        DFS(L+1, a, b+coin[L], c)
        DFS(L+1, a, b, c+coin[L])
if __name__ == '__main__':
    n = int(input())
    coin = list()
    for _ in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0, 0, 0, 0)
    print(res)
