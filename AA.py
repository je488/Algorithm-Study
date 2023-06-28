import sys
##sys.stdin = open("input.txt", "r")
n = int(input())
info = []
for _ in range(n):
    height, weight = map(int, input().split())
    info.append([height, weight])
info.sort(key = lambda x: (x[0], x[1]))
cnt = n
for i in range(len(info)-1):
    for j in range(i+1, len(info)):
        if info[i][1] < info[j][1]:
            cnt -= 1
            break
print(cnt)
