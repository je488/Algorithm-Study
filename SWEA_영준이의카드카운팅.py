import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = input().rstrip()
    res = {'S':13, 'D':13, 'H':13, 'C':13}
    card = list()
    for i in range(0, len(s), 3):
        if s[i:i+3] in card:
            print(f'#{tc} ERROR')
            break
        else:
            card.append(s[i:i + 3])
            res[s[i]] -= 1
    else:
        print(f'#{tc}', *res.values())
