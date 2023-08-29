#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ(문제링크)
#3중 for문 대신 itertools 라이브러리 이용
#combinations()를 이용하여 li에서 3개의 정수를 뽑아 더한 값을 res에 저장
#더한 값이 중복될 수 있으므로 res를 set으로 생성하여 중복 제거
#5번째 큰 수 -> res를 내림차순으로 정렬한 후 4번 인덱스의 값
#set은 인덱스로 접근이 불가능하나 sorted로 정렬한 후 리스트로 반환되므로 인덱스로 접근 가능
#실행시간을 단축시키기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
import sys
from itertools import combinations
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = list()
T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    res = set()
    for c in combinations(li, 3):
        res.add(sum(c))
    res = sorted(res, reverse=True)
    ans.append(f'#{tc} {res[4]}')
for a in ans:
    print(a)
