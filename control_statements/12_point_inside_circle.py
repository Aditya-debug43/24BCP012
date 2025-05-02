from math import sqrt
x, y = map(int, input().split())
r = int(input())
px, py = map(int, input().split())
distance = sqrt((px - x) ** 2 + (py - y) ** 2)
if distance < r:
    print("Inside the circle")
elif distance == r:
    print("On the circle")
else:
    print("Outside the circle")