s1 = input()
s2 = input()
result = ""
i = 0
while i < len(s1):
    match = False
    for j in range(len(s2)):
        if i + j < len(s1) and s1[i + j] == s2[j]:
            match = True
        else:
            match = False
            break
    if match:
        i += len(s2)
    else:
        result += s1[i]
        i += 1
print(result)