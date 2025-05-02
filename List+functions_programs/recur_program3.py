def count(s):
    if not s:
        return 0
    return 1 + count(s[1:])
print(count("hello"))