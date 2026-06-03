from student import Student
class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)
    def view_students(self):
        for students in self.students:
            students.display()
            print("-"*20)
    def total_students(self):
        return len(self.students())
    def find_student(self,roll_no):
        for student in self.students:
            if student.roll_no==roll_no:
                return student
        return None
