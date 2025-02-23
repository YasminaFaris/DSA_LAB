"""Student Class (No Class)"""
def main():
    """Student Class (No Class)"""
    lis = []
    gender = "Miss"
    for _ in range(16):
        data = input()
        lis.append(data)
    if lis[3] == lis[-1]:
        if lis[1] == "Male":
            gender = "Mr"
        print(f"{gender} {lis[0]} ({lis[2]}) ID: {lis[-1]} GPA {int(lis[4]):.2f}")
    elif lis[8] == lis[-1]:
        if lis[6] == "Male":
            gender = "Mr"
        print(f"{gender} {lis[5]} ({lis[7]}) ID: {lis[-1]} GPA {int(lis[9]):.2f}")
    elif lis[13] == lis[-1]:
        if lis[11] == "Male":
            gender = "Mr"
        print(f"{gender} {lis[10]} ({lis[12]}) ID: {lis[-1]} GPA {int(lis[14]):.2f}")
    else:
        print("Student not found")
main()

#Helpppp