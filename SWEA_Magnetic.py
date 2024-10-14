#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD(문제링크)
#board의 열을 탐색하면서 N극(1), S극(2) 짝의 개수 찾기
#flag를 이용하여 board의 값이 1이면 flag값을 True로 바꾸기
#board의 값이 2이고 flag의 값이 True이면 교착상태이므로 res에 1 더하고 flag값을 원래대로 바꾸기
#N극이 테이블 위에 있으므로 S극이 N극보다 먼저 발견되면 테이블 아래로 떨어짐
#따라서 값이 1(N극)인 것을 먼저 찾은 뒤에 값이 2(S극)인 것 찾기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        flag = False
        for j in range(n):
            if board[j][i] == 1:
                flag = True
            elif board[j][i] == 2:
                if flag:
                    res += 1
                    flag = False
    print(f'#{tc} {res}')
