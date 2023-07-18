import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    s1, s2 = input().split()
    if s1 == s2:
        print(f'#{tc} yes')
    if s1[0] != s2[0]:
        print(f'#{tc} no')
    else:
        if s1*len(s2) == s2*len(s1):
            print(f'#{tc} yes')
        else:
            print(f'#{tc} no')
