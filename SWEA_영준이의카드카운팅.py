#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIsY84KEPMDFAWN(문제링크)
#card는 겹치는 카드가 있는지 확인하기 위해 카드 정보(3자리 문자열)를 저장하는 리스트
#res는 무늬별로 부족한 카드 수를 표시하기 위한 딕셔너리
#s를 3자리씩 분리해서 card에 존재하지 않는 경우(겹치지 않는 경우) card에 저장
#또한 문자열의 첫 번째 문자(카드 무늬)에 해당하는 res의 값에 -1
#문자열이 card에 이미 존재하는 경우 겹치는 카드가 있는 것이므로 ERROR 출력 후 break
#break 없이 반복문이 종료된 경우, 겹치는 카드가 없는 것이므로 res의 value 값 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = input().rstrip()
    res = {'S':13, 'D':13, 'H':13, 'C':13}
    card = list()
    for i in range(0, len(s), 3):
        if s[i:i+3] in card:
            print(f'#{tc} ERROR')
            break
        else:
            card.append(s[i:i + 3])
            res[s[i]] -= 1
    else:
        print(f'#{tc}', *res.values())
