def count_alpha_digits(s):
    d = {'alpha': 0, 'digit': 0}
    for c in s:
        if c.isalpha():
            d['alpha'] += 1
        elif c.isdigit():
            d['digit'] += 1
    return d
print(count_alpha_digits("abc123"))