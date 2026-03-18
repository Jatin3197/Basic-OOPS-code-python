class list:
 def l(self,n):
  l=[]
  for i in range(0,5):
   n=int(input())
   l.append(n)
  print(l)
  n=int(input("Enter a number to find  "))
  if n in li:
   print(f"{n} is exists")
  else:
   print(f"{n} is not exists")

n=int(input("Enter a five numbers "))
li=list()
li.l(n)
  
   