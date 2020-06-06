def searchDifference(target, array):

    left = 0
    right = len(array)-1
    
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid+1
        else:
            right = mid - 1
    return left

def getDifference(array, val):

    if val == 0:
        return abs( abs(array[val]) - abs(array[val+1]) )
    elif val == len(array) - 1:
        return abs( abs(array[val]) - abs(array[val-1])) 

    else:
        difference1 = abs(abs(array[val]) - abs(array[val-1]))
        difference2 = abs(abs(array[val]) - abs(array[val+1]))
        return min(difference1, difference2)

def smallestDiff(arrayOne, arrayTwo):

    # Binary search and return index where element should be in list 
    minima = []
    arrayOne.sort()
    arrayTwo.sort()
    if len(arrayOne) >= len(arrayTwo):

        # searchDifference gives us where element should be, get difference gives us the smaller difference between L and R
        val = searchDifference(arrayOne[0], arrayTwo)
        print(val)
        minimum = getDifference(arrayTwo,val)
        print(minimum)
        for i in range(1, len(arrayOne)):
            # search function will find relevant index in arrayTwo and subtract L and R values, return min
            index = searchDifference(arrayOne[i], arrayTwo)
            value = getDifference(arrayTwo, index)
            if value < minimum: # if this difference smaller than previous min, append it to minima list
                minimum = value
                minima = []
                minima.append(arrayOne[i]) 
                minima.append(arrayTwo[index])
    else:
        minimum = searchDifference(arrayTwo[0], arrayOne)
        for i in range(1, len(arrayTwo)):
            index = searchDifference(arrayTwo[i], arrayOne)
            value = getDifference(arrayOne, index)
            if value < minimum:
                minimum = value
                minima = []
                minima.append(array[i])
                minima.append(array[index])
    return minima

arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]
print(smallestDiff(arrayOne, arrayTwo))
