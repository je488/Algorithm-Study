#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYzIZNkq-v4DFAQ9(문제링크)
#s, t 각각의 리스트에서 다음 순서가 없는 경우 첫 원소로 돌아감
#따라서 연도(year)가 주어지면 s, t 리스트의 길이로 나눈 나머지 값 구하기
#연도는 1부터 시작하지만 리스트는 인덱스가 0부터 시작하므로 구한 나머지 값에서 -1 해주기
import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    ans = []
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    for _ in range(q):
        year = int(input())
        ans.append(s[year%n-1] + t[year%m-1])
    print(f'#{tc}', *ans)
