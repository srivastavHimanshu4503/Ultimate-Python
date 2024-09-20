# Write a program to find the greatest of four numbers entered by the user
def greatest_number(*args):
    storeCount_num_dict = {}
    count = 0
    for i in range(len(args)):
        if args[i] not in storeCount_num_dict:
            storeCount_num_dict[args[i]] = count
            count = 0
        count += 1
    return max(list(storeCount_num_dict.keys()))    

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

print(greatest_number(num1, num2, num3))
    