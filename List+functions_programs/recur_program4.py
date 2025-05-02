def rev(lst):
    if not lst:
        return []
    return [lst[-1]] + rev(lst[:-1])
print(rev([1, 2, 3, 4]))