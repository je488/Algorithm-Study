import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10
for tc in range(1, T+1):
    n, a = input().split()
    n = int(n)
    ans = []
    for i in a:
        if len(ans) == 0 or ans[-1] != i:
            ans.append(i)
        else:
            ans.pop()
    print(f'#{tc}', ''.join(ans))