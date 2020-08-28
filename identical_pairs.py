# [1,1,1,2,3,3]
# (1,1) = 1, (1,1,1): 2 + 1 = 3, (1,1,1,1) = 3 + 2 + 1 = 6, 

def identical_pairs(lst):
    pairs = {}
    num_pairs = 0
    for num in lst:
        if num in pairs:
            pairs[num] += 1
        else:
            pairs[num] = 1 
           
    for key in pairs:
        n = pairs[key]
        num_pairs += (n*(n-1))//2

    return num_pairs

print(identical_pairs([1,2,3,1,1,3]))
