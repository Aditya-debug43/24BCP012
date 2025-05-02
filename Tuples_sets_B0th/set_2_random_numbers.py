import random
s = set(random.randint(15, 45) for _ in range(10))
count = sum(1 for x in s if x < 30)
s = {x for x in s if x <= 35}
print("Count less than 30:", count)
print("After deletion:", s)