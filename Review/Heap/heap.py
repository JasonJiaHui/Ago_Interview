
class Heap:

    # index start from 1
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # crete MinHeap
    def percUp(self, i):
        while i // 2:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]

            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        small = i
        left = i * 2
        right = i * 2 + 1

        if left < self.currentSize and self.heapList[left] < self.heapList[small]:
            small = left
        if right < self.currentSize and self.heapList[right] < self.heapList[small]:
            small = right

        if small != i:
            self.heapList[small], self.heapList[i] = self.heapList[i], self.heapList[small]
            self.percDown(small)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[-1]
        self.heapList.pop()
        self.currentSize -= 1

        self.percDown(1)


def heapify(arr, i, n):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
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
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

if __name__ == '__main__':

    arr = [1,5,3,6,9,2]

    heapSort(arr)

    print "res:", arr

