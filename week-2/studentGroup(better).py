"""Stack (Create Stack)"""
class ArrayStack():
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return
        else:
            result = self.data.pop()
            self.size -= 1
            return result
        
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def get_stack_top(self):
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return
        else:
            for i in self.data:
                keep_data = i
            return keep_data
        
    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

def main():
    group = int(input())
    n = int(input())
    members = ArrayStack()
    lis = list()
    count = 0

    for _ in range(n):
        members.push(input())

    for _ in range(group):
        num = list()
        lis.append(num)

    while not members.is_empty():
        for i in lis:
            if members.is_empty():
                break
            x = members.pop()
            i.append(x)

    for i in lis:
        count += 1
        memb = ""
        for j in i:
            memb += ", " + j
        memb = memb.replace(", ","",1)
        print(f"Group {count}: {memb}")
main()
