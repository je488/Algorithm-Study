#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_6xWk6sbADFAWS(문제링크)
#트윈혼의 수를 x, 유니콘의 수를 y라고 할 때 뿔의 개수가 n이므로 2*x + y = n
#트윈혼과 유니콘을 합친 마리 수가 m이므로 x + y = m
#위의 2개의 식을 연립방정식으로 풀면 x = n - m이므로 트윈혼의 수는 n-m
#트윈혼의 수를 구하면 m에서 트윈혼의 수를 빼서 유니콘의 수를 구할 수 있음
#코드에서 t는 트윈혼의 수, u는 유니콘의 수
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    t = n - m
    u = m - t
    print(f'#{tc} {u} {t}')
