# [2,3,1,-4,-4,2]
# if you start at 1 then true 

def next_index(cur, array):
    jump = array[cur]
    index = (cur + jump) % len(array)
    return index 

def single_cycle(array):

    visited = 0
    cur = 0

    while visited < len(array):
        if visited > 0 and cur == 0:
            return False
        visited += 1
        cur = next_index(cur, array)

    return cur == 0

       

print(single_cycle([2,3,1,-4,-4,2]))
print(single_cycle([2,2,-1]))

