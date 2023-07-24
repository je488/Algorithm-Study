import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    if L == k:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+li[L])
        DFS(L+1, sum-li[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    k = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    res = set()
    DFS(0, 0)
    print(s - len(res))
