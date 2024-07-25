def ternarySearch(array, num):
    length = len(array)
    i = 0
    j = length - 1
    while i <= j:
        middle1 = (i + 2*j) // 3
        middle2 = (j + 2*i) // 3
        if array[middle1] == num:
            return middle1
        elif array[middle2] == num:
            return middle2
        elif num < array[middle1]:
            j = middle1 - 1
        elif num < array[middle2] and num > array[middle1]:
            i = middle1 + 1
            j = middle2 - 1
        else:
            i = middle2 + 1    
    return -1

array = [3, 7, 8, 12, 15, 18, 27, 29, 32, 36]
num = 29
print(ternarySearch(array, num))