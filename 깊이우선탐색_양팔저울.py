#추를 양팔저울의 왼쪽에 놓는 경우(+), 오른쪽에 놓는 경우(-), 놓지 않는 경우(0)로 나누기(3개의 가지)
#L은 레벨 및 li의 인덱스, sum은 측정 가능한 물의 무게
#sum이 음수인 경우, 대칭되는 양수가 생기므로 고려할 필요 없음
#ex) 1과 5가 왼쪽, 7이 오른쪽인 경우(sum=1+5-7=-1)와 7이 왼쪽, 1과 5가 오른쪽인 경우(sum=7-1-5=1)
#res는 중복되는 값이 있을 수 있으므로 set()으로 생성
#ex)1만 왼쪽에 두고 5와 7은 놓지 않는 경우(sum=1), 7을 왼쪽에 두고 1과 5를 오른쪽에 두는 경우(sum=1)
#1부터 s사이의 모든 물의 무게 가지 수(s) - 측정이 가능한 물의 무게 가지 수(len(res)) -> 정답
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    if L == k:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+li[L])
        DFS(L+1, sum-li[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    k = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    res = set()
    DFS(0, 0)
    print(s - len(res))
