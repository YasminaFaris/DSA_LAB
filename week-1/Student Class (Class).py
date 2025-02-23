"""Student Class (Class)"""
class Student:
    def __init__(self, name, gender, age, student_id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.student_id = student_id
        self.gpa = gpa
    def __str__(self):
        if self.gender == "Male":
                gend = "Mr"
        else:
            gend = "Miss"
        return (f"{gend} {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}")
    
def main():
    lis = []
    for _ in range(3):
        name = input().strip()
        gender = input().strip()
        age = int(input().strip())
        student_id = input().strip()
        gpa = float(input().strip())
        lis.append(Student(name, gender, age, student_id, gpa))
    search = input().strip()
    con = False
    for i in lis:
        if i.student_id == search:
            con = True
            print(i)
            break
    if not con:
        print("Student not found")
main()
