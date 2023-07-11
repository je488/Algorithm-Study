#동전의 종류개수만큼 뻗어나가는 트리
#L은 트리의 레벨 및 사용한 동전의 개수
#동전의 종류가 큰 것부터 탐색했을 때 최소값이 나올 확률이 높으므로 동전의 종류 리스트 내림차순 정렬
#지금까지 구한 거스름돈의 합이 m보다 큰 경우 cut
#res(지금까지 구한 정답, 동전의 최소개수)보다 L(지금까지 사용한 동전의 개수 및 레벨)이 더 큰 경우
#어차피 답이 될 수 없으므로 cut
#res = L부분에서 res를 지역변수로 인식 -> if L > res에서 res를 초기화하지 않고 참조 -> 에러 발생
#global로 res가 main에 있는 전역변수임을 알려줌
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    coin.sort(reverse=True)
    DFS(0, 0)
    print(res)
