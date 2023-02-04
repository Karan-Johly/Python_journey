                        # Parameterized Method
class student:
    def stuinput(name,rollno,fee):
        student.name = name
        student.rollno = rollno
        student.fee = fee
    def stuoutput():
        print("Student Name=",student.name)
        print("Student Rollno=",student.rollno)
        print("Student Fee=",student.fee)
obj=student
obj.stuinput("Gagan",1,12.12)
obj.stuoutput()
