class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = self.calculate_average()
        self.highest = max(marks) if marks else 0
        self.lowest = min(marks) if marks else 0
        self.grade = self.assign_grade()

    def calculate_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def assign_grade(self):
        avg = self.average
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

    def summary(self):
        return f"{self.name}: Marks={self.marks}, Avg={self.average:.2f}, High={self.highest}, Low={self.lowest}, Grade={self.grade}"

class ReportGenerator:
    def __init__(self):
        self.students = []

    def collect_data(self):
        try:
            count = int(input("Enter total number of students: "))
        except ValueError:
            print("Invalid input. Defaulting to 1 student.")
            count = 1

        for i in range(count):
            name = input(f"Student #{i+1} Name: ").strip()
            try:
                scores = list(map(float, input("Enter marks separated by commas: ").split(',')))
            except ValueError:
                print("Invalid marks input. Skipping this student.")
                continue
            self.students.append(Student(name, scores))

    def generate_report(self):
        if not self.students:
            print("No student data available.")
            return

        print("\n=== Student Report ===")
        lines = []
        top = max(self.students, key=lambda s: s.average)

        for s in self.students:
            summary = s.summary()
            print(summary)
            lines.append(summary)

        top_line = f"\nTop Performer: {top.name} with Avg={top.average:.2f}"
        print(top_line)
        lines.append(top_line)

        self.save_to_file(lines)

    def save_to_file(self, lines):
        try:
            with open("report.txt", "w") as f:
                f.write("\n".join(lines))
            print("Report written to report.txt")
        except Exception as e:
            print(f"Error saving file: {e}")

def main():
    report = ReportGenerator()
    report.collect_data()
    report.generate_report()

if __name__ == "__main__":
    main()
