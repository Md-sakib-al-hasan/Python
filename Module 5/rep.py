class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.current_class=current_class
        self.id=id
    def __repr__(self) -> str:
        return f'student with name : {self.name}, class:{self.current_class},id:{self.id}'

class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self=id
    def __repr__(self) -> str:
        return f'Teacher: {self.name},subject : {self.subject}'

class School:
    def __init__(self,name) -> None:
        self.name =name
        self.teachers= []
        self.students=[]
    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        print(teacher)
        self.teachers.append(teacher)
    def enroll(self,name,fee):
        if fee> 6500:
            return 'not enout free'
        else:
            id=len(self.students)+1
            student= Student(name,'c',id)
            self.students.append(student)
            return f'{name} is enrolled with id : {id}, extra mney {fee-6500}'
    def __repr__(self) -> str:
        print ('welcome to to ',self.name)
        print('___________our Teachre - - - - ')
        for teacher in self.teachers:
            print(teacher)
        print('------- our Stuendet --------')
        for student in self.students:
            print(student)
        return 'all done for now'

# alia =Student('Alia Torkari',9,1)
# ranbeer = Teacher('Rranbr',"algorithm",101)
# print(ranbeer)
# print(alia)
phitron =School('phitron')
phitron.enroll('alia',5200)
phitron.enroll('rain',8000)
phitron.enroll('vajia',8000)

phitron.add_teacher('sakib','a')
phitron.add_teacher('sakibafaafa','x')
phitron.add_teacher('sakibafaf','y')
# print(phitron)
# print(phitron.teachers)