def max_num(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_num(lst[1:]))
print(max_num([1, 5, 3, 9, 2]))