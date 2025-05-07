import os

def get_student_data():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    students = {}

    for _ in range(num_students):
        name = input("Enter student name: ").strip()
        while True:
            try:
                marks_input = input(f"Enter comma-separated marks for {name}: ")
                marks = [float(mark.strip()) for mark in marks_input.split(',') if mark.strip()]
                if not marks:
                    raise ValueError
                students[name] = marks
                break
            except ValueError:
                print("Please enter valid marks (e.g., 85, 90.5, 78)")

    return students

def calculate_statistics(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return avg, highest, lowest

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def display_menu():
    print("\nChoose display option:")
    print("1. Original Order")
    print("2. Sorted by Average (Descending)")
    choice = input("Enter choice (1/2): ")
    return choice.strip()

def generate_report(students, sort=False):
    print("\n--- STUDENT REPORT ---")
    report_lines = []
    student_stats = []

    for name, marks in students.items():
        avg, high, low = calculate_statistics(marks)
        grade = get_grade(avg)
        student_stats.append((name, marks, avg, high, low, grade))

    if sort:
        student_stats.sort(key=lambda x: x[2], reverse=True)

    top_student = max(student_stats, key=lambda x: x[2])

    for name, marks, avg, high, low, grade in student_stats:
        line = f"{name}: Marks={marks}, Avg={avg:.2f}, High={high}, Low={low}, Grade={grade}"
        print(line)
        report_lines.append(line)

    top_line = f"\nTop Performer: {top_student[0]} with Avg={top_student[2]:.2f}"
    print(top_line)
    report_lines.append(top_line)

    save_to_file(report_lines)

def save_to_file(lines, filename="report.txt"):
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"\nReport saved to {filename}")
    except Exception as e:
        print(f"Failed to save report: {e}")

def main():
    students = get_student_data()
    choice = display_menu()
    generate_report(students, sort=(choice == '2'))

if __name__ == "__main__":
    main()
