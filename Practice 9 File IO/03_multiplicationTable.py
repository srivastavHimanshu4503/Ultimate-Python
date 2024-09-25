import os

# Specify the folder where you want to create the file
folder_path = "./Multiplication Table for 13 year old"

# Check if the folder exists, and if not, create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the full path for the new file

def multilplication_table():
    for i in range(2, 21):
        file_path = os.path.join(folder_path, f"table{i}.txt")
        for j in range(1, 11):
            with open(file_path, "a") as f:
                f.write(f"{i} x {j} = {i*j}\n")

def generate_tables():
    for i in range(2, 21):
        for j in range(1, 11):
            with open(f"Practice 9 File IO/Tables/table{i}.txt", "a") as f:
                f.write(f"{i} x {j} = {i*j}\n")


# multilplication_table()
generate_tables()