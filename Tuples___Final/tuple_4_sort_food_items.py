items = [("Apple", 50), ("Banana", 30), ("Mango", 60)]
items.sort(key=lambda x: x[1], reverse=True)
print(items)