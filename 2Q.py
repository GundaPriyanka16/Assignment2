'''Write a function that checks if a given number is prime.''' 


def is_given_prime(n): 
    if n <= 1: 
        print("False") 
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0: 
            print("False")
    print("True")

n = 9
is_given_prime(n)