#L은 레벨 및 ct(동전금액)와 cn(개수)의 인덱스, sum은 동전으로 만드는 금액
#동전의 금액별로 개수+1개의 가지로 뻗어나감(동전을 한개도 사용하지 않는 경우 포함)
#DFS를 호출할 때 동전의 금액(ct[L])과 사용할 개수(i)를 곱한 뒤 sum에 더해서 호출
#sum이 주어진 지폐의 금액(T)보다 커지면 return -> cut
#cnt += 1에서 cnt를 지역변수로 인식해 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(ct[L]*i))
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    ct = list()
    cn = list()
    for _ in range(k):
        p, n = map(int, input().split())
        ct.append(p)
        cn.append(n)
    cnt = 0
    DFS(0, 0)
    print(cnt)
