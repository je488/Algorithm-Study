import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum, cal):
    global res
    if cal > l:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+info[L][0], cal+info[L][1])
        DFS(L+1, sum, cal)
if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        n, l = map(int, input().split())
        info = list()
        res = 0
        for _ in range(n):
            s, c = map(int, input().split())
            info.append([s, c])
        DFS(0, 0, 0)
        print(f'#{tc} {res}')
