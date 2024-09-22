# Write a program to calculate the factorial of a given number using for loop.
def calculate_factorial(N):
    fac = 1
    for i in range(1, N+1):
        fac *= i
    return N

num = int(input("Enter your number: "))

print(calculate_factorial(num))