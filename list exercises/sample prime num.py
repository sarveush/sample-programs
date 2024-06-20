c=0
num=int(input("enter a number:"))
for i in range(2,num):
   if(num%i==0):
      c=c+1
if(c>0):
   print("not a prime number")
else:
   print("prime number")