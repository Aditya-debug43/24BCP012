def to_lower(s):
    result = ""
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

def to_upper(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

def toggle_case(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        elif 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

s = input()
print("Lower:", to_lower(s))
print("Upper:", to_upper(s))
print("Toggle:", toggle_case(s))