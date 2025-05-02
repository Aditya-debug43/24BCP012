n = int(input())
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
def is_armstrong(n):
    return sum(int(d)**len(str(n)) for d in str(n)) == n
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def is_automorphic(n):
    return str(n*n).endswith(str(n))
print("Prime:", is_prime(n))
print("Perfect:", is_perfect(n))
print("Armstrong:", is_armstrong(n))
print("Palindrome:", is_palindrome(n))
print("Automorphic:", is_automorphic(n))