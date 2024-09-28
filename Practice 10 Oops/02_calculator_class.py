# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, number) -> None:
        self.number = number

    def finding_square(self):
        print(f"The square of {self.number} is {self.number**2}")

    def finding_cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

    def finding_square_root(self):
        print(f"The square root of {self.number} is {self.number**0.5}")

num = Calculator(4)
num.finding_square()
num.finding_cube()
num.finding_square_root()