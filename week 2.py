try:
  
  class Human:
      def __init__(self,name,age,height,gender):
        self.name= name
        self.age=age
        self.height=height
        self.gender=gender


  c1=Human('john','50yrs','1.8m','M')
  print(f"my name is {c1.name}, I am {c1.age} old my height is {c1.height} and my gender is {c1.gender}")
  print(5/0)

except ZeroDivisionError:
  pass