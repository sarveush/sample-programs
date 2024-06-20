c=0
flist=['a','p','p','l','e']
fname=input("enter a string:")
x=len(fname)
for i in range(0,x):
    if(fname in flist):
        c=c+1
if(c>1):
    print("the repeated values are:",c)
else:
    print("no values are repeated:")           

         