def minIdx(start, array):
    minIndex = start
    length = len(array)
    for i in range(start + 1, length):
        if array[i] < array[minIndex]:
            minIndex = i
    return minIndex

def selectionSort(array):
    length = len(array)
    for i in range(length - 1): # last item of the array will be the largest after fixing n-1 items
        minIndex = minIdx(i, array)
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
            
array = [8, 10, 1, 3, 0, 0, 5, 7, -25, 5, -84, -197, 56]
selectionSort(array)
print(array)