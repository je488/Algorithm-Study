import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = list(input().rstrip())
    cnt = int(input())
    loc = sorted(list(map(int, input().split())), reverse=True)
    for l in loc:
        s.insert(l, '-')
    print(f'#{tc}', ''.join(s))
