class circle:
  def __init__(self,r):
    self.r=r
  def area(self):
    return 3.14*self.r*r
  def peri(self):
   return 2*3.14*self.r
  
r=int(input("enter a number "))

c=circle(r)
print(f"Area of a circle is {c.area()}")
print(f"perimeter of a circle is {c.peri()}")
