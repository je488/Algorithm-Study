#중복순열과 같은 방식으로 풀되 ch리스트를 사용하여 중복일 경우 가지가 뻗어나가지 못하게 함
#리스트에 값을 넣어 경우의 수를 만들 때 이미 사용한 수인지 ch리스트로 확인
#이미 사용한 수이면 ch[i]값이 1, 사용하지 않았으면 0(i는 수)
#리스트에 값을 넣을 때는 ch[i]의 값을 1로 바꿔 사용한 것을 표시
#DFS에서 다시 back했을 때(되돌아왔을 때)는 ch[i]의 값을 0으로 바꿔 다시 사용할 수 있게 함
#cnt += 1에서 지역변수로 인식하여 에러 발생할 수 있음 -> global로 cnt가 전역변수임을 알려줌
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
            if ch[i] == 0:
                li[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
if __name__ == "__main__":
   n, m = map(int, input().split())
   li = [0] * m
   ch = [0] * (n+1)
   cnt = 0
   DFS(0)
   print(cnt)
