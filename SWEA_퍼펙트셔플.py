#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW(문제링크)
#l은 cards를 반으로 나누었을 때 첫 번째 카드 그룹을 나타내는 인덱스
#r은 cards를 반으로 나누었을 때 두 번째 카드 그룹을 나타내는 인덱스
#n을 2로 나눈 몫만큼 반복해서 res에 카드를 교대로 저장하고 l과 r을 1씩 증가시키기
#n이 홀수이면 마지막에 cards의 중간에 위치한 cards[n//2]를 res에 저장
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(input().split())
    res = list()
    l = 0
    r = (n+1) // 2
    for _ in range(n//2):
        res.append(cards[l])
        res.append(cards[r])
        l += 1
        r += 1
    if n % 2 == 1:
        res.append(cards[n//2])
    print(f'#{tc}', *res)
