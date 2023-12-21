#for문을 사용하여 0부터 (s의 길이-1)까지 10씩 증가하여 10개씩 출력
#s의 길이가 10으로 나누어 떨어지지 않아도 list index out of range 에러 없이 마지막까지 출력
#인덱싱과 달리 슬라이싱은 인덱스가 시퀀스의 범위를 넘어가면 None을 의미하는 []가 반환
#따라서 슬라이싱을 할 때 s의 길이를 넘어가면 에러 없이 s의 마지막 인덱스까지만 출력
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])
