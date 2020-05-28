def isValidSubsequence(array, sequence):

    i = 0
    k = 0
    recordIndex = 0
    count = 0
    while i < len(array):
        if sequence[k] == array[i] and k >= recordIndex:
            recordIndex = k
            k+=1
            count+=1
        i+=1     
    if count == len(sequence):
        return True
    else:
        return False

#array = [5,1,22,25,6,-1,8,10]
#sequence = [5,1,22,22,25,6,-1,8,10]
#array = [5,1,22,25,6,-1,8,10]
#sequence = [1,6,-1,10]
array = [1,2,3,4]
sequence = [4,1]
print(isValidSubsequence(array,sequence))
