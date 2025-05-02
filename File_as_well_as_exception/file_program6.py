with open("fileA.txt", "w") as f:
    f.write("Line1A\nLine2A\nLine3A")
with open("fileB.txt", "w") as f:
    f.write("Line1B\nLine2B")
with open("fileA.txt") as f1, open("fileB.txt") as f2, open("merged.txt", "w") as f3:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1):
            f3.write(lines1[i])
        if i < len(lines2):
            f3.write(lines2[i])