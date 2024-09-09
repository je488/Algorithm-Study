#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14zIwqAHwCFAYD(문제링크)
#a는 원본 암호문 뭉치, c는 명령어
#c를 탐색하면서 c의 값이 'I'인 경우 삽입, 'D'인 경우 삭제, 'A'인 경우 추가
#삽입의 경우 반복문과 insert()를 이용하여 x번째 암호문 바로 다음에 y개의 암호문 삽입
#삭제의 경우 del과 슬라이싱 이용해 x번째 암호문 바로 다음부터 y개의 암호문 삭제
#추가의 경우 반복문과 append()를 이용하여 a의 맨 뒤에 y개의 암호문 추가
#수정된 암호문 뭉치의 앞 10개 암호문만 출력해야 하므로 공백을 구분자로 하여 a[:10] 출력
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
