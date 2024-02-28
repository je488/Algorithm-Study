import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def binary_search(i):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if li1[mid] == i:
            return True
        elif li1[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
li1 = list(map(int, input().split()))
li1.sort()
m = int(input())
li2 = list(map(int, input().split()))
for i in li2:
    if binary_search(i):
        print(1)
    else:
        print(0)