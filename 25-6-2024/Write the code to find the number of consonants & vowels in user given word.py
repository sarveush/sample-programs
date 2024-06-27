fname=input("enter a string:")
x=len(fname)
v=0
c=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,x):
    if(fname[i] in vowels):
        v=v+1
    else:
        c=c+1
print("no of vowels:",v)
print("no of constants:",c)            
         