#gcd는 최대공약수, lcm은 최소공배수
#최대공약수는 유클리드 호제법을 이용하여 구하기
#a % b가 r일 때 GCD(a, b) = GCD(b, r)이며 r이 0이면 그 때의 b가 최대 공약수
#재귀함수를 이용하여 b가 0이면 a를 리턴하고 그렇지 않으면 위의 식에 따라 GCD(b, a % b)를 리턴
#최소공배수는 gcd * (a / gcd) * (b / gcd) = a * b / gcd
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
a, b = map(int, input().split())
gcd = GCD(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)
