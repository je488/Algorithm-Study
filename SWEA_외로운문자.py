import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
ans = []
for tc in range(1, T+1):
    s = input().rstrip()
    li = []
    for i in set(s):
        if s.count(i) % 2 == 1:
            li.append(i)
    if len(li) == 0:
        res = 'Good'
    else:
        res = "".join(sorted(li))
    ans.append(f'#{tc} {res}')
for a in ans:
    print(a)
