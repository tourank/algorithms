def moveElementToEnd(array, toMove):

    for i in range(len(array)):
        if array[i] == toMove:
            element = array.pop(i)
            array.append(element)
    return array
array = [2,1,2,2,2,3,4,2]
print(moveElementToEnd(array,2))
