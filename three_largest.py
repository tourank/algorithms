def shiftArray(array, i, k):
    if k is not None:
        tmp = array[1]
        array[1] = array[2]
        array[0] = tmp
        array[2] = k
        return
    else:
        array[0] = array[1]
        array[1] = i
        return


def find(array):

    maxList = [0,0,0]
    index0 = 0
    index1 = 0
    for k in range(len(array)):
        if array[k] > maxList[2]:
            index0 = k
            # update index 3 and shift what was there to index 2, index 2 to to 3
            shiftArray(maxList, None, array[k])
        if k != index0 and array[k] <= maxList[2] and array[k] > maxList[1]: # [-,1,141] will shift left at 17 in array
            # shift number at index 2 to 3 then update index 2
            index1 = k
            shiftArray(maxList, array[k], None)
        if k != index1 and array[k]<= maxList[1] and array[k] > maxList[0]:
            maxList[0] = k
    return maxList 

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
#array = [10,5,9,10,12]
print(find(array))

