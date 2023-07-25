import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(ct[L]*i))
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    ct = list()
    cn = list()
    for _ in range(k):
        p, n = map(int, input().split())
        ct.append(p)
        cn.append(n)
    cnt = 0
    DFS(0, 0)
    print(cnt)
