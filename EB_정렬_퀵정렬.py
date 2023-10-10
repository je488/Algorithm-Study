#이것이 취업을 위한 코딩테스트다 - 170p
#기준 데이터(피벗)를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치 바꾸기
#피벗을 리스트의 첫 번째 데이터로 설정
#왼쪽에서부터 피벗보다 큰 데이터를 찾고 오른쪽에서부터 피벗보다 작은 데이터 찾기
#피벗보다 큰 데이터와 작은 데이터의 위치를 서로 교환
#단, 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 엇갈린 경우(if left > right)
#작은 데이터와 피벗의 위치를 서로 교환
#정렬을 수행한 후 피벗을 기준으로 왼쪽과 오른쪽 리스트에서 각각 다시 정렬 수행 -> 재귀 함수
#start, end는 현재 리스트의 시작과 끝을 나타내는 인덱스
#left, right는 현재 리스트에서 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 인덱스
#start >= end인 경우 즉, 현재 리스트의 데이터 개수가 1개인 경우 return
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(start, right-1)
    quick_sort(right+1, end)
    
quick_sort(0, len(array)-1)
print(array)
