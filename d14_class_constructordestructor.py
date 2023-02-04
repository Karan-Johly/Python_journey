class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def output(self):
        print("Student Name: ",self.name)
        print("Student Rollno: ",self.rollno)
    def __del__(self):
        print("Destructor Calling...");

obj1=student("Harry",1)
obj2=student("Mohit",2)
obj1.output()
obj2.output()
