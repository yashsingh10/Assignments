def parse_marks(marks_str):
    """Convert a comma-separated string of marks into a list of floats."""
    return list(map(float, marks_str.split(',')))

def calculate_average(marks):
    """Calculate the average of the list of marks."""
    return sum(marks) / len(marks) if marks else 0

def determine_grade(average):
    """Return the letter grade based on the average score."""
    return 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'

def get_student_data():
    """Collect student data (name and marks) and return as a list of tuples."""
    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student #{i + 1}: ")
        marks_str = input(f"Enter marks for {name} (comma-separated): ")
        marks = parse_marks(marks_str)
        students.append((name, marks))
    return students

def generate_report(students):
    """Generate and print a detailed report, and also return the top performer."""
    report = []
    top_performer = None
    highest_average = -1

    for name, marks in students:
        average = calculate_average(marks)
        grade = determine_grade(average)
        report.append(f"{name}: Marks={marks}, Average={average:.2f}, Grade={grade}")

        if average > highest_average:
            highest_average = average
            top_performer = name

    report.append(f"\nTop performer: {top_performer} with Average={highest_average:.2f}")

    # Print the report
    print("\n--- Student Report ---")
    print("\n".join(report))

    return report

def save_report_to_file(report, filename="report.txt"):
    """Save the report to a text file."""
    try:
        with open(filename, "w") as file:
            file.write("\n".join(report))
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Error saving the report: {e}")

def main():
    """Main function to execute the entire program."""
    students = get_student_data()
    report = generate_report(students)
    save_report_to_file(report)

if __name__ == "__main__":
    main()
