#1까지 26까지 반복문을 돌면서 코드의 한자리 혹은 두자리 숫자와 같은지 체크 -> 26개의 가지
#L은 code의 인덱스, P는 res(입력된 코드를 한자리 혹은 두자리 숫자로 나눠서 저장한 리스트)의 인덱스
#코드를 한자리 숫자로 보는 경우 DFS를 호출할 때 L+1, 두자리 숫자로 보는 경우 L+2
#코드를 두자리 숫자로 보는 경우 code[L]과 code[L+1]이 각각 i의 십의 자리와 일의 자리와 같은지 체크
#L이 code의 마지막 인덱스를 가리킬 때 코드를 두자리 숫자로 보는 경우 code[L+1] 탐색 불가능
#index out of range 에러가 발생할 수 있으므로 code에 -1을 추가
#-1은 에러는 발생하지 않지만 code[L+1] == i % 10에서 참이 될 수 없으므로 답에 영향을 주지 않는 값
#L == n이 되어 숫자를 문자로 바꿀 때 'A'는 65이므로 숫자에 64를 더한 뒤 chr() 이용하여 문자로 변환
#cnt += 1에서 cnt를 지역변수로 인식해 에러 발생 -> global로 전역변수 표시
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end = '')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i // 10 and code[L+1] == i % 10:
                res[P] = i
                DFS(L+2, P+1)

if __name__ == '__main__':
    code = list(map(int, input().rstrip()))
    n = len(code)
    code.append(-1)
    res = [0] * n
    cnt = 0
    DFS(0, 0)
    print(cnt)
