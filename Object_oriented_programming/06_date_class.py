class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __eq__(self, other):
        return self.d == other.d and self.m == other.m and self.y == other.y

d1 = Date(1, 5, 2023)
d2 = Date(1, 5, 2023)
print(d1 == d2)