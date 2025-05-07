import sqlite3

def create_db():
    """Create the database and the table to store student data."""
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_student_data(name, marks):
    """Insert a student's name and marks into the database."""
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, marks)
        VALUES (?, ?)
    ''', (name, ','.join(map(str, marks))))
    conn.commit()
    conn.close()

def get_all_students():
    """Fetch all students and their marks from the database."""
    conn = sqlite3.connect('student_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, marks FROM students')
    students = cursor.fetchall()
    conn.close()
    return [(name, list(map(float, marks.split(',')))) for name, marks in students]

def calculate_average(marks):
    """Calculate the average of the list of marks."""
    return sum(marks) / len(marks) if marks else 0

def determine_grade(average):
    """Return the letter grade based on the average score."""
    return 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'

def generate_report(students):
    """Generate and print the detailed report."""
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
    """Main function to execute the program."""
    create_db()

    # Insert sample data into the database
    insert_student_data("Alice", [88, 92, 85, 90])
    insert_student_data("Bob", [72, 75, 80, 78])
    insert_student_data("Charlie", [95, 96, 93, 98])

    students = get_all_students()
    report = generate_report(students)
    save_report_to_file(report)

if __name__ == "__main__":
    main()
