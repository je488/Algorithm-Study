#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT(문제링크)
#L은 트리의 레벨 및 info의 인덱스, sum은 맛에 대한 점수의 합, cal은 칼로리의 합
#각 재료를 햄버거에 포함시키는 경우와 포함시키지 않는 경우로 나눠 2개의 가지로 뻗어나감
#칼로리의 합(cal)이 주어진 제한 칼로리보다 커지는 경우 return -> cut
#sum이 기존에 구한 점수의 최댓값(res)보다 크면 res값을 sum으로 바꿔주기
#res = sum에서 res를 지역변수로 인식 -> if sum > res에서 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum, cal):
    global res
    if cal > l:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+info[L][0], cal+info[L][1])
        DFS(L+1, sum, cal)
if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        n, l = map(int, input().split())
        info = list()
        res = 0
        for _ in range(n):
            s, c = map(int, input().split())
            info.append([s, c])
        DFS(0, 0, 0)
        print(f'#{tc} {res}')
