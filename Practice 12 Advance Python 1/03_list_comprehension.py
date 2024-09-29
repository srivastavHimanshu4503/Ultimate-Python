# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

userNum = int(input("Enter a number: "))

multiplication_list = [(userNum*i) for i in range(1, 11)]
print(multiplication_list)