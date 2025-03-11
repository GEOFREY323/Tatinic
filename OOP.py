class Human:
  def __init__(self,name,age,height,gender):
    self.name= name
    self.age=age
    self.height=height
    self.gender=gender
  def DisplayName(self):
     print(f"my name is {self.name}, I am {self.age}years old my height is {self.height} and my gender is {self.gender}")

c1=Human('john',21,1.8,'M')
c2=Human('Gam',20,1.7,'M')
c3=Human('peter',50,1.6,'M')
c1.DisplayName()
c2.DisplayName()
c3.DisplayName()
