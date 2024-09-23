"""
Write a python function to print first n lines of the following pattern:
for n = 3
***
** 
*
"""
# Method 1 - Using one for loop 
# def print_rev_triangle(N):
#     for i in range(N):
#         print("*"*(N-i), end="")
#         print()

# Method 2 - Using two for loop
# def print_rev_triangle(N):
#     for i in range(N):
#         for j in range(N-i):
#             print("*", end="")
#         print()

# Method 3 - Using Recusion
def print_rev_triangle(N):
    if N==0:
        return
    print("*"*N)
    print_rev_triangle(N-1)


print_rev_triangle(3)
