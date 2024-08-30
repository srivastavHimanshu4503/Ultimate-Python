# Write a python program to print the contents of a directory using the os module. Search online for the function which does that. 

import os

path = input("Enter the path: ")

try:
    contents = os.listdir(path)
    for items in contents:
        print(items)
except FileNotFoundError:
    print(f"Error: File not find at the given path: {path}")