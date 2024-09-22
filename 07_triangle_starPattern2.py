"""Write a program to print the following star pattern:
for n = 3
*
**
***
"""

num = int(input("Enter the value for n: "))

for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print()
