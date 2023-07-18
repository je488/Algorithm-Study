#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYP5JmsqcngDFATW(문제링크)
#본연의 문자열을 비교했을 때 같으면 yes
#각 문자열의 앞글자가 다르면 무한히 반복해도 같아질 수 없으므로 no
#문자열의 길이가 다른 경우, 서로의 문자열 길이를 곱해서 문자열의 길이를 같게 만든 후 비교
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
