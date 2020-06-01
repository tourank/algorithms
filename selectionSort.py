def selectionSort(array):

    for i in range(len(array)):
        currentMin = array[i]
        for j in range(i+1,len(array)):
            if array[j] < currentMin:
                currentMin = array[j]
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]
    return array

array = [8,5,2,9,5,6,3]
print(selectionSort(array))
