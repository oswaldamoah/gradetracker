# Making text input required with a function
def get_course_code():
   while True:
       course_code = str(input("Enter Course code: "))
       if course_code.strip():  # Check if course code is not empty
           return course_code
       else:
           print("Course code is required. Please enter a valid code.")

# Making numerical input required with a function
def get_float_input(prompt):
   while True:
       try:
           return float(input(prompt))
       except ValueError:
           print("Invalid input. Please enter a number.")

# Input course code
course_code = get_course_code()  

# Input Assignment Scores
total_assignment_score = get_float_input("Enter Assignment 1 Score (20): ") + get_float_input("Enter Assignment 2 Score (30) : ")

# Input Exam Score
exam_score = float(input("Enter Exam Score (100): ")) / 100

# Expression for Average Assignment
assignment_average = total_assignment_score / 50


# Expression for final Score
final_score = (assignment_average * 30) + (exam_score * 70)


# Conditional Statement for finding grade
if final_score >= 85:
    final_grade = "A+"
elif final_score >= 80:
    final_grade = "A"
elif final_score >= 75:
    final_grade = "B+"
elif final_score >= 70:
    final_grade = "B"
elif final_score >= 65:
    final_grade = "C+"
elif final_score >= 60:
    final_grade = "C"
elif final_score >= 55:
    final_grade = "D+"
elif final_score >= 50:
    final_grade = "D"
else:
    final_grade = "E"

# Expression for GPA
gpa = (final_score / 100) * 4


# Display results
print(f"\nCOURSE: {course_code}\n"
     f"RAW SCORE: {final_score:.2f}/100\n"
     f"GRADE: {final_grade}\n"
     f"GPA: {gpa:.2f}")


# DONE
"""
* Take scores input for one course
* Calculate and display Raw Score and GPA
"""

#TO DO
"""
* Add remark system to if statement and call it in printed results 
* Make code interactive:
Welcome to LMS for UG
    - Enter scores (Adds new scores or overwrites all old scores)
        What course would you like to add scores for?
        - All 7 courses listed (depending on what is chosen, it is noted) # U can use dictionary of ussd style {"1":"MATH223" and so on}
          # Ask same previous input questions, but for that specific object course (assignment1, assignment2, examscore)
          # Calculate and Display grades for all courses based on if statement
          # Calculate and Display collective RAW Score and GPA 
    # Draw a class diagram for the OOP
    # Complete ReadMe.md


You can select courses from a list of 7 courses (Each course will be an object)
All course raw scores will be added together to get the gpa
Function to edit course info

"""