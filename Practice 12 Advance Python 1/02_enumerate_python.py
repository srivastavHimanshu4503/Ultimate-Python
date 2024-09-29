# Write a program to print third, fifth and seventh element from a list using enumerate function.
def print_certain_elements_list(lst):
    for index, item in enumerate(lst):
        if index==2 or index==4 or index==8:
            print(item, end=" ")

if __name__ == "__main__":
    mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print_certain_elements_list(mylist)