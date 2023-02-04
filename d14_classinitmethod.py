class student:
    def __init__(self,name,rollno):
        self.name="Manoj"
        self.rollno=1
    def output(self):
        print("Student Name: ",self.name)
        print("Student Rollno: ",self.rollno)
    def __del__(self):
        print("Destructor Calling...");

obj1=student()
obj2=student()
obj1.output()
obj2.output()
