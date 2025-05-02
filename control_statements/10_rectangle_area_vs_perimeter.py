l = int(input())
b = int(input())
area = l * b
perimeter = 2 * (l + b)
if area > perimeter:
    print("Area is greater")
else:
    print("Perimeter is greater")