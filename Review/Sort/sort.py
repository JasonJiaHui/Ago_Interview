
# Brief summary of some common sort algorithm

def bubbleSort(arr):

    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def selectSort(arr):

    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


def merge(left, right):
    result = []

    i,j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    if i < len(left):
        result += left[i:]

    if j < len(right):
        result += right[j:]

    return result


def mergeSort(arr):
    length = len(arr)

    if length <= 1:
        return arr

    mid = length // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    merge(left, right)


def quickSort(arr, low, high):

    if low >= high:
        return

    pivot = arr[low]
    i = low
    j = high

    while i != j:
        while arr[j] >= pivot and i < j:
            j -= 1
        while arr[i] <= pivot and i < j:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    quickSort(arr, low, i - 1)
    quickSort(arr, i + 1, high)


# construct max heap
# index start from 0
def heapify(arr, i, n):

    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

    heapify(arr, largest, n)


def heapSort(arr):

    length = len(arr)
    if length <= 1:
        return

    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, i, length)

    for i in range(length - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

################### 12_11 Review ###################


def bubble11(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - 1 - i):
            if arr[j] >= arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


def insert11(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = arr[i]


def heapify11(arr, i, n):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify11(arr, largest, n)


def heapSort11(arr):
    length = len(arr)
    if length <= 1:
        return

    for i in range(length // 2 - 1, -1, -1):
        heapify11(arr, i, length)

    for i in range(length - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)


def quickSort11(arr, low, high):

    if low >= high:
        return
    pivot = arr[low]
    i = low
    j = high

    while i != j:
        while i < j and arr[j] > pivot:
            j -= 1
        while i < j and arr[i] < pivot:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    quickSort11(arr, low, i-1)
    quickSort11(arr, i+1, high)


def merge11(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]

    return result


def mergeSort11(arr):
    length = len(arr)

    if length <= 1:
        return

    mid = length // 2
    left = mergeSort11(arr[:mid])
    right = mergeSort11(arr[mid:])

    merge11(left, right)



if __name__ == '__main__':
    arr = [1,5,3,6,9,2]

    heapSort(arr)

    print "res:", arr
