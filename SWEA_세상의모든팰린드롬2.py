#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQAz7IqAH8DFAWh(문제링크)
#세상의모든팰린드롬1의 '?'와 달리 '*'는 0 이상의 알파벳으로 대체 가능
#따라서 for문으로 s를 탐색할 때 문자와 대칭되는 문자 중 하나라도 '*'이면 팰린드롬이므로 break
#문자와 대칭문자 둘다 '*'가 아니고 둘이 서로 다른 경우 팰린드롬이 아니므로 res값 변경 후 break
#s에 '*'가 없고 팰린드롬인 경우 for문 내의 if문을 모두 만족하지 않음 ex) s = 'pip'
#따라서 res의 초기값인 Exist가 그대로 정답이 됨
#처음 풀이는 s에 '*'이 있는 경우와 없는 경우로 나눠 있는 경우에는 s[0]과 s[-1]만 비교했으나 오답
#s = 'ab*ca'인 경우 팰린드롬이 아니지만 s[0]과 s[-1]이 같은 값이므로 팰린드롬으로 인식
#따라서 for문으로 s를 탐색하며 대칭되는 문자를 비교하여 팰린드롬이 맞는지 체크해야 함
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    s = input().rstrip()
    res = 'Exist'
    for i in range(len(s)//2):
        if s[i] == '*' or s[-1-i] == '*':
            break
        if s[i] != s[-1-i]:
            res = 'Not exist'
            break
    print(f'#{tc} {res}')
