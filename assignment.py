import json
students = []

class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        # double _ means it is going to be private
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country_of_birth = country_of_birth
    
    def get_student_number(self):
        return self.__student_number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_sex(self):
        return self.__sex

    def get_country_of_birth(self):
        return self.__country_of_birth
    
    def write_contents_to_file(self):
        f = open("student_informations.txt", "a")
        # students = json.loads(f.read()) + self
        f.write(f"{self.get_student_number()}\n{self.get_first_name()}\n{self.get_last_name()}\n{self.get_date_of_birth()}\n{self.get_sex()}\n{self.get_country_of_birth()}\n")
        print(self)


def alg():
    while True:
        print("\tWhat do you want ?"+
              "\n1 - Add student"+
              "\n2 - Find student from number"+
              "\n3 - Show all students"+
              "\n4 - Show all students who were born in a given year\n5 - Modify a student record:"+
              "\n6 - Delete student with specific student number"+
              "\n7 - Show students"+
              "\n8 - Quit from program"+
              "\n9 - Write all students to file"+
              "\n10 - Read students from file")
        inpt = int(input())
        match inpt:
            case 1:
                addNewStudent()
                continue
            case 2:
                continue
            case 3:
                listStudents()
                continue
            case 4:
                continue
            case 5:
                continue
            case 6:
                continue
            case 7:
                continue
            case 8:
                quit()
            case 9:
                writeStudentsToFile()
                continue
            case 10:
                readStudentFromFile()
            case _:
                print("Please enter expected value.")
                continue
                

def readStudentFromFile():
    f = open("./student_information.txt", "r")
    inf = f.read().split('\n')
    rng = ((len(inf)) // 6)
    print(rng)
    for x in range(0,rng):
        newStudent = Student(inf[6*x],inf[6*x+1],inf[6*x+2],inf[6*x+3],inf[6*x+4],inf[6*x+5])
        students.append(newStudent)
        print(inf[6*x]+inf[6*x+1]+inf[6*x+2]+inf[6*x+3]+inf[6*x+4]+inf[6*x+5])

def writeStudentsToFile():
    for student in students:
        student.write_contents_to_file()

def listStudents():
    
    if(len(students) == 0):
        readStudentFromFile()
    for student in students:
        print(f"\t\tStudent ")
        print("\tNumber : "+student.get_student_number())
        print("\tName : " + student.get_first_name())
        print("\tSurname : " + student.get_last_name())
        print("\tDate of Birth : " + student.get_date_of_birth())
        print("\tSex : " + student.get_sex())
        print("\tCountry Of Birth : " + student.get_country_of_birth()+"\n")



def addNewStudent():
    print("enter a students information")
    print("Enter student number: ")
    student_number = input()
        
    # there is a situation that one student can have more than 1 name, for example second name, third name, ...
    # this situation should be handled
    print("Enter the first name of the student: ")
    student_name = input()

    print("Enter the last name of the student: ")
    student_last_name = input()
        
    print("Enter the date of birth of student : ")
    date_of_birth = input()

    print("Enter the students gender: ")
    gender = input()

    print("Enter the country student birth: ")
    country_birth = input()

    students.append( Student( student_number, student_name, student_last_name, date_of_birth, gender, country_birth))
alg()