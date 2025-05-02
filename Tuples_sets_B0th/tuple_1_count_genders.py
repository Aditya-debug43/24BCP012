lst = [("John",), ("Alice",), ("Bob",), ("Daisy",), "Emma", "Tom"]
boys = girls = 0
for ele in lst:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1
print("Boys:", boys)
print("Girls:", girls)