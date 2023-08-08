#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS(문제링크)
#십진수를 이진수로 변환할 때 가장 처음 2로 나눈 나머지가 마지막 비트가 됨
#따라서 이진수의 마지막 n비트가 1이 되려면 십진수를 n번동안 2로 나눴을 때 나머지가 모두 1이어야 함
#m을 2로 나누는 과정을 n번 반복하고 도중에 나머지가 0이 되는 경우 ans에 tc와 OFF 저장 후 break
#반복문이 break없이 끝까지 실행됐을 경우, 나머지가 모두 1이므로 ans에 tc와 ON 저장
#실행시간을 단축시키기 위해 정답을 ans배열에 저장한 후 한꺼번에 출력
ans = list()
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if m == 0:
        ans.append(f'#{tc} OFF')
    else:
        for _ in range(n):
            if m % 2 == 0:
                ans.append(f'#{tc} OFF')
                break
            m = m // 2
        else:
            ans.append(f'#{tc} ON')
for a in ans:
    print(a)
