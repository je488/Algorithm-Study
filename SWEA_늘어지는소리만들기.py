#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRKWITqfvIDFAV8(문제링크)
#주어진 문자열을 리스트로 저장하여 insert()로 주어진 위치(인덱스)에 '-' 삽입
#'-'을 한 번 이상 삽입한 경우 '-'을 제외한 문자열을 기준으로 주어진 위치에 '-'을 삽입해야 함
#주어진 위치 리스트 순서대로 '-'을 삽입할 경우, 문자열의 인덱스가 '-'을 삽입할 때 마다 변경
#따라서 주어진 위치 리스트를 내림차순으로 정렬하여 가장 큰 인덱스부터 '-' 삽입
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = list(input().rstrip())
    cnt = int(input())
    loc = sorted(list(map(int, input().split())), reverse=True)
    for l in loc:
        s.insert(l, '-')
    print(f'#{tc}', ''.join(s))
