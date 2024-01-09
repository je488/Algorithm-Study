#어떤 수 N이 소수인지 아닌지 판별할 때의 시간복잡도 : O(√N)
#N개의 수에 대해 소수인지 아닌지 판별할 때의 시간복잡도 : O(N√N)
#위의 방법은 오랜시간이 걸리므로 다른 방법 필요 -> 에라토스테네스의 체
#0부터 MAX값까지 소수인지 아닌지 체크할 check 리스트 생성
#check의 인덱스가 소수이면 False, 소수가 아니면 True(0과 1은 소수가 아니므로 True)
#check에서 False인 값(소수인 값)을 찾아 그 배수에 해당하는 check값을 True로 바꾸기
#배수에 해당하는 check값을 바꿀 때 i * 2가 아닌 i * i부터 바꾸기
#i * i보다 작은 배수 값은 그 전에 이미 바꿔져 있음
#ex) i = 2일 때 check[2*2], check[2*3], check[2*4].... 순서로 지움
#ex) i = 3일 때 check[3*2], check[3*3], check[3*4].... 순서로 지움
#ex) check[3*2]는 앞에서 i = 2일 때 check[2*3]으로 이미 지워짐
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True
for i in range(2, MAX+1):
    if check[i] == False:
        j = i * i
        while j <= MAX:
            check[j] = True
            j += i
m, n = map(int, input().split())
for i in range(m, n+1):
    if check[i] == False:
        print(i)
