import random

a = -1
b = -1


def partition(arr, left, right):
    pivot = arr[right]
    ind = left
    j = left
    while j < right:
        if arr[j] < pivot:
            arr[ind], arr[j] = arr[j], arr[ind]
            ind += 1
        j += 1
    arr[ind], arr[right] = arr[right], arr[ind]
    return ind


# def random_partition(arr, left, right):
#     n = right - left + 1
#     pivot = random.randrange(1, 100) % n
#     arr[left + pivot], arr[right] = arr[right], arr[left + pivot]
#     return partition(arr, left, right)


def median_check(arr, left, right,
                 med_ind, a1, b1):
    global a, b

    if (left <= right):
        partitionIndex = partition(arr, left, right)
        # partitionIndex = random_partition(arr, left, right)
        if (partitionIndex == med_ind):
            b = arr[partitionIndex]
            if (a1 != -1):
                return

        # If index = k - 1, then we get
        # a & b as middle element of
        # arr[]
        elif (partitionIndex == med_ind - 1):
            a = arr[partitionIndex]
            if (b1 != -1):
                return

        # If partitionIndex >= k then
        # find the index in first half
        # of the arr[]
        if (partitionIndex >= med_ind):
            return median_check(arr, left, partitionIndex - 1, med_ind, a, b)

        # If partitionIndex <= k then
        # find the index in second half
        # of the arr[]
        else:
            return median_check(arr, partitionIndex + 1, right, med_ind, a, b)

    return


def find_median(arr, n):
    global a
    global b
    # a = -1
    # b = -1

    if n % 2 == 0:
        median_check(arr, 0, n - 1, n // 2, a, b)
        med = (a + b) // 2
    else:
        median_check(arr, 0, n - 1, n // 2, a, b)
        med = b

    return med


arr = [12, 3, 5, 2, 4, 19, 26]
print(find_median(arr, len(arr)))
