s = input()
a = d = 0
for c in s:
    if c.isalpha():
        a += 1
    elif c.isdigit():
        d += 1
print("Alphabets:", a)
print("Digits:", d)