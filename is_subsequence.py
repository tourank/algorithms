
def is_subsequence(s, t):

    if len(s) > len(t):
        return False

    i = 0
    j = 0
    while j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1

    return i == len(s)


print(is_subsequence("abc", "ahbgdc")) # True
print(is_subsequence("ace", "abcde")) # True
print(is_subsequence("aec", "abcde")) # False
print(is_subsequence("axc", "ahbgdc")) # False
print(is_subsequence("bb", "ahbgdc"))

