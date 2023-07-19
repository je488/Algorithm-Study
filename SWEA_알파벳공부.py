#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYLnMQT6vPADFATf(문제링크)
#alpha에 순서가 올바른 알파벳 전체를 저장해두고 문자열 s와 비교
#인덱스 i로 0부터 s의 길이만큼 탐색하고 문자가 같으면 res에 1씩 더하기
#순서대로 일치하는 알파벳 개수이므로 중간에 문자가 달라지면 break
#input = sys.stdin.readline을 사용했으므로 input()으로 문자열을 읽을 때 줄바꿈 기호까지 읽음
#따라서 rstrip()으로 줄바꿈 기호 제거
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
for tc in range(1, T + 1):
    res = 0
    s = input().rstrip()
    for i in range(len(s)):
        if s[i] == alpha[i]:
            res += 1
        else:
            break
    print(f'#{tc} {res}')
