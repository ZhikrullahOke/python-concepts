import random
import sys
import os
import datetime
from Person import *

class StudentList:
    try:
        __studentList = []
        __no = 0
        __name = None
        __count = 1


        def eligiblelist(self,no):
            self.__no = no

            while (len(self.__studentList) < self.__no):
                self.__name = input("Enter student name {}: ".format(self.__count))
                if(self.__name not in self.__studentList):
                    self.__studentList.append(self.__name)
                elif(self.__no == 0):
                    print("No Student invited")
                else:
                    print("::: Name already exist in the list please add another name. \n See list below :::")
                    print(self.__studentList)
                    continue
                self.__count += 1



            print("\n:::List of Invited student:::")
            for x in self.__studentList:
                print(x)



    except:
        error = sys.exc_info()[0]
        print("Error: {}".format(error))

#creating new object called student
student = StudentList()

try:
    no_student = int(input("Enter number of student invited: "))
    student.eligiblelist(no_student)
except ValueError:
    print("Invalid value entered\nPlease enter the correct value")
except:
    error = sys.exc_info()[0]
    print("Error Detected: {}".format(error))