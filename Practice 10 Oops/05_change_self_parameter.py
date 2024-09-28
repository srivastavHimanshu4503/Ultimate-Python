#  Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Programmer:
    def __init__(harr, name, language, salary):
        harr.name = name
        harr.language = language
        harr.salary = salary

    def getInfo(slf):
        print(f"Programmer name is {slf.name}, working on programming language {slf.language} with a salary of {slf.salary}.")
    
harry = Programmer("Harry", "Python", 970000)
ramu = Programmer("Ramu", "Javascript", 470000)
badal = Programmer("Badal", "Swift", 870000)

harry.getInfo()
ramu.getInfo()
badal.getInfo()