class student:
    def stuinput(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def stuoutput(self):
        print("Student Name: ",self.name)
        print("Student Rollno: ",self.rollno)
obj=student()
obj.stuinput("Manoj",33)
obj.stuoutput()