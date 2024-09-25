# Repeat program 4 for a list of such words to be censored.
def update_file(fileName, target_lst):
    content = ""
    with open(fileName) as f:
        content = f.read()
        for i in range(len(target_lst)):
            if target_lst[i] in content:
                content = content.replace(target_lst[i], "#"*len(target_lst[i]))
    with open(fileName, "w") as f:
        f.write(content)


fileName = "Practice 9 File IO/replace_donkey.txt"
target_lst = ["donkey", "day", "laziness"]

update_file(fileName, target_lst)