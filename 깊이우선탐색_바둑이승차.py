#합이같은부분집합과 같은 방식으로 풀기
#부분집합의 합이 C(무게제한)보다 클 경우, return -> cut
#Time Limit 방지를 위해 Cut Edge 필요
#thap은 지금까지 판단한 무게의 합(부분집합 포함여부와 관계없이 무조건 지금까지 판단한 무게를 더함)
#total - thap은 전체 무게들 중 앞으로 판단해야할 무게의 합
#hap + (total - thap) -> 현재까지 만든 부분집합의 합 + 앞으로 판단할 무게의 합
#즉, 앞으로 판단할 무게를 모두 부분집합에 포함한다고 가정했을 때의 무게의 합
#hap + (total - thap)이 res(지금까지 부분집합의 합 중 최대값, 기존의 답)보다 작다면
#더이상 탐색할 필요가 없음(어차피 답이 될 수 없으므로) -> cut
#res는 res = hap으로 재할당하므로 지역변수로 인식 -> if hap > res 부분에서 초기화를 하지 않았는데 참조 -> 에러 발생
#global 키워드로 main에 있는 전역변수 res임을 표시
import sys
# sys.stdin = open("input.txt", "r")
def DFS(L, hap, thap):
    global res
    if hap + (total - thap) < res:
        return
    if hap > c:
        return
    if L == n:
        if hap > res:
            res = hap
    else:
        DFS(L+1, hap + li[L], thap + li[L])
        DFS(L+1, hap, thap + li[L])
if __name__ == "__main__":
    c, n = map(int, input().split())
    li = [0] * n
    for i in range(n):
        li[i] = int(input())
    res = -2147000000
    total = sum(li)
    DFS(0, 0, 0)
    print(res)
