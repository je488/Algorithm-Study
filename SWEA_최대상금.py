import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, n = input().split()
    n = int(n)
    now = set([a])
    nxt = set()
    for _ in range(n):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(a)-1):
                for j in range(i+1, len(a)):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    ans = max(map(int, now))
    print(f'#{tc} {ans}')
