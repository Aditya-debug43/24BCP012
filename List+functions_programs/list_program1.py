import random
odd = random.sample(range(1, 100, 2), 5)
even = random.sample(range(2, 100, 2), 4)
odd[2] = even
print("Updated list:", odd)