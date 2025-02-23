class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def get_std_id(self):
        return self.std_id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return self.gpa
    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")
class ProbHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size
    def hash(self, key: int) -> int:
        return key % self.size
    def rehash(self, old_hash: int) -> int:
        return (old_hash + 1) % self.size
    def insert_data(self, student: Student) -> None:
        key = student.get_std_id()
        hash_val = self.hash(key)
        if self.hash_table[hash_val] is None:
            self.hash_table[hash_val] = student
            print(f"Insert {key} at index {hash_val}")
        else:
            original_hash = hash_val
            stop = False
            while self.hash_table[hash_val] is not None:
                hash_val = self.rehash(hash_val)
                if hash_val == original_hash:
                    stop = True
                    break
            if stop:
                print(f"The list is full. {key} could not be inserted.")
            else:
                self.hash_table[hash_val] = student
                print(f"Insert {key} at index {hash_val}")
    def search_data(self, std_id: int) -> Student:
        start_slot = self.hash(std_id)
        position = start_slot
        stop = False
        while self.hash_table[position] is not None and not stop:
            if self.hash_table[position].get_std_id() == std_id:
                print(f"Found {std_id} at index {position}")
                return self.hash_table[position]
            position = self.rehash(position)
            if position == start_slot:
                stop = True
        print(f"{std_id} does not exist.")
        return None
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        line = input().strip()
        if line == "Done":
            break
        if " = " not in line:
            print("Invalid Condition!")
            continue
        condition, data = line.split(" = ", maxsplit=1)
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()