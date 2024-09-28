# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"Programmer name is {self.name}, working in {self.company} using programming language {self.language} with a salary of {self.salary}.")
    
harry = Programmer("Harry", "Python", 970000)
ramu = Programmer("Ramu", "Javascript", 470000)
badal = Programmer("Badal", "Swift", 870000)

harry.getInfo()
ramu.getInfo()
badal.getInfo()