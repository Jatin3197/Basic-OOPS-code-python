class interest:
  def __init__(self,p,n,r):
    self.p=p
    self.n=n
    self.r=r

  def si(self):
   return (self.p*self.n*self.r)/100

x=eval(input("Enter the value of p :"))  
y=eval(input("Enter the value of n :"))
z=eval(input("Enter the value of r :"))

i=interest(x,y,z)
print(f"simple interest is {i.si()}")


    