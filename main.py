from collections import namedtuple

if __name__ == "__main__":
    number_of_students = int(input())
    column_names = input().split()
    Student = namedtuple('Student', column_names)
    # student_x = Student(ID=1,MARKS=98,NAME="Collins",CLASS=2)
    # print(student_x)
    for i in range(number_of_students):
        student_name = f"student{i}"
        student_marks = input().split() 
        for mark in student_marks:
            student_name = Student(ID=mark[0],MARKS="mark[1]",NAME="mark[2]",CLASS="mark[3]") 
            print(student_name.MARKS)
    # for student in Student:
    #     print(student)
    # print(student0)