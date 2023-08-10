import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, str):
    global res
    if L == n:
        s = set(str)
        if len(s) == 26:
            res += 1
    else:
        DFS(L+1, str + word[L])
        DFS(L+1, str)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    word = [input().rstrip() for _ in range(n)]
    res = 0
    DFS(0, '')
    print(f'#{tc} {res}')
