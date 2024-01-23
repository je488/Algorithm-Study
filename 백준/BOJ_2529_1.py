import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def ok(num):
    for i in range(k):
        if a[i] == '<':
            if num[i] > num[i+1]:
                return False
        elif a[i] == '>':
            if num[i] < num[i+1]:
                return False
    return True

def go(index, num):
    if index == k+1:
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        check[i] = True
        go(index + 1, num + str(i))
        check[i] = False

k = int(input())
a = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])