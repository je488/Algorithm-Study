#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYj_Dz-6qLgDFASl(문제링크)
#a는 더하기만 가능하고 b는 빼기만 가능하므로 a가 b보다 큰 경우 조작 불가능
#sub이 0이면 a, b는 같으므로 조작 횟수는 0
#sub이 1이거나 음수이면 조작을 통해 a와 b를 같게 할 수 없으므로 -1
#sub이 짝수이면 가장 작은 소수인 2를 더하거나 빼주면 되므로 최대 조작 횟수는 sub // 2
#sub이 홀수이면 2를 제외한 가장 작은 소수인 3을 빼서 짝수를 만들고 2를 더하거나 빼기
#따라서 최대 조작 횟수는 (sub - 3) // 2
#최대 조작 횟수를 구해야 하므로 가장 작은 소수인 2와 2를 제외한 가장 작은 소수인 3 이용
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    sub = b - a
    if sub == 0:
        ans = 0
    elif sub <= 1:
        ans = -1
    else:
        if sub % 2 == 0:
            ans = sub // 2
        else:
            ans = (sub - 3) // 2 + 1
    print(f'#{tc} {ans}')
