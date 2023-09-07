#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWO6Oao6N4QDFAWw(문제링크)
#주어진 문자열 s를 슬라이싱을 이용해 뒤집었을 때 같으면 팰린드롬이므로 Exist
#같지 않은 경우 for문으로 s를 탐색하며 문자가 '?'이면 s에서 대칭되는 문자로 바꿔줌
#모두 탐색하고 바꿔준 뒤에 슬라이싱을 이용하여 뒤집었을 때 같으면 팰린드롬이고 다르면 팰린드롬X
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = list(input().rstrip())
    if s == s[::-1]:
        res = 'Exist'
    else:
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = s[-i-1]
        if s == s[::-1]:
            res = 'Exist'
        else:
            res = 'Not exist'
    print(f'#{tc} {res}')
