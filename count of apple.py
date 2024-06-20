string=input("enter a string:")
x=len(string)
for i in range(0,x):
    y=string.count(string[i])
    print(string[i],"-",y)
 
  