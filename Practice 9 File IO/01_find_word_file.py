# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

def contains_words_file(fileName, target):
    with open(fileName) as f:
        # Method 1
        # data = f.readline()
        # while data != "":
        #     if data.find(target) != -1:
        #         return True
        #     data = f.readline()
        # return False

        # Method 2
        content = f.read()
        if target in content:
            return True
        return False

fileName = "Practice 9 File IO/poems.txt"
target = "twinkle"
print(contains_words_file(fileName, target))





    