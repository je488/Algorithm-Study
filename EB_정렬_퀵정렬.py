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
