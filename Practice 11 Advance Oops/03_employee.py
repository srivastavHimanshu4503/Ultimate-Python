# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the new_salary of increment based on the salary.

class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary*self.increment)/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary/self.salary)-1)*100


employee1 = Employee(234)
# employee1.increment = 20
# print(employee1.salaryAfterIncrement)
employee1.salaryAfterIncrement = 280.8
print(employee1.increment)

