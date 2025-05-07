import threading

def parse_marks(marks_str):
    """Convert a comma-separated string of marks into a list of floats."""
    return list(map(float, marks_str.split(',')))

def calculate_average(marks):
    """Calculate the average of the list of marks."""
    return sum(marks) / len(marks) if marks else 0

def determine_grade(average):
    """Return the letter grade based on the average score."""
    return 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'

def process_student_data(student_name, marks, results, index):
    """Process each student's marks and append the result to the shared results list."""
    average = calculate_average(marks)
    grade = determine_grade(average)
    results[index] = f"{student_name}: Marks={marks}, Average={average:.2f}, Grade={grade}"

def get_student_data():
    """Collect student data (name and marks) from the user."""
    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student #{i + 1}: ")
        marks_str = input(f"Enter marks for {name} (comma-separated): ")
        marks = parse_marks(marks_str)
        students.append((name, marks))
    return students

def generate_report(students):
    """Generate and print the detailed report using multithreading."""
    results = [None] * len(students)
    threads = []

    # Create a thread for each student
    for i, (name, marks) in enumerate(students):
        thread = threading.Thread(target=process_student_data, args=(name, marks, results, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the report
    print("\n--- Student Report ---")
    for result in results:
        print(result)

    # Find the top performer
    top_student = max(students, key=lambda s: calculate_average(s[1]))
    print(f"\nTop performer: {top_student[0]}")

    return results

def save_report_to_file(report, filename="report.txt"):
    """Save the report to a text file."""
    try:
        with open(filename, "w") as file:
            file.write("\n".join(report))
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Error saving the report: {e}")

def main():
    """Main function to execute the program."""
    students = get_student_data()
    report = generate_report(students)
    save_report_to_file(report)

if __name__ == "__main__":
    main()
