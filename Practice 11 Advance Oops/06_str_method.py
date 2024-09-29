# Write __str__() method to print the vector as follows:
#  7i + 8j +10k 
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
vector1 = Vector(7, 8, 10)
print(vector1)