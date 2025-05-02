import random
nums = [random.randint(1, 30) for _ in range(50)]
nums = list(set(nums))
print(nums)