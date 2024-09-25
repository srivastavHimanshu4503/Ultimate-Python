# Write a program to mine a log file and find out whether it contains ‘python’ and also find the line number if it is present.
def find_python_log_file(log_file, target = "python"):
    content = ""
    count = 0
    with open(log_file) as f:
        content = f.readline()
        while content != "":
            count += 1
            if target in content:
                return True, count
            content = f.readline()
        return False

print(find_python_log_file("log_with_python.log"))
print(find_python_log_file("log_without_python.log"))