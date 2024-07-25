def binarySearch(array, num):
    length = len(array)
    i = 0
    j = length - 1
    while i <= j:
        middle = (i + j) // 2
        if array[middle] == num:
            return middle
        elif num < array[middle]:
            j = middle - 1
        else:
            i = middle + 1    
    return -1

array = [3, 7, 8, 12, 15, 18, 27, 29, 32, 36]
num = 12
print(binarySearch(array, num))
