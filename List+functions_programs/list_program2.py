import random
nums = [random.randint(1, 100) for _ in range(20)]
n = int(input())
positions = [i for i, x in enumerate(nums) if x == n]
print(positions)