import random
nums = [random.randint(-50, 50) for _ in range(30)]
pos = [x for x in nums if x >= 0]
neg = [x for x in nums if x < 0]
print(pos)
print(neg)