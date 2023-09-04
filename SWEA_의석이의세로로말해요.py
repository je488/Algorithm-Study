#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO(문제링크)
#리스트 li에 문자열 5개를 입력받아 저장
#i는 하나의 문자열에서 각각의 문자에 해당하는 인덱스, j는 li에서 각각의 문자열에 해당하는 인덱스
#문자열의 길이는 서로 다를 수 있고 최대 길이는 15이므로 0부터 14까지 반복
#i가 문자열의 길이보다 작은 경우 즉, 문자열에서 i번째 문자가 있는 경우에만 res에 문자 저장
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    li = list()
    res = ''
    for _ in range(5):
        s = input().rstrip()
        li.append(s)
    for i in range(15):
        for j in range(5):
            if i < len(li[j]):
                res += li[j][i]
    print(f'#{tc} {res}')
