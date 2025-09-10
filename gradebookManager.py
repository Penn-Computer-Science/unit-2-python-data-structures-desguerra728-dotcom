def add_student(gradebook):
    student = input("Enter student name: ")
    gradebook[student] = {}
    print("Updated gradebook:")
    print(gradebook)
    return student

def add_grade(student, gradebook):
    try:
        grade = input("Enter grade: ")
        float(grade)
    except:
        print("Please enter a number.")
        print("")
    gradebook[student].append(grade)

gradebook = {"Billy":[76, 89, 83],
             "Polly":[89, 90, 78],
             "Charlie":[75, 76, 98]}
print(gradebook)


add_student(gradebook)


# 2. User Input
# - Allow the user to:
#   - Add a new student
#   - Add grades for an existing student
#   - View the gradebook summary

# 3. Calculations
# - For each student, calculate the average grade.
# - Identify and print the student with the highest average.

# 4. Display
# - Print a clear summary of all students, their grades, and their average.
# - Example output:
#   - Alice: [90, 85, 92] Average: 89.0
#   - Bob: [78, 81, 86] Average: 81.7
#   - Top Student: Alice

# ---
# 5. Additional Features (Required)
# - Allow the user to remove a student or a grade.
# - Display letter grades (A, B, C, etc.) based on averages.
# - Sort students by average grade.
# ---