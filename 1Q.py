'''Write a Python function to calculate the factorial of a non-negative integer.'''


def factorial (n):
    if n == 0: 
        print("1") 
    else: 
        print("n*factorial(n-1)")
n = input("Input a factorial number:" )
print(factorial(n))
