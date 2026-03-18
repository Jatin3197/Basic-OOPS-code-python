class s:
 def sum_digit(self,n):
  sum=0
  while n>0:
   r=n%10
   n=n//10
   sum=sum+r
  print(f"sum of a digit is {sum}")
n=int(input("Enter a number "))
c=s()
c.sum_digit(n)



