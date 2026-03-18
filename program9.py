class sphere:
  def __init__(self,l,b,h):
     self.l=l
     self.b=b
     self.h=h
  def volume(self):
     return self.l*self.b*self.h
  def sa(self):
     return 2*(self.l*self.b+self.b*self.h+self.h*self.l)

x=eval(input("Enter the value of l :"))
y=eval(input("Enter the value of b :"))
z=eval(input("Enter the value of h :"))

s=sphere(x,y,z)
print(f"volume of a sphere is {s.volume()}")
print(f"surface area of a sphere is {s.sa()}")

