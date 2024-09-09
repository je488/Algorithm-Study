#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD(문제링크)
#번호가 같으면 계속해서 소거하기 위해 스택 이용
#a를 하나씩 탐색하면서 ans가 비어있거나 ans의 top이 a의 번호와 다르면 ans에 push
#ans의 top이 a의 번호와 같으면 소거해야 하므로 ans에서 pop
#ans의 top과 번호를 비교하므로 번호 쌍을 소거하고 소거된 번호 쌍의 좌우 번호가 같으면 또 소거 가능
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = 10
for tc in range(1, T+1):
    n, a = input().split()
    n = int(n)
    ans = []
    for i in a:
        if len(ans) == 0 or ans[-1] != i:
            ans.append(i)
        else:
            ans.pop()
    print(f'#{tc}', ''.join(ans))
