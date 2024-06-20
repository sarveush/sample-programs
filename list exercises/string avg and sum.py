
c1=0
y=0
fname=input("enter a string:")
x=len(fname)
# z=int(fname)
for i in range(0,x):
    if(fname[i].isdigit()):
         c1=c1+1
         y=y+int(fname[i])
print("sum of numbers is:",y)
print("average of numbers:",y/c1)

    

