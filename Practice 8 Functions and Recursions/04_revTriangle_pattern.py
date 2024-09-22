"""
Write a python function to print first n lines of the following pattern:
for n = 3
***
** 
*
"""
def print_rev_triangle(N):
    for i in range(N):
        print("*"*(N-i), end="")
        print()

print_rev_triangle(3)
print_rev_triangle(5)