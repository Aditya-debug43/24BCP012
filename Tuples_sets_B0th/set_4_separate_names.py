names = {"Alice", "Andrew", "Bob", "Bella", "Alex", "Ben"}
set_a = set()
set_b = set()
for name in names:
    if name.startswith("A"):
        set_a.add(name)
    elif name.startswith("B"):
        set_b.add(name)
print("A:", set_a)
print("B:", set_b)