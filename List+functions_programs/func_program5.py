def ispangram(s):
    s = set(s.lower())
    return set("abcdefghijklmnopqrstuvwxyz").issubset(s)
print(ispangram("The quick brown fox jumps over the lazy dog"))