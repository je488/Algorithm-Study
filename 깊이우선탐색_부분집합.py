#n이 주어졌을 때 1부터 n까지 부분집합에 포함시킬지 말지를 배열에 append와 pop하는 것으로 표현
#부분집합에 포함시키는 경우, 포함시키지 않는 경우 -> 2가닥으로 뻗어나가는 상태 트리로 구성
#v가 n+1이 되면 배열 내용을 출력(단, 배열의 크기가 0이 아닌 경우)
#배열의 크기가 0인 경우 공집합인데 공집합은 출력하지 않음
import sys
# sys.stdin = open("input.txt", "r")
def DFS(v):
    if v == n+1:
        if len(ans) != 0:
            print(*ans)
    else:
        ans.append(v)
        DFS(v+1)
        ans.pop()
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    ans = []
    DFS(1)
