import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    while a:
        for i in range(len(a)):
            if a[i] % 4 == 0 and int(a[i]*0.75) in a:
                tmp = a.pop(i)
                idx = a.index(int(tmp*0.75))
                ans.append(a.pop(idx))
                break
    print(f'#{tc}', *ans)