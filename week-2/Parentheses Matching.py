class ArrayStack():
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        self.data.append(input_data)
        self.size += 1
    def pop(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            result = self.data.pop()
            self.size -= 1
            return result
    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)

def is_parentheses_matching(expression):
    stack = ArrayStack()
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.is_empty():
                print("Underflow: Cannot pop data from an empty list")
                print("Parentheses in", expression, "are unmatched")
                return False
            stack.pop()
    if stack.is_empty():
        print("Parentheses in", expression, "are matched")
        return True
    else:
        print("Parentheses in", expression, "are unmatched")
        return False

def main():
    expression = input().strip()
    result = is_parentheses_matching(expression)
    print(result)
main()
