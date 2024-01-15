import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if j+3 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
            if ans < tmp: ans = tmp
        if i+3 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j-1 >= 0:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
            if ans < tmp: ans = tmp
        if i-1 >= 0 and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+1 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            if ans < tmp: ans = tmp
        if i-1 >= 0 and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j+1 < m:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            if ans < tmp: ans = tmp
        if i+1 < n and j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            if ans < tmp: ans = tmp
        if i+2 < n and j-1 >= 0:
            tmp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            if ans < tmp: ans = tmp
        if j+2 < m:
            tmp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                tmp2 = tmp + a[i-1][j+1]
                if ans < tmp2: ans = tmp2
            if i+1 < n:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2: ans = tmp2
        if i+2 < n:
            tmp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:
                tmp2 = tmp + a[i+1][j+1]
                if ans < tmp2: ans = tmp2
            if j-1 >= 0:
                tmp2 = tmp + a[i+1][j-1]
                if ans < tmp2: ans = tmp2
print(ans)