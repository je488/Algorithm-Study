#ps에는 문제를 풀었을 때의 점수, pt에는 문제를 푸는데 걸리는 시간 저장
#L은 레벨 및 ps와 pt의 인덱스, sum은 문제의 총점, time은 문제를 푸는데 사용한 시간
#주어진 n개의 문제를 푸는 경우와 풀지 않는 경우로 나눠 2개의 가지로 뻗어나감(부분집합과 같은 방식)
#L == n이되면 기존에 구한 res와 비교해서 크면 최대값 갱신하기
#문제를 푸는데 사용한 시간이 m을 넘기면 안되므로 time이 m보다 큰 경우 return
#res = sum에서 res를 지역변수로 인식 -> if sum > res에서 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+ps[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ps = []
    pt = []
    for _ in range(n):
        a, b = map(int, input().split())
        ps.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
