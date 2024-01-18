#암호를 사전식으로 출력해야 하므로 사용 가능한 알파벳 리스트 alpha를 미리 오름차순으로 정렬
#alpha의 각각의 알파벳을 사용할지, 사용하지 않을지 선택
#i는 사용할지 말지 결정해야 하는 alpha의 인덱스
#password는 현재까지 만든 암호
#알파벳을 사용하는 경우 password에 i번째 알파벳을 추가(password + alpha[i])
#알파벳을 사용하지 않는 경우 password는 그대로 유지
#password의 길이가 n과 같은 경우 암호 1개 완성
#check 함수로 password가 최소 1개의 모음과 최소 2개의 자음으로 구성되어 있는지 확인
#i >= len(alpha)이면 암호의 길이가 n이 되지 않았지만 더 이상 선택할 수 있는 알파벳이 없는 경우
#i는 1씩 증가하므로 alpha의 길이보다 커지는 경우는 없음 -> i == len(alpha)도 가능
#하나의 함수가 2개의 함수를 호출하고 함수의 깊이는 최대 C -> 2^C
#하나의 암호를 생성하면 check 함수를 호출하여 password의 글자를 하나씩 체크 -> L(password 길이)
#따라서 총 시간복잡도는 O(2^C * L)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(password):
    ja = 0
    mo = 0
    for p in password:
        if p in "aeiou":
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i + 1)
    go(n, alpha, password, i + 1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
go(l, alpha, "", 0)
