import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = []
T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)
    res = f * time
    ans.append(f'#{tc} {res:.10f}')
for a in ans:
    print(a)
