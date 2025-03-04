def load_attendance():
    attendance = {}
    try:
        with open("attendance.txt", "r") as file:
            for line in file:
                student, records = line.strip().split(":")
                attendance[student] = records.split(", ")
    except FileNotFoundError:
        pass
    return attendance

def save_attendance(attendance):
    with open("attendance.txt", "w") as file:
        for student, records in attendance.items():
            file.write(f"{student}:{', '.join(records)}\n")

def mark_attendance(attendance):
    student = input("Enter student name: ").capitalize()
    status = input("Enter (P for Present, A for Absent): ").upper()
    
    if status not in ["P", "A"]:
        print("Invalid input! Use P or A.")
        return

    if student not in attendance:
        attendance[student] = []
    attendance[student].append(status)
    save_attendance(attendance)
    print(f"Attendance marked: {student} -> {status}")

def view_attendance(attendance):
    print("\nStudent Attendance Report:")
    for student, records in attendance.items():
        total = len(records)
        present = records.count("P")
        percentage = (present / total) * 100 if total > 0 else 0
        print(f"{student}: {', '.join(records)} | {percentage:.2f}% Present")

def main():
    attendance = load_attendance()

    while True:
        print("\n1. Mark Attendance\n2. View Attendance\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            mark_attendance(attendance)
        elif choice == "2":
            view_attendance(attendance)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

