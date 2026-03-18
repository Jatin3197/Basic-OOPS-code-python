class list:
 def l(self,n):
  l=[]
  for i in range(0,5):
   n=int(input())
   l.append(n)
  print(l)
  print(sum(l))
  avg=sum(l)/len(l)
  print(f"Average ={avg}")

n=int(input("Enter a 5 numbers "))
li=list()
li.l(n)