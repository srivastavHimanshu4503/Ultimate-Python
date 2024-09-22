num = int(input("Enter your number: "))

print("Using for loop:")
for i in range(10):
    print(f"{num} x {i+1} = {num*(i+1)}")

print()

print("Using while loop:")
i = 1
while (i<11):
    print(f"{num} x {i} = {num*(i)}")
    i += 1

