class Solid:
    def __init__(self, shape, *params):
        self.shape = shape
        self.params = params

    def area_volume(self):
        if self.shape == "cube":
            a = self.params[0]
            return 6*a*a, a**3
        elif self.shape == "cuboid":
            l, b, h = self.params
            return 2*(l*b + b*h + h*l), l*b*h

s1 = Solid("cube", 3)
print(s1.area_volume())
s2 = Solid("cuboid", 2, 3, 4)
print(s2.area_volume())