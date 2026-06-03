from student import Student
from manager import StudentManager


manager = StudentManager()

# Load existing students
manager.load_students()

# Add new students
manager.add_student(Student(101, "Deepak", 95))
manager.add_student(Student(102, "Rahul", 80))
manager.add_student(Student(103, "Priya", 92))

# Save to JSON
manager.save_students()

# View students
manager.view_students()

print(f"Total Students: {manager.total_students()}")

student = manager.find_student(102)

if student:
    print("\nStudent Found:")
    student.display()
else:
    print("Student not found")