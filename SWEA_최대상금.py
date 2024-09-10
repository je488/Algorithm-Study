#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD(문제링크)
#숫자판의 최대 자릿수는 6자리이고 최대 교환 횟수는 10번이므로 모든 경우의 수는 6C2^10
#따라서 모든 경우를 다 해보면 시간초과가 발생할 수 있으므로 중복되는 경우는 제외하고 완전 탐색
#a는 숫자판, n은 교환 횟수
#now에는 교환하기 전, nxt에는 교환한 후의 숫자판을 저장하고 중복을 제거하기 위해 set() 이용
#n번 교환해야 하므로 n만큼 반복하고 now가 비어있을 때까지 반복하며 숫자 교환
#1번 교환하고 나면 다음 교환을 위해 now에는 nxt, nxt에는 비어있는 set 할당
#n번을 교환한 뒤 가능한 모든 경우의 수는 now에 저장되어 있으므로 now에서 최댓값 찾기
#참고 : https://happybplus.tistory.com/352
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    a, n = input().split()
    n = int(n)
    now = set([a])
    nxt = set()
    for _ in range(n):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(a)-1):
                for j in range(i+1, len(a)):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    ans = max(map(int, now))
    print(f'#{tc} {ans}')
