# Write a program to find whether a given username contains less than 10 characters or not.
def length_username(username):
    return True if len(username) > 10 else False

username = input("Enter your username: ")

print(length_username(username))