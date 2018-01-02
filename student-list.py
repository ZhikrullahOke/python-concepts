import random
import sys
import os
import datetime


class StudentList:


    try:
        __studentList = []
        __no = 0
        __name = None
        __count = 1
        finename = None

        def __init__(self):
            pass

        def eligiblelist(self,no):
            self.__no = no

            while (len(self.__studentList) < self.__no):
                self.__name = input("Enter student name {}: ".format(self.__count))
                if self.__name in self.__studentList:
                    print("Name already exist. Please add another name not in the list \n!!!!See list Below!!!!")
                    print(self.__studentList)
                    continue
                elif (self.__no == 0):
                    print("No Student invited")
                else:
                    self.__studentList.append(self.__name)

                self.__count += 1

            print("\n:::List of Invited student:::")
            for x in self.__studentList:
                print(x)

        def savelisttofile(self):
            with open("student.csv","w") as file:
                for x in self.__studentList:
                    file.write(x)

        def readfile(self,filename):
            with open(filename,"r") as file:
                for x in file:
                    print(x)
    except:
        error = sys.exc_info()[0]
        print("Error: {}".format(error))

#creating new object called student
student = StudentList()

try:
    num_student = int(input("Enter number of student invited: "))
    student.eligiblelist(num_student)
    student.savelisttofile()
    student.readfile('student.csv')

except ValueError:
    print("Invalid value entered\nPlease enter the correct value")

except:
    error = sys.exc_info()[0]
    print("Error Detected: {}".format(error))