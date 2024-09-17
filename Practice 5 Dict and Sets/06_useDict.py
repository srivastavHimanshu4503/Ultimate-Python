# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
movies = {}

for i in range(4):
    name_key = input("Enter your name: ")
    language_value = input("Enter your language: ")
    movies.update({f"{name_key}" : f"{language_value}"})

print(movies)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# If we add 2 friend name same then it will take the latest one in the dictionary

# 8. If languages of two friends are same; what will happen to the program in problem 6?
# If the values are same then there will be no differnce in order of execution