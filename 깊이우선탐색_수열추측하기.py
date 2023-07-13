#가능한 n개의 수열을 모두 구하고(n!) 그 수열을 바탕으로 값을 더해갔을 때 f값이 나오는지 확인
#순열과 같은 방식으로 풀되, 두개씩 더했을 때 가장 마지막에 나오는 값을 구해야 하므로 이항계수 이용
#n개의 숫자를 두개씩 더해서 구한 f값은 n개의 숫자 각각에 이항계수를 곱한 뒤 모두 더한 값과 같음
#b리스트에 n값을 바탕으로 이항계수를 구함(조합 이용)
#sum은 n개의 수와 이항계수를 각각 곱한 값을 더해가면서(누적) 가장 밑에 있는 값을 구함
#답이 여러가지일 때, 사전순으로 첫번째 값만 출력해야 하므로 첫번째 li값 출력한 뒤 프로그램 종료
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, sum):
    if L == n and sum == f:
        print(*li)
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                li[L] = i
                ch[i] = 1
                DFS(L+1, sum + (li[L] * b[L]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    ch = [0] * (n+1)
    li = [0] * n
    b = [1] * n
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i
    DFS(0, 0)
