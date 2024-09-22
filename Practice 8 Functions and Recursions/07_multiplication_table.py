# Write a python function to print multiplication table of a given number.
def print_multiplication_table(N):
    for i in range(1, 11):
        print(f"{N} x {i} = {N*i}")

print_multiplication_table(5)
print_multiplication_table(25)
print_multiplication_table(17)