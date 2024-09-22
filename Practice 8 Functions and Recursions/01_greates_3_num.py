# Write a program using functions to find greatest of three numbers
def find_greatest_3_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3
    
num1 = int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print(f"{find_greatest_3_num(num1, num2, num3)} is greatest among all.")