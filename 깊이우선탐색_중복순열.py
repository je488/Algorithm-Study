import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L):
    global cnt
    if L == m:
        print(*li)
        cnt += 1
    else:
        for i in range(1, n+1):
            li[L] = i
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    li = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
