#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXAdrmW61ssDFAXq(문제링크)
#L은 레벨 및 word의 인덱스, str은 단어를 합쳐서 만든 문자열
#주어진 단어를 str에 더하는 경우와 더하지 않는 경우로 나눠 2개의 가지로 뻗어나감
#L이 n이 되면 set()으로 str의 중복된 알파벳 제거 -> 길이가 26(알파벳 소문자 개수)이면 res += 1
#res += 1에서 res를 지역변수 인식하여 에러가 발생할 수 있음 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, str):
    global res
    if L == n:
        s = set(str)
        if len(s) == 26:
            res += 1
    else:
        DFS(L+1, str + word[L])
        DFS(L+1, str)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    word = [input().rstrip() for _ in range(n)]
    res = 0
    DFS(0, '')
    print(f'#{tc} {res}')
