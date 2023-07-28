#L은 레벨 및 coin의 인덱스이고 a, b, c는 사람 3명의 금액의 합
#각각의 동전마다 3명에게 나누어 줄 수 있으므로 3개의 가지로 뻗어나가는 상태트리
#L == n일 경우 즉, 모든 동전을 분배한 경우 3명의 금액의 합이 모두 다른지 if문으로 체크
#3명의 금액의 합이 모두 다를 경우 금액의 최댓값과 최솟값의 차 구하기
#구한 값(최댓값-최솟값)이 이전에 구한 답(res)보다 작을 경우 res의 값을 바꿔 최소차 구하기
#res = cha에서 res를 지역변수로 인식 -> if cha < res에서 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, a, b, c):
    global res
    if L == n:
        if a != b and b != c and c != a:
            cha = max(a, b, c) - min(a, b, c)
            if cha < res:
                res = cha
    else:
        DFS(L+1, a+coin[L], b, c)
        DFS(L+1, a, b+coin[L], c)
        DFS(L+1, a, b, c+coin[L])
if __name__ == '__main__':
    n = int(input())
    coin = list()
    for _ in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0, 0, 0, 0)
    print(res)
