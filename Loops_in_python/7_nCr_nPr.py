def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
n = int(input())
r = int(input())
print("nCr:", fact(n)//(fact(r)*fact(n-r)))
print("nPr:", fact(n)//fact(n-r))