import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def insert(val):
    heap.append(val)
    idx = len(heap) - 1
    while idx > 1:
        parent = idx // 2
        if heap[parent] < val:
            heap[idx] = heap[parent]
            idx = parent
        else:
            break
    heap[idx] = val

def delete():
    if len(heap) == 1:
        return -1
    res = heap[1]
    tmp = heap[-1]
    idx = 1
    while idx * 2 < len(heap) - 1:
        if heap[idx * 2] > heap[idx * 2 + 1]:
            cidx = idx * 2
        else:
            cidx = idx * 2 + 1
        if tmp < heap[cidx]:
            heap[idx] = heap[cidx]
            idx = cidx
        else:
            break
    heap[idx] = tmp
    heap.pop()
    return res

T = int(input())
for tc in range(1, T+1):
    heap = [0]
    n = int(input())
    ans = list()
    ans.append('#' + str(tc))
    for _ in range(n):
        calc, *val = map(int, input().split())
        if calc == 1:
            insert(val[0])
        elif calc == 2:
            res = delete()
            ans.append(res)
    print(*ans)