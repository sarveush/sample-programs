fnum1=[]
c=0
fname=int(input("Enter a num:"))
for i in range(1,fname+1):
    fname1=int((input("Enter number:")))    
    fnum1.append(fname1)
d=int(input("enter a divisible number:"))
for j in range(fname1,11):
    if(j%d==0):
        c=c+1
print("no of divisible by",d,"is:",c)    
    
    


   