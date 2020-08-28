# Have an array built up from 0 to target amount, for each i compute its difference for each 
# denomination which gives you number of coins needed, then store that number at i in the built up array
# as you go through denoms, check if the difference is smaller than previous value in the built up array,
# if yes, update it again. at the end return the result at built_up_array[target-1]

def coins(n, denoms):
    built_up = [2147483647] * (n+1)
    built_up[0] = 0
    for denom in denoms:
        for j in range(len(built_up)):
            if denom <= j:
                diff = j - denom
                built_up[j] = min(1 + built_up[diff], built_up[j])

    return built_up[n]



print(coins(7,[1,5,10]))


