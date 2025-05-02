def sanitize(s):
    if not s:
        return s
    if s[0].isspace():
        return "_" + sanitize(s[1:])
    return s[0] + sanitize(s[1:])
print(sanitize("This is a test"))