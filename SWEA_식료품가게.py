#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYxCRFA6iiEDFASu(문제링크)
#a[i]가 4로 나누어 떨어지고 25% 할인한 가격이 a에 포함되어 있다면 a[i]는 물건의 정상가
#물건의 정상가를 a에서 pop하여 tmp에 저장해두고 a에서 25% 할인한 가격의 인덱스를 찾아 idx에 저장
#25% 할인한 가격을 a에서 pop하여 ans(정답)에 저장
#정상가와 할인가를 찾으면 모두 a에서 pop하므로 a가 비어있으면(모든 할인가를 찾으면) 반복문 종료
#a가 오름차순으로 주어지고 할인가를 앞에서부터 찾아 저장하므로 ans를 별도로 정렬할 필요X
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    while a:
        for i in range(len(a)):
            if a[i] % 4 == 0 and int(a[i]*0.75) in a:
                tmp = a.pop(i)
                idx = a.index(int(tmp*0.75))
                ans.append(a.pop(idx))
                break
    print(f'#{tc}', *ans)
