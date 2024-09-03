# Write a program to fill in a letter template given below with name and date.
letter = '''    
Dear <|Name|>,
You are selected!
<|Date|> '''

user_name = input("Enter your name: ")
date = input("Enter date: ")

print((letter.replace("<|Name|>", user_name)).replace("<|Date|>", date))