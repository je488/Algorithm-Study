import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    ans = []
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    for _ in range(q):
        year = int(input())
        ans.append(s[year%n-1] + t[year%m-1])
    print(f'#{tc}', *ans)