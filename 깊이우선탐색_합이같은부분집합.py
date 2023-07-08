import sys
# sys.stdin = open("input.txt", "r")
def DFS(L, hap):
    if hap > total // 2:
        return
    if L == n:
        if hap == (total - hap):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, hap+li[L])
        DFS(L+1, hap)

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    total = sum(li)
    DFS(0, 0)
    print("NO")
