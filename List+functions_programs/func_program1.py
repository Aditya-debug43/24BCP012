def count_lower_upper(s):
    d = {'lower': 0, 'upper': 0}
    for c in s:
        if c.islower():
            d['lower'] += 1
        elif c.isupper():
            d['upper'] += 1
    return d
print(count_lower_upper("HelloWorld"))