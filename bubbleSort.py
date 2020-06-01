def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

array = [8,5,2,9,5,6,3]
print(bubbleSort(array))
