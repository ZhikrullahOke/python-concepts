import sys
from studentList import StudentListClass


#saving student list in file--studentList.py-- to file
student = StudentListClass()

def main():

    list_to_file()


def list_to_file():

    try:
        no_student = int(input("Enter number of student invited: "))
        student.eligiblelist(no_student)

        with open("list-of-student.csv","w") as file:
            for item in student.get_studentlist():
                file.write("%s\n" %item)
    except ValueError:
        print("Invalid value entered\nPlease enter the correct value")
    except:
        error = sys.exc_info()[0]
        print("Error Detected: {}".format(error))


if __name__ == "__main__":
    main()