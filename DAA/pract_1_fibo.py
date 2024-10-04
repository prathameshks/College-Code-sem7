arr = []

# Recursive
def fibo_rec(n):
    if n <= 1:
        arr[n] = n
        return n
    next = fibo_rec(n - 1) + fibo_rec(n - 2)
    arr[n] = next
    return next

# non recursive
def fibo_itr(n):
    if n == 0:
        print(0,end=" ")
        return 0
    a,b = 0,1
    print(a,b,end=" ",sep=" ")
    for i in range(1, n):
        a,b = b,a + b
        print(b,end=" ")

    return b

    
n = int(input("Enter Number Of Elements:"))
arr = [0 for i in range(n+1)]

print("Itretative")
fibo_itr(n)

print()
print("Recursive")
fibo_rec(n)
print(arr)
print("End")
# print("Recursive Answer: ", fibo_rec(n))

# print("Iterative Answer: ", fibo_itr(n))

"""
Analysis
Recursive:
    Time Complexity - O(2^n)
    Space Complexity - O(n)
    
Iterative:
    Time Complexity - O(n)
    Space Complexity - O(1)
"""