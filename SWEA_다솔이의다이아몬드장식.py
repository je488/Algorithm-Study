#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWSNw5jKzwMDFAUr(문제링크)
#s의 길이와 상관없이 행은 5개로 고정되어 있으므로 각 행의 규칙을 찾아 출력
#1행과 5행은 장식이 같으며 처음에 '.'이후 '.#..'이 s의 길이만큼 반복 -> s1
#2행과 4행도 장식이 같으며 처음에 '.'이후 '#.#.'이 s의 길이만큼 반복 -> s2
#3행은 처음(#.)과 마지막(.#)을 제외하고 각 문자 사이에 '.#.'이 있으므로 join 함수 이용 -> s3
#s1, s2, s3, s2, s1 사이에 줄바꿈을 구분자로 하여 1행부터 5행까지 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    s = input().rstrip()
    s1 = '.' + '.#..' * len(s)
    s2 = '.' + '#.#.' * len(s)
    s3 = '#.'+ '.#.'.join(s) + '.#'
    print(s1, s2, s3, s2, s1, sep = '\n')
