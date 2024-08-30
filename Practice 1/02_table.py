# Print the multiplication table of any number.

num = int(input("Enter the number you want multiplication table of: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")