def climb_stairs(n):

    if n == 1:
        return 1

    steps = [0] * (n+1)
    steps[0] = 1
    steps[1] = 1

    for k in range(2,len(steps)):
        steps[k] = steps[k-1] + steps[k-2]

    return steps[n]


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
