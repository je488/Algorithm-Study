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
            if ch[i] == 0:
                li[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
if __name__ == "__main__":
   n, m = map(int, input().split())
   li = [0] * m
   ch = [0] * (n+1)
   cnt = 0
   DFS(0)
   print(cnt)
