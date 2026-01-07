print("Student Result Management System")

name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: PASS")

    if percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: FAIL")
