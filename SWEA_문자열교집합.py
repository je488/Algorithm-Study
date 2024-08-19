#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Un3G64SUDFAXr(문제링크)
#cnt는 두 문자열 집합의 원소 개수를 더한 값
#set_cnt는 두 문자열 집합을 합친 후 set()을 이용하여 중복을 제거한 뒤 원소의 개수를 구한 값
#cnt는 두 문자열 집합을 단순히 합쳤을 때의 원소 개수(중복되는 문자열 원소 제거X)
#set_cnt는 두 문자열 집합을 합친 뒤 중복되는 문자열 원소를 제거했을 때의 원소 개수
#따라서 cnt - set_cnt는 두 문자열 집합에 모두 속하는 문자열 원소의 개수
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    dn = list(input().split())
    dm = list(input().split())
    cnt = n + m
    set_cnt = len(set(dn + dm))
    ans = cnt - set_cnt
    print(f'#{tc} {ans}')
