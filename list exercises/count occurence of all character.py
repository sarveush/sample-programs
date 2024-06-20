c=0
c1=0
fname=input("enter a string:")
x=len(fname)
list=[]
y=len(list)
for i in range(0,x):
    if(fname[i].isalpha()):
        list.append(fname[i])
for j in range(0,y):
    if(fname[j]%list==0):
        c=c+1
    elif(fname[j]>0):
        c1=c1+1
print("the count occurence are:",c1)

