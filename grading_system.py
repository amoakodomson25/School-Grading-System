# Grading system


print()
# Student's credentials
Student_name = input("Enter student's full name: ")
Student_Department = input("Enter student's department: ")
Student_course = input("Enter student's course of study: ")

# Checking if student has paid their fees
while True:
    Fees_Paid = input("Have You Paid Your Fees(100)? (Y/N): ")
    if Fees_Paid.lower() in ["y","n","yes","no"]:
        # Scores input
        Exam_score = int(input("Enter Exam Score: "))
        Assessment_score = int(input("Enter Assessment Score: "))
        break
    else:
        print("Please enter a valid input.")

# Credentials
print()
print(" ")
print("============================== Student Report ===================================")
print("Name: "+ Student_name )
print("Department: " + Student_Department)
print("Course: "+ Student_course)
print(" ")
# Setting the requirements
# If a student has their paid fees; Check their scores to see if they can get certified
if Fees_Paid == "Y" or Fees_Paid == "y":
        if 39 > (Assessment_score + Exam_score):
            if Exam_score < 25:
                print("Failed: Exams score is below past mark")
            if Assessment_score < 15:
                print("Failed: Assessment score is below past mark")
            if (Exam_score < 25) and (Assessment_score < 15):
                print("Hence, this student is repeated.")
        else:
            print("Student can get certificate")
    # If the student has not paid their fees;
else:
    print("Student has not paid fees")
print("==========================================================================")

# The end
