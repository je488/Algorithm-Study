import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    res = list()
    for i in range(n):
        for j in range(i+1, n):
            tmp = str(li[i] * li[j])
            for k in range(len(tmp)-1):
                if tmp[k] > tmp[k+1]:
                    break
            else:
                res.append(int(tmp))
    if len(res) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(res)}')
