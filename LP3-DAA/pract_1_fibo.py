# Recursive
def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)

# non recursive
def fibo_itr(n):
    if n == 0:
        return 0
    a = 0
    b = 1

    for i in range(1, n):
        c = a + b
        a = b
        b = c

    return b

    
n = int(input("Enter Number Of Elements:"))

print("Recursive Answer: ", fibo_rec(n))

print("Iterative Answer: ", fibo_itr(n))

"""
Analysis
Recursive:
    Time Complexity - O(2^n)
    Space Complexity - O(n)
    
Iterative:
    Time Complexity - O(n)
    Space Complexity - O(1)
"""