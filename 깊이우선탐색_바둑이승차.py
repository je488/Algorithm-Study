import sys
# sys.stdin = open("input.txt", "r")
def DFS(L, hap, thap):
    global res
    if hap + (total - thap) < res:
        return
    if hap > c:
        return
    if L == n:
        if hap > res:
            res = hap
    else:
        DFS(L+1, hap + li[L], thap + li[L])
        DFS(L+1, hap, thap + li[L])
if __name__ == "__main__":
    c, n = map(int, input().split())
    li = [0] * n
    for i in range(n):
        li[i] = int(input())
    res = -2147000000
    total = sum(li)
    DFS(0, 0, 0)
    print(res)
