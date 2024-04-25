class Course:
    def __init__(self, name, final_score, grade, remark):
        self.name = name
        self.final_score = final_score
        self.grade = grade
        self.remark = remark

def calculate_grade(final_score):
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
    
    return final_grade

def calculate_remark(final_score):
    if final_score >= 85:
        remark = "Outstanding"
    elif final_score >= 80:
        remark = "Excellent"
    elif final_score >= 75:
        remark = "Very Good"
    elif final_score >= 70:
        remark = "Good"
    elif final_score >= 65:
        remark = "Average"
    elif final_score >= 60:
        remark = "Pass"
    elif final_score >= 55:
        remark = "Poor"
    elif final_score >= 50:
        remark = "Very Poor"
    else:
        remark = "Fail"
    
    return remark


# Courses
def math():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)
 
    return Course("Mathematics", 0, grade, remark)

def int_science():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)

    return Course("Integrated Science", 0, grade, remark)

def social():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)
    
    return Course("Social Studies", 0, grade, remark)

def english():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)
    
    return Course("English Language", 0, grade, remark)

def bio():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)
    
    return Course("Biology", 0, grade, remark)

def chem():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)

    return Course("Chemistry", 0, grade, remark)

def phys():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)

    return Course("Physics", final_score, grade, remark)

def ict():
    final_score = 0
    grade = calculate_grade(final_score)
    remark = calculate_remark(final_score)

    return Course("Information Technology", final_score, grade, remark)

math = math()
int_science = int_science()
social = social()
english = english()
bio = bio()
chem = chem()
phys = phys()
ict = ict()


courses = [math, int_science, social, english, bio, chem, phys, ict]



def start():
     print("OT High School Grade Tracker")
     print(f"\t1. Enter Scores\n\t2. Get Course Information\n\t3. General Information\n\tx. Exit")

     while True:
        choice1 = input("* Select an option: ")
        print("")


        match choice1:
            case '1':
                enter_scores()
                goHome()
                break
            case '2':
                course_info()
                goHome()
                break
            case '3':
                general_info()
                goHome()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter a number from '1-3' or 'x': ")


def enter_scores():
     print("Which course score would you like to enter?")
     print(f"\t1. Math\n\t2. Science\n\t3. Social Studies\n\t4. English Language\n\t5. Biology")
     print(f"\t6. Chemistry\n\t7. Physics\n\t8. Information Technology\n\t9.Back\n\tx. Exit")

     while True:
        choice1 = input("* Select an option: ")
        print("")


        match choice1:
            case '1':
                item = math
                break
            case '2':
                item = int_science
                break
            case '3':
                item = social
                break
            case '4':
                item = english
                break
            case '5':
                item = bio
                break
            case '6':
                item = chem
                break
            case '7':
                item = phys
                break
            case '8':
                item = ict
                break
            case '9':
                start()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter a number from '1-5' or 'x': ")
    
     while True:
        try:
            a1= float(input(f"{item.name}: Enter Assignment 1 Score /20 : "))/20
            break
        except (a1>20 or a1<0):
            print("Assignment 1 Score should be positive and not more than 20")
        except ValueError:
            print("Enter a number")
        
     while True:
        try:
            a2= float(input(f"{item.name}: Enter Assignment 2 Score /20: "))/20
            break
        except (a1>20 or a1<0):
            print("Assignment 2 Score should be positive and not more than 20")
        except ValueError:
            print("Enter a number")
     
     while True:
        try:
            ms= float(input(f"{item.name}: Enter Mid-Term Exam Score /50: "))/50
            break
        except (a1>50 or a1<0):
            print("Mid-Term Exam Score should be positive and not more than 20")
        except ValueError:
            print("Enter a number")

     while True:
        try:
            eos= float(input(f"{item.name}: Enter End-Of-Term Exam Score /100: "))/100
            break
        except (a1>100 or a1<0):
            print("End-Of-Term Exam Score should be positive and not more than 100")
        except ValueError:
            print("Enter a number")
    
     print(f"Scores for {item.name} have been recorded")
        
     
     
     f_score = (a1*12.5)+(a2*12.5)+(ms*25)+(eos*50)
     item.final_score = f_score
     item.grade = calculate_grade(f_score)
     item.remark = calculate_remark(f_score)


def course_info():
     print("Which course details do you want to see?: ")
     print(f"\t1. Math\n\t2. Science\n\t3. Social Studies\n\t4. English Language\n\t5. Biology")
     print(f"\t6. Chemistry\n\t7. Physics\n\t8. Information Technology\n\t9.Back\n\tx. Exit")

     while True:
        choice1 = input("* Select an option: ")
        print("")

        match choice1:
            case '1':
                item = math
                break
            case '2':
                item = int_science
                break
            case '3':
                item = social
                break
            case '4':
                item = english
                break
            case '5':
                item = bio
                break
            case '6':
                item = chem
                break
            case '7':
                item = phys
                break
            case '8':
                item = ict
                break
            case '9':
                start()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter a number from '1-5' or 'x': ")
     
     print("---Course Details---")
     print(f"Name: {item.name}")
     print(f"Raw Score: {item.final_score}")
     print(f"Grade: {item.grade}")
     print(f"Remark: {item.remark}")


def general_info():
    print("GENERAL INFORMATION")
    print("---------------------")
    print("COURSE DETAILS")
    print("---------------------")
    cumulative_score = 0
    for course in courses:
        print("")
        print(f"Name: {course.name}")
        print(f"Grade: {course.grade}")
        print(f"Remark: {course.remark}")
        cumulative_score+=course.final_score

    gpa = (cumulative_score/800)*4
    print("")
    print("----------------------")
    print(f"GPA: {gpa:.2f}")
    




    

    




def goHome():
    print("")
    
    while True:
        decision = input("Homepage-'0' | Exit-'x' : ")
        print("")

        match decision:
            case '0':
                start()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter either '0 - Home' or 'x - Exit'")


start()