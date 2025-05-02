def frequency(s):
    d = {}
    for word in s.split():
        d[word] = d.get(word, 0) + 1
    return dict(sorted(d.items()))
print(frequency("this is a test this is only a test"))