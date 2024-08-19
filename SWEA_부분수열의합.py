import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(i, sum):
    global ans
    if sum == k:
        ans += 1
        return
    if i == n:
        return
    DFS(i+1, sum+a[i])
    DFS(i+1, sum)

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    DFS(0, 0)
    print(f'#{tc} {ans}')