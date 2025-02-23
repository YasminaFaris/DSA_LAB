import json

class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
    
    def print_details(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa}")

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if data[mid].name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return
        elif data[mid].name < name:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")

def main():
    data_input = input()
    name_input = input()
    
    data = []
    student_data = json.loads(data_input)
    
    for student in student_data:
        std = Student(student["id"], student["name"], student["gpa"])
        data.append(std)
    
    binary_search(data, name_input)

main()
