
######### 12.11 ########
#1
def binarySearch(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

'''
Rotated Brief Summary:
    
    compare arr[mid] <> arr[high]

    while low < high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < arr[high]:
            low = mid + 1
        else:
            high = mid
        ....
'''
#2
def minRotatedSearch(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            mid = high

    return arr[low]

#3 No Duplicated...
def searchRotatedArray(arr, target):

    # find Min
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + ((high-low) >> 1)
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    print "Min_value_index: ", low

    # Binary search based on min index
    if target < arr[-1]:
        print "search1: ", arr[low:]
        index = binarySearch(arr[low:], target)
        print "index1: ", index
        if index != -1:
            return low + index
        return index
    elif target > arr[-1]:
        index = binarySearch(arr[:low], target)
        return index
    else:
        return len(arr) - 1

# 4
# Contain duplicated ...
def searchRotatedArray2(arr, target):

    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == target:
            return True
        elif arr[mid] > arr[high]:
            if arr[mid] > target and target >= arr[low]:
                high = mid
            else:
                low = mid + 1
        elif arr[mid] < arr[high]:
            if arr[mid] < target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid
        else:
            high -= 1

    return True if arr[low] == target else False




'''
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]
'''
# 5
# duplicated count
def searchRange(arr, target):

    if not arr:
        return

    left = getLeft(arr, target)
    right = getRight(arr, target)

    return [left, right]


def getLeft(arr, target):
    low = 0
    high = len(arr) - 1

    leftIndex = -1
    flag = True
    while flag:
        while low <= high:
            mid = low + ((high - low) >> 1)
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                flag = True
                leftIndex = mid
                low = 0
                high = mid - 1

        flag = False

    return leftIndex

def getRight(arr, target):
    low = 0
    high = len(arr) - 1

    rightIndex = -1
    flag = True

    while flag:
        while low <= high:
            mid = low + ((high - low) >> 1)
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid +1
            else:
                flag = True
                rightIndex = mid
                low = mid + 1
                high = len(arr) - 1

        flag = False

    return rightIndex

# 6
# arr = [1,2,3,4,3,2,4,1]
def findPeakEle(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)
        mid2 = mid + 1
        if arr[mid] < arr[mid2]:
            low = mid + 1
        else:
            high = mid

    print arr[low]


'''
For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
# 7
def minSubArrayLen(arr, target):

    index = 0
    startIndex = 0
    length = len(arr)
    minLen = length + 1
    currentSum = 0

    while index < length:
        currentSum += arr[index]

        while currentSum >= target:
            print "startIndex: %d, index: %d " % (startIndex, index)
            minLen = min(minLen, index - startIndex + 1)
            print "minLen: ", minLen
            currentSum -= arr[startIndex]
            startIndex += 1

        index += 1
    print "minLen: ", minLen

# 8
'''
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
'''
def findClosestElements(arr, k, x):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid

    return arr[low:low+k]


# 9
# minK
'''
1.heap[suitable for bigdata]
2.use quickSort
'''
def minK(arr, low, high, k):
    if low >= high:
        return

    pivot = arr[low]
    i, j = low, high

    while i != j:
        while i < j and arr[j] > pivot:
            j -= 1
        while i < j and arr[i] < pivot:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    if i == k:
        return arr[:k]
    elif i > k:
        minK(arr, 0, i-1, k)
    else:
        minK(arr, i + 1, len(arr) - 1, k)


# 10
# overMean
def overMean(arr, low, high):
    if low >= high:
        return

    pivot = arr[low]
    i, j = low, high
    while i != j:
        while i < j and arr[j] > pivot:
            j -= 1
        while i < j and arr[i] < pivot:
            i += 1

        if i > j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]

    mid = len(arr) >> 1

    if i == mid:
        return arr[i]
    elif i < mid:
        return overMean(arr, i + 1, len(arr) - 1)
    else:
        return overMean(arr, 0, i - 1)


############ 11 and 12 can be the same type ############

# 11
# find duplicated number
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),

def findDuplicate(arr):

    low = 1
    high = len(arr) - 1

    while low < high:
        mid = low + ((high - low) >> 1)
        count = 0
        for ele in arr:
            if ele <= mid:
                count +=1
            else:
                break
        if count <= mid:
            low = mid + 1
        else:
            high = mid

    print arr[low]

# 12
'''
1-n  sorted array, drop one element, find it
arr = [1,3,4,5,6,7,8,9] => 2
l = 1 h = 9 mid = 5
l = 1 h = 5 mid = 3
l = 1 h = 3 mid = 2
l = 1 h = 2 mid = 1
l = 2 h = 2 break

arr = [1,2,3,4,5,7,8,9] => 6
l = 1 h = 9 mid = 5
l = 6 h = 9 mid = 7
l = 6 h = 7 mid = 6
l = 6 h = 6 break
'''
def findDropEle(arr):
    low = 1
    high = len(arr) + 1

    while low < high:
        mid = low + ((high - low) >> 1)
        if arr[mid - 1] <= mid:
            low = mid + 1
        else:
            high = mid

    print low





if __name__ == '__main__':

    # arr = [1,3,4,5,6,7,8,9]
    arr = [1,2,3,4,5,7,8,9]
    findDropEle(arr)


    # arr = [4,5,6,7,0,1,2]
    # arr = [4,0,1]
    # arr = [2, 3, 1, 2, 4, 3]
    # minSubArrayLen(arr, 7)

    # index = searchRotatedArray(arr, 1)

    # print "final: ", index
