import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+ps[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ps = []
    pt = []
    for _ in range(n):
        a, b = map(int, input().split())
        ps.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
