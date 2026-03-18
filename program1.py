class f:
 def fact(self,n):
  fact=1
  for i in range(1,n+1):
   fact=fact*i
  print(f"factorial of a given number {fact}")
n=int(input("Enter a number "))
c=f()
f.fact(n)
