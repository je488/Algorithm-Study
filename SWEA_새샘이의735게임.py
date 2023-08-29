#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ(문제링크)
#서로 다른 7개의 정수 중에서 3개의 정수를 순서 상관없이 고르기 -> 조합
#중복을 허용하지 않으므로 i는 0부터, j는 i+1부터, k는 j+1부터 시작
#3중 for문을 이용하여 3개의 정수를 뽑아 더한 값을 res에 저장
#더한 값이 중복될 수 있으므로 res를 set으로 생성하여 중복 제거
#5번째 큰 수 -> res를 내림차순으로 정렬한 후 4번 인덱스의 값
#set은 인덱스로 접근이 불가능하나 sorted로 정렬한 후 리스트로 반환되므로 인덱스로 접근 가능
#실행시간을 단축시키기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
ans = list()
T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    res = set()
    for i in range(7):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                res.add(li[i]+li[j]+li[k])
    res = sorted(res, reverse=True)
    ans.append(f'#{tc} {res[4]}')
for a in ans:
    print(a)
