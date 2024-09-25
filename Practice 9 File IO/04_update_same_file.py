# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 
def update_file(fileName, target):
    content = ""
    with open(fileName) as f:
        content = f.read()
        if target in content:
            content = content.replace(target, "#####")
    with open(fileName, "w") as f:
        f.write(content)


fileName = "replace_donkey.txt"
target = "donkey"

update_file(fileName, target)
