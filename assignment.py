from datetime import datetime

students = []

class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        # double _ means it is going to be private
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        self.__sex = sex
        self.__country_of_birth = country_of_birth
    
    # Get Methods
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
    
    # Set methods
    def set_student_number(self,number):
        self.__student_number = number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self,date_of_birth):
        self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()

    def set_sex(self, sex):
        self.__sex = sex

    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_number == other.get_student_number()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_number < other.get_student_number()
    
    def write_contents_to_file(self):
        f = open("student_informations.txt", "a")
        f.write(f"{self.get_student_number()} - {self.get_first_name()} {self.get_last_name()} - {self.get_date_of_birth()} - {self.get_sex()} - {self.get_country_of_birth()}\n")


def alg():
    while True:
        print("\tWhat do you want ?"+
              "\n1 - Add student"+
              "\n2 - Find student from number"+
              "\n3 - Show all students"+
              "\n4 - Show all students who were born in a given year"+
              "\n5 - Modify a student record"+
              "\n6 - Delete student with specific student number"+
              "\n7 - #"+
              "\n8 - Quit from program"+
              "\n9 - Write all students to file"+
              "\n10 - Read students from file")
        inpt = int(input())
        match inpt:
            case 1:
                addNewStudent()
                continue
            case 2:
                findStudentFromNumber()
                continue
            case 3:
                listStudents()
                continue
            case 4:
                showStudentsWithGivenBirth()
                continue
            case 5:
                modifyStudentInf()
                continue
            case 6:
                removeStudentById()
                continue
            case 7:
                continue
            case 8:
                quit()
            case 9:
                writeStudentsToFile(student_list = students)
                continue
            case 10:
                readStudentFromFile()
            case _:
                print("Please enter expected value.")
                continue

def removeStudentById():
    index = findStudentFromNumber()
    students.pop(index)
    writeStudentsToFile(student_list=students)
    # findStudentFromNumber()

# not completed
# input the student number, ask the field to modify, and get the new value from the user.
# Modify the record accordingly.
def modifyStudentInf():
    # There is one condition here, maybe the array named 'students' can be empty. it should be checked
    print("Enter the student number")
    student_number = input()
    student_index = getStudentIndexFromNumber(student_number)
    if(student_index == -1):
        print("enter a valid student number")
        return
    print("\tWhich field do you want to modify ?"+
              "\n1 - First name"+
              "\n2 - Last surname"+
              "\n3 - Date of birth"+
              "\n4 - Gender"+ 
              "\n5 - Country of birth")
    inp = int(input())

    match inp:
        case 1:
            print("Enter new First Name :")
            new_first_name = input()
            students[student_index].set_first_name(new_first_name)
        case 2:
            print("Enter new Last Name :")
            new_Last_Name = input()
            students[student_index].set_last_name(new_Last_Name)
        case 3:
            print("Enter new Date Of Birth : (with specified format yyyy-mm-dd )")
            new_date_of_birth = input()
            students[student_index].set_date_of_birth(new_date_of_birth)
        case 4:
            print("Enter new Sex :")
            new_gender = input()
            students[student_index].set_sex(new_gender)
        case 5:
            print("Enter new Country Of Birth :")
            new_country_of_birth = input()
            students[student_index].set_country_of_birth(new_country_of_birth)
        case _:
            print("Please enter valid student number")
            return
    
    writeStudentsToFile(students)

def showStudentsWithGivenBirth():
    print('Enter a birth :')
    birth = int(input())

    if(len(students )== 0):
        readStudentFromFile()
    
    for student in students:
        if student.get_date_of_birth().year == birth:
            showStudentInf(student)

def findStudentFromNumber():
    print('Enter a number of student : ')
    number = input()
    res = getStudentIndexFromNumber(number)
    if(res == -1):
        print('There is no student that has this student number.\nBe sure that you entered correct student number')
    showStudentInf(students[res])
    return res

def getStudentIndexFromNumber(student_number):
    if( len(students) == 0):
        readStudentFromFile()
    student_index = -1
    for index, student in enumerate(students):
        if student.get_student_number() == student_number:
            student_index = index
            # showStudentInf(student)
            print("Index of Student is "+str(student_index))
            break
    return student_index

def readStudentFromFile():
    f = open("./student_informations.txt", "r")
    inf = f.read().split('\n')
    # print(len(inf)) # output : 100
    for student in inf:
        if(student == ''):
            continue
        inf_student = student.split(' - ') # Example of output : ['1027', 'Maria da Silva', '2002', 'FEMALE', 'Brazil'] 
        NS = inf_student[1].split(' ') 
        newStudent = Student(inf_student[0],NS[0],NS[-1],inf_student[2],inf_student[3],inf_student[4])
        students.append(newStudent)
        
        # newStudent = Student(inf[6*x],inf[6*x+1],inf[6*x+2],inf[6*x+3],inf[6*x+4],inf[6*x+5])
        # students.append(newStudent)
        #print(inf[6*x]+inf[6*x+1]+inf[6*x+2]+inf[6*x+3]+inf[6*x+4]+inf[6*x+5])
    # print(students)
    
def writeStudentsToFile(student_list):
    print('The Length of students has written ')
    print(len(student_list))
    sorted_students = sorted(student_list)
    f = open("student_informations.txt", "w")
    for student in sorted_students:
        f.write(f"{student.get_student_number()} - {student.get_first_name()} {student.get_last_name()} - {student.get_date_of_birth()} - {student.get_sex()} - {student.get_country_of_birth()}\n")
    return sorted_students

def appendStudentToFile(new_student):
    f = open("student_informations.txt", "a")
    # students = json.loads(f.read()) + self
    f.write(f"{new_student.get_student_number()} - {new_student.get_first_name()} {new_student.get_last_name()} - {new_student.get_date_of_birth().year}-{new_student.get_date_of_birth().month}-{new_student.get_date_of_birth().day} - {new_student.get_sex()} - {new_student.get_country_of_birth()}\n")
    f.close()

def listStudents():
    if(len(students) == 0):
        readStudentFromFile()

    for student in students:
        showStudentInf(student)
    print(len(students))

def showStudentInf(student):
    age = (datetime.now().date() - student.get_date_of_birth()).days // 365
    print("\tNumber : "+student.get_student_number())
    print("\tName : " + student.get_first_name())
    print("\tSurname : " + student.get_last_name())
    print("\tDate of Birth : " + str(student.get_date_of_birth()))
    print("\tAge of the student : " + str(age))
    print("\tSex : " + student.get_sex())
    print("\tCountry Of Birth : " + student.get_country_of_birth()+"\n")

def addNewStudent():

    if(len(students) == 0):
        readStudentFromFile()

    if(len(students) >= 100):
        print("\nThere are 100 student. You can not add any more student.\n")
        return 
    print("enter a students information")
        
    # there is a situation that one student can have more than 1 name, for example second name, third name, ...
    # this situation should be handled
    print("Enter the first name of the student: ")
    student_name = input()

    print("Enter the last name of the student: ")
    student_last_name = input()
        
    print("Enter the date of birth of student : (it should be in the format yyyy mm dd)")
    date_of_birth = input()

    print("Enter the students gender: ")
    gender = input()

    print("Enter the country student birth: ")
    country_birth = input()

    new_student = Student( str(int(students[-1].get_student_number())+ 1) , student_name, student_last_name, date_of_birth, gender, country_birth)
    students.append(new_student)

    # write new student to file 
    appendStudentToFile(new_student)

alg()