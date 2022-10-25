def has_subls(ls, subls):
    if (set(subls) & set(ls)) == set(subls):
        return True
    elif len(ls) != len(subls):
        return False
    elif len(ls) == 0:
        return True
    elif ls[0] != subls[0]:
        return False
    else:
        return has_subls(ls[1:], subls[1:])


print(has_subls([], []))
print(has_subls([3, 3, 2, 1], []))
print(has_subls([], [3, 3, 2, 1]))
print(has_subls([3, 3, 2, 1], [3, 2, 1]))
print(has_subls([3, 2, 1], [3, 2, 1]))
