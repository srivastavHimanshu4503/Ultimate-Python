#  Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
def calculate_pass_fail(subject1_marks, subject2_marks, subject3_marks):
    # claculating total percentage
    total_percentage = True if ((subject1_marks + subject2_marks + subject3_marks)/3) > 40 else False 

    # checking whether each subject has atleast 33%
    individual_subject1 = True if subject1_marks >= 33 else False
    individual_subject2 = True if subject2_marks >= 33 else False
    individual_subject3 = True if subject3_marks >= 33 else False

    if total_percentage and individual_subject1 and individual_subject2 and individual_subject3:
        return "Passed"
    return "Failed"

subject1_marks = int(input("Enter subject 1 marks:  "))
subject2_marks = int(input("Enter subject 2 marks:  "))
subject3_marks = int(input("Enter subject 3 marks:  "))

print(calculate_pass_fail(subject1_marks, subject2_marks, subject3_marks))