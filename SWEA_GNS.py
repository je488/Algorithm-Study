#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD(문제링크)
#입력받은 문자열 s에서 ZRO부터 NIN까지 순서대로 개수를 세서 cnt에 저장
#cnt[0]은 s에서 ZRO의 개수, cnt[1]은 s에서 ONE의 개수, ..., cnt[9]는 s에서 NIN의 개수
#cnt를 바탕으로 ZRO부터 NIN까지 순서대로 개수만큼 출력
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
