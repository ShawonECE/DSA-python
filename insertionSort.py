def insertionSort(array):
    length = len(array)
    for i in range(1, length):
        itemToInsert = array[i]
        j = i - 1
        while j >= 0 and array[j] > itemToInsert:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = itemToInsert

array = [8, 10, 1, 3, -6, 0, 5, 7, -25, 5, -84, -197, 56]
insertionSort(array)
print(array)