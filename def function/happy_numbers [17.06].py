def happy_number(n):
    x=set()
    while n!=1 and n not in x:
        x.add(n)
        n=sum(int(char) **2 for char in str(n))
    return n==1
number=int(input("Enter a number:"))
if happy_number(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")        