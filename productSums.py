def productSum(array, multiplier):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) == list:
            multiplier+=1
            sum += productSum(array[i], multiplier) # returns sum so valid to add
        else:
            sum += multiplier * array[i] # Can think of this as base case, i.e. if integer just add
    return sum

array = [1, 2, [3,4]]
print(productSum(array, 1))


