import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
h = int(input())
res = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                res += 1
print(res)
