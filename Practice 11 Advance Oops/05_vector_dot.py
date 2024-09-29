# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, *nums):
        self.nums = nums
    
    def __add__(self, num):
        sums = []
        for i in range(len(self.nums)):
            sums.append(self.nums[i] + num.nums[i])
        return sums
    
    def __mul__(self, num):
        prod = []
        for i in range(len(self.nums)):
            prod.append(self.nums[i] * num.nums[i])
        return sum(prod)
    
first_vector = Vector(1, 2, 3)
second_vector = Vector(4, 5, 6)

print("Addition of vectors: ", first_vector + second_vector)
print("Dot of vectors: ", first_vector * second_vector)
