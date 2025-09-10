def add_student():
    student = input("Enter student name: ")
    gradebook[student] = []
    print("")
    print("Updated gradebook:")
    print(gradebook)
    return student

def add_grade():
    while True:
        student = input("Enter student name to update grade: ")
        if student not in gradebook:
                print(student + " is not in the gradebook.")
        # ask to add student to gradebook
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
    print("Updated gradebook:")
    print(gradebook)

gradebook = {"Billy":[76, 89, 83],
             "Polly":[89, 90, 78],
             "Charlie":[75, 76, 98]}
print(gradebook)


# 2. User Input
#   - View the gradebook summary

# 3. Calculations
# - For each student, calculate the average grade.
# - Identify and print the student with the highest average.

# 4. Display
# - Print a clear summary of all students, their grades, and their average.

def calculate_avg(student):
    sum = 0
    grades = gradebook[student]
    for grade in grades:
        sum += grade
    average = sum/len(grades)
    return average

def summary():
    for student in gradebook:
        avg = calculate_avg(student)
        print(student + ": " + gradebook[student] + " Average : " + str(avg))
    #   - Alice: [90, 85, 92] Average: 89.0
    #   - Bob: [78, 81, 86] Average: 81.7
    #   - Top Student: Alice
    pass


# ---
# 5. Additional Features (Required)
# - Allow the user to remove a student or a grade.

def remove_student():
    pass

def remove_grade():
    pass

# - Display letter grades (A, B, C, etc.) based on averages.
def view_letter():
    pass

# - Sort students by average grade.
def sort():
    pass

# ---
'''
print("Welcome to the gradebook.")
while True:
    print("")
    use = input("1: Add new student\n2: Add grade\n3: View gradebook summary\nX: Close gradebook\nEnter choice: ")
    print("")
    if use == "1":
        add_student()
    if use == "2":
        add_grade()
    if use == "3":
        print("ND")
    if use == "4":
        break
'''
