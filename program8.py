class cal: 
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mult(self):
    return self.a*self.b
  def div(self):
    return self.a//self.b

x=int(input("Enter a value of a "))
y=int(input("Enter a value of b "))

c=cal(x,y)
print(f"addition={c.add()}")
print(f"substraction={c.sub()}")
print(f"multiplication={c.mult()}")
print(f"division={c.div()}")