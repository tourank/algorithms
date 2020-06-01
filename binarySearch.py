import pdb

def binarySearch(array, target, low, high):
    
    mid = (high + low)//2
    if low > high:
        return -1
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        return binarySearch(array, target,mid+1,high)
    else: 
        return binarySearch(array, target, low, mid-1)

array = [0,1,21,33,45, 45, 61, 71, 72, 73]
target = 60
print(binarySearch(array, target, 0, len(array)-1)
