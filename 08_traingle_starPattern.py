"""Write a program to print the following star pattern.
for n = 3
* * *
*   * 
* * *
"""
num = int(input("Enter the value for n: "))

for i in range(num):

    if (i==0 or i==(num-1)):
        print("*"*num, end="")
    else:
        print("*", end="")
        print(" "*(num-2), end="")
        print("*", end="")
    print()
