import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    coin.sort(reverse=True)
    DFS(0, 0)
    print(res)
