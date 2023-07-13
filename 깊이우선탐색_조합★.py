#L은 트리의 레벨 및 res의 인덱스, s는 반복문을 시작하는 숫자
#s부터 n까지 가지가 뻗어나감
#DFS를 호출할 때 현재 돌고있는 반복문의 i에 +1한 값을 s값으로 넘겨줌
#cnt += 1에서 cnt를 지역변수로 인식하여 에러가 발생할 수 있으므로 global로 cnt가 전역변수임을 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, s):
    global cnt
    if L == m:
        print(*res)
        cnt += 1
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)
