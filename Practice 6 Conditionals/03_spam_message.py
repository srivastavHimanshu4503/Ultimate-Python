# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

def find_spam_comment(message, spam_messages_list):
    for i in range(len(spam_messages_list)):
        if message.find(spam_messages_list[i]) != -1:
            return "Spam message"
    return "Not a spam message"

spam_messages_list = ["Make a lot of money", "buy now", "subscribe this", "click this"]
message = input("Enter message: ")

print(find_spam_comment(message, spam_messages_list))