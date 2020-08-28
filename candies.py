def candy(candies, extra_candies):
    greatest = max(candies)
    result = []
    for k in candies:
        if k+extra_candies >= greatest:
            result.append(True)
        else:
            result.append(False)

    return result

print(candy([2,3,5,1,3],3))
print(candy([4,2,1,1,2],1))
print(candy([12,1,12],10))

