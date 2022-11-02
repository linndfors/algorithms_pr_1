def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr


def find_k_smallest(arr, ind):
    res = quick_sort(arr, 0, len(arr) - 1)
    return res[ind]


array = [10, 7, 8, 9, 1, 3]
print(find_k_smallest(array, 2))
