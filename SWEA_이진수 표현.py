ans = list()
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if m == 0:
        ans.append(f'#{tc} OFF')
    else:
        for _ in range(n):
            if m % 2 == 0:
                ans.append(f'#{tc} OFF')
                break
            m = m // 2
        else:
            ans.append(f'#{tc} ON')
for a in ans:
    print(a)
