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
     print(f"\t1. Enter Scores\n\t2. Get Course Information\n\t3. Edit Scores\n\t4. Reset Course\n\t5. General Information\n\tx. Exit")

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
                enter_scores()
                goHome()
                break
            case '4':
                reset_scores()
                goHome()
                break
            case '5':
                general_info()
                goHome()
                break


def enter_scores():
     ''' REMOVE COMMENT AND EDIT
     print("Which course score would you like to enter?")
     print(f"\t1. Math\n\t2. Science\n\t3. Edit Scores\n\t4. Reset Course\n\t5. General Information\n\tx. Exit")
     print(f"\t1. Enter Scores\n\t2. Get Course Information\n\t3. Edit Scores\n\t4. Reset Course\n\t5. General Information\n\tx. Exit")

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
                enter_scores()
                goHome()
                break
            case '4':
                reset_scores()
                goHome()
                break
            case '5':
                general_info()
                goHome()
                break
                
                '''


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
                break
            case _:
                print("Enter either '0 - Home' or 'x - Exit'")