import sys
# sys.stdin = open("input.txt", "r")
def DFS(v):
    if v == n+1:
        if len(ans) != 0:
            print(*ans)
    else:
        ans.append(v)
        DFS(v+1)
        ans.pop()
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ans = []
    DFS(1)
