#부분집합 하나를 만들어 합을 구하면 나머지 부분집합의 합도 구할 수 있음(주어진 리스트의 합 - 부분집합 하나의 합)
#L은 트리의 레벨 겸 리스트의 인덱스
#hap은 부분집합의 합으로 첫번째 DFS에서는 부분집합에 리스트의 값을 포함시키고 두번째 DFS에서는 값을 포함시키지 않음
#sys.exit(0)은 프로그램 종료
#시간복잡도 줄이기 위해 if hap > total // 2 사용
#hap이 다른 부분집합의 합과 같으려면 hap이 total의 절반 값이 되어야 함
#따라서 hap이 total의 절반보다 크면 더 이상 뻗어나갈 필요 없음 -> return
#if hap == (total - hap) 대신 if hap == (total // 2)를 사용할 경우, total이 홀수일 때 소수점이 삭제되어 YES로 출력될 수 있음
#total이 홀수일 경우, 답이 YES가 될 수 없음
import sys
# sys.stdin = open("input.txt", "r")
def DFS(L, hap):
    if hap > total // 2:
        return
    if L == n:
        if hap == (total - hap):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, hap+li[L])
        DFS(L+1, hap)

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    total = sum(li)
    DFS(0, 0)
    print("NO")
