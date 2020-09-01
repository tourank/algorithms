import math

def combination_sum(nums, target):
    sols = [0] * target
    sols[0] = 1
    for i in range(1,len(sols)):
        sols[i] = sols[i-1] + math.pow(2,i)

    return int(sols[target-2])

print(combination_sum([1,2,3,4], 5))

def min_path_sum(grid):

    for row in range(len(grid)-1, -1, -1):
        for col in range(len(row)-1, -1, -1):

            cost += min(grid[row-1][col], grid[row][col-1])


def min_cost_stairs(steps):

    cost = 0
    for i in range(2,len(steps)):
        cost[i] += min(steps[i-1], steps[i-2])

    return min(cost[len(steps)-1], cost[len(steps)-2])


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

def max_profit(prices):

    min_price = float("inf") 
    max_price = 0
    index = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        else:
            max_price = max(max_price, prices[i] - min_price)

    return max_price

def house_robber(nums):
    # keep track of cur_max and prev_max 
    # loop over array at each i check if i + prev_max > cur_max. if so then update cur_max and prev_max

    cur_max = max(nums[0], nums[1])
    prev_max = min(nums[0], nums[1])
    total = 0

    for i in range(2, len(nums)):

        total = max(cur_max, prev_max + nums[i])
        prev_max = cur_max
        cur_max = total

    return cur_max

       
