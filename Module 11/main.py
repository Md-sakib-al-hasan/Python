from School import School ,ClassRoom,Subject
from person import Student,Teacher
def main():
    school = School('adam jee','U TT RA')
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)




    abul = Student('Abul khan',eight)
    school.student_admission(abul)
    babul = Student('babul khan',eight)
    school.student_admission(babul)
    kabul = Student('kabul khan',eight)
    school.student_admission(kabul)





    physics_teacher = Teacher('rana tapon shajana')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('anishol islam')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    math_teacher = Teacher('khoka')
    math = Subject('math',math_teacher)
    eight.add_subject(math)


    eight.take_semester_final()
    


    print(school)
if __name__ == '__main__':
    main()