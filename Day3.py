class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=[]
    def displayname(self):
        print(f"Am {self.name} and am {self.age}years old")
    def addgrades(self,grade):
        self.grades.append(grade)
    def displaygrades(self):
    
     average_grades=sum(self.grades)/len(self.grades)
     print(average_grades)
c1=Student("Gam",23,100) 
c1.displayname()
c1.addgrades(90) 
c1.addgrades(100)  
c1.displaygrades()

class Form1student(Student):
    def average_grades(self):
        average_grades=sum(self.grades)
        print(average_grades)
    def displayname(self):
        print(f"Am {self.name} ")

    
c2=Form1student("blessing",23,65)
c2.addgrades(56)
c2.addgrades(70)
c2.addgrades(46)
c2.average_grades()  
c2.displayname()     

  
























