class ar:
 def arm(self,n):
  s=0
  t=n
  while n>0:
   r=n%10
   n=n//10
   s=s+r*r*r;
  if t==s:
    print(f"{t} is  a Armstrong number")
  else:
    print(f"{t} is not a Armstrong number")
  
n=int(input("Enter a number "))
c=ar()
c.arm(n)

  