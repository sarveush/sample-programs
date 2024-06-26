import math
list1=[1,3,6,6,4,6]
# x=sorted(list1)
x=sorted(list(set(list1)))
print(x)
y=len(x)
# print(y)
if(y%2==0):
    a=int(y/2)
    b=int(a-1)
    # print(int(a))
    # print(int(b))
    print(x[b])
    print(x[a])
else:
    c= math.floor(y/2)
    print(x[c])
