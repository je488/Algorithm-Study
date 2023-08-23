#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn(문제링크)
#정류장은 총 5000개로 cnt의 인덱스는 정류장 번호, cnt의 값은 정류장을 지나가는 버스 노선의 개수
#n개의 버스 노선 범위를 입력받고 a부터 b까지 반복하며 cnt의 정류장 번호에 해당하는 값에 +1
#p개의 정류장 번호를 입력받고 cnt에서 정류장 번호에 해당하는 값을 찾아 res에 저장 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 5001
    res = list()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            cnt[i] += 1
    p = int(input())
    for _ in range(p):
        c = int(input())
        res.append(cnt[c])
    print(f'#{tc}', *res)
