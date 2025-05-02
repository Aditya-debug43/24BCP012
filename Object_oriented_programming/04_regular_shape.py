class Shape:
    def __init__(self, shape, *params):
        self.shape = shape
        self.params = params

    def calc(self):
        if self.shape == "square":
            a = self.params[0]
            return 4*a, a*a
        elif self.shape == "rectangle":
            l, b = self.params
            return 2*(l+b), l*b

s1 = Shape("square", 5)
print(s1.calc())
s2 = Shape("rectangle", 4, 6)
print(s2.calc())