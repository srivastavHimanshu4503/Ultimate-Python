# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self, number) -> None:
        self.number = number

    @staticmethod
    def greet_user():
        print("Good Morning!")

    def finding_square(self):
        print(f"The square of {self.number} is {self.number**2}")

    def finding_cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

    def finding_square_root(self):
        print(f"The square root of {self.number} is {self.number**0.5}")

num = Calculator(4)
num.greet_user()
num.finding_square()
num.finding_cube()
num.finding_square_root()