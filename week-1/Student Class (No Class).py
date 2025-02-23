"""Student Class (No Class)"""
def main():
    """Student Class (No Class)"""
    lis = []
    for _ in range(3):
        name = input().strip()
        gender = input().strip()
        age = int(input().strip())
        student_id = input().strip()
        gpa = float(input().strip())
        lis.append([name, gender, age, student_id, gpa])
    search = input().strip()
    con = False
    for i in lis:
        if i[3] == search:
            con = True
            if i[1] == "Male":
                gend = "Mr"
            else:
                gend = "Miss"
            print(f"{gend} {i[0]} ({i[2]}) ID: {i[3]} GPA {i[4]:.2f}")
            break
    if not con:
        print("Student not found")
main()
