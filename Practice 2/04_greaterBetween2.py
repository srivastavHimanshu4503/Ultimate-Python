# Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"Both {a} and {b} are equal")