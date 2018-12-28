def grade_students_marks(marks):
    greater_than_50 = []
    less_than_50 = []
    print(greater_than_50)
    print(less_than_50)
    for mark in marks:
        if mark > 50:
            greater_than_50.append(mark)
        else:
            less_than_50.append(mark)
        if mark>=90 and mark<=100:
            print('Student mark {0} is Excellent'.format(mark))
        elif mark>=70 and mark<=89:
            print('Student mark {0} is very good'.format(mark))
        elif mark>=60 and mark<=69:
            print('Student mark {0} is good'.format(mark))
        elif mark>=40 and mark<=59:
            print('Student mark {0} is poor'.format(mark))
        elif mark>=20 and mark<=39:
            print('Student mark {0} is very poor'.format(mark))
        else:
            print('Student mark {0} is too vegg, You should repeat'.format(mark))

if __name__ == '__main__':
    student_marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
print(grade_students_marks(student_marks))