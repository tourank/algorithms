def shuffle(array,n):

    j = n 
    i = 1
    while i < n:
        array[i], array[j] = array[j], array[i]
        j+=1

    return array 


print(shuffle([2,5,1,3,4,7],3))
print(shuffle([1,2,3,4,4,3,2,1],4))
print(shuffle([1,1,2,2],2))
