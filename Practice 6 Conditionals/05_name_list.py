# Write a program which finds out whether a given name is present in a list or not.
def find_name_list(names, target):
    return True if target in names else False

names = ["Alice", "Rahul", "Himanshu", "Shivam", "William"]
target = input("Enter your target: ")

print(find_name_list(names, target))