# Store the multiplication tables generated in problem 3 in a file named Tables.txt
def store_table_in_file(userNum):
    multiplication_list = [(userNum*i) for i in range(1, 11)]
    with open("Tables.txt", "a") as f:
        for num in multiplication_list:
            f.write(f"{num}\n")

store_table_in_file(5)
