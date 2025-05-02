def create_list(l1, l2):
    return [x for x in l1 if x in l2]
print(create_list([1, 2, 3], [2, 3, 4]))