import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
li = list(map(int, input().split()))
lt = 0
rt = n-1
res = ''
last = 0
tmp = []
while lt <= rt:
    if li[lt] > last:
        tmp.append((li[lt], 'L'))
    if li[rt] > last:
        tmp.append((li[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
        last = tmp[0][0]
    tmp.clear()
print(len(res))
print(res)
