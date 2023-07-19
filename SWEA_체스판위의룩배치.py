#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYOBfxwaAXsDFATW(문제링크)
#조건을 만족하기 위해서는 각 행과 열마다 'O'가 한 개씩 존재해야함 ex)1행, 1열에 'O'가 한개씩 존재
#주어진 체스판 배치를 입력받아 li를 생성하고 zip()을 이용하여 li의 행과 열을 바꾼 cli 생성
#li와 cli에서 count()를 이용하여 한줄씩 'O'개수를 세고 1개가 아닐 경우, res를 'no'로 바꾸고 break
#조건을 만족하면 res가 바뀌지 않으므로 'yes'를 출력하고 조건을 만족하지 않을 경우 'no'출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    res = 'yes'
    li = [list(input().rstrip()) for _ in range(8)]
    cli = [list(x) for x in (zip(*li))]
    for i in range(8):
        if li[i].count('O') != 1 or cli[i].count('O') != 1:
            res = 'no'
            break
    print(f'#{tc} {res}')
