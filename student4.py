def get_data():
    num = int(input("Enter number of students: "))
    return {input(f"Enter name of student #{i+1}: "): list(map(float, input(f"Enter marks for student #{i+1} (comma-separated): ").split(','))) for i in range(num)}

def calc_stats(marks):
    avg = sum(marks) / len(marks) if marks else 0
    return avg, max(marks), min(marks)

def grade(avg):
    return ('A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D' if avg >= 60 else 'F')

def report(students):
    result = [(name, *calc_stats(marks), grade(calc_stats(marks)[0])) for name, marks in students.items()]
    top_student = max(result, key=lambda x: x[1])
    [print(f"{name}: Marks={marks}, Avg={avg:.2f}, Max={high}, Min={low}, Grade={grade}") for name, marks, avg, high, low, grade in result]
    print(f"\nTop performer: {top_student[0]} with Avg={top_student[1]:.2f}")

    try:
        with open("report.txt", "w") as f:
            for name, marks, avg, high, low, grade in result:
                f.write(f"{name}: Marks={marks}, Avg={avg:.2f}, Max={high}, Min={low}, Grade={grade}\n")
            f.write(f"\nTop performer: {top_student[0]} with Avg={top_student[1]:.2f}")
        print("Report saved to 'report.txt'")
    except Exception as e:
        print(f"Error saving the file: {e}")

def main():
    students = get_data()
    report(students)

if __name__ == "__main__":
    main()
