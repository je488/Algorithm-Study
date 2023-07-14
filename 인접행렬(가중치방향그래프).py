#그래프는 노드와 간선의 집합
#간선에 방향(화살표)이 설정되어 있으면 방향그래프, 간선에 값까지 설정되어 있으면 가중치 방향그래프
#그래프를 코드로 표현하기 위해 2차원 리스트 사용(0으로 초기화), 리스트 인덱스가 노드 번호
#리스트에서 값이 0이면 노드가 연결되어 있지 않음
#인접행렬은 행에서 열로 이동
#ex)무방향 그래프에서 1 2가 입력되면 1번노드 -> 2번노드, 2번노드 -> 1번노드 둘 다 가능
#리스트에서 1행2열, 2행1열에 값 1이 들어감(연결 표시)
#가중치 방향 그래프의 경우, 1 대신 주어진 값이 리스트에 들어가고 방향이 정해져 있음
#ex)가중치 방향그래프에서 1 2 7이 입력되면 1번노드 -> 2번노드만 가능하고 리스트에서 1행2열의 값은 7
#1번에서 n번노드까지 표현하기 위해 행과 열이 n+1인 리스트 생성(인덱스번호 0 ~ n)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, value = map(int, input().split())
        res[a][b] = value
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(res[i][j], end=' ')
        print()
