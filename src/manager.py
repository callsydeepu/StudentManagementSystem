from student import Student
import json
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
        return len(self.students)
    def find_student(self,roll_no):
        for student in self.students:
            if student.roll_no==roll_no:
                return student
        return None
    def save_students(self):
        data=[student.to_dict() for student in self.students]
        with open("data/students.json","w") as file:
            json.dump(data,file,indent=4)
    def load_students(self):
        try:
            with open("data/students.json", "r") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["roll_no"],
                    item["name"],
                    item["marks"]
                )
                self.students.append(student)

        except FileNotFoundError:
            print("students.json not found. Starting with empty data.")

        except json.JSONDecodeError:
            print("Invalid JSON data.")
