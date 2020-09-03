def get_all_subsets(s):
    subsets = []
    if len(s) == 0:
        subsets.append([])
    else:
        s_copy = s.copy()
        first_element = s_copy.pop(0)
        subsets += [x for x in get_all_subsets(s_copy)]
        subsets += [[first_element, *x] for x in get_all_subsets(s_copy)]
    return subsets

print(get_all_subsets([5, 7, 8]))


