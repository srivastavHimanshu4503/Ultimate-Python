# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
nums = set()
for i in range(8):
    num = int(input(f"Enter number{i+1}: "))
    nums.add(num)
print(nums)
