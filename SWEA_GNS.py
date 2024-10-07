import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for _ in range(T):
    tc, n = input().split()
    s = list(input().split())
    cnt = []
    for i in range(10):
        tmp = s.count(li[i])
        cnt.append(tmp)
    print(tc)
    for i in range(10):
        print((li[i] + " ") * cnt[i])