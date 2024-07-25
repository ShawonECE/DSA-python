def bubbleSort(array):
    length = len(array)
    for i in range(length):
        isSwapped = False
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                isSwapped = True
        if not isSwapped:
            break

array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubbleSort(array)
print(array)
                