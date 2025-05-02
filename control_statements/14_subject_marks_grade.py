def get_grade(m):
    if m == -1:
        return "NA"
    elif m <= 39:
        return "F"
    elif m <= 44:
        return "P"
    elif m <= 49:
        return "C"
    elif m <= 54:
        return "B"
    elif m <= 59:
        return "B+"
    elif m <= 69:
        return "A"
    elif m <= 79:
        return "A+"
    else:
        return "O"

marks = []
total = 0
fail = False
for i in range(3):
    m = input()
    if m.lower() == "absent":
        marks.append(-1)
        continue
    m = int(m)
    if m <= 39:
        fail = True
    marks.append(m)
    total += m

average = total / 3
for i, m in enumerate(marks):
    if m == -1:
        print(f"Subject {i+1}: NA")
    else:
        print(f"Subject {i+1}: {get_grade(m)}")

print("Total:", total)
print("Average:", average)
if fail:
    print("Result: Fail")
else:
    print("Result: Pass")