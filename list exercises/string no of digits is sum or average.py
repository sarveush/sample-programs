c=0
y=0
fname=input("Enter a string:")
x=len(fname)
for i in range(0,x):
    if(fname[i].isdigit()):
        c=c+1
        y=y+int(fname[i])
print("The sum is :",y)    
print("The average is:",y/c)    
