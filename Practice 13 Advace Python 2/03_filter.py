# Write a program to filter a list of numbers which are divisible by 5.

divisble_by5 = lambda x: x%5==0
lst_num = [2, 5, 10, 17, -20]
list_divisible_by_5 = list(filter(divisble_by5, lst_num))
print(list_divisible_by_5)