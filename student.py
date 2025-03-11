class Student:
    def __init__(self,name,matricule,department):
       self.name=name
       self.matricule=matricule
       self.department=department
       self.courses=[]
    def displayName(self):
        print(f"my name is {self.name},matricul={self.matricule},from the department of {self.department}")
        
    def addCourses(self,courses):
        self.courses.append(courses)
    def displayCourses(self):
         print(f"i offer {self.courses}")
    

    

c1=Student("gam","uba24ph066","CEN")
c1.displayName()
c1.addCourses("maths")
c1.addCourses("chem")
c1.addCourses("physics")
c1.addCourses("computer")
c1.addCourses("bio")
c1.courses.pop(1)
c1.displayCourses()






      
       
       

