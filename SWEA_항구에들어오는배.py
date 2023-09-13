#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMedCxalW8DFAXd(문제링크)
#최소한의 배로 주어진 즐거운 날들의 목록(happy)을 만들 수 있어야 함
#따라서 각 배들의 주기를 구하고 주기를 기준으로 배가 들어오는 날을 구했을 때 happy와 같아져야 함
#주기의 최소 개수가 배의 최소 개수와 같음
#happy의 두번째 값부터 ship에 없는 경우에만 1을 빼서 주기(tmp) 구하기
#구한 주기를 기준으로 1일차를 제외하고 마지막 즐거운 날까지 배가 들어온 날을 ship에 추가
#새로운 주기를 계산할 때마다 배의 개수(res)가 1씩 증가
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    happy = list(int(input()) for _ in range(n))
    ships = set()
    res = 0
    for i in range(1, len(happy)):
        if happy[i] in ships:
            continue
        tmp = happy[i] - 1
        for j in range(tmp + 1, happy[-1] + 1, tmp):
            ships.add(j)
        res += 1
    print(f'#{tc} {res}')
