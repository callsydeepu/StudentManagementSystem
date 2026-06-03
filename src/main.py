from student import Student
from manager import StudentManager

manager=StudentManager()
student1 = Student(101, "Deepak", 95)
student2 = Student(102, "Rahul", 80)
student3 = Student(103, "Priya", 92)# student1.display()

manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)
# print(student1.isPassed())
# print(student1.get_grade())

# manager.view_students()
student=manager.find_student(101)

if student:
    student.display()
else:
    print("Student not found")