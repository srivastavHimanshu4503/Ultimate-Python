# Write a program to find out whether a file is identical & matches the content of another file.
with open("this.txt") as f:
    content1 = f.read()

with open("copy_this.txt") as g:
    content2 = g.read()

if content1 == content2:
    print("Identical files")
else:
    print("Not identical files")