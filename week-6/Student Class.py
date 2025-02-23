class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
