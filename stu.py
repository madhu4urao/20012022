class Student:
    def __init__(self,name,rno,pno):
        self.name=name
        self.roolno=rno
        self.phonenumber=pno
    def display(self):
        print(self.name,self.roolno,self.phonenumber)
std=Student("vishal",30,1233667788)
std.display()



