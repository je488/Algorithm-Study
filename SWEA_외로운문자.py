#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXVJuEvqLAADFASe(문제링크)
#입력받은 문자열 s를 set()으로 중복을 제거한 상태에서 i로 문자를 하나씩 탐색
#i가 중복을 제거하지 않은 원래의 s에서 홀수개이면 2개씩 짝짓고 남는 문자이므로 li에 저장
#li가 0이면 즉, 같은 문자들이 모두 짝수개여서 짝짓고 남는 문자가 없는 경우 res에 Good 저장
#같은 문자들이 2개씩 짝짓고 남는 문자가 있는 경우 li에 있는 문자를 정렬한 뒤 res에 문자열로 저장
#실행시간을 단축하기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
ans = []
for tc in range(1, T+1):
    s = input().rstrip()
    li = []
    for i in set(s):
        if s.count(i) % 2 == 1:
            li.append(i)
    if len(li) == 0:
        res = 'Good'
    else:
        res = "".join(sorted(li))
    ans.append(f'#{tc} {res}')
for a in ans:
    print(a)
