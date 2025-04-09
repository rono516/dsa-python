from collections import namedtuple

if __name__ == "__main__":
    number_of_students = int(input())
    column_names = input().split()
    Student = namedtuple('Student', column_names)
    students = []
    for i in range(number_of_students):
        student_marks = input().split()  
        student = Student(*student_marks)
        students.append(student)

    total_marks = sum(int(student.MARKS) for student in students)
    average = total_marks/ number_of_students

    print(f"{average:.2f}")
