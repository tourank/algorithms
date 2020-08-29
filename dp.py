def climb_stairs(n):

    if n == 1:
        return 1

    steps = [0] * (n+1)
    steps[0] = 1
    steps[1] = 1

    for k in range(2,len(steps)):
        steps[k] = steps[k-1] + steps[k-2]

    return steps[n]

def coins(n, denoms):
    built_up = [2147483647] * (n+1)
    built_up[0] = 0
    for denom in denoms:
        for j in range(len(built_up)):
            if denom <= j:
                diff = j - denom
                built_up[j] = min(1 + built_up[diff], built_up[j])

    return built_up[n]


def max_subarray(nums):
    
    cur_max = nums[0] 
    global_max = nums[0]
    # at each index compute max 
    # [3,5,-9,1] = 3, 5 or 8, -9 or -1, 1 or 0
    for k in range(1,len(nums)):
        if cur_max > global_max:
            global_max = cur_max
        cur_max = max(nums[k],cur_max+nums[k])

    return global_max 


        
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
#print(max_subarray([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))
       

