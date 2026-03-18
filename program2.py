class fa:
 def fab(self,n):
  a=0
  b=1
  for i in range(1,n+1):
   fab=a+b
   print(f"fabonacci seriies of a given number is {fab}")
   a=b
   b=fab
n=int(input("Enter a number "))
c=fa()
c.fab(n)