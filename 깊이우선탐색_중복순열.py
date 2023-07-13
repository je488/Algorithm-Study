#이진트리가 아닌 n가닥으로 뻗는 트리
#for문을 이용하여 n가닥으로 뻗음(1부터 n까지)
#m은 리스트의 크기, L은 리스트의 인덱스로 m이 되면 리스트 출력하고 cnt(경우의 수)+1
#cnt는 global 사용하여 main에 있는 전역변수 cnt임을 표시
#input = sys.stdin.readline은 대량 입력 시 입력 속도가 빨라짐
#단, input()으로 문자열 읽을 때 줄바꿈 기호까지 읽으므로 input().rstrip()으로 제거
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L):
    global cnt
    if L == m:
        print(*li)
        cnt += 1
    else:
        for i in range(1, n+1):
            li[L] = i
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    li = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
