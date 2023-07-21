#날짜별로 잡힌 상담을 할 것인지, 말 것인지 2개의 가지로 뻗어나감(부분집합과 같은 방식)
#상담을 할 경우 상담을 진행하고 그 다음날로 이동, 상담을 안하면 다음날로 이동
#L은 날짜 및 T(걸리는 시간)와 P(얻을 수 있는 금액)의 인덱스, sum은 상담을 하고 받은 금액의 합
#n+1일에 휴가를 떠나므로 L이 n+1이 되면 종료
#T와 P의 인덱스는 날짜와 같기 때문에 인덱스 0에 0을 추가하여 1(첫째날)부터 탐색
#L+T[L]은 L번째날의 상담을 진행하고 그 다음날이므로 n+1(휴가를 떠나는 날)보다 작거나 같아야 함
#res = sum에서 res를 지역변수로 인식 -> if sum > res에서 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    res = -2147000000
    for _ in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)
