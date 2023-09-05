import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    s = input().rstrip()
    s1 = '.' + '.#..' * len(s)
    s2 = '.' + '#.#.' * len(s)
    s3 = '#.'+ '.#.'.join(s) + '.#'
    print(s1, s2, s3, s2, s1, sep = '\n')
