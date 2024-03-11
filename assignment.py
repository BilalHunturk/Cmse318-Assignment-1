from datetime import datetime
import numpy as np



class Student:
    # we use __ to make attributes private 
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        # double _ means it is going to be private
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        self.__sex = sex
        self.__country_of_birth = country_of_birth
    
    # Getter Methods to get the properties of student
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
    
    # Set methods to set attributes of student
    def set_student_number(self,number):
        self.__student_number = number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    # the input date_of_birth should be in the format yyyy-mm-dd
    def set_date_of_birth(self,date_of_birth):
        # the function datetime.strptime(date_of_birth, '%Y-%m-%d').date() takes year month and day
        # after that operation, the input contains time of the day also, but we just need the date of the day. 
        # So it makes it date() object. which contains just date of the date of birth. So it doesnt contain time. 
        self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()

    def set_sex(self, sex):
        self.__sex = sex

    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth
    
    # 
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_number == other.get_student_number()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__student_number < other.get_student_number()

students = []

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
              "\n9 - Writes students to file"+
              "\n10 - Read students from file")
        inpt = int(input())
        # Switch case to step into part that user wants.
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

# finds the index of student and deletes from array with founded index and then saves to the file.
def removeStudentById():
    index = findStudentFromNumber()
    students.pop(index)
    writeStudentsToFile(student_list=students)


# input the student number, ask the field to modify, and get the new value from the user.
# Modify the record accordingly.
#    
def modifyStudentInf():
    # There is one condition here, maybe the array named 'students' can be empty. it should be checked

    # Takes input and finds the index number of the student.
    print("Enter the student number")
    student_number = input()
    student_index = getStudentIndexFromNumber(student_number)

    # if the index number is -1, it means the user entered wrong student number. And returns.
    if(student_index == -1):
        print("enter a valid student number")
        return
    
    # Asking which field to modify.
    print("\tWhich field do you want to modify ?"+
              "\n1 - First name"+
              "\n2 - Last surname"+
              "\n3 - Date of birth"+
              "\n4 - Gender"+ 
              "\n5 - Country of birth")
    inp = int(input())

    # takes input and calls the set methods to set that property 
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
    
    # Save array to file.
    writeStudentsToFile(students)

# takes the year of the birth
def showStudentsWithGivenBirth():
    print('Enter a birth year :')
    birth = int(input())

    # checks if array is empty, it goes and reads file and takes datas from file.
    if(len(students )== 0):
        readStudentFromFile()
    
    # checks if any of them has the same with the input 
    for student in students:
        if student.get_date_of_birth().year == birth:
            showStudentInf(student)


def findStudentFromNumber():
    # takes the number of student
    print('Enter a number of student : ')
    number = input()

    # use the function getStudentIndexFromNumber to get the index of the student.
    # if the result is -1 it means there is no student with that number.
    res = getStudentIndexFromNumber(number)
    if(res == -1):
        print('There is no student that has this student number.\nBe sure that you entered correct student number')
    
    # if res is differ then -1 it means it returned the index of student. 
    # we show student with function showStudentInf()
    showStudentInf(students[res])
    return res

# It takes student number
def getStudentIndexFromNumber(student_number):
    # if the array students is empty it reads the file and fulls the array  
    if( len(students) == 0):
        readStudentFromFile()
    student_index = -1
    
    #  it starts loop to find the expected student with student number.
    for index, student in enumerate(students):
        # if any match happens it puts this index to the student_index
        # and prints the index number of student.
        if student.get_student_number() == student_number:
            student_index = index
            print("Index of Student is "+str(student_index))
            break
        # finally it returns the index number of the student.
    return student_index

