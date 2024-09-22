"""Write a program to print the following star pattern.
for n = 3
  *
 ***
***** 
"""

n_value = int(input("Enter the value for n: "))

for i in range(n_value):
    
    for space in range(n_value-i-1):
        print(" ", end="")
    
    for star in range((2*i)+1):
        print("*", end="")
        
    print()

