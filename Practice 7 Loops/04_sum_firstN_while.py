# Write a program to find the sum of first n natural numbers using while loop.
def find_sum_first_N_naturalNumbers(N):
    sum = 0
    i = 0
    while (i < N):
        sum += (i+1)
        i += 1
    return sum
num = int(input("Enter your number: "))

print(find_sum_first_N_naturalNumbers(num))