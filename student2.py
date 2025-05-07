def input_student_info():
    total = int(input("How many students? "))
    records = {}

    for i in range(total):
        student = input(f"Name of student #{i+1}: ")
        try:
            raw_scores = input(f"Enter scores for {student} separated by commas: ")
            scores = [float(x) for x in raw_scores.split(",")]
        except ValueError:
            print("Invalid input, skipping student.")
            continue
        records[student] = scores

    return records

def stats(scores):
    if not scores:
        return 0.0, 0, 0
    average = sum(scores) / len(scores)
    return average, max(scores), min(scores)

def assign_letter(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

def print_and_save(records):
    output = []
    best_avg = -1
    top_student = ""

    print("\nStudent Performance Report\n-------------------------")
    for name in records:
        marks = records[name]
        avg, high, low = stats(marks)
        grade = assign_letter(avg)
        if avg > best_avg:
            best_avg = avg
            top_student = name

        line = f"{name}: Marks={marks}, Avg={avg:.2f}, Max={high}, Min={low}, Grade={grade}"
        print(line)
        output.append(line)

    summary = f"\nTop Student: {top_student} with average {best_avg:.2f}"
    print(summary)
    output.append(summary)

    try:
        with open("report.txt", "w") as file:
            for item in output:
                file.write(item + "\n")
        print("Saved report to file.")
    except IOError:
        print("File writing error!")

def runner():
    data = input_student_info()
    print_and_save(data)

if __name__ == "__main__":
    runner()