# this function created to read the file that contains students information.
def readStudentFromFile():
    # it opens the file to read with "r"
    f = open("./student_informations.txt", "r")
    # students informations stored with 
    # [student_number] - [student_first_name student_last_name] - [date_of_birth] - [sex] - [country_of_birth]\n
    # so we need to split first with '\n' 
    # then we can get the data line by line.
    # So each element of data should refer to student    
    inf = f.read().split('\n')
    # print(len(inf)) # output : 100
    for student in inf:
        # checks if there is empty element.  
        if(student == ''):
            continue
        # it splits each line with ' - ' because each line contains 4 ' - '  
        inf_student = student.split(' - ') # Example of output : ['1027', 'Maria da Silva', '2002', 'FEMALE', 'Brazil'] 
        
        # then we need to split firstname and lastname because they gotted together. 
        # we split them with character space ' ' and then put them into NS .
        # so we can get first name with NS[0] and last name with NS[-1]
        # we use -1 to get last name because student can have more then one name.
        NS = inf_student[1].split(' ') 

        # created a student with taken informations.
        newStudent = Student(inf_student[0],NS[0],NS[-1],inf_student[2],inf_student[3],inf_student[4])

        # append new student to the array. 
        students.append(newStudent)


    # this function is created to write students array to file. 
def writeStudentsToFile(student_list):

    print('The Length of students has written ')
    print(len(student_list))
    # we are sorting student_list to enhance any confusion in system.
    sorted_students = sorted(student_list)
    # open file to write 'w'
    f = open("student_informations.txt", "w")
    # writes sorted_students array with specific format to handle data correctly.
    for student in sorted_students:
        f.write(f"{student.get_student_number()} - {student.get_first_name()} {student.get_last_name()} - {student.get_date_of_birth()} - {student.get_sex()} - {student.get_country_of_birth()}\n")
    return sorted_students

    # this function is created to append new student to a file.
def appendStudentToFile(new_student):
    # to append this student we opened file with 'a'
    f = open("student_informations.txt", "a")
    # students = json.loads(f.read()) + self
    f.write(f"{new_student.get_student_number()} - {new_student.get_first_name()} {new_student.get_last_name()} - {new_student.get_date_of_birth().year}-{new_student.get_date_of_birth().month}-{new_student.get_date_of_birth().day} - {new_student.get_sex()} - {new_student.get_country_of_birth()}\n")
    f.close()

    # this function is created to show all students inf.
def listStudents():
    # it checks if the array is empty
    # if its empty it reads students from file with the function.
    if(len(students) == 0):
        readStudentFromFile()

    # It displays each students information with little for loop
    for student in students:
        showStudentInf(student)

    # This function is created to show students information including its age.
def showStudentInf(student):
    # it takes nows date and subtract with students birth date.
    # then converts it to days so we can divide by 365 to get age of student.
    # we use double slash to get rid of the remainder.
    age = (datetime.now().date() - student.get_date_of_birth()).days // 365
    print("\tNumber : "+student.get_student_number())
    print("\tName : " + student.get_first_name())
    print("\tSurname : " + student.get_last_name())
    print("\tDate of Birth : " + str(student.get_date_of_birth()))
    print("\tAge of the student : " + str(age))
    print("\tSex : " + student.get_sex())
    print("\tCountry Of Birth : " + student.get_country_of_birth()+"\n")


def addNewStudent():
    # checks if the array is empty.
    if(len(students) == 0):
        readStudentFromFile()

    # if the length of the array is more than 100 it can not add any more student to array or file.
    if(len(students) >= 100):
        print("\nThere are 100 student. You can not add any more student.\n")
        return 
    print("enter a students information")
        
    # Taking students information except number.
    print("Enter the first name of the student: ")
    student_first_name = input()

    print("Enter the last name of the student: ")
    student_last_name = input()
        
    print("Enter the date of birth of student : (it should be in the format yyyy mm dd)")
    date_of_birth = input()

    print("Enter the students gender: ")
    gender = input()

    print("Enter the country student birth: ")
    country_birth = input()

    # the id is given by the system
    # it takes last element's student_number and adds 1 then give it to the new student. 
    new_student = Student( str(int(students[-1].get_student_number())+ 1) , student_first_name, student_last_name, date_of_birth, gender, country_birth)
    # adds new student to the array.
    students.append(new_student)

    # append new student to the end of the file.
    # write new student to file 
    appendStudentToFile(new_student)

alg()