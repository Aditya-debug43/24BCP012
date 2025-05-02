x = float(input())
x = x * 3.14159 / 180
s = 0
for i in range(10):
    sign = (-1)**i
    term = x**(2*i+1)
    fact = 1
    for j in range(1, 2*i+2):
        fact *= j
    s += sign * term / fact
print(s)