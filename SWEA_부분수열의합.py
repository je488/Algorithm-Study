#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB(문제링크)
#n개의 자연수를 각각 부분 수열에 포함하거나 포함하지 않는 경우로 나누기
#i는 a의 인덱스, sum은 부분 수열의 합, ans는 정답
#부분 수열의 합이 k가 되면 ans를 1 증가시키고 return(return이 없으면 중복 계산됨)
#부분 수열의 합이 k가 되지 않았는데 i가 n이 되어 a를 모두 탐색한 경우 return
#DFS(i+1, sum+a[i])는 부분 수열에 a[i]를 포함하는 경우
#DFS(i+1, sum)은 부분 수열에 a[i]를 포함하지 않는 경우
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(i, sum):
    global ans
    if sum == k:
        ans += 1
        return
    if i == n:
        return
    DFS(i+1, sum+a[i])
    DFS(i+1, sum)

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    DFS(0, 0)
    print(f'#{tc} {ans}')
