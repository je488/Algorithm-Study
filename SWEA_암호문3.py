import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10
for tc in range(1, T+1):
    n = int(input())
    a = list(input().split())
    m = int(input())
    c = input().split()
    for i in range(len(c)):
        if c[i] == 'I':
            x = int(c[i+1])
            y = int(c[i+2])
            for j in range(y):
                a.insert(x+j, c[i+3+j])
        elif c[i] == 'D':
            x = int(c[i+1])
            y = int(c[i+2])
            del a[x:x+y]
        elif c[i] == 'A':
            y = int(c[i+1])
            for j in range(y):
                a.append(c[i+2+j])
    print(f'#{tc}', ' '.join(a[:10]))
