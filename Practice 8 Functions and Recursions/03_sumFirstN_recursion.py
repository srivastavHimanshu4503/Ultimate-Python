def calculate_sum_first_N(N):
    if N <= 1:
        return 1
    return (N + calculate_sum_first_N(N-1))

print(calculate_sum_first_N(10))
print(calculate_sum_first_N(5))
print(calculate_sum_first_N(3))