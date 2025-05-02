def convert(s):
    words = list(set(s.split()))
    words.sort()
    return ' '.join(words)
print(convert("hello world hello python python code"))