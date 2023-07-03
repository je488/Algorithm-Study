#lt, rt는 리스트에서 왼쪽 맨끝, 오른쪽 맨끝의 인덱스를 표시하는 포인터 변수
#lt가 rt보다 커지면 반복 멈춤
#last는 수열의 마지막 값(가장 최근에 들어온 값)으로 li[lt], li[rt]는 last보다 커야 함
#tmp에 (값, 왼오정보)를 넣어 값에 의해 정렬한 후 첫번째 값(더 작은 값)을 수열에 추가하고 last값 변경
#tmp에 아무것도 없는 경우는 왼쪽, 오른쪽 값 모두 수열을 만들 수 없는 것므로 break
#수열에 값을 추가할 때 왼쪽인 경우 lt에 1을 더해 다른 값을 가리키게 함(오른쪽인 경우 rt에서 1을 빼기)
#값이 하나만 남고(lt == rt) 수열에 추가할 수 있는 경우에도 tmp에 넣고 정렬하면 L이 먼저 나오므로 문제 없음
import sys
# sys.stdin = open("input.txt", "r")
n = int(input())
li = list(map(int, input().split()))
lt = 0
rt = n-1
res = ''
last = 0
tmp = []
while lt <= rt:
    if li[lt] > last:
        tmp.append((li[lt], 'L'))
    if li[rt] > last:
        tmp.append((li[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
        last = tmp[0][0]
    tmp.clear()
print(len(res))
print(res)
