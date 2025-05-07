def get_student_count():
    """Ask for the number of students and ensure it's a valid positive integer."""
    while True:
        try:
            count = int(input("Enter the number of students: "))
            if count <= 0:
                raise ValueError("Number must be greater than zero.")
            return count
        except ValueError as e:
            print(f"Invalid input. {e}, please enter a positive integer.")

def get_marks_for_student(student_name):
    """Prompt for the marks of a specific student and validate input."""
    while True:
        try:
            marks_input = input(f"Enter marks for {student_name} (comma-separated): ")
            marks = [float(mark.strip()) for mark in marks_input.split(',')]
            if not marks:
                raise ValueError("Marks cannot be empty.")
            return marks
        except ValueError as e:
            print(f"Invalid marks input: {e}. Please enter valid numbers separated by commas.")

def calculate_average(marks):
    """Calculate the average of a student's marks."""
    return sum(marks) / len(marks)

def assign_grade(average):
    """Assign a letter grade based on the student's average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

def collect_student_data(num_students):
    """Collect names and marks of all students."""
    students = {}
    for i in range(num_students):
        name = input(f"Enter the name of student #{i+1}: ")
        marks = get_marks_for_student(name)
        students[name] = marks
    return students

def print_student_report(students):
    """Print a detailed report of all students' marks, averages, and grades."""
    print("\n--- STUDENT REPORT ---")
    highest_avg = -1
    top_student = ""
    report_lines = []

    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = assign_grade(avg)
        print(f"{name}: Marks={marks}, Average={avg:.2f}, Grade={grade}")

        if avg > highest_avg:
            highest_avg = avg
            top_student = name

        report_lines.append(f"{name}: Marks={marks}, Average={avg:.2f}, Grade={grade}")

    print(f"\nTop Performer: {top_student} with Average={highest_avg:.2f}")
    report_lines.append(f"Top Performer: {top_student} with Average={highest_avg:.2f}")

    save_report_to_file(report_lines)

def save_report_to_file(report_lines, filename="report.txt"):
    """Save the report to a text file."""
    try:
        with open(filename, "w") as file:
            for line in report_lines:
                file.write(line + "\n")
        print(f"Report saved to {filename}")
    except IOError as e:
        print(f"Failed to save report: {e}")

def main():
    """Main function to execute the program."""
    num_students = get_student_count()
    students = collect_student_data(num_students)
    print_student_report(students)

if __name__ == "__main__":
    main()
