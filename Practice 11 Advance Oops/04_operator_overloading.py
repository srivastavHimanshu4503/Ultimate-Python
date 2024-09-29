# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part
    
    def __add__(self, complexNum):
        return Complex((self.real_part + complexNum.real_part), (self.complex_part + complexNum.complex_part))
    
    def __mul__(self, complexNum):
        """
        z1 = (a+ bi) and z2 = (c +di)
        z1 x z2 =(ac-bd)+(ad+bc)i
        """
        self.prod_real = (self.real_part*complexNum.real_part - self.complex_part*complexNum.complex_part) 
        self.prod_complex = (self.real_part*complexNum.complex_part + self.complex_part*complexNum.real_part) 
        return Complex(self.prod_real, self.prod_complex)
    
    def __str__(self):
        return f"{self.real_part} + {self.complex_part}i"

complexNum1 = Complex(1, 2)
complexNum2 = Complex(3, 4)

print(complexNum1 + complexNum2)
print(complexNum1 * complexNum2)
