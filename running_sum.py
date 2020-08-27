def running_sum_helper(lst, hd, result, total):

    if len(lst) == 0:
        return None

    running_sum_helper(lst[hd:],hd+1,result,total+lst[0])
    result.append(total)

def running_sum_recursive(lst,result):
    running_sum_helper(lst,0,result,0)
    return result


def running_sum(lst):

    sigma = 0
    result = []
    for i in lst:
        sigma += i
        result.append(sigma)
    return result


x = [1,2,3,4]
print(running_sum_recursive(x,[]))
