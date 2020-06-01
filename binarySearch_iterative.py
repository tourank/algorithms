def binarySearch(array, target):

    high = len(array)
    low = 0
    mid = (high + low)//2
    while(low <= high):
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            low = mid+1
            mid = (high + low)//2
        else:
            high = mid-1
            mid = (high + low)//2
    return -1

array = [0,1,21,33,45, 45, 61, 71, 72, 73]
target = 333
print(binarySearch(array,target))

