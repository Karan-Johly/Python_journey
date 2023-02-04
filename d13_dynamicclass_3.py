class student:
    def stuinput(obj,name,rollno,fee):
        obj.name = name
        obj.rollno = rollno
        obj.fee = fee
    def stuoutput(obj):
        print("Student Name=",obj.name)
        print("Student Rollno=",obj.rollno)
        print("Student Fee=",obj.fee)

obj=student()
obj.stuinput("karan",33,4564)
obj.stuoutput()