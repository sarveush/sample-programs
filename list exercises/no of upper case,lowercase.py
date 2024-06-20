c=0
c1=0
c2=0
c3=0
fname=(input("enter a string:" ))
x=len(fname)
for i in range(0,x):
    if(fname[i].isupper()):
        c=c+1
    elif(fname[i].islower()):
        c1=c1+1
    elif(fname[i].isdigit()):
        c2=c2+1
    elif(fname[i].isidentifier()):
        c3=c3+1    
print("the no of upper case is:",c)
print("the lower case is:",c1) 
print("the no of digits is:",c2 )
print("the number of special character is:",c3)
    



       
