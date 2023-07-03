import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
li = list(map(int, input().split()))
res = [0] * n
li.insert(0, 0)
for i in range(1, n+1):
    for j in range(n):
        if li[i] == 0 and res[j] == 0:
            res[j] = i
            break
        elif res[j] == 0:
            li[i] -= 1
print(*res)
