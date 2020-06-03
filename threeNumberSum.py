def threeNumberSum(array, target):

    array.sort()
    totals = []
    targets = []
    for i in range(len(array)):
        l = i+1
        r = len(array)-1
        while l < r:
            total = array[i] + array[l] + array[r]
            if total < target:
                l+=1
            elif total > target:
                r -=1
            if total == target:
                targets.append(array[i])
                targets.append(array[l])
                targets.append(array[r])
                totals.append(targets)
                l+=1
                r-=1
                targets = []
    return totals

array = [12,3,1,2,-6,5,-8,6]
print(threeNumberSum(array,0))


        

