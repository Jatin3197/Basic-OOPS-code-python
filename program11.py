class table:
 def tab(self,num):
  for i in range(1,11):
   m=num*i
   print(f"{num}*{i}={m}")
num=int(input("Enter a number :"))
t=table()
t.tab(num)
