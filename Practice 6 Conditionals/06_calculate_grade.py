"""
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
"""
def calculate_grade_students(marks):
    if 90 < marks <= 100:
        return "Excellent"
    elif 80 < marks <= 90:
        return "A"
    elif 70 < marks <= 80:
        return "B"
    elif 60 < marks <= 70:
        return "C"
    elif 50 < marks <= 60:
        return "D"
    elif  0 < marks <= 50:
        return "F"
    else:
        return "Invalid Marks"
    
marks = int(input("Enter your marks: "))

print(calculate_grade_students(marks))