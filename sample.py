fnum=int(input("enter the num:"))
if(fnum>50):
    for i in range(2,501,2):
        print(i,"range more than 500")
elif(fnum<50):
     for j in range(1,501,2):
         print(j,"range less than 500")    
else:
    print(fnum)         