#titles
#cancel choice (leave choice)

gradebook = {"Billy":[76, 89, 83],
             "Polly":[67, 85, 75],
             "Charlie":[75, 90, 83]}

def view_letter():
    pass

# - Sort students by average grade.
def sort():
    pass

def add_student():
    student = input("Enter student name: ")
    gradebook[student] = []
    print("")
    print("Current gradebook:")
    print(gradebook)

# replace if "no grade"
def add_grade():
    while True:
        student = input("Enter student name to update grade: ")
        if student not in gradebook:
            print("The name \""+ student + "\" is not in the gradebook. Check spelling and capitalization.")
        # ask to add student to gradebook; otherwise, leave add grade
        else:
             break
    while True:
        try:
            grade = input("Enter grade: ")
            grade = float(grade)
            break
        except:
            print("Please enter a number.")
            print("")
    gradebook[student].append(grade)
    print("")
    print("Current gradebook:")
    print(gradebook)

def calculate_avg(student):
    sum = 0
    grades = gradebook[student]
    for grade in grades:
        sum += grade
    try:
        average = sum/len(grades)
    except:
        average = "No Grade"
    return average

# negative grades not allowed
# if a student does not have any grades, then it is aZeroDivisionError, if not grade, then output "no grades"
def summary():
    top_student = []
    top_grade = 0
    for student in gradebook:
        avg = calculate_avg(student)
        print(student + ": " + str(gradebook[student]) + " Average : " + str(avg))
        if avg != "No Grade":
            if avg > top_grade:
                top_grade = avg
                top_student = [student]
            elif avg == top_grade:
                top_student.append(student)
    final_top =  ", ".join(top_student)
    print("Top Student(s): " + final_top)

    #view letter grades

    # sort

# ---

def remove_student():
    while True:
        student = input("Enter name of the student to remove from the gradebook: ")
        if student not in gradebook:
            print("The name \""+ student + "\" is not in the gradebook. Check spelling and capitalization.")
        else:
            break
    while True:
        confirm = input("You want to remove " + student + " from the gradebook. Are you sure? Y/N: ")
        confirm = confirm.lower()
        if confirm == "y":
            del gradebook[student]
            print("")
            break
        elif confirm == "n":
            break
        else:
            print("Enter either Y or N.")
            print("")
    print("")
    print("Current gradebook:")
    print(gradebook)


def remove_grade():
    while True:
        student = input("Enter name of the student to remove their grade: ")
        if student not in gradebook:
            print("The name \""+ student + "\" is not in the gradebook. Check spelling and capitalization.")
        else:
            break

    print(student + "'s Grades:")
    grade_list = gradebook[student]
    for i in range(len(grade_list)):
        print(str(i) + ": " + str(grade_list[i]))
    while True:
        try:
            index = input("Which grade do you want to remove? ")
            index = int(index)
            if index > (len(grade_list)):
                print("Please enter an integer from the choices indicated....")
            else:
                break
        except:
            print("Please enter an integer from the choices indicated..")
    
    while True:
        confirm = input("You want to remove " + str(grade_list[index]) + " from " + student +"'s grades. Are you sure? Y/N: ")
        confirm = confirm.lower()
        if confirm == "y":
            gradebook[student].pop(index)
            print("")
            break
        elif confirm == "n":
            break
        else:
            print("Enter either Y or N.")
            print("")

    print("Current gradebook:")
    print(gradebook)


# ---

print("Welcome to the gradebook.")
while True:
    print("")
    choice = input(\
    "0: Add new student\n" \
    "1: Add grade\n" \
    "2: Remove student\n" \
    "3: Remove grade\n" \
    "4: View gradebook summary\n" \
    "X: Close gradebook\n" \
    "Enter choice: ")
    choice = choice.lower()
    print("")
    if choice == "0":
        add_student()
    if choice == "1":
        add_grade()
    if choice == "2":
        remove_student()
    if choice == "3":
        remove_grade()
    if choice == "4":
        summary()
    if choice == "x":
        break
    else:
        print("")
        print("Please enter a number or \'X\' from the choices indicated.")
