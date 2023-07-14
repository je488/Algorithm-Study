#L은 레벨, s는 반복문을 시작하는 숫자, sum은 조합의 합
#조합의 합을 구해서 m의 배수인지 체크하면 되므로 조합을 저장할 리스트가 별도로 필요 없음
#주어진 n개의 정수에서 k를 뽑는 것이므로 n개의 정수를 리스트에 저장하고 탐색
#s부터 n-1까지 가지가 뻗어나감
#DFS호출 시, 현재 돌고있는 반복문의 i에 +1한 값을 s값으로 넘겨줌
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+li[i])

if __name__ == "__main__":
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
