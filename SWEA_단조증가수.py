#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWcPjEuKAFgDFAU4(문제링크)
#n개의 수 중에서 2개씩 곱해 단조 증가하는 수인지 판별
#판별하기 위해 2개씩 곱한 수를 문자열로 바꾸어 각 숫자의 자릿수가 증가하는 지 체크
#하나라도 증가하지 않으면 break로 반복문 탈출 -> 단조 증가하는 수가 아님
#break없이 for문이 끝까지 실행됐을 경우 단조 증가하는 수이므로 res에 저장
#res의 길이가 0이면 단조 증가하는 수가 없으므로 -1 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    res = list()
    for i in range(n):
        for j in range(i+1, n):
            tmp = str(li[i] * li[j])
            for k in range(len(tmp)-1):
                if tmp[k] > tmp[k+1]:
                    break
            else:
                res.append(int(tmp))
    if len(res) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(res)}')
