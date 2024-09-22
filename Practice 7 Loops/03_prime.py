# Write a program to find whether a given number is prime or not.
def checkPrime_number(number):
    if number==1 or number==0:
        return False
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

number = int(input("Enter number: "))

print(f"{number} is a Prime number: {checkPrime_number(number)}")