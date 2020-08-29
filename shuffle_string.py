def shuffle_string(s, indices):

    result = [None]*len(s)
    i = 0
    for index in indices:
        result[index] = s[i]
        i+=1

    string = ""
    for k in result:
        string += k

    return string

print(shuffle_string("codeleet",[4,5,6,7,0,2,1,3]))
print(shuffle_string("abc",[0,1,2]))
print(shuffle_string("aiohn",[3,1,4,2,0]))
