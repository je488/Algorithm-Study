#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYtrCJQaDb4DFAR-(문제링크)
#여러 문자열을 합쳐서 팰린드롬 문자열을 만들기 위해서는 팰린드롬인 문자열이 가운데 하나만 존재
#즉, 팰린드롬인 문자열이 아무리 많아도 한 개만 사용가능
#yPal은 팰린드롬인 문자열을 저장한 리스트, nPal은 팰린드롬이 아닌 문자열을 저장한 리스트
#yPal의 길이가 1 이상이면 즉, 팰린드롬인 문자열이 한 개 이상이면 ans += m(한 개만 사용가능하므로)
#nPal에서 문자열을 하나씩 탐색하면서 현재 문자열을 뒤집은 것이 nPal에 존재하면 ans += m
#ex) nPal = ['aab', 'baa'], ans = 0일 때
#ex) 'aab'를 탐색할 때 'aab'를 뒤집은 것과 같은 'baa'가 nPal에 존재하므로 ans += 3
#ex) 'baa'를 탐색할 때 'baa'를 뒤집은 것과 같은 'aab'가 nPal에 존재하므로 ans += 3
#ex) 'aab'와 'baa'를 합친 'aabbaa'가 팰린드롬이 되므로 ans = 6
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    yPal = []
    nPal = []
    for _ in range(n):
        s = input().rstrip()
        if s == s[::-1]:
            yPal.append(s)
        else:
            nPal.append(s)
    ans = 0
    if len(yPal) >= 1:
        ans += m
    for i in nPal:
        if i[::-1] in nPal:
            ans += m
    print(f'#{tc} {ans}')
