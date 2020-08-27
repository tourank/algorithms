# Have an array built up from 0 to target amount, for each i compute its difference for each 
# denomination which gives you number of coins needed, then store that number at i in the built up array
# as you go through denoms, check if the difference is smaller than previous value in the built up array,
# if yes, update it again. at the end return the result at built_up_array[target-1]

def coins(n, denoms):


