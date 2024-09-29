# Write a program to open three files file1.txt, file2.txt and file3.txt if any these files are # not present, a message without exiting the program must be printed prompting the same
try:
    with (
        open("G:/Ultimate Python Course/Projects/file1.txt") as f1,
        open("G:/Ultimate Python Course/Projects/file2.txt") as f2,
        open("G:/Ultimate Python Course/Projects/file3.txt") as f3
    ):
        print(f1.read())
        print(f2.read())
        print(f3.read())
except FileNotFoundError as fe:
    print("In FileNotFoundError exception block")
    print(fe)

except Exception as e:
    print("In general exception block")
    print(e)
