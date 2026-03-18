class lb:
 def __init__(self,l,b):
   self.l=l
   self.b=b
 def area(self):
   return self.l*self.b
 
 def peri(self):
   return 2*self.l+2*self.b

x=int(input("Enter a length "))
y=int(input("Enter a breadth "))

c=lb(x,y)
print("area of a rectangle ",c.area())
print("perimeter of  a rectangle",c.peri())

