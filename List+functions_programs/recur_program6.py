def alt_sign(n):
    if n == 0:
        return 0
    return (-1)**(n+1) * n + alt_sign(n-1)
print(alt_sign(5))