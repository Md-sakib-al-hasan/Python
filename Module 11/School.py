class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.classrooms = {}
        self.teachers = {}


    def add_teacher(self,subject,teacher):
            self.teachers[subject] = teacher


    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom 
        print(classroom)

    def student_admission(self,student):
        classroom =student.classroom
        if classroom.name in self.classrooms:
            self.classrooms[classroom.name].add_student(student)
        else:
            print(f'No classroom as name {classroom.name}')



    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00, 
            'A': 4.00, 
            'A-': 3.50, 
            'B': 3.00, 
            'C': 2.00, 
            'D': 1.00, 
            'F': 0.00
            }
        return grade_map[grade]



    def __repr__(self) -> str:
        print('------------------ ALL Classroms---------')
        for key,value in self.classrooms.items():
            print(key)


        print('-------------STUDENT=========')
        eight = self.classrooms['eight']
        for student in eight.students:

            print(student.name)
        print("-------------subjects-----------")
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print("------------------- marks")
        for student in eight.students:

            for key,value in student.marks.items():
                print(student.name,key,value, student.subject_grade[key])
            print('--------end students ------------')
        return ''
        
class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self,student):
      serial_id =f'{self.name}-{len(self.students)+1}'
      student.id= serial_id
      student.classroom = self.name
      self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f'{self.name}- {len(self.students)}'
    
    def get_top_students(self):
        pass


class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name
        self.max_marks =100
        self.pass_mark = 30
        self.teacher = teacher

    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)



oo = School("ooo",'j')
man = ClassRoom("sakib")
oo.add_classroom(man)

