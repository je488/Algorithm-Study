#v는 노드번호, path는 방문경로
#주어진 연결정보를 이용하여 인접행렬(g) 생성(방향그래프이므로 주어진 행과 열에 1 넣기)
#한 번 방문한 노드는 다시 방문할 수 없으므로 ch리스트로 방문여부 체크
#1번부터 n번노드까지 사용하므로 행과 열이 n+1인 리스트 생성(인덱스 0번은 사용하지 않음)
#n가지로 뻗어나가면서(1~n) 현재 노드와 연결되어있는지, 방문한 적 없는지 확인
#DFS를 호출할 때 v에 돌고있는 반복문의 i(방문할 노드 번호)를 넘겨줌
#DFS를 호출하기 전에 ch에 1로 방문표시, path에 방문할 노드번호 저장
#DFS에서 다시 back했을 때 ch값을 0으로 바꿔 다른 경로에서 방문할 수 있게 함(path에서도 노드 삭제)
#res += 1에서 res를 지역변수로 인식하여 에러 발생할 수 있으므로 global로 res가 전역변수임을 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(v):
    global res
    if v == n:
        res += 1
        print(*path)
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    res = 0
    path = []
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    ch[1] = 1
    path.append(1)
    DFS(1)
    print(res)
