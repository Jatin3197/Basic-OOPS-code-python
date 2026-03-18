class re:
 def re_digit(self,n):
  rev=0
  while n>0:
   r=n%10
   n=n//10
   rev=rev*10+r
  print(f"reverse of a digit is {rev}")
n=int(input("Enter a number "))
c=re()
c.re_digit(n)


