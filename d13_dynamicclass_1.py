                # Dynamic Class
class student:
    def stuinput(student,name,rollno,fee):
        student.name = name
        student.rollno = rollno
        student.fee = fee
    def stuoutput(student):
        print("Student Name=",student.name)
        print("Student Rollno=",student.rollno)
        print("Student Fee=",student.fee)

obj=student()
obj.stuinput("karan",33,4564)
obj.stuoutput()
