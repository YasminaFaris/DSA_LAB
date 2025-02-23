"""Rectangle"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def calculate_area(self):
        return self.height*self.width
    
    def calculate_perimater(self):
        return 2*(self.height+self.width)

def main():
    rectangle = Rectangle(float(input()), float(input()))
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimater()
    print(f"{result:.2f}")
main()
