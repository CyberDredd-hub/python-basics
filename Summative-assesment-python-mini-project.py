#function to calculate  letter grades
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#List to store students
students = []

#while loop to collect student data
while True:
    first_name = input("Enter student's first name:")
    if first_name.lower() == "done":
        break
    last_name = input("Enter student's last name:")
    
    first_name = first_name.strip().title()
    last_name = last_name.strip().title()

#retrive score and convert string to float
    try:
        score = float(input(f"Enter score for {first_name}, {last_name}:"))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100")
            continue
    except ValueError:
        print("Invalid score. Please enter using a number.")
        continue

#function to print student summary
def print_student_summary(students):
    full_name = (f"{student["first_name"]} {student["last_name"]}")
    print(f"Name: {full_name}, Score: {student["score"]}, Grade: {student["grade"]}")

#calculating the letter grade
grade = get_letter_grade(score)

#dictionary and append to list
student = {
    "first_name": first_name,
    "last_name": last_name,
    "score": score, 
    "grade": grade
}
students.append(student)

#Printing student summary
print("\n--- Student Summaries ---")
if students:
    for s in students:
        print_student_summary
else:
        print("No student names were entered")

with open("grades.text", "w") as file:
    for s in students:
        full_name = f"{["first_name"]} {s["last_name"]}"
        file.write(f"{full_name}, score:{s["score"]}, grade:{s["grade"]}\n")

print("\nStudent information saved to 'grades.txt'.")

get_letter_grade(score)
print_student_summary(students)





